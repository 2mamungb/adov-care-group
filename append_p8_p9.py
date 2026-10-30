with open("generate_government_project_report.py", "a") as f:
    f.write('''
    # =========================================================================
    # PAGE 8: CHAPTER 7 - STATUTORY LICENSING & CQC REGISTRATION
    # =========================================================================
    p8 = doc.add_page()
    
    p8.set_fill_color(0.06, 0.10, 0.18)
    p8.draw_text("7. STATUTORY LICENSING: CQC REGISTRATION & GOVERNANCE", 36, 794, font="F2", size=13.0)
    p8.set_stroke_color(0.85, 0.60, 0.15)
    p8.draw_line(36, 786, p8.width - 36, 786, stroke_w=1.2)
    
    # CQC Regulatory Scope Box
    p8.set_fill_color(0.97, 0.98, 1.0)
    p8.set_stroke_color(0.20, 0.35, 0.60)
    p8.draw_rect(36, 640, p8.cw, 135, fill=True, stroke=True, stroke_w=1.0)
    
    p8.set_fill_color(0.10, 0.20, 0.40)
    p8.draw_rect(36, 745, p8.cw, 25, fill=True)
    p8.set_fill_color(1.0, 1.0, 1.0)
    p8.draw_text("7.1 REGULATED ACTIVITY: PERSONAL CARE IN SUPPORTED LIVING", 46, 753, font="F2", size=9.0)
    
    p8_cqc_text = (
        "Under the Health and Social Care Act 2008 (Regulated Activities) Regulations 2014, ADOV Care Group LIMITED applies to the Care Quality "
        "Commission (CQC) for registration as a Service Provider for the regulated activity of 'Personal Care'. "
        "In accordance with CQC's statutory guidance 'Housing with Care' and the 'Right Support, Right Care, Right Culture' policy, the service "
        "operates as a Supported Living scheme. Service users reside under individual Assured Shorthold Tenancy agreements (or licenses), giving them "
        "exclusive possession of their personal bedrooms and shared use of communal areas. Personal care and PBS support are delivered under a "
        "completely separate Care and Support Agreement, establishing clear statutory separation between housing and care."
    )
    p8.set_fill_color(0.15, 0.20, 0.25)
    p8.draw_wrapped_text(p8_cqc_text, 46, 735, p8.cw - 20, font="F1", size=7.8, leading=10.2)
    
    # Statutory Leadership Roles Box
    p8.set_fill_color(0.98, 0.98, 0.99)
    p8.set_stroke_color(0.25, 0.35, 0.55)
    p8.draw_rect(36, 395, p8.cw, 235, fill=True, stroke=True, stroke_w=1.0)
    
    p8.set_fill_color(0.12, 0.22, 0.40)
    p8.draw_rect(36, 600, p8.cw, 25, fill=True)
    p8.set_fill_color(1.0, 1.0, 1.0)
    p8.draw_text("7.2 STATUTORY APPOINTMENTS & FIT AND PROPER PERSON COMPLIANCE", 46, 608, font="F2", size=9.0)
    
    gov_roles = [
        ("Registered Manager (Regulation 7 Mandate):",
         "The Health and Social Care Act mandates that a CQC-registered provider must have a Registered Manager in day-to-day operational charge. "
         "Statutory requirements: 1) Must hold the Level 5 Diploma in Leadership and Management for Adult Care (or equivalent RMA/NVQ Level 4). "
         "2) Minimum 3 years supervisory experience in autism, learning disabilities, and PBS. 3) Enhanced DBS on update service. 4) Passing the "
         "rigorous CQC Fit and Proper Person registration interview assessing clinical regulations, safeguarding, and leadership."),
         
        ("Nominated Individual (Regulation 6 Mandate):",
         "An executive Director of ADOV Care Group LIMITED is appointed as the Nominated Individual (NI). Under Regulation 6, the NI is legally "
         "responsible for supervising the management of regulated activities and acts as the official liaison with CQC inspectors."),
         
        ("Fit and Proper Persons Requirement for Directors (Regulation 5):",
         "All corporate directors of Mamun LIMITED, ADOV LIMITED, and ADOV Care Group LIMITED must satisfy Regulation 5 (good character, financial "
         "solvency, absence of bankruptcy or serious criminal offenses, and mental/physical competence to oversee care delivery).")
    ]
    cur_gy = 590
    for g_t, g_d in gov_roles:
        p8.set_fill_color(0.12, 0.25, 0.50)
        p8.draw_text(g_t, 46, cur_gy, font="F2", size=7.5)
        cur_gy -= 10
        p8.set_fill_color(0.18, 0.22, 0.28)
        cur_gy = p8.draw_wrapped_text(g_d, 46, cur_gy, p8.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_gy -= 6
        
    # CQC Assessment & Quality Framework Box
    p8.set_fill_color(0.97, 0.99, 0.97)
    p8.set_stroke_color(0.15, 0.55, 0.25)
    p8.draw_rect(36, 48, p8.cw, 335, fill=True, stroke=True, stroke_w=1.0)
    
    p8.set_fill_color(0.12, 0.45, 0.20)
    p8.draw_rect(36, 353, p8.cw, 25, fill=True)
    p8.set_fill_color(1.0, 1.0, 1.0)
    p8.draw_text("7.3 CQC SINGLE ASSESSMENT FRAMEWORK & STATUTORY POLICIES", 46, 361, font="F2", size=9.0)
    
    cqc_pts = [
        ("The Single Assessment Framework (34 Quality Statements):",
         "CQC evaluates providers across 5 Key Questions: Safe, Effective, Caring, Responsive, Well-Led. Compliance is verified through continuous "
         "evidence collection, service user feedback, local authority contract monitoring reports, and unannounced site inspections."),
         
        ("Oliver McGowan Mandatory Training for Autism and Learning Disabilities:",
         "In compliance with Section 181 of the Health and Care Act 2022, all 14 frontline support staff and managers complete the Oliver McGowan "
         "Mandatory Training (Tier 1 eLearning + Tier 2 co-delivered interactive training with autistic individuals) prior to service user intake."),
         
        ("Bespoke Operational Policy Suite (42 Policies):",
         "Full statutory policy framework prepared: Safeguarding Adults at Risk (Level 3), Mental Capacity Act 2005 & Deprivation of Liberty "
         "Safeguards (DoLS/LPS), Safe Administration of Medication (NICE SC1 guidelines), Positive Behavioural Support (PBS), Whistleblowing, "
         "Infection Prevention & Control (HTM 01-04), Business Continuity & Emergency Evacuation (BS 5839-1).")
    ]
    cur_qy = 343
    for q_t, q_d in cqc_pts:
        p8.set_fill_color(0.12, 0.45, 0.20)
        p8.draw_text(q_t, 46, cur_qy, font="F2", size=7.5)
        cur_qy -= 10
        p8.set_fill_color(0.18, 0.22, 0.28)
        cur_qy = p8.draw_wrapped_text(q_d, 46, cur_qy, p8.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_qy -= 6

    print("Added Page 8.")


    # =========================================================================
    # PAGE 9: CHAPTER 8 - COMMISSIONING & ZERO-VOID STRATEGY
    # =========================================================================
    p9 = doc.add_page()
    
    p9.set_fill_color(0.06, 0.10, 0.18)
    p9.draw_text("8. COMMISSIONING PIPELINE & ZERO-VOID PLACEMENT STRATEGY", 36, 794, font="F2", size=13.0)
    p9.set_stroke_color(0.85, 0.60, 0.15)
    p9.draw_line(36, 786, p9.width - 36, 786, stroke_w=1.2)
    
    # Commissioning Architecture Box
    p9.set_fill_color(0.97, 0.98, 1.0)
    p9.set_stroke_color(0.20, 0.35, 0.60)
    p9.draw_rect(36, 640, p9.cw, 135, fill=True, stroke=True, stroke_w=1.0)
    
    p9.set_fill_color(0.10, 0.20, 0.40)
    p9.draw_rect(36, 745, p9.cw, 25, fill=True)
    p9.set_fill_color(1.0, 1.0, 1.0)
    p9.draw_text("8.1 LOCAL AUTHORITY & NHS COMMISSIONING FRAMEWORKS", 46, 753, font="F2", size=9.0)
    
    p9_comm_text = (
        "ADOV Care Group enters the Luton Adult Social Care commissioning ecosystem via three formal procurement mechanisms: "
        "1) Luton Borough Council ProContract Portal: Onboarding onto the Dynamic Purchasing System (DPS) under Framework AT1115 (Adult Supported "
        "Living Services). 2) NHS BLMK Integrated Care Board (ICB): Direct accreditation for NHS Continuing Healthcare (CHC) and Section 117 "
        "Mental Health Act joint-funded placements. 3) Transforming Care Partnership: Luton Social Services actively seeks local specialist providers "
        "to repatriate vulnerable adults currently placed in distant counties at exorbitant costs (£3,500-£4,500/week). ADOV Care Group's 8-bed "
        "campus provides the council with high-quality, local, cost-effective placement capacity."
    )
    p9.set_fill_color(0.15, 0.20, 0.25)
    p9.draw_wrapped_text(p9_comm_text, 46, 735, p9.cw - 20, font="F1", size=7.8, leading=10.2)
    
    # 6-Stage Zero-Void Placement Protocol Box
    p9.set_fill_color(0.98, 0.98, 0.99)
    p9.set_stroke_color(0.25, 0.35, 0.55)
    p9.draw_rect(36, 385, p9.cw, 245, fill=True, stroke=True, stroke_w=1.0)
    
    p9.set_fill_color(0.12, 0.22, 0.40)
    p9.draw_rect(36, 600, p9.cw, 25, fill=True)
    p9.set_fill_color(1.0, 1.0, 1.0)
    p9.draw_text("8.2 THE 6-STAGE ZERO-VOID REFERRAL & TRANSITION PROTOCOL", 46, 608, font="F2", size=9.0)
    
    stages = [
        ("Stage 1: Referral & Initial Desk Review (48-Hour Response):",
         "Referral received via Luton Brokerage or BLMK CHC portal. Registered Manager conducts instant clinical assessment against compatibility matrices."),
        ("Stage 2: Multidisciplinary Pre-Admission Assessment:",
         "Face-to-face assessment conducted with service user, social worker, community learning disability nurse, and family. Formulation of baseline PBS plan."),
        ("Stage 3: Peer Compatibility & Sensory Impact Audit:",
         "Assessing compatibility with existing residents in 78 or 80. Ensuring quiet, harmonious sensory matching to prevent emotional dysregulation."),
        ("Stage 4: Commissioning Approval & Individual Placement Agreement (IPA):",
         "Luton Council / BLMK ICB issues formal IPA approving core shared hours + 1:1 assessed PBS hours (£2,150/week)."),
        ("Stage 5: Graduated 4-Week Domestic Transition:",
         "Carefully phased transition: 1) Initial daytime visit for tea. 2) Dinner visit. 3) Full day stay. 4) Weekend overnight stay with dedicated 1:1 carer."),
        ("Stage 6: Formal Tenancy Execution & Admission (Zero-Void Commenced):",
         "Signing Assured Shorthold Tenancy (AST) and Supported Exempt Accommodation Housing Benefit claim (£350/week). Service user enters permanent domestic tenure.")
    ]
    cur_sty = 590
    for s_title, s_desc in stages:
        p9.set_fill_color(0.12, 0.25, 0.50)
        p9.draw_text(s_title, 46, cur_sty, font="F2", size=7.2)
        cur_sty -= 9
        p9.set_fill_color(0.18, 0.22, 0.28)
        cur_sty = p9.draw_wrapped_text(s_desc, 46, cur_sty, p9.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_sty -= 4
        
    # Stakeholder Engagement Map Box
    p9.set_fill_color(0.97, 0.99, 0.97)
    p9.set_stroke_color(0.15, 0.55, 0.25)
    p9.draw_rect(36, 48, p9.cw, 325, fill=True, stroke=True, stroke_w=1.0)
    
    p9.set_fill_color(0.12, 0.45, 0.20)
    p9.draw_rect(36, 345, p9.cw, 25, fill=True)
    p9.set_fill_color(1.0, 1.0, 1.0)
    p9.draw_text("8.3 KEY REFERRAL STAKEHOLDERS IN LUTON GUARANTEEING OCCUPANCY", 46, 353, font="F2", size=9.0)
    
    stakeholders = [
        ("Luton Council Adult Learning Disability Team (ALDT) - Charter House, Alma St, Luton:",
         "Primary commissioning team managing all adult placements in Luton. Priority relationship established 3 months before CQC certificate issuance."),
        ("Luton Children & Young People's Transitions Team (16-25 Team):",
         "Manages adolescents transitioning from residential schools into adult supported living. Crucial pipeline providing young adults with 10-20 year tenure."),
        ("Bedfordshire & Luton Mental Health and Wellbeing Services (ELFT / Calnwood Court):",
         "NHS Trust discharge coordinators seeking high-support community step-down placements for stable individuals ready for supported living."),
        ("Financial Guarantee (Retainers & Length of Stay):",
         "Once admitted, average stay for autism/LD service users is 7 to 15+ years. Luton Council contracts provide a 28-day notice period and paid vacancy "
         "retainer fees during temporary hospital stays, permanently shielding ADOV Care Group from void cashflow losses.")
    ]
    cur_sky = 335
    for k_t, k_d in stakeholders:
        p9.set_fill_color(0.12, 0.45, 0.20)
        p9.draw_text(k_t, 46, cur_sky, font="F2", size=7.5)
        cur_sky -= 10
        p9.set_fill_color(0.18, 0.22, 0.28)
        cur_sky = p9.draw_wrapped_text(k_d, 46, cur_sky, p9.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_sky -= 6

    print("Added Page 9.")
''')

print("append_p8_p9 written.")
