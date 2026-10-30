with open("generate_luxury_brochure.py", "a") as f:
    f.write('''
    # =========================================================================
    # PAGE 8: CHAPTER 6 - FINANCIAL ENGINEERING & 3-YEAR P&L MODEL
    # =========================================================================
    p8 = doc.add_page()
    p8.draw_header_banner("6", "FINANCIAL ENGINEERING: CAPEX & 3-YEAR P&L", "INVESTMENT YIELD")
    
    # CapEx Table (Left Box)
    p8.set_fill_color(0.97, 0.98, 1.0)
    p8.set_stroke_color(0.20, 0.35, 0.60)
    p8.draw_rect(36, 440, 255, 335, fill=True, stroke=True, stroke_w=1.0)
    
    p8.set_fill_color(0.10, 0.20, 0.40)
    p8.draw_rect(36, 750, 255, 25, fill=True)
    p8.set_fill_color(1.0, 1.0, 1.0)
    p8.draw_text("ITEMIZED TURNKEY CAPEX BUDGET (£150k)", 44, 758, font="F2", size=8.0)
    
    capex_items = [
        ("Architectural, Plans & S.192 CLPUD", "£6,500"),
        ("BS 5839-1 Cat L1 Fire Alarm & Panel", "£14,000"),
        ("FD30S Fire Doorsets (14 sets fitted)", "£12,500"),
        ("Sanitary Adaptations (1 En-Suite + TMV3)", "£18,000"),
        ("Acoustic Soundproofing (Doc E Partitions)", "£15,000"),
        ("HTM 01-04 Commercial Laundry & Kitchen", "£16,500"),
        ("Anti-Ligature / Tamper-Proof Finishes", "£14,000"),
        ("Sensory Suite & Multi-Sensory Garden", "£8,000"),
        ("Access Control, Panic Alarms & Intercom", "£11,000"),
        ("CQC Registration, Legal & Policy Suite", "£14,500"),
        ("Contingency & Working Capital Reserve", "£20,000"),
        ("TOTAL TURNKEY CAPITAL EXPENDITURE", "£150,000")
    ]
    cur_cpx_y = 732
    for c_item, c_cost in capex_items:
        bold = "TOTAL" in c_item
        p8.set_fill_color(0.85, 0.65, 0.18) if bold else p8.set_fill_color(0.15, 0.20, 0.28)
        p8.draw_text(c_item, 44, cur_cpx_y, font="F2" if bold else "F1", size=6.8)
        p8.draw_text(c_cost, 240, cur_cpx_y, font="F2" if bold else "F1", size=6.8, align="right", max_w=45)
        cur_cpx_y -= 13.5
        
    p8.set_fill_color(0.40, 0.45, 0.55)
    cpx_note = (
        "*Note: Existing wetrooms in 78 & 80 save £42,000 vs standard retrofit. All works comply with Building Regs Approved Documents B, M, E, F."
    )
    p8.draw_wrapped_text(cpx_note, 44, 580, 240, font="F3", size=6.2, leading=8.5)
    
    # 3-Year P&L Model (Right Box)
    p8.set_fill_color(0.98, 0.98, 0.99)
    p8.set_stroke_color(0.25, 0.35, 0.55)
    p8.draw_rect(298, 440, 261, 335, fill=True, stroke=True, stroke_w=1.0)
    
    p8.set_fill_color(0.12, 0.22, 0.40)
    p8.draw_rect(298, 750, 261, 25, fill=True)
    p8.set_fill_color(1.0, 1.0, 1.0)
    p8.draw_text("3-YEAR STABILIZED P&L MODEL (£)", 306, 758, font="F2", size=8.0)
    
    pnl_headers = ["P&L Line Item", "Year 1 (60%)", "Year 2 (88%)", "Year 3 (95%)"]
    pw = [95, 52, 55, 55]
    
    p8.set_fill_color(0.15, 0.25, 0.45)
    p8.draw_rect(298, 730, 261, 14, fill=True)
    p8.set_fill_color(1.0, 1.0, 1.0)
    px = 298
    for i, ph in enumerate(pnl_headers):
        p8.draw_text(ph, px + 3, 734, font="F2", size=6.2)
        px += pw[i]
        
    pnl_rows = [
        ("Gross Care & SEA Revenue", "£625,997", "£1,043,328", "£1,126,394"),
        ("Frontline PBS Staff (14 FT)", "(£320,000)", "(£425,000)", "(£440,000)"),
        ("Registered Manager / Lead", "(£55,000)", "(£60,000)", "(£65,000)"),
        ("Internal Property Leases", "(£115,000)", "(£115,000)", "(£115,000)"),
        ("Food, Heat, Light, Insurance", "(£25,000)", "(£35,000)", "(£38,000)"),
        ("NET OPERATING EBITDA", "£110,997", "£408,328", "£468,394"),
        ("EBITDA Margin (%)", "17.7%", "39.1%", "41.6%"),
        ("Internal Rental Income", "£115,000", "£115,000", "£115,000"),
        ("TOTAL GROUP CASHFLOW", "£225,997", "£523,328", "£583,394"),
        ("ROCE on £150k CapEx", "150.6%", "261.6%", "291.5%")
    ]
    cur_pnl_y = 716
    for p_lbl, py1, py2, py3 in pnl_rows:
        bold = "EBITDA" in p_lbl or "TOTAL" in p_lbl or "ROCE" in p_lbl or "Gross" in p_lbl
        p8.set_fill_color(0.85, 0.65, 0.18) if bold else p8.set_fill_color(0.18, 0.22, 0.28)
        p8.draw_text(p_lbl, 301, cur_pnl_y, font="F2" if bold else "F1", size=6.2)
        p8.draw_text(py1, 396, cur_pnl_y, font="F2" if bold else "F1", size=6.2)
        p8.draw_text(py2, 448, cur_pnl_y, font="F2" if bold else "F1", size=6.2)
        p8.draw_text(py3, 503, cur_pnl_y, font="F2" if bold else "F1", size=6.2)
        cur_pnl_y -= 14.0

    # Executive Commentary Box
    p8.set_fill_color(0.97, 0.99, 0.97)
    p8.set_stroke_color(0.15, 0.55, 0.25)
    p8.draw_rect(36, 42, p8.cw, 385, fill=True, stroke=True, stroke_w=1.0)
    
    p8.set_fill_color(0.12, 0.45, 0.20)
    p8.draw_rect(36, 403, p8.cw, 24, fill=True)
    p8.set_fill_color(1.0, 1.0, 1.0)
    p8.draw_text("6.2 COMMERCIAL VIABILITY & RETURN ON CAPITAL EMPLOYED (ROCE) AUDIT", 46, 410, font="F2", size=8.5)
    
    fin_commentary = [
        ("Exceptional Capital Efficiency (£150,000 Turnkey Investment):",
         "Because 78 and 80 Marston Gardens already possess existing large wetrooms and separate WCs, the total CapEx required across both properties "
         "is limited to £150,000 (£18,750 per bed). This covers full BS 5839-1 Cat L1 fire systems, FD30S doors, Document E soundproofing, anti-ligature "
         "fittings, CQC registration, and a £20,000 cash reserve."),
         
        ("Outstanding Operating EBITDA Margin (39.1% at Stabilized Capacity):",
         "At stabilized occupancy (Year 2 with 7 active beds / 88%), gross revenue from Luton Council care hours and Supported Exempt Accommodation "
         "Housing Benefit reaches £1,043,328. Total operating expenditures (including 14 full-time PBS care staff at competitive Luton wages, "
         "Registered Manager, Team Leader, utilities, and insurance) total £635,000. OpCo delivers £408,328 in net operating profit (EBITDA)."),
         
        ("Total Annual Net Group Cashflow (£523,328 / year):",
         "FAIRYTALES GROUP captures revenue across two streams: 1) OpCo net operating profit: £408,328/year. 2) Property leases paid by OpCo: £115,000/year "
         "(£65,000 to ADOV LIMITED for 78, and £50,000 to the Director for 80). Total combined group cashflow equals £523,328 per annum."),
         
        ("Unprecedented 261.6% ROCE & 3.5-Month Payback Period:",
         "Dividing annual EBITDA (£408,328) by initial CapEx (£150,000) yields a Return on Capital Employed (ROCE) of 261.6% per annum. "
         "The entire capital expenditure is fully repaid from operating cashflow within 3.5 months of reaching stabilized occupancy.")
    ]
    cur_cy_fin = 390
    for f_t, f_d in fin_commentary:
        p8.set_fill_color(0.12, 0.45, 0.20)
        p8.draw_text(f_t, 46, cur_cy_fin, font="F2", size=7.5)
        cur_cy_fin -= 10
        p8.set_fill_color(0.18, 0.22, 0.28)
        cur_cy_fin = p8.draw_wrapped_text(f_d, 46, cur_cy_fin, p8.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_cy_fin -= 6


    # =========================================================================
    # PAGE 9: CHAPTER 7 - STATUTORY CARE LICENSING & CQC REGISTRATION
    # =========================================================================
    p9 = doc.add_page()
    p9.draw_header_banner("7", "STATUTORY CARE LICENSING & GOVERNANCE", "CQC REGISTRATION")
    
    # CQC Regulatory Scope Box
    p9.set_fill_color(0.97, 0.98, 1.0)
    p9.set_stroke_color(0.20, 0.35, 0.60)
    p9.draw_rect(36, 640, p9.cw, 130, fill=True, stroke=True, stroke_w=1.0)
    
    p9.set_fill_color(0.10, 0.20, 0.40)
    p9.draw_rect(36, 745, p9.cw, 25, fill=True)
    p9.set_fill_color(1.0, 1.0, 1.0)
    p9.draw_text("7.1 REGULATED ACTIVITY: PERSONAL CARE IN SUPPORTED LIVING", 46, 753, font="F2", size=9.0)
    
    p9_cqc_text = (
        "Under the Health and Social Care Act 2008 (Regulated Activities) Regulations 2014, ADOV Care Group LIMITED applies to the Care Quality "
        "Commission (CQC) for registration as a Service Provider for the regulated activity of 'Personal Care'. "
        "In accordance with CQC's statutory guidance 'Housing with Care' and the 'Right Support, Right Care, Right Culture' policy, the service "
        "operates as a Supported Living scheme. Service users reside under individual Assured Shorthold Tenancy agreements (or licenses), giving them "
        "exclusive possession of their personal bedrooms and shared use of communal areas. Personal care and PBS support are delivered under a "
        "completely separate Care and Support Agreement, establishing clear statutory separation between housing and care."
    )
    p9.set_fill_color(0.15, 0.20, 0.25)
    p9.draw_wrapped_text(p9_cqc_text, 46, 735, p9.cw - 20, font="F1", size=7.8, leading=10.0)
    
    # Statutory Leadership Roles Box
    p9.set_fill_color(0.98, 0.98, 0.99)
    p9.set_stroke_color(0.25, 0.35, 0.55)
    p9.draw_rect(36, 395, p9.cw, 235, fill=True, stroke=True, stroke_w=1.0)
    
    p9.set_fill_color(0.12, 0.22, 0.40)
    p9.draw_rect(36, 600, p9.cw, 25, fill=True)
    p9.set_fill_color(1.0, 1.0, 1.0)
    p9.draw_text("7.2 STATUTORY APPOINTMENTS & FIT AND PROPER PERSON COMPLIANCE", 46, 608, font="F2", size=9.0)
    
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
         "All corporate directors of FAIRYTALES GROUP, ADOV LIMITED, and ADOV Care Group LIMITED must satisfy Regulation 5 (good character, financial "
         "solvency, absence of bankruptcy or serious criminal offenses, and mental/physical competence to oversee care delivery).")
    ]
    cur_gy = 590
    for g_t, g_d in gov_roles:
        p9.set_fill_color(0.12, 0.25, 0.50)
        p9.draw_text(g_t, 46, cur_gy, font="F2", size=7.5)
        cur_gy -= 10
        p9.set_fill_color(0.18, 0.22, 0.28)
        cur_gy = p9.draw_wrapped_text(g_d, 46, cur_gy, p9.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_gy -= 6
        
    # CQC Assessment & Quality Framework Box
    p9.set_fill_color(0.97, 0.99, 0.97)
    p9.set_stroke_color(0.15, 0.55, 0.25)
    p9.draw_rect(36, 42, p9.cw, 340, fill=True, stroke=True, stroke_w=1.0)
    
    p9.set_fill_color(0.12, 0.45, 0.20)
    p9.draw_rect(36, 353, p9.cw, 25, fill=True)
    p9.set_fill_color(1.0, 1.0, 1.0)
    p9.draw_text("7.3 CQC SINGLE ASSESSMENT FRAMEWORK & STATUTORY POLICIES", 46, 361, font="F2", size=9.0)
    
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
        p9.set_fill_color(0.12, 0.45, 0.20)
        p9.draw_text(q_t, 46, cur_qy, font="F2", size=7.5)
        cur_qy -= 10
        p9.set_fill_color(0.18, 0.22, 0.28)
        cur_qy = p9.draw_wrapped_text(q_d, 46, cur_qy, p9.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_qy -= 6


    # =========================================================================
    # PAGE 10: CHAPTER 8 - COMMISSIONING & ZERO-VOID STRATEGY
    # =========================================================================
    p10 = doc.add_page()
    p10.draw_header_banner("8", "COMMISSIONING & ZERO-VOID PLACEMENT PIPELINE", "OCCUPANCY ANNUITY")
    
    # Commissioning Architecture Box
    p10.set_fill_color(0.97, 0.98, 1.0)
    p10.set_stroke_color(0.20, 0.35, 0.60)
    p10.draw_rect(36, 640, p10.cw, 130, fill=True, stroke=True, stroke_w=1.0)
    
    p10.set_fill_color(0.10, 0.20, 0.40)
    p10.draw_rect(36, 745, p10.cw, 25, fill=True)
    p10.set_fill_color(1.0, 1.0, 1.0)
    p10.draw_text("8.1 LOCAL AUTHORITY & NHS COMMISSIONING FRAMEWORKS", 46, 753, font="F2", size=9.0)
    
    p10_comm_text = (
        "ADOV Care Group enters the Luton Adult Social Care commissioning ecosystem via three formal procurement mechanisms: "
        "1) Luton Borough Council ProContract Portal: Onboarding onto the Dynamic Purchasing System (DPS) under Framework AT1115 (Adult Supported "
        "Living Services). 2) NHS BLMK Integrated Care Board (ICB): Direct accreditation for NHS Continuing Healthcare (CHC) and Section 117 "
        "Mental Health Act joint-funded placements. 3) Transforming Care Partnership: Luton Social Services actively seeks local specialist providers "
        "to repatriate vulnerable adults currently placed in distant counties at exorbitant costs (£3,500-£4,500/week). ADOV Care Group's 8-bed "
        "campus provides the council with high-quality, local, cost-effective placement capacity."
    )
    p10.set_fill_color(0.15, 0.20, 0.25)
    p10.draw_wrapped_text(p10_comm_text, 46, 735, p10.cw - 20, font="F1", size=7.8, leading=10.0)
    
    # 6-Stage Zero-Void Placement Protocol Box
    p10.set_fill_color(0.98, 0.98, 0.99)
    p10.set_stroke_color(0.25, 0.35, 0.55)
    p10.draw_rect(36, 385, p10.cw, 245, fill=True, stroke=True, stroke_w=1.0)
    
    p10.set_fill_color(0.12, 0.22, 0.40)
    p10.draw_rect(36, 600, p10.cw, 25, fill=True)
    p10.set_fill_color(1.0, 1.0, 1.0)
    p10.draw_text("8.2 THE 6-STAGE ZERO-VOID REFERRAL & TRANSITION PROTOCOL", 46, 608, font="F2", size=9.0)
    
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
        p10.set_fill_color(0.12, 0.25, 0.50)
        p10.draw_text(s_title, 46, cur_sty, font="F2", size=7.2)
        cur_sty -= 9
        p10.set_fill_color(0.18, 0.22, 0.28)
        cur_sty = p10.draw_wrapped_text(s_desc, 46, cur_sty, p10.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_sty -= 4
        
    # Stakeholder Engagement Map Box
    p10.set_fill_color(0.97, 0.99, 0.97)
    p10.set_stroke_color(0.15, 0.55, 0.25)
    p10.draw_rect(36, 42, p10.cw, 332, fill=True, stroke=True, stroke_w=1.0)
    
    p10.set_fill_color(0.12, 0.45, 0.20)
    p10.draw_rect(36, 345, p10.cw, 25, fill=True)
    p10.set_fill_color(1.0, 1.0, 1.0)
    p10.draw_text("8.3 KEY REFERRAL STAKEHOLDERS IN LUTON GUARANTEEING OCCUPANCY", 46, 353, font="F2", size=9.0)
    
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
        p10.set_fill_color(0.12, 0.45, 0.20)
        p10.draw_text(k_t, 46, cur_sky, font="F2", size=7.5)
        cur_sky -= 10
        p10.set_fill_color(0.18, 0.22, 0.28)
        cur_sky = p10.draw_wrapped_text(k_d, 46, cur_sky, p10.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_sky -= 6


    # =========================================================================
    # PAGE 11: CHAPTER 9 - RISK REGISTRY & 26-WEEK EXECUTION ROADMAP
    # =========================================================================
    p11 = doc.add_page()
    p11.draw_header_banner("9", "STATUTORY RISK REGISTRY & 26-WEEK ROADMAP", "FAIRYTALES GROUP")
    
    # Risk Registry Table Box
    p11.set_fill_color(0.97, 0.98, 1.0)
    p11.set_stroke_color(0.20, 0.35, 0.60)
    p11.draw_rect(36, 525, p11.cw, 250, fill=True, stroke=True, stroke_w=1.0)
    
    p11.set_fill_color(0.10, 0.20, 0.40)
    p11.draw_rect(36, 750, p11.cw, 25, fill=True)
    p11.set_fill_color(1.0, 1.0, 1.0)
    p11.draw_text("9.1 STATUTORY RISK REGISTRY & MITIGATION CONTROLS", 46, 758, font="F2", size=9.0)
    
    rw = [105, 55, 60, 303]
    p11.set_fill_color(0.15, 0.25, 0.45)
    p11.draw_rect(36, 730, p11.cw, 16, fill=True)
    p11.set_fill_color(1.0, 1.0, 1.0)
    rx = 36
    r_hdrs = ["Risk Factor", "Likelihood", "Impact", "Statutory Mitigation Strategy"]
    for i, rh in enumerate(r_hdrs):
        p11.draw_text(rh, rx + 4, 735, font="F2", size=6.8)
        rx += rw[i]
        
    risk_data = [
        ("Town Planning Refusal", "VERY LOW", "CRITICAL", "Dual Section 192 CLPUD (Use Class C3b). Binding case law (North Devon) makes refusal ultra vires. Planning policies and neighbor letters are legally irrelevant."),
        ("CQC Registration Delay", "MEDIUM", "HIGH", "Headhunt qualified Level 5 RM at Day 1. Deploy fully pre-audited 42-policy suite and robust 5-year financial forecast to eliminate validation delays."),
        ("Staff Recruitment Deficit", "MEDIUM", "HIGH", "Recruit 14 full-time carers at £13.50/hr (above Luton market average). Deliver Oliver McGowan training and guarantee clear pathway to Team Leader."),
        ("Occupancy / Void Losses", "LOW", "HIGH", "Establish early pipeline with Luton ALDT (Charter House) and Transitions 16-25 Team. Average placement tenure is 7-15+ years; 28-day notice protects voids."),
        ("HMRC BIK Challenge (82)", "VERY LOW", "MEDIUM", "Formal Assured Shorthold Tenancy (AST) paying open market rent of £1,500/mo (£18,000/yr) from personal funds, legally reducing BIK to NIL under s.105/106 ITEPA.")
    ]
    cur_ry11 = 712
    for r_lbl, r_lk, r_imp, r_mit in risk_data:
        p11.set_fill_color(0.96, 0.98, 1.0)
        p11.draw_rect(36, cur_ry11 - 4, p11.cw, 28, fill=True)
        
        p11.set_fill_color(0.12, 0.22, 0.40)
        p11.draw_text(r_lbl, 40, cur_ry11 + 10, font="F2", size=6.8)
        
        p11.set_fill_color(0.05, 0.45, 0.15) if "VERY LOW" in r_lk or "LOW" in r_lk else p11.set_fill_color(0.75, 0.35, 0.05)
        p11.draw_text(r_lk, 145, cur_ry11 + 10, font="F2", size=6.5)
        
        p11.set_fill_color(0.70, 0.10, 0.10) if "CRITICAL" in r_imp or "HIGH" in r_imp else p11.set_fill_color(0.75, 0.35, 0.05)
        p11.draw_text(r_imp, 200, cur_ry11 + 10, font="F2", size=6.5)
        
        p11.set_fill_color(0.18, 0.22, 0.28)
        p11.draw_wrapped_text(r_mit, 260, cur_ry11 + 14, 255, font="F1", size=6.2, leading=8.0)
        cur_ry11 -= 31.0

    # 26-Week Critical Path Roadmap Table Box
    p11.set_fill_color(0.98, 0.98, 0.99)
    p11.set_stroke_color(0.25, 0.35, 0.55)
    p11.draw_rect(36, 175, p11.cw, 340, fill=True, stroke=True, stroke_w=1.0)
    
    p11.set_fill_color(0.12, 0.22, 0.40)
    p11.draw_rect(36, 490, p11.cw, 25, fill=True)
    p11.set_fill_color(1.0, 1.0, 1.0)
    p11.draw_text("9.2 26-WEEK CRITICAL PATH MASTER EXECUTION ROADMAP", 46, 498, font="F2", size=9.0)
    
    gw = [75, 115, 230, 103]
    p11.set_fill_color(0.15, 0.25, 0.45)
    p11.draw_rect(36, 472, p11.cw, 15, fill=True)
    p11.set_fill_color(1.0, 1.0, 1.0)
    gx = 36
    g_hdrs = ["Timeline", "Phase / Domain", "Key Statutory & Physical Deliverables", "Status / Milestone"]
    for i, gh in enumerate(g_hdrs):
        p11.draw_text(gh, gx + 4, 476, font="F2", size=6.5)
        gx += gw[i]
        
    gantt_rows = [
        ("Weeks 1 - 4", "Corporate & RM Setup", "Incorporate ADOV Care Group; Execute commercial FRI leases; Headhunt Level 5 Registered Manager.", "Phase 1 Complete"),
        ("Weeks 5 - 8", "Planning & CQC Portal", "Lodge Dual S.192 CLPUDs to Luton Council; Submit CQC provider application with 42 policies.", "Applications Lodged"),
        ("Weeks 9 - 16", "CapEx Refurbishment", "Procure contractors; Fit BS 5839-1 Cat L1 fire system, FD30S doors, wetroom upgrade, Doc E acoustic walls.", "Site Turnkey Ready"),
        ("Weeks 17 - 20", "Statutory Interviews", "CQC Fit & Proper interviews for RM & NI; Submit Luton Council ProContract DPS (AT1115) tender.", "Interviews Cleared"),
        ("Weeks 21 - 24", "Licensing & Commission", "Receive CQC Certificate of Registration; Building Control Sign-Off; Host ALDT social work showcases.", "CQC CERTIFICATE ISSUED"),
        ("Weeks 25 - 26", "Zero-Void Admissions", "Admit Residents 1-4 to 78 Marston Gardens; Stabilize 14 FT care team; Open Phase 2 (80 Marston Gdns).", "COMMERCIAL GO-LIVE")
    ]
    cur_gy11 = 454
    for g_time, g_ph, g_del, g_st in gantt_rows:
        p11.set_fill_color(0.96, 0.98, 1.0)
        p11.draw_rect(36, cur_gy11 - 4, p11.cw, 34, fill=True)
        
        p11.set_fill_color(0.85, 0.65, 0.18) if "GO-LIVE" in g_st or "ISSUED" in g_st else p11.set_fill_color(0.12, 0.22, 0.40)
        p11.draw_text(g_time, 40, cur_gy11 + 14, font="F2", size=6.8)
        p11.draw_text(g_ph, 115, cur_gy11 + 14, font="F2", size=6.5)
        
        p11.set_fill_color(0.18, 0.22, 0.28)
        p11.draw_wrapped_text(g_del, 230, cur_gy11 + 18, 220, font="F1", size=6.2, leading=8.0)
        
        p11.set_fill_color(0.05, 0.45, 0.15) if "ISSUED" in g_st or "GO-LIVE" in g_st else p11.set_fill_color(0.12, 0.25, 0.50)
        p11.draw_text(g_st, 460, cur_gy11 + 14, font="F2", size=6.2)
        cur_gy11 -= 38.0

    # Executive Declaration Box
    p11.set_fill_color(0.97, 0.99, 0.97)
    p11.set_stroke_color(0.15, 0.55, 0.25)
    p11.draw_rect(36, 42, p11.cw, 118, fill=True, stroke=True, stroke_w=1.0)
    
    p11.set_fill_color(0.12, 0.45, 0.20)
    p11.draw_rect(36, 135, p11.cw, 25, fill=True)
    p11.set_fill_color(1.0, 1.0, 1.0)
    p11.draw_text("9.3 FORMAL BOARD RESOLUTION: FAIRYTALES GROUP & ADOV LIMITED", 46, 143, font="F2", size=9.0)
    
    sign_text = (
        "RESOLVED: That FAIRYTALES GROUP (Trading Name of Mamun Limited) and ADOV LIMITED formally adopt the 8-Bed Unified "
        "Supported Living Masterplan across 78 & 80 Marston Gardens, Luton, dedicating the facility to Autism & Complex Learning Disabilities under Class C3(b). "
        "The Board approves the relocation of the executive beneficiary to 82 Marston Gardens via an Assured Shorthold Tenancy at £1,500/month, "
        "authorizes the execution of internal commercial FRI leases, approves the £150,000 turnkey capital expenditure, and directs the "
        "immediate submission of Dual Section 192 CLPUD applications to Luton Borough Council and provider registration to the CQC."
    )
    p11.set_fill_color(0.15, 0.20, 0.25)
    p11.draw_wrapped_text(sign_text, 46, 125, p11.cw - 20, font="F1", size=7.2, leading=9.4)


    # =========================================================================
    # PAGE 12: LUXURY BROCHURE BACK COVER
    # =========================================================================
    p12 = doc.add_page()
    p12.page_type = "back_cover"
    
    # Deep Midnight Navy Canvas
    p12.set_fill_color(0.04, 0.08, 0.16)
    p12.draw_rect(0, 0, p12.width, p12.height)
    
    # Outer Architectural Gold Frame
    p12.set_stroke_color(0.85, 0.65, 0.18)
    p12.draw_rect(24, 24, p12.width - 48, p12.height - 48, fill=False, stroke=True, stroke_w=1.5)
    
    # Inner Fine Gold Accent Frame
    p12.set_stroke_color(0.55, 0.42, 0.12)
    p12.draw_rect(28, 28, p12.width - 56, p12.height - 56, fill=False, stroke=True, stroke_w=0.6)
    
    # Gold Crest Badge Center Top
    p12.set_fill_color(0.85, 0.65, 0.18)
    p12.draw_rect(p12.width/2 - 40, p12.height - 120, 80, 24, fill=True)
    p12.set_fill_color(0.04, 0.08, 0.16)
    p12.draw_text("PROSPECTUS", p12.width/2, p12.height - 104, font="F2", size=9.5, align="center", max_w=70)
    
    # Back Cover Main Titles
    p12.set_fill_color(1.0, 1.0, 1.0)
    p12.draw_text("ADOV CARE GROUP", p12.width/2 - 130, p12.height - 165, font="F2", size=24.0)
    
    p12.set_fill_color(0.85, 0.65, 0.18)
    p12.draw_text("EXCELLENCE IN SPECIALIST SUPPORTED LIVING & PBS CARE", p12.width/2 - 170, p12.height - 188, font="F2", size=11.0)
    
    p12.set_stroke_color(0.85, 0.65, 0.18)
    p12.draw_line(70, p12.height - 200, p12.width - 70, p12.height - 200, stroke_w=1.0)
    
    # Closing Strategic Statement Card
    p12.set_fill_color(0.08, 0.14, 0.26)
    p12.set_stroke_color(0.25, 0.38, 0.60)
    p12.draw_rect(54, 410, p12.width - 108, 190, fill=True, stroke=True, stroke_w=1.0)
    
    p12.set_fill_color(0.85, 0.65, 0.18)
    p12.draw_text("THE DEFINITIVE HEALTHCARE & REAL ESTATE PROPOSITION", 70, 575, font="F2", size=10.0)
    
    back_statement = (
        "ADOV Care Group unites premier residential property assets with high-acuity specialist care commissioning "
        "to deliver an unparalleled model of social impact and commercial profitability. By establishing an 8-bed "
        "supported living campus across 78 & 80 Marston Gardens, the enterprise solves Luton Borough Council's critical "
        "need for local autism and complex learning disability placements, while delivering £523,328 in annual net group cashflow "
        "with an extraordinary 261.6% Return on Capital Employed (ROCE). Operating with zero neighbor friction, 8 dedicated "
        "off-street parking bays, and 100% lawful planning immunity under Use Class C3(b), the Marston Gardens campus represents "
        "the gold standard in sustainable, ethical, and high-yielding UK healthcare property development."
    )
    p12.set_fill_color(0.92, 0.95, 1.0)
    p12.draw_wrapped_text(back_statement, 70, 555, p12.width - 140, font="F1", size=7.8, leading=10.8)
    
    # Corporate Directory & Project Planner Box
    p12.set_fill_color(0.12, 0.18, 0.32)
    p12.set_stroke_color(0.85, 0.65, 0.18)
    p12.draw_rect(54, 150, p12.width - 108, 235, fill=True, stroke=True, stroke_w=1.2)
    
    p12.set_fill_color(0.85, 0.65, 0.18)
    p12.draw_text("PROJECT PLANNED BY ABDULLAHMAMUN.COM", 70, 360, font="F2", size=12.0)
    p12.set_stroke_color(0.85, 0.65, 0.18)
    p12.draw_line(70, 350, p12.width - 70, 350, stroke_w=0.6)
    
    dir_rows = [
        ("Strategic Project Planner:", "AbdullahMamun.com (Private Project & Business Consultant)"),
        ("Parent Holding Entity:", "FAIRYTALES GROUP (Trading Name of Mamun Limited / 100% Parent)"),
        ("Property Holding Entity:", "ADOV LIMITED (Freehold Asset Owner: 78 & 82 Marston Gardens)"),
        ("Operating Care Provider:", "ADOV Care Group LIMITED (CQC Regulated Activity: Personal Care)"),
        ("Care Campus Assets:", "78 & 80 Marston Gardens, Luton, Bedfordshire, LU2 7DY, UK"),
        ("Executive Family Residence:", "82 Marston Gardens, Luton, Bedfordshire, LU2 7DY, UK"),
        ("Official Executive Portal:", "www.AbdullahMamun.com  |  info@AbdullahMamun.com"),
        ("Lead Commissioning Bodies:", "Luton Borough Council Adult Social Care & NHS BLMK ICB")
    ]
    cur_dy12 = 332
    for dl, dv in dir_rows:
        p12.set_fill_color(0.70, 0.80, 0.95)
        p12.draw_text(dl, 70, cur_dy12, font="F2", size=7.5)
        p12.set_fill_color(1.0, 1.0, 1.0)
        p12.draw_text(dv, 210, cur_dy12, font="F1", size=7.5)
        cur_dy12 -= 18.0
        
    # Bottom Legal Disclaimer
    p12.set_fill_color(0.55, 0.65, 0.80)
    disclaimer = (
        "CONFIDENTIALITY & LEGAL NOTICE: This private investment prospectus is prepared exclusively for FAIRYTALES GROUP and ADOV LIMITED. "
        "All data, models, and projections are formulated by AbdullahMamun.com based on current UK Town Planning legislation (TCPA 1990 s.55), "
        "CQC Single Assessment Regulations, and Luton Borough Council Adult Social Care commissioning frameworks. "
        "Copyright © 2026 AbdullahMamun.com & FAIRYTALES GROUP. All rights reserved."
    )
    p12.draw_wrapped_text(disclaimer, 54, 110, p12.width - 108, font="F1", size=6.2, leading=8.5)

    doc.save()
    print("Full 12-Page Luxury Brochure PDF Successfully Generated!")


# ==============================================================================
# LUXURY BROCHURE WORD (.DOCX) OPENXML ENGINE (PURE PYTHON)
# ==============================================================================

def build_luxury_word_prospectus():
    filename = "ADOV_Care_Group_Private_Project_Prospectus.docx"
    
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '</Types>'
    )
    
    pkg_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '</Relationships>'
    )
    
    doc_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        '</Relationships>'
    )
    
    styles_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:docDefaults><w:rPrDefault><w:rPr>'
        '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>'
        '<w:sz w:val="22"/><w:color w:val="1E293B"/>'
        '</w:rPr></w:rPrDefault></w:docDefaults>'
        '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/>'
        '<w:rPr><w:b/><w:color w:val="0F1A2E"/><w:sz w:val="34"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/>'
        '<w:rPr><w:b/><w:color w:val="1E3A8A"/><w:sz w:val="26"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/>'
        '<w:rPr><w:b/><w:color w:val="D97706"/><w:sz w:val="22"/></w:rPr></w:style>'
        '</w:styles>'
    )
    
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
        p = (
            f'<w:p><w:pPr><w:pStyle w:val="ListParagraph"/>'
            f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
            f'<w:spacing w:after="80"/></w:pPr>'
            f'<w:r><w:t>• {safe}</w:t></w:r></w:p>'
        )
        doc_body.append(p)

    add_p("PRIVATE INVESTMENT & PROJECT PROSPECTUS", style="Heading3", bold=True, color="D97706", space_after=60)
    add_p("ADOV CARE GROUP - 8-BED SPECIALIST SUPPORTED LIVING CAMPUS", style="Heading1", bold=True, color="0F1A2E", space_after=80)
    add_p("Project Planned by AbdullahMamun.com", bold=True, color="D4AF37", space_after=100)
    add_p("Ultimate Parent Entity: FAIRYTALES GROUP (Trading Name of Mamun Limited)", bold=True, color="1E3A8A", space_after=60)
    add_p("Asset Holding Entity: ADOV LIMITED // Operating Entity: ADOV Care Group LIMITED", color="555555", space_after=60)
    add_p("Target Properties: 78 & 80 Marston Gardens (Care Campus) // 82 Marston Gardens (Executive Residence), Luton, LU2 7DY", color="555555", space_after=240)
    
    add_p("TABLE OF CONTENTS", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("Chapter 1: Executive Summary, Campus Real Estate Assets & Strategic Rationale (Page 3)")
    add_bullet("Chapter 2: Master 4-Sector Statutory Investment & Feasibility Matrix (Page 4)")
    add_bullet("Chapter 3: Statutory Town Planning Law & Dual Section 192 CLPUD Blueprint (Page 5)")
    add_bullet("Chapter 4: Corporate Governance, Intercompany FRI Leases & HMRC Tax Rent-Swap (Page 6)")
    add_bullet("Chapter 5: Architectural & Physical Infrastructure (Wetroom CapEx Optimization) (Page 7)")
    add_bullet("Chapter 6: Financial Engineering: Itemized CapEx Budget & 3-Year P&L Model (Page 8)")
    add_bullet("Chapter 7: Statutory Care Licensing: CQC Registration & Leadership Governance (Page 9)")
    add_bullet("Chapter 8: Local Authority Commissioning & Zero-Void Placement Pipeline (Page 10)")
    add_bullet("Chapter 9: Statutory Risk Registry, 26-Week Critical Path Roadmap & Resolution (Page 11)")
    add_bullet("Back Cover: Strategic Summary, Corporate Directory & Closing Sign-Off (Page 12)")

    add_p("1. EXECUTIVE SUMMARY & STRATEGIC RATIONALE", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_p(
        "This Private Project Prospectus, designed and formulated by AbdullahMamun.com for FAIRYTALES GROUP (Trading Name of Mamun Limited), "
        "establishes the definitive feasibility, town planning, corporate governance, architectural adaptation, CQC licensing, and zero-void "
        "occupancy model for an 8-bed specialist supported living campus across 78 & 80 Marston Gardens, Luton, with executive living at 82 Marston Gardens. "
        "Crucially, 78 and 80 form a self-contained semi-detached block with zero attached neighbors, twin driveways accommodating 8 cars off-street, "
        "and existing wetroom infrastructure that slashes CapEx by £42,000 to £150,000 while generating £1,043,328 in annual revenue "
        "and £523,328 in total net group cashflow.",
        space_after=140
    )
    
    add_p("2. MASTER 4-SECTOR INVESTMENT MATRIX & VERDICT", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_bullet("Sector 1 (Child Care EBD - Ages 8-17): Weekly fee £5,500; Gross revenue £1.15M/yr; Net EBITDA £434k/yr. DISQUALIFIED: Requires Class C2 full planning permission (severe neighbor resistance in residential street) and exposes the adjacent family home at 82 to police cruisers, missing-person episodes, and severe lifestyle disruption.")
    add_bullet("Sector 2 (Elderly Care - CQC C2): Weekly fee £800; Gross revenue £332k/yr; Operating expenses £380k/yr. DEFINITIVELY FATAL: Loses -£48,000/year due to lack of scale at 8 beds. Retrofitting a commercial passenger lift costs £45,000-£55,000 and destroys 2 ground-floor rooms. REJECTED.")
    add_bullet("Sector 3 (Mental Health Step-Down - s.117): Dual revenue: Care hours (£1,500/wk) + Exempt Housing Benefit (£350/wk). Gross revenue £640k/yr; Net EBITDA £165k/yr. VIABLE SECONDARY: Higher turnover (3-12 month stays) creates void risks and relapse management challenges.")
    add_bullet("Sector 4 (Autism & Complex LD PBS Supported Living): Weekly tariff £2,500 (£2,150 care + £350 SEA Housing Benefit). Gross revenue £1,043,328/yr; Net EBITDA £408,328/yr (39.1% margin); Total Net Group Cashflow £523,328/yr. UNDISPUTED CHAMPION (Score 98/100): 100% lawful planning immunity via Class C3(b) Section 192 CLPUD, zero police involvement, and 7-15+ year placements eliminating voids.")

    add_p("3. STATUTORY PLANNING LAW & SECTION 192 CLPUD", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_bullet("Statutory Legal Foundation: Town & Country Planning Act 1990 s.55(2)(f) and Town & Country Planning (Use Classes) Order 1987 Class C3(b) (up to 6 persons living together as a single household receiving care).")
    add_bullet("High Court Binding Precedents: North Devon DC v First Secretary of State [2004] EWHC 587 (Admin) established that adults who cannot live independently living with resident/visiting carers constitute a single household. Hossack v Kettering BC [2002] and Crawley BC v FSS [2004] confirm domestic character is determinative.")
    add_bullet("Dual S.192 CLPUD Submissions: Submitting two separate Certificate of Lawfulness applications (78 for 5 beds, 80 for 3 beds) guarantees statutory immunity. Planning officers cannot evaluate need, neighbor letters, or traffic. Refusal is legally ultra vires.")
    add_bullet("Highways & Parking: Luton Local Plan Policy LLP32 and Appendix 2 standards are fully satisfied by the 8 dedicated off-street parking bays (4 on each driveway) and 2 garages.")

    add_p("4. CORPORATE ARCHITECTURE & TAX-NEUTRAL RENT-SWAP", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_bullet("Corporate Hierarchy: FAIRYTALES GROUP (Trading Name of Mamun Limited / 100% Parent) -> ADOV LIMITED (PropCo holding 78 & 82) + Director (Personal owner of 80) -> ADOV Care Group LIMITED (OpCo / CQC Registered Entity).")
    add_bullet("Intercompany Commercial Leases: 78 Marston Gardens is leased to OpCo for £65,000/yr; 80 Marston Gardens is leased to OpCo for £50,000/yr. Total rent = £115,000/yr (100% tax-deductible trading expense in OpCo, saving £28,750/yr Corporation Tax).")
    add_bullet("HMRC Tax-Neutral Rent-Swap for 82 Marston Gardens: Director resides at 82 under a formal Assured Shorthold Tenancy (AST), paying open market rent of £1,500/month (£18,000/yr) from personal funds. Under s.105 & s.106 ITEPA 2003, paying full market rent reduces Benefit in Kind (BIK) to NIL.")
    add_bullet("Net Personal Cashflow: Director receives £50,000/yr rent for 80, pays £18,000/yr rent for 82, netting +£32,000/yr in tax-efficient personal cashflow.")
    add_bullet("ATED & VAT: 82 Marston Gardens is valued <£500k (immune to ATED). Welfare services are VAT-exempt under VATA 1994 Sch 9 Grp 7. ADOV LIMITED does NOT opt to tax commercial rents.")

    add_p("5. ARCHITECTURAL & INFRASTRUCTURE ADAPTATION", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_bullet("Existing Wetroom Capital Advantage: Both 78 and 80 already possess 1 separate WC and 1 large-size wetroom; 78 has an en-suite. By adding only 1 additional en-suite to Bed 2 in 78, sanitary ratios reach 1:1.25 in 78 and 1:1.5 in 80 (exceeding CQC standard of 1:3). Slashes CapEx by £42,000.")
    add_bullet("Life Safety & Fire Engineering: Installation of BS 5839-1 Category L1 addressable fire alarm system across all rooms, FD30S fire doors with acoustic cold-smoke seals, and BS 5266-1 emergency lighting.")
    add_bullet("Infection Control & HTM 01-04: Establishment of dedicated commercial barrier laundry with thermal disinfection (71°C for 3 min).")
    add_bullet("Acoustic Soundproofing (Document E): High-density SoundBloc acoustic insulation installed across the internal party wall and bedroom partitions (>43dB separation).")

    add_p("6. FINANCIAL P&L & INVESTMENT RETURNS", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_bullet("Turnkey CapEx: £150,000 across both properties (£18,750/bed), including fire safety, sanitary works, acoustic insulation, sensory room, CQC legal costs, and £20k cash reserve.")
    add_bullet("Gross Stabilized Revenue (Year 2 @ 88% / 7 active beds): £1,043,328 / year (Core Care £179k + 1:1 PBS £736k + Supported Exempt Housing Benefit £127k).")
    add_bullet("Direct Operating Costs: Frontline PBS Carers (14 FT @ £13.50/hr): £425,000; Registered Manager & Team Leader: £60,000; Food, Utilities, Software & Insurance: £35,000; Total OpEx = £520,000/year.")
    add_bullet("Property Rent: £115,000 / year paid internally to PropCo & Director.")
    add_bullet("Net EBITDA Profit: £408,328 / year (39.1% net EBITDA margin).")
    add_bullet("Total Net Group Cashflow: £523,328 / year (OpCo Profit + Property Rents).")
    add_bullet("Return on Capital Employed (ROCE): 261.6% per annum on £150,000 CapEx. Full capital payback in 3.5 months.")

    add_p("7. STATUTORY LICENSING & CQC REGISTRATION", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_bullet("Regulated Activity: 'Personal Care' in Supported Living under Health & Social Care Act 2008 Regs 2014.")
    add_bullet("Registered Manager (Regulation 7): Level 5 Diploma in Leadership & Management for Adult Care, min 3 yrs autism/LD experience, enhanced DBS, CQC Fit and Proper interview.")
    add_bullet("Nominated Individual (Regulation 6): Corporate Director appointed for statutory supervision.")
    add_bullet("Oliver McGowan Mandatory Training: All 14 frontline staff trained in Tier 1 and Tier 2 autism/LD competencies prior to intake.")
    add_bullet("Single Assessment Framework: 34 Quality Statements embedded across Safe, Effective, Caring, Responsive, and Well-Led domains.")

    add_p("8. COMMISSIONING & ZERO-VOID STRATEGY", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_bullet("Procurement Portals: Onboarding onto Luton Borough Council ProContract DPS (Framework AT1115) and NHS BLMK ICB Continuing Healthcare Framework.")
    add_bullet("Local Repatriation Priority: Partnering with Luton Adult Learning Disability Team (ALDT) at Charter House and Transitions 16-25 Team to repatriate out-of-borough placements.")
    add_bullet("6-Stage Placement Protocol: 1) 48h Desk Review. 2) Multidisciplinary Assessment. 3) Peer Sensory Matching. 4) Individual Placement Agreement (£2,500/wk). 5) Graduated 4-Week Transition. 6) Tenancy & Admission.")
    add_bullet("Zero Void Guarantee: 7-15+ year average length of stay; 28-day notice period and council retainer fees during temporary hospitalizations.")

    add_p("9. 26-WEEK EXECUTION ROADMAP & RESOLUTION", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_bullet("Weeks 1-4: Corporate structuring, FRI commercial leases, recruitment of Level 5 RM.")
    add_bullet("Weeks 5-8: Dual Section 192 CLPUD submission to Luton Planning; CQC portal submission with 42 policies.")
    add_bullet("Weeks 9-16: CLPUD determination; Contractor CapEx fit-out (Cat L1 fire, wetroom upgrade, Doc E acoustic walls).")
    add_bullet("Weeks 17-20: CQC Fit & Proper interviews; Luton ProContract DPS submission.")
    add_bullet("Weeks 21-24: CQC Registration Certificate issued; Building Control sign-off; ALDT social work showcases.")
    add_bullet("Weeks 25-26: Phased admission of Residents 1-4; Operational Go-Live; £523k/year cashflow activation.")

    add_p("CORPORATE DIRECTORY & CLOSING DECLARATION", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("Project Strategic Planner: AbdullahMamun.com (Private Project & Business Consultant)")
    add_bullet("Parent Holding Entity: FAIRYTALES GROUP (Trading Name of Mamun Limited)")
    add_bullet("Property Holding Entity: ADOV LIMITED (Asset Owner: 78 & 82 Marston Gardens)")
    add_bullet("Care Operating Entity: ADOV Care Group LIMITED (CQC Provider)")
    add_bullet("Executive Website: www.AbdullahMamun.com")

    doc_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body>' + "".join(doc_body) +
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>'
        '</w:body></w:document>'
    )
    
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as docx:
        docx.writestr('[Content_Types].xml', content_types)
        docx.writestr('_rels/.rels', pkg_rels)
        docx.writestr('word/_rels/document.xml.rels', doc_rels)
        docx.writestr('word/styles.xml', styles_xml)
        docx.writestr('word/document.xml', doc_xml)
        
    print(f"Generated Master Luxury Word Prospectus '{filename}' successfully.")


if __name__ == "__main__":
    build_luxury_brochure_pdf()
    build_luxury_word_prospectus()
''')

print("append_brochure_p8_p12 written.")
