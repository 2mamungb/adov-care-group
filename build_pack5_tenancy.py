#!/usr/bin/env python3
"""
ADOV Care Group - Document Pack 5: Supported Living Tenancy & Care Agreement Pack
"""

import sys, os, zlib, zipfile
from build_statutory_document_packs import SimplePDF

def build_pdf():
    doc = SimplePDF("ADOV_Care_Group_Supported_Living_Tenancy_Pack.pdf", "SUPPORTED LIVING TENANCY PACK")
    
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
    p1.draw_text("RESIDENT ADMISSION & TENANCY DOSSIER", 62, p1.height - 67, font="F2", size=8.5)
    
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("ADOV CARE GROUP", 54, p1.height - 125, font="F2", size=24.0)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_line(54, p1.height - 138, p1.width - 54, p1.height - 138, stroke_w=1.5)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("SUPPORTED LIVING TENANCY & CARE PACK", 54, p1.height - 162, font="F2", size=14.0)
    p1.set_fill_color(0.80, 0.88, 1.0)
    p1.draw_text("Resident Tenancy Agreement, Care Support Contract & SEA Housing Benefit Claim", 54, p1.height - 180, font="F1", size=10.0)
    p1.draw_text("Operating at: 78 & 80 Marston Gardens, Luton, Bedfordshire, LU2 7DY", 54, p1.height - 198, font="F1", size=8.5)
    
    # Metadata Card
    p1.set_fill_color(0.08, 0.14, 0.26)
    p1.set_stroke_color(0.25, 0.38, 0.60)
    p1.draw_rect(54, 340, p1.width - 108, 260, fill=True, stroke=True, stroke_w=1.0)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("RESIDENT ADMISSION CONTRACTS & HOUSING BENEFIT", 70, 575, font="F2", size=10.0)
    p1.draw_line(70, 567, p1.width - 70, 567, stroke_w=0.8)
    
    meta_t = [
        ("Landlord Entity (Leaseholder):", "ADOV Care Group LIMITED (Operating under commercial lease)"),
        ("Parent Holding Group:", "FAIRYTALES GROUP (Trading Name of Mamun Limited / 100% Parent)"),
        ("Tenancy Legal Structure:", "Assured Shorthold Tenancy (AST) granting exclusive possession of bedroom"),
        ("Care & Support Separation:", "Independent Care Contract compliant with CQC 'Housing with Care' rules"),
        ("Housing Benefit Category:", "Supported Exempt Accommodation (SEA) under Housing Benefit Regs 2006 Reg 13D"),
        ("Target Eligible Rent:", "£350.00 per week (£18,200 per annum per resident) covering intensive housing management"),
        ("Care & Support Tariff:", "£2,150.00 per week (funded jointly by Luton Council ASC & BLMK ICB)")
    ]
    cur_ty1 = 548
    for l, v in meta_t:
        p1.set_fill_color(0.70, 0.80, 0.95)
        p1.draw_text(l, 70, cur_ty1, font="F2", size=7.5)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_wrapped_text(v, 205, cur_ty1, p1.width - 275, font="F1", size=7.2, leading=9.0)
        cur_ty1 -= 21.0
        
    p1.set_fill_color(0.12, 0.18, 0.32)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_rect(54, 140, p1.width - 108, 160, fill=True, stroke=True, stroke_w=1.2)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("PROJECT PLANNED BY ABDULLAHMAMUN.COM", 70, 275, font="F2", size=11.0)
    p1.draw_line(70, 267, p1.width - 70, 267, stroke_w=0.6)
    
    p1_t_desc = (
        "This pack contains the complete legal documentation required to admit vulnerable adults into supported living "
        "at 78 and 80 Marston Gardens. It rigorously establishes the statutory separation between housing tenure (AST) and "
        "care delivery (Care Agreement), and provides the full evidential breakdown for the £350/week Supported Exempt "
        "Accommodation claim submitted to Luton Borough Council Revenues & Benefits."
    )
    p1.set_fill_color(0.90, 0.94, 1.0)
    p1.draw_wrapped_text(p1_t_desc, 70, 250, p1.width - 140, font="F1", size=7.5, leading=10.5)
    
    p1.set_fill_color(0.60, 0.70, 0.85)
    p1.draw_text("RESIDENT ADMISSION PACK // PRINT READY // OCTOBER 2026", 54, 50, font="F1", size=7.2)

    # -------------------------------------------------------------
    # PAGE 2: RESIDENT ASSURED SHORTHOLD TENANCY (AST)
    # -------------------------------------------------------------
    p2 = doc.add_page()
    p2.draw_header_banner("T1", "SUPPORTED LIVING ASSURED SHORTHOLD TENANCY (AST)", "CONTRACT 1 OF 3")
    
    p2.set_fill_color(0.98, 0.98, 1.0)
    p2.set_stroke_color(0.20, 0.35, 0.60)
    p2.draw_rect(36, 45, p2.cw, 725, fill=True, stroke=True, stroke_w=1.0)
    p2.set_fill_color(0.10, 0.20, 0.40)
    p2.draw_rect(36, 745, p2.cw, 25, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    p2.draw_text("SUPPORTED LIVING ASSURED SHORTHOLD TENANCY AGREEMENT", 46, 753, font="F2", size=8.5)
    
    ast_sections = [
        ("PARTIES & PREMISES:",
         "LANDLORD: ADOV Care Group LIMITED (Company Registered in England & Wales), acting as leaseholder provider. "
         "TENANT: The Service User (or their Deputy / Court of Protection Appointee / Power of Attorney). "
         "PREMISES: Bedroom [   ] (for private exclusive possession) together with shared non-exclusive use of the communal lounges, dining rooms, "
         "kitchen, wetrooms, WCs, sensory areas, and gardens at 78 / 80 Marston Gardens, Luton, LU2 7DY."),
         
        ("1. TERM & SECURITY OF TENURE:",
         "The tenancy commences on [   ] for an initial fixed term of 12 months, and continues on a monthly periodic basis thereafter. "
         "The Tenant enjoys exclusive possession of their allocated bedroom. The Landlord may only terminate the tenancy in accordance with "
         "the Housing Act 1988 upon obtaining an order from the County Court."),
         
        ("2. RENT & INTENSIVE HOUSING MANAGEMENT CHARGE:",
         "Total weekly accommodation charge: £350.00 PER WEEK (eligible for Supported Exempt Accommodation Housing Benefit). Breakdown: "
         "1) Core Property Rent: £165.00/week. 2) Communal Utilities & Depreciation (Heat, Light, Water): £45.00/week (ineligible HB element). "
         "3) Intensive Housing Management (IHM): £140.00/week, covering 24/7 property maintenance, concierge, fire safety system management, "
         "tenancy support, and welfare compliance."),
         
        ("3. LANDLORD STATUTORY COVENANTS:",
         "The Landlord covenants: 1) To ensure quiet enjoyment of the premises. 2) To maintain structural integrity, heating, hot water (TMV3 max 41°C), "
         "and electrical systems. 3) To service and inspect BS 5839-1 Cat L1 fire detection and FD30S doors. 4) To maintain building insurance."),
         
        ("4. INDEPENDENCE OF CARE DELIVERY:",
         "The parties agree that this tenancy is independent of the provision of care. The Tenant's occupation of the room is not conditional upon "
         "receiving personal care from ADOV Care Group; the Tenant has the statutory right to select an alternative CQC-registered provider."),
         
        ("SIGNATURES & EXECUTION:",
         "Signed on behalf of Landlord ADOV Care Group LIMITED: _________________________ Date: _______________. "
         "Signed by / on behalf of Tenant (Service User / Deputy / Appointee): _________________________ Relationship: _________________________ Date: _______________.")
    ]
    cur_ty2 = 730
    for a_t, a_d in ast_sections:
        p2.set_fill_color(0.10, 0.20, 0.40)
        p2.draw_text(a_t, 46, cur_ty2, font="F2", size=7.2)
        cur_ty2 -= 9
        p2.set_fill_color(0.18, 0.22, 0.28)
        cur_ty2 = p2.draw_wrapped_text(a_d, 46, cur_ty2, p2.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_ty2 -= 5

    # -------------------------------------------------------------
    # PAGE 3: CARE AGREEMENT & HOUSING BENEFIT EXEMPT CLAIM
    # -------------------------------------------------------------
    p3 = doc.add_page()
    p3.draw_header_banner("T2", "CARE CONTRACT & HOUSING BENEFIT EXEMPT LETTER", "CONTRACTS 2 & 3")
    
    # Top Box: Care Agreement
    p3.set_fill_color(0.98, 0.98, 1.0)
    p3.set_stroke_color(0.20, 0.35, 0.60)
    p3.draw_rect(36, 420, p3.cw, 350, fill=True, stroke=True, stroke_w=1.0)
    p3.set_fill_color(0.10, 0.20, 0.40)
    p3.draw_rect(36, 745, p3.cw, 25, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("SEPARATE CARE & SUPPORT AGREEMENT (CQC HOUSING WITH CARE COMPLIANCE)", 46, 753, font="F2", size=8.5)
    
    care_clauses = [
        ("PARTIES & REGULATORY BASIS:",
         "PROVIDER: ADOV Care Group LIMITED (CQC Registered Provider for Personal Care). SERVICE USER: [   ] (Resident at 78 / 80 Marston Gardens). "
         "COMMISSIONING BODY: Luton Borough Council Adult Social Care / NHS BLMK ICB under Individual Placement Agreement."),
         
        ("SCOPE OF CARE & PBS SUPPORT:",
         "The Provider delivers personal care and Positive Behavioural Support (PBS) in accordance with the multidisciplinary care plan: "
         "1) Assistance with personal hygiene, dressing, bathing, and medication administration (NICE SC1 guidelines). "
         "2) Support with meal preparation, sensory diet, and independent living skills. 3) 1:1 community engagement, education, and vocational activities. "
         "4) Core shared hours: 20 hours/week. 5) Assessed 1:1 PBS hours: [   ] hours/week @ £22.00/hour. Total weekly care package: £2,150.00/week."),
         
        ("SIGNATURES:",
         "Signed on behalf of Care Provider (Registered Manager): _________________________ Date: _______________. "
         "Signed by / on behalf of Service User (Appointee / Social Worker): _________________________ Date: _______________.")
    ]
    cur_cy3 = 730
    for c_t, c_d in care_clauses:
        p3.set_fill_color(0.10, 0.20, 0.40)
        p3.draw_text(c_t, 46, cur_cy3, font="F2", size=7.2)
        cur_cy3 -= 9
        p3.set_fill_color(0.18, 0.22, 0.28)
        cur_cy3 = p3.draw_wrapped_text(c_d, 46, cur_cy3, p3.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_cy3 -= 6

    # Bottom Box: Housing Benefit Letter
    p3.set_fill_color(0.97, 0.99, 0.97)
    p3.set_stroke_color(0.15, 0.55, 0.25)
    p3.draw_rect(36, 42, p3.cw, 365, fill=True, stroke=True, stroke_w=1.0)
    p3.set_fill_color(0.12, 0.45, 0.20)
    p3.draw_rect(36, 382, p3.cw, 25, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("SUPPORTED EXEMPT ACCOMMODATION CLAIM LETTER (LUTON REVENUES & BENEFITS)", 46, 390, font="F2", size=8.5)
    
    sea_clauses = [
        ("TO: Luton Borough Council Revenues & Benefits Department, Town Hall, Luton, LU1 2BQ.",
         "RE: Housing Benefit Claim for Supported Exempt Accommodation under Regulation 13D of the Housing Benefit Regulations 2006."),
         
        ("STATUTORY ELIGIBILITY & HOUSING MANAGEMENT PROOF:",
         "We formally certify that Bedroom [   ] at 78 / 80 Marston Gardens qualifies as 'Specified / Supported Exempt Accommodation' on the basis that: "
         "1) The accommodation is provided by ADOV Care Group LIMITED to a person with a learning disability / autism. "
         "2) The landlord provides more than minimal care, support, and supervision directly linked to the accommodation. "
         "3) The eligible rent of £350.00/week reflects the high-intensity housing management required for complex needs service users."),
         
        ("WEEKLY COST BREAKDOWN SUBMITTED FOR DIRECT PAYMENT:",
         "• Core Property Rent: £165.00/week  |  • 24/7 Concierge & Security: £55.00/week  |  • Building Maintenance & Repairs: £45.00/week\n"
         "• Fire Safety & L1 System Servicing: £25.00/week  |  • Tenancy & Welfare Support: £60.00/week  |  TOTAL ELIGIBLE RENT: £350.00 / WEEK."),
         
        ("DECLARATION & DIRECT PAYMENT REQUEST:",
         "We request that Housing Benefit be awarded in full at £350.00/week and paid directly to the Landlord ADOV Care Group LIMITED under Regulation 95 "
         "of the Housing Benefit Regulations 2006. Signed: _________________________ Commercial Director, ADOV Care Group LIMITED. Date: _______________.")
    ]
    cur_sy3 = 366
    for s_t, s_d in sea_clauses:
        p3.set_fill_color(0.12, 0.45, 0.20)
        p3.draw_text(s_t, 46, cur_sy3, font="F2", size=7.2)
        cur_sy3 -= 9
        p3.set_fill_color(0.18, 0.22, 0.28)
        cur_sy3 = p3.draw_wrapped_text(s_d, 46, cur_sy3, p3.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_sy3 -= 6

    doc.save()

def build_docx():
    filename = "ADOV_Care_Group_Supported_Living_Tenancy_Pack.docx"
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

    add_p("RESIDENT ADMISSION & TENANCY DOSSIER", style="Heading3", bold=True, color="D97706", space_after=60)
    add_p("ADOV CARE GROUP - SUPPORTED LIVING TENANCY & CARE PACK", style="Heading1", bold=True, color="0F1A2E", space_after=80)
    add_p("Project Planned by AbdullahMamun.com", bold=True, color="D4AF37", space_after=100)
    add_p("Landlord: ADOV Care Group LIMITED // Parent Group: FAIRYTALES GROUP (Trading Name of Mamun Limited)", color="555555", space_after=60)
    add_p("Target Premises: 78 & 80 Marston Gardens, Luton, LU2 7DY", color="555555", space_after=180)
    
    add_p("1. RESIDENT ASSURED SHORTHOLD TENANCY (AST) AGREEMENT", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_p("Grants exclusive possession of allocated private bedroom and non-exclusive shared use of communal wetrooms, dining, lounge, and gardens. Accommodation charge: £350.00 per week, eligible for direct payment under Supported Exempt Accommodation Housing Benefit.", space_after=100)

    add_p("2. SEPARATE CARE & SUPPORT AGREEMENT (CQC HOUSING WITH CARE)", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_p("Establishes strict legal and contractual separation between tenancy and care provision. Care tariff: £2,150.00 per week covering core shared support and 1:1 Positive Behavioural Support (PBS) hours, funded by Luton Council Adult Social Care and NHS BLMK ICB.", space_after=100)

    add_p("3. SUPPORTED EXEMPT ACCOMMODATION HOUSING BENEFIT CLAIM LETTER", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_p("Formal claim letter to Luton Borough Council Revenues & Benefits Department proving specified accommodation status under Regulation 13D of Housing Benefit Regulations 2006. Full breakdown of £350/week eligible rent covering 24/7 intensive housing management, safety systems, and tenancy support.", space_after=100)

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
