import os
import sys
import sqlite3
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ukvi_hr_system.database import get_connection, COMPANY_NAME, SPONSOR_LICENCE_NUMBER, AUTHORISING_OFFICER_NAME

APPENDIX_D_MANDATORY_CATEGORIES = [
    {"category": "PASSPORT_BIO", "label": "Passport / Travel Document Bio Page", "ukvi_ref": "Appendix D, Item 1"},
    {"category": "BRP_EVISA_SHARE_CODE", "label": "eVisa / Online Right to Work Share Code Record", "ukvi_ref": "Appendix D, Item 1 & 2"},
    {"category": "RTW_VERIFICATION_CHECK", "label": "Statutory Right to Work Online Check Record (Dated)", "ukvi_ref": "Appendix D, Item 2"},
    {"category": "CONTRACT_OF_EMPLOYMENT", "label": "Signed Contract of Employment / Particulars", "ukvi_ref": "Appendix D, Item 3"},
    {"category": "JOB_DESCRIPTION", "label": "Detailed Job Description Matching SOC Code", "ukvi_ref": "Appendix D, Item 3"},
    {"category": "NI_PROOF", "label": "National Insurance Evidence (HMRC / P45 / P60)", "ukvi_ref": "Appendix D, Item 4"},
    {"category": "QUALIFICATIONS_AND_REGISTRATION", "label": "Professional Qualifications / Degree / Certifications", "ukvi_ref": "Appendix D, Item 5"},
    {"category": "UK_ADDRESS_PROOF", "label": "Proof of Current UK Residential Address (<3 months old)", "ukvi_ref": "Appendix D, Item 7"},
    {"category": "ABSENCE_RECORD", "label": "Accurate Daily Time, Attendance & Sickness Tracker", "ukvi_ref": "Appendix D, Item 8"},
    {"category": "PAYROLL_RECORDS", "label": "Itemised Statutory Payslips Matching CoS Rate", "ukvi_ref": "Appendix D, Item 9"}
]

# Standard Occupational Classification (SOC 2020) Going Rates for E-Commerce Enterprise
SOC_CODE_BENCHMARKS = {
    "2136": {"title": "Programmers and software development professionals", "min_salary": 49400.0, "hourly_rate": 25.33},
    "2424": {"title": "Business and financial project management professionals", "min_salary": 44700.0, "hourly_rate": 22.92},
    "3545": {"title": "Sales accounts and business development managers", "min_salary": 38700.0, "hourly_rate": 19.85},
    "1136": {"title": "Information technology and telecommunications directors", "min_salary": 58900.0, "hourly_rate": 30.21},
    "3562": {"title": "Human resources and industrial relations officers", "min_salary": 38700.0, "hourly_rate": 19.85},
    "2431": {"title": "Advertising and marketing communications professionals", "min_salary": 38700.0, "hourly_rate": 19.85}
}

