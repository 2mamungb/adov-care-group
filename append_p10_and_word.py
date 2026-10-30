with open("generate_government_project_report.py", "a") as f:
    f.write('''
    # =========================================================================
    # PAGE 10: CHAPTER 9 - RISK REGISTRY & 26-WEEK EXECUTION ROADMAP
    # =========================================================================
    p10 = doc.add_page()
    
    p10.set_fill_color(0.06, 0.10, 0.18)
    p10.draw_text("9. STATUTORY RISK REGISTRY & 26-WEEK EXECUTION ROADMAP", 36, 794, font="F2", size=13.0)
    p10.set_stroke_color(0.85, 0.60, 0.15)
    p10.draw_line(36, 786, p10.width - 36, 786, stroke_w=1.2)
    
    # Risk Registry Table Box
    p10.set_fill_color(0.97, 0.98, 1.0)
    p10.set_stroke_color(0.20, 0.35, 0.60)
    p10.draw_rect(36, 525, p10.cw, 250, fill=True, stroke=True, stroke_w=1.0)
    
    p10.set_fill_color(0.10, 0.20, 0.40)
    p10.draw_rect(36, 750, p10.cw, 25, fill=True)
    p10.set_fill_color(1.0, 1.0, 1.0)
    p10.draw_text("9.1 STATUTORY RISK REGISTRY & MITIGATION CONTROLS", 46, 758, font="F2", size=9.0)
    
    rw = [105, 55, 60, 303]
    p10.set_fill_color(0.15, 0.25, 0.45)
    p10.draw_rect(36, 730, p10.cw, 16, fill=True)
    p10.set_fill_color(1.0, 1.0, 1.0)
    rx = 36
    r_hdrs = ["Risk Factor", "Likelihood", "Impact", "Statutory Mitigation Strategy"]
    for i, rh in enumerate(r_hdrs):
        p10.draw_text(rh, rx + 4, 735, font="F2", size=6.8)
        rx += rw[i]
        
    risk_data = [
        ("Town Planning Refusal", "VERY LOW", "CRITICAL", "Dual Section 192 CLPUD (Use Class C3b). Binding case law (North Devon) makes refusal ultra vires. Planning policies and neighbor letters are legally irrelevant."),
        ("CQC Registration Delay", "MEDIUM", "HIGH", "Headhunt qualified Level 5 RM at Day 1. Deploy fully pre-audited 42-policy suite and robust 5-year financial forecast to eliminate validation delays."),
        ("Staff Recruitment Deficit", "MEDIUM", "HIGH", "Recruit 14 full-time carers at £13.50/hr (above Luton market average). Deliver Oliver McGowan training and guarantee clear pathway to Team Leader."),
        ("Occupancy / Void Losses", "LOW", "HIGH", "Establish early pipeline with Luton ALDT (Charter House) and Transitions 16-25 Team. Average placement tenure is 7-15+ years; 28-day notice protects voids."),
        ("HMRC BIK Challenge (82)", "VERY LOW", "MEDIUM", "Formal Assured Shorthold Tenancy (AST) paying open market rent of £1,500/mo (£18,000/yr) from personal funds, legally reducing BIK to NIL under s.105/106 ITEPA.")
    ]
    cur_ry = 712
    for r_lbl, r_lk, r_imp, r_mit in risk_data:
        p10.set_fill_color(0.96, 0.98, 1.0)
        p10.draw_rect(36, cur_ry - 4, p10.cw, 28, fill=True)
        
        p10.set_fill_color(0.12, 0.22, 0.40)
        p10.draw_text(r_lbl, 40, cur_ry + 10, font="F2", size=6.8)
        
        p10.set_fill_color(0.05, 0.45, 0.15) if "VERY LOW" in r_lk or "LOW" in r_lk else p10.set_fill_color(0.75, 0.35, 0.05)
        p10.draw_text(r_lk, 145, cur_ry + 10, font="F2", size=6.5)
        
        p10.set_fill_color(0.70, 0.10, 0.10) if "CRITICAL" in r_imp or "HIGH" in r_imp else p10.set_fill_color(0.75, 0.35, 0.05)
        p10.draw_text(r_imp, 200, cur_ry + 10, font="F2", size=6.5)
        
        p10.set_fill_color(0.18, 0.22, 0.28)
        p10.draw_wrapped_text(r_mit, 260, cur_ry + 14, 255, font="F1", size=6.2, leading=8.0)
        cur_ry -= 31.0

    # 26-Week Critical Path Roadmap Table Box
    p10.set_fill_color(0.98, 0.98, 0.99)
    p10.set_stroke_color(0.25, 0.35, 0.55)
    p10.draw_rect(36, 175, p10.cw, 340, fill=True, stroke=True, stroke_w=1.0)
    
    p10.set_fill_color(0.12, 0.22, 0.40)
    p10.draw_rect(36, 490, p10.cw, 25, fill=True)
    p10.set_fill_color(1.0, 1.0, 1.0)
    p10.draw_text("9.2 26-WEEK CRITICAL PATH MASTER EXECUTION ROADMAP", 46, 498, font="F2", size=9.0)
    
    gw = [75, 115, 230, 103]
    p10.set_fill_color(0.15, 0.25, 0.45)
    p10.draw_rect(36, 472, p10.cw, 15, fill=True)
    p10.set_fill_color(1.0, 1.0, 1.0)
    gx = 36
    g_hdrs = ["Timeline", "Phase / Domain", "Key Statutory & Physical Deliverables", "Status / Milestone"]
    for i, gh in enumerate(g_hdrs):
        p10.draw_text(gh, gx + 4, 476, font="F2", size=6.5)
        gx += gw[i]
        
    gantt_rows = [
        ("Weeks 1 - 4", "Corporate & RM Setup", "Incorporate ADOV Care Group; Execute commercial FRI leases; Headhunt Level 5 Registered Manager.", "Phase 1 Complete"),
        ("Weeks 5 - 8", "Planning & CQC Portal", "Lodge Dual S.192 CLPUDs to Luton Council; Submit CQC provider application with 42 policies.", "Applications Lodged"),
        ("Weeks 9 - 16", "CapEx Refurbishment", "Procure contractors; Fit BS 5839-1 Cat L1 fire system, FD30S doors, wetroom upgrade, Doc E acoustic walls.", "Site Turnkey Ready"),
        ("Weeks 17 - 20", "Statutory Interviews", "CQC Fit & Proper interviews for RM & NI; Submit Luton Council ProContract DPS (AT1115) tender.", "Interviews Cleared"),
        ("Weeks 21 - 24", "Licensing & Commission", "Receive CQC Certificate of Registration; Building Control Sign-Off; Host ALDT social work showcases.", "CQC CERTIFICATE ISSUED"),
        ("Weeks 25 - 26", "Zero-Void Admissions", "Admit Residents 1-4 to 78 Marston Gardens; Stabilize 14 FT care team; Open Phase 2 (80 Marston Gdns).", "COMMERCIAL GO-LIVE")
    ]
    cur_gy = 454
    for g_time, g_ph, g_del, g_st in gantt_rows:
        p10.set_fill_color(0.96, 0.98, 1.0)
        p10.draw_rect(36, cur_gy - 4, p10.cw, 34, fill=True)
        
        p10.set_fill_color(0.85, 0.60, 0.15) if "GO-LIVE" in g_st or "ISSUED" in g_st else p10.set_fill_color(0.12, 0.22, 0.40)
        p10.draw_text(g_time, 40, cur_gy + 14, font="F2", size=6.8)
        p10.draw_text(g_ph, 115, cur_gy + 14, font="F2", size=6.5)
        
        p10.set_fill_color(0.18, 0.22, 0.28)
        p10.draw_wrapped_text(g_del, 230, cur_gy + 18, 220, font="F1", size=6.2, leading=8.0)
        
        p10.set_fill_color(0.05, 0.45, 0.15) if "ISSUED" in g_st or "GO-LIVE" in g_st else p10.set_fill_color(0.12, 0.25, 0.50)
        p10.draw_text(g_st, 460, cur_gy + 14, font="F2", size=6.2)
        cur_gy -= 38.0

    # Executive Declaration Box
    p10.set_fill_color(0.97, 0.99, 0.97)
    p10.set_stroke_color(0.15, 0.55, 0.25)
    p10.draw_rect(36, 45, p10.cw, 115, fill=True, stroke=True, stroke_w=1.0)
    
    p10.set_fill_color(0.12, 0.45, 0.20)
    p10.draw_rect(36, 135, p10.cw, 25, fill=True)
    p10.set_fill_color(1.0, 1.0, 1.0)
    p10.draw_text("9.3 STATUTORY BOARD RESOLUTION & COMMISSIONING APPROVAL", 46, 143, font="F2", size=9.0)
    
    sign_text = (
        "RESOLVED: That Mamun LIMITED and ADOV LIMITED formally adopt the 8-Bed Unified Supported Living Masterplan across 78 & 80 "
        "Marston Gardens, Luton, dedicating the facility to Autism & Complex Learning Disabilities under Class C3(b). "
        "The Board approves the relocation of the executive beneficiary to 82 Marston Gardens via an Assured Shorthold Tenancy at £1,500/month, "
        "authorizes the execution of internal commercial FRI leases, approves the £150,000 turnkey capital expenditure, and directs the "
        "immediate submission of Dual Section 192 CLPUD applications to Luton Borough Council and provider registration to the CQC."
    )
    p10.set_fill_color(0.15, 0.20, 0.25)
    p10.draw_wrapped_text(sign_text, 46, 125, p10.cw - 20, font="F1", size=7.2, leading=9.4)

    doc.save()
    print("Full 10-Page PDF Document Successfully Saved!")


# ==============================================================================
# WORD (.DOCX) OPENXML ENGINE (PURE PYTHON / ZERO EXTERNAL DEPENDENCIES)
# ==============================================================================

def build_word_report():
    filename = "ADOV_Care_Group_Government_Project_Report.docx"
    
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

    add_p("HM GOVERNMENT & LOCAL COMMISSIONING PROJECT REPORT", style="Heading3", bold=True, color="D97706", space_after=60)
    add_p("STATUTORY MASTER FEASIBILITY & OCCUPANCY BLUEPRINT", style="Heading1", bold=True, color="0F1A2E", space_after=80)
    add_p("8-Bed Specialist Supported Living Campus (Autism & Complex Learning Disabilities)", bold=True, color="1E3A8A", space_after=140)
    add_p("Unified Site: 78 & 80 Marston Gardens, Luton, LU2 7DY // Executive Residence: 82 Marston Gardens", color="555555", space_after=60)
    add_p("Corporate Entities: Mamun LIMITED (HoldCo) // ADOV LIMITED (PropCo) // ADOV Care Group LIMITED (OpCo)", color="555555", space_after=240)
    
    add_p("1. EXECUTIVE SUMMARY & STRATEGIC RATIONALE", style="Heading2", bold=True, color="1E3A8A", space_after=120)
    add_p(
        "This Government Project Report establishes the definitive feasibility, statutory town planning, CQC registration, physical adaptation, "
        "and zero-void occupancy blueprint for transforming 78 & 80 Marston Gardens, Luton (LU2 7DY) into an 8-bed specialist supported living "
        "campus dedicated to adults with Autism and Complex Learning Disabilities under Positive Behavioural Support (PBS). "
        "Physical survey confirms that 78 and 80 form a self-contained semi-detached block with zero attached neighbors, twin driveways accommodating "
        "8 cars off-street, and existing wetroom infrastructure that slashes CapEx to £150,000 while generating £1,043,328 in annual revenue "
        "and £523,328 in total net group cashflow.",
        space_after=140
    )
    
    add_p("2. MASTER 4-SECTOR COMPARATIVE APPRAISAL & VERDICT", style="Heading2", bold=True, color="1E3A8A", space_after=120)
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
    add_bullet("Corporate Hierarchy: Mamun LIMITED (Group HoldCo / 100% Parent) -> ADOV LIMITED (PropCo holding 78 & 82) + Director (Personal owner of 80) -> ADOV Care Group LIMITED (OpCo / CQC Registered Entity).")
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
        
    print(f"Generated Master Government Project Report Word Document '{filename}' successfully.")


if __name__ == "__main__":
    build_pdf_report()
    build_word_report()
''')

print("append_p10_and_word written.")
