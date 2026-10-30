#!/usr/bin/env python3
"""
ADOV Care Group - Document Pack 1: Master Document Checklist & Execution Binder
"""

import sys, os, zlib, zipfile
from build_statutory_document_packs import SimplePDF

def build_pdf():
    doc = SimplePDF("ADOV_Care_Group_Master_Document_Checklist.pdf", "MASTER STATUTORY DOCUMENT CHECKLIST")
    
    # -------------------------------------------------------------
    # PAGE 1: COVER & EXECUTIVE INVENTORY
    # -------------------------------------------------------------
    p1 = doc.add_page(is_cover=True)
    p1.set_fill_color(0.04, 0.08, 0.16)
    p1.draw_rect(0, 0, p1.width, p1.height)
    
    # Gold border
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_rect(24, 24, p1.width - 48, p1.height - 48, fill=False, stroke=True, stroke_w=1.5)
    p1.set_stroke_color(0.55, 0.42, 0.12)
    p1.draw_rect(28, 28, p1.width - 56, p1.height - 56, fill=False, stroke=True, stroke_w=0.6)
    
    # Pill
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_rect(54, p1.height - 80, 240, 20, fill=True)
    p1.set_fill_color(0.04, 0.08, 0.16)
    p1.draw_text("STATUTORY EXECUTION DOSSIER", 62, p1.height - 67, font="F2", size=8.5)
    
    # Titles
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("ADOV CARE GROUP", 54, p1.height - 125, font="F2", size=24.0)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_line(54, p1.height - 138, p1.width - 54, p1.height - 138, stroke_w=1.5)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("MASTER STATUTORY DOCUMENT CHECKLIST", 54, p1.height - 162, font="F2", size=14.0)
    p1.set_fill_color(0.80, 0.88, 1.0)
    p1.draw_text("Complete Regulatory, Planning, Corporate, Building Safety & Commissioning Inventory", 54, p1.height - 180, font="F1", size=10.0)
    p1.draw_text("Target Assets: 78, 80 & 82 Marston Gardens, Luton, LU2 7DY", 54, p1.height - 198, font="F1", size=8.5)
    
    # Metadata Card
    p1.set_fill_color(0.08, 0.14, 0.26)
    p1.set_stroke_color(0.25, 0.38, 0.60)
    p1.draw_rect(54, 340, p1.width - 108, 260, fill=True, stroke=True, stroke_w=1.0)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("DOCUMENT SUITE LIFECYCLE & SUBMISSION STAGES", 70, 575, font="F2", size=10.0)
    p1.draw_line(70, 567, p1.width - 70, 567, stroke_w=0.8)
    
    stages = [
        ("Phase 1: Corporate & Tax Pack", "Companies House, HMRC, FRI commercial leases, AST for 82, Board resolutions."),
        ("Phase 2: Statutory Town Planning Pack", "Dual Section 192 CLPUD applications, planning statements, parking evidence to Luton Council."),
        ("Phase 3: Property Compliance & Safety Pack", "BS 5839-1 Cat L1 fire system, FD30S doors, EICR, CP12 gas, TMV3 valves, HTM 01-04 laundry."),
        ("Phase 4: CQC Provider Registration Pack", "Statement of Purpose (SoP), Level 5 RM vetting, Nominated Individual, 42 core policies."),
        ("Phase 5: Local Authority Commissioning Pack", "Luton Council ProContract DPS (AT1115), BLMK ICB CHC, Supported Living AST, SEA Housing Benefit.")
    ]
    cur_sy = 548
    for s_title, s_desc in stages:
        p1.set_fill_color(0.85, 0.65, 0.18)
        p1.draw_text(s_title, 70, cur_sy, font="F2", size=7.8)
        cur_sy -= 10
        p1.set_fill_color(0.90, 0.94, 1.0)
        cur_sy = p1.draw_wrapped_text(s_desc, 70, cur_sy, p1.width - 140, font="F1", size=7.2, leading=9.5)
        cur_sy -= 5
        
    # Sponsor Box
    p1.set_fill_color(0.12, 0.18, 0.32)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_rect(54, 140, p1.width - 108, 160, fill=True, stroke=True, stroke_w=1.2)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("PROJECT PLANNED BY ABDULLAHMAMUN.COM", 70, 275, font="F2", size=11.0)
    p1.draw_line(70, 267, p1.width - 70, 267, stroke_w=0.6)
    
    meta_rows = [
        ("Parent Holding Entity:", "FAIRYTALES GROUP (Trading Name of Mamun Limited / 100% Parent)"),
        ("Property Holding Entity:", "ADOV LIMITED (Freehold Owner: 78 & 82 Marston Gardens)"),
        ("Operating Care Entity:", "ADOV Care Group LIMITED (CQC Registered Provider)"),
        ("Target Service Cohort:", "Adults with Autism, Complex Learning Disabilities & Challenging Behaviour (PBS)"),
        ("Executive Living Strategy:", "Beneficiary resides at 82 Marston Gardens under AST (BIK NIL, +£32k/yr surplus)")
    ]
    cur_my = 250
    for l, v in meta_rows:
        p1.set_fill_color(0.70, 0.80, 0.95)
        p1.draw_text(l, 70, cur_my, font="F2", size=7.5)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_text(v, 205, cur_my, font="F1", size=7.5)
        cur_my -= 16.0
        
    p1.set_fill_color(0.60, 0.70, 0.85)
    p1.draw_text("PRINT-READY MASTER CHECKLIST // CONFIDENTIAL EXECUTIVE BINDER // OCTOBER 2026", 54, 50, font="F1", size=7.2)

    # -------------------------------------------------------------
    # PAGE 2: DOMAIN 1 (CORPORATE) & DOMAIN 2 (PLANNING)
    # -------------------------------------------------------------
    p2 = doc.add_page()
    p2.draw_header_banner("D1", "DOMAIN 1: CORPORATE & DOMAIN 2: TOWN PLANNING", "STATUTORY CHECKLIST")
    
    # Domain 1 Box
    p2.set_fill_color(0.98, 0.98, 1.0)
    p2.set_stroke_color(0.20, 0.35, 0.60)
    p2.draw_rect(36, 440, p2.cw, 335, fill=True, stroke=True, stroke_w=1.0)
    p2.set_fill_color(0.10, 0.20, 0.40)
    p2.draw_rect(36, 750, p2.cw, 25, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    p2.draw_text("1. CORPORATE STRUCTURING, LEASES & HMRC TAX GOVERNANCE", 46, 758, font="F2", size=8.5)
    
    headers = ["Status", "Document Name & Purpose", "When to Use", "Where to Submit", "Signatories"]
    hw = [35, 175, 105, 105, 103]
    
    p2.set_fill_color(0.15, 0.25, 0.45)
    p2.draw_rect(36, 730, p2.cw, 16, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    hx = 36
    for i, h in enumerate(headers):
        p2.draw_text(h, hx + 4, 735, font="F2", size=6.8)
        hx += hw[i]
        
    corp_docs = [
        ("[ ]", "Certificate of Incorporation - ADOV Care Group Ltd", "Week 1 (Day 1)", "Companies House / Bank", "Director / UBO"),
        ("[ ]", "10-Year FRI Commercial Lease (78 Marston Gdns - £65k/yr)", "Week 2 (Pre-Planning)", "ADOV Ltd & OpCo Records", "PropCo & OpCo Directors"),
        ("[ ]", "10-Year FRI Commercial Lease (80 Marston Gdns - £50k/yr)", "Week 2 (Pre-Planning)", "Director & OpCo Records", "Owner & OpCo Director"),
        ("[ ]", "Assured Shorthold Tenancy (82 Marston Gdns - £1.5k/mo)", "Week 3 (Pre-Occupation)", "HMRC BIK Exemption Audit", "ADOV Ltd & Director"),
        ("[ ]", "Board Written Resolutions (Fairytales Group & ADOV Ltd)", "Week 1 (Corporate Kickoff)", "Group Company Registers", "All Corporate Directors"),
        ("[ ]", "Corporate Bank Accounts & £20k Working Capital Reserve", "Weeks 2-4", "Commercial Bank (Barclays/NatWest)", "Managing Director")
    ]
    cur_y = 712
    for st, name, when, where, sig in corp_docs:
        p2.set_fill_color(0.96, 0.98, 1.0)
        p2.draw_rect(36, cur_y - 3, p2.cw, 22, fill=True)
        p2.set_fill_color(0.10, 0.20, 0.40)
        p2.draw_text(st, 42, cur_y + 4, font="F2", size=7.5)
        p2.draw_text(name, 75, cur_y + 4, font="F2", size=6.8)
        p2.set_fill_color(0.25, 0.30, 0.40)
        p2.draw_text(when, 250, cur_y + 4, font="F1", size=6.5)
        p2.draw_text(where, 355, cur_y + 4, font="F1", size=6.5)
        p2.draw_text(sig, 460, cur_y + 4, font="F1", size=6.5)
        cur_y -= 25.0

    # Domain 2 Box
    p2.set_fill_color(0.97, 0.99, 0.97)
    p2.set_stroke_color(0.15, 0.55, 0.25)
    p2.draw_rect(36, 42, p2.cw, 375, fill=True, stroke=True, stroke_w=1.0)
    p2.set_fill_color(0.12, 0.45, 0.20)
    p2.draw_rect(36, 392, p2.cw, 25, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    p2.draw_text("2. STATUTORY TOWN PLANNING & HIGHWAYS COMPLIANCE (CLASS C3b)", 46, 400, font="F2", size=8.5)
    
    p2.set_fill_color(0.15, 0.25, 0.45)
    p2.draw_rect(36, 372, p2.cw, 16, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    hx = 36
    for i, h in enumerate(headers):
        p2.draw_text(h, hx + 4, 377, font="F2", size=6.8)
        hx += hw[i]
        
    plan_docs = [
        ("[ ]", "Section 192 CLPUD Application 1 (78 Marston Gdns - 5 Beds)", "Week 5 (Statutory Lodgment)", "Luton Council Planning Portal", "Planning Agent / OpCo"),
        ("[ ]", "Section 192 CLPUD Application 2 (80 Marston Gdns - 3 Beds)", "Week 5 (Statutory Lodgment)", "Luton Council Planning Portal", "Planning Agent / OpCo"),
        ("[ ]", "Statutory Planning Statement (TCPA s.55 & North Devon Case)", "Week 5 (Accompanying S.192)", "Luton Council Planning Dept", "Planning Counsel"),
        ("[ ]", "Highways & Parking Assessment (8 Cars + 2 Garages LLP32)", "Week 5 (Highways Defense)", "Luton Highways Development", "Surveyor / Agent"),
        ("[ ]", "Existing & Proposed 1:50 Architectural Floor Plans & Elevations", "Week 4 (Survey Completion)", "Luton Planning & Building Control", "Chartered Architect"),
        ("[ ]", "OS Site Location Plan (1:1250) & Block Plan (1:500)", "Week 4", "Luton Council Planning Portal", "Architect / Surveyor"),
        ("[ ]", "Section 192 Certificate of Lawfulness Decision Notices", "Week 13 (Statutory Determination)", "OpCo Records & CQC Portal", "Luton Borough Council")
    ]
    cur_py = 354
    for st, name, when, where, sig in plan_docs:
        p2.set_fill_color(0.96, 0.98, 1.0)
        p2.draw_rect(36, cur_py - 3, p2.cw, 20, fill=True)
        p2.set_fill_color(0.12, 0.45, 0.20)
        p2.draw_text(st, 42, cur_py + 3, font="F2", size=7.5)
        p2.draw_text(name, 75, cur_py + 3, font="F2", size=6.8)
        p2.set_fill_color(0.25, 0.30, 0.40)
        p2.draw_text(when, 250, cur_py + 3, font="F1", size=6.5)
        p2.draw_text(where, 355, cur_py + 3, font="F1", size=6.5)
        p2.draw_text(sig, 460, cur_py + 3, font="F1", size=6.5)
        cur_py -= 23.0

    # -------------------------------------------------------------
    # PAGE 3: DOMAIN 3 (PROPERTY & LIFE SAFETY) & DOMAIN 4 (CQC)
    # -------------------------------------------------------------
    p3 = doc.add_page()
    p3.draw_header_banner("D2", "DOMAIN 3: PROPERTY SAFETY & DOMAIN 4: CQC LICENSING", "STATUTORY CHECKLIST")
    
    # Domain 3 Box
    p3.set_fill_color(0.98, 0.98, 1.0)
    p3.set_stroke_color(0.20, 0.35, 0.60)
    p3.draw_rect(36, 420, p3.cw, 355, fill=True, stroke=True, stroke_w=1.0)
    p3.set_fill_color(0.10, 0.20, 0.40)
    p3.draw_rect(36, 750, p3.cw, 25, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("3. PROPERTY COMPLIANCE, BUILDING REGULATIONS & LIFE SAFETY", 46, 758, font="F2", size=8.5)
    
    p3.set_fill_color(0.15, 0.25, 0.45)
    p3.draw_rect(36, 730, p3.cw, 16, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    hx = 36
    for i, h in enumerate(headers):
        p3.draw_text(h, hx + 4, 735, font="F2", size=6.8)
        hx += hw[i]
        
    prop_docs = [
        ("[ ]", "BS 5839-1 Category L1 Fire Alarm Installation & Commissioning Cert", "Week 16 (Post-Fitout)", "Building Control & CQC Inspector", "NICEIC / BAFE Contractor"),
        ("[ ]", "Fire Risk Assessment (FRA) under Regulatory Reform Order 2005", "Week 16 (Pre-Occupation)", "Bedfordshire Fire & CQC", "Certified Fire Risk Assessor"),
        ("[ ]", "FD30S Fire Doorset Installation Compliance Certificates (14 Doors)", "Week 15 (Carpentry Signoff)", "Building Control Inspector", "FIRAS Certified Joiner"),
        ("[ ]", "Electrical Installation Condition Report (EICR - Satisfactory)", "Week 15", "Building Control & Insurance", "NICEIC Approved Contractor"),
        ("[ ]", "Gas Safety CP12 Landlord Certificate (Commercial Boilers)", "Week 15", "OpCo & Tenant Records", "Gas Safe Engineer"),
        ("[ ]", "TMV3 Thermostatic Mixing Valve Calibration Certificate (Max 41°C)", "Week 16 (Plumbing Signoff)", "CQC Health & Safety Audit", "WRAS Plumber"),
        ("[ ]", "HTM 01-04 Commercial Laundry Decontamination Validation Cert", "Week 16", "CQC Infection Control Audit", "Laundry Equipment Engineer"),
        ("[ ]", "Legionella Risk Assessment & Temperature Logbook", "Week 16", "CQC & Environmental Health", "Water Hygiene Assessor")
    ]
    cur_y3 = 712
    for st, name, when, where, sig in prop_docs:
        p3.set_fill_color(0.96, 0.98, 1.0)
        p3.draw_rect(36, cur_y3 - 3, p3.cw, 20, fill=True)
        p3.set_fill_color(0.10, 0.20, 0.40)
        p3.draw_text(st, 42, cur_y3 + 3, font="F2", size=7.5)
        p3.draw_text(name, 75, cur_y3 + 3, font="F2", size=6.8)
        p3.set_fill_color(0.25, 0.30, 0.40)
        p3.draw_text(when, 250, cur_y3 + 3, font="F1", size=6.5)
        p3.draw_text(where, 355, cur_y3 + 3, font="F1", size=6.5)
        p3.draw_text(sig, 460, cur_y3 + 3, font="F1", size=6.5)
        cur_y3 -= 23.0

    # Domain 4 Box (CQC)
    p3.set_fill_color(0.97, 0.99, 0.97)
    p3.set_stroke_color(0.15, 0.55, 0.25)
    p3.draw_rect(36, 42, p3.cw, 355, fill=True, stroke=True, stroke_w=1.0)
    p3.set_fill_color(0.12, 0.45, 0.20)
    p3.draw_rect(36, 372, p3.cw, 25, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("4. CARE QUALITY COMMISSION (CQC) REGISTRATION & CLINICAL GOVERNANCE", 46, 380, font="F2", size=8.5)
    
    p3.set_fill_color(0.15, 0.25, 0.45)
    p3.draw_rect(36, 352, p3.cw, 16, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    hx = 36
    for i, h in enumerate(headers):
        p3.draw_text(h, hx + 4, 357, font="F2", size=6.8)
        hx += hw[i]
        
    cqc_docs = [
        ("[ ]", "CQC Statement of Purpose (SoP - Reg 12 Registration Regs)", "Week 7 (Portal Submission)", "CQC Provider Portal", "Nominated Individual & RM"),
        ("[ ]", "Registered Manager Level 5 Diploma & Enhanced DBS (Reg 7)", "Week 6 (RM Verification)", "CQC Provider Portal", "Registered Manager"),
        ("[ ]", "Nominated Individual Statutory Appointment Resolution (Reg 6)", "Week 6 (Board Resolution)", "CQC Provider Portal", "Fairytales Group Board"),
        ("[ ]", "Financial Viability Statement & 5-Year Cashflow Model", "Week 7", "CQC Provider Portal", "Chartered Accountant / Bank"),
        ("[ ]", "42 Core Operational Policies (Safeguarding, PBS, Meds, MCA)", "Week 7 (Full Submission)", "CQC Regulatory Assessor", "Registered Manager"),
        ("[ ]", "Oliver McGowan Mandatory Training Certs (All 14 Staff)", "Weeks 18-22", "CQC Inspection & Luton Council", "Certified PBS Trainer"),
        ("[ ]", "CQC Certificate of Registration (Personal Care - Supported Living)", "Week 24 (Statutory Approval)", "Commissioning Teams & Display", "Care Quality Commission")
    ]
    cur_cy3 = 334
    for st, name, when, where, sig in cqc_docs:
        p3.set_fill_color(0.96, 0.98, 1.0)
        p3.draw_rect(36, cur_cy3 - 3, p3.cw, 20, fill=True)
        p3.set_fill_color(0.12, 0.45, 0.20)
        p3.draw_text(st, 42, cur_cy3 + 3, font="F2", size=7.5)
        p3.draw_text(name, 75, cur_cy3 + 3, font="F2", size=6.8)
        p3.set_fill_color(0.25, 0.30, 0.40)
        p3.draw_text(when, 250, cur_cy3 + 3, font="F1", size=6.5)
        p3.draw_text(where, 355, cur_cy3 + 3, font="F1", size=6.5)
        p3.draw_text(sig, 460, cur_cy3 + 3, font="F1", size=6.5)
        cur_cy3 -= 23.0

    # -------------------------------------------------------------
    # PAGE 4: DOMAIN 5 (COMMISSIONING) & EXECUTION PROTOCOL
    # -------------------------------------------------------------
    p4 = doc.add_page()
    p4.draw_header_banner("D3", "DOMAIN 5: COMMISSIONING & STATUTORY SIGN-OFF", "STATUTORY CHECKLIST")
    
    # Domain 5 Box
    p4.set_fill_color(0.98, 0.98, 1.0)
    p4.set_stroke_color(0.20, 0.35, 0.60)
    p4.draw_rect(36, 420, p4.cw, 355, fill=True, stroke=True, stroke_w=1.0)
    p4.set_fill_color(0.10, 0.20, 0.40)
    p4.draw_rect(36, 750, p4.cw, 25, fill=True)
    p4.set_fill_color(1.0, 1.0, 1.0)
    p4.draw_text("5. LOCAL AUTHORITY COMMISSIONING & RESIDENT ADMISSIONS", 46, 758, font="F2", size=8.5)
    
    p4.set_fill_color(0.15, 0.25, 0.45)
    p4.draw_rect(36, 730, p4.cw, 16, fill=True)
    p4.set_fill_color(1.0, 1.0, 1.0)
    hx = 36
    for i, h in enumerate(headers):
        p4.draw_text(h, hx + 4, 735, font="F2", size=6.8)
        hx += hw[i]
        
    comm_docs = [
        ("[ ]", "Luton Borough Council ProContract DPS (Framework AT1115)", "Week 20 (DPS Onboarding)", "Luton Procurement Portal", "Commercial Director"),
        ("[ ]", "NHS BLMK ICB Continuing Healthcare (CHC) Framework Contract", "Week 20", "BLMK Procurement Hub", "Commercial Director"),
        ("[ ]", "Individual Placement Agreement (IPA) Template (£2,500/week)", "Week 24 (Prior to Intake)", "Luton Council / BLMK ICB", "Council Brokerage & OpCo"),
        ("[ ]", "Supported Living Assured Shorthold Tenancy Agreement (Resident AST)", "Week 25 (Admission Day)", "Service User / Deputy / Appointee", "Tenant & Landlord OpCo"),
        ("[ ]", "Separate Care & Support Agreement (CQC Housing with Care)", "Week 25 (Admission Day)", "Service User / Social Worker", "Service User & RM"),
        ("[ ]", "Supported Exempt Accommodation (SEA) Housing Benefit Claim", "Week 25 (Day 1 Admission)", "Luton Revenues & Benefits Dept", "Appointee / OpCo"),
        ("[ ]", "Pre-Admission Multi-Disciplinary PBS Transition Protocol", "Weeks 21-24", "Charter House ALDT & Family", "Registered Manager / BCBA")
    ]
    cur_y4 = 712
    for st, name, when, where, sig in comm_docs:
        p4.set_fill_color(0.96, 0.98, 1.0)
        p4.draw_rect(36, cur_y4 - 3, p4.cw, 20, fill=True)
        p4.set_fill_color(0.10, 0.20, 0.40)
        p4.draw_text(st, 42, cur_y4 + 3, font="F2", size=7.5)
        p4.draw_text(name, 75, cur_y4 + 3, font="F2", size=6.8)
        p4.set_fill_color(0.25, 0.30, 0.40)
        p4.draw_text(when, 250, cur_y4 + 3, font="F1", size=6.5)
        p4.draw_text(where, 355, cur_y4 + 3, font="F1", size=6.5)
        p4.draw_text(sig, 460, cur_y4 + 3, font="F1", size=6.5)
        cur_y4 -= 23.0

    # Step-by-Step Strategic Roadmap Box
    p4.set_fill_color(0.06, 0.10, 0.18)
    p4.set_stroke_color(0.85, 0.65, 0.18)
    p4.draw_rect(36, 175, p4.cw, 225, fill=True, stroke=True, stroke_w=1.2)
    
    p4.set_fill_color(0.85, 0.65, 0.18)
    p4.draw_text("EXECUTIVE STEP-BY-STEP SUBMISSION TIMELINE", 50, 378, font="F2", size=10.0)
    p4.draw_line(50, 370, p4.width - 50, 370, stroke_w=0.6)
    
    steps = [
        ("Step 1 (Weeks 1-4): Corporate Governance & Lease Execution", "Incorporate ADOV Care Group Ltd, execute commercial FRI leases for 78 & 80, execute AST for 82 (BIK NIL), headhunt Level 5 RM."),
        ("Step 2 (Weeks 5-8): Dual S.192 CLPUD & CQC Portal Submission", "Submit Dual CLPUDs to Luton Council with planning statements. Concurrently lodge CQC provider application with 42 policies."),
        ("Step 3 (Weeks 9-16): CapEx Refurbishment & Safety Certification", "Complete building works (BS 5839-1 Cat L1, FD30S doors, wetroom TMV3 upgrade, Doc E soundproofing). Obtain all completion certs."),
        ("Step 4 (Weeks 17-20): CQC Statutory Interviews & DPS Submission", "RM and NI clear CQC Fit & Proper interviews. Submit tender for Luton Borough Council ProContract DPS (AT1115)."),
        ("Step 5 (Weeks 21-24): CQC Certificate Issuance & Brokerage Engagement", "Receive CQC Certificate of Registration. Host showcase visits with Charter House ALDT and Transitions 16-25 Team."),
        ("Step 6 (Weeks 25-26): Zero-Void Admissions & Revenue Activation", "Execute resident ASTs and Care Agreements. Submit SEA Housing Benefit claims. Activate £1,043,328 revenue and £523,328 cashflow.")
    ]
    cur_step_y = 354
    for st_title, st_desc in steps:
        p4.set_fill_color(0.85, 0.65, 0.18)
        p4.draw_text(st_title, 50, cur_step_y, font="F2", size=7.2)
        cur_step_y -= 9
        p4.set_fill_color(0.90, 0.94, 1.0)
        cur_step_y = p4.draw_wrapped_text(st_desc, 50, cur_step_y, p4.cw - 28, font="F1", size=6.8, leading=8.8)
        cur_step_y -= 4

    # Sign-off Box
    p4.set_fill_color(0.97, 0.99, 0.97)
    p4.set_stroke_color(0.15, 0.55, 0.25)
    p4.draw_rect(36, 42, p4.cw, 115, fill=True, stroke=True, stroke_w=1.0)
    p4.set_fill_color(0.12, 0.45, 0.20)
    p4.draw_rect(36, 132, p4.cw, 25, fill=True)
    p4.set_fill_color(1.0, 1.0, 1.0)
    p4.draw_text("EXECUTIVE AUDIT SIGN-OFF // FAIRYTALES GROUP & ADOV LIMITED", 46, 140, font="F2", size=9.0)
    
    p4.set_fill_color(0.15, 0.20, 0.25)
    sign_text = (
        "This Master Document Checklist has been formulated by AbdullahMamun.com for FAIRYTALES GROUP and ADOV LIMITED. "
        "All statutory, regulatory, planning, and tax filings identified herein are required under UK legislation. "
        "Completion of each milestone unlocks subsequent operational phases, ensuring complete legal immunity and commercial success."
    )
    p4.draw_wrapped_text(sign_text, 46, 122, p4.cw - 20, font="F1", size=7.2, leading=9.2)

    doc.save()

def build_docx():
    filename = "ADOV_Care_Group_Master_Document_Checklist.docx"
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
        '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/><w:color w:val="1E293B"/></w:rPr></w:rPrDefault></w:docDefaults>'
        '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:rPr><w:b/><w:color w:val="0F1A2E"/><w:sz w:val="34"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:rPr><w:b/><w:color w:val="1E3A8A"/><w:sz w:val="26"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:rPr><w:b/><w:color w:val="D97706"/><w:sz w:val="22"/></w:rPr></w:style>'
        '</w:styles>')
        
    doc_body = []
    def add_p(text, style=None, bold=False, color=None, space_after=120):
        r_pr = "<w:rPr>"
        if bold: r_pr += "<w:b/>"
        if color: r_pr += f'<w:color w:val="{color}"/>'
        r_pr += "</w:rPr>"
        p_pr = "<w:pPr>"
        if style: p_pr += f'<w:pStyle w:val="{style}"/>'
        p_pr += f'<w:spacing w:after="{space_after}"/>'
        p_pr += "</w:pPr>"
        safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        doc_body.append(f'<w:p>{p_pr}<w:r>{r_pr}<w:t>{safe}</w:t></w:r></w:p>')

    def add_bullet(text):
        safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        p = f'<w:p><w:pPr><w:pStyle w:val="ListParagraph"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr><w:spacing w:after="80"/></w:pPr><w:r><w:t>• {safe}</w:t></w:r></w:p>'
        doc_body.append(p)

    add_p("STATUTORY EXECUTION DOSSIER", style="Heading3", bold=True, color="D97706", space_after=60)
    add_p("ADOV CARE GROUP - MASTER STATUTORY DOCUMENT CHECKLIST", style="Heading1", bold=True, color="0F1A2E", space_after=80)
    add_p("Project Planned by AbdullahMamun.com", bold=True, color="D4AF37", space_after=100)
    add_p("Holding Entity: FAIRYTALES GROUP (Trading Name of Mamun Limited) // Asset Entity: ADOV LIMITED", color="555555", space_after=180)
    
    add_p("1. CORPORATE STRUCTURING, LEASES & HMRC TAX GOVERNANCE", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("[ ] Certificate of Incorporation - ADOV Care Group Ltd (Week 1 / Companies House)")
    add_bullet("[ ] 10-Year FRI Commercial Lease (78 Marston Gdns - £65k/yr) (Week 2 / ADOV Ltd to OpCo)")
    add_bullet("[ ] 10-Year FRI Commercial Lease (80 Marston Gdns - £50k/yr) (Week 2 / Director to OpCo)")
    add_bullet("[ ] Assured Shorthold Tenancy Agreement (82 Marston Gdns - £1.5k/mo) (Week 3 / Eliminates BIK)")
    add_bullet("[ ] Board Written Resolutions (Fairytales Group & ADOV Ltd) (Week 1 / Group Company Registers)")
    add_bullet("[ ] Corporate Commercial Bank Accounts & £20k Cash Reserve (Weeks 2-4)")

    add_p("2. STATUTORY TOWN PLANNING & HIGHWAYS COMPLIANCE (CLASS C3b)", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("[ ] Section 192 CLPUD Application 1 (78 Marston Gdns - 5 Beds) (Week 5 / Luton Planning)")
    add_bullet("[ ] Section 192 CLPUD Application 2 (80 Marston Gdns - 3 Beds) (Week 5 / Luton Planning)")
    add_bullet("[ ] Statutory Planning Statement (TCPA s.55 & North Devon Case Law) (Week 5)")
    add_bullet("[ ] Highways & Parking Evidence Statement (8 Cars + 2 Garages under Policy LLP32) (Week 5)")
    add_bullet("[ ] Existing & Proposed Architectural Floor Plans (1:50) & Elevations (Week 4)")
    add_bullet("[ ] Section 192 Certificate of Lawfulness Determination Notices (Week 13)")

    add_p("3. PROPERTY COMPLIANCE, BUILDING REGULATIONS & LIFE SAFETY", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("[ ] BS 5839-1 Category L1 Fire Alarm Installation & Commissioning Certificate (Week 16)")
    add_bullet("[ ] Fire Risk Assessment (FRA) under Regulatory Reform (Fire Safety) Order 2005 (Week 16)")
    add_bullet("[ ] FD30S Fire Doorset Compliance Certificates (14 Doorsets Fitted) (Week 15)")
    add_bullet("[ ] Electrical Installation Condition Report (EICR - Satisfactory) (Week 15)")
    add_bullet("[ ] Gas Safety CP12 Landlord Certificate (Commercial Boilers) (Week 15)")
    add_bullet("[ ] TMV3 Thermostatic Mixing Valve Calibration Certificate (Max 41°C) (Week 16)")
    add_bullet("[ ] HTM 01-04 Commercial Laundry Decontamination Validation Certificate (Week 16)")
    add_bullet("[ ] Legionella Risk Assessment & Temperature Logbook (Week 16)")

    add_p("4. CARE QUALITY COMMISSION (CQC) REGISTRATION & CLINICAL GOVERNANCE", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("[ ] CQC Statement of Purpose (SoP - Reg 12 Registration Regulations) (Week 7)")
    add_bullet("[ ] Registered Manager Level 5 Diploma & Enhanced DBS Verification (Reg 7) (Week 6)")
    add_bullet("[ ] Nominated Individual Statutory Appointment Resolution (Reg 6) (Week 6)")
    add_bullet("[ ] Financial Viability Statement & 5-Year Financial Forecast Model (Week 7)")
    add_bullet("[ ] 42 Core Operational Policies (Safeguarding Adults, PBS, Meds, MCA 2005) (Week 7)")
    add_bullet("[ ] Oliver McGowan Mandatory Training Certificates (All 14 Care Staff) (Weeks 18-22)")
    add_bullet("[ ] CQC Certificate of Registration (Personal Care in Supported Living) (Week 24)")

    add_p("5. LOCAL AUTHORITY COMMISSIONING & RESIDENT ADMISSIONS", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("[ ] Luton Borough Council ProContract DPS (Framework AT1115) Onboarding (Week 20)")
    add_bullet("[ ] NHS BLMK ICB Continuing Healthcare (CHC) Framework Contract (Week 20)")
    add_bullet("[ ] Individual Placement Agreement (IPA) Template (£2,500/week agreed) (Week 24)")
    add_bullet("[ ] Supported Living Assured Shorthold Tenancy Agreement (Resident AST) (Week 25)")
    add_bullet("[ ] Separate Care & Support Agreement (CQC Housing with Care Separation) (Week 25)")
    add_bullet("[ ] Supported Exempt Accommodation (SEA) Housing Benefit Claim Form (Week 25)")
    add_bullet("[ ] Pre-Admission Multi-Disciplinary PBS Transition Protocol (Weeks 21-24)")

    add_p("STEP-BY-STEP SUBMISSION TIMELINE", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("Phase 1 (Weeks 1-4): Corporate Governance & Lease Execution")
    add_bullet("Phase 2 (Weeks 5-8): Dual S.192 CLPUD & CQC Portal Lodgment")
    add_bullet("Phase 3 (Weeks 9-16): CapEx Refurbishment & Safety Certification")
    add_bullet("Phase 4 (Weeks 17-20): CQC Fit & Proper Interviews & DPS Tender")
    add_bullet("Phase 5 (Weeks 21-24): CQC Certificate Issuance & ALDT Showcases")
    add_bullet("Phase 6 (Weeks 25-26): Resident Admissions & £523k/yr Cashflow Activation")

    doc_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body>' + "".join(doc_body) +
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>'
        '</w:body></w:document>')
        
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as docx:
        docx.writestr('[Content_Types].xml', content_types)
        docx.writestr('_rels/.rels', pkg_rels)
        docx.writestr('word/_rels/document.xml.rels', doc_rels)
        docx.writestr('word/styles.xml', styles_xml)
        docx.writestr('word/document.xml', doc_xml)
    print(f"Generated DOCX '{filename}'.")

if __name__ == "__main__":
    build_pdf()
    build_docx()
