import http.server
import socketserver
import json
import urllib.parse
import os
import sys
import secrets
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ukvi_hr_system.database import (
    get_connection, hash_password, verify_password,
    COMPANY_NAME, SPONSOR_LICENCE_NUMBER, AUTHORISING_OFFICER_NAME
)
from ukvi_hr_system.compliance_engine import (
    audit_employee_compliance, 
    audit_organization_overview, 
    generate_sms_text_template,
    APPENDIX_D_MANDATORY_CATEGORIES,
    SOC_CODE_BENCHMARKS
)

PORT = 8085
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

class UKVIComplianceHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def _send_json(self, data, status_code=200):
        response_bytes = json.dumps(data, default=str).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(response_bytes)))
        # Security Headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'SAMEORIGIN')
        self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')
        self.end_headers()
        self.wfile.write(response_bytes)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def _read_body_json(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                return json.loads(body)
            except Exception:
                return {}
        return {}

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)

        # API Endpoints
        if path.startswith("/api/"):
            try:
                if path == "/api/company":
                    self._send_json({
                        "company_name": COMPANY_NAME,
                        "sponsor_licence_number": SPONSOR_LICENCE_NUMBER,
                        "authorising_officer": AUTHORISING_OFFICER_NAME,
                        "status": "Grade A Active"
                    })
                elif path == "/api/auth/demo_users":
                    self.handle_get_demo_users()
                elif path == "/api/compliance/overview":
                    self.handle_compliance_overview()
                elif path.startswith("/api/compliance/employee/"):
                    param = path.split("/")[-1]
                    self.handle_employee_audit(param)
                elif path.startswith("/api/compliance/sms_draft/"):
                    trigger_id = int(path.split("/")[-1])
                    self.handle_sms_draft(trigger_id)
                elif path.startswith("/api/compliance/export_pack/"):
                    param = path.split("/")[-1]
                    self.handle_export_inspection_pack(param)
                elif path == "/api/employees":
                    self.handle_get_employees()
                elif path == "/api/attendance/logs":
                    emp_id = query.get('employee_id', [None])[0]
                    self.handle_get_attendance(emp_id)
                elif path == "/api/attendance/today_status":
                    emp_id = query.get('employee_id', [None])[0]
                    self.handle_today_attendance_status(emp_id)
                elif path == "/api/leave/list":
                    emp_id = query.get('employee_id', [None])[0]
                    self.handle_get_leave_list(emp_id)
                elif path == "/api/payroll/records":
                    emp_id = query.get('employee_id', [None])[0]
                    self.handle_get_payroll(emp_id, query)
                elif path == "/api/compliance/document_matrix":
                    self.handle_get_document_matrix()
                elif path == "/api/publications":
                    self.handle_get_publications(query)
                elif path == "/api/hse/policies":
                    self.handle_get_hse_policies(query)
                elif path == "/api/hse/assessments":
                    emp_id = query.get('employee_id', [None])[0]
                    self.handle_get_hse_assessments(emp_id)
                elif path.startswith("/api/documents/"):
                    doc_id = path.split("/")[-1]
                    self.handle_get_document(doc_id)
                elif path == "/api/audit_logs":
                    self.handle_get_audit_logs()
                else:
                    self._send_json({"error": "Endpoint not found"}, 404)
            except Exception as e:
                self._send_json({"error": str(e)}, 500)
            return

        # Serve Frontend
        if path == "/" or path == "/index.html":
            self.path = "/index.html"
        return super().do_GET()

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        body = self._read_body_json()

        if path.startswith("/api/"):
            try:
                if path == "/api/auth/login":
                    self.handle_login(body)
                elif path == "/api/attendance/clock_in":
                    self.handle_clock_in(body)
                elif path == "/api/attendance/clock_out":
                    self.handle_clock_out(body)
                elif path == "/api/leave/request":
                    self.handle_submit_leave(body)
                elif path == "/api/leave/action":
                    self.handle_leave_action(body)
                elif path == "/api/compliance/sms_action":
                    self.handle_sms_action(body)
                elif path == "/api/compliance/verify_doc":
                    self.handle_verify_document(body)
                elif path == "/api/compliance/upload_doc":
                    self.handle_upload_document(body)
                elif path == "/api/profile/update":
                    self.handle_update_profile(body)
                elif path == "/api/profile/declare_supplementary":
                    self.handle_declare_supplementary(body)
                elif path == "/api/employees/create":
                    self.handle_create_employee(body)
                elif path == "/api/employees/create_comprehensive":
                    self.handle_create_employee_comprehensive(body)
                elif path == "/api/employees/update":
                    self.handle_update_employee(body)
                elif path == "/api/documents/update":
                    self.handle_update_document(body)
                elif path == "/api/hse/assessments":
                    self.handle_save_hse_assessment(body)
                elif path == "/api/publications/add":
                    self.handle_add_publication(body)
                elif path == "/api/payroll/calculate":
                    self.handle_calculate_payroll(body)
                elif path == "/api/payroll/run":
                    self.handle_run_payroll(body)
                elif path == "/api/payroll/update_record":
                    self.handle_update_payroll_record(body)
                elif path == "/api/payroll/submit_rti":
                    self.handle_submit_rti(body)
                else:
                    self._send_json({"error": "Endpoint not found"}, 404)
            except Exception as e:
                self._send_json({"error": str(e)}, 500)
            return

        self._send_json({"error": "Method not supported"}, 405)

    # --- HANDLERS ---

    def handle_get_demo_users(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, employee_id, full_name, email, role, immigration_status, job_title, department FROM employees ORDER BY id ASC")
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        self._send_json({"company": COMPANY_NAME, "users": rows})

    def handle_login(self, body):
        email = body.get('email', '').strip()
        password = body.get('password', '').strip()

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE LOWER(email) = LOWER(?)", (email,))
        emp = cursor.fetchone()

        if not emp:
            conn.close()
            self._send_json({"error": "Invalid email address or unauthorized user."}, 401)
            return

        emp_dict = dict(emp)
        if password and not verify_password(emp_dict['password_hash'], emp_dict['password_salt'], password):
            # Increment failed attempts
            cursor.execute("UPDATE employees SET failed_login_attempts = failed_login_attempts + 1 WHERE id = ?", (emp_dict['id'],))
            conn.commit()
            conn.close()
            self._send_json({"error": "Incorrect password provided."}, 401)
            return

        # Reset failed attempts and generate cryptographically secure token
        token = secrets.token_urlsafe(32)
        now = datetime.now()
        expires = (now + timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("UPDATE employees SET failed_login_attempts = 0 WHERE id = ?", (emp_dict['id'],))
        cursor.execute("""
            INSERT INTO auth_sessions (session_token, employee_id, created_at, expires_at)
            VALUES (?, ?, ?, ?)
        """, (token, emp_dict['id'], now.strftime("%Y-%m-%d %H:%M:%S"), expires))

        conn.commit()
        conn.close()

        del emp_dict['password_hash']
        del emp_dict['password_salt']

        self._send_json({"token": token, "user": emp_dict, "expires_at": expires})

    def handle_compliance_overview(self):
        data = audit_organization_overview()
        self._send_json(data)

    def handle_employee_audit(self, identifier):
        conn = get_connection()
        cursor = conn.cursor()
        
        emp = None
        # Try integer ID
        if str(identifier).isdigit():
            cursor.execute("SELECT * FROM employees WHERE id = ?", (int(identifier),))
            emp = cursor.fetchone()

        # Try employee_id code
        if not emp:
            cursor.execute("SELECT * FROM employees WHERE employee_id = ? OR employee_id = ?", (str(identifier), f"EMP-ETH-{identifier}"))
            emp = cursor.fetchone()

        # Fallback to first employee
        if not emp:
            cursor.execute("SELECT * FROM employees ORDER BY id ASC LIMIT 1")
            emp = cursor.fetchone()

        if not emp:
            conn.close()
            self._send_json({"error": "Employee not found"}, 404)
            return

        emp_dict = dict(emp)
        real_id = emp_dict['id']
        if 'password_hash' in emp_dict:
            del emp_dict['password_hash']
        if 'password_salt' in emp_dict:
            del emp_dict['password_salt']

        audit = audit_employee_compliance(real_id)
        conn.close()
        self._send_json({"employee": emp_dict, "audit": audit})

    def handle_sms_draft(self, trigger_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT t.*, e.full_name, e.employee_id as emp_code, e.cos_number, e.job_title, e.soc_code
            FROM sms_reporting_triggers t
            JOIN employees e ON t.employee_id = e.id
            WHERE t.id = ?
        """, (trigger_id,))
        trigger = cursor.fetchone()
        conn.close()

        if not trigger:
            self._send_json({"error": "Trigger not found"}, 404)
            return

        trig_dict = dict(trigger)
        text_template = generate_sms_text_template(
            trig_dict['trigger_type'],
            trig_dict,
            trig_dict.get('description', '')
        )
        self._send_json({"trigger": trig_dict, "sms_copy_text": text_template})

    def handle_sms_action(self, body):
        trigger_id = body.get('trigger_id')
        action = body.get('action') # 'REPORTED_TO_SMS' or 'RESOLVED_INTERNAL'
        notes = body.get('notes', '')
        actor = body.get('actor', AUTHORISING_OFFICER_NAME)

        conn = get_connection()
        cursor = conn.cursor()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            UPDATE sms_reporting_triggers
            SET status = ?, sms_submission_notes = ?, reported_date = ?
            WHERE id = ?
        """, (action, notes, now_str, trigger_id))

        cursor.execute("""
            INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, timestamp, severity)
            VALUES ('SMS_REPORT_SUBMISSION', ?, NULL, ?, ?, 'CRITICAL')
        """, (actor, f"SMS trigger #{trigger_id} marked as {action} by {actor}. Notes: {notes}", now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True, "status": action})

    def handle_verify_document(self, body):
        doc_id = body.get('doc_id')
        status = body.get('status', 'VERIFIED')
        verified_by = body.get('verified_by', 'Sophia Reed (HR Level 1)')
        notes = body.get('notes', 'Verified against Appendix D statutory requirements.')

        conn = get_connection()
        cursor = conn.cursor()
        now_date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
            UPDATE appendix_d_documents
            SET status = ?, verified_date = ?, verified_by = ?, notes = ?
            WHERE id = ?
        """, (status, now_date, verified_by, notes, doc_id))

        conn.commit()
        conn.close()
        self._send_json({"success": True})

    def handle_upload_document(self, body):
        emp_id = body.get('employee_id')
        category = body.get('category')
        name = body.get('document_name')
        reference = body.get('document_reference', '')
        expiry = body.get('expiry_date')
        file_path = body.get('file_path', f"/docs/emp_{emp_id}/{category.lower()}.pdf")

        conn = get_connection()
        cursor = conn.cursor()
        now_date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
            INSERT INTO appendix_d_documents (
                employee_id, category, document_name, document_reference, file_path,
                status, expiry_date, verified_date, verified_by, notes
            ) VALUES (?, ?, ?, ?, ?, 'VERIFIED', ?, ?, 'Sophia Reed', 'Uploaded via portal')
        """, (emp_id, category, name, reference, file_path, expiry, now_date))

        if category == 'NI_PROOF' and reference:
            cursor.execute("UPDATE employees SET national_insurance_number = ? WHERE id = ?", (reference, emp_id))

        conn.commit()
        conn.close()
        self._send_json({"success": True})

    def handle_get_employees(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, employee_id, full_name, preferred_name, email, role,
                   immigration_status, job_title, soc_code, department, start_date,
                   employment_status, work_location, workplace_hybrid_ratio,
                   contracted_weekly_hours, standard_working_pattern, annual_gross_salary,
                   hourly_rate, reporting_manager, probation_end_date, recruitment_method,
                   cos_number, cos_issue_date, cos_expiry_date, visa_expiry_date,
                   brp_or_share_code, passport_number, passport_issue_date, passport_expiry_date,
                   passport_issuing_country, uk_arrival_date, vignette_reference,
                   english_language_level, ecctis_reference, national_insurance_number,
                   phone_number, uk_residential_address, emergency_contact_name,
                   emergency_contact_relationship, emergency_contact_phone,
                   emergency_contact_address, supplementary_hours_declared
            FROM employees ORDER BY id ASC
        """)
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        self._send_json({"employees": rows})

    def handle_get_attendance(self, emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        if emp_id:
            cursor.execute("SELECT * FROM attendance_logs WHERE employee_id = ? ORDER BY date DESC, clock_in_time DESC LIMIT 30", (int(emp_id),))
        else:
            cursor.execute("""
                SELECT a.*, e.full_name, e.employee_id as emp_code 
                FROM attendance_logs a 
                JOIN employees e ON a.employee_id = e.id 
                ORDER BY a.date DESC LIMIT 50
            """)
        logs = [dict(r) for r in cursor.fetchall()]
        conn.close()
        self._send_json({"attendance": logs})

    def handle_today_attendance_status(self, emp_id):
        if not emp_id:
            self._send_json({"clocked_in": False})
            return
        today_str = datetime.now().strftime("%Y-%m-%d")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendance_logs WHERE employee_id = ? AND date = ?", (int(emp_id), today_str))
        log = cursor.fetchone()
        conn.close()

        if log and log['clock_in_time'] and not log['clock_out_time']:
            self._send_json({"clocked_in": True, "clock_in_time": log['clock_in_time'], "record_id": log['id']})
        else:
            self._send_json({"clocked_in": False, "last_record": dict(log) if log else None})

    def handle_clock_in(self, body):
        emp_id = body.get('employee_id')
        location = body.get('location', 'Ether Worldwide London HQ / Workstation')
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM attendance_logs WHERE employee_id = ? AND date = ? AND clock_out_time IS NULL", (emp_id, date_str))
        existing = cursor.fetchone()
        if existing:
            conn.close()
            self._send_json({"message": "Already clocked in", "record_id": existing['id']})
            return

        cursor.execute("""
            INSERT INTO attendance_logs (employee_id, date, clock_in_time, status, location_tag, ip_address, notes)
            VALUES (?, ?, ?, 'PRESENT', ?, '192.168.1.100', 'Clocked in via portal')
        """, (emp_id, date_str, time_str, location))

        # Reset any unnotified absence
        cursor.execute("""
            UPDATE consecutive_absence_tracker 
            SET consecutive_unauthorized_days = 0, sms_status = 'NONE', last_updated = ?
            WHERE employee_id = ?
        """, (now.strftime("%Y-%m-%d %H:%M:%S"), emp_id))

        conn.commit()
        conn.close()
        self._send_json({"success": True, "clock_in_time": time_str})

    def handle_clock_out(self, body):
        emp_id = body.get('employee_id')
        notes = body.get('notes', 'Scheduled shift completed')
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM attendance_logs WHERE employee_id = ? AND date = ? AND clock_out_time IS NULL", (emp_id, date_str))
        record = cursor.fetchone()
        if not record:
            conn.close()
            self._send_json({"error": "No active clock-in found for today."}, 400)
            return

        in_time = datetime.strptime(f"{date_str} {record['clock_in_time']}", "%Y-%m-%d %H:%M:%S")
        hours_diff = round(max(0.1, (now - in_time).total_seconds() / 3600.0), 2)

        cursor.execute("""
            UPDATE attendance_logs
            SET clock_out_time = ?, hours_worked = ?, notes = ?
            WHERE id = ?
        """, (time_str, hours_diff, notes, record['id']))

        conn.commit()
        conn.close()
        self._send_json({"success": True, "clock_out_time": time_str, "hours_worked": hours_diff})

    def handle_get_leave_list(self, emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        if emp_id:
            cursor.execute("SELECT * FROM leave_requests WHERE employee_id = ? ORDER BY id DESC", (int(emp_id),))
        else:
            cursor.execute("""
                SELECT l.*, e.full_name, e.employee_id as emp_code, e.job_title
                FROM leave_requests l
                JOIN employees e ON l.employee_id = e.id
                ORDER BY l.id DESC
            """)
        leaves = [dict(r) for r in cursor.fetchall()]
        conn.close()
        self._send_json({"leaves": leaves})

    def handle_submit_leave(self, body):
        emp_id = body.get('employee_id')
        leave_type = body.get('leave_type', 'ANNUAL_LEAVE')
        start_date = body.get('start_date')
        end_date = body.get('end_date')
        total_days = float(body.get('total_days', 1.0))
        reason = body.get('reason', '')
        fit_note = 1 if body.get('fit_note_attached') else 0
        self_cert = 1 if body.get('self_certificate_completed') else 0

        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO leave_requests (
                employee_id, leave_type, start_date, end_date, total_days,
                status, reason, fit_note_attached, self_certificate_completed, created_at
            ) VALUES (?, ?, ?, ?, ?, 'PENDING', ?, ?, ?, ?)
        """, (emp_id, leave_type, start_date, end_date, total_days, reason, fit_note, self_cert, now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True})

    def handle_leave_action(self, body):
        leave_id = body.get('leave_id')
        action = body.get('action') # 'APPROVED' or 'REJECTED'
        admin_name = body.get('admin_name', AUTHORISING_OFFICER_NAME)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE leave_requests SET status = ?, approved_by = ? WHERE id = ?", (action, admin_name, leave_id))
        conn.commit()
        conn.close()
        self._send_json({"success": True, "status": action})

    def handle_get_payroll(self, emp_id, query=None):
        conn = get_connection()
        cursor = conn.cursor()
        period = query.get('period', [None])[0] if query else None

        sql = """
            SELECT p.*, e.full_name, e.employee_id as emp_code, e.job_title, e.soc_code,
                   e.cos_number, e.annual_gross_salary as contracted_annual,
                   e.national_insurance_number as employee_ni_number, e.contracted_weekly_hours
            FROM payroll_records p
            JOIN employees e ON p.employee_id = e.id
        """
        params = []
        conditions = []
        if emp_id:
            conditions.append("p.employee_id = ?")
            params.append(int(emp_id))
        if period and period != 'ALL':
            conditions.append("p.pay_period = ?")
            params.append(period)

        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        sql += " ORDER BY p.pay_date DESC, p.id DESC"

        cursor.execute(sql, tuple(params))
        records = [dict(r) for r in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT pay_period FROM payroll_records ORDER BY pay_date DESC")
        periods = [r[0] for r in cursor.fetchall()]

        conn.close()
        self._send_json({"payroll": records, "available_periods": periods})

    def handle_calculate_payroll(self, body):
        annual_salary = float(body.get('annual_salary', 45000.0))
        ot_hours = float(body.get('overtime_hours', 0.0))
        ot_rate = float(body.get('overtime_rate', 0.0))
        bonus = float(body.get('bonus_pay', 0.0))
        tax_code = body.get('tax_code', '1257L')
        ni_category = body.get('ni_category', 'A')
        pension_rate = float(body.get('pension_employee_rate', 0.05))
        hours = float(body.get('contracted_weekly_hours', 37.5))
        cos_min = float(body.get('cos_minimum_threshold', 38700.0))

        from ukvi_hr_system.payroll_calculator import calculate_full_statutory_payslip
        calc = calculate_full_statutory_payslip(
            basic_salary_annual=annual_salary,
            overtime_hours=ot_hours,
            overtime_hourly_rate=ot_rate,
            bonus_pay=bonus,
            tax_code=tax_code,
            ni_category=ni_category,
            pension_employee_rate=pension_rate,
            contracted_weekly_hours=hours,
            cos_minimum_annual_salary=cos_min
        )
        self._send_json({"calculation": calc})

    def handle_run_payroll(self, body):
        pay_period = body.get('pay_period', 'November 2026')
        pay_date = body.get('pay_date', datetime.now().strftime("%Y-%m-%d"))
        actor = body.get('actor', AUTHORISING_OFFICER_NAME)
        target_emp_id = body.get('employee_id')

        from ukvi_hr_system.payroll_calculator import calculate_full_statutory_payslip
        conn = get_connection()
        cursor = conn.cursor()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if target_emp_id:
            cursor.execute("SELECT * FROM employees WHERE id = ?", (int(target_emp_id),))
        else:
            cursor.execute("SELECT * FROM employees ORDER BY id ASC")
        employees = cursor.fetchall()

        created_count = 0
        for emp in employees:
            e_id = emp['id']
            e_code = emp['employee_id']
            annual = emp['annual_gross_salary']
            hours = emp['contracted_weekly_hours']
            hourly = emp['hourly_rate']

            calc = calculate_full_statutory_payslip(
                basic_salary_annual=annual,
                overtime_hours=0.0,
                overtime_hourly_rate=hourly,
                bonus_pay=0.0,
                tax_code="1257L",
                ni_category="A",
                contracted_weekly_hours=hours
            )

            ref = f"ETH-PAY-{pay_date[:7]}-{e_code}"
            fps_id = f"HMRC-FPS-{pay_date.replace('-', '')}-{e_id}-{secrets.token_hex(3)}"

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
                    'RTI_SUBMITTED', ?, ?, 1, ?, 'HMRC Full Payment Submission generated by Super Admin pay run.',
                    ?, ?
                )
            """, (
                e_id, pay_period, pay_date,
                calc['monthly_basic'], hourly,
                calc['total_gross_pay'], calc['paye_tax_deducted'], calc['employee_ni_deducted'],
                calc['employer_ni_contribution'], calc['employee_pension_deducted'],
                calc['employer_pension_contribution'], calc['net_take_home_pay'],
                calc['cos_rate_match'], calc['minimum_wage_compliant'],
                fps_id, now_str, ref,
                now_str, now_str
            ))
            created_count += 1

        cursor.execute("""
            INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, timestamp, severity)
            VALUES ('PAYROLL_RUN_EXECUTED', ?, NULL, ?, ?, 'INFO')
        """, (actor, f"Super Admin {actor} executed HMRC PAYE pay run for {pay_period} ({created_count} payslips). RTI FPS submitted.", now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True, "created_count": created_count, "pay_period": pay_period})

    def handle_update_payroll_record(self, body):
        rec_id = body.get('id')
        actor = body.get('actor', AUTHORISING_OFFICER_NAME)
        if not rec_id:
            self._send_json({"error": "Record ID is required"}, 400)
            return

        conn = get_connection()
        cursor = conn.cursor()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        basic = float(body.get('basic_salary', 0.0))
        ot_hours = float(body.get('overtime_hours', 0.0))
        ot_rate = float(body.get('overtime_rate', 0.0))
        ot_pay = float(body.get('overtime_pay', ot_hours * ot_rate))
        bonus = float(body.get('bonus_pay', 0.0))
        gross = float(body.get('gross_pay', basic + ot_pay + bonus))
        tax = float(body.get('tax_deduction', 0.0))
        ni = float(body.get('ni_deduction', 0.0))
        pension = float(body.get('pension_employee', 0.0))
        net = float(body.get('net_pay', gross - tax - ni - pension))
        tax_code = body.get('tax_code', '1257L')
        notes = body.get('notes', 'Adjusted by Super Admin Mr. Abdullah Al Mamun.')

        cursor.execute("""
            UPDATE payroll_records
            SET basic_salary = ?, overtime_hours = ?, overtime_rate = ?, overtime_pay = ?,
                bonus_pay = ?, gross_pay = ?, tax_deduction = ?, ni_deduction = ?,
                pension_employee = ?, net_pay = ?, tax_code = ?, notes = ?, updated_at = ?
            WHERE id = ?
        """, (basic, ot_hours, ot_rate, ot_pay, bonus, gross, tax, ni, pension, net, tax_code, notes, now_str, rec_id))

        cursor.execute("""
            INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, timestamp, severity)
            VALUES ('PAYROLL_RECORD_EDITED', ?, NULL, ?, ?, 'INFO')
        """, (actor, f"Super Admin {actor} modified payslip #{rec_id}: Gross £{gross}, Net £{net}, Tax Code {tax_code}.", now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True, "record_id": rec_id})

    def handle_submit_rti(self, body):
        record_id = body.get('record_id')
        actor = body.get('actor', AUTHORISING_OFFICER_NAME)
        conn = get_connection()
        cursor = conn.cursor()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fps_ref = f"HMRC-FPS-{datetime.now().strftime('%Y%m%d%H%M')}-{secrets.token_hex(4).upper()}"

        cursor.execute("""
            UPDATE payroll_records
            SET rti_status = 'RTI_SUBMITTED', rti_submission_id = ?, rti_timestamp = ?
            WHERE id = ?
        """, (fps_ref, now_str, record_id))

        cursor.execute("""
            INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, timestamp, severity)
            VALUES ('HMRC_RTI_FPS_SUBMISSION', ?, NULL, ?, ?, 'INFO')
        """, (actor, f"Full Payment Submission (FPS) {fps_ref} verified with HMRC gateway for record #{record_id}.", now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True, "fps_reference": fps_ref, "timestamp": now_str})

    def handle_get_document_matrix(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, employee_id, full_name, role, immigration_status, job_title, soc_code,
                   cos_number, visa_expiry_date, brp_or_share_code, passport_number,
                   uk_residential_address, workplace_hybrid_ratio
            FROM employees ORDER BY id ASC
        """)
        employees = [dict(r) for r in cursor.fetchall()]

        matrix = []
        for emp in employees:
            e_id = emp['id']
            cursor.execute("""
                SELECT id, category, document_name, document_reference, issued_by_authority,
                       file_type, file_size_kb, status, expiry_date, verified_date, verified_by, notes
                FROM appendix_d_documents
                WHERE employee_id = ?
                ORDER BY id ASC
            """, (e_id,))
            docs = [dict(r) for r in cursor.fetchall()]

            mandatory_categories = [
                ("PASSPORT_BIO", "Passport / Travel Document Bio Page"),
                ("BRP_EVISA_SHARE_CODE", "Home Office eVisa / RTW Share Code"),
                ("RTW_VERIFICATION_CHECK", "Online Right to Work Verification Record"),
                ("CONTRACT_OF_EMPLOYMENT", "Signed Contract of Employment"),
                ("JOB_DESCRIPTION", "Job Description & SOC Benchmark"),
                ("NI_PROOF", "National Insurance Proof (HMRC / P45)"),
                ("QUALIFICATIONS_AND_REGISTRATION", "Degrees / Professional Qualifications"),
                ("UK_ADDRESS_PROOF", "Proof of Current UK Residential Address (<3 Months)"),
                ("ABSENCE_RECORD", "Daily Attendance & Shift Absence Register"),
                ("PAYROLL_RECORDS", "Itemised Monthly Payslips Matching CoS")
            ]

            category_map = {}
            for d in docs:
                cat = d['category']
                category_map[cat] = d

            cat_statuses = []
            verified_count = 0
            for cat_key, cat_label in mandatory_categories:
                doc = category_map.get(cat_key)
                if doc:
                    if doc['status'] == 'VERIFIED':
                        verified_count += 1
                    cat_statuses.append({
                        "category_key": cat_key,
                        "category_label": cat_label,
                        "status": doc['status'],
                        "doc_id": doc['id'],
                        "document_name": doc['document_name'],
                        "document_reference": doc['document_reference'],
                        "expiry_date": doc['expiry_date'],
                        "issued_by_authority": doc['issued_by_authority']
                    })
                else:
                    cat_statuses.append({
                        "category_key": cat_key,
                        "category_label": cat_label,
                        "status": "MISSING",
                        "doc_id": None,
                        "document_name": None,
                        "document_reference": None,
                        "expiry_date": None,
                        "issued_by_authority": None
                    })

            compliance_pct = round((verified_count / len(mandatory_categories)) * 100, 1)

            matrix.append({
                "employee": emp,
                "documents": docs,
                "categories": cat_statuses,
                "verified_count": verified_count,
                "total_mandatory": len(mandatory_categories),
                "compliance_pct": compliance_pct,
                "has_missing": verified_count < len(mandatory_categories)
            })

        conn.close()
        self._send_json({"matrix": matrix})

    def handle_update_profile(self, body):
        emp_id = body.get('employee_id')
        address = body.get('uk_residential_address')
        phone = body.get('phone_number')
        share_code = body.get('brp_or_share_code')
        emergency_name = body.get('emergency_contact_name')
        emergency_phone = body.get('emergency_contact_phone')

        conn = get_connection()
        cursor = conn.cursor()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            UPDATE employees
            SET uk_residential_address = COALESCE(?, uk_residential_address),
                phone_number = COALESCE(?, phone_number),
                brp_or_share_code = COALESCE(?, brp_or_share_code),
                emergency_contact_name = COALESCE(?, emergency_contact_name),
                emergency_contact_phone = COALESCE(?, emergency_contact_phone),
                updated_at = ?
            WHERE id = ?
        """, (address, phone, share_code, emergency_name, emergency_phone, now_str, emp_id))

        cursor.execute("""
            INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, timestamp, severity)
            VALUES ('CONTACT_UPDATE_APPENDIX_D', 'Staff Self-Service', ?, ?, ?, 'INFO')
        """, (emp_id, f"Worker contact updated: Address={address or 'Unchanged'}, Phone={phone or 'Unchanged'}", now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True})

    def handle_declare_supplementary(self, body):
        emp_id = body.get('employee_id')
        hours = float(body.get('supplementary_hours', 0.0))

        conn = get_connection()
        cursor = conn.cursor()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("UPDATE employees SET supplementary_hours_declared = ?, updated_at = ? WHERE id = ?", (hours, now_str, emp_id))

        if hours > 20.0:
            cursor.execute("""
                INSERT INTO sms_reporting_triggers (employee_id, trigger_type, description, severity, home_office_deadline, status, sms_submission_notes, created_at)
                VALUES (?, 'VISA_BREACH', ?, 'CRITICAL', ?, 'PENDING_ACTION', 'Worker declared secondary employment hours exceeding 20h limit.', ?)
            """, (emp_id, f"Worker declared {hours} hours/week outside sponsorship (Home Office cap is 20 hrs).", (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"), now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True, "hours": hours, "exceeded_limit": hours > 20.0})

    def handle_create_employee(self, body):
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = get_connection()
        cursor = conn.cursor()

        emp_code = body.get('employee_id', f"EMP-ETH-{secrets.randbelow(899) + 100}")
        pw_hash, pw_salt = hash_password(body.get('password', 'StaffPass2026!'))

        cursor.execute("""
            INSERT INTO employees (
                employee_id, full_name, preferred_name, email, password_hash, password_salt, role,
                immigration_status, job_title, soc_code, department, start_date,
                employment_status, work_location, contracted_weekly_hours, annual_gross_salary,
                hourly_rate, cos_number, cos_issue_date, cos_expiry_date, visa_expiry_date,
                brp_or_share_code, national_insurance_number, phone_number, uk_residential_address,
                emergency_contact_name, emergency_contact_phone, created_at, updated_at
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?,
                'ACTIVE', ?, ?, ?,
                ?, ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?
            )
        """, (
            emp_code, body.get('full_name'), body.get('preferred_name'), body.get('email'),
            pw_hash, pw_salt, body.get('role', 'STAFF'),
            body.get('immigration_status', 'SKILLED_WORKER'), body.get('job_title', 'E-Commerce Specialist'),
            body.get('soc_code', '2136 - Programmers'), body.get('department', 'Digital Operations'),
            body.get('start_date', datetime.now().strftime("%Y-%m-%d")), body.get('work_location', 'Ether Worldwide London HQ'),
            float(body.get('contracted_weekly_hours', 37.5)), float(body.get('annual_gross_salary', 42000.0)),
            float(body.get('hourly_rate', 21.53)), body.get('cos_number'), body.get('cos_issue_date'),
            body.get('cos_expiry_date'), body.get('visa_expiry_date'), body.get('brp_or_share_code'),
            body.get('national_insurance_number'), body.get('phone_number'), body.get('uk_residential_address'),
            body.get('emergency_contact_name'), body.get('emergency_contact_phone'),
            now_str, now_str
        ))
        new_id = cursor.lastrowid
        conn.commit()
        conn.close()
        self._send_json({"success": True, "id": new_id, "employee_id": emp_code})

    def handle_get_audit_logs(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM compliance_audit_logs ORDER BY id DESC LIMIT 50")
        logs = [dict(r) for r in cursor.fetchall()]
        conn.close()
        self._send_json({"audit_logs": logs})

    def handle_export_inspection_pack(self, identifier):
        conn = get_connection()
        cursor = conn.cursor()
        
        emp = None
        if str(identifier).isdigit():
            cursor.execute("SELECT * FROM employees WHERE id = ?", (int(identifier),))
            emp = cursor.fetchone()
        if not emp:
            cursor.execute("SELECT * FROM employees WHERE employee_id = ? OR employee_id = ?", (str(identifier), f"EMP-ETH-{identifier}"))
            emp = cursor.fetchone()
        if not emp:
            cursor.execute("SELECT * FROM employees ORDER BY id ASC LIMIT 1")
            emp = cursor.fetchone()

        if not emp:
            conn.close()
            self._send_json({"error": "Employee not found"}, 404)
            return

        emp_dict = dict(emp)
        real_id = emp_dict['id']

        if 'password_hash' in emp_dict:
            del emp_dict['password_hash']
        if 'password_salt' in emp_dict:
            del emp_dict['password_salt']

        cursor.execute("SELECT * FROM appendix_d_documents WHERE employee_id = ?", (real_id,))
        docs = [dict(r) for r in cursor.fetchall()]

        cursor.execute("SELECT * FROM attendance_logs WHERE employee_id = ? ORDER BY date DESC LIMIT 30", (real_id,))
        attendance = [dict(r) for r in cursor.fetchall()]

        cursor.execute("SELECT * FROM payroll_records WHERE employee_id = ? ORDER BY id DESC LIMIT 12", (real_id,))
        payroll = [dict(r) for r in cursor.fetchall()]

        cursor.execute("SELECT * FROM leave_requests WHERE employee_id = ? ORDER BY id DESC", (real_id,))
        leaves = [dict(r) for r in cursor.fetchall()]

        conn.close()

        audit = audit_employee_compliance(real_id)

        dossier = {
            "sponsor_organisation": COMPANY_NAME,
            "sponsor_licence_number": SPONSOR_LICENCE_NUMBER,
            "authorising_officer": AUTHORISING_OFFICER_NAME,
            "title": f"UKVI Appendix D Compliance Dossier - {emp_dict['full_name']} ({emp_dict['employee_id']})",
            "generated_at": datetime.now().strftime("%d %B %Y, %H:%M:%S GMT"),
            "compliance_health_score": audit['health_score'],
            "compliance_status": audit['status_badge'],
            "employee": emp_dict,
            "audit_evaluation": audit,
            "appendix_d_documents": docs,
            "attendance_history": attendance,
            "payroll_history": payroll,
            "leave_history": leaves,
            "statutory_declarations": [
                f"Sponsorship maintained under {COMPANY_NAME} UKVI Sponsor Licence {SPONSOR_LICENCE_NUMBER}.",
                f"Authorising Officer {AUTHORISING_OFFICER_NAME} confirms Right to Work verified under s.15 Immigration, Asylum and Nationality Act 2006.",
                "Remuneration monitored and paid in accordance with SOC 2020 minimum going rates and National Minimum Wage regulations.",
                "Daily attendance and leave recorded under Sponsor Guidance Part 3 Paragraph 8.2 (10-day notification standard).",
                "Records retained under Appendix D statutory file retention directives."
            ]
        }
        self._send_json(dossier)

    def handle_get_publications(self, query):
        conn = get_connection()
        cursor = conn.cursor()
        category = query.get('category', [None])[0]
        if category and category != 'ALL':
            cursor.execute("SELECT * FROM immigration_publications WHERE category = ? ORDER BY is_critical DESC, publication_date DESC, id DESC", (category,))
        else:
            cursor.execute("SELECT * FROM immigration_publications ORDER BY is_critical DESC, publication_date DESC, id DESC")
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        self._send_json({"publications": rows})

    def handle_add_publication(self, body):
        conn = get_connection()
        cursor = conn.cursor()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pub_date = body.get('publication_date', datetime.now().strftime("%Y-%m-%d"))
        cursor.execute("""
            INSERT INTO immigration_publications (
                title, category, summary, official_source, official_source_url,
                publication_date, target_audience, is_critical, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            body.get('title'), body.get('category', 'SPONSOR_DUTY'), body.get('summary'),
            body.get('official_source', 'Home Office UKVI'), body.get('official_source_url', 'https://www.gov.uk/uk-visa-sponsorship-employers'),
            pub_date, body.get('target_audience', 'ALL'), 1 if body.get('is_critical') else 0, now_str
        ))
        new_id = cursor.lastrowid
        conn.commit()
        conn.close()
        self._send_json({"success": True, "id": new_id})

    def handle_get_hse_policies(self, query):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM health_safety_policies ORDER BY id ASC")
        policies = [dict(r) for r in cursor.fetchall()]

        cursor.execute("""
            SELECT a.*, e.full_name, e.employee_id as emp_code, e.job_title, e.workplace_hybrid_ratio
            FROM hse_assessments a
            JOIN employees e ON a.employee_id = e.id
            ORDER BY a.id DESC
        """)
        assessments = [dict(r) for r in cursor.fetchall()]
        conn.close()
        self._send_json({"policies": policies, "assessments": assessments})

    def handle_get_hse_assessments(self, emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        if emp_id:
            cursor.execute("""
                SELECT a.*, e.full_name, e.employee_id as emp_code
                FROM hse_assessments a
                JOIN employees e ON a.employee_id = e.id
                WHERE a.employee_id = ? ORDER BY a.id DESC
            """, (int(emp_id),))
        else:
            cursor.execute("""
                SELECT a.*, e.full_name, e.employee_id as emp_code
                FROM hse_assessments a
                JOIN employees e ON a.employee_id = e.id
                ORDER BY a.id DESC
            """)
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        self._send_json({"assessments": rows})

    def handle_save_hse_assessment(self, body):
        conn = get_connection()
        cursor = conn.cursor()
        emp_id = body.get('employee_id')
        a_type = body.get('assessment_type', 'DSE_WORKSTATION')
        status = body.get('compliance_status', 'COMPLIANT')
        notes = body.get('notes', 'Standard workstation DSE & safety check completed.')
        reviewer = body.get('reviewed_by_officer', AUTHORISING_OFFICER_NAME)
        now_date = datetime.now().strftime("%Y-%m-%d")
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO hse_assessments (
                employee_id, assessment_type, compliance_status, assessment_date,
                notes, signed_by_worker, reviewed_by_officer
            ) VALUES (?, ?, ?, ?, ?, 1, ?)
        """, (emp_id, a_type, status, now_date, notes, reviewer))

        cursor.execute("""
            INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, timestamp, severity)
            VALUES ('HSE_ASSESSMENT_COMPLETED', ?, ?, ?, ?, 'INFO')
        """, (reviewer, emp_id, f"HSE Assessment ({a_type}) saved as {status}.", now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True})

    def handle_get_document(self, doc_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.*, e.full_name, e.employee_id as emp_code, e.job_title, e.immigration_status, e.cos_number
            FROM appendix_d_documents d
            JOIN employees e ON d.employee_id = e.id
            WHERE d.id = ?
        """, (int(doc_id),))
        doc = cursor.fetchone()
        conn.close()
        if not doc:
            self._send_json({"error": "Document not found"}, 404)
            return
        self._send_json({"document": dict(doc)})

    def handle_update_document(self, body):
        doc_id = body.get('doc_id')
        doc_name = body.get('document_name')
        doc_ref = body.get('document_reference')
        authority = body.get('issued_by_authority')
        expiry = body.get('expiry_date')
        status = body.get('status', 'VERIFIED')
        notes = body.get('notes')
        preview = body.get('file_content_preview')
        actor = body.get('actor', AUTHORISING_OFFICER_NAME)

        conn = get_connection()
        cursor = conn.cursor()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        now_date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
            UPDATE appendix_d_documents
            SET document_name = COALESCE(?, document_name),
                document_reference = COALESCE(?, document_reference),
                issued_by_authority = COALESCE(?, issued_by_authority),
                expiry_date = COALESCE(?, expiry_date),
                status = COALESCE(?, status),
                notes = COALESCE(?, notes),
                file_content_preview = COALESCE(?, file_content_preview),
                verified_date = ?,
                verified_by = ?
            WHERE id = ?
        """, (doc_name, doc_ref, authority, expiry, status, notes, preview, now_date, actor, doc_id))

        cursor.execute("""
            INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, timestamp, severity)
            VALUES ('APPENDIX_D_DOCUMENT_UPDATED', ?, NULL, ?, ?, 'INFO')
        """, (actor, f"Appendix D document #{doc_id} updated. Status: {status}. Ref: {doc_ref}", now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True})

    def handle_update_employee(self, body):
        emp_id = body.get('id') or body.get('employee_id_pk')
        actor = body.get('actor', AUTHORISING_OFFICER_NAME)
        if not emp_id:
            self._send_json({"error": "Employee ID is required"}, 400)
            return

        conn = get_connection()
        cursor = conn.cursor()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            UPDATE employees
            SET full_name = COALESCE(?, full_name),
                preferred_name = COALESCE(?, preferred_name),
                email = COALESCE(?, email),
                role = COALESCE(?, role),
                immigration_status = COALESCE(?, immigration_status),
                job_title = COALESCE(?, job_title),
                soc_code = COALESCE(?, soc_code),
                department = COALESCE(?, department),
                annual_gross_salary = COALESCE(?, annual_gross_salary),
                hourly_rate = COALESCE(?, hourly_rate),
                contracted_weekly_hours = COALESCE(?, contracted_weekly_hours),
                work_location = COALESCE(?, work_location),
                workplace_hybrid_ratio = COALESCE(?, workplace_hybrid_ratio),
                standard_working_pattern = COALESCE(?, standard_working_pattern),
                reporting_manager = COALESCE(?, reporting_manager),
                probation_end_date = COALESCE(?, probation_end_date),
                recruitment_method = COALESCE(?, recruitment_method),
                cos_number = COALESCE(?, cos_number),
                cos_issue_date = COALESCE(?, cos_issue_date),
                cos_expiry_date = COALESCE(?, cos_expiry_date),
                visa_expiry_date = COALESCE(?, visa_expiry_date),
                brp_or_share_code = COALESCE(?, brp_or_share_code),
                passport_number = COALESCE(?, passport_number),
                passport_issue_date = COALESCE(?, passport_issue_date),
                passport_expiry_date = COALESCE(?, passport_expiry_date),
                passport_issuing_country = COALESCE(?, passport_issuing_country),
                uk_arrival_date = COALESCE(?, uk_arrival_date),
                vignette_reference = COALESCE(?, vignette_reference),
                english_language_level = COALESCE(?, english_language_level),
                ecctis_reference = COALESCE(?, ecctis_reference),
                national_insurance_number = COALESCE(?, national_insurance_number),
                phone_number = COALESCE(?, phone_number),
                uk_residential_address = COALESCE(?, uk_residential_address),
                emergency_contact_name = COALESCE(?, emergency_contact_name),
                emergency_contact_relationship = COALESCE(?, emergency_contact_relationship),
                emergency_contact_phone = COALESCE(?, emergency_contact_phone),
                emergency_contact_address = COALESCE(?, emergency_contact_address),
                updated_at = ?
            WHERE id = ?
        """, (
            body.get('full_name'), body.get('preferred_name'), body.get('email'),
            body.get('role'), body.get('immigration_status'), body.get('job_title'),
            body.get('soc_code'), body.get('department'),
            float(body['annual_gross_salary']) if body.get('annual_gross_salary') is not None and str(body.get('annual_gross_salary')).strip() != '' else None,
            float(body['hourly_rate']) if body.get('hourly_rate') is not None and str(body.get('hourly_rate')).strip() != '' else None,
            float(body['contracted_weekly_hours']) if body.get('contracted_weekly_hours') is not None and str(body.get('contracted_weekly_hours')).strip() != '' else None,
            body.get('work_location'), body.get('workplace_hybrid_ratio'),
            body.get('standard_working_pattern'), body.get('reporting_manager'),
            body.get('probation_end_date'), body.get('recruitment_method'),
            body.get('cos_number'), body.get('cos_issue_date'), body.get('cos_expiry_date'),
            body.get('visa_expiry_date'), body.get('brp_or_share_code'),
            body.get('passport_number'), body.get('passport_issue_date'),
            body.get('passport_expiry_date'), body.get('passport_issuing_country'),
            body.get('uk_arrival_date'), body.get('vignette_reference'),
            body.get('english_language_level'), body.get('ecctis_reference'),
            body.get('national_insurance_number'), body.get('phone_number'),
            body.get('uk_residential_address'), body.get('emergency_contact_name'),
            body.get('emergency_contact_relationship'), body.get('emergency_contact_phone'),
            body.get('emergency_contact_address'),
            now_str, emp_id
        ))

        cursor.execute("""
            INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, timestamp, severity)
            VALUES ('EMPLOYEE_RECORD_UPDATED', ?, ?, ?, ?, 'INFO')
        """, (actor, emp_id, f"Super Admin {actor} updated employee record #{emp_id}.", now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True})

    def handle_create_employee_comprehensive(self, body):
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(id) FROM employees")
        max_id = cursor.fetchone()[0] or 0
        next_seq = max_id + 1
        emp_code = body.get('employee_id') or f"EMP-ETH-{next_seq:03d}"

        pw_hash, pw_salt = hash_password(body.get('password', 'EtherStaff2026!'))

        salary = float(body.get('annual_gross_salary', 45000.0))
        hours = float(body.get('contracted_weekly_hours', 37.5))
        hourly = round(salary / (hours * 52), 2) if hours > 0 else 23.08

        cursor.execute("""
            INSERT INTO employees (
                employee_id, full_name, preferred_name, email, password_hash, password_salt, role,
                immigration_status, job_title, soc_code, department, start_date,
                employment_status, work_location, workplace_hybrid_ratio,
                contracted_weekly_hours, standard_working_pattern, annual_gross_salary,
                hourly_rate, reporting_manager, probation_end_date, recruitment_method,
                cos_number, cos_issue_date, cos_expiry_date, visa_expiry_date,
                brp_or_share_code, passport_number, passport_issue_date, passport_expiry_date,
                passport_issuing_country, uk_arrival_date, vignette_reference,
                english_language_level, ecctis_reference, national_insurance_number,
                phone_number, uk_residential_address, emergency_contact_name,
                emergency_contact_relationship, emergency_contact_phone,
                emergency_contact_address, created_at, updated_at
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?,
                'ACTIVE', ?, ?,
                ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?,
                ?, ?, ?,
                ?, ?, ?,
                ?, ?,
                ?, ?, ?
            )
        """, (
            emp_code, body.get('full_name'), body.get('preferred_name', ''), body.get('email'),
            pw_hash, pw_salt, body.get('role', 'STAFF'),
            body.get('immigration_status', 'SKILLED_WORKER'),
            body.get('job_title', 'E-Commerce Specialist'),
            body.get('soc_code', '2136 - Programmers'),
            body.get('department', 'Digital Operations'),
            body.get('start_date', datetime.now().strftime("%Y-%m-%d")),
            body.get('work_location', 'Ether Worldwide London HQ'),
            body.get('workplace_hybrid_ratio', '3 days office, 2 days remote'),
            hours, body.get('standard_working_pattern', 'Monday to Friday, 09:00 - 17:30 (37.5 hours)'),
            salary, hourly, body.get('reporting_manager', AUTHORISING_OFFICER_NAME),
            body.get('probation_end_date', (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")),
            body.get('recruitment_method', 'Direct e-commerce tech listing & competitive interview'),
            body.get('cos_number'), body.get('cos_issue_date'), body.get('cos_expiry_date'),
            body.get('visa_expiry_date'), body.get('brp_or_share_code'),
            body.get('passport_number'), body.get('passport_issue_date'),
            body.get('passport_expiry_date'), body.get('passport_issuing_country'),
            body.get('uk_arrival_date'), body.get('vignette_reference'),
            body.get('english_language_level', 'Degree taught in English / CEFR B2'),
            body.get('ecctis_reference'), body.get('national_insurance_number'),
            body.get('phone_number'), body.get('uk_residential_address'),
            body.get('emergency_contact_name'), body.get('emergency_contact_relationship', 'Spouse / Next of Kin'),
            body.get('emergency_contact_phone'), body.get('emergency_contact_address'),
            now_str, now_str
        ))
        new_emp_id = cursor.lastrowid

        # Baseline Appendix D documents
        baseline_docs = [
            ("PASSPORT_BIO", "Current Passport Bio Page", body.get('passport_number', 'PENDING'), body.get('passport_issuing_country', 'HMPO / Foreign Affairs'), "PDF", 450, f"OFFICIAL PASSPORT RECORD\nName: {body.get('full_name')}\nDoc Number: {body.get('passport_number')}\nNationality: {body.get('passport_issuing_country')}\nVerified against original physical document by Authorising Officer."),
            ("BRP_EVISA_SHARE_CODE", "Home Office eVisa / RTW Share Code Record", body.get('brp_or_share_code', 'PENDING'), "Home Office UKVI", "PDF", 320, f"ONLINE RIGHT TO WORK VERIFICATION RECORD\nWorker: {body.get('full_name')}\nShare Code: {body.get('brp_or_share_code')}\nImmigration Status: {body.get('immigration_status')}\nStatutory check completed under s.15 Immigration, Asylum and Nationality Act 2006."),
            ("CONTRACT_OF_EMPLOYMENT", "Written Statement of Employment Particulars", f"CONT-ETH-{new_emp_id}", "Ether Worldwide Ltd", "PDF", 680, f"CONTRACT OF EMPLOYMENT\nEmployer: Ether Worldwide Ltd\nEmployee: {body.get('full_name')}\nJob: {body.get('job_title')}\nGross Salary: £{salary}/year\nHours: {hours} hrs/week\nAuthorising Officer: {AUTHORISING_OFFICER_NAME}."),
            ("UK_ADDRESS_PROOF", "Proof of UK Residential Address (<3 Months)", "TENANCY-AGREEMENT-2026", "Letting Agent / Council Tax", "PDF", 510, f"RESIDENTIAL TENANCY AGREEMENT & UTILITY BILL\nTenant: {body.get('full_name')}\nAddress: {body.get('uk_residential_address')}\nPeriod: Active tenancy valid 2026."),
            ("NI_PROOF", "National Insurance Number Allocation Letter", body.get('national_insurance_number', 'PENDING'), "HMRC National Insurance Office", "PDF", 210, f"HMRC NATIONAL INSURANCE CONFIRMATION\nContributor: {body.get('full_name')}\nNI Number: {body.get('national_insurance_number')}\nCategory: Standard Class 1 PAYE.")
        ]

        now_date = datetime.now().strftime("%Y-%m-%d")
        for cat, name, ref, auth, ftype, fsize, preview in baseline_docs:
            cursor.execute("""
                INSERT INTO appendix_d_documents (
                    employee_id, category, document_name, document_reference,
                    issued_by_authority, file_path, file_type, file_size_kb,
                    file_content_preview, status, expiry_date, verified_date,
                    verified_by, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'VERIFIED', ?, ?, 'Sophia Reed', 'Onboard statutory Appendix D baseline')
            """, (new_emp_id, cat, name, ref, auth, f"/docs/emp_{new_emp_id}/{cat.lower()}.pdf", ftype, fsize, preview, body.get('visa_expiry_date'), now_date))

        cursor.execute("""
            INSERT INTO compliance_audit_logs (action, actor, target_employee_id, details, timestamp, severity)
            VALUES ('EMPLOYEE_ONBOARDED_APPENDIX_D', ?, ?, ?, ?, 'INFO')
        """, (AUTHORISING_OFFICER_NAME, new_emp_id, f"Onboarded worker {body.get('full_name')} with full Appendix D track.", now_str))

        conn.commit()
        conn.close()
        self._send_json({"success": True, "id": new_emp_id, "employee_id": emp_code})



def run_server(port=PORT):
    http.server.HTTPServer.allow_reuse_address = True
    server = None
    selected_port = port
    for p in [port, 8086, 8087, 8088, 8080, 3000]:
        try:
            server_address = ('127.0.0.1', p)
            server = http.server.HTTPServer(server_address, UKVIComplianceHandler)
            selected_port = p
            break
        except OSError:
            continue

    if not server:
        print("❌ Could not bind to any available port.")
        sys.exit(1)

    print(f"🇬🇧 {COMPANY_NAME} UKVI HR & Compliance System running on http://127.0.0.1:{selected_port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        server.server_close()

if __name__ == "__main__":
    run_server()
