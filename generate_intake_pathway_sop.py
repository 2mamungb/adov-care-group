#!/usr/bin/env python3
"""
ADOV Care Group - Resident Intake Pathway & Commissioning SOP
Generates print-ready PDF and Word DOCX deliverables for Director and Registered Manager.
"""

import sys, os, zlib, zipfile
from build_statutory_document_packs import SimplePDF

def build_pdf():
    pdf_filename = "ADOV_Care_Group_Resident_Intake_Pathway_SOP.pdf"
    doc = SimplePDF(pdf_filename, "RESIDENT INTAKE PATHWAY & COMMISSIONING SOP")

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
    p1.draw_text("EXECUTIVE COMMISSIONING & INTAKE SOP", 62, p1.height - 67, font="F2", size=8.5)

    # Titles
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("ADOV CARE GROUP", 54, p1.height - 125, font="F2", size=24.0)
    p1.set_stroke_color(0.76, 0.61, 0.22)
    p1.draw_line(54, p1.height - 138, p1.width - 54, p1.height - 138, stroke_w=1.5)

    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("RESIDENT INTAKE PATHWAY & COMMISSIONING PLAYBOOK", 54, p1.height - 162, font="F2", size=13.0)
    p1.set_fill_color(0.85, 0.90, 0.98)
    p1.draw_text("Operational Strategy Manual for Managing Directors & Registered Managers", 54, p1.height - 180, font="F1", size=10.0)
    p1.draw_text("Target Campus: 78 & 80 Marston Gardens, Luton (LU2 7DY) // Supported Living (C3b)", 54, p1.height - 198, font="F1", size=8.5)

    # Executive Overview Box
    p1.set_fill_color(0.09, 0.16, 0.28)
    p1.set_stroke_color(0.25, 0.38, 0.60)
    p1.draw_rect(54, 330, p1.width - 108, 280, fill=True, stroke=True, stroke_w=1.0)

    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("EXECUTIVE INTAKE MANDATE & ZERO-VOID OPERATING PHILOSOPHY", 70, 585, font="F2", size=10.0)
    p1.draw_line(70, 577, p1.width - 70, 577, stroke_w=0.8)

    summary_bullets = [
        ("The Strategic Challenge", "Care businesses fail when they either suffer prolonged bed voids or accept incompatible referrals that break down."),
        ("Dual-Leadership Accountability", "Director leads commercial viability, contracting & commissioner relations; Registered Manager leads clinical assessment & safety."),
        ("Proactive Pipeline Architecture", "Direct interface with Luton Borough Council (Framework AT1115), BLMK ICB Continuing Healthcare, and 16-25 Transitions."),
        ("Strict Clinical Triage Matrix", "Red, Amber, and Green flag clinical risk stratification before booking face-to-face assessments."),
        ("Forensic Compatibility Matching", "Careful balancing of noise, sensory needs, and peer dynamics between House 78 (5 beds) and House 80 (3 beds)."),
        ("Transparent Fee Modeling", "Granular unbundling: Core Care Hours, 1:1 Enhanced Hours, Night Support, plus £350/wk Exempt Housing Benefit."),
        ("4-Stage Graduated Familiarization", "Zero-breakdown phased transition (tea visits -> meals -> day visits -> overnight trial) prior to move-in day."),
        ("Structured Post-Admission Stabilization", "Formal multi-agency gateways at 72 Hours, 28 Days, and 90 Days securing long-term placement viability.")
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
    p1.draw_text("SOP OPERATIONAL METADATA & LEADERSHIP SIGN-OFF", 70, 215, font="F2", size=9.5)
    p1.draw_line(70, 207, p1.width - 70, 207, stroke_w=0.6)

    meta_items = [
        ("Commercial Authority:", "Managing Director / Nominated Individual (ADOV Care Group LIMITED)"),
        ("Clinical Authority:", "Registered Manager (Level 5 Diploma in Leadership for Adult Care)"),
        ("Asset & Landlord Entity:", "ADOV LIMITED (Owner & Landlord under Assured Shorthold Tenancies)"),
        ("Corporate Group Parent:", "FAIRYTALES GROUP (Trading Name of Mamun Limited)"),
        ("Primary Commissioning Bodies:", "Luton Borough Council Adult Social Care & NHS BLMK ICB Brokerage"),
        ("Statutory Target Standard:", "CQC Single Assessment Framework & Transforming Care National Guidance")
    ]
    cur_my = 190
    for m_lbl, m_val in meta_items:
        p1.set_fill_color(0.76, 0.61, 0.22)
        p1.draw_text(m_lbl, 70, cur_my, font="F2", size=8.0)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_text(m_val, 210, cur_my, font="F1", size=8.0)
        cur_my -= 18

    p1.set_fill_color(0.55, 0.65, 0.75)
    p1.draw_text("CONFIDENTIAL - FOR INTERNAL EXECUTIVE MANAGEMENT & OPERATIONAL USE ONLY", p1.width / 2, 45, font="F1", size=7.5, align="center", max_w=p1.cw)

    # =========================================================================
    # PAGE 2: STRATEGIES 1 & 2 - COMMISSIONING PIPELINE & CLINICAL TRIAGE
    # =========================================================================
    p2 = doc.add_page()
    p2.draw_header_banner("SOP-INT-01", "STRATEGIES 1 & 2: PIPELINE & CLINICAL TRIAGE", "INTAKE STRATEGY PLAYBOOK")

    # Strategy 1 Box
    p2.set_fill_color(0.97, 0.98, 1.0)
    p2.set_stroke_color(0.15, 0.25, 0.45)
    p2.draw_rect(p2.mx, p2.height - 350, p2.cw, 280, fill=True, stroke=True, stroke_w=1.0)

    p2.set_fill_color(0.06, 0.12, 0.21)
    p2.draw_rect(p2.mx, p2.height - 90, p2.cw, 20, fill=True)
    p2.set_fill_color(0.76, 0.61, 0.22)
    p2.draw_text("STRATEGY 1: PROACTIVE COMMISSIONING PIPELINE & RELATIONSHIP MANAGEMENT", p2.mx + 10, p2.height - 76, font="F2", size=8.5)

    s1_text = (
        "Operational Reality: Waiting passively for local authority portal broadcasts guarantees long bed voids and low-margin placements. "
        "Management must establish active, direct relationships with key commissioning decision-makers across three dedicated streams: "
        "Luton Adult Social Care Brokerage (AT1115), NHS BLMK ICB Continuing Healthcare, and the Luton 16-25 Transitions Team."
    )
    p2.set_fill_color(0.15, 0.20, 0.30)
    p2.draw_wrapped_text(s1_text, p2.mx + 12, p2.height - 105, p2.cw - 24, font="F1", size=7.8, leading=10.5)

    p2.set_fill_color(0.06, 0.12, 0.21)
    p2.draw_text("Actionable Execution Protocol for Strategy 1:", p2.mx + 12, p2.height - 148, font="F2", size=8.2)

    s1_steps = [
        "Director Action: Maintain 100% active standing on Luton ProContract DPS (Framework AT1115). Schedule bi-monthly performance check-ins with Luton ASC Strategic Commissioning Officers and BLMK ICB Placements Lead at Arndale House.",
        "Registered Manager Action: Publish and distribute a bi-weekly 'Live Campus Vacancy & Cohort Bulletin' directly to Luton Social Work Team Managers, Hospital Discharge Coordinators at Calnwood Court, and Community Learning Disability Nurses.",
        "Specific Cohort Broadcasting: Clearly specify room attributes: e.g. 'Suite 2, House 80: Ground floor, ensuite wet room, low-arousal environment, immediate availability for adult male with autism/sensory sensitivities.'",
        "Rigorous Referral SLA: Enforce a strict internal Service Level Agreement: Acknowledge every incoming referral within 2 hours; deliver initial paper review decision within 24 hours; schedule face-to-face assessment within 48 hours."
    ]
    cur_y = p2.height - 164
    for stp in s1_steps:
        cur_y = p2.draw_wrapped_text(stp, p2.mx + 12, cur_y, p2.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    # Strategy 2 Box
    p2.set_fill_color(0.97, 0.98, 1.0)
    p2.set_stroke_color(0.76, 0.61, 0.22)
    p2.draw_rect(p2.mx, 55, p2.cw, 320, fill=True, stroke=True, stroke_w=1.0)

    p2.set_fill_color(0.06, 0.12, 0.21)
    p2.draw_rect(p2.mx, 355, p2.cw, 20, fill=True)
    p2.set_fill_color(0.76, 0.61, 0.22)
    p2.draw_text("STRATEGY 2: STATUTORY PRE-ADMISSION CLINICAL TRIAGE & RISK STRATIFICATION", p2.mx + 10, 369, font="F2", size=8.5)

    s2_text = (
        "Operational Reality: Accepting an unmanageable referral out of urgency to fill a room destroys service stability, risks staff injury, "
        "causes property damage, and triggers CQC regulatory enforcement. The Registered Manager must execute strict clinical paper triage "
        "before committing organizational resources to an on-site visit."
    )
    p2.set_fill_color(0.15, 0.20, 0.30)
    p2.draw_wrapped_text(s2_text, p2.mx + 12, 342, p2.cw - 24, font="F1", size=7.8, leading=10.5)

    p2.set_fill_color(0.06, 0.12, 0.21)
    p2.draw_text("The 3-Tier Clinical Triage Matrix:", p2.mx + 12, 298, font="F2", size=8.2)

    s2_steps = [
        "RED FLAGS (Immediate Rejection): Active unmanaged fire-setting/arson history; acute active psychotic crisis requiring hospital admission; severe unmanaged psychopathy; active IV substance addiction; predatory violence against vulnerable adults.",
        "AMBER FLAGS (Conditional Acceptance with Enhanced Funding): History of physical aggression triggered by environmental noise; self-injurious behaviour (SIB); complex epilepsy rescue medication protocols; wandering/absconding risk. Action: Require minimum 1:1 or 2:1 funded staffing hours and accredited Positive Behavioural Support (PBS) plan.",
        "GREEN FLAGS (Ideal Placement Fit): Autistic adults or individuals with mild/moderate learning disabilities seeking independent living; stable step-down from mental health rehabilitation; clients with reliable day-opportunity routines.",
        "Registered Manager Document Audit: Cross-examine: (1) Care Act 2014 Assessment; (2) Multi-disciplinary Risk Assessment; (3) PBS plan; (4) Psychiatric/Psychological reports; (5) Past 12-month incident logs; (6) MAR medication profile.",
        "Director Commercial Gate: Review the council's indicative budget. Never accept a high-acuity Amber referral at basic core care rates."
    ]
    cur_y = 284
    for stp in s2_steps:
        cur_y = p2.draw_wrapped_text(stp, p2.mx + 12, cur_y, p2.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    p2.set_fill_color(0.55, 0.65, 0.75)
    p2.draw_text("Page 2 of 6 // Resident Intake Pathway SOP // ADOV Care Group LIMITED", p2.width / 2, 28, font="F1", size=7.5, align="center", max_w=p2.cw)

    # =========================================================================
    # PAGE 3: STRATEGIES 3 & 4 - HOLISTIC ASSESSMENT & CAMPUS PEER MATCHING
    # =========================================================================
    p3 = doc.add_page()
    p3.draw_header_banner("SOP-INT-02", "STRATEGIES 3 & 4: ASSESSMENT & PEER MATCHING", "INTAKE STRATEGY PLAYBOOK")

    # Strategy 3 Box
    p3.set_fill_color(0.97, 0.98, 1.0)
    p3.set_stroke_color(0.15, 0.25, 0.45)
    p3.draw_rect(p3.mx, p3.height - 350, p3.cw, 280, fill=True, stroke=True, stroke_w=1.0)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_rect(p3.mx, p3.height - 90, p3.cw, 20, fill=True)
    p3.set_fill_color(0.76, 0.61, 0.22)
    p3.draw_text("STRATEGY 3: MULTI-DISCIPLINARY IN-PERSON ASSESSMENT & HOLISTIC PROFILING", p3.mx + 10, p3.height - 76, font="F2", size=8.5)

    s3_text = (
        "Operational Reality: Paperwork provided by local authorities is often outdated, defensive, or glosses over daily practical challenges. "
        "The Registered Manager must visit the prospective resident in person in their current setting (family home, ATU, hospital ward, "
        "or college) to observe real-world communication, sensory triggers, and daily living abilities."
    )
    p3.set_fill_color(0.15, 0.20, 0.30)
    p3.draw_wrapped_text(s3_text, p3.mx + 12, p3.height - 105, p3.cw - 24, font="F1", size=7.8, leading=10.5)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_text("The 5 Core Clinical Assessment Domains:", p3.mx + 12, p3.height - 150, font="F2", size=8.2)

    s3_steps = [
        "1. Communication & Cognition: Receptive vs expressive verbal skills, Makaton, PECS, visual timetables, processing speed, decision-making capacity under Mental Capacity Act (MCA 2005).",
        "2. Sensory Profile & PBS Triggers: Noise sensitivity, visual light tolerance, tactile aversions, crowded space anxiety; identify baseline behaviours, rumbling signs, and proven soothing strategies.",
        "3. Activities of Daily Living (ADLs) & Active Support: Eating, personal hygiene, dressing, mobility, road safety awareness, cooking potential, money handling capability.",
        "4. Health & Medication Governance: Chronic conditions, dysphagia (IDDSI level), epilepsy, medication compliance, allergies, required clinical nursing input.",
        "5. Family & Advocate Engagement: Meet family members, Court of Protection deputies, and advocates; clearly establish that Marston Gardens is Supported Living (their private home), not a residential care home."
    ]
    cur_y = p3.height - 165
    for stp in s3_steps:
        cur_y = p3.draw_wrapped_text(stp, p3.mx + 12, cur_y, p3.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    # Strategy 4 Box
    p3.set_fill_color(0.97, 0.98, 1.0)
    p3.set_stroke_color(0.76, 0.61, 0.22)
    p3.draw_rect(p3.mx, 55, p3.cw, 320, fill=True, stroke=True, stroke_w=1.0)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_rect(p3.mx, 355, p3.cw, 20, fill=True)
    p3.set_fill_color(0.76, 0.61, 0.22)
    p3.draw_text("STRATEGY 4: FORENSIC CAMPUS TOPOLOGY & PEER COMPATIBILITY MATCHING", p3.mx + 10, 369, font="F2", size=8.5)

    s4_text = (
        "Operational Reality: Successful supported living depends on micro-community harmony. Placing a highly vocal, pacing individual "
        "in the same house as a noise-sensitive tenant triggers mutual escalation. Management must leverage the distinct physical "
        "characteristics of 78 Marston Gardens (5 suites) and 80 Marston Gardens (3 suites)."
    )
    p3.set_fill_color(0.15, 0.20, 0.30)
    p3.draw_wrapped_text(s4_text, p3.mx + 12, 342, p3.cw - 24, font="F1", size=7.8, leading=10.5)

    p3.set_fill_color(0.06, 0.12, 0.21)
    p3.draw_text("The Campus Topology & Peer Matching Protocol:", p3.mx + 12, 298, font="F2", size=8.2)

    s4_steps = [
        "House 78 Profile (5 Suites): Active social environment, commercial central kitchen, shared dining area, direct patio access to large therapeutic garden. Best suited for residents who enjoy peer engagement, shared meals, and community activities.",
        "House 80 Profile (3 Suites): Low-arousal, quiet sensory sanctuary, sensory de-escalation lounge, staff administrative hub. Best suited for tenants with acute sensory sensitivities, noise intolerance, or higher 1:1 supervision needs.",
        "Physical Room Suitability: Assign ground-floor suites to tenants with physical mobility limits or high night-time movement; upper-floor suites for agile, more independent residents.",
        "Peer Compatibility Audit: The Registered Manager completes a formal 'Peer Impact Matrix': evaluate existing tenants' vulnerabilities, gender balance, vocalization tolerance, and shared bathroom/wetroom routines.",
        "Director Verification: Confirm that the room allocation preserves quiet enjoyment under landlord-tenant law and does not breach HMO/C3b planning conditions."
    ]
    cur_y = 284
    for stp in s4_steps:
        cur_y = p3.draw_wrapped_text(stp, p3.mx + 12, cur_y, p3.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    p3.set_fill_color(0.55, 0.65, 0.75)
    p3.draw_text("Page 3 of 6 // Resident Intake Pathway SOP // ADOV Care Group LIMITED", p3.width / 2, 28, font="F1", size=7.5, align="center", max_w=p3.cw)

    # =========================================================================
    # PAGE 4: STRATEGIES 5 & 6 - FEE MODELING & 4-STAGE GRADUATED TRANSITION
    # =========================================================================
    p4 = doc.add_page()
    p4.draw_header_banner("SOP-INT-03", "STRATEGIES 5 & 6: FEE MODELING & TRANSITION", "INTAKE STRATEGY PLAYBOOK")

    # Strategy 5 Box
    p4.set_fill_color(0.97, 0.98, 1.0)
    p4.set_stroke_color(0.15, 0.25, 0.45)
    p4.draw_rect(p4.mx, p4.height - 350, p4.cw, 280, fill=True, stroke=True, stroke_w=1.0)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_rect(p4.mx, p4.height - 90, p4.cw, 20, fill=True)
    p4.set_fill_color(0.76, 0.61, 0.22)
    p4.draw_text("STRATEGY 5: GRANULAR FEE MODELING & INDIVIDUAL PLACEMENT AGREEMENT (IPA)", p4.mx + 10, p4.height - 76, font="F2", size=8.5)

    s5_text = (
        "Operational Reality: Care businesses often bleed cash by agreeing to composite fees that do not cover true 1:1 staffing, "
        "waking night costs, or employer NI and pension overheads. The Director must unbundle every element transparently into a "
        "bulletproof Individual Placement Agreement (IPA) alongside a separate Housing Benefit claim."
    )
    p4.set_fill_color(0.15, 0.20, 0.30)
    p4.draw_wrapped_text(s5_text, p4.mx + 12, p4.height - 105, p4.cw - 24, font="F1", size=7.8, leading=10.5)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_text("The 4-Part Unbundled Fee Architecture:", p4.mx + 12, p4.height - 150, font="F2", size=8.2)

    s5_steps = [
        "1. Core Care Hours (£19.50 - £23.50/hr): Shared background support covering 24/7 concierge, management supervision, on-call senior, and communal activities. Typically 28 - 35 core hours per resident per week.",
        "2. Dedicated 1:1 / 2:1 Hours (£24.00 - £28.50/hr): Individualized support for community engagement, healthcare appointments, Active Support, and PBS de-escalation. Never absorb 1:1 hours into core.",
        "3. Night Care Cover: Dedicated waking night or sleep-in allowance (£85 - £115/night or hourly equivalent) explicitly itemized in the IPA to ensure waking night rotas are fully funded.",
        "4. Supported Exempt Accommodation (SEA) Housing Benefit: £350/week claimed directly by ADOV LIMITED (Landlord) from Luton Borough Council for rent, intensive housing management (IHM), communal utilities, and maintenance.",
        "Director Commercial Negotiation: Present commissioners with the itemized breakdown. Ensure contracts stipulate that if 1:1 hours are reduced, the provider has 28 days notice to adjust rotas."
    ]
    cur_y = p4.height - 165
    for stp in s5_steps:
        cur_y = p4.draw_wrapped_text(stp, p4.mx + 12, cur_y, p4.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    # Strategy 6 Box
    p4.set_fill_color(0.97, 0.98, 1.0)
    p4.set_stroke_color(0.76, 0.61, 0.22)
    p4.draw_rect(p4.mx, 55, p4.cw, 320, fill=True, stroke=True, stroke_w=1.0)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_rect(p4.mx, 355, p4.cw, 20, fill=True)
    p4.set_fill_color(0.76, 0.61, 0.22)
    p4.draw_text("STRATEGY 6: THE 4-STAGE GRADUATED TRANSITION ROADMAP (ZERO BREAKDOWN)", p4.mx + 10, 369, font="F2", size=8.5)

    s6_text = (
        "Operational Reality: Rushed, abrupt move-ins cause severe psychological trauma for autistic individuals, resulting in immediate "
        "crisis behaviors, property damage, and placement failure. The Registered Manager must execute a calm, graduated 2 to 4-week "
        "familiarization schedule tailored to the resident's pace."
    )
    p4.set_fill_color(0.15, 0.20, 0.30)
    p4.draw_wrapped_text(s6_text, p4.mx + 12, 342, p4.cw - 24, font="F1", size=7.8, leading=10.5)

    p4.set_fill_color(0.06, 0.12, 0.21)
    p4.draw_text("The 4 Chronological Transition Stages:", p4.mx + 12, 298, font="F2", size=8.2)

    s6_steps = [
        "Stage 1: Informal Tea & Garden Visit (Days 1 - 7): 1 to 2 hour visit during quiet afternoon hours. Tenant tours their private suite and sensory garden with familiar family/carer. No pressure to interact with others.",
        "Stage 2: Shared Meal & Activity Visit (Days 8 - 14): 3 to 4 hour half-day visit. Tenant prepares or shares lunch in the kitchen, spends time personalizing their room, and has low-key introductions to peers and assigned key worker.",
        "Stage 3: Extended Day & Evening Routine (Days 15 - 21): 6 to 8 hour visit extending into the evening. Tenant experiences dinner, relaxation in the sensory lounge, bath/shower routine, and meets the night waking staff.",
        "Stage 4: Overnight Trial Stay (Days 22 - 28): One overnight stay supported by a familiar carer from their current placement. Evaluate nighttime anxiety, sleep quality, and morning transition.",
        "Manager Clinical Debrief: Registered Manager holds a debrief after each stage with family, social worker, and staff. Only advance to the next stage when the tenant exhibits calm baseline behavior."
    ]
    cur_y = 284
    for stp in s6_steps:
        cur_y = p4.draw_wrapped_text(stp, p4.mx + 12, cur_y, p4.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    p4.set_fill_color(0.55, 0.65, 0.75)
    p4.draw_text("Page 4 of 6 // Resident Intake Pathway SOP // ADOV Care Group LIMITED", p4.width / 2, 28, font="F1", size=7.5, align="center", max_w=p4.cw)

    # =========================================================================
    # PAGE 5: STRATEGIES 7 & 8 - PERSONALIZATION, DAY ONE & STABILIZATION
    # =========================================================================
    p5 = doc.add_page()
    p5.draw_header_banner("SOP-INT-04", "STRATEGIES 7 & 8: DAY ONE & STABILIZATION", "INTAKE STRATEGY PLAYBOOK")

    # Strategy 7 Box
    p5.set_fill_color(0.97, 0.98, 1.0)
    p5.set_stroke_color(0.15, 0.25, 0.45)
    p5.draw_rect(p5.mx, p5.height - 350, p5.cw, 280, fill=True, stroke=True, stroke_w=1.0)

    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_rect(p5.mx, p5.height - 90, p5.cw, 20, fill=True)
    p5.set_fill_color(0.76, 0.61, 0.22)
    p5.draw_text("STRATEGY 7: SUITE PERSONALIZATION, 'DAY ONE' READINESS & STAFF BRIEFING", p5.mx + 10, p5.height - 76, font="F2", size=8.5)

    s7_text = (
        "Operational Reality: When a resident arrives to an empty, sterile room or unfamiliar staff who do not know their communication "
        "style, the risk of acute distress peaks. The private suite must feel like 'home before arrival' and all staff on shift must be "
        "forensically briefed on the resident's Positive Behavioural Support (PBS) plan."
    )
    p5.set_fill_color(0.15, 0.20, 0.30)
    p5.draw_wrapped_text(s7_text, p5.mx + 12, p5.height - 105, p5.cw - 24, font="F1", size=7.8, leading=10.5)

    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_text("Suite Personalization & 'Day One' Readiness Protocol:", p5.mx + 12, p5.height - 150, font="F2", size=8.2)

    s7_steps = [
        "1. Pre-Move-In Suite Personalization: Paint room in chosen calming pastel tone; hang personal family photos, artwork, and curtains; assemble familiar furniture; set up media/sensory lighting 48h before move-in.",
        "2. Bedroom Key Handover: Issue 2 cylinder keys directly to tenant (or advocate) to establish legal tenancy exclusive possession under Supported Living law.",
        "3. Clinical One-Page Profile: Produce a visual One-Page Profile displayed in the staff office: 'What people appreciate about me', 'What is important to me', and 'How best to support me'.",
        "4. Mandatory 45-Minute Shift Briefing: Registered Manager briefs 100% of shift support workers on the PBS plan: proactive triggers, low-arousal de-escalation, dietary needs, and eMAR medication schedule.",
        "5. Day One Welcome Protocol: Key worker meets tenant at the front door; favorite meal prepared; zero external visitors on Day 1 to avoid sensory overwhelm."
    ]
    cur_y = p5.height - 165
    for stp in s7_steps:
        cur_y = p5.draw_wrapped_text(stp, p5.mx + 12, cur_y, p5.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    # Strategy 8 Box
    p5.set_fill_color(0.97, 0.98, 1.0)
    p5.set_stroke_color(0.76, 0.61, 0.22)
    p5.draw_rect(p5.mx, 55, p5.cw, 320, fill=True, stroke=True, stroke_w=1.0)

    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_rect(p5.mx, 355, p5.cw, 20, fill=True)
    p5.set_fill_color(0.76, 0.61, 0.22)
    p5.draw_text("STRATEGY 8: THE 72-HOUR, 28-DAY & 90-DAY MULTI-AGENCY STABILIZATION CYCLE", p5.mx + 10, 369, font="F2", size=8.5)

    s8_text = (
        "Operational Reality: Admissions often experience a 'honeymoon period' in week 1, followed by behavioral testing in week 3. "
        "Structured multi-disciplinary review milestones ensure that subtle issues are caught early, care hours are adjusted if needed, "
        "and long-term placement stability is cemented."
    )
    p5.set_fill_color(0.15, 0.20, 0.30)
    p5.draw_wrapped_text(s8_text, p5.mx + 12, 342, p5.cw - 24, font="F1", size=7.8, leading=10.5)

    p5.set_fill_color(0.06, 0.12, 0.21)
    p5.draw_text("The 4 Structured Post-Admission Milestones:", p5.mx + 12, 298, font="F2", size=8.2)

    s8_steps = [
        "72-Hour Clinical Triage: Registered Manager reviews initial sleep logs, food intake, eMAR medication charts, and early behavioral signs. Adjust daily rota and support approach immediately if distress is detected.",
        "14-Day Internal MDT Review: Internal review between Registered Manager, Key Worker, and Nominated Individual. Audit peer dynamics, community outings, and staff rapport. Refine PBS strategies.",
        "28-Day Statutory Placement Review: Formal multi-agency meeting with Luton Social Worker, BLMK ICB Commissioner, Family, and Advocate. Present a written 28-day outcome report. Formally confirm or adjust commissioned hours.",
        "90-Day Stabilization Sign-Off: Placement transitions from 'provisional intake' to 'stabilized tenancy'. Formulate 12-month independence milestones (e.g. voluntary work, college courses, independent cooking).",
        "Director Financial Audit: Verify prompt payment of council invoices; audit hours delivered against hours invoiced; ensure Housing Benefit payments are running seamlessly."
    ]
    cur_y = 284
    for stp in s8_steps:
        cur_y = p5.draw_wrapped_text(stp, p5.mx + 12, cur_y, p5.cw - 24, font="F1", size=7.2, leading=9.5)
        cur_y -= 4

    p5.set_fill_color(0.55, 0.65, 0.75)
    p5.draw_text("Page 5 of 6 // Resident Intake Pathway SOP // ADOV Care Group LIMITED", p5.width / 2, 28, font="F1", size=7.5, align="center", max_w=p5.cw)

    # =========================================================================
    # PAGE 6: MASTER ACTION MATRIX - DIRECTOR VS REGISTERED MANAGER
    # =========================================================================
    p6 = doc.add_page()
    p6.draw_header_banner("SOP-INT-05", "MASTER ACTION MATRIX: DIRECTOR VS REGISTERED MANAGER", "INTAKE STRATEGY PLAYBOOK")

    p6.set_fill_color(0.06, 0.12, 0.21)
    p6.draw_text("OPERATIONAL DIVISION OF RESPONSIBILITIES ACROSS THE 8 INTAKE GATEWAYS", p6.mx, p6.height - 70, font="F2", size=9.5)
    p6.set_fill_color(0.35, 0.40, 0.50)
    p6.draw_text("Clear, unambiguous division of executive actions between Managing Director and Registered Manager.", p6.mx, p6.height - 82, font="F1", size=8.0)

    # Table Header
    ty = p6.height - 105
    p6.set_fill_color(0.06, 0.12, 0.21)
    p6.draw_rect(p6.mx, ty, p6.cw, 20, fill=True)
    p6.set_fill_color(1.0, 1.0, 1.0)
    p6.draw_text("GATEWAY", p6.mx + 6, ty + 6, font="F2", size=8.0)
    p6.draw_text("DIRECTOR ACTIONS (COMMERCIAL & LEGAL)", p6.mx + 80, ty + 6, font="F2", size=8.0)
    p6.draw_text("REGISTERED MANAGER ACTIONS (CLINICAL & CARE)", p6.mx + 300, ty + 6, font="F2", size=8.0)

    matrix_rows = [
        ("1. Pipeline", "Luton DPS profile, contract framework, commissioner meetings.", "Bi-weekly vacancy bulletin, social worker & hospital outreach."),
        ("2. Triage", "Financial feasibility check against council indicative budget.", "Forensic paper audit (Care Act, PBS, risk logs, red/amber flags)."),
        ("3. Assessment", "Approve travel & mobile assessment toolkit resources.", "Face-to-face assessment in current setting, family & advocate meeting."),
        ("4. Matching", "Confirm lease covenants & HMO/planning class alignment.", "Peer compatibility impact assessment, house & suite allocation (78/80)."),
        ("5. Contracting", "Negotiate IPA with Luton/ICB, agree £350/wk Housing Benefit.", "Validate commissioned hours (core + 1:1) cover rota requirements."),
        ("6. Transition", "Authorize transition logistics & catering budget.", "Formulate 4-stage graduated transition plan (tea -> meals -> overnight)."),
        ("7. Day One", "Verify staff employment compliance (DBS, RTW, contracts).", "Suite personalization, PBS one-page profile, mandatory team briefing."),
        ("8. Review", "Audit invoice payments, monitor gross margins & billing accuracy.", "72h clinical check, 28d social worker review, 90d independence goals.")
    ]

    row_y = ty - 42
    for idx, (gw, d_act, rm_act) in enumerate(matrix_rows):
        bg = (0.97, 0.98, 1.0) if idx % 2 == 0 else (1.0, 1.0, 1.0)
        p6.set_fill_color(bg[0], bg[1], bg[2])
        p6.draw_rect(p6.mx, row_y, p6.cw, 40, fill=True)
        p6.set_stroke_color(0.85, 0.88, 0.92)
        p6.draw_line(p6.mx, row_y, p6.mx + p6.cw, row_y, stroke_w=0.4)

        p6.set_fill_color(0.06, 0.12, 0.21)
        p6.draw_text(gw, p6.mx + 6, row_y + 24, font="F2", size=7.8)
        p6.set_fill_color(0.15, 0.25, 0.45)
        p6.draw_wrapped_text(d_act, p6.mx + 80, row_y + 28, 205, font="F1", size=7.2, leading=9.2)
        p6.set_fill_color(0.76, 0.61, 0.22)
        p6.draw_wrapped_text(rm_act, p6.mx + 300, row_y + 28, 205, font="F1", size=7.2, leading=9.2)

        row_y -= 42

    # Bottom Signature Box
    p6.set_fill_color(0.06, 0.12, 0.21)
    p6.draw_rect(p6.mx, 55, p6.cw, 65, fill=True)
    p6.set_fill_color(0.76, 0.61, 0.22)
    p6.draw_text("EXECUTIVE ADOPTION & OPERATIONAL SIGN-OFF", p6.mx + 12, 105, font="F2", size=9.0)
    p6.set_fill_color(1.0, 1.0, 1.0)
    p6.draw_text("This Standard Operating Procedure is formally adopted by ADOV Care Group LIMITED.", p6.mx + 12, 92, font="F1", size=8.0)
    p6.draw_text("Director: ___________________________ (Sign & Date)      Registered Manager: ___________________________ (Sign & Date)", p6.mx + 12, 75, font="F2", size=8.0)

    p6.set_fill_color(0.55, 0.65, 0.75)
    p6.draw_text("Page 6 of 6 // Resident Intake Pathway SOP // ADOV Care Group LIMITED", p6.width / 2, 28, font="F1", size=7.5, align="center", max_w=p6.cw)

    doc.save()
    print(f"Generated PDF '{pdf_filename}'.")

def build_docx():
    docx_filename = "ADOV_Care_Group_Resident_Intake_Pathway_SOP.docx"
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
    add_p("RESIDENT INTAKE PATHWAY & COMMISSIONING OPERATING MANUAL", style="Subtitle", bold=True, size=26, color="C29B38", space_after=140)
    add_p("Standard Operating Procedure (SOP) for Managing Directors & Registered Managers // Target Assets: 78 & 80 Marston Gardens, Luton", style="Normal", italic=True, size=20, color="64748B", space_after=200)

    add_p("1. EXECUTIVE MANDATE & DUAL-LEADERSHIP ACCOUNTABILITY", style="Heading1", bold=True, size=28, color="0F1E36", space_after=100)
    add_p("Care businesses fail when they either suffer prolonged bed voids due to passive marketing, or accept unmanageable, incompatible residents out of financial pressure. This SOP establishes a zero-void, zero-breakdown intake pathway across 78 & 80 Marston Gardens, Luton (LU2 7DY).", space_after=100)
    add_p("Clear division of responsibilities is mandatory: The Managing Director owns commercial viability, commissioner contracts, fee negotiation, and legal leases. The Registered Manager owns clinical triage, compatibility matching, PBS formulation, transition execution, and CQC compliance.", space_after=140)

    add_p("2. THE 8 CORE STRATEGIES OF THE RESIDENT INTAKE PATHWAY", style="Heading1", bold=True, size=28, color="0F1E36", space_after=100)

    strategies = [
        ("Strategy 1: Proactive Multi-Channel Commissioning Pipeline",
         "Maintain active registration on Luton Borough Council ProContract (AT1115), BLMK ICB Continuing Healthcare, and Luton 16-25 Transitions. Publish bi-weekly live vacancy bulletins to social work managers. Enforce a 2-hour referral acknowledgment SLA."),
        
        ("Strategy 2: Statutory Pre-Admission Clinical Triage & Risk Stratification",
         "Apply the 3-Tier Clinical Matrix before booking assessments: Red Flags (immediate rejection for active arson, acute psychosis, predatory violence); Amber Flags (conditional acceptance with confirmed 1:1/2:1 hours and PBS); Green Flags (ideal autism/LD independent living fit)."),
        
        ("Strategy 3: Multi-Disciplinary In-Person Assessment & Holistic Profiling",
         "Conduct face-to-face assessment in the resident's current setting (family home, ATU, hospital ward, or college). Evaluate communication (Makaton/PECS), sensory profile, PBS triggers, ADLs, and family aspirations. Avoid relying on outdated council paperwork."),
        
        ("Strategy 4: Forensic Campus Topology & Peer Compatibility Matching",
         "Match the resident to the optimal house and suite: House 78 (5 suites) for active social engagement and commercial kitchen access; House 80 (3 suites) for low-arousal, quiet sensory living. Ground floor suites for mobility/night movement. Complete formal Peer Impact Matrix."),
        
        ("Strategy 5: Granular Fee Modeling & Individual Placement Agreement (IPA)",
         "Unbundle fees transparently: Core Care Hours (£19.50-£23.50/hr), Dedicated 1:1 Hours (£24.00-£28.50/hr), Sleep-In/Waking Night Allowance, plus £350/wk Exempt Housing Benefit claimed by Landlord (PropCo). Never accept a loss-making composite rate."),
        
        ("Strategy 6: The 4-Stage Graduated Transition Roadmap",
         "Execute a calm 2 to 4-week familiarization plan to prevent placement breakdown: Stage 1 (tea and garden visit); Stage 2 (shared meal and key worker introduction); Stage 3 (extended day and evening routine); Stage 4 (overnight familiarization trial stay)."),
        
        ("Strategy 7: Suite Personalization, 'Day One' Readiness & Staff Briefing",
         "Pre-decorate the private suite in calming tones with familiar bedding and personal photos before arrival. Issue bedroom cylinder keys directly to tenant. Hold mandatory 45-minute shift team briefing on the PBS plan and One-Page Profile before the tenant arrives."),
        
        ("Strategy 8: The 72-Hour, 28-Day & 90-Day Multi-Agency Stabilization Cycle",
         "Enforce structured review gateways: 72-hour clinical triage (sleep/medication); 14-day internal MDT review; 28-day formal placement review with Luton Social Worker and family; 90-day stabilization sign-off transitioning to long-term independence goals.")
    ]

    for s_title, s_desc in strategies:
        add_p(s_title, style="Heading2", bold=True, size=22, color="C29B38", space_after=60)
        add_p(s_desc, space_after=120)

    add_p("3. MASTER ACTION MATRIX: DIRECTOR VS REGISTERED MANAGER", style="Heading1", bold=True, size=28, color="0F1E36", space_after=100)
    matrix = [
        "Pipeline (Gateway 1): Director manages DPS portal and commissioner relations; RM publishes vacancy bulletins and networks with social workers.",
        "Triage (Gateway 2): Director checks indicative budget against staff cost; RM conducts forensic paper review and filters Red/Amber flags.",
        "Assessment (Gateway 3): Director approves assessment logistics; RM travels to current placement to conduct comprehensive face-to-face clinical audit.",
        "Matching (Gateway 4): Director verifies lease covenants and planning class; RM completes Peer Compatibility Impact Matrix and assigns House 78 vs 80.",
        "Contracting (Gateway 5): Director negotiates and signs IPA and Housing Benefit claim; RM validates commissioned hours mathematically cover rota.",
        "Transition (Gateway 6): Director approves transition logistics budget; RM coordinates 4-stage graduated visits and debriefs family.",
        "Day One (Gateway 7): Director ensures all staff compliance (DBS, training, right to work); RM leads suite personalization and mandatory team PBS briefing.",
        "Review (Gateway 8): Director audits council invoice payments and gross margin; RM presents 28-day outcome report and sets 90-day independence milestones."
    ]
    for m_item in matrix:
        add_bullet(m_item)

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
