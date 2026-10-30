with open("generate_luxury_brochure.py", "a") as f:
    f.write('''
    # =========================================================================
    # PAGE 4: CHAPTER 2 - MASTER 4-SECTOR INVESTMENT MATRIX
    # =========================================================================
    p4 = doc.add_page()
    p4.draw_header_banner("2", "MASTER 4-SECTOR STATUTORY INVESTMENT MATRIX", "SECTOR AUDIT")
    
    # Narrative Intro
    p4.set_fill_color(0.20, 0.25, 0.35)
    p4_intro = (
        "To establish rigorous fiduciary and planning justification for FAIRYTALES GROUP, all four primary UK social care sectors "
        "were audited across thirteen critical statutory, operational, and financial metrics specifically calibrated for Marston Gardens."
    )
    p4.draw_wrapped_text(p4_intro, 36, 780, p4.cw, font="F1", size=7.8, leading=10.0)
    
    # 4-Sector Matrix Table
    th_w = [115, 102, 100, 102, 104]
    th_titles = ["Statutory Metric", "1. Child Care (EBD)", "2. Elderly Care (C2)", "3. Mental Health", "4. Autism / LD (C3b)"]
    
    p4.set_fill_color(0.10, 0.16, 0.28)
    p4.draw_rect(36, 735, p4.cw, 20, fill=True)
    p4.set_fill_color(1.0, 1.0, 1.0)
    cur_tx = 36
    for idx, th in enumerate(th_titles):
        p4.draw_text(th, cur_tx + 4, 742, font="F2", size=7.2)
        cur_tx += th_w[idx]
        
    matrix_rows = [
        ("Regulator & Regime", "Ofsted (SCCIF Framework)", "CQC (Care Home C2)", "CQC (Supported Living)", "CQC (Supported Living)"),
        ("Town Planning Class", "Class C2 (Full Planning)", "Class C2 (Full Planning)", "Class C3b / HMO Sui Gen", "Class C3(b) (Immune)"),
        ("Planning Approval Risk", "HIGH (Fierce neighbor veto)", "MEDIUM (Parking/Amenity)", "LOW (S192 CLPUD)", "ZERO (S192 CLPUD)"),
        ("CapEx Fit-Out Budget", "£160,000 - £180,000", "£250k - £300k (Lift fatal)", "£120,000 - £140,000", "£145,000 - £160,000"),
        ("Weekly Tariff per Bed", "£5,000 - £7,500 / week", "£750 - £950 / week", "£1,400 - £1,800 / week", "£2,500 - £2,800 / week"),
        ("Gross Yield (8-Bed)", "£1,800,000 / year (4-bed)", "£332,000 / year (8-bed)", "£640,000 / year (8-bed)", "£1,043,328 / year (8-bed)"),
        ("Frontline Payroll", "£750k/yr (2:1/1:1 ratios)", "£280,000 / year", "£310,000 / year", "£425,000 / year (14 FT)"),
        ("Net Operating EBITDA", "£550k/yr (30.5% margin)", "-£48,000 / yr (LOSS)", "£165,000 / yr (25.8%)", "£408,328 / yr (39.1%)"),
        ("Placement Tenure", "6 - 18 Months (Volatile)", "1 - 3 Years (Palliative)", "3 - 12 Months (Turnover)", "7 - 15+ YEARS (STABLE)"),
        ("Void Frequency Risk", "Medium-High (Referral gap)", "High (Mortality voids)", "High (Relapse/Discharge)", "VIRTUALLY ZERO VOIDS"),
        ("Police / ASB Exposure", "VERY HIGH (Runaways/Crime)", "Zero (Frailty)", "Medium (Relapse crises)", "ZERO (Peaceful routines)"),
        ("Impact on Neighbor 82", "SEVERE (Noise/Siren risk)", "Low (Ambulance visits)", "Medium (Transient footfall)", "ZERO (Ideal quiet living)"),
        ("Strategic Merit Score", "52 / 100 (Disqualified)", "28 / 100 (FATAL LOSS)", "71 / 100 (Secondary)", "98 / 100 (CHAMPION)")
    ]
    
    cur_ty = 718
    for r_idx, r_data in enumerate(matrix_rows):
        bg = (0.95, 0.97, 1.0) if r_idx % 2 == 0 else (1.0, 1.0, 1.0)
        p4.set_fill_color(*bg)
        p4.draw_rect(36, cur_ty - 3, p4.cw, 14, fill=True)
        
        cur_col_x = 36
        for c_idx, val in enumerate(r_data):
            bold = c_idx == 0 or "CHAMPION" in val or "FATAL" in val or "Disqualified" in val or "98" in val
            color = (0.10, 0.15, 0.25)
            if "CHAMPION" in val or "98" in val or "ZERO" in val: color = (0.05, 0.45, 0.15)
            elif "FATAL" in val or "LOSS" in val or "SEVERE" in val: color = (0.70, 0.10, 0.10)
            elif "VERY HIGH" in val or "Disqualified" in val: color = (0.75, 0.35, 0.05)
            
            p4.set_fill_color(*color)
            p4.draw_text(val, cur_col_x + 3, cur_ty + 1, font="F2" if bold else "F1", size=6.5)
            cur_col_x += th_w[c_idx]
        cur_ty -= 14.5
        
    # Analysis & Disqualification Cards
    p4.set_fill_color(0.98, 0.98, 0.99)
    p4.set_stroke_color(0.25, 0.35, 0.55)
    p4.draw_rect(36, 42, p4.cw, 470, fill=True, stroke=True, stroke_w=1.0)
    
    p4.set_fill_color(0.12, 0.22, 0.40)
    p4.draw_rect(36, 488, p4.cw, 24, fill=True)
    p4.set_fill_color(1.0, 1.0, 1.0)
    p4.draw_text("STRATEGIC DEDUCTIONS & DISQUALIFICATION RATIONALES", 46, 495, font="F2", size=8.5)
    
    disq_cards = [
        ("DISQUALIFICATION OF SECTOR 2: ELDERLY CARE (MATHEMATICALLY FATAL AT 8 BEDS)",
         "Operating an elderly residential care home at 78 & 80 Marston Gardens is commercially and physically unviable. Modern elderly care "
         "demands 50-80 beds to amortize 24/7 waking night teams, chefs, and clinical leads. At Luton Council's baseline rate of £800/week, an 8-bed "
         "home yields £332k/year against £380k in fixed staff, utilities, and commercial rent, generating an immediate NET ANNUAL LOSS of -£48,000! "
         "Furthermore, Building Regulations Part M mandates a commercial 8-person passenger lift (£45,000-£55,000), destroying 2 ground-floor rooms. "
         "Conclusion: Elderly care is definitively rejected.", 0.65, 0.15, 0.15),
         
        ("DISQUALIFICATION OF SECTOR 1: CHILD CARE EBD (FATAL PLANNING & POLICE EXPOSURE)",
         "While Child Care (Ages 8-17 Emotional & Behavioural Difficulties) yields high revenue (£5,500/child/week), it is categorically incompatible "
         "with the Marston Gardens residential context. 1) Town Planning: Requires Class C2 full planning permission. In Luton, residential street "
         "applications face intense neighbor petitions regarding antisocial behavior, traffic, and noise, leading to near-certain planning committee refusal. "
         "2) Operational Reality: High-acuity EBD homes experience frequent missing-person episodes (Ofsted notifications), Child Sexual Exploitation "
         "(CSE) risks, and police cruiser attendance at 2:00 AM. Placing this operational chaos directly adjacent to the Director's family home at 82 "
         "creates severe lifestyle degradation and permanent neighborhood hostility. Conclusion: Rejected.", 0.70, 0.35, 0.05),
         
        ("DEFINITIVE VERDICT: AUTISM & COMPLEX LEARNING DISABILITIES (THE UNCHALLENGED MODEL)",
         "Autism & Learning Disabilities PBS Supported Living scores 98/100, outperforming all sectors on every legal, operational, and commercial metric. "
         "1) 100% Lawful planning certainty via Class C3(b) Section 192 CLPUD. 2) Exceptional cashflow: £1,043,328 revenue and £408,328 OpCo EBITDA. "
         "3) Zero void risk: Service users remain for 7 to 15+ years. 4) Domestic tranquility: PBS routines ensure peaceful, respectful community living "
         "that perfectly protects the living environment of the Director residing at 82 Marston Gardens.", 0.10, 0.45, 0.20)
    ]
    cur_dy = 475
    for d_title, d_text, r, g, b in disq_cards:
        p4.set_fill_color(r, g, b)
        p4.draw_text(d_title, 46, cur_dy, font="F2", size=7.8)
        cur_dy -= 10
        p4.set_fill_color(0.18, 0.22, 0.28)
        cur_dy = p4.draw_wrapped_text(d_text, 46, cur_dy, p4.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_dy -= 12


    # =========================================================================
    # PAGE 5: CHAPTER 3 - STATUTORY TOWN PLANNING & SECTION 192 CLPUD
    # =========================================================================
    p5 = doc.add_page()
    p5.draw_header_banner("3", "STATUTORY TOWN PLANNING LAW & S.192 CLPUD", "PLANNING CERTAINTY")
    
    # Legal Foundation Callout
    p5.set_fill_color(0.97, 0.98, 1.0)
    p5.set_stroke_color(0.20, 0.35, 0.60)
    p5.draw_rect(36, 645, p5.cw, 125, fill=True, stroke=True, stroke_w=1.0)
    
    p5.set_fill_color(0.10, 0.20, 0.40)
    p5.draw_rect(36, 745, p5.cw, 25, fill=True)
    p5.set_fill_color(1.0, 1.0, 1.0)
    p5.draw_text("3.1 STATUTORY LEGAL BASIS: TCPA 1990 S.55(2)(f) & USE CLASS C3(b)", 46, 753, font="F2", size=9.0)
    
    p5_law_text = (
        "The Town and Country Planning (Use Classes) Order 1987 (as amended) establishes Use Class C3(b) as: "
        "'Use as a dwellinghouse by not more than six residents living together as a single household where care is provided for residents'. "
        "Furthermore, Section 55(2)(f) of the Town and Country Planning Act 1990 expressly provides that the use of a building or other land within "
        "the same class specified in an order made by the Secretary of State shall NOT be taken for the purposes of this Act to involve development. "
        "Therefore, operating a supported living home for up to 6 residents living together as a single household with 24/7 care does NOT constitute "
        "development and does NOT require planning permission. Compliance is certified via Section 192 Certificate of Lawfulness (CLPUD)."
    )
    p5.set_fill_color(0.15, 0.20, 0.25)
    p5.draw_wrapped_text(p5_law_text, 46, 735, p5.cw - 20, font="F1", size=7.8, leading=10.0)
    
    # Landmark Case Law Precedents Box
    p5.set_fill_color(0.98, 0.98, 0.99)
    p5.set_stroke_color(0.25, 0.35, 0.55)
    p5.draw_rect(36, 385, p5.cw, 250, fill=True, stroke=True, stroke_w=1.0)
    
    p5.set_fill_color(0.12, 0.22, 0.40)
    p5.draw_rect(36, 610, p5.cw, 25, fill=True)
    p5.set_fill_color(1.0, 1.0, 1.0)
    p5.draw_text("3.2 BINDING HIGH COURT CASE LAW PRECEDENTS PROTECTING ADOV CARE GROUP", 46, 618, font="F2", size=9.0)
    
    cases = [
        ("North Devon District Council v First Secretary of State [2004] EWHC 587 (Admin):",
         "The High Court definitively held that children or adults who cannot live independently due to disability, living together with resident "
         "or visiting care staff providing 24-hour supervision and care, constitute a 'single household' within the meaning of Class C3(b). "
         "The presence of non-resident carers operating on rotas does not displace Class C3(b) status, provided the property maintains a domestic character."),
         
        ("Hossack v Kettering Borough Council [2002] EWCA Civ 886:",
         "The Court of Appeal established the 'fact and degree' test, ruling that whether a supported living facility falls within Class C3(b) depends "
         "upon the domestic mode of living. Communal cooking, shared dining, collective lounge areas, and domestic routines establish that the "
         "occupants live together as a single household, distinguishing it completely from institutional use (Class C2)."),
         
        ("Crawley Borough Council v First Secretary of State [2004] EWHC 160 (Admin):",
         "The High Court affirmed that a change of use between classes in the same order, or within Class C3, does not constitute development. "
         "Local planning authorities possess no statutory discretion to refuse a Section 192 Certificate of Lawfulness where the physical domestic "
         "character and number of residents comply with statutory thresholds.")
    ]
    cur_cy = 600
    for c_title, c_text in cases:
        p5.set_fill_color(0.12, 0.25, 0.50)
        p5.draw_text(c_title, 46, cur_cy, font="F2", size=7.5)
        cur_cy -= 10
        p5.set_fill_color(0.18, 0.22, 0.28)
        cur_cy = p5.draw_wrapped_text(c_text, 46, cur_cy, p5.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_cy -= 8
        
    # Section 192 Strategy & Highways Compliance Box
    p5.set_fill_color(0.97, 0.99, 0.97)
    p5.set_stroke_color(0.15, 0.55, 0.25)
    p5.draw_rect(36, 42, p5.cw, 332, fill=True, stroke=True, stroke_w=1.0)
    
    p5.set_fill_color(0.12, 0.45, 0.20)
    p5.draw_rect(36, 350, p5.cw, 24, fill=True)
    p5.set_fill_color(1.0, 1.0, 1.0)
    p5.draw_text("3.3 DUAL S.192 CLPUD SUBMISSION PROTOCOL & HIGHWAYS IMMUNITY", 46, 357, font="F2", size=8.5)
    
    s192_pts = [
        ("The Dual-Application Strategy (Separate Titles):",
         "Because 78 and 80 Marston Gardens sit on separate Land Registry freehold titles, ADOV Care Group will submit TWO INDEPENDENT Section 192 "
         "CLPUD applications concurrently: 1) 78 Marston Gardens for 5 resident service users + visiting care staff. 2) 80 Marston Gardens for 3 resident "
         "service users + visiting care staff. Both properties sit safely below the statutory ceiling of 6 residents, ensuring absolute statutory compliance."),
         
        ("Neighbor Veto & Committee Immunity (Ultra Vires):",
         "Section 192 of the TCPA 1990 is a legal certification of existing rights, NOT a discretionary planning application. Public consultation "
         "is not required by statute. Planning officers cannot evaluate 'need', neighbor objections, or local politics. If an officer purports to refuse "
         "a valid C3(b) CLPUD, it is legally ultra vires, subject to immediate Section 195 appeal with a full award of legal costs against Luton Council."),
         
        ("Luton Local Plan 2011-2031 Policy LLP32 (Highways & Parking):",
         "Under Appendix 2 of the Luton Local Plan, residential care standards require 1 parking space per 4 beds plus 1 per staff member. "
         "The Marston Gardens campus provides 8 full off-street parking spaces (4 on the left driveway of 80, 4 on the right driveway of 78) plus "
         "2 detached rear garages. Maximum daytime staff across both houses is 4-5 carers. Luton Highways cannot raise an objection.")
    ]
    cur_sy = 338
    for s_t, s_d in s192_pts:
        p5.set_fill_color(0.12, 0.45, 0.20)
        p5.draw_text(s_t, 46, cur_sy, font="F2", size=7.5)
        cur_sy -= 10
        p5.set_fill_color(0.18, 0.22, 0.28)
        cur_sy = p5.draw_wrapped_text(s_d, 46, cur_sy, p5.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_sy -= 7

    print("Added Page 4 and Page 5.")
''')

print("append_brochure_p4_p5 written.")
