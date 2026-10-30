
def add_p1_p2(pdf):
    # --------------------------------------------------------------------------
    # PAGE 1: COVER & WORKING PAPER ABSTRACT (OXFORD/CAMBRIDGE STYLE)
    # --------------------------------------------------------------------------
    p1 = pdf.add_page(is_cover=True)
    
    p1.set_stroke_color(0.08, 0.14, 0.24)
    p1.draw_line(p1.mx, p1.height - 34, p1.width - p1.mx, p1.height - 34, stroke_w=1.2)
    p1.draw_line(p1.mx, p1.height - 38, p1.width - p1.mx, p1.height - 38, stroke_w=0.5)
    
    p1.set_fill_color(0.40, 0.45, 0.55)
    p1.draw_text("WORKING PAPER SERIES IN HEALTH ECONOMICS & ASSET STRATEGY // MONOGRAPH NO. 2026-MG-04", p1.mx, p1.height - 49, font="F2", size=7.0)
    p1.draw_text("OCTOBER 2026 // DEFINITIVE COMMISSION APPRAISAL", p1.width - p1.mx, p1.height - 49, font="F1", size=6.8, align="right", max_w=220)
    
    p1.set_fill_color(0.08, 0.14, 0.24)
    p1.draw_text("STRATEGIC CAMPUS LOCATION & OPERATIONAL APPRAISAL", p1.mx, p1.height - 74, font="F2", size=15.0)
    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_text("Head-to-Head Feasibility: Unified Campus (78 & 80) vs. Disconnected Properties (78 & 82)", p1.mx, p1.height - 89, font="F2", size=9.4)
    p1.set_fill_color(0.35, 0.42, 0.52)
    p1.draw_text("A Forensic Multi-Dimensional Evaluation across Workforce Rotas, Planning Law, CapEx, HMRC Tax & Family Living", p1.mx, p1.height - 102, font="F3", size=7.6)
    
    p1.set_stroke_color(0.75, 0.80, 0.88)
    p1.draw_line(p1.mx, p1.height - 109, p1.width - p1.mx, p1.height - 109, stroke_w=0.6)
    
    p1.set_fill_color(0.08, 0.14, 0.24)
    p1.draw_text("INSTITUTIONAL METADATA & STATUTORY GOVERNANCE FRAMEWORK", p1.mx, p1.height - 120, font="F2", size=7.2)
    
    meta_rows = [
        ("Lead Project Author:", "Project Planned by AbdullahMamun.com (Strategic Advisory Lead)"),
        ("Commissioning Holding Entity:", "FAIRYTALES GROUP (Trading Name of Mamun Limited)"),
        ("Asset Holding & OpCo Entities:", "ADOV LIMITED (Freehold Asset Co) & ADOV Care Group LIMITED (Regulated OpCo)"),
        ("Statutory Planning Framework:", "Town & Country Planning (Use Classes) Order 1987 (Class C3b / C2) // Luton Local Plan LLP32"),
        ("Regulated Quality Standards:", "Health and Social Care Act 2008 (Regulated Activities) Regulations 2014 (Reg 12, 15, 18)")
    ]
    cur_ay = p1.height - 130
    for l_txt, v_txt in meta_rows:
        p1.set_fill_color(0.40, 0.45, 0.55)
        p1.draw_text(l_txt, p1.mx, cur_ay, font="F2", size=6.4)
        p1.set_fill_color(0.12, 0.16, 0.24)
        p1.draw_text(v_txt, p1.mx + 140, cur_ay, font="F1", size=6.4)
        cur_ay -= 9.6
        
    p1.set_stroke_color(0.75, 0.80, 0.88)
    p1.draw_line(p1.mx, cur_ay + 1, p1.width - p1.mx, cur_ay + 1, stroke_w=0.6)
    cur_ay -= 7
    
    p1.set_fill_color(0.08, 0.14, 0.24)
    p1.draw_text("EXECUTIVE ABSTRACT & STATUTORY COMMISSION MANDATE", p1.mx, cur_ay, font="F2", size=7.5)
    cur_ay -= 8
    
    p1_abstract_1 = (
        "This academic working paper delivers a forensic operational, spatial, and financial appraisal commissioned by the Board of "
        "Directors of FAIRYTALES GROUP to determine the definitive campus deployment for an 8-bed high-dependency residential supported living "
        "facility for adults presenting with severe autism and complex challenging behaviours. The appraisal conducts a rigorous head-to-head "
        "evaluation between two mutually exclusive configurations on Marston Gardens, Luton: Scenario A (unifying contiguous semi-detached "
        "properties 78 & 80 into a single 8-bed operational campus, relocating the founding Director to modern detached 82) versus Scenario B "
        "(operating disconnected facilities across 78 and detached 82, leaving the Director residing at 80)."
    )
    cur_ay = p1.draw_wrapped_text(p1_abstract_1, p1.mx, cur_ay, p1.cw, font="F1", size=6.8, leading=8.6)
    cur_ay -= 3
    
    p1_abstract_2 = (
        "Utilizing statutory health economics methodologies, empirical night rota workforce modeling under CQC Regulation 18, and HMRC tax "
        "jurisprudence (ITEPA 2003 ss.105-106), this monograph establishes that Scenario A represents the only legally compliant, operationally "
        "viable, and commercially resilient configuration. Scenario B induces structural night rota duplication (£70,200/year deadweight loss), "
        "exposes the Director's family to severe acoustic nuisance under Section 79 EPA 1990, and destroys £32,000/year in tax-neutral director living allowance."
    )
    cur_ay = p1.draw_wrapped_text(p1_abstract_2, p1.mx, cur_ay, p1.cw, font="F1", size=6.8, leading=8.6)
    cur_ay -= 4
    
    t1_cols = [("Performance Indicator / Dimension", 165), ("Scenario A: Campus (78 & 80)", 175), ("Scenario B: Split (78 & 82)", 175)]
    t1_rows = [
        ("Specialist Bed Capacity", "8 High-Dependency Autism Beds", "8 Disconnected Beds (5 at 78 + 3 at 82)"),
        ("Spatial Contiguity & Party Wall", "Contiguous Pair // 100% Internal Party Wall", "Disconnected Across Public Street // External Party Wall"),
        ("Night Staffing Model (CQC Reg 18)", "Unified Hub: 1 Waking Night + 1 Sleep-in", "Duplicate Rotas: 2 Waking Nights + 2 Sleep-ins"),
        ("Annual Waking Night Payroll", "£140,400 / year (Optimized)", "£210,600 / year (+£70,200 Deadweight Penalty)"),
        ("CapEx Conversion Budget", "£143,000 (80 already has DDA Wetroom)", "£230,000 (+£87,000 CapEx Destruction)"),
        ("HMRC AST Rent Arbitrage (ITEPA 03)", "£0 BIK // +£32,000/year Surplus Cash", "£0 Rent Surplus // Family Entangled at 80"),
        ("Year 1 Net EBITDA", "£265,000 (31.8% EBITDA Margin)", "£187,000 (22.5% EBITDA Margin // -£78k Delta)"),
        ("3-Year Cumulative EBITDA", "£1,254,000 (Highly Resilient)", "£1,020,000 (-£234,000 Cumulative Cash Drain)"),
        ("Breakeven Occupancy Threshold", "48.2% (3.8 Resident Beds)", "68.4% (5.5 Resident Beds // High Risk)"),
        ("Statutory Nuisance Risk (EPA 1990)", "Zero / Complete Commercial Insulation", "Severe / Direct Party Wall Noise Intrusion")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.0: CORE EMPIRICAL PERFORMANCE INDICATORS (HEAD-TO-HEAD SYNTHESIS)", t1_cols, t1_rows, cur_ay, row_h=9.8, font_size=5.8)
    cur_ay -= 2
    
    p1_rec_box = (
        "DEFINITIVE STRATEGIC DETERMINATION: The Board of Directors of FAIRYTALES GROUP unanimously adopts SCENARIO A. "
        "Operating 78 & 80 as a contiguous 8-bed campus captures an immediate £87,000 CapEx saving, eliminates £70,200/year in duplicate night staff "
        "wages, secures statutory immunity against Section 79 EPA 1990 noise abatement notices, and unlocks £32,000/year in tax-free family cash surplus."
    )
    cur_ay = p1.draw_academic_callout("STRATEGIC DIRECTIVE // FAIRYTALES GROUP BOARD OF DIRECTORS", p1_rec_box, cur_ay, h=36)
    cur_ay -= 2
    
    t11_cols = [("Governance Discipline", 130), ("Assurance Standard", 195), ("Attestation Status", 190)]
    t11_rows = [
        ("Health Economics & Strategy", "Multi-Dimensional Head-to-Head Feasibility Model", "Project Planned by AbdullahMamun.com"),
        ("Statutory Town Planning", "Town & Country Planning Class C3b / CLEUD s.192", "Certified Lawful Permitted Development"),
        ("Regulated Quality & Rotas", "Health & Social Care Act 2008 Regulated Activities Reg 18", "CQC Single Registered Scheme Model"),
        ("HMRC Property & Tax Law", "ITEPA 2003 ss.105-106 // CTA 2009 s.54 Deductibility", "Tax-Neutral Arm's Length AST Approved")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.1: MULTI-DISCIPLINARY APPRAISAL ASSURANCE PANEL", t11_cols, t11_rows, cur_ay, row_h=9.5, font_size=5.6)
    cur_ay -= 2
    
    t12_cols = [("Statutory Enactment / Instrument", 145), ("Legal Subject Matter", 185), ("Regulatory Compliance Mandate", 185)]
    t12_rows = [
        ("Health & Social Care Act 2008 Reg 18", "Staffing Sufficiency & Competence", "Mandatory active waking night cover without lone-worker isolation"),
        ("Town & Country Planning Order Class C3b", "Permitted Residential Care Use", "Up to 6 residents living together as single household with care"),
        ("Environmental Protection Act 1990 s.79", "Statutory Noise Nuisance Control", "Prevention of nocturnal noise transmission across residential party walls"),
        ("ITEPA 2003 Sections 105 & 106", "Living Accommodation BIK Neutrality", "Open-market AST rent paid by Director eliminates taxable BIK to £0"),
        ("Corporation Tax Act 2009 Section 54", "Commercial Lease Rent Deductibility", "100% tax deductibility of £50k commercial lease paid by Care OpCo")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.2: STATUTORY CODIFICATION & ENABLING LEGAL INSTRUMENTS", t12_cols, t12_rows, cur_ay, row_h=9.5, font_size=5.6)
    cur_ay -= 2
    
    t13_cols = [("Document Control Element", 130), ("Operational Parameter", 195), ("Attestation Certification", 190)]
    t13_rows = [
        ("Monograph Version & Status", "Version 2.4 (Definitive Master Pack)", "Print-Ready Scholarly University Edition"),
        ("Security & Disclosure Classification", "COMMERCIAL-IN-CONFIDENCE // STRICTLY PRIVATE", "Board of Directors Fairytales Group Only"),
        ("Statutory Legal Jurisdiction", "England & Wales (Luton Borough Council)", "DHSC, CQC, UK Planning Inspectorate, HMRC"),
        ("Definitive Implementation Mandate", "Execute Scenario A Unanimous Resolution", "Immediate Transition to Commercial Leases & AST")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.3: MONOGRAPH GOVERNANCE & FORMAL ATTESTATION REGISTER", t13_cols, t13_rows, cur_ay, row_h=9.4, font_size=5.6)
    
    p1.set_stroke_color(0.75, 0.80, 0.88)
    p1.draw_line(p1.mx, cur_ay - 2, p1.width - p1.mx, cur_ay - 2, stroke_w=0.6)
    p1.set_fill_color(0.40, 0.45, 0.55)
    p1.draw_text("Project Planned by AbdullahMamun.com  |  FAIRYTALES GROUP  |  ADOV LIMITED  |  Print-Ready Academic Monograph", p1.mx, cur_ay - 11, font="F1", size=6.2)


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
    y = p2.draw_wrapped_text(p2_txt1, p2.mx, y, p2.cw, font="F1", size=6.9, leading=8.9)
    y -= 4
    
    y = p2.draw_section_heading("1.1", "The Core Operational Dilemma: Unified Campus vs. Disconnected Sites", y)
    p2_txt2 = (
        "Currently, the founding Director and their family reside in 80 Marston Gardens, an extended 3-bedroom property with extensive "
        "ground-floor living space, a commercial-size wetroom, and an independent driveway. Directly adjoining 80 is 78 Marston Gardens, "
        "a 5-bedroom property configured for care operations. Crucially, 78 and 80 form a contiguous semi-detached building block flanked on both "
        "sides by wide 4-car private driveways, completely insulated from any attached residential neighbours. Located 30 meters down the street "
        "is 82 Marston Gardens, a detached 4-bedroom house. The Board faces two mutually exclusive options:\\n\\n"
        "• SCENARIO A (The Unified 8-Bed Specialist Campus): Unify 78 and 80 Marston Gardens under 10-year commercial leases to ADOV Care Group "
        "LIMITED to operate as an integrated 8-bed supported living scheme. The Director relocates their family residence to 82 Marston Gardens "
        "under an open-market Assured Shorthold Tenancy (AST at £1,500/month).\\n\\n"
        "• SCENARIO B (The Disconnected Properties Model): Commission 78 Marston Gardens as a 5-bed care facility and convert 82 Marston Gardens "
        "into a 3-bed care facility down the street. The Director's family remains residing at 80 Marston Gardens, sharing a party wall with 78."
    )
    y = p2.draw_wrapped_text(p2_txt2, p2.mx, y, p2.cw, font="F1", size=6.8, leading=8.7)
    y -= 4
    
    y = p2.draw_section_heading("1.2", "Statutory & Economic Imperatives in Complex Autism Commissioning", y)
    p2_txt12 = (
        "Commissioners from NHS Integrated Care Boards (ICBs) and Bedfordshire Local Authorities evaluate supported living schemes against "
        "exacting regulatory metrics under the Building the Right Support national guidance. Placements commanding £3,000 to £3,500 weekly "
        "tariffs demand dedicated sensory de-escalation environments, robust single-point management oversight, and bulletproof staffing "
        "continuity. Fragmenting 8 beds across disconnected residential addresses introduces operational instability that jeopardises ICB placement approvals."
    )
    y = p2.draw_wrapped_text(p2_txt12, p2.mx, y, p2.cw, font="F1", size=6.8, leading=8.7)
    y -= 4
    
    y = p2.draw_section_heading("2.0", "ASSET TOPOLOGY & SPATIAL CONFIGURATION", y)
    p2_txt3 = (
        "The physical property cluster on Marston Gardens presents distinct architectural characteristics. Numbers 78 and 80 were "
        "constructed together as a pair of substantial semi-detached residences. Both properties have been extensively modernized and extended, "
        "incorporating wide private driveways on their outer flanks. Together, they create a standalone architectural footprint. "
        "Number 82 is a detached, modern executive family residence set in private domestic grounds with a dedicated garden."
    )
    y = p2.draw_wrapped_text(p2_txt3, p2.mx, y, p2.cw, font="F1", size=6.8, leading=8.7)
    y -= 4
    
    cols_t2 = [("Property", 85), ("Structural Baseline", 110), ("Specialist Bedrooms", 85), ("Sanitary / Wetrooms", 115), ("Parking / Garages", 120)]
    rows_t2 = [
        ("78 Marston Gdns", "Extended Semi-Detached", "5 Resident Bedrooms", "1 Wetroom, 1 En-suite, 1 WC", "4-Car Driveway + Rear Garage"),
        ("80 Marston Gdns", "Extended Semi-Detached", "3 Resident Bedrooms", "1 Large Wetroom, 1 WC, 1 En-suite", "4-Car Driveway + Rear Garage"),
        ("82 Marston Gdns", "Modern Detached House", "4 Domestic Bedrooms", "1 Family Bath, 1 En-suite, 1 WC", "1-2 Off-Street Driveway Spaces")
    ]
    y = p2.draw_booktabs_table("TABLE 2.0: PHYSICAL ASSET ATTRIBUTES & STRUCTURAL BASELINE", cols_t2, rows_t2, y, row_h=10.0, font_size=5.8)
    y -= 3
    
    y = p2.draw_section_heading("2.1", "Site Boundary, Curtilage & Parking Infrastructure (Luton Local Plan LLP32)", y)
    p2_curtilage = (
        "A critical asset advantage of 78 & 80 Marston Gardens is the substantial curtilage and private off-street parking capacity. "
        "Each property features an independent, hard-standing private driveway accommodating 4 vehicles, delivering a combined capacity of "
        "8 off-street spaces, supplemented by two detached brick-built garages at the rear. Under Luton Local Plan 2011-2031 Policy LLP32, "
        "commercial care operations must demonstrate adequate parking to prevent on-street congestion. Unifying 78 & 80 provides complete on-site "
        "absorption of shift changeovers, multidisciplinary team (MDT) visits, and emergency vehicles, securing total highway compliance."
    )
    y = p2.draw_wrapped_text(p2_curtilage, p2.mx, y, p2.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    cols_t21 = [("Campus Wing / Room", 120), ("Internal Floor Area", 100), ("Specialist Adaptation Features", 175), ("Statutory Care Standard", 120)]
    rows_t21 = [
        ("78 Ground Floor Communal", "42.5 sq m (Kitchen/Dining)", "Commercial anti-ligature appliances, HTM 01-04 laundry", "CQC Regulation 15 (Premises)"),
        ("78 First Floor Bedrooms", "5 Bedrooms (12-16 sq m)", "En-suite wetrooms, acoustic insulation, Cat L1 alarms", "Building the Right Support DDA"),
        ("80 Ground Floor Therapy", "38.0 sq m (Sensory Suite)", "Sensory calming pods, DDA tracking hoist, wetroom", "NHS Complex Autism Guidance"),
        ("80 First Floor Bedrooms", "3 Bedrooms (14-18 sq m)", "Spacious independent living, soundproof party wall", "CQC Regulation 12 (Safe Care)"),
        ("80 Staff Sleep-in / Office", "16.5 sq m (Dedicated Hub)", "Unified Cat L1 repeater panel, CCTV, secure records", "CQC Regulation 18 (Staffing)")
    ]
    y = p2.draw_booktabs_table("TABLE 2.1: SPATIAL ACCOMMODATION & ADAPTATION SCHEDULE", cols_t21, rows_t21, y, row_h=9.6, font_size=5.6)
    y -= 3
    
    cols_t22 = [("External Curtilage Feature", 120), ("Dimensions / Capacity", 100), ("Operational Specification", 175), ("Statutory Safeguard", 120)]
    rows_t22 = [
        ("Combined Driveways", "8 Vehicles (4 at 78 + 4 at 80)", "Tarmac hard-standing with EV charging provisions", "Luton Local Plan LLP32 Compliant"),
        ("Rear Therapeutic Gardens", "250 sq m Enclosed Grounds", "Level lawn, sensory sensory planting, acoustic fencing", "CQC Regulation 15 (Safe Outdoor)"),
        ("Detached Garages", "2 Detached Brick Garages", "Secure dry archives, clinical consumables, maintenance storage", "HTM 07-01 Waste Regulations"),
        ("Perimeter Fencing", "2.1m Acoustic Timber Fence", "Sound attenuation, anti-climb profile, discrete locks", "Section 79 EPA 1990 Mitigation")
    ]
    y = p2.draw_booktabs_table("TABLE 2.2: THERAPEUTIC OUTDOOR & CURTILAGE SPECIFICATION MATRIX", cols_t22, rows_t22, y, row_h=9.6, font_size=5.6)
    y -= 3
    
    cols_t23 = [("Accessibility Feature", 130), ("Engineering Baseline", 185), ("Operational Impact", 200)]
    rows_t23 = [
        ("Level Access Ingress", "100% Step-free ground floor", "Permits wheelchair and mobility equipment ingress across wings"),
        ("Specialist Wetroom", "Pre-installed commercial DDA wetroom in 80", "Eliminates £35,000 in upfront plumbing and excavation expenditure"),
        ("Circadian LED Lighting", "Tunable flicker-free 2700K-6500K LED", "Reduces sensory overload and nocturnal agitation in autistic adults"),
        ("Acoustic Stud Wall Lining", "Rockwool RW3 dense acoustic insulation", "Decouples resident bedrooms, meeting 55dB sound reduction target")
    ]
    y = p2.draw_booktabs_table("TABLE 2.3: DDA ACCESSIBILITY & SENSORY ENVIRONMENT COMPLIANCE", cols_t23, rows_t23, y, row_h=9.6, font_size=5.6)
    y -= 2
    
    y = p2.draw_section_heading("2.2", "Topological Synthesis: Structural Decoupling from Adjoining Neighbours", y)
    p2_topo_concl = (
        "In synthesis, 78 and 80 Marston Gardens represent an exceptional topological configuration. As a self-contained semi-detached "
        "pair bounded entirely by wide driveways, the care home curtilage does not share a party wall with any third-party private resident. "
        "Unifying both properties internalizes all acoustic transmission within the business, completely protecting adjoining home owners."
    )
    y = p2.draw_wrapped_text(p2_topo_concl, p2.mx, y, p2.cw, font="F1", size=6.8, leading=8.7)
    y -= 2
    
    p2.draw_academic_callout(
        "TOPOLOGICAL TAKEAWAY // INTERNALISATION OF PARTY WALL BOUNDARIES",
        "78 and 80 Marston Gardens form an entirely self-contained residential island. Unifying them internalizes all acoustic and party "
        "wall friction within ADOV Care Group curtilage, eliminating statutory nuisance risk under Section 79 Environmental Protection Act 1990.",
        y, h=36
    )
