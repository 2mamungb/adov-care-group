#!/usr/bin/env python3
"""
ADOV Care Group - Document Pack 2: Corporate Legal & Intercompany Lease Pack
"""

import sys, os, zlib, zipfile
from build_statutory_document_packs import SimplePDF

def build_pdf():
    doc = SimplePDF("ADOV_Care_Group_Corporate_Legal_Pack.pdf", "CORPORATE LEGAL & INTERCOMPANY LEASE PACK")
    
    # -------------------------------------------------------------
    # PAGE 1: COVER
    # -------------------------------------------------------------
    p1 = doc.add_page(is_cover=True)
    p1.set_fill_color(0.04, 0.08, 0.16)
    p1.draw_rect(0, 0, p1.width, p1.height)
    
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_rect(24, 24, p1.width - 48, p1.height - 48, fill=False, stroke=True, stroke_w=1.5)
    p1.set_stroke_color(0.55, 0.42, 0.12)
    p1.draw_rect(28, 28, p1.width - 56, p1.height - 56, fill=False, stroke=True, stroke_w=0.6)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_rect(54, p1.height - 80, 240, 20, fill=True)
    p1.set_fill_color(0.04, 0.08, 0.16)
    p1.draw_text("STATUTORY LEGAL PACK", 62, p1.height - 67, font="F2", size=8.5)
    
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("ADOV CARE GROUP", 54, p1.height - 125, font="F2", size=24.0)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_line(54, p1.height - 138, p1.width - 54, p1.height - 138, stroke_w=1.5)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("CORPORATE LEGAL & INTERCOMPANY LEASE PACK", 54, p1.height - 162, font="F2", size=14.0)
    p1.set_fill_color(0.80, 0.88, 1.0)
    p1.draw_text("Commercial FRI Leases, Tax-Neutral AST Agreement & Board Written Resolutions", 54, p1.height - 180, font="F1", size=10.0)
    p1.draw_text("Target Assets: 78, 80 & 82 Marston Gardens, Luton, LU2 7DY", 54, p1.height - 198, font="F1", size=8.5)
    
    # Summary Box
    p1.set_fill_color(0.08, 0.14, 0.26)
    p1.set_stroke_color(0.25, 0.38, 0.60)
    p1.draw_rect(54, 340, p1.width - 108, 260, fill=True, stroke=True, stroke_w=1.0)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("STATUTORY CONTRACTS CONTAINED IN THIS DOSSIER", 70, 575, font="F2", size=10.0)
    p1.draw_line(70, 567, p1.width - 70, 567, stroke_w=0.8)
    
    docs = [
        ("Instrument 1: 10-Year Commercial FRI Lease (78 Marston Gardens)", "Landlord: ADOV LIMITED // Tenant: ADOV Care Group LIMITED // Rent: £65,000/yr // Tax-deductible trading expense."),
        ("Instrument 2: 10-Year Commercial FRI Lease (80 Marston Gardens)", "Landlord: Director / Property Owner // Tenant: ADOV Care Group LIMITED // Rent: £50,000/yr // Tax-deductible trading expense."),
        ("Instrument 3: Assured Shorthold Tenancy (82 Marston Gardens)", "Landlord: ADOV LIMITED // Tenant: Director // Rent: £1,500/mo (£18,000/yr) // Reduces HMRC Benefit in Kind (BIK) to NIL."),
        ("Instrument 4: Group Board Written Resolutions", "Approving adoption of 8-bed Supported Living Campus, commercial leases, CapEx budget, and executive living strategy.")
    ]
    cur_sy = 545
    for d_title, d_desc in docs:
        p1.set_fill_color(0.85, 0.65, 0.18)
        p1.draw_text(d_title, 70, cur_sy, font="F2", size=7.8)
        cur_sy -= 10
        p1.set_fill_color(0.90, 0.94, 1.0)
        cur_sy = p1.draw_wrapped_text(d_desc, 70, cur_sy, p1.width - 140, font="F1", size=7.2, leading=9.5)
        cur_sy -= 6
        
    p1.set_fill_color(0.12, 0.18, 0.32)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_rect(54, 140, p1.width - 108, 160, fill=True, stroke=True, stroke_w=1.2)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("PROJECT PLANNED BY ABDULLAHMAMUN.COM", 70, 275, font="F2", size=11.0)
    p1.draw_line(70, 267, p1.width - 70, 267, stroke_w=0.6)
    
    meta_rows = [
        ("Ultimate Parent Group:", "FAIRYTALES GROUP (Trading Name of Mamun Limited)"),
        ("Asset Holding Entity:", "ADOV LIMITED (Company No. Registered in England & Wales)"),
        ("Operating Care Entity:", "ADOV Care Group LIMITED (Company No. Registered in England & Wales)"),
        ("Total Annual Lease Expense:", "£115,000 / year (Saving £28,750 Corporation Tax annually)"),
        ("Net Personal Cashflow:", "+£32,000 / year tax-efficient net cashflow to Director")
    ]
    cur_my = 250
    for l, v in meta_rows:
        p1.set_fill_color(0.70, 0.80, 0.95)
        p1.draw_text(l, 70, cur_my, font="F2", size=7.5)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_text(v, 205, cur_my, font="F1", size=7.5)
        cur_my -= 16.0
        
    p1.set_fill_color(0.60, 0.70, 0.85)
    p1.draw_text("EXECUTION COPY // READY FOR SIGNATURE & SEAL // OCTOBER 2026", 54, 50, font="F1", size=7.2)

    # -------------------------------------------------------------
    # PAGE 2: COMMERCIAL FRI LEASE 78 MARSTON GARDENS
    # -------------------------------------------------------------
    p2 = doc.add_page()
    p2.draw_header_banner("L1", "COMMERCIAL FRI LEASE: 78 MARSTON GARDENS", "CONTRACT 1 OF 3")
    
    p2.set_fill_color(0.98, 0.98, 1.0)
    p2.set_stroke_color(0.20, 0.35, 0.60)
    p2.draw_rect(36, 45, p2.cw, 725, fill=True, stroke=True, stroke_w=1.0)
    p2.set_fill_color(0.10, 0.20, 0.40)
    p2.draw_rect(36, 745, p2.cw, 25, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    p2.draw_text("10-YEAR COMMERCIAL FULLY REPAIRING & INSURING (FRI) LEASE AGREEMENT", 46, 753, font="F2", size=8.5)
    
    lease78_clauses = [
        ("DATE & PARTIES:", "DATED: 1st November 2026. (1) LANDLORD: ADOV LIMITED (Company No. Registered in England & Wales), whose registered office is at Marston Gardens, Luton, UK. (2) TENANT: ADOV Care Group LIMITED (Company No. Registered in England & Wales), whose registered office is at Marston Gardens, Luton, UK."),
        ("1. PREMISES DEMISED:", "78 Marston Gardens, Luton, Bedfordshire, LU2 7DY (Title Number registered at HM Land Registry), comprising a 6-bedroom semi-detached property, driveway parking for 4 vehicles, detached garage, and rear gardens."),
        ("2. TERM OF LEASE:", "A term of TEN (10) YEARS commencing on 1st November 2026 and expiring on 31st October 2036, with an option to renew for a further term of 10 years upon mutual written agreement."),
        ("3. ANNUAL BASIC RENT:", "The Tenant shall pay to the Landlord an annual rent of £65,000 (SIXTY-FIVE THOUSAND POUNDS STERLING), payable in equal monthly installments of £5,416.67 in advance on the first day of each calendar month."),
        ("4. PERMITTED USE:", "Use as a specialist supported living facility within Use Class C3(b) of the Town and Country Planning (Use Classes) Order 1987, providing residential care and accommodation for persons with learning disabilities and autism, and ancillary office and staff sleep-in facilities."),
        ("5. REPAIRING & INSURING OBLIGATIONS (FRI):", "The Tenant shall keep the interior, exterior, structural foundations, roof, mechanical and electrical services, and fire detection systems in good, substantial repair and condition throughout the Term. The Tenant shall reimburse the Landlord for building insurance premiums."),
        ("6. ALIENATION & SUBLETTING:", "The Tenant is expressly permitted to grant individual Assured Shorthold Tenancy agreements or occupancy licenses to vulnerable adult service users receiving care, without requiring prior Landlord consent."),
        ("7. STATUTORY COMPLIANCE & CQC:", "The Tenant shall comply in all respects with the Health and Social Care Act 2008, the Care Quality Commission regulations, and the Regulatory Reform (Fire Safety) Order 2005."),
        ("SIGNATURES & EXECUTION:", "EXECUTED as a DEED by ADOV LIMITED acting by a Director: _________________________ in the presence of Witness: _________________________. EXECUTED as a DEED by ADOV Care Group LIMITED acting by a Director: _________________________ in the presence of Witness: _________________________.")
    ]
    cur_ly = 730
    for c_title, c_text in lease78_clauses:
        p2.set_fill_color(0.10, 0.20, 0.40)
        p2.draw_text(c_title, 46, cur_ly, font="F2", size=7.2)
        cur_ly -= 9
        p2.set_fill_color(0.18, 0.22, 0.28)
        cur_ly = p2.draw_wrapped_text(c_text, 46, cur_ly, p2.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_ly -= 5

    # -------------------------------------------------------------
    # PAGE 3: COMMERCIAL FRI LEASE 80 MARSTON GARDENS
    # -------------------------------------------------------------
    p3 = doc.add_page()
    p3.draw_header_banner("L2", "COMMERCIAL FRI LEASE: 80 MARSTON GARDENS", "CONTRACT 2 OF 3")
    
    p3.set_fill_color(0.98, 0.98, 1.0)
    p3.set_stroke_color(0.20, 0.35, 0.60)
    p3.draw_rect(36, 45, p3.cw, 725, fill=True, stroke=True, stroke_w=1.0)
    p3.set_fill_color(0.10, 0.20, 0.40)
    p3.draw_rect(36, 745, p3.cw, 25, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("10-YEAR COMMERCIAL FULLY REPAIRING & INSURING (FRI) LEASE AGREEMENT", 46, 753, font="F2", size=8.5)
    
    lease80_clauses = [
        ("DATE & PARTIES:", "DATED: 1st November 2026. (1) LANDLORD: The Freehold Property Owner (Director / UBO of Fairytales Group). (2) TENANT: ADOV Care Group LIMITED (Company No. Registered in England & Wales), whose registered office is at Marston Gardens, Luton, UK."),
        ("1. PREMISES DEMISED:", "80 Marston Gardens, Luton, Bedfordshire, LU2 7DY (Title Number registered at HM Land Registry), comprising a 3-bedroom semi-detached property, 2 sitting rooms, 1 dining room, driveway parking for 4 vehicles, garage, and rear gardens."),
        ("2. TERM OF LEASE:", "A term of TEN (10) YEARS commencing on 1st November 2026 and expiring on 31st October 2036, with an option to renew for a further term of 10 years upon mutual written agreement."),
        ("3. ANNUAL BASIC RENT:", "The Tenant shall pay to the Landlord an annual rent of £50,000 (FIFTY THOUSAND POUNDS STERLING), payable in equal monthly installments of £4,166.67 in advance on the first day of each calendar month. (100% tax-deductible trading expense in Tenant OpCo)."),
        ("4. PERMITTED USE:", "Use as a specialist supported living facility within Use Class C3(b) of the Town and Country Planning (Use Classes) Order 1987, providing residential care and accommodation for persons with learning disabilities and autism, staff sleep-in hub, and day rooms."),
        ("5. REPAIRING & INSURING OBLIGATIONS (FRI):", "The Tenant shall keep the interior, exterior, structural foundations, roof, mechanical and electrical services, and fire detection systems in good, substantial repair and condition throughout the Term. The Tenant shall maintain comprehensive building and public liability insurance."),
        ("6. ALIENATION & SUBLETTING:", "The Tenant is expressly permitted to grant individual Assured Shorthold Tenancy agreements or occupancy licenses to vulnerable adult service users receiving care, without requiring prior Landlord consent."),
        ("7. STATUTORY COMPLIANCE & CQC:", "The Tenant shall comply in all respects with the Health and Social Care Act 2008, the Care Quality Commission regulations, and the Regulatory Reform (Fire Safety) Order 2005."),
        ("SIGNATURES & EXECUTION:", "SIGNED and DELIVERED as a DEED by the LANDLORD: _________________________ in the presence of Witness: _________________________. EXECUTED as a DEED by ADOV Care Group LIMITED acting by a Director: _________________________ in the presence of Witness: _________________________.")
    ]
    cur_ly3 = 730
    for c_title, c_text in lease80_clauses:
        p3.set_fill_color(0.10, 0.20, 0.40)
        p3.draw_text(c_title, 46, cur_ly3, font="F2", size=7.2)
        cur_ly3 -= 9
        p3.set_fill_color(0.18, 0.22, 0.28)
        cur_ly3 = p3.draw_wrapped_text(c_text, 46, cur_ly3, p3.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_ly3 -= 5

    # -------------------------------------------------------------
    # PAGE 4: AST FOR 82 MARSTON GARDENS & BOARD RESOLUTIONS
    # -------------------------------------------------------------
    p4 = doc.add_page()
    p4.draw_header_banner("L3", "ASSURED SHORTHOLD TENANCY (82) & BOARD RESOLUTIONS", "CONTRACT 3 OF 3")
    
    # Top Box: AST
    p4.set_fill_color(0.97, 0.99, 0.97)
    p4.set_stroke_color(0.15, 0.55, 0.25)
    p4.draw_rect(36, 415, p4.cw, 355, fill=True, stroke=True, stroke_w=1.0)
    p4.set_fill_color(0.12, 0.45, 0.20)
    p4.draw_rect(36, 745, p4.cw, 25, fill=True)
    p4.set_fill_color(1.0, 1.0, 1.0)
    p4.draw_text("ASSURED SHORTHOLD TENANCY (AST) AGREEMENT - 82 MARSTON GARDENS (HMRC BIK = NIL)", 46, 753, font="F2", size=8.5)
    
    ast_clauses = [
        ("PARTIES & PREMISES:", "LANDLORD: ADOV LIMITED. TENANT: The Director / Beneficiary of Fairytales Group. PREMISES: 82 Marston Gardens, Luton, LU2 7DY (4-bedroom detached house)."),
        ("TERM & RENT:", "TERM: Initial 12 months fixed term from 1st November 2026, continuing periodically thereafter. RENT: £1,500 per calendar month (£18,000 per annum) payable in advance on the 1st of each month from personal funds."),
        ("HMRC STATUTORY COMPLIANCE (s.105 & s.106 ITEPA 2003):", "The parties formally declare and record that the Rent of £1,500/month represents the full open market rental value of the Premises, supported by independent RICS market comparables. Under Sections 105 and 106 of the Income Tax (Earnings and Pensions) Act 2003, the payment of full market rent from personal earnings legally reduces the taxable Benefit in Kind (BIK) to NIL."),
        ("SIGNATURES:", "Signed by Landlord ADOV LIMITED: _________________________ Signed by Tenant Director: _________________________ Date: 1st November 2026.")
    ]
    cur_ay = 730
    for a_t, a_d in ast_clauses:
        p4.set_fill_color(0.12, 0.45, 0.20)
        p4.draw_text(a_t, 46, cur_ay, font="F2", size=7.2)
        cur_ay -= 9
        p4.set_fill_color(0.18, 0.22, 0.28)
        cur_ay = p4.draw_wrapped_text(a_d, 46, cur_ay, p4.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_ay -= 6

    # Bottom Box: Board Resolutions
    p4.set_fill_color(0.06, 0.10, 0.18)
    p4.set_stroke_color(0.85, 0.65, 0.18)
    p4.draw_rect(36, 42, p4.cw, 355, fill=True, stroke=True, stroke_w=1.2)
    p4.set_fill_color(0.85, 0.65, 0.18)
    p4.draw_rect(36, 372, p4.cw, 25, fill=True)
    p4.set_fill_color(0.04, 0.08, 0.16)
    p4.draw_text("WRITTEN BOARD RESOLUTIONS: FAIRYTALES GROUP & ADOV LIMITED", 46, 380, font="F2", size=8.5)
    
    resolutions = [
        ("RESOLUTION 1: APPROVAL OF SUPPORTED LIVING MASTERPLAN", "IT WAS RESOLVED that FAIRYTALES GROUP (Trading Name of Mamun Limited) and ADOV LIMITED formally approve the development of an 8-bed specialist supported living campus across 78 & 80 Marston Gardens, dedicated to Autism & Complex Learning Disabilities under Town Planning Use Class C3(b)."),
        ("RESOLUTION 2: EXECUTION OF INTERCOMPANY COMMERCIAL LEASES", "IT WAS RESOLVED that ADOV LIMITED enter into a 10-year commercial FRI lease for 78 Marston Gardens to ADOV Care Group LIMITED at £65,000/year, and approve the lease of 80 Marston Gardens at £50,000/year, representing £115,000/year in deductible operating expenses."),
        ("RESOLUTION 3: APPROVAL OF EXECUTIVE LIVING STRATEGY AT 82", "IT WAS RESOLVED that ADOV LIMITED enter into an Assured Shorthold Tenancy (AST) for 82 Marston Gardens with the Director at an open market rent of £1,500/month (£18,000/year), eliminating HMRC Benefit in Kind (BIK) under s.105/106 ITEPA 2003."),
        ("RESOLUTION 4: APPOINTMENT OF OFFICERS & BANKING MANDATE", "IT WAS RESOLVED that the Director be appointed as Nominated Individual for CQC registration, and executive management be authorized to open corporate commercial banking accounts and deploy £150,000 in capital expenditure."),
        ("BOARD SIGN-OFF & CERTIFICATION:", "CERTIFIED as a true and correct record of the decisions of the Board of Directors of FAIRYTALES GROUP and ADOV LIMITED on 1st November 2026. Signed: _________________________ Managing Director & Chairperson.")
    ]
    cur_ry4 = 356
    for r_t, r_d in resolutions:
        p4.set_fill_color(0.85, 0.65, 0.18)
        p4.draw_text(r_t, 46, cur_ry4, font="F2", size=7.2)
        cur_ry4 -= 9
        p4.set_fill_color(0.90, 0.94, 1.0)
        cur_ry4 = p4.draw_wrapped_text(r_d, 46, cur_ry4, p4.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_ry4 -= 5

    doc.save()

def build_docx():
    filename = "ADOV_Care_Group_Corporate_Legal_Pack.docx"
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
        '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/><w:color w:val="1E293B"/></w:rPr></w:rPrDefault></w:docDefaults>'
        '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:rPr><w:b/><w:color w:val="0F1A2E"/><w:sz w:val="34"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:rPr><w:b/><w:color w:val="1E3A8A"/><w:sz w:val="26"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:rPr><w:b/><w:color w:val="D97706"/><w:sz w:val="22"/></w:rPr></w:style>'
        '</w:styles>')
        
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
        p = f'<w:p><w:pPr><w:pStyle w:val="ListParagraph"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr><w:spacing w:after="80"/></w:pPr><w:r><w:t>• {safe}</w:t></w:r></w:p>'
        doc_body.append(p)

    add_p("STATUTORY LEGAL PACK", style="Heading3", bold=True, color="D97706", space_after=60)
    add_p("ADOV CARE GROUP - CORPORATE LEGAL & INTERCOMPANY LEASE PACK", style="Heading1", bold=True, color="0F1A2E", space_after=80)
    add_p("Project Planned by AbdullahMamun.com", bold=True, color="D4AF37", space_after=100)
    add_p("Parent Group: FAIRYTALES GROUP (Trading Name of Mamun Limited) // Asset Entity: ADOV LIMITED", color="555555", space_after=180)
    
    add_p("1. COMMERCIAL FRI LEASE AGREEMENT: 78 MARSTON GARDENS", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_p("Parties: (1) ADOV LIMITED (Landlord) and (2) ADOV Care Group LIMITED (Tenant). Term: 10 Years from 1st November 2026. Basic Rent: £65,000 per annum payable monthly in advance. Permitted Use: Specialist supported living facility within Use Class C3(b). Repairing & Insuring: Full Repairing and Insuring (FRI) lease terms.", space_after=100)
    
    add_p("2. COMMERCIAL FRI LEASE AGREEMENT: 80 MARSTON GARDENS", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_p("Parties: (1) The Property Owner / Director (Landlord) and (2) ADOV Care Group LIMITED (Tenant). Term: 10 Years from 1st November 2026. Basic Rent: £50,000 per annum payable monthly in advance. Permitted Use: Specialist supported living facility within Use Class C3(b). Repairing & Insuring: Full Repairing and Insuring (FRI) lease terms.", space_after=100)

    add_p("3. ASSURED SHORTHOLD TENANCY (AST): 82 MARSTON GARDENS", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_p("Parties: (1) ADOV LIMITED (Landlord) and (2) The Director / Beneficiary of Fairytales Group (Tenant). Premises: 82 Marston Gardens, Luton, LU2 7DY. Rent: £1,500 per month (£18,000 per annum). Statutory Tax Impact: Paying full open market rent from personal taxed earnings legally reduces HMRC Benefit in Kind (BIK) under s.105 & s.106 ITEPA 2003 to NIL. Net surplus personal cashflow: +£32,000/year.", space_after=100)

    add_p("4. WRITTEN BOARD RESOLUTIONS: FAIRYTALES GROUP & ADOV LIMITED", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("Resolution 1: Approval of 8-bed Supported Living Campus across 78 & 80 Marston Gardens under Use Class C3(b).")
    add_bullet("Resolution 2: Execution of commercial FRI leases for 78 (£65,000/yr) and 80 (£50,000/yr) to ADOV Care Group LIMITED.")
    add_bullet("Resolution 3: Approval of AST for 82 Marston Gardens with the Director at £1,500/month, eliminating HMRC BIK.")
    add_bullet("Resolution 4: Appointment of Nominated Individual for CQC and authorization of £150,000 capital expenditure budget.")

    doc_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body>' + "".join(doc_body) +
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>'
        '</w:body></w:document>')
        
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as docx:
        docx.writestr('[Content_Types].xml', content_types)
        docx.writestr('_rels/.rels', pkg_rels)
        docx.writestr('word/_rels/document.xml.rels', doc_rels)
        docx.writestr('word/styles.xml', styles_xml)
        docx.writestr('word/document.xml', doc_xml)
    print(f"Generated DOCX '{filename}'.")

if __name__ == "__main__":
    build_pdf()
    build_docx()
