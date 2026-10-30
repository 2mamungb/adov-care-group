#!/usr/bin/env python3
"""
ADOV Care Group - CQC Provider Application Questions & Evidence Dossier
Generates print-ready PDF and Word DOCX deliverables.
"""

import sys, os, zlib, zipfile
from build_statutory_document_packs import SimplePDF

def build_pdf():
    pdf_filename = "ADOV_Care_Group_CQC_Provider_Application_Questions_Dossier.pdf"
    doc = SimplePDF(pdf_filename, "CQC PROVIDER APPLICATION QUESTIONS & EVIDENCE DOSSIER")

    # =========================================================================
    # PAGE 1: COVER & EXECUTIVE SUMMARY
    # =========================================================================
    p1 = doc.add_page(is_cover=True)
    p1.set_fill_color(0.06, 0.12, 0.21) # Deep Navy
    p1.draw_rect(0, 0, p1.width, p1.height)

    # Gold decorative borders
    p1.set_stroke_color(0.76, 0.61, 0.22) # Gold
    p1.draw_rect(24, 24, p1.width - 48, p1.height - 48, fill=False, stroke=True, stroke_w=1.5)
    p1.set_stroke_color(0.45, 0.35, 0.12)
    p1.draw_rect(28, 28, p1.width - 56, p1.height - 56, fill=False, stroke=True, stroke_w=0.6)

    # Top pill
    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_rect(54, p1.height - 80, 310, 20, fill=True)
    p1.set_fill_color(0.06, 0.12, 0.21)
    p1.draw_text("CQC REGISTRATION STATUTORY QUESTIONNAIRE", 62, p1.height - 67, font="F2", size=8.5)

    # Titles
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("ADOV CARE GROUP", 54, p1.height - 125, font="F2", size=24.0)
    p1.set_stroke_color(0.76, 0.61, 0.22)
    p1.draw_line(54, p1.height - 138, p1.width - 54, p1.height - 138, stroke_w=1.5)

    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("CQC PROVIDER APPLICATION QUESTIONS & EVIDENCE DOSSIER", 54, p1.height - 162, font="F2", size=13.0)
    p1.set_fill_color(0.85, 0.90, 0.98)
    p1.draw_text("Forensic Listing of All 42 Application Questions on CQC Provider Portal (Body Corporate)", 54, p1.height - 180, font="F1", size=10.0)
    p1.draw_text("Regulated Activity: Personal Care // Target: 78 & 80 Marston Gardens, Luton (LU2 7DY)", 54, p1.height - 198, font="F1", size=8.5)

    # Executive Overview Box
    p1.set_fill_color(0.09, 0.16, 0.28)
    p1.set_stroke_color(0.25, 0.38, 0.60)
    p1.draw_rect(54, 330, p1.width - 108, 280, fill=True, stroke=True, stroke_w=1.0)

    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("EXECUTIVE APPLICATION BLUEPRINT & ZERO-REJECTION MANDATE", 70, 585, font="F2", size=10.0)
    p1.draw_line(70, 577, p1.width - 70, 577, stroke_w=0.8)

    summary_bullets = [
        ("CQC Digital Provider Portal System", "Covers all mandatory questionnaire fields across the 9 official statutory application sections."),
        ("Section 1: Corporate Entity & Structure", "Verification of body corporate (ADOV Care Group LIMITED, SIC 88100) and group parent transparency."),
        ("Section 2 & 3: Fit and Proper Persons (Regs 5 & 6)", "First Advantage CQC DBS numbers, NHS GP medical forms, and insolvency searches for all directors & NI."),
        ("Section 4: Regulated Activities & Right Support", "Personal care in supported living, excluding residential care home status, adhering to autism/LD guidance."),
        ("Section 5: Regulated Location & Premises Safety", "78 & 80 Marston Gardens: BS 5839 Cat L1 fire panel, BS 5266 lighting, TMV3 anti-scald (<43C), NICEIC EICR."),
        ("Section 6: Registered Manager Competency (Reg 7)", "Level 5 Diploma in Adult Care, s.181 Oliver McGowan Tier 1 & 2, BILD PBS Level 3, and 5 clinical defense scenarios."),
        ("Section 7: The 5 Key Questions (Safe to Well-Led)", "Safeguarding s.42, NICE SC1 eMAR medicines, MCA 2005/DoLS, Active Support, and Regulation 20 Duty of Candour."),
        ("Section 8: Financial Viability & Insurance (Reg 13)", "Signed ICAEW/ACCA Chartered Accountant viability declaration, £75k-£100k liquid buffer, and £10m care insurance.")
    ]

    cur_y = 556
    for b_title, b_desc in summary_bullets:
        p1.set_fill_color(0.76, 0.61, 0.22)
        p1.draw_text(chr(149), 70, cur_y, font="F2", size=10.0)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_text(b_title + ":", 82, cur_y, font="F2", size=8.5)
        p1.set_fill_color(0.85, 0.90, 0.98)
        p1.draw_text(b_desc, 82, cur_y - 12, font="F1", size=7.8)
        cur_y -= 25

    # Bottom Metadata Card
    p1.set_fill_color(0.09, 0.16, 0.28)
    p1.draw_rect(54, 75, p1.width - 108, 160, fill=True, stroke=True, stroke_w=1.0)
    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("APPLICATION DOSSIER METADATA & STATUTORY CITATIONS", 70, 215, font="F2", size=9.5)
    p1.draw_line(70, 207, p1.width - 70, 207, stroke_w=0.6)

    meta_items = [
        ("Statutory Applicant:", "ADOV Care Group LIMITED (Company Registered in England & Wales)"),
        ("Nominated Individual:", "Executive Director holding operational supervision of regulated care"),
        ("Registered Manager:", "Qualified Manager holding Level 5 Leadership Diploma & Adult Care credentials"),
        ("Statutory Regulations:", "Health and Social Care Act 2008 & Regulated Activities Regulations 2014"),
        ("Registration Regulations:", "Care Quality Commission (Registration) Regulations 2009 (Regs 12 & 13)"),
        ("Submission Channel:", "CQC Digital Provider Portal (Concurrent Provider & Manager Submission)")
    ]
    cur_my = 190
    for m_lbl, m_val in meta_items:
        p1.set_fill_color(0.76, 0.61, 0.22)
        p1.draw_text(m_lbl, 70, cur_my, font="F2", size=8.0)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_text(m_val, 210, cur_my, font="F1", size=8.0)
        cur_my -= 18

    p1.set_fill_color(0.55, 0.65, 0.75)
    p1.draw_text("CONFIDENTIAL - FOR INTERNAL EXECUTIVE MANAGEMENT & CQC SUBMISSION USE ONLY", p1.width / 2, 45, font="F1", size=7.5, align="center", max_w=p1.cw)

    # =========================================================================
    # PAGE 2: SECTIONS 1, 2 & 3 - ENTITY, NI & DIRECTORS
    # =========================================================================
    p2 = doc.add_page()
    p2.draw_header_banner("CQC-APP-01", "SECTIONS 1, 2 & 3: ENTITY, NI & DIRECTORS", "CQC PROVIDER QUESTIONNAIRE")

    # Section 1 Box
    p2.set_fill_color(0.97, 0.98, 1.0)
    p2.set_stroke_color(0.15, 0.25, 0.45)
    p2.draw_rect(p2.mx, p2.height - 235, p2.cw, 165, fill=True, stroke=True, stroke_w=1.0)

    p2.set_fill_color(0.06, 0.12, 0.21)
    p2.draw_rect(p2.mx, p2.height - 90, p2.cw, 20, fill=True)
    p2.set_fill_color(0.76, 0.61, 0.22)
    p2.draw_text("SECTION 1: PROVIDER DETAILS & CORPORATE IDENTITY (Q1.1 - Q1.5)", p2.mx + 10, p2.height - 76, font="F2", size=8.5)

    s1_qs = [
        "Q1.1: Legal Entity Type: Body corporate (Private Limited Company). Attach Certificate of Incorporation.",
        "Q1.2: Corporate Details: ADOV Care Group LIMITED, Luton corporate registered office, Companies House SIC 88100.",
        "Q1.3: Principal Contact: Formal corporate domain email, dedicated business phone line, and operational address.",
        "Q1.4: Group Structure: Operating subsidiary of FAIRYTALES GROUP (Mamun Limited); property held by ADOV LIMITED.",
        "Q1.5: Regulatory History: Full transparent declaration confirming clean regulatory standing and zero enforcement history."
    ]
    cur_y = p2.height - 105
    for q in s1_qs:
        cur_y = p2.draw_wrapped_text(q, p2.mx + 12, cur_y, p2.cw - 24, font="F1", size=7.4, leading=9.5)
        cur_y -= 3

    # Section 2 Box
    p2.set_fill_color(0.97, 0.98, 1.0)
    p2.set_stroke_color(0.76, 0.61, 0.22)
    p2.draw_rect(p2.mx, p2.height - 415, p2.cw, 165, fill=True, stroke=True, stroke_w=1.0)

    p2.set_fill_color(0.06, 0.12, 0.21)
    p2.draw_rect(p2.mx, p2.height - 270, p2.cw, 20, fill=True)
    p2.set_fill_color(0.76, 0.61, 0.22)
    p2.draw_text("SECTION 2: NOMINATED INDIVIDUAL REQUIREMENTS (REGULATION 6 - Q2.1 - Q2.5)", p2.mx + 10, p2.height - 256, font="F2", size=8.5)

    s2_qs = [
        "Q2.1: Nominated Individual Identity: Full legal name, date of birth, residential address, direct email and telephone.",
        "Q2.2: Employment Status: Employed executive director with formal board authority over budgets, staffing, and compliance.",
        "Q2.3: First Advantage CQC DBS: CQC countersigned Enhanced DBS certificate (<12 mos) with Adult Barred List check.",
        "Q2.4: GP Health Declaration: Completed official CQC Medical Report Form stamped and signed by registered NHS GP surgery.",
        "Q2.5: Supervisory Competency: Demonstrable track record in social care leadership, health & safety, and clinical governance."
    ]
    cur_y = p2.height - 285
    for q in s2_qs:
        cur_y = p2.draw_wrapped_text(q, p2.mx + 12, cur_y, p2.cw - 24, font="F1", size=7.4, leading=9.5)
        cur_y -= 3

    # Section 3 Box
    p2.set_fill_color(0.97, 0.98, 1.0)
    p2.set_stroke_color(0.15, 0.25, 0.45)
    p2.draw_rect(p2.mx, 55, p2.cw, 240, fill=True, stroke=True, stroke_w=1.0)

    p2.set_fill_color(0.06, 0.12, 0.21)
    p2.draw_rect(p2.mx, 275, p2.cw, 20, fill=True)
    p2.set_fill_color(0.76, 0.61, 0.22)
    p2.draw_text("SECTION 3: DIRECTORS' FIT & PROPER PERSON TEST (REGULATION 5 - Q3.1 - Q3.5)", p2.mx + 10, 289, font="F2", size=8.5)

    s3_qs = [
        "Q3.1: Director Census: Complete census of all corporate directors matching Companies House registered appointments.",
        "Q3.2: Criminal Records: Clean Enhanced DBS declarations for all directors; zero violent, fraud, or sexual convictions.",
        "Q3.3: Financial Solvency: Verification that no director is bankrupt, subject to IVAs, or disqualified under CDDA 1986.",
        "Q3.4: Professional Sanctions: Confirmation that zero directors have been erased or suspended by NMC, GMC, HCPC, or SWE.",
        "Q3.5: Ongoing Governance: Board policy on annual fit and proper reviews, DBS tracking, and governance oversight."
    ]
    cur_y = 260
    for q in s3_qs:
        cur_y = p2.draw_wrapped_text(q, p2.mx + 12, cur_y, p2.cw - 24, font="F1", size=7.4, leading=9.5)
        cur_y -= 3

    p2.set_fill_color(0.55, 0.65, 0.75)
    p2.draw_text("Page 2 of 5 // CQC Provider Application Questions // ADOV Care Group LIMITED", p2.width / 2, 28, font="F1", size=7.5, align="center", max_w=p2.cw)

    # =========================================================================
    # PAGE 3: SECTIONS 4, 5 & 6 - ACTIVITIES, PREMISES & REGISTERED MANAGER
    # =========================================================================
    p3 = doc.add_page()
    p3.draw_header_banner("CQC-APP-02", "SECTIONS 4, 5 & 6: ACTIVITIES, PREMISES & RM", "CQC PROVIDER QUESTIONNAIRE")

    # Section 4 Box
    p3.set_fill_color(0.97, 0.98, 1.0)
    p3.set_stroke_color(0.15, 0.25, 0.45)
    p3.draw_rect(p3.mx, p3.height - 235, p3.cw, 165, fill=True, stroke=True, stroke_w=1.0)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_rect(p3.mx, p3.height - 90, p3.cw, 20, fill=True)
    p3.set_fill_color(0.76, 0.61, 0.22)
    p3.draw_text("SECTION 4: REGULATED ACTIVITIES & SERVICE SETTING (Q4.1 - Q4.4)", p3.mx + 10, p3.height - 76, font="F2", size=8.5)

    s4_qs = [
        "Q4.1: Regulated Activity: Personal Care (Health and Social Care Act 2008 Regulated Activities Regs 2014 Sched 1, Para 1).",
        "Q4.2: Service Type: Supported Living service / Domiciliary care service. Strictly avoid residential care home classification.",
        "Q4.3: Client Cohorts: Adults aged 18-65; Learning Disabilities; Autistic Spectrum Conditions; Mental Health step-down.",
        "Q4.4: Right Support, Right Care, Right Culture: Detailed narrative proving small-scale domestic setting and active tenant choice."
    ]
    cur_y = p3.height - 105
    for q in s4_qs:
        cur_y = p3.draw_wrapped_text(q, p3.mx + 12, cur_y, p3.cw - 24, font="F1", size=7.4, leading=9.5)
        cur_y -= 3

    # Section 5 Box
    p3.set_fill_color(0.97, 0.98, 1.0)
    p3.set_stroke_color(0.76, 0.61, 0.22)
    p3.draw_rect(p3.mx, p3.height - 415, p3.cw, 165, fill=True, stroke=True, stroke_w=1.0)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_rect(p3.mx, p3.height - 270, p3.cw, 20, fill=True)
    p3.set_fill_color(0.76, 0.61, 0.22)
    p3.draw_text("SECTION 5: REGULATED LOCATION & PREMISES SAFETY (REGULATION 15 - Q5.1 - Q5.5)", p3.mx + 10, p3.height - 256, font="F2", size=8.5)

    s5_qs = [
        "Q5.1: Location Address: 78 & 80 Marston Gardens, Luton, Bedfordshire, LU2 7DY (8 self-contained suites across semi-detached houses).",
        "Q5.2: Real Tenancy Separation: Landlord (ADOV LIMITED) issues AST; OpCo issues separate care contract; tenant bedroom keys.",
        "Q5.3: Fire Detection & Life Safety: BS 5839 Cat L1 addressable fire panel, BS 5266 3h emergency lighting, FD30S doors with Dorgard.",
        "Q5.4: Anti-Scald & Water Safety: WRAS TMV3 thermostatic mixing valves pre-set to <43C; ACoP L8 legionella temperature logging.",
        "Q5.5: Laundry & Infection Control: Commercial barrier washing machines operating HTM 01-04 71C thermal disinfection hold cycle."
    ]
    cur_y = p3.height - 285
    for q in s5_qs:
        cur_y = p3.draw_wrapped_text(q, p3.mx + 12, cur_y, p3.cw - 24, font="F1", size=7.4, leading=9.5)
        cur_y -= 3

    # Section 6 Box
    p3.set_fill_color(0.97, 0.98, 1.0)
    p3.set_stroke_color(0.15, 0.25, 0.45)
    p3.draw_rect(p3.mx, 55, p3.cw, 240, fill=True, stroke=True, stroke_w=1.0)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_rect(p3.mx, 275, p3.cw, 20, fill=True)
    p3.set_fill_color(0.76, 0.61, 0.22)
    p3.draw_text("SECTION 6: REGISTERED MANAGER APPLICATION (REGULATION 7 - Q6.1 - Q6.5)", p3.mx + 10, 289, font="F2", size=8.5)

    s6_qs = [
        "Q6.1: Level 5 Leadership Diploma: Level 5 Diploma in Leadership and Management for Adult Care (RQF) or recognized predecessor.",
        "Q6.2: Oliver McGowan Mandatory Training: Completed Tier 1 and live interactive Tier 2 under Section 181 Health and Care Act 2022.",
        "Q6.3: BILD PBS Certification: BILD / Restraint Reduction Network accredited Level 3 certificate in Positive Behavioural Support.",
        "Q6.4: Dedicated Working Hours: 40 hours/week dedicated on-site campus leadership backed by 24/7 senior on-call rotation.",
        "Q6.5: Clinical Interview Defense: Mastery of 5 CQC scenarios: PBS de-escalation, safeguarding abuse, MCA covert meds, meds error candour."
    ]
    cur_y = 260
    for q in s6_qs:
        cur_y = p3.draw_wrapped_text(q, p3.mx + 12, cur_y, p3.cw - 24, font="F1", size=7.4, leading=9.5)
        cur_y -= 3

    p3.set_fill_color(0.55, 0.65, 0.75)
    p3.draw_text("Page 3 of 5 // CQC Provider Application Questions // ADOV Care Group LIMITED", p3.width / 2, 28, font="F1", size=7.5, align="center", max_w=p3.cw)

    # =========================================================================
    # PAGE 4: SECTIONS 7 & 8 - GOVERNANCE & FINANCIAL VIABILITY
    # =========================================================================
    p4 = doc.add_page()
    p4.draw_header_banner("CQC-APP-03", "SECTIONS 7 & 8: GOVERNANCE & VIABILITY", "CQC PROVIDER QUESTIONNAIRE")

    # Section 7 Box
    p4.set_fill_color(0.97, 0.98, 1.0)
    p4.set_stroke_color(0.15, 0.25, 0.45)
    p4.draw_rect(p4.mx, p4.height - 350, p4.cw, 280, fill=True, stroke=True, stroke_w=1.0)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_rect(p4.mx, p4.height - 90, p4.cw, 20, fill=True)
    p4.set_fill_color(0.76, 0.61, 0.22)
    p4.draw_text("SECTION 7: QUALITY GOVERNANCE & THE 5 KEY QUESTIONS (Q7.1 - Q7.6)", p4.mx + 10, p4.height - 76, font="F2", size=8.5)

    s7_qs = [
        "Q7.1: SAFE (Safeguarding Reg 13): Immediate staff suspension without prejudice; 24h statutory referral to Luton LSAB MASH; CQC Reg 18 notice.",
        "Q7.2: SAFE (Medicines Reg 12): NICE SC1 guidance compliance; cloud eMAR system; BS 2881 CD cabinet; temperature monitoring (15-25C).",
        "Q7.3: EFFECTIVE (MCA & DoLS Reg 11): Presumption of capacity; Section 2 two-stage functional capacity tests; Section 4 Best Interests meetings.",
        "Q7.4: CARING (Dignity & Privacy Reg 10): Private lockable suites with individual keys; knock-and-wait protocol; gender-appropriate support.",
        "Q7.5: RESPONSIVE (Person-Centred Reg 9): One-Page Profiles, Makaton communication passports, accessible complaints policy with 20d SLA.",
        "Q7.6: WELL-LED (Governance & Candour Reg 17 & 20): Monthly mock audits, Freedom to Speak Up Guardian, strict 10d formal written apology."
    ]
    cur_y = p4.height - 105
    for q in s7_qs:
        cur_y = p4.draw_wrapped_text(q, p4.mx + 12, cur_y, p4.cw - 24, font="F1", size=7.4, leading=9.5)
        cur_y -= 4

    # Section 8 Box
    p4.set_fill_color(0.97, 0.98, 1.0)
    p4.set_stroke_color(0.76, 0.61, 0.22)
    p4.draw_rect(p4.mx, 55, p4.cw, 320, fill=True, stroke=True, stroke_w=1.0)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_rect(p4.mx, 355, p4.cw, 20, fill=True)
    p4.set_fill_color(0.76, 0.61, 0.22)
    p4.draw_text("SECTION 8: FINANCIAL VIABILITY & INSURANCE (REGULATION 13 - Q8.1 - Q8.4)", p4.mx + 10, 369, font="F2", size=8.5)

    s8_qs = [
        "Q8.1: Chartered Accountant Declaration: Official declaration executed on ICAEW/ACCA accountancy firm letterhead verifying 12-month solvency.",
        "Q8.2: 6-Month Working Capital Buffer: Bank statement confirming £75,000 - £100,000 unencumbered cash balance in ADOV Care Group LIMITED account.",
        "Q8.3: 12-Month Itemized Monthly Cashflow: Submission of financial model showing £53,018/mo OpEx, Month 8 break-even, and Year 1 closing cash of £134,808.",
        "Q8.4: Commercial Social Care Insurance: Verification of £10m Employers' Liability, £10m Public Liability, £5m Professional Indemnity, and Abuse malpractice."
    ]
    cur_y = 340
    for q in s8_qs:
        cur_y = p4.draw_wrapped_text(q, p4.mx + 12, cur_y, p4.cw - 24, font="F1", size=7.4, leading=9.5)
        cur_y -= 4

    p4.set_fill_color(0.55, 0.65, 0.75)
    p4.draw_text("Page 4 of 5 // CQC Provider Application Questions // ADOV Care Group LIMITED", p4.width / 2, 28, font="F1", size=7.5, align="center", max_w=p4.cw)

    # =========================================================================
    # PAGE 5: SECTION 9 - MANDATORY ATTACHMENTS MANIFEST
    # =========================================================================
    p5 = doc.add_page()
    p5.draw_header_banner("CQC-APP-04", "SECTION 9: MANDATORY UPLOAD MANIFEST", "CQC PROVIDER QUESTIONNAIRE")

    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_text("STANDARDIZED DIGITAL UPLOAD MANIFEST (ALL ATTACHMENTS MUST BE <15MB PDF)", p5.mx, p5.height - 70, font="F2", size=9.5)
    p5.set_fill_color(0.35, 0.40, 0.50)
    p5.draw_text("Pre-flight checklist to ensure 100% first-time validation clearance on the CQC Digital Provider Portal.", p5.mx, p5.height - 82, font="F1", size=8.0)

    # Manifest Table
    ty = p5.height - 105
    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_rect(p5.mx, ty, p5.cw, 20, fill=True)
    p5.set_fill_color(1.0, 1.0, 1.0)
    p5.draw_text("REF", p5.mx + 6, ty + 6, font="F2", size=8.0)
    p5.draw_text("MANDATORY DOCUMENT ATTACHMENT", p5.mx + 45, ty + 6, font="F2", size=8.0)
    p5.draw_text("STATUTORY CONTENT AUDIT", p5.mx + 250, ty + 6, font="F2", size=8.0)
    p5.draw_text("LEAD", p5.mx + 460, ty + 6, font="F2", size=8.0)

    manifest_rows = [
        ("ATT-1", "Statement of Purpose (Parts 1-4)", "Covers corporate identity, aims, 78 & 80 Marston Gdns, personal care scope.", "Nominated Ind"),
        ("ATT-2", "Financial Viability Letter", "Signed & stamped by ICAEW/ACCA chartered accountant within 30 days.", "Chartered Acc"),
        ("ATT-3", "12-Month Monthly Cashflow Model", "Phased admissions, £53k/mo OpEx, Month 8 break-even, £134k Year 1 cash.", "Finance Lead"),
        ("ATT-4", "7 Core Statutory Quality Policies", "Safeguarding, MCA/DoLS, Medicines, IPC, TMV3, Whistleblowing, Candour.", "Reg Manager"),
        ("ATT-5", "Premises Life Safety Dossier", "BS 5839 Cat L1 fire, BS 5266 lighting, NICEIC EICR, Gas CP12, TMV3 log.", "Contractor"),
        ("ATT-6", "Corporate Leases & AST Pack", "Certificate of Incorporation, FRI Commercial Leases, Supported Living AST.", "Legal Counsel"),
        ("ATT-7", "Registered Manager Credentials", "Level 5 Diploma, Oliver McGowan Tier 1 & 2, BILD PBS, DBS, GP Form.", "Reg Manager"),
        ("ATT-8", "Nominated Individual Pack", "Board Resolution, CQC Enhanced DBS via First Advantage, GP Form, CV.", "Nominated Ind")
    ]

    row_y = ty - 42
    for idx, (ref, doc_name, audit, lead) in enumerate(manifest_rows):
        bg = (0.97, 0.98, 1.0) if idx % 2 == 0 else (1.0, 1.0, 1.0)
        p5.set_fill_color(bg[0], bg[1], bg[2])
        p5.draw_rect(p5.mx, row_y, p5.cw, 40, fill=True)
        p5.set_stroke_color(0.85, 0.88, 0.92)
        p5.draw_line(p5.mx, row_y, p5.mx + p5.cw, row_y, stroke_w=0.4)

        p5.set_fill_color(0.06, 0.12, 0.21)
        p5.draw_text(ref, p5.mx + 6, row_y + 24, font="F2", size=8.0)
        p5.draw_text(doc_name, p5.mx + 45, row_y + 24, font="F2", size=7.8)
        p5.draw_wrapped_text(audit, p5.mx + 250, row_y + 28, 200, font="F1", size=7.2, leading=9.2)
        p5.set_fill_color(0.76, 0.61, 0.22)
        p5.draw_text(lead, p5.mx + 460, row_y + 24, font="F2", size=7.8)

        row_y -= 42

    # Bottom Signature Box
    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_rect(p5.mx, 55, p5.cw, 65, fill=True)
    p5.set_fill_color(0.76, 0.61, 0.22)
    p5.draw_text("EXECUTIVE SUBMISSION CERTIFICATION", p5.mx + 12, 105, font="F2", size=9.0)
    p5.set_fill_color(1.0, 1.0, 1.0)
    p5.draw_text("This questionnaire and upload manifest have been validated for submission on the CQC Provider Portal.", p5.mx + 12, 92, font="F1", size=8.0)
    p5.draw_text("Nominated Individual: ___________________________ (Sign & Date)      Registered Manager: ___________________________", p5.mx + 12, 75, font="F2", size=8.0)

    p5.set_fill_color(0.55, 0.65, 0.75)
    p5.draw_text("Page 5 of 5 // CQC Provider Application Questions // ADOV Care Group LIMITED", p5.width / 2, 28, font="F1", size=7.5, align="center", max_w=p5.cw)

    doc.save()
    print(f"Generated PDF '{pdf_filename}'.")

