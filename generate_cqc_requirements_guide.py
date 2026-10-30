#!/usr/bin/env python3
"""
ADOV Care Group - CQC Registration Requirements & Statutory Fulfillment Guide
Generates print-ready PDF and Word DOCX deliverables.
"""

import sys, os, zlib, zipfile
from build_statutory_document_packs import SimplePDF

def build_pdf():
    pdf_filename = "ADOV_Care_Group_CQC_Requirements_and_Fulfillment_Guide.pdf"
    doc = SimplePDF(pdf_filename, "CQC REGISTRATION REQUIREMENTS & FULFILLMENT GUIDE")

    # =========================================================================
    # PAGE 1: COVER & EXECUTIVE SUMMARY
    # =========================================================================
    p1 = doc.add_page(is_cover=True)
    p1.set_fill_color(0.06, 0.12, 0.21) # Deep Navy #0F1E36
    p1.draw_rect(0, 0, p1.width, p1.height)

    # Gold decorative borders
    p1.set_stroke_color(0.76, 0.61, 0.22) # Gold #C29B38
    p1.draw_rect(24, 24, p1.width - 48, p1.height - 48, fill=False, stroke=True, stroke_w=1.5)
    p1.set_stroke_color(0.45, 0.35, 0.12)
    p1.draw_rect(28, 28, p1.width - 56, p1.height - 56, fill=False, stroke=True, stroke_w=0.6)

    # Top pill
    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_rect(54, p1.height - 80, 290, 20, fill=True)
    p1.set_fill_color(0.06, 0.12, 0.21)
    p1.draw_text("EXECUTIVE STATUTORY COMPLIANCE MANUAL", 62, p1.height - 67, font="F2", size=8.5)

    # Main Titles
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("ADOV CARE GROUP", 54, p1.height - 125, font="F2", size=24.0)
    p1.set_stroke_color(0.76, 0.61, 0.22)
    p1.draw_line(54, p1.height - 138, p1.width - 54, p1.height - 138, stroke_w=1.5)

    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("CQC REGISTRATION REQUIREMENTS & FULFILLMENT GUIDE", 54, p1.height - 162, font="F2", size=13.0)
    p1.set_fill_color(0.85, 0.90, 0.98)
    p1.draw_text("Comprehensive 10-Pillar Statutory Breakdown & 24-Point Audit Checklist", 54, p1.height - 180, font="F1", size=10.0)
    p1.draw_text("Regulated Activity: Personal Care in Supported Living // Target: 78 & 80 Marston Gardens, Luton", 54, p1.height - 198, font="F1", size=8.5)

    # Executive Overview Box
    p1.set_fill_color(0.09, 0.16, 0.28)
    p1.set_stroke_color(0.25, 0.38, 0.60)
    p1.draw_rect(54, 330, p1.width - 108, 280, fill=True, stroke=True, stroke_w=1.0)

    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("EXECUTIVE SUMMARY & STATUTORY GOVERNANCE FRAMEWORK", 70, 585, font="F2", size=10.0)
    p1.draw_line(70, 577, p1.width - 70, 577, stroke_w=0.8)

    summary_bullets = [
        ("Health & Social Care Act 2008 & 2014 Regulations", "Mandatory compliance across Regulations 4, 5, 6, 7, 12, 13, 15, 17, 18 and 20."),
        ("Strict Supported Living 'Real Tenancy' Separation", "Housing tenure (PropCo AST) legally separated from Care (OpCo) to prevent s.10 HSCA care home prosecution."),
        ("Fit and Proper Person Governance (Regs 5 & 6)", "CQC-countersigned Enhanced DBS checks, GP health declarations, and solvency verification for all directors."),
        ("Registered Manager Qualifications (Reg 7)", "Level 5 Diploma in Adult Care, s.181 Oliver McGowan Tier 1 & 2, and BILD-accredited PBS Level 3 credentials."),
        ("Statutory Financial Viability Solvency (Reg 13)", "ICAEW/ACCA Chartered Accountant viability sign-off backed by £75,000 - £100,000 liquid capital buffer."),
        ("Premises Safety & Engineering Standards (Reg 15)", "BS 5839-1 Cat L1 fire detection, BS 5266 emergency lighting, WRAS TMV3 anti-scald (<43C), NICEIC EICR."),
        ("Section 28(3) Fast-Track Statutory Acceleration", "Immediate waiver of representations upon Notice of Proposal (NOP) receipt, collapsing 28 days to 48 hours.")
    ]

    cur_y = 556
    for b_title, b_desc in summary_bullets:
        p1.set_fill_color(0.76, 0.61, 0.22)
        p1.draw_text(chr(149), 70, cur_y, font="F2", size=10.0)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_text(b_title + ":", 82, cur_y, font="F2", size=8.5)
        p1.set_fill_color(0.85, 0.90, 0.98)
        p1.draw_text(b_desc, 82, cur_y - 12, font="F1", size=7.8)
        cur_y -= 26

    # Bottom Metadata Card
    p1.set_fill_color(0.09, 0.16, 0.28)
    p1.draw_rect(54, 75, p1.width - 108, 160, fill=True, stroke=True, stroke_w=1.0)
    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("STATUTORY DOSSIER METADATA & AUTHORIZATION", 70, 215, font="F2", size=9.5)
    p1.draw_line(70, 207, p1.width - 70, 207, stroke_w=0.6)

    meta_items = [
        ("Applicant Body Corporate:", "ADOV Care Group LIMITED (Company No. Registered in England & Wales)"),
        ("Property Holding SPV:", "ADOV LIMITED (Owner / Commercial Landlord of 78, 80 & 82 Marston Gardens)"),
        ("Corporate Group Parent:", "FAIRYTALES GROUP (Trading Name of Mamun Limited)"),
        ("Strategic Advisory:", "Project Planned & Engineered by AbdullahMamun.com"),
        ("Regulated Activity:", "Personal Care (Health and Social Care Act 2008 Regulated Activities Regulations 2014)"),
        ("Commissioning Target:", "Luton Borough Council Adult Social Care Supported Living Framework & BLMK ICB")
    ]
    cur_my = 190
    for m_lbl, m_val in meta_items:
        p1.set_fill_color(0.76, 0.61, 0.22)
        p1.draw_text(m_lbl, 70, cur_my, font="F2", size=8.0)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_text(m_val, 210, cur_my, font="F1", size=8.0)
        cur_my -= 18

    # Footer note
    p1.set_fill_color(0.55, 0.65, 0.75)
    p1.draw_text("CONFIDENTIAL - FOR INTERNAL EXECUTIVE MANAGEMENT & CQC SUBMISSION USE ONLY", p1.width / 2, 45, font="F1", size=7.5, align="center", max_w=p1.cw)

    # =========================================================================
    # PAGE 2: 24-POINT STATUTORY AUDIT & FULFILLMENT CHECKLIST
    # =========================================================================
    p2 = doc.add_page()
    p2.draw_header_banner("DOC-CQC-01", "24-POINT STATUTORY AUDIT & FULFILLMENT CHECKLIST", "CQC REGISTRATION BLUEPRINT")

    p2.set_fill_color(0.06, 0.12, 0.21)
    p2.draw_text("MANDATORY REGISTRATION AUDIT INVENTORY (ZERO NON-COMPLIANCE TOLERANCE)", p2.mx, p2.height - 70, font="F2", size=10.0)
    p2.set_fill_color(0.35, 0.40, 0.50)
    p2.draw_text("Every item below must be fully verified and evidenced prior to lodging on the CQC digital provider portal.", p2.mx, p2.height - 82, font="F1", size=8.0)

    # Checklist Table
    ty = p2.height - 100
    p2.set_fill_color(0.06, 0.12, 0.21)
    p2.draw_rect(p2.mx, ty, p2.cw, 18, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    p2.draw_text("REF", p2.mx + 6, ty + 5, font="F2", size=7.5)
    p2.draw_text("STATUTORY REQUIREMENT & REGULATORY CITATION", p2.mx + 35, ty + 5, font="F2", size=7.5)
    p2.draw_text("MANDATORY EVIDENCE / DOCUMENT", p2.mx + 300, ty + 5, font="F2", size=7.5)
    p2.draw_text("LEAD", p2.mx + 450, ty + 5, font="F2", size=7.5)
    p2.draw_text("STATUS", p2.mx + 485, ty + 5, font="F2", size=7.5)

    checklist_items = [
        ("A1", "CQC Enhanced DBS with Adult Barred List (Reg 5/6)", "First Advantage CQC Certificate (<12 mos)", "Directors", "[READY]"),
        ("A2", "NHS GP Health Declaration Form (Reg 5/6)", "Stamped & signed GP Medical Declaration", "NI / RM", "[READY]"),
        ("A3", "Registered Manager Level 5 Diploma (Reg 7)", "Level 5 Leadership for Adult Care / RMA", "Reg Manager", "[READY]"),
        ("A4", "Oliver McGowan Tier 1 & 2 + BILD PBS (s.181)", "NHS Oliver McGowan & BILD PBS certs", "Reg Manager", "[READY]"),
        ("B5", "Statement of Purpose Part 1 & 2: Entity & Aims", "CQC Template (SIC 88100, Values, Ethos)", "Nominated Ind", "[READY]"),
        ("B6", "Statement of Purpose Part 3: Campus Facilities", "78 & 80 Marston Gdns (8 suites, gardens)", "Reg Manager", "[READY]"),
        ("B7", "Statement of Purpose Part 4: Personal Care Scope", "Right Support Right Care Right Culture doc", "Reg Manager", "[READY]"),
        ("C8", "ICAEW/ACCA Chartered Accountant Declaration (Reg 13)", "Signed Viability Letter on Accountancy Firm letterhead", "Chartered Acc", "[READY]"),
        ("C9", "12-Month Itemized Monthly Cashflow Model (Reg 13)", "Forecast showing £53k/mo OpEx, M8 break-even", "Finance Team", "[READY]"),
        ("C10", "£75k - £100k Liquid Working Capital Buffer (Reg 13)", "Bank statement under ADOV Care Group LTD", "Holding Board", "[READY]"),
        ("D11", "Safeguarding Adults at Risk Policy (Care Act s.42)", "Luton LSAB aligned procedure, 24h MASH notice", "Reg Manager", "[READY]"),
        ("D12", "Mental Capacity Act (MCA 2005) & DoLS / LPS Policy", "Two-stage capacity tests & Section 4 Best Interests", "Reg Manager", "[READY]"),
        ("D13", "Safe Management of Medicines Policy (NICE SC1)", "eMAR protocols, storage, CD Cabinet BS 2881", "Reg Manager", "[READY]"),
        ("D14", "Health, Safety, COSHH, Legionella & TMV3 Protocol", "ACoP L8 water risk log & TMV3 calibration log", "Operations", "[READY]"),
        ("D15", "Whistleblowing (PIDA 1998) & Duty of Candour (Reg 20)", "Speak Up Guardian & 10-day formal apology policy", "Nominated Ind", "[READY]"),
        ("E16", "BS 5839-1 Category L1 Fire Detection System (Reg 15)", "BAFE SP203 Commissioning Certificate", "Fire Contractor", "[READY]"),
        ("E17", "BS 5266-1 3-Hour Emergency Lighting (Reg 15)", "BS 5266 Electrical Commissioning Certificate", "Electrician", "[READY]"),
        ("E18", "FD30S Fire Doors with Intumescent Seals (Reg 15)", "14 Doorsets + Dorgard / acoustic magnetic hold-opens", "Contractor", "[READY]"),
        ("E19", "WRAS TMV3 Anti-Scald Thermostatic Valves (Reg 15)", "Plumbing calibration certificate (<43C shut-off)", "Plumber", "[READY]"),
        ("E20", "NICEIC EICR & Gas Safe CP12 Certificates (Reg 15)", "Satisfactory EICR & Landlord Gas Safety CP12", "Contractor", "[READY]"),
        ("F21", "The 'Real Tenancy' Test: Housing Separation (s.10)", "PropCo AST distinct from Care Provider contract", "Legal Counsel", "[READY]"),
        ("F22", "Freedom of Choice & Lockable Rooms (s.10 HSCA)", "Tenancy freedom clause & individual bedroom keys", "Legal Counsel", "[READY]"),
        ("F23", "CQC Provider Portal Concurrent Lodging Pack", "15 standardized PDF uploads (<15MB each)", "Nominated Ind", "[READY]"),
        ("F24", "Section 28(3) Fast-Track Statutory Waiver of Reps", "Pre-drafted waiver letter ready for NOP receipt", "Nominated Ind", "[READY]")
    ]

    row_y = ty - 16
    for idx, (ref, req, doc_name, lead, stat) in enumerate(checklist_items):
        bg = (0.97, 0.98, 1.0) if idx % 2 == 0 else (1.0, 1.0, 1.0)
        p2.set_fill_color(bg[0], bg[1], bg[2])
        p2.draw_rect(p2.mx, row_y, p2.cw, 15, fill=True)
        p2.set_stroke_color(0.85, 0.88, 0.92)
        p2.draw_line(p2.mx, row_y, p2.mx + p2.cw, row_y, stroke_w=0.4)

        p2.set_fill_color(0.06, 0.12, 0.21)
        p2.draw_text(ref, p2.mx + 6, row_y + 4, font="F2", size=7.2)
        p2.draw_text(req, p2.mx + 35, row_y + 4, font="F1", size=6.8)
        p2.draw_text(doc_name, p2.mx + 300, row_y + 4, font="F1", size=6.5)
        p2.set_fill_color(0.76, 0.61, 0.22)
        p2.draw_text(lead, p2.mx + 450, row_y + 4, font="F2", size=6.5)
        p2.set_fill_color(0.05, 0.55, 0.25)
        p2.draw_text(stat, p2.mx + 485, row_y + 4, font="F2", size=6.8)

        row_y -= 15.5

    # Footer note
    p2.set_fill_color(0.55, 0.65, 0.75)
    p2.draw_text("Page 2 of 7 // CQC Statutory Compliance Dossier // ADOV Care Group LIMITED", p2.width / 2, 28, font="F1", size=7.5, align="center", max_w=p2.cw)

    # =========================================================================
    # PAGE 3: PILLARS 1 & 2 - GOVERNANCE, FPPT & REGISTERED MANAGER
    # =========================================================================
    p3 = doc.add_page()
    p3.draw_header_banner("DOC-CQC-02", "PILLARS 1 & 2: FPPT GOVERNANCE & REGISTERED MANAGER", "CQC REGISTRATION BLUEPRINT")

    # Pillar 1 Card
    p3.set_fill_color(0.97, 0.98, 1.0)
    p3.set_stroke_color(0.15, 0.25, 0.45)
    p3.draw_rect(p3.mx, p3.height - 350, p3.cw, 280, fill=True, stroke=True, stroke_w=1.0)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_rect(p3.mx, p3.height - 90, p3.cw, 20, fill=True)
    p3.set_fill_color(0.76, 0.61, 0.22)
    p3.draw_text("PILLAR 1: FIT AND PROPER PERSON GOVERNANCE (REGULATIONS 4, 5 & 6)", p3.mx + 10, p3.height - 76, font="F2", size=8.5)

    p1_text = (
        "Statutory Mandate: Regulation 5 of the Health and Social Care Act 2008 (Regulated Activities) Regulations 2014 "
        "imposes a strict legal requirement that all directors of care provider entities are of good character, have the "
        "necessary qualifications, skills and experience, and are physically and mentally fit. Regulation 6 mandates "
        "the appointment of an employed Nominated Individual (NI) with operational authority to supervise regulated activities."
    )
    p3.set_fill_color(0.15, 0.20, 0.30)
    p3.draw_wrapped_text(p1_text, p3.mx + 12, p3.height - 105, p3.cw - 24, font="F1", size=7.8, leading=10.5)

    # Pillar 1 Action Steps
    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_text("Step-by-Step Fulfillment Protocol for Pillar 1:", p3.mx + 12, p3.height - 150, font="F2", size=8.2)

    p1_steps = [
        "1. CQC Enhanced DBS via First Advantage: Initiate online applications specifically through CQC's registered body. Verify ID at Post Office. DBS must include Adult Barred List and be <12 months old at submission.",
        "2. NHS GP Health Fitness Declarations: Download CQC's official Medical Report Form. Book appointment with registered NHS GP. Secure practice stamp, signature, and confirmation of medical fitness.",
        "3. Directors' Bankruptcy & Disqualification Audits: Perform formal searches on Companies House Disqualified Directors Register and the Individual Insolvency Register. Retain search printouts in company statutory books.",
        "4. Employment History & Verified References: Audit CVs to eliminate any unexplained gaps. Secure minimum 2 written supervisory references covering the last 3-5 years.",
        "5. Board Resolution Appointing Nominated Individual: Pass formal board resolution in ADOV Care Group LIMITED appointing the director responsible for supervising regulated care. File Form AP01 at Companies House."
    ]
    cur_y = p3.height - 165
    for stp in p1_steps:
        cur_y = p3.draw_wrapped_text(stp, p3.mx + 12, cur_y, p3.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    # Pillar 2 Card
    p3.set_fill_color(0.97, 0.98, 1.0)
    p3.set_stroke_color(0.76, 0.61, 0.22)
    p3.draw_rect(p3.mx, 55, p3.cw, 320, fill=True, stroke=True, stroke_w=1.0)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_rect(p3.mx, 355, p3.cw, 20, fill=True)
    p3.set_fill_color(0.76, 0.61, 0.22)
    p3.draw_text("PILLAR 2: REGISTERED MANAGER STATUTORY CREDENTIALS (REGULATION 7)", p3.mx + 10, 369, font="F2", size=8.5)

    p2_text = (
        "Statutory Mandate: Under Regulation 7, the Registered Manager must satisfy CQC of their fitness, clinical competence, "
        "and leadership ability to carry on the regulated activity of Personal Care. For Supported Living specializing in autism "
        "and complex learning disabilities, CQC applies heightened scrutiny to behavioral de-escalation and medication governance."
    )
    p3.set_fill_color(0.15, 0.20, 0.30)
    p3.draw_wrapped_text(p2_text, p3.mx + 12, 342, p3.cw - 24, font="F1", size=7.8, leading=10.5)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_text("Mandatory Qualifications & Fulfillment Actions for Pillar 2:", p3.mx + 12, 298, font="F2", size=8.2)

    p2_steps = [
        "1. Leadership Qualification: Level 5 Diploma in Leadership and Management for Adult Care (RQF), or predecessor NVQ Level 4 in Health and Social Care / Registered Manager Award (RMA). Certificates must be validated.",
        "2. Section 181 Oliver McGowan Mandatory Training: Tier 1 (online knowledge) and Tier 2 (live interactive session with autistic co-trainers) under Section 181 Health and Care Act 2022. Both modules must be certified.",
        "3. BILD-Accredited Positive Behavioural Support (PBS): BILD / Restraint Reduction Network (RRN) accredited Level 3 certificate (e.g. MAPA, Team Teach, or CPI Safety Intervention) with zero-tolerance for mechanical restraint.",
        "4. 3+ Years Adult Care Supervisory Track Record: Verifiable evidence of leading staff rotas, managing eMAR medication, conducting safeguarding investigations, and handling multi-agency local authority reviews.",
        "5. CQC Registration Interview Preparation: Complete 3 mock clinical interviews covering PBS crisis de-escalation, Section 4 Mental Capacity Act covert meds, medication error Duty of Candour, and safeguarding escalation."
    ]
    cur_y = 284
    for stp in p2_steps:
        cur_y = p3.draw_wrapped_text(stp, p3.mx + 12, cur_y, p3.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    p3.set_fill_color(0.55, 0.65, 0.75)
    p3.draw_text("Page 3 of 7 // CQC Statutory Compliance Dossier // ADOV Care Group LIMITED", p3.width / 2, 28, font="F1", size=7.5, align="center", max_w=p3.cw)

    # =========================================================================
    # PAGE 4: PILLARS 3 & 4 - STATEMENT OF PURPOSE & FINANCIAL VIABILITY
    # =========================================================================
    p4 = doc.add_page()
    p4.draw_header_banner("DOC-CQC-03", "PILLARS 3 & 4: STATEMENT OF PURPOSE & VIABILITY", "CQC REGISTRATION BLUEPRINT")

    # Pillar 3 Card
    p4.set_fill_color(0.97, 0.98, 1.0)
    p4.set_stroke_color(0.15, 0.25, 0.45)
    p4.draw_rect(p4.mx, p4.height - 350, p4.cw, 280, fill=True, stroke=True, stroke_w=1.0)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_rect(p4.mx, p4.height - 90, p4.cw, 20, fill=True)
    p4.set_fill_color(0.76, 0.61, 0.22)
    p4.draw_text("PILLAR 3: STATUTORY STATEMENT OF PURPOSE (REGULATION 12 & SCHEDULE 3)", p4.mx + 10, p4.height - 76, font="F2", size=8.5)

    p3_sop_text = (
        "Statutory Mandate: Regulation 12 of the Care Quality Commission (Registration) Regulations 2009 requires every provider "
        "to maintain a formal Statement of Purpose describing the service, its aims, locations, and regulated activities. "
        "Under Section 24 of the Regulations, delivering services inconsistent with the Statement of Purpose is a summary criminal offence."
    )
    p4.set_fill_color(0.15, 0.20, 0.30)
    p4.draw_wrapped_text(p3_sop_text, p4.mx + 12, p4.height - 105, p4.cw - 24, font="F1", size=7.8, leading=10.5)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_text("The 4 Mandatory Parts & Fulfillment Actions for Pillar 3:", p4.mx + 12, p4.height - 150, font="F2", size=8.2)

    p3_steps = [
        "Part 1: Provider Details: Legal entity name (ADOV Care Group LIMITED), Companies House registration number, corporate registered office address, and nominated individual direct contact details.",
        "Part 2: Aims & Objectives: Person-centered care philosophy, promotion of autonomy, Active Support framework, inclusion values, and outcome measurement for autistic adults and individuals with learning disabilities.",
        "Part 3: Locations & Facilities: Detailed physical descriptions of 78 & 80 Marston Gardens, Luton (LU2 7DY) - 8 private suites, accessible wetrooms, commercial kitchens, sensory quiet lounges, and 500m2+ secure grounds.",
        "Part 4: Regulated Activities & User Bands: Regulated activity 'Personal Care' (Schedule 1, Paragraph 1). Target cohort: Adults 18-65 with learning disabilities, autistic spectrum conditions, and mental health step-down needs.",
        "Right Support, Right Care, Right Culture Alignment: CQC statutory guidance must be explicitly integrated. Emphasize that service users hold private tenancies and can choose their care provider freely."
    ]
    cur_y = p4.height - 165
    for stp in p3_steps:
        cur_y = p4.draw_wrapped_text(stp, p4.mx + 12, cur_y, p4.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    # Pillar 4 Card
    p4.set_fill_color(0.97, 0.98, 1.0)
    p4.set_stroke_color(0.76, 0.61, 0.22)
    p4.draw_rect(p4.mx, 55, p4.cw, 320, fill=True, stroke=True, stroke_w=1.0)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_rect(p4.mx, 355, p4.cw, 20, fill=True)
    p4.set_fill_color(0.76, 0.61, 0.22)
    p4.draw_text("PILLAR 4: FINANCIAL VIABILITY & SOLVENCY ASSURANCE (REGULATION 13)", p4.mx + 10, 369, font="F2", size=8.5)

    p4_viab_text = (
        "Statutory Mandate: Regulation 13 of the CQC (Registration) Regulations 2009 mandates that providers must demonstrate financial "
        "viability to carry on regulated activities safely. CQC strictly rejects applications supported only by uncertified bookkeepers "
        "or lacking clear evidence of 6 months' debt-free working capital reserves."
    )
    p4.set_fill_color(0.15, 0.20, 0.30)
    p4.draw_wrapped_text(p4_viab_text, p4.mx + 12, 342, p4.cw - 24, font="F1", size=7.8, leading=10.5)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_text("Mandatory Viability Deliverables & Fulfillment Actions for Pillar 4:", p4.mx + 12, 298, font="F2", size=8.2)

    p4_steps = [
        "1. ICAEW / ACCA Chartered Accountant Declaration: Official declaration letter on chartered accountancy firm letterhead executing CQC's exact statutory text confirming 12-month solvency and financial viability.",
        "2. £75,000 - £100,000 Unencumbered Liquid Cash Buffer: Bank balance statement confirming sufficient cash reserves in ADOV Care Group LIMITED commercial account to cover 6 months' payroll before council payments clear.",
        "3. 12-Month Itemized Monthly Cashflow Model: Submission of group cashflow model showing phased ramp-up, £53,018/month steady-state OpEx, Month 8 cashflow break-even, and Year 1 closing cash of £134,808.",
        "4. Commercial Social Care Insurance Schedule: Verification of £10m Employers' Liability, £10m Public Liability, £5m Professional Indemnity, and Abuse malpractice cover through care sector brokers.",
        "5. Clean Corporate Separation: Clean intercompany FRI commercial leases from PropCo (ADOV LIMITED) to OpCo (ADOV Care Group LIMITED) establishing rent as a formal tax-deductible operational expense."
    ]
    cur_y = 284
    for stp in p4_steps:
        cur_y = p4.draw_wrapped_text(stp, p4.mx + 12, cur_y, p4.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    p4.set_fill_color(0.55, 0.65, 0.75)
    p4.draw_text("Page 4 of 7 // CQC Statutory Compliance Dossier // ADOV Care Group LIMITED", p4.width / 2, 28, font="F1", size=7.5, align="center", max_w=p4.cw)

    # =========================================================================
    # PAGE 5: PILLARS 5 & 6 - THE 7 CORE POLICIES & PREMISES SAFETY
    # =========================================================================
    p5 = doc.add_page()
    p5.draw_header_banner("DOC-CQC-04", "PILLARS 5 & 6: 7 CORE POLICIES & PREMISES SAFETY", "CQC REGISTRATION BLUEPRINT")

    # Pillar 5 Card
    p5.set_fill_color(0.97, 0.98, 1.0)
    p5.set_stroke_color(0.15, 0.25, 0.45)
    p5.draw_rect(p5.mx, p5.height - 350, p5.cw, 280, fill=True, stroke=True, stroke_w=1.0)

    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_rect(p5.mx, p5.height - 90, p5.cw, 20, fill=True)
    p5.set_fill_color(0.76, 0.61, 0.22)
    p5.draw_text("PILLAR 5: THE 7 CORE STATUTORY POLICIES (REGULATION 17 - GOOD GOVERNANCE)", p5.mx + 10, p5.height - 76, font="F2", size=8.5)

    p5_pol_text = (
        "Statutory Mandate: Regulation 17 requires providers to operate robust governance systems. Policies must not be generic internet "
        "templates; they must be customized to ADOV Care Group LIMITED and explicitly reference Luton Borough Council Adult Social Care, "
        "the Bedfordshire Safeguarding Adults Board (BSAB/LSAB), and local clinical escalation pathways."
    )
    p5.set_fill_color(0.15, 0.20, 0.30)
    p5.draw_wrapped_text(p5_pol_text, p5.mx + 12, p5.height - 105, p5.cw - 24, font="F1", size=7.8, leading=10.5)

    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_text("The 7 Mandatory Core Policies & Localized Operational Rules:", p5.mx + 12, p5.height - 150, font="F2", size=8.2)

    p5_steps = [
        "1. Safeguarding Adults at Risk (Care Act 2014 s.42): Zero tolerance; immediate staff suspension without prejudice; 24h statutory referral to Luton LSAB Multi-Agency Safeguarding Hub (MASH); CQC Regulation 18 notification.",
        "2. Mental Capacity Act (MCA 2005) & DoLS / LPS: Presumption of capacity; Section 2 functional assessments; Section 4 multi-disciplinary Best Interests meetings; Court of Protection; least-restrictive principle.",
        "3. Safe Administration of Medicines (NICE SC1): Cloud-based eMAR system with barcode verification; temperature-controlled storage (15-25C); British Standard BS 2881 Controlled Drugs cabinet; six rights of administration.",
        "4. Infection Prevention & Control (IPC) & Laundry: Health & Social Care Act Code of Practice; HTM 01-04 commercial laundry decontamination with 71C thermal disinfection hold cycle; barrier nursing procedures.",
        "5. Health, Safety, COSHH & TMV3 Anti-Scald: ACoP L8 Legionella monitoring (<20C cold, >50C hot); WRAS TMV3 thermostatic mixing valves calibrated to <43C; annual PAT testing; locked hazardous chemical stores.",
        "6. Whistleblowing (PIDA 1998): Independent Freedom to Speak Up Guardian; confidential reporting channels; statutory protection from detrimental treatment or dismissal; mandatory executive board reporting.",
        "7. Statutory Duty of Candour (Regulation 20): Strict legal mandate to inform service users/advocates within 24h of any notifiable safety incident; formal written apology within 10 working days; full root cause report."
    ]
    cur_y = p5.height - 165
    for stp in p5_steps:
        cur_y = p5.draw_wrapped_text(stp, p5.mx + 12, cur_y, p5.cw - 24, font="F1", size=7.0, leading=9.2)
        cur_y -= 3

    # Pillar 6 Card
    p5.set_fill_color(0.97, 0.98, 1.0)
    p5.set_stroke_color(0.76, 0.61, 0.22)
    p5.draw_rect(p5.mx, 55, p5.cw, 320, fill=True, stroke=True, stroke_w=1.0)

    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_rect(p5.mx, 355, p5.cw, 20, fill=True)
    p5.set_fill_color(0.76, 0.61, 0.22)
    p5.draw_text("PILLAR 6: PREMISES & ENVIRONMENTAL SAFETY STANDARDS (REGULATION 15)", p5.mx + 10, 369, font="F2", size=8.5)

    p6_prem_text = (
        "Statutory Mandate: Regulation 15 mandates that all premises used to deliver care must be clean, safe, suitable, and properly maintained. "
        "CQC inspectors inspect physical premises to ensure vulnerable tenants are fully safeguarded from fire, hot water scalding, "
        "and environmental hazards across the 78 & 80 Marston Gardens supported living campus."
    )
    p5.set_fill_color(0.15, 0.20, 0.30)
    p5.draw_wrapped_text(p6_prem_text, p5.mx + 12, 342, p5.cw - 24, font="F1", size=7.8, leading=10.5)

    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_text("Engineering Certifications & Safety Fulfillment for Pillar 6:", p5.mx + 12, 298, font="F2", size=8.2)

    p6_steps = [
        "1. BS 5839-1 Category L1 Fire Detection: BAFE-accredited addressable system with optical smoke detectors in every bedroom, lounge, and roof void; heat detector in kitchen; sounders >75dB at bedheads. Commissioning cert required.",
        "2. BS 5266-1 3-Hour Emergency Lighting: Maintained/non-maintained LED emergency fittings along all escape corridors, stairwells, and external doorways. Formal electrical commissioning certificate and monthly test log.",
        "3. FD30S Fire Doorsets: 30-minute fire-resisting doorsets with intumescent heat strips and cold smoke brushes fitted to all 8 bedrooms and risk rooms. Acoustic Dorgard / magnetic hold-open retainers linked to fire panel.",
        "4. WRAS TMV3 Anti-Scald Thermostatic Valves: TMV3 valves fitted to all baths, showers, and washbasins calibrated to shut off automatically if water exceeds 43C, eliminating scalding risk for sensory-impaired adults.",
        "5. Electrical (NICEIC EICR) & Gas Safe (CP12): Satisfactory 5-year commercial electrical installation certificate with zero Code 1/2 faults; annual commercial landlord Gas Safe certificate for central heating boilers.",
        "6. Therapeutic Garden Perimeter Security: Fully enclosed 24.5m rear grounds with 1.8m close-boarded fencing, secure self-latching gates, tactile non-slip pathways, and sensory outdoor seating."
    ]
    cur_y = 284
    for stp in p6_steps:
        cur_y = p5.draw_wrapped_text(stp, p5.mx + 12, cur_y, p5.cw - 24, font="F1", size=7.0, leading=9.2)
        cur_y -= 3

    p5.set_fill_color(0.55, 0.65, 0.75)
    p5.draw_text("Page 5 of 7 // CQC Statutory Compliance Dossier // ADOV Care Group LIMITED", p5.width / 2, 28, font="F1", size=7.5, align="center", max_w=p5.cw)

    # =========================================================================
    # PAGE 6: PILLARS 7, 8, 9 & 10 - TENANCY, PORTAL, INTERVIEW & WAIVER
    # =========================================================================
    p6 = doc.add_page()
    p6.draw_header_banner("DOC-CQC-05", "PILLARS 7-10: TENANCY, PORTAL, DEFENSE & WAIVER", "CQC REGISTRATION BLUEPRINT")

    # Real Tenancy & Section 28(3) Split Box
    p6.set_fill_color(0.97, 0.98, 1.0)
    p6.set_stroke_color(0.15, 0.25, 0.45)
    p6.draw_rect(p6.mx, p6.height - 350, p6.cw, 280, fill=True, stroke=True, stroke_w=1.0)

    p6.set_fill_color(0.06, 0.12, 0.21)
    p6.draw_rect(p6.mx, p6.height - 90, p6.cw, 20, fill=True)
    p6.set_fill_color(0.76, 0.61, 0.22)
    p6.draw_text("PILLAR 7: THE REAL TENANCY TEST & AVOIDING SECTION 10 HSCA CRIMINAL CHARGES", p6.mx + 10, p6.height - 76, font="F2", size=8.5)

    p7_text = (
        "Statutory Mandate: In Supported Living, Housing (Landlord) and Personal Care (Care Provider) must be completely separate. "
        "If accommodation and care are bundled into an indivisible package, CQC legally reclassifies the service as an unregistered Care Home. "
        "Carrying on an unregistered care home is a criminal offence under Section 10 of the Health and Social Care Act 2008."
    )
    p6.set_fill_color(0.15, 0.20, 0.30)
    p6.draw_wrapped_text(p7_text, p6.mx + 12, p6.height - 105, p6.cw - 24, font="F1", size=7.8, leading=10.5)

    p6.set_fill_color(0.06, 0.12, 0.21)
    p6.draw_text("The 4 Legal Tests Satisfied by ADOV Care Group:", p6.mx + 12, p6.height - 150, font="F2", size=8.2)

    p7_steps = [
        "1. Independent Tenancy Agreement: Executed directly between Landlord (ADOV LIMITED / Housing Association) and resident. ADOV Care Group LIMITED (care provider) is NOT a party to the lease.",
        "2. Separate Care & Support Contract: Executed between ADOV Care Group LIMITED and the resident (or Luton Council / ICB commissioner) completely detached from housing tenure.",
        "3. Explicit 'Freedom of Choice' Clause: Tenancy agreement guarantees that the resident has the statutory right to change or dismiss their care provider at any time without forfeiting their tenancy or facing eviction.",
        "4. Exclusive Possession of Bedroom: Resident holds personal keys to their lockable bedroom door; staff knock and seek permission before entering; emergency override protocol strictly limited to life-safety threats."
    ]
    cur_y = p6.height - 165
    for stp in p7_steps:
        cur_y = p6.draw_wrapped_text(stp, p6.mx + 12, cur_y, p6.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    # Pillars 8, 9 & 10 Box
    p6.set_fill_color(0.97, 0.98, 1.0)
    p6.set_stroke_color(0.76, 0.61, 0.22)
    p6.draw_rect(p6.mx, 55, p6.cw, 320, fill=True, stroke=True, stroke_w=1.0)

    p6.set_fill_color(0.06, 0.12, 0.21)
    p6.draw_rect(p6.mx, 355, p6.cw, 20, fill=True)
    p6.set_fill_color(0.76, 0.61, 0.22)
    p6.draw_text("PILLARS 8, 9 & 10: PORTAL SUBMISSION, INTERVIEW DEFENSE & SECTION 28(3) WAIVER", p6.mx + 10, 369, font="F2", size=8.5)

    p8_text = (
        "Operational Execution: Applications are lodged concurrently on the CQC digital provider portal. The Registered Manager "
        "defends 5 mandatory clinical scenarios during the CQC fit and proper interview. Upon receipt of the Notice of Proposal (NOP), "
        "management executes Section 28(3) of the Act to collapse the 28-day statutory waiting period into 48-72 hours."
    )
    p6.set_fill_color(0.15, 0.20, 0.30)
    p6.draw_wrapped_text(p8_text, p6.mx + 12, 342, p6.cw - 24, font="F1", size=7.8, leading=10.5)

    p6.set_fill_color(0.06, 0.12, 0.21)
    p6.draw_text("Clinical Interview Defense & Statutory Fast-Track Waiver:", p6.mx + 12, 298, font="F2", size=8.2)

    p8_steps = [
        "Pillar 8: Portal Lodging Manifest: Submit Provider and Registered Manager applications simultaneously. Attach all 15 validated PDF documents (<15MB each, text-searchable) to clear administrative validation within 5 working days.",
        "Pillar 9 Scenario 1 (PBS De-escalation): Primary proactive prevention; low-arousal environment; diversion and active support; zero unauthorized restraint; mandatory 24h debrief and PBS plan revision.",
        "Pillar 9 Scenario 2 (Staff Abuse Allegation): Immediate protective suspension without prejudice; 24h statutory referral to Luton LSAB MASH; Regulation 18 notification to CQC; police liaison if criminal.",
        "Pillar 9 Scenario 3 (MCA & Covert Meds): Two-stage capacity test; if lacking, Section 4 Best Interests meeting with GP and pharmacist; Court of Protection approval; written covert administration protocol.",
        "Pillar 9 Scenario 4 (Meds Error & Duty of Candour): Vital signs triage; 999/GP call; Regulation 20 Duty of Candour written apology within 10 days; electronic MAR audit; incident investigation report.",
        "Pillar 10 (Section 28(3) Fast-Track Waiver): Under Section 28(3) HSCA 2008, applicant submits written waiver of representations against NOP, forcing CQC to issue final Notice of Decision and Certificate in 48-72 hours."
    ]
    cur_y = 284
    for stp in p8_steps:
        cur_y = p6.draw_wrapped_text(stp, p6.mx + 12, cur_y, p6.cw - 24, font="F1", size=7.0, leading=9.2)
        cur_y -= 3

    p6.set_fill_color(0.55, 0.65, 0.75)
    p6.draw_text("Page 6 of 7 // CQC Statutory Compliance Dossier // ADOV Care Group LIMITED", p6.width / 2, 28, font="F1", size=7.5, align="center", max_w=p6.cw)

    # =========================================================================
    # PAGE 7: MASTER 16-WEEK CHRONOLOGICAL IMPLEMENTATION ROADMAP
    # =========================================================================
    p7 = doc.add_page()
    p7.draw_header_banner("DOC-CQC-06", "16-WEEK MASTER IMPLEMENTATION ROADMAP", "CQC REGISTRATION BLUEPRINT")

    p7.set_fill_color(0.06, 0.12, 0.21)
    p7.draw_text("CHRONOLOGICAL EXECUTION SCHEDULE: PRE-APPLICATION TO COMMISSIONING", p7.mx, p7.height - 70, font="F2", size=10.0)
    p7.set_fill_color(0.35, 0.40, 0.50)
    p7.draw_text("Rigorous week-by-week timeline detailing responsible leads, milestones, and statutory gate clearances.", p7.mx, p7.height - 82, font="F1", size=8.0)

    # Master Timeline Table
    ty = p7.height - 105
    p7.set_fill_color(0.06, 0.12, 0.21)
    p7.draw_rect(p7.mx, ty, p7.cw, 20, fill=True)
    p7.set_fill_color(1.0, 1.0, 1.0)
    p7.draw_text("WEEKS", p7.mx + 8, ty + 6, font="F2", size=8.0)
    p7.draw_text("PHASE & OPERATIONAL FOCUS", p7.mx + 60, ty + 6, font="F2", size=8.0)
    p7.draw_text("STATUTORY ACTIONS, MILESTONES & CLEARANCE CRITERIA", p7.mx + 210, ty + 6, font="F2", size=8.0)
    p7.draw_text("RESPONSIBLE LEAD", p7.mx + 440, ty + 6, font="F2", size=8.0)

    phases = [
        ("Weeks 1 - 2", "Phase 1: Governance & DBS", "Initiate CQC Enhanced DBS checks via First Advantage for all directors and Nominated Individual. Book NHS GP medical appointments. Pass board resolutions.", "Nominated Ind"),
        ("Weeks 3 - 4", "Phase 2: Management Vetting", "Appoint Registered Manager with Level 5 Diploma. Audit Oliver McGowan Tier 1 & 2 certificates and BILD PBS credentials. Execute employment agreement.", "Board / NI"),
        ("Weeks 5 - 6", "Phase 3: Policies & Statement", "Draft Statement of Purpose Parts 1 to 4. Finalize 7 core policies localized to Luton LSAB. Obtain signed ICAEW Chartered Accountant viability declaration.", "RM & Accountant"),
        ("Weeks 7 - 8", "Phase 4: Premises Fit-Out", "Complete BS 5839 Cat L1 fire alarm installation, BS 5266 emergency lighting, TMV3 anti-scald testing (<43C), and NICEIC EICR certification across 78 & 80.", "Contractor Lead"),
        ("Weeks 9 - 10", "Phase 5: Portal Submission", "Submit Provider and Manager applications simultaneously via CQC Provider Portal with 15 validated PDF attachments. Clear administrative validation.", "Nominated Ind"),
        ("Weeks 11 - 12", "Phase 6: CQC Assessment", "CQC Registration Inspector reviews documentation, policies, and financial viability. Respond to Requests for Information (RFIs) within 48 hours.", "RM & NI"),
        ("Weeks 13 - 14", "Phase 7: Interview & Site Visit", "Registered Manager completes 90-minute clinical defense interview covering 5 scenarios. CQC inspector carries out physical site visit of 78 & 80 campus.", "RM & NI"),
        ("Week 15", "Phase 8: Fast-Track Waiver", "Receive formal Notice of Proposal (NOP). Immediately execute Section 28(3) statutory waiver of representations, collapsing 28-day wait to 48 hours.", "Nominated Ind"),
        ("Week 16", "Phase 9: DPS Activation", "Receive CQC Certificate of Registration. Register on Luton Borough Council ProContract portal; apply for Supported Living DPS Lot 1 & BLMK ICB CHC.", "Executive Team")
    ]

    row_y = ty - 42
    for idx, (wk, ph, desc, lead) in enumerate(phases):
        bg = (0.97, 0.98, 1.0) if idx % 2 == 0 else (1.0, 1.0, 1.0)
        p7.set_fill_color(bg[0], bg[1], bg[2])
        p7.draw_rect(p7.mx, row_y, p7.cw, 40, fill=True)
        p7.set_stroke_color(0.85, 0.88, 0.92)
        p7.draw_line(p7.mx, row_y, p7.mx + p7.cw, row_y, stroke_w=0.4)

        p7.set_fill_color(0.06, 0.12, 0.21)
        p7.draw_text(wk, p7.mx + 8, row_y + 24, font="F2", size=8.0)
        p7.draw_text(ph, p7.mx + 60, row_y + 24, font="F2", size=7.8)
        p7.draw_wrapped_text(desc, p7.mx + 210, row_y + 28, 220, font="F1", size=7.2, leading=9.2)
        p7.set_fill_color(0.76, 0.61, 0.22)
        p7.draw_text(lead, p7.mx + 440, row_y + 24, font="F2", size=7.8)

        row_y -= 42

    # Bottom Callout Box
    p7.set_fill_color(0.06, 0.12, 0.21)
    p7.draw_rect(p7.mx, 55, p7.cw, 65, fill=True)
    p7.set_fill_color(0.76, 0.61, 0.22)
    p7.draw_text("EXECUTIVE AUTHORIZATION & IMPLEMENTATION MANDATE", p7.mx + 12, 105, font="F2", size=9.0)
    p7.set_fill_color(1.0, 1.0, 1.0)
    p7.draw_text("By order of the Board of Directors of ADOV Care Group LIMITED and FAIRYTALES GROUP.", p7.mx + 12, 92, font="F1", size=8.0)
    p7.draw_text("This statutory compliance document constitutes the definitive operational roadmap for all regulatory filings.", p7.mx + 12, 80, font="F1", size=8.0)
    p7.draw_text("Signed: ___________________________ (Nominated Individual)      Date: ___________________________", p7.mx + 12, 66, font="F2", size=8.0)

    p7.set_fill_color(0.55, 0.65, 0.75)
    p7.draw_text("Page 7 of 7 // CQC Statutory Compliance Dossier // ADOV Care Group LIMITED", p7.width / 2, 28, font="F1", size=7.5, align="center", max_w=p7.cw)

    doc.save()
    print(f"Generated PDF '{pdf_filename}'.")

def build_docx():
    docx_filename = "ADOV_Care_Group_CQC_Requirements_and_Fulfillment_Guide.docx"
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
    add_p("CQC REGISTRATION REQUIREMENTS & STATUTORY FULFILLMENT GUIDE", style="Subtitle", bold=True, size=26, color="C29B38", space_after=140)
    add_p("Comprehensive 10-Pillar Statutory Manual & 24-Point Audit Checklist under Health and Social Care Act 2008 & 2014 Regulations", style="Normal", italic=True, size=20, color="64748B", space_after=200)

    add_p("1. EXECUTIVE SUMMARY & STATUTORY AUTHORITY", style="Heading1", bold=True, size=28, color="0F1E36", space_after=100)
    add_p("This statutory compliance document defines the complete operational checklist, statutory evidence repository, and step-by-step fulfillment actions required for ADOV Care Group LIMITED to obtain Care Quality Commission (CQC) registration for the regulated activity of Personal Care (Health and Social Care Act 2008 Regulated Activities Regulations 2014) across 78 & 80 Marston Gardens, Luton (LU2 7DY).", space_after=140)

    add_p("2. 24-POINT STATUTORY AUDIT CHECKLIST", style="Heading1", bold=True, size=28, color="0F1E36", space_after=100)
    checklist = [
        "Domain A (Governance & Fit and Proper): CQC Enhanced DBS checks with Adult Barred List via First Advantage (<12 months).",
        "Domain A (Governance & Fit and Proper): Stamped and signed NHS GP Medical Fitness Declaration Forms for Nominated Individual & RM.",
        "Domain A (Governance & Fit and Proper): Registered Manager Level 5 Diploma in Leadership & Management for Adult Care (RQF).",
        "Domain A (Governance & Fit and Proper): Section 181 Oliver McGowan Mandatory Training (Tier 1 & 2) & BILD-accredited PBS Level 3.",
        "Domain B (Statement of Purpose): Part 1 Provider Details, legal identity, SIC 88100, and Nominated Individual details.",
        "Domain B (Statement of Purpose): Part 2 Aims & Objectives, Active Support framework, and independence ethos.",
        "Domain B (Statement of Purpose): Part 3 Physical campus facilities at 78 & 80 Marston Gardens (8 suites, large sensory gardens).",
        "Domain B (Statement of Purpose): Part 4 Personal Care scope aligned with CQC 'Right Support, Right Care, Right Culture'.",
        "Domain C (Financial Viability): ICAEW / ACCA Chartered Accountant Declaration on accountancy firm letterhead.",
        "Domain C (Financial Viability): 12-Month itemized monthly cash flow forecast showing steady-state OpEx of £53,018/mo.",
        "Domain C (Financial Viability): Proof of £75,000 - £100,000 unencumbered liquid working capital in company bank account.",
        "Domain D (Core Policies): Safeguarding Adults at Risk Policy aligned to Luton Safeguarding Adults Board (LSAB) s.42 procedures.",
        "Domain D (Core Policies): Mental Capacity Act 2005 & Deprivation of Liberty Safeguards (DoLS / LPS) policy & Best Interests protocol.",
        "Domain D (Core Policies): Safe Management of Medicines Policy adhering to NICE SC1, cloud eMAR, and BS 2881 CD cabinet.",
        "Domain D (Core Policies): Infection Prevention & Control (IPC) policy & commercial HTM 01-04 laundry decontamination cycle.",
        "Domain D (Core Policies): Health, Safety, COSHH, Legionella ACoP L8 monitoring & TMV3 thermostatic mixing valves (<43°C).",
        "Domain D (Core Policies): Whistleblowing Policy complying with PIDA 1998 with designated Freedom to Speak Up Guardian.",
        "Domain D (Core Policies): Statutory Duty of Candour (Regulation 20) with strict 10-day formal apology and investigation protocol.",
        "Domain E (Premises Safety): BS 5839-1 Category L1 addressable fire alarm system with BAFE commissioning certificate.",
        "Domain E (Premises Safety): BS 5266-1 3-hour emergency lighting installation & commissioning certificate.",
        "Domain E (Premises Safety): FD30S fire-resisting doorsets with intumescent cold smoke seals and magnetic hold-opens.",
        "Domain E (Premises Safety): WRAS-approved TMV3 valves calibrated to fail-safe shut-off at <43°C on all hot water outlets.",
        "Domain E (Premises Safety): Satisfactory NICEIC Electrical Installation Condition Report (EICR) & Gas Safe CP12 certificate.",
        "Domain F (Tenancy & Waiver): Strict separation of Housing (PropCo AST) from Personal Care (OpCo) satisfying Real Tenancy test.",
        "Domain F (Tenancy & Waiver): Explicit 'Freedom of Choice' tenancy clause & individual bedroom door cylinder keys.",
        "Domain F (Tenancy & Waiver): Concurrent submission of Provider & Registered Manager applications on CQC Provider Portal.",
        "Domain F (Tenancy & Waiver): Section 28(3) Fast-Track Statutory Waiver of representations letter executed to cut 28 days."
    ]
    for c_item in checklist:
        add_bullet(c_item)

    add_p("3. THE 10 STATUTORY REQUIREMENT PILLARS", style="Heading1", bold=True, size=28, color="0F1E36", space_after=100)
    pillars = [
        ("Pillar 1: Fit and Proper Person Requirements (Regs 4, 5 & 6)", "Directors and Nominated Individual must have clean CQC Enhanced DBS checks, GP medical fitness sign-off, and verified solvency."),
        ("Pillar 2: Registered Manager Competency (Reg 7)", "Level 5 Diploma in Adult Care, Section 181 Oliver McGowan training, and BILD PBS certification with 3+ years experience."),
        ("Pillar 3: Statutory Statement of Purpose (Reg 12)", "The 4-part legal document defining corporate details, aims, physical locations, and Right Support Right Care Right Culture ethos."),
        ("Pillar 4: Financial Viability Solvency Assurance (Reg 13)", "ICAEW/ACCA Chartered Accountant viability letter, 12-month cashflow, and £75k-£100k liquid working capital buffer."),
        ("Pillar 5: The 7 Core Statutory Quality Policies (Reg 17)", "Safeguarding (s.42), MCA/DoLS, Medicines (NICE SC1), IPC (HTM 01-04), TMV3 Anti-Scald, Whistleblowing (PIDA 1998), Duty of Candour (Reg 20)."),
        ("Pillar 6: Physical Premises & Environmental Safety (Reg 15)", "BS 5839 Cat L1 fire detection, BS 5266 emergency lighting, FD30S fire doors, TMV3 valves (<43°C), NICEIC EICR, secure gardens."),
        ("Pillar 7: The Real Tenancy Test & Housing Separation", "Independent tenancy agreement with PropCo, separate care contract with OpCo, and tenant freedom of choice to prevent s.10 HSCA care home prosecution."),
        ("Pillar 8: CQC Provider Portal Evidence Upload Pack", "Concurrent application submission, standardized file naming, text-searchable PDFs (<15MB each), and pre-flight validation."),
        ("Pillar 9: Registered Manager Competency Interview Defense", "Model defense answers for the 5 CQC scenarios: PBS de-escalation, safeguarding abuse allegation, MCA covert meds, meds error Duty of Candour, understaffing."),
        ("Pillar 10: Section 28(3) Fast-Track Statutory Waiver", "Executing the statutory waiver of representations upon Notice of Proposal (NOP) receipt to collapse the 28-day waiting period to 48-72 hours.")
    ]
    for p_title, p_desc in pillars:
        add_p(p_title, style="Heading2", bold=True, size=22, color="C29B38", space_after=60)
        add_p(p_desc, space_after=120)

    add_p("4. MASTER 16-WEEK CHRONOLOGICAL IMPLEMENTATION ROADMAP", style="Heading1", bold=True, size=28, color="0F1E36", space_after=100)
    timeline = [
        "Weeks 1 - 2 (Governance & DBS): Order CQC Enhanced DBS checks via First Advantage; book GP appointments; pass board resolutions.",
        "Weeks 3 - 4 (Management Vetting): Contract Registered Manager holding Level 5 Diploma; verify Oliver McGowan & PBS certs.",
        "Weeks 5 - 6 (Policies & Statement): Draft Statement of Purpose Parts 1 to 4; finalize 7 core policies; secure ICAEW viability letter.",
        "Weeks 7 - 8 (Premises Fit-Out): Commission BS 5839 Cat L1 fire alarm, BS 5266 emergency lighting, TMV3 valves, and NICEIC EICR.",
        "Weeks 9 - 10 (Portal Submission): Submit Provider & Manager applications simultaneously on CQC portal; clear validation.",
        "Weeks 11 - 12 (CQC Assessment): CQC Inspector reviews policies and accountant letter; resolve any RFIs within 48 hours.",
        "Weeks 13 - 14 (Clinical Interview & Site Visit): RM defends 5 clinical scenarios in 90-min interview; CQC inspects 78 & 80 campus.",
        "Week 15 (Notice of Proposal & Fast-Track): Receive NOP; execute Section 28(3) statutory waiver immediately; collapse 28-day wait.",
        "Week 16 (Registration & DPS Activation): Receive CQC Registration Certificate; onboard onto Luton Council Supported Living DPS."
    ]
    for t_item in timeline:
        add_bullet(t_item)

    # Packaging openxml docx
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
