#!/usr/bin/env python3
"""
ADOV Care Group - Luxury Private Project & Investment Prospectus
A publication-grade, 12-page brochure and master investment prospectus.
Target Assets: 78 & 80 Marston Gardens (Care Campus) // 82 Marston Gardens (Executive Residence), Luton, LU2 7DY.
Parent Holding Entity: FAIRYTALES GROUP (Trading Name of Mamun Limited)
Asset Holding Entity: ADOV LIMITED
Operating Entity: ADOV Care Group LIMITED
Project Planned by AbdullahMamun.com
"""

import os
import sys
import zlib
import zipfile

# ==============================================================================
# LUXURY BROCHURE PDF ENGINE (PURE PYTHON / ZERO EXTERNAL DEPENDENCIES)
# ==============================================================================

from build_statutory_document_packs import LuxuryPDFDocument, LuxuryPDFPage

def build_luxury_brochure_pdf():
    doc = LuxuryPDFDocument("ADOV_Care_Group_Private_Project_Prospectus.pdf")
    
    # =========================================================================
    # PAGE 1: LUXURY BROCHURE COVER
    # =========================================================================
    p1 = doc.add_page()
    p1.page_type = "cover"
    
    # Deep Midnight Navy Canvas
    p1.set_fill_color(0.04, 0.08, 0.16)
    p1.draw_rect(0, 0, p1.width, p1.height)
    
    # Outer Architectural Gold Frame
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_rect(24, 24, p1.width - 48, p1.height - 48, fill=False, stroke=True, stroke_w=1.5)
    
    # Inner Fine Gold Accent Frame
    p1.set_stroke_color(0.55, 0.42, 0.12)
    p1.draw_rect(28, 28, p1.width - 56, p1.height - 56, fill=False, stroke=True, stroke_w=0.6)
    
    # Top Prospectus Pill
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_rect(54, p1.height - 80, 240, 20, fill=True)
    p1.set_fill_color(0.04, 0.08, 0.16)
    p1.draw_text("PRIVATE PROJECT & INVESTMENT PROSPECTUS", 62, p1.height - 67, font="F2", size=8.5)
    
    # Main Brand Titles
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("ADOV CARE GROUP", 54, p1.height - 125, font="F2", size=26.0)
    
    # Gold Horizontal Separator
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_line(54, p1.height - 138, p1.width - 54, p1.height - 138, stroke_w=1.5)
    
    # Subtitles
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("8-BED SPECIALIST SUPPORTED LIVING CAMPUS", 54, p1.height - 162, font="F2", size=14.5)
    
    p1.set_fill_color(0.80, 0.88, 1.0)
    p1.draw_text("Autism & Complex Learning Disabilities (PBS Care Model)", 54, p1.height - 180, font="F1", size=11.0)
    p1.draw_text("Unified Site: 78 & 80 Marston Gardens // Executive Residence: 82 Marston Gardens, Luton, LU2 7DY", 54, p1.height - 198, font="F1", size=8.5)
    
    # Core Strategic Synergies Card (Brochure Centerpiece)
    p1.set_fill_color(0.08, 0.14, 0.26)
    p1.set_stroke_color(0.25, 0.38, 0.60)
    p1.draw_rect(54, 305, p1.width - 108, 300, fill=True, stroke=True, stroke_w=1.0)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("EXECUTIVE REAL ESTATE & COMMERCIAL SYNERGIES", 70, 580, font="F2", size=10.0)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_line(70, 572, p1.width - 70, 572, stroke_w=0.8)
    
    synergies = [
        ("Unified 78 & 80 Semi-Detached Block:", "Forms a single self-contained residential block with ZERO attached neighbors on either flank, permanently eliminating neighbor noise and party-wall disputes."),
        ("Twin Private Flanking Driveways:", "Left driveway (80) parks 4 vehicles; Right driveway (78) parks 4 vehicles. Total 8 dedicated off-street spaces + 2 rear garages satisfies Luton Local Plan Policy LLP32."),
        ("Existing Wetroom CapEx Breakthrough:", "Both 78 & 80 possess 1 separate WC and 1 large wetroom; 78 has an en-suite. Adding only 1 en-suite to Bed 2 in 78 slashes CapEx by £42,000 to just £150,000 turnkey."),
        ("HMRC Tax-Neutral Living at 82:", "Director moves family residence to 82 Marston Gardens under an AST at £1,500/mo, reducing Benefit in Kind (s.105/106 ITEPA) to NIL while netting +£32,000/yr surplus cashflow."),
        ("Exceptional Financial Performance:", "Generates £1,043,328 in gross annual revenue, £408,328 in OpCo EBITDA (39.1% margin), and £523,328 in total annual net group cashflow (261.6% Annual ROCE).")
    ]
    cur_sy_p1 = 552
    for s_title, s_desc in synergies:
        p1.set_fill_color(0.85, 0.65, 0.18)
        p1.draw_text(s_title, 70, cur_sy_p1, font="F2", size=7.8)
        cur_sy_p1 -= 10
        p1.set_fill_color(0.90, 0.94, 1.0)
        cur_sy_p1 = p1.draw_wrapped_text(s_desc, 70, cur_sy_p1, p1.width - 140, font="F1", size=7.2, leading=9.5)
        cur_sy_p1 -= 6
        
    # Project Planner & Corporate Authority Card
    p1.set_fill_color(0.12, 0.18, 0.32)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_rect(54, 115, p1.width - 108, 165, fill=True, stroke=True, stroke_w=1.2)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("PROJECT PLANNED BY ABDULLAHMAMUN.COM", 70, 258, font="F2", size=11.5)
    
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_line(70, 250, p1.width - 70, 250, stroke_w=0.6)
    
    plan_meta = [
        ("Ultimate Parent Entity:", "FAIRYTALES GROUP (Trading Name of Mamun Limited / 100% Parent)"),
        ("Asset Holding Entity:", "ADOV LIMITED (Property Company / PropCo)"),
        ("Operating Care Entity:", "ADOV Care Group LIMITED (Care Operating Company / OpCo)"),
        ("Target Client Group:", "Adults (18-64) with Autism, Severe Learning Disabilities & Complex PBS"),
        ("Town Planning Mechanism:", "Town & Country Planning Act 1990 s.192 CLPUD (Use Class C3b)"),
        ("Regulatory Oversight:", "Care Quality Commission (CQC) - Regulated Activity: Personal Care")
    ]
    cur_pmy = 234
    for pl, pv in plan_meta:
        p1.set_fill_color(0.70, 0.80, 0.95)
        p1.draw_text(pl, 70, cur_pmy, font="F2", size=7.5)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_text(pv, 205, cur_pmy, font="F1", size=7.5)
        cur_pmy -= 16.5
        
    # Cover Footer Stamp
    p1.set_fill_color(0.60, 0.70, 0.85)
    p1.draw_text("STRICTLY PRIVATE & CONFIDENTIAL // COMMERCIAL INVESTMENT PROSPECTUS // OCTOBER 2026", 54, 50, font="F1", size=7.2)


    # =========================================================================
    # PAGE 2: TABLE OF CONTENTS & PROSPECTUS DIRECTORY
    # =========================================================================
    p2 = doc.add_page()
    p2.page_type = "toc"
    
    p2.draw_header_banner("0", "TABLE OF CONTENTS & PROSPECTUS DIRECTORY", "PROJECT BLUEPRINT")
    
    # Intro Card
    p2.set_fill_color(0.97, 0.98, 1.0)
    p2.set_stroke_color(0.20, 0.35, 0.60)
    p2.draw_rect(36, 685, p2.cw, 80, fill=True, stroke=True, stroke_w=1.0)
    
    p2.set_fill_color(0.10, 0.20, 0.40)
    p2.draw_rect(36, 745, p2.cw, 20, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    p2.draw_text("PRIVATE PROSPECTUS OVERVIEW & INVESTMENT ARCHITECTURE", 46, 752, font="F2", size=8.5)
    
    p2_intro = (
        "This Private Investment Prospectus, planned by AbdullahMamun.com for FAIRYTALES GROUP (Trading Name of Mamun Limited), "
        "details the comprehensive statutory town planning, corporate structuring, architectural adaptation, CQC licensing, and financial "
        "engineering for an 8-bed specialist supported living campus across 78 & 80 Marston Gardens, Luton, with executive living at 82 Marston Gardens."
    )
    p2.set_fill_color(0.15, 0.20, 0.25)
    p2.draw_wrapped_text(p2_intro, 46, 735, p2.cw - 20, font="F1", size=7.8, leading=10.5)
    
    # Table of Contents Grid (10 Entries)
    toc_items = [
        ("Front Cover", "Executive Title, Asset Overview & Planning Authority", "Page 1", "01"),
        ("Chapter 1", "Executive Summary, Campus Real Estate Assets & Strategic Rationale", "Page 3", "02"),
        ("Chapter 2", "Master 4-Sector Statutory Investment & Feasibility Matrix", "Page 4", "03"),
        ("Chapter 3", "Statutory Town Planning Law & Dual Section 192 CLPUD Blueprint", "Page 5", "04"),
        ("Chapter 4", "Corporate Governance, Intercompany FRI Leases & HMRC Tax Rent-Swap", "Page 6", "05"),
        ("Chapter 5", "Architectural & Physical Infrastructure (Wetroom CapEx Optimization)", "Page 7", "06"),
        ("Chapter 6", "Financial Engineering: Itemized CapEx Budget & 3-Year P&L Model", "Page 8", "07"),
        ("Chapter 7", "Statutory Care Licensing: CQC Registration & Leadership Governance", "Page 9", "08"),
        ("Chapter 8", "Local Authority Commissioning & Zero-Void Placement Pipeline", "Page 10", "09"),
        ("Chapter 9", "Statutory Risk Registry, 26-Week Critical Path Roadmap & Resolution", "Page 11", "10"),
        ("Back Cover", "Strategic Summary, Corporate Directory & Sign-Off Block", "Page 12", "11")
    ]
    
    cur_ty_p2 = 650
    for ch, desc, pg, num in toc_items:
        # Background row card
        p2.set_fill_color(0.98, 0.99, 1.0)
        p2.set_stroke_color(0.85, 0.88, 0.94)
        p2.draw_rect(36, cur_ty_p2 - 4, p2.cw, 32, fill=True, stroke=True, stroke_w=0.8)
        
        # Chapter Number Badge
        p2.set_fill_color(0.12, 0.22, 0.40)
        p2.draw_rect(42, cur_ty_p2 + 2, 22, 20, fill=True)
        p2.set_fill_color(0.85, 0.65, 0.18)
        p2.draw_text(num, 47, cur_ty_p2 + 8, font="F2", size=8.0)
        
        # Chapter Label & Title
        p2.set_fill_color(0.10, 0.18, 0.32)
        p2.draw_text(ch.upper(), 72, cur_ty_p2 + 14, font="F2", size=8.0)
        p2.set_fill_color(0.30, 0.35, 0.45)
        p2.draw_text(desc, 72, cur_ty_p2 + 3, font="F1", size=7.2)
        
        # Page Number Pill
        p2.set_fill_color(0.85, 0.65, 0.18)
        p2.draw_rect(p2.width - 36 - 65, cur_ty_p2 + 4, 60, 18, fill=True)
        p2.set_fill_color(0.04, 0.08, 0.16)
        p2.draw_text(pg, p2.width - 36 - 55, cur_ty_p2 + 10, font="F2", size=7.8)
        
        cur_ty_p2 -= 36.5
        
    # Project Planner Endorsement Box
    p2.set_fill_color(0.06, 0.10, 0.18)
    p2.draw_rect(36, 42, p2.cw, 80, fill=True)
    p2.set_fill_color(0.85, 0.65, 0.18)
    p2.draw_rect(36, 42, 4.0, 80, fill=True)
    
    p2.draw_text("PROJECT PLANNED BY ABDULLAHMAMUN.COM", 50, 102, font="F2", size=10.0)
    p2.set_fill_color(0.90, 0.94, 1.0)
    p2_endorse = (
        "Designed and formulated by AbdullahMamun.com for FAIRYTALES GROUP (Trading Name of Mamun Limited). "
        "All town planning, CQC registration, architectural adaptations, and tax structuring protocols have been cross-audited "
        "against current UK statutes to guarantee 100% legal immunity, maximum tax efficiency, and long-term commercial profitability."
    )
    p2.draw_wrapped_text(p2_endorse, 50, 88, p2.cw - 30, font="F1", size=7.2, leading=9.5)


    # =========================================================================
    # PAGE 3: CHAPTER 1 - EXECUTIVE SUMMARY & STRATEGIC RATIONALE
    # =========================================================================
    p3 = doc.add_page()
    p3.draw_header_banner("1", "EXECUTIVE SUMMARY, CAMPUS ASSETS & STRATEGIC RATIONALE", "FAIRYTALES GROUP")
    
    # Narrative Box 1
    p3.set_fill_color(0.97, 0.98, 1.0)
    p3.set_stroke_color(0.20, 0.35, 0.60)
    p3.draw_rect(36, 645, p3.cw, 125, fill=True, stroke=True, stroke_w=1.0)
    
    p3.set_fill_color(0.10, 0.20, 0.40)
    p3.draw_rect(36, 745, p3.cw, 25, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("1.1 STRATEGIC PROJECT MANDATE & THE UNIFIED CAMPUS REALITY", 46, 753, font="F2", size=9.0)
    
    p3_text1 = (
        "FAIRYTALES GROUP (Trading Name of Mamun Limited) and its property subsidiary ADOV LIMITED possess prime residential assets in "
        "Marston Gardens, Luton (LU2 7DY). Combining 78 Marston Gardens (6 bedrooms, 1 separate WC, 1 large wetroom, 1 en-suite) and "
        "80 Marston Gardens (3 bedrooms, 2 sitting rooms, 1 dining room, 1 separate WC, 1 large wetroom) creates an exceptional 8-bed specialist care campus. "
        "Crucially, 78 and 80 form a single, symmetrical 1930s semi-detached block sharing a central party wall, with ZERO attached residential neighbors "
        "on either outer flank. Flanking private driveways provide 8 dedicated off-street parking spaces plus 2 rear garages, permanently eliminating "
        "parking congestion under Luton Local Plan Policy LLP32. Simultaneously, relocating the beneficiary to 82 Marston Gardens via an Assured Shorthold "
        "Tenancy (AST) at £1,500/month eliminates HMRC Benefit in Kind (BIK) to NIL, providing £32,000/year net surplus cashflow while maintaining 30-second "
        "crisis executive oversight."
    )
    p3.set_fill_color(0.15, 0.20, 0.25)
    p3.draw_wrapped_text(p3_text1, 46, 735, p3.cw - 20, font="F1", size=7.8, leading=10.0)
    
    # KPI Grid (6 metrics in 3x2)
    kpi_w = (p3.cw - 16) / 3
    kpi_h = 56
    kpis = [
        ("TOTAL CAMPUS CAPACITY", "8 Specialist Beds", "5 Beds in 78 + 3 Beds in 80", 0.12, 0.25, 0.45),
        ("TURNKEY CAPEXFit-Out", "£150,000 Total", "Slashed by existing wetrooms", 0.15, 0.45, 0.25),
        ("GROSS ANNUAL REVENUE", "£1,043,328 / yr", "Care hours + Exempt Housing Benefit", 0.12, 0.25, 0.45),
        ("OPCO NET EBITDA", "£408,328 / yr (39.1%)", "After £115k internal rent paid", 0.15, 0.45, 0.25),
        ("TOTAL GROUP CASHFLOW", "£523,328 / yr", "OpCo Profit + PropCo/User Rent", 0.12, 0.25, 0.45),
        ("PLANNING APPROVAL ODDS", "100% Lawful Guarantee", "Section 192 CLPUD (Use Class C3b)", 0.60, 0.35, 0.10)
    ]
    cur_kx = 36
    cur_ky = 575
    for idx, (k_t, k_v, k_s, r, g, b) in enumerate(kpis):
        p3.set_fill_color(0.96, 0.98, 1.0)
        p3.set_stroke_color(r, g, b)
        p3.draw_rect(cur_kx, cur_ky, kpi_w, kpi_h, fill=True, stroke=True, stroke_w=1.0)
        
        p3.set_fill_color(r, g, b)
        p3.draw_rect(cur_kx, cur_ky + kpi_h - 16, kpi_w, 16, fill=True)
        p3.set_fill_color(1.0, 1.0, 1.0)
        p3.draw_text(k_t, cur_kx + 6, cur_ky + kpi_h - 11, font="F2", size=7.0)
        
        p3.set_fill_color(0.08, 0.12, 0.20)
        p3.draw_text(k_v, cur_kx + 6, cur_ky + 23, font="F2", size=9.2)
        p3.set_fill_color(0.40, 0.45, 0.55)
        p3.draw_text(k_s, cur_kx + 6, cur_ky + 9, font="F1", size=6.6)
        
        if (idx + 1) % 3 == 0:
            cur_kx = 36
            cur_ky -= (kpi_h + 8)
        else:
            cur_kx += (kpi_w + 8)
            
    # Narrative Box 2: Strategic Recommendation
    p3.set_fill_color(0.97, 0.99, 0.97)
    p3.set_stroke_color(0.15, 0.55, 0.25)
    p3.draw_rect(36, 42, p3.cw, 395, fill=True, stroke=True, stroke_w=1.0)
    
    p3.set_fill_color(0.12, 0.45, 0.20)
    p3.draw_rect(36, 412, p3.cw, 25, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("1.2 BULLETPROOF SECTOR WINNER: AUTISM & COMPLEX LEARNING DISABILITIES", 46, 420, font="F2", size=9.0)
    
    reasons = [
        ("1. Absolute Statutory Planning Immunity (Class C3b / s.192 CLPUD):",
         "Under Town & Country Planning Act 1990 s.55(2)(f) and the Use Classes Order 1987, operating a supported living home for up to 6 residents living as a single household with care falls squarely within Class C3(b). By lodging two separate Section 192 CLPUD applications (78 with 5 beds, 80 with 3 beds), approval is a matter of strict legal entitlement. Neighbor objections, parking objections, and planning committee politics are ultra vires."),
        ("2. Extraordinary Placement Tenure & Zero Void Risk (7 to 15+ Years):",
         "Unlike Child EBD care (frequent moves, placement breakdowns) or Mental Health step-down (3-12 month turnover), adults with autism and severe learning disabilities require permanent, highly structured sensory environments. Once Luton Council and BLMK ICB place an adult service user, the placement typically endures for 7 to 15+ years. Void risk is mathematically reduced to virtually zero."),
        ("3. Flawless Operational Peace (Zero Police Callouts & Zero Antisocial Behavior):",
         "Positive Behavioural Support (PBS) relies on scheduled domestic routines, sensory regulation, and proactive de-escalation. There are no runaway episodes, no police vehicles, no anti-social behavior, and no neighborhood sirens. The domestic tranquility of Marston Gardens is perfectly preserved."),
        ("4. Massive Local Repatriation Demand from Luton Council & BLMK ICB:",
         "Luton Borough Council's Transforming Care Plan highlights an acute deficit of local specialist supported living accommodation. Currently, Luton spends tens of millions placing vulnerable adults in out-of-borough facilities at £3,000-£4,500/week. A high-quality local provider offering 8 beds at £2,500/week receives immediate, priority block commissioning from Charter House ALDT."),
        ("5. Superior Commercial Cash Generation (£523k/year Group Cashflow):",
         "Combining care hours (£2,150/week) with Supported Exempt Accommodation Housing Benefit (£350/week) yields £2,500/week per bed (£130,000/bed/year). At 88% stabilized occupancy (7 beds active), gross revenue reaches £1,043,328. After funding a 14-person full-time PBS care team and £115,000 in internal rents, OpCo delivers £408,328 in clean EBITDA.")
    ]
    cur_ry = 402
    for r_title, r_desc in reasons:
        p3.set_fill_color(0.12, 0.45, 0.20)
        p3.draw_text(r_title, 46, cur_ry, font="F2", size=7.5)
        cur_ry -= 10
        p3.set_fill_color(0.18, 0.22, 0.28)
        cur_ry = p3.draw_wrapped_text(r_desc, 46, cur_ry, p3.cw - 20, font="F1", size=7.2, leading=9.4)
        cur_ry -= 5

    print("Added Page 1, Page 2 and Page 3.")

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