def audit_employee_compliance(emp_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    emp = cursor.fetchone()
    if not emp:
        conn.close()
        return None

    emp_dict = dict(emp)
    is_sponsored = emp_dict['immigration_status'] in ['SKILLED_WORKER', 'HEALTH_AND_CARE', 'STUDENT_VISA']

    # 1. Fetch Appendix D Docs
    cursor.execute("SELECT * FROM appendix_d_documents WHERE employee_id = ?", (emp_id,))
    docs = [dict(row) for row in cursor.fetchall()]
    uploaded_categories = {d['category']: d for d in docs}

    missing_docs = []
    expired_docs = []
    verified_docs_count = 0
    now_date = datetime.now().date()

    for item in APPENDIX_D_MANDATORY_CATEGORIES:
        cat_key = item['category']
        # If settled or British citizen, online share code isn't strictly mandatory
        if not is_sponsored and cat_key in ['BRP_EVISA_SHARE_CODE', 'RTW_VERIFICATION_CHECK']:
            continue

        if cat_key not in uploaded_categories:
            missing_docs.append({
                "category": cat_key,
                "label": item['label'],
                "ukvi_ref": item['ukvi_ref'],
                "severity": "CRITICAL" if cat_key in ['PASSPORT_BIO', 'RTW_VERIFICATION_CHECK', 'CONTRACT_OF_EMPLOYMENT'] else "HIGH"
            })
        else:
            doc = uploaded_categories[cat_key]
            if doc['status'] == 'VERIFIED':
                verified_docs_count += 1
                if doc.get('expiry_date'):
                    try:
                        exp = datetime.strptime(doc['expiry_date'], "%Y-%m-%d").date()
                        if exp <= now_date:
                            expired_docs.append({"category": cat_key, "label": item['label'], "expiry_date": doc['expiry_date']})
                    except Exception:
                        pass
            elif doc['status'] == 'EXPIRED':
                expired_docs.append({"category": cat_key, "label": item['label'], "expiry_date": doc.get('expiry_date', 'Unknown')})
            elif doc['status'] == 'PENDING_REVIEW':
                missing_docs.append({
                    "category": cat_key,
                    "label": f"{item['label']} (Pending Compliance Officer Sign-off)",
                    "ukvi_ref": item['ukvi_ref'],
                    "severity": "MEDIUM"
                })

    # 2. Check Visa / RTW Expiry
    visa_alert = None
    days_to_visa_expiry = None
    if is_sponsored and emp_dict.get('visa_expiry_date'):
        try:
            visa_exp = datetime.strptime(emp_dict['visa_expiry_date'], "%Y-%m-%d").date()
            delta = (visa_exp - now_date).days
            days_to_visa_expiry = delta
            if delta < 0:
                visa_alert = {"level": "CRITICAL", "message": f"IMMIGRATION BREACH: Skilled Worker Visa expired {abs(delta)} days ago! Immediate Home Office reporting and curtailment risk."}
            elif delta <= 30:
                visa_alert = {"level": "CRITICAL", "message": f"URGENT: Visa expires in {delta} days! Follow-up Right to Work check or CoS renewal required."}
            elif delta <= 90:
                visa_alert = {"level": "WARNING", "message": f"Visa expires in {delta} days. Initiate extension or transition consultation with Authorising Officer."}
        except Exception:
            pass

    # 3. Check Consecutive Unauthorized Absence (SMS 10-Day Rule)
    cursor.execute("SELECT * FROM consecutive_absence_tracker WHERE employee_id = ?", (emp_id,))
    abs_track = cursor.fetchone()
    consecutive_abs_days = abs_track['consecutive_unauthorized_days'] if abs_track else 0
    absence_alert = None
    if consecutive_abs_days >= 10:
        absence_alert = {
            "level": "CRITICAL_SMS_TRIGGER",
            "days": consecutive_abs_days,
            "message": f"STATUTORY BREACH: {consecutive_abs_days} consecutive unnotified working days. MANDATORY SMS report to UKVI within 10 working days!"
        }
    elif consecutive_abs_days >= 7:
        absence_alert = {
            "level": "WARNING",
            "days": consecutive_abs_days,
            "message": f"High Risk: {consecutive_abs_days} unnotified days absent. GP Medical Fit Note legally required by Day 8; SMS trigger at Day 10."
        }
    elif consecutive_abs_days >= 3:
        absence_alert = {
            "level": "NOTICE",
            "days": consecutive_abs_days,
            "message": f"Worker absent without notification for {consecutive_abs_days} days. Stage 1 telephone contact protocol required."
        }

    # 4. Check Salary vs SOC Benchmark & CoS Declared Rate
    soc_code = emp_dict.get('soc_code', '').split(' ')[0]
    soc_rule = SOC_CODE_BENCHMARKS.get(soc_code)
    salary_alert = None
    if is_sponsored and soc_rule:
        required_min = soc_rule['min_salary']
        actual_salary = float(emp_dict.get('annual_gross_salary', 0.0))
        if actual_salary < required_min:
            salary_alert = {
                "level": "CRITICAL",
                "message": f"Remuneration shortfall: Paid £{actual_salary:,.2f}/yr, minimum SOC going rate is £{required_min:,.2f}/yr. Violation of UKVI Sponsorship duties!"
            }

    # 5. Check Supplementary Employment (20 Hours Rule)
    supp_hours = float(emp_dict.get('supplementary_hours_declared', 0.0))
    supp_alert = None
    if is_sponsored and supp_hours > 20.0:
        supp_alert = {
            "level": "CRITICAL",
            "message": f"Supplementary employment violation: Worker declared {supp_hours} hrs/week secondary work. Home Office cap is strictly 20 hrs/week!"
        }

    # 6. Contact Details Validation
    missing_info = []
    if not emp_dict.get('uk_residential_address'):
        missing_info.append("UK Residential Address Missing (Appendix D violation)")
    if not emp_dict.get('phone_number'):
        missing_info.append("Mobile Phone Number Missing")
    if not emp_dict.get('national_insurance_number'):
        missing_info.append("National Insurance Number Missing")
    if not emp_dict.get('emergency_contact_phone'):
        missing_info.append("Emergency Contact Missing")

    # Compute Compliance Health Score (0 - 100%)
    deductions = (len(missing_docs) * 8) + (len(expired_docs) * 12) + (len(missing_info) * 3)
    if visa_alert and visa_alert['level'] == 'CRITICAL':
        deductions += 30
    if absence_alert and absence_alert['level'] == 'CRITICAL_SMS_TRIGGER':
        deductions += 35
    if salary_alert:
        deductions += 25
    if supp_alert:
        deductions += 20

    health_score = max(5, min(100, 100 - deductions))

    status_badge = "COMPLIANT"
    if health_score < 60 or (absence_alert and absence_alert['level'] == 'CRITICAL_SMS_TRIGGER'):
        status_badge = "CRITICAL_ACTION_REQUIRED"
    elif health_score < 85 or len(missing_docs) > 0 or len(missing_info) > 0 or (visa_alert and visa_alert['level'] == 'WARNING'):
        status_badge = "ATTENTION_NEEDED"

    conn.close()

    return {
        "employee_id": emp_dict['id'],
        "employee_code": emp_dict['employee_id'],
        "name": emp_dict['full_name'],
        "immigration_status": emp_dict['immigration_status'],
        "job_title": emp_dict['job_title'],
        "soc_code": emp_dict['soc_code'],
        "annual_gross_salary": emp_dict['annual_gross_salary'],
        "health_score": health_score,
        "status_badge": status_badge,
        "is_sponsored": is_sponsored,
        "days_to_visa_expiry": days_to_visa_expiry,
        "visa_alert": visa_alert,
        "absence_alert": absence_alert,
        "salary_alert": salary_alert,
        "supp_alert": supp_alert,
        "missing_docs": missing_docs,
        "expired_docs": expired_docs,
        "missing_info": missing_info,
        "documents": docs,
        "consecutive_unauthorized_days": consecutive_abs_days
    }

def audit_organization_overview():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, full_name, immigration_status, role FROM employees ORDER BY id ASC")
    employees = cursor.fetchall()

    total_staff = len(employees)
    sponsored_staff = 0
    total_score = 0
    critical_cases = 0
    attention_cases = 0
    compliant_cases = 0
    all_audits = []

    for row in employees:
        audit = audit_employee_compliance(row['id'])
        if audit:
            all_audits.append(audit)
            if audit['is_sponsored']:
                sponsored_staff += 1
            total_score += audit['health_score']
            if audit['status_badge'] == "CRITICAL_ACTION_REQUIRED":
                critical_cases += 1
            elif audit['status_badge'] == "ATTENTION_NEEDED":
                attention_cases += 1
            else:
                compliant_cases += 1

    overall_health = round(total_score / max(1, total_staff), 1)

    # Active SMS Triggers
    cursor.execute("""
        SELECT t.*, e.full_name, e.employee_id as emp_code 
        FROM sms_reporting_triggers t
        JOIN employees e ON t.employee_id = e.id
        WHERE t.status = 'PENDING_ACTION'
        ORDER BY t.home_office_deadline ASC
    """)
    pending_sms = [dict(r) for r in cursor.fetchall()]

    # Leave requests pending
    cursor.execute("""
        SELECT l.*, e.full_name, e.employee_id as emp_code
        FROM leave_requests l
        JOIN employees e ON l.employee_id = e.id
        WHERE l.status = 'PENDING'
    """)
    pending_leaves = [dict(r) for r in cursor.fetchall()]

    conn.close()

    return {
        "company_name": COMPANY_NAME,
        "sponsor_licence_number": SPONSOR_LICENCE_NUMBER,
        "authorising_officer": AUTHORISING_OFFICER_NAME,
        "overall_health_score": overall_health,
        "total_staff": total_staff,
        "sponsored_staff": sponsored_staff,
        "compliant_count": compliant_cases,
        "attention_count": attention_cases,
        "critical_count": critical_cases,
        "pending_sms_count": len(pending_sms),
        "pending_sms_triggers": pending_sms,
        "pending_leaves": pending_leaves,
        "employee_audits": all_audits
    }

def generate_sms_text_template(trigger_type: str, employee_data: dict, details: str = ""):
    """Generates the official SMS draft for Ether Worldwide Ltd ready for UKVI submission"""
    now_str = datetime.now().strftime("%d/%m/%Y")
    worker_name = employee_data.get('full_name', 'N/A')
    cos_num = employee_data.get('cos_number', 'N/A')
    soc_code = employee_data.get('soc_code', 'N/A')
    job_title = employee_data.get('job_title', 'N/A')

    if trigger_type == "UNAUTHORIZED_ABSENCE_10_DAYS":
        return f"""[UKVI SPONSORSHIP MANAGEMENT SYSTEM (SMS) NOTIFICATION]
Sponsor Organisation: {COMPANY_NAME}
Sponsor Licence Number: {SPONSOR_LICENCE_NUMBER}
Authorising Officer: {AUTHORISING_OFFICER_NAME}
Date of Notification: {now_str}

Worker Details:
- Full Legal Name: {worker_name}
- Certificate of Sponsorship (CoS): {cos_num}
- Sponsored Job Title: {job_title} (SOC: {soc_code})

Reason for Report: Unauthorised absence exceeding 10 consecutive working days.
Details: The above-named sponsored worker has been absent from their contracted duties at Ether Worldwide Ltd without notification or authorisation since {details}. 
Sponsor Compliance Actions Taken:
1. Day 3: Telephone contact attempts made to worker's mobile and emergency contact.
2. Day 5: Formal written notice dispatched to recorded UK residential address.
3. Day 8: Medical certification deadline elapsed with no valid GP Fit Note provided.
Statutory Basis: Obligation executed under Paragraph 8.2 of Workers and Temporary Workers Sponsor Guidance Part 3.
Submitted by Authorising Officer: {AUTHORISING_OFFICER_NAME}."""

    elif trigger_type == "CHANGE_IN_SALARY":
        return f"""[UKVI SMS NOTIFICATION - VISA EXPIRY & SPONSORSHIP REVIEW]
Sponsor Organisation: {COMPANY_NAME}
Sponsor Licence Number: {SPONSOR_LICENCE_NUMBER}
Authorising Officer: {AUTHORISING_OFFICER_NAME}
Date: {now_str}

Worker Details:
- Name: {worker_name}
- CoS Number: {cos_num}
- Job Title: {job_title} (SOC: {soc_code})

Notification: Time-limited Skilled Worker leave expiry notice.
Details: {details}
Sponsor Action: Extension application consultation in progress or CoS close-out to be confirmed within statutory deadline.
Authorising Officer: {AUTHORISING_OFFICER_NAME}."""

    elif trigger_type == "START_DATE_DELAY_28_DAYS":
        return f"""[UKVI SMS NOTIFICATION - DELAYED COMMENCEMENT]
Sponsor Organisation: {COMPANY_NAME}
Sponsor Licence Number: {SPONSOR_LICENCE_NUMBER}
Authorising Officer: {AUTHORISING_OFFICER_NAME}
Date: {now_str}

Worker Name: {worker_name}
CoS Number: {cos_num}

Reason: Sponsored worker has not commenced work within 28 days of agreed CoS start date.
Details: {details}
Submitted by Authorising Officer: {AUTHORISING_OFFICER_NAME}."""

    else:
        return f"""[UKVI SMS NOTIFICATION - CHANGE OF CIRCUMSTANCES]
Sponsor Organisation: {COMPANY_NAME}
Sponsor Licence Number: {SPONSOR_LICENCE_NUMBER}
Authorising Officer: {AUTHORISING_OFFICER_NAME}
Date: {now_str}

Worker Name: {worker_name}
CoS Number: {cos_num}
Category: {trigger_type}
Details: {details}
Submitted by Authorising Officer: {AUTHORISING_OFFICER_NAME}."""
