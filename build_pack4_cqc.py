#!/usr/bin/env python3
"""
ADOV Care Group - Document Pack 4: CQC Statement of Purpose (SoP) & Leadership Pack
"""

import sys, os, zlib, zipfile
from build_statutory_document_packs import SimplePDF

def build_pdf():
    doc = SimplePDF("ADOV_Care_Group_CQC_Statement_of_Purpose.pdf", "CQC STATEMENT OF PURPOSE (SoP)")
    
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
    p1.draw_text("CQC STATUTORY REGISTRATION DOSSIER", 62, p1.height - 67, font="F2", size=8.5)
    
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("ADOV CARE GROUP", 54, p1.height - 125, font="F2", size=24.0)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_line(54, p1.height - 138, p1.width - 54, p1.height - 138, stroke_w=1.5)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("STATEMENT OF PURPOSE (REGULATION 12)", 54, p1.height - 162, font="F2", size=14.0)
    p1.set_fill_color(0.80, 0.88, 1.0)
    p1.draw_text("Health and Social Care Act 2008 // CQC (Registration) Regulations 2009", 54, p1.height - 180, font="F1", size=10.0)
    p1.draw_text("Service Model: Specialist Supported Living // Regulated Activity: Personal Care", 54, p1.height - 198, font="F1", size=8.5)
    
    # Metadata Card
    p1.set_fill_color(0.08, 0.14, 0.26)
    p1.set_stroke_color(0.25, 0.38, 0.60)
    p1.draw_rect(54, 340, p1.width - 108, 260, fill=True, stroke=True, stroke_w=1.0)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("CQC REGULATORY REGISTRATION PARTICULARS", 70, 575, font="F2", size=10.0)
    p1.draw_line(70, 567, p1.width - 70, 567, stroke_w=0.8)
    
    meta_cqc = [
        ("Registered Provider Name:", "ADOV Care Group LIMITED (Company Registered in England & Wales)"),
        ("Parent Holding Group:", "FAIRYTALES GROUP (Trading Name of Mamun Limited / 100% Parent)"),
        ("Regulated Activity:", "Personal Care (Health and Social Care Act 2008 Regulated Activities Regs 2014)"),
        ("Service Type / Model:", "Supported Living Scheme ('Housing with Care' CQC Guidance)"),
        ("Service Band / Specialism:", "Autism, Severe Learning Disabilities, Challenging Behaviour, PBS"),
        ("Location 1 (Main Hub):", "78 Marston Gardens, Luton, LU2 7DY (5 Specialist Resident Bedrooms)"),
        ("Location 2 (Supported Wing):", "80 Marston Gardens, Luton, LU2 7DY (3 Specialist Resident Bedrooms)")
    ]
    cur_cy1 = 548
    for l, v in meta_cqc:
        p1.set_fill_color(0.70, 0.80, 0.95)
        p1.draw_text(l, 70, cur_cy1, font="F2", size=7.5)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_wrapped_text(v, 205, cur_cy1, p1.width - 275, font="F1", size=7.2, leading=9.0)
        cur_cy1 -= 21.0
        
    p1.set_fill_color(0.12, 0.18, 0.32)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_rect(54, 140, p1.width - 108, 160, fill=True, stroke=True, stroke_w=1.2)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("PROJECT PLANNED BY ABDULLAHMAMUN.COM", 70, 275, font="F2", size=11.0)
    p1.draw_line(70, 267, p1.width - 70, 267, stroke_w=0.6)
    
    p1_cqc_desc = (
        "This Statement of Purpose is formulated in strict accordance with the CQC Single Assessment Framework "
        "and Section 12 of the Care Quality Commission (Registration) Regulations 2009. It demonstrates full statutory "
        "compliance across all 5 Key Questions (Safe, Effective, Caring, Responsive, Well-Led) and the Oliver McGowan "
        "Mandatory Training requirements under Section 181 of the Health and Care Act 2022."
    )
    p1.set_fill_color(0.90, 0.94, 1.0)
    p1.draw_wrapped_text(p1_cqc_desc, 70, 250, p1.width - 140, font="F1", size=7.5, leading=10.5)
    
    p1.set_fill_color(0.60, 0.70, 0.85)
    p1.draw_text("CQC REGISTRATION DOSSIER // SUBMISSION READY // OCTOBER 2026", 54, 50, font="F1", size=7.2)

    # -------------------------------------------------------------
    # PAGE 2: PARTS 1, 2 & 3 (AIMS, LOCATIONS & REGULATED ACTIVITIES)
    # -------------------------------------------------------------
    p2 = doc.add_page()
    p2.draw_header_banner("C1", "PARTS 1, 2 & 3: PROVIDER, AIMS & LOCATIONS", "CQC REGULATION 12")
    
    p2.set_fill_color(0.98, 0.98, 1.0)
    p2.set_stroke_color(0.20, 0.35, 0.60)
    p2.draw_rect(36, 45, p2.cw, 725, fill=True, stroke=True, stroke_w=1.0)
    p2.set_fill_color(0.10, 0.20, 0.40)
    p2.draw_rect(36, 745, p2.cw, 25, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    p2.draw_text("CQC STATEMENT OF PURPOSE: SECTIONS 1, 2 AND 3", 46, 753, font="F2", size=8.5)
    
    sop_parts = [
        ("PART 1: PROVIDER INFORMATION & GOVERNANCE:",
         "Provider Name: ADOV Care Group LIMITED. Company No. Registered in England & Wales. Registered Office: Marston Gardens, Luton, LU2 7DY. "
         "Parent Company: FAIRYTALES GROUP (Trading Name of Mamun Limited). Legal Status: Private Limited Company. Nominated Individual (Regulation 6): "
         "Executive Director of Fairytales Group. Accountable Body: Board of Directors."),
         
        ("PART 2: AIMS AND OBJECTIVES OF ADOV CARE GROUP:",
         "1) To deliver bespoke, person-centred supported living services to adults aged 18-64 with autism, severe learning disabilities, and complex "
         "behavioural presentations under the Positive Behavioural Support (PBS) framework. 2) To uphold service user choice, independence, and domestic "
         "dignity in compliance with CQC's 'Right Support, Right Care, Right Culture' guidance. 3) To provide continuous multi-disciplinary support in "
         "partnership with Luton Borough Council Adult Social Care and NHS Bedfordshire, Luton & Milton Keynes ICB. 4) To operate on STOMP principles "
         "(Stopping Over-Medication of People with Learning Disabilities) and British Institute of Learning Disabilities (BILD) accredited restraint reduction."),
         
        ("PART 3: SERVICE LOCATIONS & PHYSICAL CAMPUS ASSETS:",
         "Location 1: 78 Marston Gardens, Luton, LU2 7DY. 5 resident bedrooms (13m²-16m²), 2 en-suites, 1 large communal wetroom, 1 separate WC, commercial "
         "kitchen, dining room, quiet sensory room, and sensory garden access. Flanking private driveway for 4 vehicles + detached rear garage. "
         "Location 2: 80 Marston Gardens, Luton, LU2 7DY. 3 resident bedrooms, 1 large communal wetroom, 1 separate WC, staff management hub/sleep-in room, "
         "day room, and direct garden access. Flanking private driveway for 4 vehicles + detached rear garage."),
         
        ("STATUTORY SEPARATION OF HOUSING AND CARE:",
         "In strict compliance with CQC guidance on Supported Living, housing management and personal care are legally and contractually separated. "
         "Residents hold individual Assured Shorthold Tenancy agreements granting exclusive possession of their personal bedrooms and shared communal areas. "
         "Care and support are provided under a completely independent Care & Support Agreement. Residents retain the statutory right to change care providers "
         "without jeopardizing their housing tenure.")
    ]
    cur_py2 = 730
    for p_t, p_d in sop_parts:
        p2.set_fill_color(0.10, 0.20, 0.40)
        p2.draw_text(p_t, 46, cur_py2, font="F2", size=7.2)
        cur_py2 -= 9
        p2.set_fill_color(0.18, 0.22, 0.28)
        cur_py2 = p2.draw_wrapped_text(p_d, 46, cur_py2, p2.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_py2 -= 6

    # -------------------------------------------------------------
    # PAGE 3: PART 4 (LEADERSHIP, RM QUALIFICATIONS & 34 STATEMENTS)
    # -------------------------------------------------------------
    p3 = doc.add_page()
    p3.draw_header_banner("C2", "PART 4: REGISTERED MANAGER & CQC QUALITY STATEMENTS", "CQC REGULATION 12")
    
    p3.set_fill_color(0.98, 0.98, 1.0)
    p3.set_stroke_color(0.20, 0.35, 0.60)
    p3.draw_rect(36, 45, p3.cw, 725, fill=True, stroke=True, stroke_w=1.0)
    p3.set_fill_color(0.10, 0.20, 0.40)
    p3.draw_rect(36, 745, p3.cw, 25, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("CQC STATEMENT OF PURPOSE: PART 4 - MANAGEMENT & QUALITY FRAMEWORK", 46, 753, font="F2", size=8.5)
    
    part4_sections = [
        ("4.1 REGISTERED MANAGER STATUTORY SPECIFICATION (REGULATION 7):",
         "The Registered Manager holds statutory day-to-day operational responsibility. Requirements: 1) Level 5 Diploma in Leadership and Management "
         "for Adult Care (or equivalent RMA/NVQ Level 4). 2) Minimum 3 years supervisory management experience in autism and complex learning disabilities. "
         "3) Enhanced DBS on update service with barring list check. 4) Passing CQC Fit and Proper Persons interview assessing clinical knowledge, "
         "Safeguarding Adults Level 3, Mental Capacity Act 2005 & DoLS/LPS, and medication management under NICE SC1 guidelines."),
         
        ("4.2 NOMINATED INDIVIDUAL SPECIFICATION (REGULATION 6):",
         "The Nominated Individual is a corporate Director of Fairytales Group and ADOV Care Group LIMITED, responsible for supervising the management "
         "of regulated activities, providing financial and physical governance, ensuring resource availability, and acting as CQC liaison."),
         
        ("4.3 OLIVER MCGOWAN MANDATORY TRAINING IN AUTISM & LEARNING DISABILITIES:",
         "Under Section 181 of the Health and Care Act 2022, all 14 frontline PBS support staff and managers complete the Oliver McGowan Mandatory Training. "
         "Tier 1 (eLearning) and Tier 2 (co-delivered live interactive training with autistic experts by experience) are completed prior to resident intake."),
         
        ("4.4 EMBEDDING THE CQC SINGLE ASSESSMENT FRAMEWORK (34 QUALITY STATEMENTS):",
         "SAFE: Robust safeguarding protocols, BS 5839-1 Cat L1 fire systems, electronic MAR medication tracking, environmental risk assessments. "
         "EFFECTIVE: Evidence-based PBS care planning, nutritional support, physical health tracking with local GPs, speech and language therapy integration. "
         "CARING: Person-centred dignity, privacy, advocacy support, promotion of communication aids (PECS/Makaton). "
         "RESPONSIVE: Proactive behavioural support, sensory regulation rooms, tailored transition protocols, independent living skill building. "
         "WELL-LED: Rigorous clinical auditing, monthly Regulation 17 governance reviews, transparent whistleblowing, open stakeholder engagement."),
         
        ("DECLARATION & SUBMISSION:",
         "Signed on behalf of ADOV Care Group LIMITED: _________________________ Registered Manager. _________________________ Nominated Individual. "
         "Date: 1st November 2026. Submitted to the Care Quality Commission via the CQC Provider Portal.")
    ]
    cur_py3 = 730
    for p4_t, p4_d in part4_sections:
        p3.set_fill_color(0.10, 0.20, 0.40)
        p3.draw_text(p4_t, 46, cur_py3, font="F2", size=7.2)
        cur_py3 -= 9
        p3.set_fill_color(0.18, 0.22, 0.28)
        cur_py3 = p3.draw_wrapped_text(p4_d, 46, cur_py3, p3.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_py3 -= 5

    doc.save()

def build_docx():
    filename = "ADOV_Care_Group_CQC_Statement_of_Purpose.docx"
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

    add_p("CQC STATUTORY REGISTRATION DOSSIER", style="Heading3", bold=True, color="D97706", space_after=60)
    add_p("ADOV CARE GROUP - STATEMENT OF PURPOSE (REGULATION 12)", style="Heading1", bold=True, color="0F1A2E", space_after=80)
    add_p("Project Planned by AbdullahMamun.com", bold=True, color="D4AF37", space_after=100)
    add_p("Provider: ADOV Care Group LIMITED // Parent Group: FAIRYTALES GROUP (Trading Name of Mamun Limited)", color="555555", space_after=60)
    add_p("Regulated Activity: Personal Care // Model: Supported Living ('Housing with Care')", color="555555", space_after=180)
    
    add_p("PART 1 & 2: PROVIDER DETAILS & AIMS", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("Registered Provider: ADOV Care Group LIMITED (Company Registered in England & Wales).")
    add_bullet("Parent Company: FAIRYTALES GROUP (Trading Name of Mamun Limited / 100% Parent Entity).")
    add_bullet("Aims & Objectives: Person-centred supported living for adults with autism and complex learning disabilities under Positive Behavioural Support (PBS).")
    add_bullet("Clinical Framework: BILD-accredited restraint reduction and STOMP over-medication reduction protocols.")

    add_p("PART 3: LOCATIONS & STATUTORY SEPARATION", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("Location 1: 78 Marston Gardens, Luton, LU2 7DY (5 Specialist Bedrooms, 2 En-suites, Wetroom, Commercial Kitchen).")
    add_bullet("Location 2: 80 Marston Gardens, Luton, LU2 7DY (3 Specialist Bedrooms, Wetroom, Staff Office Hub, Day Room).")
    add_bullet("Statutory Separation: Strict legal separation between Assured Shorthold Tenancies and Care & Support Agreements under CQC 'Housing with Care'.")

    add_p("PART 4: STATUTORY LEADERSHIP & CQC FRAMEWORK", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("Registered Manager (Regulation 7): Level 5 Diploma in Leadership & Management for Adult Care, min 3 yrs autism/LD experience, enhanced DBS.")
    add_bullet("Nominated Individual (Regulation 6): Corporate Director appointed for statutory governance and CQC interface.")
    add_bullet("Oliver McGowan Mandatory Training: All 14 care staff trained in Tier 1 and Tier 2 autism/LD competencies prior to intake.")
    add_bullet("Single Assessment Framework: Safe, Effective, Caring, Responsive, Well-Led quality statements fully embedded.")

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
