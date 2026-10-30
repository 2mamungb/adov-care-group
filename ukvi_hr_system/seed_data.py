import os
import sys
import sqlite3
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ukvi_hr_system.database import (
    get_connection, init_db, hash_password, 
    COMPANY_NAME, SPONSOR_LICENCE_NUMBER, AUTHORISING_OFFICER_NAME
)

def seed_database():
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    # Clear old data safely and reset sequence
    cursor.execute("PRAGMA foreign_keys = OFF;")
    tables = [
        'appendix_d_documents', 'attendance_logs', 
        'leave_requests', 'consecutive_absence_tracker', 
        'payroll_records', 'sms_reporting_triggers', 'compliance_audit_logs', 'auth_sessions',
        'immigration_publications', 'health_safety_policies', 'hse_assessments',
        'company_profile', 'employees'
    ]
    for tbl in tables:
        cursor.execute(f"DELETE FROM {tbl}")
    try:
        cursor.execute("DELETE FROM sqlite_sequence")
    except Exception:
        pass
    cursor.execute("PRAGMA foreign_keys = ON;")

    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # 1. Company Profile: Ether Worldwide Ltd
    cursor.execute("""
        INSERT INTO company_profile (
            company_name, trading_name, sponsor_licence_number, licence_tier,
            licence_rating, authorising_officer, key_contact, registered_address,
            operating_sector, created_at, updated_at
        ) VALUES (
            ?, 'Ether Worldwide', ?, 'Worker / Skilled Worker',
            'Grade A (Premium)', ?, 'Sophia Reed (Head of People)',
            'Ether Worldwide Tech House, 100 Bishopsgate, London, EC2N 4AG',
            'Cross-Border E-Commerce, Global Supply Chain & Digital Retail Infrastructure',
            ?, ?
        )
    """, (COMPANY_NAME, SPONSOR_LICENCE_NUMBER, AUTHORISING_OFFICER_NAME, now_str, now_str))

    # 2. Key Personnel & Comprehensive Employees
    pw_mamun, salt_mamun = hash_password("MamunPass2026!")
    pw_ariful, salt_ariful = hash_password("ArifulPass2026!")
    pw_prabal, salt_prabal = hash_password("PrabalPass2026!")
    pw_amina, salt_amina = hash_password("AminaPass2026!")
    pw_sophia, salt_sophia = hash_password("SophiaPass2026!")

    employees = [
        # Employee 1: Mr. Abdullah Al Mamun (Authorising Officer & Managing Director)
        {
            "employee_id": "EMP-ETH-001",
            "full_name": "Mr. Abdullah Al Mamun",
            "preferred_name": "Mamun",
            "nationality": "British",
            "date_of_birth": "1983-04-12",
            "gender": "Male",
            "email": "abdullah.mamun@etherworldwide.co.uk",
            "password_hash": pw_mamun,
            "password_salt": salt_mamun,
            "role": "SUPER_ADMIN",
            "immigration_status": "BRITISH_CITIZEN",
            "job_title": "Managing Director & Authorising Officer",
            "soc_code": "1136 - Information technology and telecommunications directors",
            "department": "Executive Leadership & Board",
            "start_date": "2020-03-01",
            "employment_status": "ACTIVE",
            "work_location": "Ether Worldwide London HQ, 100 Bishopsgate",
            "workplace_hybrid_ratio": "On-Site Executive Office",
            "contracted_weekly_hours": 40.0,
            "standard_working_pattern": "Mon - Fri, 09:00 - 18:00 (40.0 hrs)",
            "annual_gross_salary": 85000.0,
            "hourly_rate": 40.86,
            "reporting_manager": "Board of Directors",
            "probation_end_date": "2020-09-01",
            "recruitment_method": "Founding Director Appointment",
            "cos_number": None,
            "cos_issue_date": None,
            "cos_expiry_date": None,
            "visa_expiry_date": None,
            "brp_or_share_code": None,
            "share_code_verified_date": "2020-03-01",
            "next_rtw_check_due": None,
            "passport_number": "UK-882910401",
            "passport_issue_date": "2022-01-10",
            "passport_expiry_date": "2032-01-10",
            "passport_issuing_country": "United Kingdom",
            "uk_arrival_date": None,
            "vignette_reference": None,
            "english_language_level": "Native English / British Citizen",
            "ecctis_reference": "N/A",
            "national_insurance_number": "AM882910B",
            "phone_number": "+44 7700 900101",
            "uk_residential_address": "Flat 12, Tower Bridge Wharf, St Katharine Docks, London, E1W 1LA",
            "previous_address_history": "14 Canary Riverside, London, E14 (2018 - 2021)",
            "emergency_contact_name": "Family Emergency Contact",
            "emergency_contact_relationship": "Spouse",
            "emergency_contact_phone": "+44 7700 900102",
            "emergency_contact_address": "Flat 12, Tower Bridge Wharf, London, E1W 1LA",
            "dbs_certificate_number": "DBS-008129481",
            "dbs_issue_date": "2024-01-15",
            "supplementary_hours_declared": 0.0
        },
        # Employee 2: Ariful Islam (Lead E-Commerce Software Architect)
        {
            "employee_id": "EMP-ETH-002",
            "full_name": "Ariful Islam",
            "preferred_name": "Ariful",
            "nationality": "Bangladeshi",
            "date_of_birth": "1991-08-24",
            "gender": "Male",
            "email": "ariful.islam@etherworldwide.co.uk",
            "password_hash": pw_ariful,
            "password_salt": salt_ariful,
            "role": "STAFF",
            "immigration_status": "SKILLED_WORKER",
            "job_title": "Lead E-Commerce Software Architect & Cloud Engineer",
            "soc_code": "2136 - Programmers and software development professionals",
            "department": "E-Commerce Tech & Digital Infrastructure",
            "start_date": "2023-04-15",
            "employment_status": "ACTIVE",
            "work_location": "Ether Worldwide London HQ / Hybrid",
            "workplace_hybrid_ratio": "3 Days London HQ / 2 Days Remote",
            "contracted_weekly_hours": 37.5,
            "standard_working_pattern": "Mon - Fri, 09:00 - 17:30 (37.5 hrs)",
            "annual_gross_salary": 52500.0,
            "hourly_rate": 26.92,
            "reporting_manager": "Mr. Abdullah Al Mamun (Managing Director)",
            "probation_end_date": "2023-10-15",
            "recruitment_method": "Direct specialized tech vacancy listing on LinkedIn & tech boards; 3-stage coding interview",
            "cos_number": "C7X9K20241",
            "cos_issue_date": "2023-03-20",
            "cos_expiry_date": "2028-09-15",
            "visa_expiry_date": "2028-09-15",
            "brp_or_share_code": "SH-7821-A912-M401",
            "share_code_verified_date": "2024-04-10",
            "next_rtw_check_due": "2028-08-15",
            "passport_number": "BD-A88291044",
            "passport_issue_date": "2019-05-14",
            "passport_expiry_date": "2029-05-14",
            "passport_issuing_country": "Bangladesh",
            "uk_arrival_date": "2023-04-02",
            "vignette_reference": "VIG-UK-7719204A",
            "english_language_level": "MSc taught in English / CEFR Level C1",
            "ecctis_reference": "ECCTIS-2023-881920",
            "national_insurance_number": "AI492817D",
            "phone_number": "+44 7700 900202",
            "uk_residential_address": "28 Canary Riverside, Westferry Circus, London, E14 8RR",
            "previous_address_history": "55 Marsh Wall, Isle of Dogs, London, E14 9TP (2023 - 2024)",
            "emergency_contact_name": "Tanzina Islam",
            "emergency_contact_relationship": "Spouse",
            "emergency_contact_phone": "+44 7700 900203",
            "emergency_contact_address": "28 Canary Riverside, Westferry Circus, London, E14 8RR",
            "dbs_certificate_number": "DBS-009182341",
            "dbs_issue_date": "2024-02-10",
            "supplementary_hours_declared": 0.0
        },
        # Employee 3: Prabal Barua (Supply Chain & Inventory Operations Manager - Visa Expiring 28d)
        {
            "employee_id": "EMP-ETH-003",
            "full_name": "Prabal Barua",
            "preferred_name": "Prabal",
            "nationality": "Bangladeshi",
            "date_of_birth": "1993-11-19",
            "gender": "Male",
            "email": "prabal.barua@etherworldwide.co.uk",
            "password_hash": pw_prabal,
            "password_salt": salt_prabal,
            "role": "STAFF",
            "immigration_status": "SKILLED_WORKER",
            "job_title": "E-Commerce Supply Chain & Inventory Operations Manager",
            "soc_code": "2424 - Business and financial project management professionals",
            "department": "Global Logistics & Fulfilment",
            "start_date": "2023-11-20",
            "employment_status": "ACTIVE",
            "work_location": "Ether Worldwide London HQ / Fulfilment Hub",
            "workplace_hybrid_ratio": "4 Days London Fulfilment Hub / 1 Day Remote",
            "contracted_weekly_hours": 37.5,
            "standard_working_pattern": "Mon - Fri, 08:30 - 17:00 (37.5 hrs)",
            "annual_gross_salary": 46000.0,
            "hourly_rate": 23.58,
            "reporting_manager": "Mr. Abdullah Al Mamun (Managing Director)",
            "probation_end_date": "2024-05-20",
            "recruitment_method": "Global Supply Chain Recruitment portal; 2-stage case study evaluation",
            "cos_number": "C4M8L91823",
            "cos_issue_date": "2023-10-15",
            "cos_expiry_date": "2026-11-26",
            "visa_expiry_date": (now + timedelta(days=28)).strftime("%Y-%m-%d"),
            "brp_or_share_code": "SH-4921-P801-D339",
            "share_code_verified_date": "2023-11-15",
            "next_rtw_check_due": (now + timedelta(days=20)).strftime("%Y-%m-%d"),
            "passport_number": "BD-P91820491",
            "passport_issue_date": "2017-10-15",
            "passport_expiry_date": "2027-10-15",
            "passport_issuing_country": "Bangladesh",
            "uk_arrival_date": "2023-11-05",
            "vignette_reference": "VIG-UK-8819201B",
            "english_language_level": "IELTS Academic Band 7.5 / CEFR C1",
            "ecctis_reference": "ECCTIS-2023-991204",
            "national_insurance_number": "PB192834A",
            "phone_number": "+44 7700 900303",
            "uk_residential_address": "45 Stratford High Street, London, E15 2NE",
            "previous_address_history": "12 Romford Road, Stratford, London, E15 (2023 - 2024)",
            "emergency_contact_name": "Rini Barua",
            "emergency_contact_relationship": "Sister",
            "emergency_contact_phone": "+44 7700 900304",
            "emergency_contact_address": "45 Stratford High Street, London, E15 2NE",
            "dbs_certificate_number": "DBS-007718293",
            "dbs_issue_date": "2023-11-01",
            "supplementary_hours_declared": 0.0
        },
        # Employee 4: Amina Zaib (Senior Marketplace Growth Strategist - Missing Address Proof)
        {
            "employee_id": "EMP-ETH-004",
            "full_name": "Amina Zaib",
            "preferred_name": "Amina",
            "nationality": "Pakistani",
            "date_of_birth": "1994-06-15",
            "gender": "Female",
            "email": "amina.zaib@etherworldwide.co.uk",
            "password_hash": pw_amina,
            "password_salt": salt_amina,
            "role": "STAFF",
            "immigration_status": "SKILLED_WORKER",
            "job_title": "Senior Marketplace Growth & Digital Marketing Strategist",
            "soc_code": "3545 - Sales accounts and business development managers",
            "department": "Marketplace Growth & Partnerships",
            "start_date": "2024-01-15",
            "employment_status": "ACTIVE",
            "work_location": "Ether Worldwide London HQ / Hybrid",
            "workplace_hybrid_ratio": "3 Days London HQ / 2 Days Remote",
            "contracted_weekly_hours": 37.5,
            "standard_working_pattern": "Mon - Fri, 09:00 - 17:30 (37.5 hrs)",
            "annual_gross_salary": 40500.0,
            "hourly_rate": 20.76,
            "reporting_manager": "Mr. Abdullah Al Mamun (Managing Director)",
            "probation_end_date": "2024-07-15",
            "recruitment_method": "E-Commerce Growth Talent Pool & Executive Headhunt",
            "cos_number": "C8B2T88412",
            "cos_issue_date": "2023-12-10",
            "cos_expiry_date": "2027-08-20",
            "visa_expiry_date": "2027-08-20",
            "brp_or_share_code": "SH-6612-Z819-K204",
            "share_code_verified_date": "2024-01-10",
            "next_rtw_check_due": "2027-07-20",
            "passport_number": "PK-V99182390",
            "passport_issue_date": "2021-07-22",
            "passport_expiry_date": "2031-07-22",
            "passport_issuing_country": "Pakistan",
            "uk_arrival_date": "2024-01-05",
            "vignette_reference": "VIG-UK-9912841C",
            "english_language_level": "MSc E-Commerce Analytics (UK University) / CEFR C1",
            "ecctis_reference": "UK-DEGREE-2023-AZ",
            "national_insurance_number": "AZ991823C",
            "phone_number": "+44 7700 900404",
            "uk_residential_address": "18 Greenwich South Street, London, SE10 8BW",
            "previous_address_history": "8 Creek Road, Deptford, London, SE8 (2022 - 2023)",
            "emergency_contact_name": "Farhan Zaib",
            "emergency_contact_relationship": "Brother",
            "emergency_contact_phone": "+44 7700 900405",
            "emergency_contact_address": "18 Greenwich South Street, London, SE10 8BW",
            "dbs_certificate_number": "DBS-001284719",
            "dbs_issue_date": "2024-01-05",
            "supplementary_hours_declared": 0.0
        },
        # Employee 5: Sophia Reed (Head of People & Level 1 SMS User)
        {
            "employee_id": "EMP-ETH-005",
            "full_name": "Sophia Reed",
            "preferred_name": "Sophia",
            "nationality": "British / EU Settled",
            "date_of_birth": "1988-02-14",
            "gender": "Female",
            "email": "sophia.reed@etherworldwide.co.uk",
            "password_hash": pw_sophia,
            "password_salt": salt_sophia,
            "role": "HR_ADMIN",
            "immigration_status": "SETTLED_STATUS",
            "job_title": "Head of People & UKVI Sponsor Compliance",
            "soc_code": "3562 - Human resources and industrial relations officers",
            "department": "People & Legal Compliance",
            "start_date": "2022-06-01",
            "employment_status": "ACTIVE",
            "work_location": "Ether Worldwide London HQ",
            "workplace_hybrid_ratio": "4 Days London HQ / 1 Day Remote",
            "contracted_weekly_hours": 37.5,
            "standard_working_pattern": "Mon - Fri, 09:00 - 17:30 (37.5 hrs)",
            "annual_gross_salary": 48000.0,
            "hourly_rate": 24.61,
            "reporting_manager": "Mr. Abdullah Al Mamun (Managing Director)",
            "probation_end_date": "2022-12-01",
            "recruitment_method": "Executive HR Search & Board Appointment",
            "cos_number": None,
            "cos_issue_date": None,
            "cos_expiry_date": None,
            "visa_expiry_date": None,
            "brp_or_share_code": "EUSS-771920",
            "share_code_verified_date": "2024-01-10",
            "next_rtw_check_due": None,
            "passport_number": "EU-771920412",
            "passport_issue_date": "2021-08-10",
            "passport_expiry_date": "2031-08-10",
            "passport_issuing_country": "Lithuania",
            "uk_arrival_date": None,
            "vignette_reference": None,
            "english_language_level": "Fluent / CIPD Level 7 Qualified",
            "ecctis_reference": "N/A",
            "national_insurance_number": "SR881920E",
            "phone_number": "+44 7700 900505",
            "uk_residential_address": "8 Marylebone Lane, London, W1U 2PZ",
            "previous_address_history": "22 Baker Street, London, W1U 3BW (2019 - 2022)",
            "emergency_contact_name": "Michael Reed",
            "emergency_contact_relationship": "Spouse",
            "emergency_contact_phone": "+44 7700 900506",
            "emergency_contact_address": "8 Marylebone Lane, London, W1U 2PZ",
            "dbs_certificate_number": "DBS-004819201",
            "dbs_issue_date": "2024-02-01",
            "supplementary_hours_declared": 0.0
        }
    ]

    for emp in employees:
        cursor.execute("""
            INSERT INTO employees (
                employee_id, full_name, preferred_name, nationality, date_of_birth, gender, email, password_hash, password_salt, role,
                immigration_status, job_title, soc_code, department, start_date,
                employment_status, work_location, workplace_hybrid_ratio, contracted_weekly_hours, standard_working_pattern,
                annual_gross_salary, hourly_rate, reporting_manager, probation_end_date, recruitment_method,
                cos_number, cos_issue_date, cos_expiry_date, visa_expiry_date,
                brp_or_share_code, share_code_verified_date, next_rtw_check_due,
                passport_number, passport_issue_date, passport_expiry_date, passport_issuing_country,
                uk_arrival_date, vignette_reference, english_language_level, ecctis_reference,
                national_insurance_number, phone_number, uk_residential_address, previous_address_history,
                emergency_contact_name, emergency_contact_relationship, emergency_contact_phone, emergency_contact_address,
                dbs_certificate_number, dbs_issue_date, supplementary_hours_declared, created_at, updated_at
            ) VALUES (
                :employee_id, :full_name, :preferred_name, :nationality, :date_of_birth, :gender, :email, :password_hash, :password_salt, :role,
                :immigration_status, :job_title, :soc_code, :department, :start_date,
                :employment_status, :work_location, :workplace_hybrid_ratio, :contracted_weekly_hours, :standard_working_pattern,
                :annual_gross_salary, :hourly_rate, :reporting_manager, :probation_end_date, :recruitment_method,
                :cos_number, :cos_issue_date, :cos_expiry_date, :visa_expiry_date,
                :brp_or_share_code, :share_code_verified_date, :next_rtw_check_due,
                :passport_number, :passport_issue_date, :passport_expiry_date, :passport_issuing_country,
                :uk_arrival_date, :vignette_reference, :english_language_level, :ecctis_reference,
                :national_insurance_number, :phone_number, :uk_residential_address, :previous_address_history,
                :emergency_contact_name, :emergency_contact_relationship, :emergency_contact_phone, :emergency_contact_address,
                :dbs_certificate_number, :dbs_issue_date, :supplementary_hours_declared, :created_at, :updated_at
            )
        """, {**emp, "created_at": now_str, "updated_at": now_str})

    conn.commit()

    # Map employee IDs
    cursor.execute("SELECT id, employee_id, full_name FROM employees")
    emp_map = {row['employee_id']: dict(row) for row in cursor.fetchall()}

    # Appendix D Documents with Rich Text Preview Simulation for QuickLook
    def insert_doc(eid, cat, name, ref, auth, status, exp, ver_dt, ver_by, notes, preview):
        cursor.execute("""
            INSERT INTO appendix_d_documents (
                employee_id, category, document_name, document_reference, issued_by_authority,
                file_path, file_type, file_size_kb, file_content_preview, status, expiry_date, verified_date, verified_by, notes
            ) VALUES (?, ?, ?, ?, ?, ?, 'PDF', 312, ?, ?, ?, ?, ?, ?)
        """, (eid, cat, name, ref, auth, f"/docs/emp_{eid}/{cat.lower()}.pdf", preview, status, exp, ver_dt, ver_by, notes))

    # 1. Mr. Abdullah Al Mamun (Authorising Officer)
    mamun_id = emp_map['EMP-ETH-001']['id']
    insert_doc(mamun_id, "PASSPORT_BIO", "British Passport Bio Page", "UK-882910401", "HM Passport Office", "VERIFIED", "2032-01-10", "2020-03-01", "System", "Verified statutory director file.",
        "[HM PASSPORT OFFICE - UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND]\nDocument Type: P | Country Code: GBR | Passport No: UK-882910401\nSurname: AL MAMUN | Given Names: ABDULLAH\nNationality: BRITISH CITIZEN | Date of Birth: 12 APR 1983 | Sex: M\nPlace of Birth: LONDON, GBR | Date of Issue: 10 JAN 2022 | Expiry: 10 JAN 2032\nAuthority: HMPO | Status: Verified Valid for Statutory Identity and RTW.")
    
    insert_doc(mamun_id, "CONTRACT_OF_EMPLOYMENT", "Managing Director Service Agreement", "CONT-DIR-ETH-01", "Ether Worldwide Ltd Board", "VERIFIED", None, "2020-03-01", "Board of Directors", "Executive particulars.",
        "[ETHER WORLDWIDE LTD - EXECUTIVE SERVICE AGREEMENT]\nEmployer: Ether Worldwide Ltd (100 Bishopsgate, London, EC2N 4AG)\nExecutive: Mr. Abdullah Al Mamun\nPosition: Managing Director & Authorising Officer\nRemuneration: £85,000.00 Gross Per Annum (£40.86/hr base)\nContracted Hours: 40.0 Hours/Week | Governance: UK Employment Rights Act 1996\nSignatures: Chairman of the Board & Managing Director Mr. Abdullah Al Mamun.")

    insert_doc(mamun_id, "JOB_DESCRIPTION", "Executive Director & Authorising Officer Role Profile", "JD-EXEC-001", "Board of Directors", "VERIFIED", None, "2020-03-01", "Board", "Verified.",
        "[ROLE PROFILE: MANAGING DIRECTOR & AUTHORISING OFFICER (SOC 1136)]\nOrganisation: Ether Worldwide Ltd | Sponsor Licence: SMS-ETH-882910\nKey Responsibilities: Executive leadership of cross-border e-commerce operations, cloud tech architecture, global supply chain partnerships, and statutory oversight as UKVI Authorising Officer.")

    insert_doc(mamun_id, "NI_PROOF", "HMRC P60 Confirmation (AM882910B)", "HMRC-P60-AM", "HM Revenue & Customs", "VERIFIED", None, "2020-03-05", "Payroll", "Verified.",
        "[HMRC TAX YEAR P60 CERTIFICATE OF PAY AND TAX DEDUCTED]\nEmployer Name: Ether Worldwide Ltd | PAYE Ref: 120/ETH98210\nEmployee: Mr. Abdullah Al Mamun | National Insurance No: AM882910B\nTotal Pay: £85,000.00 | Tax Deducted: £17,450.00 | NI Contributions: Compliant.")

    insert_doc(mamun_id, "UK_ADDRESS_PROOF", "Council Tax & Utility Verification", "PROOF-ADDR-AM", "Tower Hamlets Council", "VERIFIED", "2027-01-01", "2024-03-15", "Sophia Reed", "Verified.",
        "[LONDON BOROUGH OF TOWER HAMLETS - COUNCIL TAX DEMAND NOTICE]\nAccount Reference: CT-88291-AM\nProperty Address: Flat 12, Tower Bridge Wharf, St Katharine Docks, London, E1W 1LA\nLiable Person: Mr. Abdullah Al Mamun | Status: Verified Active Residential Record.")

    # 2. Ariful Islam (Lead E-Commerce Software Architect) - 100% Compliant
    ariful_id = emp_map['EMP-ETH-002']['id']
    insert_doc(ariful_id, "PASSPORT_BIO", "Passport Bio Page (Bangladesh)", "BD-A88291044", "Govt of Bangladesh", "VERIFIED", "2029-05-14", "2023-04-10", "Mr. Abdullah Al Mamun", "Verified valid passport bio.",
        "[PEOPLE'S REPUBLIC OF BANGLADESH - PASSPORT BIO DATA]\nPassport No: BD-A88291044 | Type: P | Country Code: BGD\nSurname: ISLAM | Given Name: ARIFUL\nNationality: BANGLADESHI | DOB: 24 AUG 1991 | Sex: M\nDate of Issue: 14 MAY 2019 | Date of Expiry: 14 MAY 2029\nImmigration Status: UK Skilled Worker Visa Vignette Verified.")

    insert_doc(ariful_id, "BRP_EVISA_SHARE_CODE", "Home Office Online Share Code Record", "SH-7821-A912-M401", "UK Visas and Immigration", "VERIFIED", "2028-09-15", "2024-04-10", "Sophia Reed", "Online eVisa record.",
        "[HOME OFFICE - RIGHT TO WORK ONLINE SHARE CODE VERIFICATION]\nWorker Name: Ariful Islam | Share Code: SH-7821-A912-M401\nImmigration Status: Skilled Worker | Continuous Work Permission: YES\nSponsor: Ether Worldwide Ltd | Permission Expiry Date: 15 September 2028\nConditions: Employment restricted to sponsor; Supplementary work permitted up to 20 hrs/week.")

    insert_doc(ariful_id, "RTW_VERIFICATION_CHECK", "Statutory Right to Work Online Check Certificate", "RTW-CERT-AI-2024", "Home Office Employer Checking Service", "VERIFIED", "2028-09-15", "2024-04-10", "Sophia Reed", "Section 15 excuse active.",
        "[STATUTORY RIGHT TO WORK CHECK CERTIFICATE - SECTION 15 IMMIGRATION ACT 2006]\nEmployer: Ether Worldwide Ltd (Sponsor Licence SMS-ETH-882910)\nEmployee: Ariful Islam | Verification Date: 10 April 2024, 11:24 GMT\nVerified By: Sophia Reed (Head of People)\nHome Office Reference: ECS-2024-881920\nResult: Statutory excuse established for the duration of permission until 15/09/2028.")

    insert_doc(ariful_id, "CONTRACT_OF_EMPLOYMENT", "Employment Contract - Lead Software Architect", "CONT-ETH-AI-02", "Ether Worldwide Ltd", "VERIFIED", None, "2023-04-15", "Mr. Abdullah Al Mamun", "Permanent contract.",
        "[ETHER WORLDWIDE LTD - EMPLOYMENT AGREEMENT]\nEmployee: Ariful Islam | Position: Lead E-Commerce Software Architect & Cloud Engineer\nSOC Code: 2136 | Contracted Weekly Hours: 37.5 Hours\nRemuneration: £52,500.00 Gross Per Annum (£26.92/hr)\nWorking Pattern: Monday to Friday 09:00 - 17:30 | Workplace: London HQ (3 Days) / Remote (2 Days)\nSignatures: Mr. Abdullah Al Mamun (Authorising Officer) & Ariful Islam.")

    insert_doc(ariful_id, "JOB_DESCRIPTION", "Job Description & Hierarchy (SOC 2136)", "JD-2136-AI", "Ether Worldwide Ltd Tech Dept", "VERIFIED", None, "2023-04-15", "Sophia Reed", "SOC match verified.",
        "[JOB DESCRIPTION: LEAD E-COMMERCE SOFTWARE ARCHITECT (SOC 2136)]\nReporting Line: Reports directly to Mr. Abdullah Al Mamun (Managing Director)\nKey Duties: Architect high-throughput distributed e-commerce APIs, cloud microservices on AWS, database sharding, and real-time inventory synchronization engine for global marketplaces.")

    insert_doc(ariful_id, "NI_PROOF", "HMRC Confirmation of NI Number (AI492817D)", "HMRC-AI-2023", "HM Revenue & Customs", "VERIFIED", None, "2023-04-20", "Payroll", "NI confirmed.",
        "[HM REVENUE & CUSTOMS - NATIONAL INSURANCE ALLOCATION CONFIRMATION]\nNational Insurance Number: AI 49 28 17 D\nWorker Name: Ariful Islam\nAddress Recorded: 28 Canary Riverside, Westferry Circus, London, E14 8RR\nEmployer Registered: Ether Worldwide Ltd.")

    insert_doc(ariful_id, "QUALIFICATIONS_AND_REGISTRATION", "MSc Software Engineering & AWS Solutions Architect", "DEG-MSC-AI", "University of Manchester / AWS", "VERIFIED", None, "2023-03-25", "Mr. Abdullah Al Mamun", "Degree & Cert on file.",
        "[QUALIFICATIONS DOSSIER]\n1. Master of Science in Advanced Software Engineering (First Class Honours, University of Manchester)\n2. AWS Certified Solutions Architect - Professional (Validation No: AWS-PSA-881920)\n3. Ecctis English Medium of Instruction Equivalence Statement.")

    insert_doc(ariful_id, "UK_ADDRESS_PROOF", "Canary Riverside Tenancy & Utility Bill", "ADDR-AI-2024", "Canary Riverside Management", "VERIFIED", "2027-04-01", "2024-04-10", "Sophia Reed", "Current address proof.",
        "[RESIDENTIAL TENANCY & UTILITY RECORD]\nTenant Name: Ariful Islam\nAddress: 28 Canary Riverside, Westferry Circus, London, E14 8RR\nCouncil Tax Band F | Thames Water Account: TW-99210-AI\nVerified Date: 10 April 2024 by Sophia Reed.")

    insert_doc(ariful_id, "ABSENCE_RECORD", "Daily Shift & Attendance Log 2024/2026", "ABS-AI-2026", "UKVI SponsorGuard Attendance", "VERIFIED", None, "2026-10-01", "Sophia Reed", "Zero absence.",
        "[STATUTORY ATTENDANCE & SHIFT REGISTER - APPENDIX D ITEM 8]\nEmployee: Ariful Islam (EMP-ETH-002)\nTracking Period: October 2026 | Shifts Completed: 100% On-Schedule\nUnnotified Absences: 0 Days | Annual Leave Taken: Pre-approved 3 Days.")

    insert_doc(ariful_id, "PAYROLL_RECORDS", "Monthly Itemised Payslips (Gross £4,375.00/mo)", "PAY-AI-2026", "Ether Worldwide Payroll", "VERIFIED", None, "2026-10-28", "Payroll", "Matches CoS.",
        "[ETHER WORLDWIDE LTD - ITEMISED STATUTORY PAYSLIP (OCTOBER 2026)]\nEmployee: Ariful Islam | CoS No: C7X9K20241 | Tax Code: 1257L\nGross Pay: £4,375.00 (£52,500/yr) | PAYE Tax: £875.00 | Employee NI: £350.00\nPension (5%): £218.75 | Net Pay BACS Transfer: £2,931.25\nCompliance Check: Salary matches Certificate of Sponsorship; exceeds SOC 2136 minimum rate of £49,400.")

    # 3. Prabal Barua (Supply Chain Operations Manager) - Visa Expiring 28d
    prabal_id = emp_map['EMP-ETH-003']['id']
    insert_doc(prabal_id, "PASSPORT_BIO", "Passport Bio Page (Bangladesh)", "BD-P91820491", "Govt of Bangladesh", "VERIFIED", "2027-10-15", "2023-11-15", "Sophia Reed", "Passport bio.",
        "[PEOPLE'S REPUBLIC OF BANGLADESH - PASSPORT BIO DATA]\nPassport No: BD-P91820491 | Name: PRABAL BARUA\nNationality: BANGLADESHI | DOB: 19 NOV 1993 | Sex: M\nIssue Date: 15 OCT 2017 | Expiry Date: 15 OCT 2027.")

    insert_doc(prabal_id, "BRP_EVISA_SHARE_CODE", "Home Office Share Code Verification", "SH-4921-P801-D339", "UK Visas and Immigration", "VERIFIED", (now + timedelta(days=28)).strftime("%Y-%m-%d"), "2023-11-15", "Sophia Reed", "Expires in 28 days.",
        "[HOME OFFICE - RIGHT TO WORK VERIFICATION]\nName: Prabal Barua | Share Code: SH-4921-P801-D339\nVisa Type: Skilled Worker | Expiry: 26 November 2026\nAlert: 28 Days remaining on current permission. CoS extension allocation in progress by Authorising Officer Mr. Abdullah Al Mamun.")

    insert_doc(prabal_id, "RTW_VERIFICATION_CHECK", "Right to Work Verification Certificate", "RTW-CERT-PB-2023", "UK Home Office", "VERIFIED", (now + timedelta(days=28)).strftime("%Y-%m-%d"), "2023-11-15", "Sophia Reed", "Expiring.",
        "[STATUTORY RIGHT TO WORK CERTIFICATE]\nEmployer: Ether Worldwide Ltd | Employee: Prabal Barua\nExpiry Date: 26 November 2026 | Follow-up RTW check scheduled before 26/11/2026.")

    insert_doc(prabal_id, "CONTRACT_OF_EMPLOYMENT", "Employment Contract - Supply Chain Operations", "CONT-ETH-PB-03", "Ether Worldwide Ltd", "VERIFIED", None, "2023-11-20", "Mr. Abdullah Al Mamun", "Contract on file.",
        "[EMPLOYMENT CONTRACT - SUPPLY CHAIN OPERATIONS (SOC 2424)]\nEmployer: Ether Worldwide Ltd | Employee: Prabal Barua\nRemuneration: £46,000.00 / yr (£23.58/hr) | Hours: 37.5 Hours/Week\nLocation: London Fulfilment Hub / London HQ | Signatures: Mr. Abdullah Al Mamun & Prabal Barua.")

    insert_doc(prabal_id, "JOB_DESCRIPTION", "Job Description (SOC 2424)", "JD-2424-PB", "Logistics Operations", "VERIFIED", None, "2023-11-20", "Sophia Reed", "SOC match.",
        "[JOB SPECIFICATION: SUPPLY CHAIN & INVENTORY OPERATIONS MANAGER (SOC 2424)]\nDuties: Global freight forwarding management, customs clearance compliance, warehouse automated pick-pack logistics, inventory forecasting across UK/EU distribution hubs.")

    insert_doc(prabal_id, "NI_PROOF", "Official HMRC NI Letter (PB192834A)", "NI-PB-2023", "HM Revenue & Customs", "VERIFIED", None, "2023-11-25", "Payroll", "NI verified.",
        "[HM REVENUE & CUSTOMS - NATIONAL INSURANCE ALLOCATION]\nNI Number: PB 19 28 34 A | Name: Prabal Barua\nAddress: 45 Stratford High Street, London, E15 2NE.")

    insert_doc(prabal_id, "UK_ADDRESS_PROOF", "Tenancy Agreement (Stratford)", "ADDR-PB-2023", "Stratford Residential Lettings", "VERIFIED", "2026-11-01", "2023-11-15", "Sophia Reed", "Tenancy on file.",
        "[ASSURED SHORTHOLD TENANCY AGREEMENT]\nTenant: Prabal Barua | Address: 45 Stratford High Street, London, E15 2NE\nVerified Valid for Appendix D Residence Record.")

    insert_doc(prabal_id, "PAYROLL_RECORDS", "Monthly Itemised Payslips (Gross £3,833.33/mo)", "PAY-PB-2026", "Ether Worldwide Payroll", "VERIFIED", None, "2026-10-28", "Payroll", "Compliant.",
        "[ITEMISED PAYSLIP - OCTOBER 2026]\nEmployee: Prabal Barua | Gross Pay: £3,833.33 (£46,000/yr)\nNet Pay BACS: £2,580.00 | Matches CoS Rate; Exceeds SOC 2424 going rate of £44,700.")

    # 4. Amina Zaib (Marketplace Growth Strategist) - Missing Address Proof
    amina_id = emp_map['EMP-ETH-004']['id']
    insert_doc(amina_id, "PASSPORT_BIO", "Pakistan Passport Bio Page", "PK-V99182390", "Govt of Pakistan", "VERIFIED", "2031-07-22", "2024-01-10", "Sophia Reed", "Passport bio.",
        "[ISLAMIC REPUBLIC OF PAKISTAN - PASSPORT DATA]\nPassport No: PK-V99182390 | Surname: ZAIB | Given Name: AMINA\nNationality: PAKISTANI | DOB: 15 JUN 1994 | Sex: F\nIssue Date: 22 JUL 2021 | Expiry Date: 22 JUL 2031.")

    insert_doc(amina_id, "BRP_EVISA_SHARE_CODE", "eVisa Share Code Verification", "SH-6612-Z819-K204", "UK Visas and Immigration", "VERIFIED", "2027-08-20", "2024-01-10", "Sophia Reed", "Valid share code.",
        "[HOME OFFICE RIGHT TO WORK ONLINE VERIFICATION]\nName: Amina Zaib | Share Code: SH-6612-Z819-K204\nVisa Status: Skilled Worker | Valid Until: 20 August 2027\nSponsor: Ether Worldwide Ltd.")

    insert_doc(amina_id, "RTW_VERIFICATION_CHECK", "Online Right to Work Certificate Stamp", "RTW-CERT-AZ-2024", "UK Home Office", "VERIFIED", "2027-08-20", "2024-01-10", "Sophia Reed", "Statutory excuse.",
        "[RIGHT TO WORK VERIFICATION CERTIFICATE]\nEmployer: Ether Worldwide Ltd | Employee: Amina Zaib\nStatus: Statutory excuse established under s.15 Immigration Act 2006 until 20/08/2027.")

    insert_doc(amina_id, "CONTRACT_OF_EMPLOYMENT", "Employment Contract - Marketplace Growth Strategist", "CONT-ETH-AZ-04", "Ether Worldwide Ltd", "VERIFIED", None, "2024-01-15", "Mr. Abdullah Al Mamun", "Contract on file.",
        "[EMPLOYMENT CONTRACT: MARKETPLACE GROWTH STRATEGIST (SOC 3545)]\nEmployer: Ether Worldwide Ltd | Employee: Amina Zaib\nGross Salary: £40,500.00 / yr (£20.76/hr) | Hours: 37.5 Hours/Week\nSignatures: Mr. Abdullah Al Mamun (Authorising Officer) & Amina Zaib.")

    insert_doc(amina_id, "JOB_DESCRIPTION", "Job Description (SOC 3545)", "JD-3545-AZ", "Growth Dept", "VERIFIED", None, "2024-01-15", "Sophia Reed", "SOC match.",
        "[JOB SPECIFICATION: SENIOR MARKETPLACE GROWTH STRATEGIST (SOC 3545)]\nDuties: Lead Amazon, eBay, TikTok Shop, and international marketplace catalog expansion, cross-border PPC ad campaigns, brand registry governance, and B2B distributor partnerships.")

    insert_doc(amina_id, "NI_PROOF", "HMRC NI Confirmation (AZ991823C)", "HMRC-AZ-2024", "HM Revenue & Customs", "VERIFIED", None, "2024-01-20", "Payroll", "NI verified.",
        "[HM REVENUE & CUSTOMS - NATIONAL INSURANCE NUMBER CONFIRMATION]\nNI Number: AZ 99 18 23 C | Name: Amina Zaib\nEmployer Registered: Ether Worldwide Ltd.")

    insert_doc(amina_id, "PAYROLL_RECORDS", "Monthly Itemised Payslips (Gross £3,375.00/mo)", "PAY-AZ-2026", "Ether Worldwide Payroll", "VERIFIED", None, "2026-10-28", "Payroll", "Compliant.",
        "[ITEMISED PAYSLIP - OCTOBER 2026]\nEmployee: Amina Zaib | Gross Pay: £3,375.00 (£40,500/yr)\nNet Pay BACS: £2,290.00 | Matches CoS Rate; Exceeds SOC 3545 minimum rate of £38,700.")

    # 3. Immigration Publications & Government Advisory News
    publications = [
        {
            "title": "Home Office Sponsor Guidance: Transition to Fully Digital eVisas for All Sponsored Workers",
            "category": "IMMIGRATION_RULES",
            "summary": "UK Visas and Immigration (UKVI) reiterates that physical Biometric Residence Permits (BRPs) are fully superseded by digital eVisas. Authorising Officers must ensure all existing sponsored workers have accessed their digital UKVI account and that online Right to Work share codes are retained under Appendix D.",
            "official_source": "UKVI Policy Paper & Employer Guidance",
            "official_source_url": "https://www.gov.uk/guidance/online-right-to-work-checks",
            "publication_date": "2026-10-15",
            "target_audience": "ALL",
            "is_critical": 1
        },
        {
            "title": "Skilled Worker Salary Thresholds: Strict Enforcement of SOC 2020 Going Rates",
            "category": "SPONSOR_DUTY",
            "summary": "Employers are reminded that the General Skilled Worker salary threshold of £38,700 (or applicable SOC going rate, whichever is higher) applies strictly. Employers must ensure hourly rates also meet statutory floors across standard 37.5h or 40h work weeks. Salary reductions below declared CoS figures trigger mandatory SMS notification within 10 working days.",
            "official_source": "Home Office Immigration Rules Appendix Skilled Worker",
            "official_source_url": "https://www.gov.uk/skilled-worker-visa/your-job",
            "publication_date": "2026-10-01",
            "target_audience": "AUTHORISING_OFFICER",
            "is_critical": 1
        },
        {
            "title": "Mandatory 10-Day SMS Absence Reporting Duty: Enforcement Blitz",
            "category": "SPONSOR_DUTY",
            "summary": "Compliance visits by UKVI compliance officers continue to spotlight unreported absences. Sponsoring organisations must report via SMS whenever a sponsored worker is absent for >10 consecutive working days without permission. Failure to report within 10 working days risks immediate licence suspension or downgrade from Grade A to B.",
            "official_source": "Sponsor Guidance Part 3: Sponsor Duties",
            "official_source_url": "https://www.gov.uk/government/publications/workers-and-temporary-workers-guidance-for-sponsors-part-3-sponsor-duties-and-compliance",
            "publication_date": "2026-09-20",
            "target_audience": "AUTHORISING_OFFICER",
            "is_critical": 1
        },
        {
            "title": "Worker Advisory: Supplementary Employment Permitted Strictly up to 20 Hours per Week",
            "category": "WORKER_RIGHTS",
            "summary": "Skilled Worker visa holders are permitted to undertake secondary employment up to a maximum of 20 hours per week, provided it is either in a role on the Immigration Salary List or in the same professional SOC code and level as their sponsored employment. Working beyond 20 hours outside the sponsor is a civil breach of visa conditions.",
            "official_source": "UKVI Workers Conditions of Stay",
            "official_source_url": "https://www.gov.uk/skilled-worker-visa/second-job",
            "publication_date": "2026-08-15",
            "target_audience": "SPONSORED_WORKER",
            "is_critical": 0
        },
        {
            "title": "Sponsorship Management System (SMS) Scheduled Maintenance Notice",
            "category": "SMS_SYSTEM",
            "summary": "The Sponsorship Management System (SMS) will undergo routine infrastructure maintenance on Saturday night. Level 1 and Level 2 users are advised to submit time-sensitive worker notifications and CoS assignment requests prior to the maintenance window.",
            "official_source": "UKVI SMS Service Desk",
            "official_source_url": "https://www.points.homeoffice.gov.uk/gui-sms-jsf/SMS-003-Landing.faces",
            "publication_date": "2026-10-24",
            "target_audience": "AUTHORISING_OFFICER",
            "is_critical": 0
        }
    ]

    for pub in publications:
        cursor.execute("""
            INSERT INTO immigration_publications (
                title, category, summary, official_source, official_source_url,
                publication_date, target_audience, is_critical, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            pub['title'], pub['category'], pub['summary'], pub['official_source'],
            pub['official_source_url'], pub['publication_date'], pub['target_audience'],
            pub['is_critical'], now_str
        ))

    # 4. Statutory Health & Safety (HSE) Policies & Standards for Ether Worldwide Ltd
    hse_policies = [
        {
            "policy_code": "HSE-DSE-01",
            "title": "Display Screen Equipment (DSE) & Ergonomics Workstation Standard",
            "description": "Mandatory workstation assessment for all software architects, growth strategists, and office personnel spending over 2 hours daily on display screens. Enforces ergonomic seating, monitor eye-level alignment, anti-glare filters, and 5-minute hourly breaks.",
            "category": "OFFICE_DSE",
            "legislation_ref": "Health and Safety (Display Screen Equipment) Regulations 1992 (as amended 2002)",
            "mandatory_for": "ALL_STAFF",
            "last_reviewed_date": "2026-06-01",
            "next_review_due": "2027-06-01",
            "responsible_officer": "Sophia Reed (Head of People)"
        },
        {
            "policy_code": "HSE-WHSE-02",
            "title": "E-Commerce Fulfilment Hub Manual Handling & Logistics Safety Standard",
            "description": "Governs package sorting, pallet lifting, repetitive motion ergonomics, and high-visibility PPE requirements across London fulfilment and dispatch zones. Implements strict maximum lifting guidelines (25kg male / 16kg female at waist level).",
            "category": "WAREHOUSE_ERGONOMICS",
            "legislation_ref": "Manual Handling Operations Regulations 1992 (MHOR) & Workplace (Health, Safety and Welfare) Regulations 1992",
            "mandatory_for": "LOGISTICS_WAREHOUSE",
            "last_reviewed_date": "2026-05-15",
            "next_review_due": "2027-05-15",
            "responsible_officer": "Prabal Barua (Supply Chain Operations Manager)"
        },
        {
            "policy_code": "HSE-FIRE-03",
            "title": "Workplace Fire Risk Assessment, Prevention & Emergency Evacuation Protocol",
            "description": "Establishes mandatory fire warden routes, twice-annual alarm drills, clear fire escape pathways at 100 Bishopsgate HQ, and emergency lighting verification logs.",
            "category": "FIRE_SAFETY",
            "legislation_ref": "Regulatory Reform (Fire Safety) Order 2005",
            "mandatory_for": "ALL_STAFF",
            "last_reviewed_date": "2026-09-01",
            "next_review_due": "2027-09-01",
            "responsible_officer": "Mr. Abdullah Al Mamun (Managing Director)"
        },
        {
            "policy_code": "HSE-HYBRID-04",
            "title": "Hybrid & Remote Home Workstation Electrical & Welfare Safety Standard",
            "description": "Ensures home working environments for software developers and remote staff comply with electrical safety (PAT testing guidelines), adequate ventilation, and ergonomic seating.",
            "category": "OFFICE_DSE",
            "legislation_ref": "Health and Safety at Work etc. Act 1974 Section 2",
            "mandatory_for": "TECH_REMOTE",
            "last_reviewed_date": "2026-07-10",
            "next_review_due": "2027-07-10",
            "responsible_officer": "Ariful Islam (Lead Software Architect)"
        },
        {
            "policy_code": "HSE-FIRSTAID-05",
            "title": "Workplace First Aid, Medical Emergency & Mental Health Well-Being Standard",
            "description": "Appoints trained certified First Aiders, maintains stocked First Aid kits at London HQ and fulfilment hubs, and provides access to confidential Employee Assistance Programs (EAP).",
            "category": "FIRST_AID",
            "legislation_ref": "Health and Safety (First-Aid) Regulations 1981",
            "mandatory_for": "ALL_STAFF",
            "last_reviewed_date": "2026-04-01",
            "next_review_due": "2027-04-01",
            "responsible_officer": "Sophia Reed (Head of People)"
        }
    ]

    for pol in hse_policies:
        cursor.execute("""
            INSERT INTO health_safety_policies (
                policy_code, title, description, category, legislation_ref,
                mandatory_for, last_reviewed_date, next_review_due, responsible_officer, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'ACTIVE')
        """, (
            pol['policy_code'], pol['title'], pol['description'], pol['category'],
            pol['legislation_ref'], pol['mandatory_for'], pol['last_reviewed_date'],
            pol['next_review_due'], pol['responsible_officer']
        ))

    # 5. HSE Risk Assessments & Worker Signed Declarations
    cursor.execute("""
        INSERT INTO hse_assessments (employee_id, assessment_type, compliance_status, assessment_date, notes, signed_by_worker, reviewed_by_officer)
        VALUES (?, 'DSE_WORKSTATION', 'COMPLIANT', '2026-05-10', 'Dual monitor eye-level setup verified. Ergonomic lumbar chair installed for software architecture desk.', 1, ?)
    """, (ariful_id, AUTHORISING_OFFICER_NAME))

    cursor.execute("""
        INSERT INTO hse_assessments (employee_id, assessment_type, compliance_status, assessment_date, notes, signed_by_worker, reviewed_by_officer)
        VALUES (?, 'MANUAL_HANDLING', 'COMPLIANT', '2026-06-15', 'Completed warehouse pallet & inventory ergonomics training. Steel toe safety footwear verified.', 1, 'Sophia Reed')
    """, (prabal_id,))

    cursor.execute("""
        INSERT INTO hse_assessments (employee_id, assessment_type, compliance_status, assessment_date, notes, signed_by_worker, reviewed_by_officer)
        VALUES (?, 'DSE_WORKSTATION', 'COMPLIANT', '2026-07-20', 'Marketplace analytics multi-screen assessment completed. Adjustable desk setup approved.', 1, 'Sophia Reed')
    """, (amina_id,))

    # SMS Trigger for Prabal Barua (Upcoming 28-day visa expiry)
    cursor.execute("""
        INSERT INTO sms_reporting_triggers (
            employee_id, trigger_type, description, severity, home_office_deadline, status, sms_submission_notes, created_at
        ) VALUES (?, 'CHANGE_IN_SALARY', ?, 'HIGH', ?, 'PENDING_ACTION', ?, ?)
    """, (
        prabal_id,
        "Skilled Worker permission expiring in 28 days (26 Nov 2026). Extension CoS allocation or cessation of sponsorship must be filed.",
        (now + timedelta(days=28)).strftime("%Y-%m-%d"),
        f"Authorising Officer {AUTHORISING_OFFICER_NAME} reviewing renewal allocation on SMS.",
        now_str
    ))

    # Attendance logs (Past 7 days)
    for emp_code, emp_obj in emp_map.items():
        eid = emp_obj['id']
        for d in range(1, 6):
            att_date = (now - timedelta(days=d)).strftime("%Y-%m-%d")
            cursor.execute("""
                INSERT INTO attendance_logs (employee_id, date, clock_in_time, clock_out_time, hours_worked, break_minutes, status, location_tag, ip_address, notes)
                VALUES (?, ?, '09:00:00', '17:00:00', 7.5, 30, 'PRESENT', 'Ether Worldwide London HQ / Workstation', '192.168.1.45', 'Standard shift completed')
            """, (eid, att_date))

    # Leave requests
    cursor.execute("""
        INSERT INTO leave_requests (employee_id, leave_type, start_date, end_date, total_days, status, reason, fit_note_attached, self_certificate_completed, approved_by, created_at)
        VALUES (?, 'ANNUAL_LEAVE', ?, ?, 3.0, 'APPROVED', 'Annual pre-booked leave entitlement', 0, 0, ?, ?)
    """, (ariful_id, (now + timedelta(days=14)).strftime("%Y-%m-%d"), (now + timedelta(days=17)).strftime("%Y-%m-%d"), AUTHORISING_OFFICER_NAME, now_str))

    cursor.execute("""
        INSERT INTO leave_requests (employee_id, leave_type, start_date, end_date, total_days, status, reason, fit_note_attached, self_certificate_completed, created_at)
        VALUES (?, 'ANNUAL_LEAVE', ?, ?, 2.0, 'PENDING', 'Marketplace tech conference and study leave', 0, 0, ?)
    """, (amina_id, (now + timedelta(days=20)).strftime("%Y-%m-%d"), (now + timedelta(days=22)).strftime("%Y-%m-%d"), now_str))

    # 6. HMRC Compliant Payroll Records (Past 3 Months: Aug, Sep, Oct 2026)
    from ukvi_hr_system.payroll_calculator import calculate_full_statutory_payslip
    
    pay_periods = [
        ("August 2026", "2026-08-28"),
        ("September 2026", "2026-09-28"),
        ("October 2026", "2026-10-28")
    ]

    for emp_code, emp_obj in emp_map.items():
        eid = emp_obj['id']
        cursor.execute("SELECT annual_gross_salary, hourly_rate, contracted_weekly_hours, soc_code FROM employees WHERE id = ?", (eid,))
        emp_salary_data = cursor.fetchone()
        annual = emp_salary_data['annual_gross_salary']
        hours = emp_salary_data['contracted_weekly_hours']

        for period_name, pay_dt in pay_periods:
            calc = calculate_full_statutory_payslip(
                basic_salary_annual=annual,
                overtime_hours=0.0,
                overtime_hourly_rate=emp_salary_data['hourly_rate'],
                bonus_pay=0.0,
                tax_code="1257L",
                ni_category="A",
                contracted_weekly_hours=hours
            )

            ref = f"ETH-PAY-{pay_dt[:7]}-{emp_code}"
            cursor.execute("""
                INSERT INTO payroll_records (
                    employee_id, tax_year, pay_period, pay_date, pay_frequency, tax_code, ni_category,
                    basic_salary, overtime_hours, overtime_rate, overtime_pay, bonus_pay,
                    gross_pay, tax_deduction, ni_deduction, ni_employer, pension_employee, pension_employer,
                    student_loan_deduction, net_pay, cos_rate_match, minimum_wage_compliant,
                    rti_status, rti_submission_id, rti_timestamp, p60_generated, payslip_reference, notes,
                    created_at, updated_at
                ) VALUES (
                    ?, '2026/27', ?, ?, 'MONTHLY', '1257L', 'A - Standard Rate',
                    ?, 0.0, ?, 0.0, 0.0,
                    ?, ?, ?, ?, ?, ?,
                    0.0, ?, ?, ?,
                    'RTI_SUBMITTED', ?, ?, 1, ?, 'HMRC Full Payment Submission (FPS) confirmed with gateway.',
                    ?, ?
                )
            """, (
                eid, period_name, pay_dt,
                calc['monthly_basic'], emp_salary_data['hourly_rate'],
                calc['total_gross_pay'], calc['paye_tax_deducted'], calc['employee_ni_deducted'],
                calc['employer_ni_contribution'], calc['employee_pension_deducted'],
                calc['employer_pension_contribution'], calc['net_take_home_pay'],
                calc['cos_rate_match'], calc['minimum_wage_compliant'],
                f"HMRC-FPS-{pay_dt.replace('-', '')}-{eid}", f"{pay_dt} 10:15:00", ref,
                now_str, now_str
            ))

    # Audit log
    cursor.execute("""
        INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, ip_address, timestamp, severity)
        VALUES ('SYSTEM_INITIALIZATION', ?, NULL, 'Ether Worldwide Ltd comprehensive Appendix D, Immigration Publications, and HSE data initialized.', '127.0.0.1', ?, 'INFO')
    """, (AUTHORISING_OFFICER_NAME, now_str))

    conn.commit()
    conn.close()
    print(f"✅ {COMPANY_NAME} database successfully seeded with comprehensive records, news publications, and HSE standards.")

if __name__ == "__main__":
    seed_database()