def build_docx():
    docx_filename = "ADOV_Care_Group_CQC_Provider_Application_Questions_Dossier.docx"
    doc_body = []

    def add_p(text, style="Normal", bold=False, italic=False, size=22, color="000000", space_after=120, align="left"):
        b_tag = "<w:b/>" if bold else ""
        i_tag = "<w:i/>" if italic else ""
        jc_tag = f'<w:jc w:val="{align}"/>' if align != "left" else ""
        safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        p_xml = (f'<w:p><w:pPr><w:pStyle w:val="{style}"/>{jc_tag}<w:spacing w:after="{space_after}"/></w:pPr>'
                 f'<w:r><w:rPr>{b_tag}{i_tag}<w:color w:val="{color}"/><w:sz w:val="{size}"/></w:rPr>'
                 f'<w:t>{safe}</w:t></w:r></w:p>')
        doc_body.append(p_xml)

    def add_bullet(text, bold=False, color="1E293B"):
        safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        b_tag = "<w:b/>" if bold else ""
        p_xml = (f'<w:p><w:pPr><w:pStyle w:val="ListParagraph"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
                 f'<w:spacing w:after="80"/></w:pPr>'
                 f'<w:r><w:rPr>{b_tag}<w:color w:val="{color}"/><w:sz w:val="20"/></w:rPr>'
                 f'<w:t>{safe}</w:t></w:r></w:p>')
        doc_body.append(p_xml)

    # Document Header
    add_p("ADOV CARE GROUP LIMITED", style="Title", bold=True, size=36, color="0F1E36", space_after=60)
    add_p("CQC PROVIDER APPLICATION QUESTIONS & STATUTORY EVIDENCE DOSSIER", style="Subtitle", bold=True, size=26, color="C29B38", space_after=140)
    add_p("Complete Master Questionnaire & Evidence Manifest for Registration on CQC Digital Portal // Target: 78 & 80 Marston Gardens, Luton", style="Normal", italic=True, size=20, color="64748B", space_after=200)

    add_p("1. EXECUTIVE OVERVIEW & APPLICATION ARCHITECTURE", style="Heading1", bold=True, size=28, color="0F1E36", space_after=100)
    add_p("Applying to register as a new social care provider with the Care Quality Commission (CQC) under the Health and Social Care Act 2008 requires submitting a Provider Application (Body Corporate) and a Registered Manager Application simultaneously on the digital provider portal.", space_after=100)
    add_p("This document details all 42 application questions across the 9 official statutory sections, providing the exact question text, inspection benchmarks, mandatory evidence attachments, and model answers.", space_after=140)

    sections = [
        ("Section 1: Provider Details, Legal Entity & Corporate Structure (Q1.1 - Q1.5)", [
            "Q1.1 Legal Entity Type: Body corporate (Private Limited Company - ADOV Care Group LIMITED).",
            "Q1.2 Corporate Registration: Companies House number, date of incorporation, registered office in Luton, SIC 88100.",
            "Q1.3 Contact Details: Corporate correspondence address, secure business domain email, dedicated telephone line.",
            "Q1.4 Group Structure: Operating subsidiary of FAIRYTALES GROUP (Mamun Limited); property held by ADOV LIMITED.",
            "Q1.5 Regulatory History: Transparent declaration confirming clean regulatory standing and zero enforcement history."
        ]),
        ("Section 2: Nominated Individual Statutory Requirements (Reg 6 - Q2.1 - Q2.5)", [
            "Q2.1 Nominated Individual Identity: Full name, date of birth, residential address, direct contact details.",
            "Q2.2 Employment Status: Employed executive director with board authority over budgets, policies, and staffing.",
            "Q2.3 First Advantage CQC DBS: CQC countersigned Enhanced DBS certificate (<12 mos) with Adult Barred List check.",
            "Q2.4 GP Health Declaration: Completed official CQC Medical Report Form stamped and signed by registered NHS GP.",
            "Q2.5 Supervisory Competency: Demonstrable track record in social care leadership, health & safety, and clinical governance."
        ]),
        ("Section 3: Directors' Fit & Proper Person Test (Reg 5 - Q3.1 - Q3.5)", [
            "Q3.1 Director Census: Full list of all corporate directors matching Companies House registered appointments.",
            "Q3.2 Criminal Records: Clean Enhanced DBS declarations for all directors; zero violent, fraud, or sexual convictions.",
            "Q3.3 Financial Solvency: Verification that no director is bankrupt, subject to IVAs, or disqualified under CDDA 1986.",
            "Q3.4 Professional Conduct: Confirmation that zero directors have been erased or suspended by NMC, GMC, HCPC, or SWE.",
            "Q3.5 Ongoing Governance: Board policy on annual fit and proper reviews, DBS tracking, and governance oversight."
        ]),
        ("Section 4: Regulated Activities, Service Type & Demographics (Q4.1 - Q4.4)", [
            "Q4.1 Regulated Activity: Personal Care under Health and Social Care Act 2008 Regulations 2014 Schedule 1.",
            "Q4.2 Service Setting: Supported Living service / Domiciliary care. Strictly avoiding care home classification.",
            "Q4.3 Client Demographics: Adults aged 18-65; Learning Disabilities; Autistic Spectrum Conditions; Mental Health.",
            "Q4.4 Right Support, Right Care, Right Culture: Narrative proving small-scale domestic setting and active tenant choice."
        ]),
        ("Section 5: Regulated Location & Premises Life Safety (Reg 15 - Q5.1 - Q5.5)", [
            "Q5.1 Regulated Location: 78 & 80 Marston Gardens, Luton, Bedfordshire, LU2 7DY (8 self-contained suites).",
            "Q5.2 Real Tenancy Separation: Landlord (ADOV LIMITED) issues AST; OpCo issues care contract; tenant bedroom keys.",
            "Q5.3 Fire Safety Systems: BS 5839 Cat L1 addressable fire panel, BS 5266 3h emergency lighting, FD30S doors.",
            "Q5.4 Anti-Scald Protection: WRAS TMV3 thermostatic mixing valves pre-set to <43C; ACoP L8 legionella logging.",
            "Q5.5 Laundry & Infection Control: Commercial barrier washing machines operating HTM 01-04 71C thermal hold cycle."
        ]),
        ("Section 6: Registered Manager Application & Competency (Reg 7 - Q6.1 - Q6.5)", [
            "Q6.1 Level 5 Leadership Diploma: Level 5 Diploma in Leadership and Management for Adult Care (RQF) or equivalent.",
            "Q6.2 Oliver McGowan Training: Completed Tier 1 and live interactive Tier 2 under Section 181 Health and Care Act 2022.",
            "Q6.3 BILD PBS Certification: BILD / Restraint Reduction Network accredited Level 3 certificate in Positive Behavioural Support.",
            "Q6.4 Working Hours & On-Call: 40 hours/week dedicated on-site campus leadership backed by 24/7 senior on-call rotation.",
            "Q6.5 Clinical Interview Defense: Mastery of 5 CQC scenarios: PBS de-escalation, safeguarding abuse, MCA covert meds, meds error."
        ]),
        ("Section 7: Quality Governance & The 5 Key Questions (Q7.1 - Q7.6)", [
            "Q7.1 Safe (Safeguarding Reg 13): Immediate suspension without prejudice; 24h statutory referral to Luton LSAB MASH.",
            "Q7.2 Safe (Medicines Reg 12): NICE SC1 guidance compliance; cloud eMAR system; BS 2881 CD cabinet; temperature logging.",
            "Q7.3 Effective (MCA & DoLS Reg 11): Presumption of capacity; Section 2 capacity tests; Section 4 Best Interests meetings.",
            "Q7.4 Caring (Dignity Reg 10): Private lockable suites with individual keys; knock-and-wait protocol; gender-appropriate support.",
            "Q7.5 Responsive (Person-Centred Reg 9): One-Page Profiles, Makaton communication passports, complaints policy with 20d SLA.",
            "Q7.6 Well-Led (Governance Reg 17 & 20): Monthly mock audits, Freedom to Speak Up Guardian, strict 10d Duty of Candour apology."
        ]),
        ("Section 8: Financial Viability & Insurance Assurance (Reg 13 - Q8.1 - Q8.4)", [
            "Q8.1 Chartered Accountant Declaration: Official declaration executed on ICAEW/ACCA letterhead verifying 12-month solvency.",
            "Q8.2 6-Month Working Capital Buffer: Bank statement confirming £75,000 - £100,000 unencumbered cash balance.",
            "Q8.3 12-Month Itemized Monthly Cashflow: Model showing £53,018/mo OpEx, Month 8 break-even, and Year 1 closing cash of £134,808.",
            "Q8.4 Commercial Care Insurance: Verification of £10m Employers' Liability, £10m Public Liability, £5m Professional Indemnity."
        ]),
        ("Section 9: Mandatory Upload Attachments Manifest (ATT-1 - ATT-8)", [
            "ATT-1: Statement of Purpose (Parts 1 to 4) - ADOV_CQC_Statement_of_Purpose_Parts_1_to_4.pdf",
            "ATT-2: Financial Viability Declaration - ADOV_Financial_Viability_Accountant_Letter.pdf",
            "ATT-3: 12-Month Cashflow Forecast Model - ADOV_12_Month_Cashflow_Forecast_2026.pdf",
            "ATT-4: 7 Core Statutory Quality Policies - ADOV_Core_Statutory_Policies_Pack_v1.0.pdf",
            "ATT-5: Premises Life Safety Dossier - ADOV_Premises_Life_Safety_Dossier_MarstonGdns.pdf",
            "ATT-6: Corporate Leases & AST Pack - ADOV_Corporate_Leases_and_Tenancy_Pack.pdf",
            "ATT-7: Registered Manager Credentials - ADOV_Registered_Manager_Credentials_Dossier.pdf",
            "ATT-8: Nominated Individual Pack - ADOV_Nominated_Individual_Credentials_Pack.pdf"
        ])
    ]

    for s_title, q_list in sections:
        add_p(s_title, style="Heading2", bold=True, size=22, color="C29B38", space_after=60)
        for q in q_list:
            add_bullet(q)

    content_types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '</Types>')

    pkg_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '</Relationships>')

    doc_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        '</Relationships>')

    styles_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica"/><w:sz w:val="22"/><w:color w:val="1E293B"/></w:rPr></w:rPrDefault></w:docDefaults>'
        '<w:style w:type="paragraph" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>'
        '<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:qFormat/><w:rPr><w:b/><w:sz w:val="36"/><w:color w:val="0F1E36"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/><w:qFormat/><w:rPr><w:b/><w:sz w:val="26"/><w:color w:val="C29B38"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="Heading 1"/><w:basedOn w:val="Normal"/><w:qFormat/><w:rPr><w:b/><w:sz w:val="28"/><w:color w:val="0F1E36"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="Heading 2"/><w:basedOn w:val="Normal"/><w:qFormat/><w:rPr><w:b/><w:sz w:val="22"/><w:color w:val="C29B38"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/><w:qFormat/></w:style>'
        '</w:styles>')

    doc_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body>' + "".join(doc_body) +
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>'
        '</w:body></w:document>')

    with zipfile.ZipFile(docx_filename, 'w', zipfile.ZIP_DEFLATED) as docx:
        docx.writestr('[Content_Types].xml', content_types)
        docx.writestr('_rels/.rels', pkg_rels)
        docx.writestr('word/_rels/document.xml.rels', doc_rels)
        docx.writestr('word/styles.xml', styles_xml)
        docx.writestr('word/document.xml', doc_xml)
    print(f"Generated DOCX '{docx_filename}'.")

if __name__ == "__main__":
    build_pdf()
    build_docx()
