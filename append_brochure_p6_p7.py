with open("generate_luxury_brochure.py", "a") as f:
    f.write('''
    # =========================================================================
    # PAGE 6: CHAPTER 4 - CORPORATE GOVERNANCE & TAX RENT-SWAP
    # =========================================================================
    p6 = doc.add_page()
    p6.draw_header_banner("4", "CORPORATE GOVERNANCE, LEASES & TAX RENT-SWAP", "FAIRYTALES GROUP")
    
    # Group Structure Overview Box
    p6.set_fill_color(0.97, 0.98, 1.0)
    p6.set_stroke_color(0.20, 0.35, 0.60)
    p6.draw_rect(36, 645, p6.cw, 125, fill=True, stroke=True, stroke_w=1.0)
    
    p6.set_fill_color(0.10, 0.20, 0.40)
    p6.draw_rect(36, 745, p6.cw, 25, fill=True)
    p6.set_fill_color(1.0, 1.0, 1.0)
    p6.draw_text("4.1 THREE-TIER CORPORATE GOVERNANCE: HOLDCO, PROPCO & OPCO", 46, 753, font="F2", size=9.0)
    
    p6_corp_text = (
        "To achieve complete commercial asset protection, statutory CQC compliance, and maximum tax efficiency, the enterprise operates "
        "under a tripartite structure: 1) FAIRYTALES GROUP (Trading Name of Mamun Limited / Group Holding Company / HoldCo): 100% parent entity, "
        "retaining retained earnings and controlling strategic group assets. 2) ADOV LIMITED (Property Holding Company / PropCo): Freehold title "
        "holder of 78 and 82 Marston Gardens, completely ring-fenced from care operational liabilities. 3) ADOV Care Group LIMITED (Care Operating "
        "Company / OpCo): CQC-registered regulated provider, employing all frontline care staff, managing council/NHS contracts, and leasing the physical assets."
    )
    p6.set_fill_color(0.15, 0.20, 0.25)
    p6.draw_wrapped_text(p6_corp_text, 46, 735, p6.cw - 20, font="F1", size=7.8, leading=10.0)
    
    # Intercompany Commercial FRI Leases Box
    p6.set_fill_color(0.98, 0.98, 0.99)
    p6.set_stroke_color(0.25, 0.35, 0.55)
    p6.draw_rect(36, 425, p6.cw, 210, fill=True, stroke=True, stroke_w=1.0)
    
    p6.set_fill_color(0.12, 0.22, 0.40)
    p6.draw_rect(36, 610, p6.cw, 25, fill=True)
    p6.set_fill_color(1.0, 1.0, 1.0)
    p6.draw_text("4.2 INTERCOMPANY FULLY REPAIRING & INSURING (FRI) LEASES", 46, 618, font="F2", size=9.0)
    
    fri_pts = [
        ("78 Marston Gardens FRI Lease (ADOV LIMITED to OpCo):",
         "A formal 10-year FRI commercial lease is executed between ADOV LIMITED (Landlord) and ADOV Care Group LIMITED (Tenant) at an independent "
         "market rent of £65,000 / year. This rental payment represents a fully tax-deductible trading expense for Corporation Tax in OpCo, "
         "transferring profits safely into the asset-holding company."),
         
        ("80 Marston Gardens FRI Lease (Director/UBO to OpCo):",
         "A formal 10-year FRI commercial lease is executed between the property owner (the Director) and ADOV Care Group LIMITED (Tenant) at an "
         "independent market rent of £50,000 / year. This £50,000 expense is 100% tax-deductible in OpCo, providing direct personal rental income."),
         
        ("Combined Corporate Deduction (£115,000 / year):",
         "Total internal property lease expenses paid by OpCo equal £115,000 / year. At the 25% UK Corporation Tax rate, this lease structuring "
         "delivers an immediate £28,750 annual corporation tax saving within the operating business.")
    ]
    cur_fy = 600
    for f_t, f_d in fri_pts:
        p6.set_fill_color(0.12, 0.25, 0.50)
        p6.draw_text(f_t, 46, cur_fy, font="F2", size=7.5)
        cur_fy -= 10
        p6.set_fill_color(0.18, 0.22, 0.28)
        cur_fy = p6.draw_wrapped_text(f_d, 46, cur_fy, p6.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_fy -= 8
        
    # The Tax-Neutral Rent-Swap Box
    p6.set_fill_color(0.97, 0.99, 0.97)
    p6.set_stroke_color(0.15, 0.55, 0.25)
    p6.draw_rect(36, 42, p6.cw, 372, fill=True, stroke=True, stroke_w=1.0)
    
    p6.set_fill_color(0.12, 0.45, 0.20)
    p6.draw_rect(36, 390, p6.cw, 24, fill=True)
    p6.set_fill_color(1.0, 1.0, 1.0)
    p6.draw_text("4.3 THE HMRC TAX-NEUTRAL RENT-SWAP (LIVING AT 82 MARSTON GARDENS)", 46, 397, font="F2", size=8.5)
    
    swap_pts = [
        ("HMRC Benefit in Kind (BIK) Elimination (s.105 & s.106 ITEPA 2003):",
         "Under Section 105 and 106 of the Income Tax (Earnings and Pensions) Act 2003, living in corporate-owned residential property triggers a heavy "
         "annual Benefit in Kind tax charge based on property value. However, the legislation explicitly mandates that where the director pays "
         "FULL OPEN MARKET RENT under a formal tenancy, the taxable benefit is legally reduced to NIL. By executing a standard Assured Shorthold Tenancy "
         "(AST) between ADOV LIMITED (Landlord) and the Director (Tenant) at £1,500/month (£18,000/year), BIK liability is 100% extinguished."),
         
        ("Net Personal Cashflow Surplus (+£32,000 / year):",
         "The financial mechanism produces an exceptional personal cash advantage: The Director receives £50,000/year rental income from leasing "
         "80 Marston Gardens to OpCo. The Director pays £18,000/year to ADOV LIMITED to reside at 82 Marston Gardens. Net personal cash surplus = "
         "+£32,000 / year. Meanwhile, the £18,000 paid into ADOV LIMITED remains within the group corporate perimeter."),
         
        ("Annual Tax on Enveloped Dwellings (ATED) & Section 133 Relief:",
         "Finance Act 2013 imposes ATED on corporate-held dwellings valued over £500,000. 82 Marston Gardens has an independent market value "
         "under £450,000, falling safely below the statutory threshold. Furthermore, commercial care letting of 78 Marston Gardens qualifies for "
         "100% statutory relief under Section 133 of the Finance Act 2013."),
         
        ("VAT Welfare Exemption (Schedule 9, Group 7 VATA 1994):",
         "Regulated health and social care services are VAT-exempt. Because OpCo cannot recover input VAT, ADOV LIMITED must NOT execute an "
         "Option to Tax on 78 Marston Gardens, preserving VAT neutrality across all intercompany rents.")
    ]
    cur_wy = 378
    for w_t, w_d in swap_pts:
        p6.set_fill_color(0.12, 0.45, 0.20)
        p6.draw_text(w_t, 46, cur_wy, font="F2", size=7.5)
        cur_wy -= 10
        p6.set_fill_color(0.18, 0.22, 0.28)
        cur_wy = p6.draw_wrapped_text(w_d, 46, cur_wy, p6.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_wy -= 6


    # =========================================================================
    # PAGE 7: CHAPTER 5 - ARCHITECTURAL & SANITARY ADAPTATION
    # =========================================================================
    p7 = doc.add_page()
    p7.draw_header_banner("5", "ARCHITECTURAL & SANITARY ADAPTATION", "WETROOM BREAKTHROUGH")
    
    # Sanitary Engineering Callout Box
    p7.set_fill_color(0.97, 0.98, 1.0)
    p7.set_stroke_color(0.20, 0.35, 0.60)
    p7.draw_rect(36, 620, p7.cw, 150, fill=True, stroke=True, stroke_w=1.0)
    
    p7.set_fill_color(0.10, 0.20, 0.40)
    p7.draw_rect(36, 745, p7.cw, 25, fill=True)
    p7.set_fill_color(1.0, 1.0, 1.0)
    p7.draw_text("5.1 SANITARY INFRASTRUCTURE REALITY & £42,000 CAPEX REDUCTION", 46, 753, font="F2", size=9.0)
    
    p7_san_text = (
        "A transformative architectural advantage is that BOTH 78 AND 80 MARSTON GARDENS ALREADY POSSESS A DEDICATED SEPARATE WC "
        "AND A LARGE-SIZE WETROOM / SHOWER ROOM, with 78 additionally featuring an en-suite bathroom to Bedroom 1. "
        "Standard care conversions frequently waste over £60,000 attempting to retrofit small en-suites into every bedroom, causing massive "
        "drainage disruptions and reducing usable bedroom floor space. By capitalizing on the existing wetroom infrastructure, ADOV Care Group "
        "adds just ONE additional en-suite to Bedroom 2 in 78. This delivers 2 en-suites + 1 communal wetroom + 1 WC in 78 (Toilet ratio 1:1.25, "
        "Shower ratio 1:1.67 for 5 residents), and 1 large wetroom + 1 WC in 80 (Toilet ratio 1:1.5, Shower ratio 1:3 for 3 residents). "
        "This substantially exceeds CQC and Luton Council minimum standards (1:3 ratio) and slashes sanitary CapEx by £42,000."
    )
    p7.set_fill_color(0.15, 0.20, 0.25)
    p7.draw_wrapped_text(p7_san_text, 46, 735, p7.cw - 20, font="F1", size=7.8, leading=10.0)
    
    # Campus Space Allocation Table
    p7.set_fill_color(0.10, 0.16, 0.28)
    p7.draw_rect(36, 595, p7.cw, 20, fill=True)
    p7.set_fill_color(1.0, 1.0, 1.0)
    
    p7.draw_text("Property Asset", 40, 602, font="F2", size=7.2)
    p7.draw_text("Allocated Room Layout & Functional Use", 160, 602, font="F2", size=7.2)
    p7.draw_text("Sanitary & Compliance Ratios", 360, 602, font="F2", size=7.2)
    
    space_rows = [
        ("78 Marston Gdns (Main Residence)", "5 Resident Bedrooms (13m² - 16m²), Commercial Kitchen, Dining Room, Sensory Lounge, Garden Access.", "2 En-Suites + 1 Large Wetroom + 1 WC (Toilets 1:1.25, Showers 1:1.67) - EXCEEDS CQC"),
        ("80 Marston Gdns (Specialist Wing)", "3 Resident Bedrooms (Bed 7 Ground Floor, Beds 6 & 8 Upstairs), Staff Sleep-in Office, Day Room.", "1 Large Wetroom + 1 Separate WC (Toilets 1:1.5, Showers 1:3.0) - CQC COMPLIANT"),
        ("Exterior & Grounds (Both Houses)", "Twin flanking private driveways accommodating 8 vehicles off-street + 2 detached rear garages.", "LLP32 Compliant: 1:1 Parking to bed ratio. Zero highway impact on Marston Gardens.")
    ]
    cur_sy7 = 578
    for s_prop, s_layout, s_san in space_rows:
        p7.set_fill_color(0.96, 0.98, 1.0)
        p7.draw_rect(36, cur_sy7 - 4, p7.cw, 26, fill=True)
        
        p7.set_fill_color(0.12, 0.22, 0.40)
        p7.draw_text(s_prop, 40, cur_sy7 + 8, font="F2", size=6.8)
        
        p7.set_fill_color(0.18, 0.22, 0.28)
        p7.draw_wrapped_text(s_layout, 160, cur_sy7 + 12, 195, font="F1", size=6.5, leading=8.5)
        p7.draw_wrapped_text(s_san, 360, cur_sy7 + 12, 195, font="F1", size=6.5, leading=8.5)
        cur_sy7 -= 28.0

    # Technical Engineering Box
    p7.set_fill_color(0.98, 0.98, 0.99)
    p7.set_stroke_color(0.25, 0.35, 0.55)
    p7.draw_rect(36, 42, p7.cw, 445, fill=True, stroke=True, stroke_w=1.0)
    
    p7.set_fill_color(0.12, 0.22, 0.40)
    p7.draw_rect(36, 463, p7.cw, 24, fill=True)
    p7.set_fill_color(1.0, 1.0, 1.0)
    p7.draw_text("5.2 STATUTORY BUILDING REGULATIONS & LIFE SAFETY COMPLIANCE", 46, 470, font="F2", size=8.5)
    
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
        p7.set_fill_color(0.12, 0.25, 0.50)
        p7.draw_text(e_t, 46, cur_ey, font="F2", size=7.5)
        cur_ey -= 10
        p7.set_fill_color(0.18, 0.22, 0.28)
        cur_ey = p7.draw_wrapped_text(e_d, 46, cur_ey, p7.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_ey -= 7

    print("Added Page 6 and Page 7.")
''')

print("append_brochure_p6_p7 written.")
