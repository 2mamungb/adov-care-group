
def add_pages_1_to_3(pdf):
    # --------------------------------------------------------------------------
    # PAGE 1: COVER & WORKING PAPER ABSTRACT (OXFORD/CAMBRIDGE STYLE)
    # --------------------------------------------------------------------------
    p1 = pdf.add_page(is_cover=True)
    
    p1.set_stroke_color(0.08, 0.14, 0.24)
    p1.draw_line(p1.mx, p1.height - 36, p1.width - p1.mx, p1.height - 36, stroke_w=1.2)
    p1.draw_line(p1.mx, p1.height - 40, p1.width - p1.mx, p1.height - 40, stroke_w=0.5)
    
    p1.set_fill_color(0.40, 0.45, 0.55)
    p1.draw_text("WORKING PAPER SERIES IN HEALTH ECONOMICS & ASSET STRATEGY // MONOGRAPH NO. 2026-MG-04", p1.mx, p1.height - 52, font="F2", size=7.2)
    p1.draw_text("OCTOBER 2026 // DEFINITIVE COMMISSION APPRAISAL", p1.width - p1.mx, p1.height - 52, font="F1", size=7.0, align="right", max_w=220)
    
    p1.set_fill_color(0.08, 0.14, 0.24)
    p1.draw_text("STRATEGIC CAMPUS LOCATION & OPERATIONAL APPRAISAL", p1.mx, p1.height - 82, font="F2", size=16.5)
    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("Head-to-Head Feasibility: Unified Campus (78 & 80) vs. Disconnected Properties (78 & 82)", p1.mx, p1.height - 99, font="F2", size=10.0)
    p1.set_fill_color(0.35, 0.42, 0.52)
    p1.draw_text("A Forensic Multi-Dimensional Evaluation across Workforce Rotas, Planning Law, CapEx, HMRC Tax & Family Living", p1.mx, p1.height - 113, font="F3", size=8.0)
    
    p1.set_stroke_color(0.75, 0.80, 0.88)
    p1.draw_line(p1.mx, p1.height - 121, p1.width - p1.mx, p1.height - 121, stroke_w=0.6)
    
    p1.set_fill_color(0.08, 0.14, 0.24)
    p1.draw_text("INSTITUTIONAL METADATA & STATUTORY GOVERNANCE FRAMEWORK", p1.mx, p1.height - 134, font="F2", size=7.6)
    
    meta_rows = [
        ("Lead Project Author:", "Project Planned by AbdullahMamun.com (Strategic Advisory Lead)"),
        ("Commissioning Holding Entity:", "FAIRYTALES GROUP (Trading Name of Mamun Limited)"),
        ("Asset Holding & OpCo Entities:", "ADOV LIMITED (Freehold Asset Co) & ADOV Care Group LIMITED (Regulated OpCo)"),
        ("Statutory Planning Framework:", "Town & Country Planning (Use Classes) Order 1987 (Class C3b / C2) // Luton Local Plan LLP32"),
        ("Regulated Quality Standards:", "Health and Social Care Act 2008 (Regulated Activities) Regulations 2014 (Reg 12, 15, 18)")
    ]
    cur_ay = p1.height - 146
    for l_txt, v_txt in meta_rows:
        p1.set_fill_color(0.40, 0.45, 0.55)
        p1.draw_text(l_txt, p1.mx, cur_ay, font="F2", size=6.8)
        p1.set_fill_color(0.12, 0.16, 0.24)
        p1.draw_text(v_txt, p1.mx + 140, cur_ay, font="F1", size=6.8)
        cur_ay -= 11.5
        
    p1.set_stroke_color(0.75, 0.80, 0.88)
    p1.draw_line(p1.mx, cur_ay + 1, p1.width - p1.mx, cur_ay + 1, stroke_w=0.6)
    cur_ay -= 12
    
    p1.set_fill_color(0.08, 0.14, 0.24)
    p1.draw_text("EXECUTIVE ABSTRACT & STATUTORY COMMISSION MANDATE", p1.mx, cur_ay, font="F2", size=8.0)
    cur_ay -= 10
    
    p1_abstract = (
        "This academic working paper delivers a forensic operational, spatial, and financial appraisal commissioned by the Board of "
        "Directors of FAIRYTALES GROUP to determine the definitive campus deployment for an 8-bed high-dependency residential supported living "
        "facility for adults presenting with severe autism and complex challenging behaviours. The appraisal conducts a rigorous head-to-head "
        "evaluation between two mutually exclusive configurations on Marston Gardens, Luton: Scenario A (unifying contiguous semi-detached "
        "properties 78 & 80 into a single 8-bed operational campus, relocating the founding Director to modern detached 82) versus Scenario B "
        "(operating disconnected facilities across 78 and detached 82, leaving the Director residing at 80). Utilizing statutory health "
        "economics methodologies, empirical night rota workforce modeling under CQC Regulation 18, and HMRC tax jurisprudence (ITEPA 2003 "
        "ss.105-106), this monograph establishes that Scenario A represents the only legally compliant, operationally viable, and commercially "
        "resilient configuration. Scenario B induces structural night rota duplication (£70,200/year deadweight loss), exposes the Director's family "
        "to severe acoustic nuisance under Section 79 EPA 1990, and destroys £32,000/year in tax-neutral director living allowance."
    )
    cur_ay = p1.draw_wrapped_text(p1_abstract, p1.mx, cur_ay, p1.cw, font="F1", size=7.1, leading=9.6)
    cur_ay -= 8
    
    t1_cols = [("Performance Indicator / Dimension", 165), ("Scenario A: Campus (78 & 80)", 175), ("Scenario B: Split (78 & 82)", 175)]
    t1_rows = [
        ("Specialist Bed Capacity", "8 High-Dependency Autism Beds", "8 Disconnected Beds (5 at 78 + 3 at 82)"),
        ("Spatial Contiguity & Party Wall", "Contiguous Pair // 100% Internal Party Wall", "Disconnected Across Public Street // External Party Wall"),
        ("Night Staffing Model (CQC Reg 18)", "Unified Hub: 1 Waking Night + 1 Sleep-in", "Duplicate Rotas: 2 Waking Nights + 2 Sleep-ins"),
        ("Annual Waking Night Payroll", "£140,400 / year (Optimized)", "£210,600 / year (+£70,200 Deadweight Penalty)"),
        ("CapEx Conversion Budget", "£143,000 (80 already has DDA Wetroom)", "£230,000 (+£87,000 CapEx Destruction)"),
        ("HMRC AST Rent Arbitrage (ITEPA 03)", "£0 BIK // +£32,000/year Surplus Cash", "£0 Rent Surplus // Family Entangled at 80"),
        ("Year 1 Net EBITDA", "£265,000 (31.8% EBITDA Margin)", "£187,000 (22.5% EBITDA Margin // -£78k Delta)"),
        ("3-Year Cumulative EBITDA", "£1,254,000 (Highly Resilient)", "£1,020,000 (-£234,000 Cumulative Cash Drain)")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.0: CORE EMPIRICAL PERFORMANCE INDICATORS (HEAD-TO-HEAD SYNTHESIS)", t1_cols, t1_rows, cur_ay, row_h=11.5, font_size=6.3)
    cur_ay -= 4
    
    p1_rec_box = (
        "DEFINITIVE STRATEGIC DETERMINATION: The Board of Directors of FAIRYTALES GROUP unanimously adopts SCENARIO A. "
        "Operating 78 & 80 as a contiguous 8-bed campus captures an immediate £87,000 CapEx saving, eliminates £70,200/year in duplicate night staff "
        "wages, secures statutory immunity against Section 79 EPA 1990 noise abatement notices, and unlocks £32,000/year in tax-free family cash surplus."
    )
    cur_ay = p1.draw_academic_callout("STRATEGIC DIRECTIVE // FAIRYTALES GROUP BOARD OF DIRECTORS", p1_rec_box, cur_ay, h=44)
    cur_ay -= 2
    
    p1.set_fill_color(0.08, 0.14, 0.24)
    p1.draw_text("CORE EMPIRICAL FINDINGS & BOARD TAKEAWAYS", p1.mx, cur_ay, font="F2", size=7.4)
    cur_ay -= 9
    
    bullets_p1 = [
        ("Spatial Decoupling:", "Contiguous 78 & 80 internalizes all acoustic and behavioural impact within group curtilage, insulated by 8 driveway spaces."),
        ("Workforce Efficiency:", "Unified night rota saves 8,760 staff hours and £210,600 in payroll over 3 years while satisfying CQC Regulation 18."),
        ("Tax-Neutral Arbitrage:", "Executing open-market AST for 82 Marston Gardens eliminates BIK under ITEPA 2003 s.105/106 and yields £32k/yr surplus."),
        ("Planning & CapEx Certainty:", "80 already possesses an extended commercial DDA wetroom; Section 192 CLEUD secures lawful Class C3b care use.")
    ]
    for b_title, b_desc in bullets_p1:
        p1.set_fill_color(0.76, 0.61, 0.22)
        p1.draw_text("•", p1.mx + 2, cur_ay, font="F2", size=7.0)
        p1.set_fill_color(0.08, 0.14, 0.24)
        p1.draw_text(b_title, p1.mx + 10, cur_ay, font="F2", size=6.7)
        p1.set_fill_color(0.20, 0.25, 0.35)
        p1.draw_text(b_desc, p1.mx + 95, cur_ay, font="F1", size=6.6)
        cur_ay -= 10.5
        
    p1.set_stroke_color(0.75, 0.80, 0.88)
    p1.draw_line(p1.mx, 48, p1.width - p1.mx, 48, stroke_w=0.6)
    p1.set_fill_color(0.40, 0.45, 0.55)
    p1.draw_text("Project Planned by AbdullahMamun.com  |  FAIRYTALES GROUP  |  ADOV LIMITED  |  Print-Ready Academic Monograph", p1.mx, 36, font="F1", size=6.5)


    # --------------------------------------------------------------------------
    # PAGE 2: 1.0 EXECUTIVE SUMMARY & 2.0 ASSET TOPOLOGY BASELINE
    # --------------------------------------------------------------------------
    p2 = pdf.add_page()
    p2.draw_academic_header("SECTION 1.0 & 2.0", "EXECUTIVE SUMMARY & ASSET TOPOLOGY")
    
    y = p2.height - 48
    y = p2.draw_section_heading("1.0", "EXECUTIVE SUMMARY & STRATEGIC RATIONALE", y)
    
    p2_txt1 = (
        "This strategic location appraisal addresses a critical commercial, operational, and domestic crossroad confronting "
        "the Board of Directors of FAIRYTALES GROUP and its operating subsidiaries (ADOV LIMITED and ADOV Care Group LIMITED). "
        "The group has acquired and controls three significant residential properties on Marston Gardens, Luton (numbers 78, 80, and 82). "
        "The core commercial objective is the commissioning and long-term operation of a high-dependency supported living facility for adults "
        "aged 18 to 64 presenting with severe autism, complex learning disabilities, and challenging behavioural needs, funded under "
        "specialist local authority social care and NHS Continuing Healthcare (CHC) tariffs."
    )
    y = p2.draw_wrapped_text(p2_txt1, p2.mx, y, p2.cw, font="F1", size=7.3, leading=9.8)
    y -= 6
    
    y = p2.draw_section_heading("1.1", "The Core Operational Dilemma: Unified Campus vs. Disconnected Sites", y)
    p2_txt2 = (
        "Currently, the founding Director and their family reside in 80 Marston Gardens, an extended 3-bedroom property with extensive "
        "ground-floor living space, a commercial-size wetroom, and an independent driveway. Directly adjoining 80 is 78 Marston Gardens, "
        "a 5-bedroom property configured for care operations. Crucially, 78 and 80 form a contiguous semi-detached building block flanked on both "
        "sides by wide 4-car private driveways, completely insulated from any attached residential neighbours. Located 30 meters down the street "
        "is 82 Marston Gardens, a detached 4-bedroom house. The Board faces two mutually exclusive options:\n\n"
        "• SCENARIO A (The Unified 8-Bed Specialist Campus): Unify 78 and 80 Marston Gardens under 10-year commercial leases to ADOV Care Group "
        "LIMITED to operate as an integrated 8-bed supported living scheme. The Director relocates their family residence to 82 Marston Gardens "
        "under an open-market Assured Shorthold Tenancy (AST at £1,500/month).\n\n"
        "• SCENARIO B (The Disconnected Properties Model): Commission 78 Marston Gardens as a 5-bed care facility and convert 82 Marston Gardens "
        "into a 3-bed care facility down the street. The Director's family remains residing at 80 Marston Gardens, sharing a party wall with 78."
    )
    y = p2.draw_wrapped_text(p2_txt2, p2.mx, y, p2.cw, font="F1", size=7.2, leading=9.6)
    y -= 6
    
    y = p2.draw_section_heading("1.2", "Statutory & Economic Imperatives in Complex Autism Commissioning", y)
    p2_txt12 = (
        "Commissioners from NHS Integrated Care Boards (ICBs) and Bedfordshire Local Authorities evaluate supported living schemes against "
        "exacting regulatory metrics under the Building the Right Support national guidance. Placements commanding £3,000 to £3,500 weekly "
        "tariffs demand dedicated sensory de-escalation environments, robust single-point management oversight, and bulletproof staffing "
        "continuity. Fragmenting 8 beds across disconnected residential addresses introduces operational instability that jeopardises ICB placement approvals."
    )
    y = p2.draw_wrapped_text(p2_txt12, p2.mx, y, p2.cw, font="F1", size=7.2, leading=9.6)
    y -= 6
    
    y = p2.draw_section_heading("2.0", "ASSET TOPOLOGY & SPATIAL CONFIGURATION", y)
    p2_txt3 = (
        "The physical property cluster on Marston Gardens presents distinct architectural characteristics. Numbers 78 and 80 were "
        "constructed together as a pair of substantial semi-detached residences. Both properties have been extensively modernized and extended, "
        "incorporating wide private driveways on their outer flanks. Together, they create a standalone architectural footprint. "
        "Number 82 is a detached, modern executive family residence set in private domestic grounds with a dedicated garden."
    )
    y = p2.draw_wrapped_text(p2_txt3, p2.mx, y, p2.cw, font="F1", size=7.2, leading=9.6)
    y -= 6
    
    cols_t2 = [("Property", 85), ("Structural Baseline", 110), ("Specialist Bedrooms", 85), ("Sanitary / Wetrooms", 115), ("Parking / Garages", 120)]
    rows_t2 = [
        ("78 Marston Gdns", "Extended Semi-Detached", "5 Resident Bedrooms", "1 Wetroom, 1 En-suite, 1 WC", "4-Car Driveway + Rear Garage"),
        ("80 Marston Gdns", "Extended Semi-Detached", "3 Resident Bedrooms", "1 Large Wetroom, 1 WC, 1 En-suite", "4-Car Driveway + Rear Garage"),
        ("82 Marston Gdns", "Modern Detached House", "4 Domestic Bedrooms", "1 Family Bath, 1 En-suite, 1 WC", "1-2 Off-Street Driveway Spaces")
    ]
    y = p2.draw_booktabs_table("TABLE 2.0: PHYSICAL ASSET ATTRIBUTES & STRUCTURAL BASELINE", cols_t2, rows_t2, y, row_h=12.0, font_size=6.3)
    y -= 4
    
    y = p2.draw_section_heading("2.1", "Site Boundary, Curtilage & Parking Infrastructure (Luton Local Plan LLP32)", y)
    p2_curtilage = (
        "A critical asset advantage of 78 & 80 Marston Gardens is the substantial curtilage and private off-street parking capacity. "
        "Each property features an independent, hard-standing private driveway accommodating 4 vehicles, delivering a combined capacity of "
        "8 off-street spaces, supplemented by two detached brick-built garages at the rear. Under Luton Local Plan 2011-2031 Policy LLP32, "
        "commercial care operations must demonstrate adequate parking to prevent on-street congestion. Unifying 78 & 80 provides complete on-site "
        "absorption of shift changeovers, multidisciplinary team (MDT) visits, and emergency vehicles, securing total highway compliance."
    )
    y = p2.draw_wrapped_text(p2_curtilage, p2.mx, y, p2.cw, font="F1", size=7.2, leading=9.6)
    y -= 6
    
    p2.draw_academic_callout(
        "TOPOLOGICAL TAKEAWAY // INTERNALISATION OF PARTY WALL BOUNDARIES",
        "78 and 80 Marston Gardens form an entirely self-contained residential island. Unifying them internalizes all acoustic and party "
        "wall friction within ADOV Care Group curtilage, eliminating statutory nuisance risk under Section 79 Environmental Protection Act 1990.",
        y, h=44
    )


    # --------------------------------------------------------------------------
    # PAGE 3: FIGURE 1 & SPATIAL CONTIGUITY ANALYSIS
    # --------------------------------------------------------------------------
    p3 = pdf.add_page()
    p3.draw_academic_header("SECTION 2.0 (CONT.)", "SPATIAL CONTIGUITY & SITE SCHEMATIC")
    
    y = p3.height - 48
    y = p3.draw_section_heading("2.2", "Spatial Contiguity vs. Public Street Disconnection", y)
    
    p3_txt = (
        "The spatial relationship between the physical assets represents the fundamental constraint governing care home "
        "operations. 78 and 80 Marston Gardens form a unique, semi-detached architectural block that is completely detached from all "
        "other residential properties. Flanked on both sides by wide 4-car private driveways, the combined block enjoys a 10-meter "
        "acoustic buffer to the nearest neighbouring houses. By contrast, 82 Marston Gardens is a detached residential house located "
        "30 meters to the west, separated by public roadway and an intervening third-party residence."
    )
    y = p3.draw_wrapped_text(p3_txt, p3.mx, y, p3.cw, font="F1", size=7.2, leading=9.6)
    y -= 6
    
    p3.set_fill_color(0.08, 0.14, 0.24)
    p3.draw_text("FIGURE 1: ARCHITECTURAL SITE PLAN & SPATIAL TOPOLOGY SCHEMATIC", p3.mx, y, font="F2", size=7.8)
    y -= 6
    
    fig1_h = 195
    fig1_y = y - fig1_h
    p3.set_fill_color(0.99, 0.995, 1.0)
    p3.set_stroke_color(0.70, 0.78, 0.88)
    p3.draw_rect(p3.mx, fig1_y, p3.cw, fig1_h, fill=True, stroke=True, stroke_w=0.8)
    
    # Roadway
    p3.set_fill_color(0.92, 0.94, 0.96)
    p3.draw_rect(p3.mx + 10, fig1_y + fig1_h - 24, p3.cw - 20, 18, fill=True, stroke=True, stroke_w=0.5)
    p3.set_fill_color(0.40, 0.45, 0.55)
    p3.draw_text("MARSTON GARDENS (PUBLIC HIGHWAY // RESIDENTIAL ACCESS ROAD)", p3.mx + 15, fig1_y + fig1_h - 13, font="F2", size=7.0)
    
    # Contiguous Block 78 & 80
    cw_block = 245
    cx_block = p3.mx + 25
    cy_block = fig1_y + 22
    ch_block = 135
    
    p3.set_fill_color(0.95, 0.97, 1.0)
    p3.set_stroke_color(0.08, 0.14, 0.24)
    p3.draw_rect(cx_block, cy_block, cw_block, ch_block, fill=True, stroke=True, stroke_w=1.2)
    
    p3.set_stroke_color(0.76, 0.61, 0.22)
    p3.draw_line(cx_block + cw_block/2, cy_block, cx_block + cw_block/2, cy_block + ch_block, stroke_w=1.4)
    
    # 78 Half
    p3.set_fill_color(0.08, 0.14, 0.24)
    p3.draw_text("78 MARSTON GDNS", cx_block + 10, cy_block + ch_block - 18, font="F2", size=7.6)
    p3.set_fill_color(0.20, 0.28, 0.38)
    p3.draw_text("• 5 Resident Bedrooms", cx_block + 10, cy_block + ch_block - 32, font="F1", size=6.5)
    p3.draw_text("• Commercial Life-Skills Kitchen", cx_block + 10, cy_block + ch_block - 44, font="F1", size=6.5)
    p3.draw_text("• Communal Wetroom & En-suite", cx_block + 10, cy_block + ch_block - 56, font="F1", size=6.5)
    p3.draw_text("• Central HTM 01-04 Laundry", cx_block + 10, cy_block + ch_block - 68, font="F1", size=6.5)
    p3.draw_text("• Cat L1 Addressable Fire Alarm", cx_block + 10, cy_block + ch_block - 80, font="F1", size=6.5)
    p3.draw_text("• Detached Rear Lock-up Garage", cx_block + 10, cy_block + ch_block - 92, font="F1", size=6.5)
    
    # 80 Half
    p3.set_fill_color(0.08, 0.14, 0.24)
    p3.draw_text("80 MARSTON GDNS", cx_block + cw_block/2 + 10, cy_block + ch_block - 18, font="F2", size=7.6)
    p3.set_fill_color(0.20, 0.28, 0.38)
    p3.draw_text("• 3 Resident Bedrooms", cx_block + cw_block/2 + 10, cy_block + ch_block - 32, font="F1", size=6.5)
    p3.draw_text("• Ground-Floor DDA Wetroom", cx_block + cw_block/2 + 10, cy_block + ch_block - 44, font="F1", size=6.5)
    p3.draw_text("• Sensory Suite & Therapy Lounge", cx_block + cw_block/2 + 10, cy_block + ch_block - 56, font="F1", size=6.5)
    p3.draw_text("• RM Office & Staff Sleep-In", cx_block + cw_block/2 + 10, cy_block + ch_block - 68, font="F1", size=6.5)
    p3.draw_text("• Quiet Dining & Day Room", cx_block + cw_block/2 + 10, cy_block + ch_block - 80, font="F1", size=6.5)
    p3.draw_text("• Detached Rear Lock-up Garage", cx_block + cw_block/2 + 10, cy_block + ch_block - 92, font="F1", size=6.5)
    
    # Flanking Driveways
    p3.set_fill_color(0.90, 0.93, 0.96)
    p3.draw_rect(cx_block - 16, cy_block, 14, ch_block, fill=True, stroke=True, stroke_w=0.5)
    p3.draw_rect(cx_block + cw_block + 2, cy_block, 14, ch_block, fill=True, stroke=True, stroke_w=0.5)
    
    p3.set_fill_color(0.35, 0.42, 0.52)
    p3.draw_text("4 Bays", cx_block - 16, cy_block + 12, font="F2", size=5.5)
    p3.draw_text("4 Bays", cx_block + cw_block + 2, cy_block + 12, font="F2", size=5.5)
    
    p3.set_fill_color(0.12, 0.40, 0.22)
    p3.draw_text("SCENARIO A: CONTIGUOUS 8-BED CAMPUS (100% INTERNAL PARTY WALL // 8 DRIVEWAY SPACES)", cx_block + 6, cy_block + 12, font="F2", size=6.3)
    
    # 82 Marston Gardens
    cx_82 = p3.mx + cw_block + 70
    cw_82 = 135
    p3.set_fill_color(0.98, 0.99, 0.95)
    p3.set_stroke_color(0.76, 0.61, 0.22)
    p3.draw_rect(cx_82, cy_block + 18, cw_82, ch_block - 36, fill=True, stroke=True, stroke_w=1.0)
    
    p3.set_fill_color(0.08, 0.14, 0.24)
    p3.draw_text("82 MARSTON GDNS", cx_82 + 8, cy_block + ch_block - 26, font="F2", size=7.6)
    p3.set_fill_color(0.20, 0.28, 0.38)
    p3.draw_text("Director Private Residence", cx_82 + 8, cy_block + ch_block - 40, font="F2", size=6.6)
    p3.draw_text("• 4-Bed Modern Detached", cx_82 + 8, cy_block + ch_block - 52, font="F1", size=6.3)
    p3.draw_text("• 100% Family Tranquility", cx_82 + 8, cy_block + ch_block - 64, font="F1", size=6.3)
    p3.set_fill_color(0.76, 0.61, 0.22)
    p3.draw_text("30-Meter Oversight Walk", cx_82 + 8, cy_block + ch_block - 76, font="F3", size=6.2)
    
    p3.set_stroke_color(0.40, 0.45, 0.55)
    p3.draw_line(cx_block + cw_block + 18, cy_block + 65, cx_82 - 2, cy_block + 65, stroke_w=0.6)
    p3.set_fill_color(0.40, 0.45, 0.55)
    p3.draw_text("30m Separation", cx_block + cw_block + 20, cy_block + 70, font="F3", size=6.0)
    
    y = fig1_y - 8
    
    y = p3.draw_section_heading("2.3", "Party Wall Decoupling & Statutory Nuisance Elimination (EPA 1990 s.79)", y)
    p3_nuisance = (
        "Under Section 79 of the Environmental Protection Act 1990, local authorities possess statutory powers to serve abatement "
        "notices upon care homes where noise emissions interfere with the personal comfort of neighbouring occupiers. Autistic residents "
        "frequently vocalise or experience nocturnal meltdowns. Under Scenario B, 78 shares a direct party wall with the Director's family, "
        "while 82 is surrounded by private owners sensitive to care noise. Under Scenario A, 78 and 80 form an integrated block where the party "
        "wall is internal to the business. Flanked by driveways on both sides, care operations are decoupled from external neighbours."
    )
    y = p3.draw_wrapped_text(p3_nuisance, p3.mx, y, p3.cw, font="F1", size=7.2, leading=9.6)
    y -= 6
    
    y = p3.draw_section_heading("2.4", "Environmental Health, Acoustic Isolation & Community Relations Protocol", y)
    p3_acoustics = (
        "To ensure robust acoustic containment, the unified scheme incorporates resilient acoustic mineral wool stud linings along internal "
        "flanking walls and heavy-duty acoustic seals on all fire doors. Luton Borough Council's Environmental Protection Team requires care "
        "facilities in predominantly residential streets to demonstrate noise mitigation. Insulating the care function within the contiguous "
        "78 & 80 envelope establishes an impervious physical boundary, safeguarding community relations and preventing statutory complaints."
    )
    y = p3.draw_wrapped_text(p3_acoustics, p3.mx, y, p3.cw, font="F1", size=7.2, leading=9.6)
    y -= 6
    
    cols_t21 = [("Location / Asset", 110), ("Scenario A (Unified Campus)", 195), ("Scenario B (Split Scheme)", 210)]
    rows_t21 = [
        ("Party Wall 78 / 80", "Internalized within Care Business (Zero Risk)", "Direct Transmission into Director Domestic Residence"),
        ("Flanking Boundaries", "10-meter Buffer via Double Private Driveways", "Direct Proximity to Third-Party Neighbours at 82"),
        ("Statutory Nuisance Risk", "Negligible / Section 79 EPA 1990 Protected", "Severe Risk of Neighbour Objections & Abatement Action")
    ]
    y = p3.draw_booktabs_table("TABLE 2.1: ACOUSTIC & STATUTORY NUISANCE RISK MATRIX", cols_t21, rows_t21, y, row_h=11.5, font_size=6.2)
    y -= 4
    
    p3.draw_academic_callout(
        "STATUTORY NUISANCE SAFEGUARD // SECTION 79 EPA 1990 COMPLIANCE",
        "By internalizing the semi-detached party wall within the commercial envelope of ADOV Care Group, Scenario A legally insulates "
        "the care home against noise abatement orders. In contrast, Scenario B places the Director's young family directly on the receiving "
        "end of nocturnal autistic meltdowns, breaching domestic peace and creating statutory vulnerability.",
        y, h=44
    )
