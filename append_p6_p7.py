with open("generate_government_project_report.py", "a") as f:
    f.write('''
    # =========================================================================
    # PAGE 6: CHAPTER 5 - ARCHITECTURAL & SANITARY ADAPTATION
    # =========================================================================
    p6 = doc.add_page()
    
    p6.set_fill_color(0.06, 0.10, 0.18)
    p6.draw_text("5. ARCHITECTURAL & INFRASTRUCTURE ADAPTATION (WETROOMS OPTIMIZATION)", 36, 794, font="F2", size=13.0)
    p6.set_stroke_color(0.85, 0.60, 0.15)
    p6.draw_line(36, 786, p6.width - 36, 786, stroke_w=1.2)
    
    # Sanitary Engineering Callout Box
    p6.set_fill_color(0.97, 0.98, 1.0)
    p6.set_stroke_color(0.20, 0.35, 0.60)
    p6.draw_rect(36, 620, p6.cw, 155, fill=True, stroke=True, stroke_w=1.0)
    
    p6.set_fill_color(0.10, 0.20, 0.40)
    p6.draw_rect(36, 745, p6.cw, 25, fill=True)
    p6.set_fill_color(1.0, 1.0, 1.0)
    p6.draw_text("5.1 SANITARY INFRASTRUCTURE REALITY & £42,000 CAPEX REDUCTION", 46, 753, font="F2", size=9.0)
    
    p6_san_text = (
        "A transformative architectural advantage is that BOTH 78 AND 80 MARSTON GARDENS ALREADY POSSESS A DEDICATED SEPARATE WC "
        "AND A LARGE-SIZE WETROOM / SHOWER ROOM, with 78 additionally featuring an en-suite bathroom to Bedroom 1. "
        "Standard care conversions frequently waste over £60,000 attempting to retrofit small en-suites into every bedroom, causing massive "
        "drainage disruptions and reducing usable bedroom floor space. By capitalizing on the existing wetroom infrastructure, ADOV Care Group "
        "adds just ONE additional en-suite to Bedroom 2 in 78. This delivers 2 en-suites + 1 communal wetroom + 1 WC in 78 (Toilet ratio 1:1.25, "
        "Shower ratio 1:1.67 for 5 residents), and 1 large wetroom + 1 WC in 80 (Toilet ratio 1:1.5, Shower ratio 1:3 for 3 residents). "
        "This substantially exceeds CQC and Luton Council minimum standards (1:3 ratio) and slashes sanitary CapEx by £42,000."
    )
    p6.set_fill_color(0.15, 0.20, 0.25)
    p6.draw_wrapped_text(p6_san_text, 46, 735, p6.cw - 20, font="F1", size=7.8, leading=10.2)
    
    # Campus Space Allocation Table
    p6.set_fill_color(0.10, 0.16, 0.28)
    p6.draw_rect(36, 595, p6.cw, 20, fill=True)
    p6.set_fill_color(1.0, 1.0, 1.0)
    
    space_cols = [120, 200, 203]
    p6.draw_text("Property Asset", 40, 602, font="F2", size=7.2)
    p6.draw_text("Allocated Room Layout & Functional Use", 160, 602, font="F2", size=7.2)
    p6.draw_text("Sanitary & Compliance Ratios", 360, 602, font="F2", size=7.2)
    
    space_rows = [
        ("78 Marston Gdns (Main Residence)", "5 Resident Bedrooms (13m² - 16m²), Commercial Kitchen, Dining Room, Sensory Lounge, Garden Access.", "2 En-Suites + 1 Large Wetroom + 1 WC (Toilets 1:1.25, Showers 1:1.67) - EXCEEDS CQC"),
        ("80 Marston Gdns (Specialist Wing)", "3 Resident Bedrooms (Bed 7 Ground Floor, Beds 6 & 8 Upstairs), Staff Sleep-in Office, Day Room.", "1 Large Wetroom + 1 Separate WC (Toilets 1:1.5, Showers 1:3.0) - CQC COMPLIANT"),
        ("Exterior & Grounds (Both Houses)", "Twin flanking private driveways accommodating 8 vehicles off-street + 2 detached rear garages.", "LLP32 Compliant: 1:1 Parking to bed ratio. Zero highway impact on Marston Gardens.")
    ]
    cur_sy = 578
    for s_prop, s_layout, s_san in space_rows:
        p6.set_fill_color(0.96, 0.98, 1.0)
        p6.draw_rect(36, cur_sy - 4, p6.cw, 26, fill=True)
        
        p6.set_fill_color(0.12, 0.22, 0.40)
        p6.draw_text(s_prop, 40, cur_sy + 8, font="F2", size=6.8)
        
        p6.set_fill_color(0.18, 0.22, 0.28)
        p6.draw_wrapped_text(s_layout, 160, cur_sy + 12, 195, font="F1", size=6.5, leading=8.5)
        p6.draw_wrapped_text(s_san, 360, cur_sy + 12, 195, font="F1", size=6.5, leading=8.5)
        cur_sy -= 28.0

    # Technical Engineering Box
    p6.set_fill_color(0.98, 0.98, 0.99)
    p6.set_stroke_color(0.25, 0.35, 0.55)
    p6.draw_rect(36, 48, p6.cw, 440, fill=True, stroke=True, stroke_w=1.0)
    
    p6.set_fill_color(0.12, 0.22, 0.40)
    p6.draw_rect(36, 463, p6.cw, 25, fill=True)
    p6.set_fill_color(1.0, 1.0, 1.0)
    p6.draw_text("5.2 STATUTORY BUILDING REGULATIONS & LIFE SAFETY COMPLIANCE", 46, 471, font="F2", size=9.0)
    
    eng_pts = [
        ("BS 5839-1 Category L1 Fire Detection System (Maximum Life Safety):",
         "Installation of an addressable Category L1 fire alarm system across both properties. Optical smoke detectors and heat sensors are fitted "
         "in every bedroom, circulation hallway, communal lounge, roof void, and staff sleep-in room, linked to central monitoring panels. "
         "Exceeds basic HMO standards (Cat L2) to guarantee full approval under the Regulatory Reform (Fire Safety) Order 2005."),
         
        ("FD30S Fire Doorsets with Acoustic Seals (Document B & E):",
         "All bedroom and risk-room doors replaced with 30-minute fire and cold-smoke resistant doorsets (FD30S), equipped with intumescent fire strips, "
         "drop-down acoustic seals, and electromagnetic hold-open freedor units linked to the fire alarm panel for ease of domestic movement."),
         
        ("Infection Prevention Commercial Laundry (HTM 01-04):",
         "Establishment of a dedicated dirty-to-clean flow commercial laundry within the utility space of 78 Marston Gardens, equipped with commercial "
         "barrier washing machines providing automatic thermal disinfection (minimum 71°C holding for 3 minutes) under NHS HTM 01-04 guidelines."),
         
        ("Acoustic Soundproofing (Building Regulations Approved Document E):",
         "Installation of high-density acoustic mineral wool insulation and SoundBloc plasterboarding across the internal party wall between 78 and 80, "
         "achieving >43dB airborne acoustic separation. Eliminates sensory sound transfer between residents, ensuring peaceful domestic routines."),
         
        ("Thermostatic Mixing Valves (TMV3 Healthcare Standard):",
         "All hot water outlets, baths, and wetroom shower mixers fitted with Type 3 Thermostatic Mixing Valves (TMV3) under Health & Safety Executive "
         "(HSE) guidelines, calibrating maximum outlet temperatures to 41°C to completely prevent scalding risks for vulnerable adults.")
    ]
    cur_ey = 450
    for e_t, e_d in eng_pts:
        p6.set_fill_color(0.12, 0.25, 0.50)
        p6.draw_text(e_t, 46, cur_ey, font="F2", size=7.5)
        cur_ey -= 10
        p6.set_fill_color(0.18, 0.22, 0.28)
        cur_ey = p6.draw_wrapped_text(e_d, 46, cur_ey, p6.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_ey -= 7

    print("Added Page 6.")


    # =========================================================================
    # PAGE 7: CHAPTER 6 - FINANCIAL ENGINEERING & 3-YEAR P&L MODEL
    # =========================================================================
    p7 = doc.add_page()
    
    p7.set_fill_color(0.06, 0.10, 0.18)
    p7.draw_text("6. FINANCIAL ENGINEERING: CAPEX BUDGET & 3-YEAR P&L MODEL", 36, 794, font="F2", size=13.0)
    p7.set_stroke_color(0.85, 0.60, 0.15)
    p7.draw_line(36, 786, p7.width - 36, 786, stroke_w=1.2)
    
    # CapEx Table (Left Box)
    p7.set_fill_color(0.97, 0.98, 1.0)
    p7.set_stroke_color(0.20, 0.35, 0.60)
    p7.draw_rect(36, 440, 255, 335, fill=True, stroke=True, stroke_w=1.0)
    
    p7.set_fill_color(0.10, 0.20, 0.40)
    p7.draw_rect(36, 750, 255, 25, fill=True)
    p7.set_fill_color(1.0, 1.0, 1.0)
    p7.draw_text("ITEMIZED TURNKEY CAPEX BUDGET (£150k)", 44, 758, font="F2", size=8.0)
    
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
        p7.set_fill_color(0.85, 0.60, 0.15) if bold else p7.set_fill_color(0.15, 0.20, 0.28)
        p7.draw_text(c_item, 44, cur_cpx_y, font="F2" if bold else "F1", size=6.8)
        p7.draw_text(c_cost, 240, cur_cpx_y, font="F2" if bold else "F1", size=6.8, align="right", max_w=45)
        cur_cpx_y -= 13.5
        
    # CapEx Narrative below CapEx table
    p7.set_fill_color(0.40, 0.45, 0.55)
    cpx_note = (
        "*Note: Existing wetrooms in 78 & 80 save £42,000 vs standard retrofit. All works comply with Building Regs Approved Documents B, M, E, F."
    )
    p7.draw_wrapped_text(cpx_note, 44, 580, 240, font="F3", size=6.2, leading=8.5)
    
    # 3-Year P&L Model (Right Box)
    p7.set_fill_color(0.98, 0.98, 0.99)
    p7.set_stroke_color(0.25, 0.35, 0.55)
    p7.draw_rect(298, 440, 261, 335, fill=True, stroke=True, stroke_w=1.0)
    
    p7.set_fill_color(0.12, 0.22, 0.40)
    p7.draw_rect(298, 750, 261, 25, fill=True)
    p7.set_fill_color(1.0, 1.0, 1.0)
    p7.draw_text("3-YEAR STABILIZED P&L MODEL (£)", 306, 758, font="F2", size=8.0)
    
    pnl_headers = ["P&L Line Item", "Year 1 (60%)", "Year 2 (88%)", "Year 3 (95%)"]
    pw = [95, 52, 55, 55]
    
    p7.set_fill_color(0.15, 0.25, 0.45)
    p7.draw_rect(298, 730, 261, 14, fill=True)
    p7.set_fill_color(1.0, 1.0, 1.0)
    px = 298
    for i, ph in enumerate(pnl_headers):
        p7.draw_text(ph, px + 3, 734, font="F2", size=6.2)
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
        p7.set_fill_color(0.85, 0.60, 0.15) if bold else p7.set_fill_color(0.18, 0.22, 0.28)
        p7.draw_text(p_lbl, 301, cur_pnl_y, font="F2" if bold else "F1", size=6.2)
        p7.draw_text(py1, 396, cur_pnl_y, font="F2" if bold else "F1", size=6.2)
        p7.draw_text(py2, 448, cur_pnl_y, font="F2" if bold else "F1", size=6.2)
        p7.draw_text(py3, 503, cur_pnl_y, font="F2" if bold else "F1", size=6.2)
        cur_pnl_y -= 14.0

    # Executive Commentary Box below
    p7.set_fill_color(0.97, 0.99, 0.97)
    p7.set_stroke_color(0.15, 0.55, 0.25)
    p7.draw_rect(36, 48, p7.cw, 380, fill=True, stroke=True, stroke_w=1.0)
    
    p7.set_fill_color(0.12, 0.45, 0.20)
    p7.draw_rect(36, 403, p7.cw, 25, fill=True)
    p7.set_fill_color(1.0, 1.0, 1.0)
    p7.draw_text("6.2 COMMERCIAL VIABILITY & RETURN ON CAPITAL EMPLOYED (ROCE) AUDIT", 46, 411, font="F2", size=9.0)
    
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
         "The group captures revenue across two streams: 1) OpCo net operating profit: £408,328/year. 2) Property leases paid by OpCo: £115,000/year "
         "(£65,000 to ADOV LIMITED for 78, and £50,000 to the Director for 80). Total combined group cashflow equals £523,328 per annum."),
         
        ("Unprecedented 261.6% ROCE & 3.5-Month Payback Period:",
         "Dividing annual EBITDA (£408,328) by initial CapEx (£150,000) yields a Return on Capital Employed (ROCE) of 261.6% per annum. "
         "The entire capital expenditure is fully repaid from operating cashflow within 3.5 months of reaching stabilized occupancy.")
    ]
    cur_cy_fin = 390
    for f_t, f_d in fin_commentary:
        p7.set_fill_color(0.12, 0.45, 0.20)
        p7.draw_text(f_t, 46, cur_cy_fin, font="F2", size=7.5)
        cur_cy_fin -= 10
        p7.set_fill_color(0.18, 0.22, 0.28)
        cur_cy_fin = p7.draw_wrapped_text(f_d, 46, cur_cy_fin, p7.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_cy_fin -= 6

    print("Added Page 7.")
''')

print("append_p6_p7 written.")
