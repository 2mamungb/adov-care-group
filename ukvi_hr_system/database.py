import sqlite3
import os
import hashlib
import secrets
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "ukvi_compliance_hr.db")
COMPANY_NAME = "Ether Worldwide Ltd"
SPONSOR_LICENCE_NUMBER = "SMS-ETH-882910"
AUTHORISING_OFFICER_NAME = "Mr. Abdullah Al Mamun"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def hash_password(password: str, salt: str = None) -> tuple:
    if not salt:
        salt = secrets.token_hex(16)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    )
    return key.hex(), salt

def verify_password(stored_hash: str, salt: str, password_attempt: str) -> bool:
    attempt_hash, _ = hash_password(password_attempt, salt)
    return secrets.compare_digest(stored_hash, attempt_hash)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Company Profile
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS company_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        trading_name TEXT NOT NULL,
        sponsor_licence_number TEXT UNIQUE NOT NULL,
        licence_tier TEXT NOT NULL DEFAULT 'Worker / Skilled Worker',
        licence_rating TEXT NOT NULL DEFAULT 'Grade A (Premium)',
        authorising_officer TEXT NOT NULL,
        key_contact TEXT NOT NULL,
        registered_address TEXT NOT NULL,
        operating_sector TEXT NOT NULL,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    );
    """)

    # 2. Comprehensive Employee Table (All Statutory Appendix D & HR Compliance Fields)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT UNIQUE NOT NULL,
        full_name TEXT NOT NULL,
        preferred_name TEXT,
        nationality TEXT DEFAULT 'British',
        date_of_birth TEXT,
        gender TEXT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        password_salt TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'STAFF', -- 'SUPER_ADMIN', 'HR_ADMIN', 'STAFF'
        immigration_status TEXT NOT NULL,  -- 'SKILLED_WORKER', 'BRITISH_CITIZEN', 'SETTLED_STATUS', 'STUDENT_VISA'
        job_title TEXT NOT NULL,
        soc_code TEXT NOT NULL,            -- e.g. '2136 - Programmers and software development professionals'
        department TEXT NOT NULL,
        start_date TEXT NOT NULL,
        employment_status TEXT NOT NULL DEFAULT 'ACTIVE', -- 'ACTIVE', 'PROBATION', 'NOTICE', 'SUSPENDED', 'TERMINATED'
        work_location TEXT NOT NULL,
        workplace_hybrid_ratio TEXT DEFAULT '3 Days Office / 2 Days Remote',
        contracted_weekly_hours REAL NOT NULL DEFAULT 37.5,
        standard_working_pattern TEXT DEFAULT 'Mon - Fri, 09:00 - 17:30',
        annual_gross_salary REAL NOT NULL,
        hourly_rate REAL NOT NULL,
        reporting_manager TEXT DEFAULT 'Mr. Abdullah Al Mamun',
        probation_end_date TEXT,
        recruitment_method TEXT DEFAULT 'Direct e-commerce tech listing & competitive interview',
        
        -- Immigration & Right to Work particulars
        cos_number TEXT,
        cos_issue_date TEXT,
        cos_expiry_date TEXT,
        visa_expiry_date TEXT,
        brp_or_share_code TEXT,
        share_code_verified_date TEXT,
        next_rtw_check_due TEXT,
        passport_number TEXT,
        passport_issue_date TEXT,
        passport_expiry_date TEXT,
        passport_issuing_country TEXT,
        uk_arrival_date TEXT,
        vignette_reference TEXT,
        english_language_level TEXT DEFAULT 'Degree level taught in English / CEFR B2',
        ecctis_reference TEXT,
        
        -- Statutory Identity & Residential Contacts
        national_insurance_number TEXT,
        phone_number TEXT,
        uk_residential_address TEXT,
        previous_address_history TEXT,
        emergency_contact_name TEXT,
        emergency_contact_relationship TEXT,
        emergency_contact_phone TEXT,
        emergency_contact_address TEXT,
        dbs_certificate_number TEXT,
        dbs_issue_date TEXT,
        supplementary_hours_declared REAL DEFAULT 0.0,
        failed_login_attempts INTEGER DEFAULT 0,
        account_locked INTEGER DEFAULT 0,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    );
    """)

    # 3. Appendix D Documents Table (with Document Content for QuickLook previewer)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appendix_d_documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        category TEXT NOT NULL, 
        document_name TEXT NOT NULL,
        document_reference TEXT,
        issued_by_authority TEXT DEFAULT 'Official Authority',
        file_path TEXT,
        file_type TEXT DEFAULT 'PDF',
        file_size_kb INTEGER DEFAULT 245,
        file_content_preview TEXT,
        status TEXT NOT NULL DEFAULT 'VERIFIED', -- 'VERIFIED', 'PENDING_REVIEW', 'EXPIRED', 'MISSING'
        expiry_date TEXT,
        verified_date TEXT,
        verified_by TEXT,
        notes TEXT,
        FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
    );
    """)

    # 4. Attendance & Shift Logs Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        clock_in_time TEXT,
        clock_out_time TEXT,
        hours_worked REAL DEFAULT 0.0,
        break_minutes INTEGER DEFAULT 30,
        status TEXT NOT NULL DEFAULT 'PRESENT', -- 'PRESENT', 'LATE', 'HALF_DAY', 'OVERTIME', 'ABSENT'
        location_tag TEXT,
        ip_address TEXT,
        notes TEXT,
        FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
    );
    """)

    # 5. Leave & Absence Requests Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leave_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        leave_type TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        total_days REAL NOT NULL,
        status TEXT NOT NULL DEFAULT 'PENDING',
        reason TEXT,
        fit_note_attached INTEGER DEFAULT 0,
        self_certificate_completed INTEGER DEFAULT 0,
        approved_by TEXT,
        created_at TEXT NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
    );
    """)

    # 6. Consecutive Absence Tracker (SMS 10-Day Rule)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consecutive_absence_tracker (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER UNIQUE NOT NULL,
        consecutive_unauthorized_days INTEGER DEFAULT 0,
        first_absence_date TEXT,
        last_absence_date TEXT,
        sms_status TEXT DEFAULT 'NONE',
        last_updated TEXT NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
    );
    """)

    # 7. HMRC Compliant Payroll Records Table (Real Time Information & PAYE)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payroll_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        tax_year TEXT DEFAULT '2026/27',
        pay_period TEXT NOT NULL,
        pay_date TEXT NOT NULL,
        pay_frequency TEXT DEFAULT 'MONTHLY',
        tax_code TEXT DEFAULT '1257L',
        ni_category TEXT DEFAULT 'A - Standard Rate',
        basic_salary REAL NOT NULL,
        overtime_hours REAL DEFAULT 0.0,
        overtime_rate REAL DEFAULT 0.0,
        overtime_pay REAL DEFAULT 0.0,
        bonus_pay REAL DEFAULT 0.0,
        gross_pay REAL NOT NULL,
        tax_deduction REAL NOT NULL, -- PAYE Income Tax
        ni_deduction REAL NOT NULL,  -- Employee Class 1 Primary NI
        ni_employer REAL DEFAULT 0.0, -- Employer Class 1 Secondary NI
        pension_employee REAL NOT NULL, -- Statutory 5% qualifying
        pension_employer REAL DEFAULT 0.0, -- Statutory 3% qualifying
        student_loan_deduction REAL DEFAULT 0.0,
        net_pay REAL NOT NULL,
        cos_rate_match INTEGER DEFAULT 1,
        minimum_wage_compliant INTEGER DEFAULT 1,
        rti_status TEXT DEFAULT 'RTI_SUBMITTED', -- 'RTI_SUBMITTED', 'PENDING_SUBMISSION'
        rti_submission_id TEXT,
        rti_timestamp TEXT,
        p60_generated INTEGER DEFAULT 0,
        payslip_reference TEXT,
        notes TEXT,
        created_at TEXT,
        updated_at TEXT,
        FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
    );
    """)

    # 8. SMS Reporting Duty Triggers Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sms_reporting_triggers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        trigger_type TEXT NOT NULL,
        description TEXT NOT NULL,
        severity TEXT NOT NULL DEFAULT 'HIGH',
        home_office_deadline TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'PENDING_ACTION',
        sms_submission_notes TEXT,
        reported_date TEXT,
        created_at TEXT NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
    );
    """)

    # 9. Audit Logs Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS compliance_audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT NOT NULL,
        actor TEXT NOT NULL,
        target_employee_id INTEGER,
        details TEXT NOT NULL,
        ip_address TEXT DEFAULT '127.0.0.1',
        timestamp TEXT NOT NULL,
        severity TEXT NOT NULL DEFAULT 'INFO'
    );
    """)

    # 10. Immigration News & Government Publications Feed Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS immigration_publications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT NOT NULL, -- 'SPONSOR_DUTY', 'IMMIGRATION_RULES', 'SMS_SYSTEM', 'WORKER_RIGHTS'
        summary TEXT NOT NULL,
        official_source TEXT NOT NULL,
        official_source_url TEXT NOT NULL,
        publication_date TEXT NOT NULL,
        target_audience TEXT NOT NULL DEFAULT 'ALL', -- 'ALL', 'AUTHORISING_OFFICER', 'SPONSORED_WORKER'
        is_critical INTEGER DEFAULT 0,
        created_at TEXT NOT NULL
    );
    """)

    # 11. Health & Safety (HSE) Policies & Statutory Standards Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS health_safety_policies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        policy_code TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        category TEXT NOT NULL, -- 'OFFICE_DSE', 'WAREHOUSE_ERGONOMICS', 'FIRE_SAFETY', 'FIRST_AID', 'MENTAL_HEALTH'
        legislation_ref TEXT NOT NULL,
        mandatory_for TEXT NOT NULL, -- 'ALL_STAFF', 'TECH_REMOTE', 'LOGISTICS_WAREHOUSE'
        last_reviewed_date TEXT NOT NULL,
        next_review_due TEXT NOT NULL,
        responsible_officer TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'ACTIVE'
    );
    """)

    # 12. HSE Assessments & Worker Declarations Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hse_assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        assessment_type TEXT NOT NULL, -- 'DSE_WORKSTATION', 'MANUAL_HANDLING', 'FIRE_EVACUATION', 'HYBRID_HOME_SAFETY'
        compliance_status TEXT NOT NULL DEFAULT 'COMPLIANT', -- 'COMPLIANT', 'NEEDS_ADJUSTMENT'
        assessment_date TEXT NOT NULL,
        notes TEXT,
        signed_by_worker INTEGER DEFAULT 1,
        reviewed_by_officer TEXT,
        FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
    );
    """)

    # 13. Active Sessions Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS auth_sessions (
        session_token TEXT PRIMARY KEY,
        employee_id INTEGER NOT NULL,
        created_at TEXT NOT NULL,
        expires_at TEXT NOT NULL,
        is_revoked INTEGER DEFAULT 0,
        FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
    );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database schema successfully expanded with comprehensive Appendix D, Immigration Publications, and HSE compliance tables.")
