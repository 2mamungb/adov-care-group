#!/usr/bin/env python3
"""
ADOV Care Group - Document Pack 3: Section 192 Planning Justification Statement
"""

import sys, os, zlib, zipfile
from build_statutory_document_packs import SimplePDF

def build_pdf():
    doc = SimplePDF("ADOV_Care_Group_Section_192_Planning_Statement.pdf", "SECTION 192 PLANNING STATEMENT")
    
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
    p1.draw_text("TOWN PLANNING STATUTORY SUBMISSION", 62, p1.height - 67, font="F2", size=8.5)
    
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("ADOV CARE GROUP", 54, p1.height - 125, font="F2", size=24.0)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_line(54, p1.height - 138, p1.width - 54, p1.height - 138, stroke_w=1.5)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("SECTION 192 PLANNING JUSTIFICATION STATEMENT", 54, p1.height - 162, font="F2", size=13.5)
    p1.set_fill_color(0.80, 0.88, 1.0)
    p1.draw_text("Application for Certificate of Lawfulness for Proposed Use under Class C3(b)", 54, p1.height - 180, font="F1", size=10.0)
    p1.draw_text("Sites: 78 & 80 Marston Gardens, Luton, Bedfordshire, LU2 7DY", 54, p1.height - 198, font="F1", size=8.5)
    
    # Metadata Card
    p1.set_fill_color(0.08, 0.14, 0.26)
    p1.set_stroke_color(0.25, 0.38, 0.60)
    p1.draw_rect(54, 340, p1.width - 108, 260, fill=True, stroke=True, stroke_w=1.0)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("STATUTORY PLANNING APPLICATION DETAILS", 70, 575, font="F2", size=10.0)
    p1.draw_line(70, 567, p1.width - 70, 567, stroke_w=0.8)
    
    meta_p1 = [
        ("Local Planning Authority:", "Luton Borough Council Planning Department, Town Hall, Luton, LU1 2BQ"),
        ("Applicant Name:", "ADOV Care Group LIMITED (on behalf of FAIRYTALES GROUP & ADOV LIMITED)"),
        ("Application Mechanism:", "Section 192 of the Town and Country Planning Act 1990 (CLPUD)"),
        ("Existing Use Class:", "Class C3(a) (Dwellinghouse)"),
        ("Proposed Use Class:", "Class C3(b) (Supported living for up to 6 persons living together with care)"),
        ("High Court Precedents:", "North Devon DC v FSS [2004] EWHC 587; Hossack v Kettering BC [2002] EWCA Civ 886"),
        ("Highways Compliance:", "Luton Local Plan 2011-2031 Policy LLP32 (8 off-street spaces + 2 garages)")
    ]
    cur_py1 = 548
    for l, v in meta_p1:
        p1.set_fill_color(0.70, 0.80, 0.95)
        p1.draw_text(l, 70, cur_py1, font="F2", size=7.5)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_wrapped_text(v, 205, cur_py1, p1.width - 275, font="F1", size=7.2, leading=9.0)
        cur_py1 -= 21.0
        
    p1.set_fill_color(0.12, 0.18, 0.32)
    p1.set_stroke_color(0.85, 0.65, 0.18)
    p1.draw_rect(54, 140, p1.width - 108, 160, fill=True, stroke=True, stroke_w=1.2)
    
    p1.set_fill_color(0.85, 0.65, 0.18)
    p1.draw_text("PROJECT PLANNED BY ABDULLAHMAMUN.COM", 70, 275, font="F2", size=11.0)
    p1.draw_line(70, 267, p1.width - 70, 267, stroke_w=0.6)
    
    p1_summary = (
        "This Planning Justification Statement formally accompanies two concurrent Section 192 Certificate of Lawfulness "
        "applications submitted to Luton Borough Council. Under Section 55(2)(f) of the Town and Country Planning Act 1990, "
        "the proposed use of 78 Marston Gardens (5 resident service users) and 80 Marston Gardens (3 resident service users) "
        "falls squarely within Use Class C3(b) and does NOT constitute development. Approval is a matter of strict legal entitlement."
    )
    p1.set_fill_color(0.90, 0.94, 1.0)
    p1.draw_wrapped_text(p1_summary, 70, 250, p1.width - 140, font="F1", size=7.5, leading=10.5)
    
    p1.set_fill_color(0.60, 0.70, 0.85)
    p1.draw_text("STATUTORY PLANNING STATEMENT // SUBMISSION READY // OCTOBER 2026", 54, 50, font="F1", size=7.2)

    # -------------------------------------------------------------
    # PAGE 2: STATUTORY BASIS & CASE LAW
    # -------------------------------------------------------------
    p2 = doc.add_page()
    p2.draw_header_banner("S1", "STATUTORY LEGISLATIVE BASIS & CASE LAW PRECEDENTS", "PLANNING LAW")
    
    p2.set_fill_color(0.98, 0.98, 1.0)
    p2.set_stroke_color(0.20, 0.35, 0.60)
    p2.draw_rect(36, 45, p2.cw, 725, fill=True, stroke=True, stroke_w=1.0)
    p2.set_fill_color(0.10, 0.20, 0.40)
    p2.draw_rect(36, 745, p2.cw, 25, fill=True)
    p2.set_fill_color(1.0, 1.0, 1.0)
    p2.draw_text("1. LEGISLATIVE FOUNDATION & JURISPRUDENTIAL COMPLIANCE", 46, 753, font="F2", size=8.5)
    
    law_sections = [
        ("1.1 THE TOWN AND COUNTRY PLANNING ACT 1990 SECTION 55(2)(f):",
         "Section 55(1) of the 1990 Act defines development as including the making of any material change in the use of any buildings or other land. "
         "However, Section 55(2)(f) expressly provides that: 'in the case of buildings or other land which are used for a purpose of any class specified "
         "in an order made by the Secretary of State under this section, the use of the buildings or other land or, subject to the provisions of the order, "
         "of any part thereof for any other purpose of the same class' shall NOT be taken for the purposes of this Act to involve development. "
         "Because both properties are existing dwellinghouses within Class C3, continuation within Class C3(b) is exempt from requiring planning permission."),
         
        ("1.2 USE CLASS C3(b) OF THE USE CLASSES ORDER 1987 (AS AMENDED):",
         "Class C3 is divided into three distinct sub-classes. Class C3(b) encompasses: 'Use as a dwellinghouse by not more than six residents living "
         "together as a single household where care is provided for residents'. The proposed operational scheme across 78 Marston Gardens provides for "
         "FIVE (5) resident service users, and 80 Marston Gardens provides for THREE (3) resident service users. Both properties remain strictly below "
         "the statutory ceiling of six residents, fully qualifying for Class C3(b) status."),
         
        ("1.3 HIGH COURT AUTHORITY: NORTH DEVON DC v FIRST SECRETARY OF STATE [2004]:",
         "In North Devon District Council v First Secretary of State [2004] EWHC 587 (Admin), Collins J considered whether a supported living home for "
         "two children with visiting care staff operating on shifts fell within Class C3(b). The High Court held that children or adults who cannot live "
         "independently due to disability, living together with carers providing 24-hour care, constitute a 'single household' under Class C3(b). "
         "The judgment establishes that resident carers are NOT required to reside permanently on the premises for Class C3(b) to apply."),
         
        ("1.4 COURT OF APPEAL: HOSSACK v KETTERING BOROUGH COUNCIL [2002]:",
         "In Hossack v Kettering Borough Council [2002] EWCA Civ 886, the Court of Appeal confirmed that the domestic character of the occupation is "
         "the decisive test. Communal meal preparation, shared dining and lounge facilities, and domestic chores confirm that the property operates "
         "as a domestic dwellinghouse, rather than an institutional establishment (Class C2)."),
         
        ("1.5 LACK OF STATUTORY DISCRETION UNDER SECTION 192:",
         "Section 192 applications evaluate questions of strict law and fact. The local planning authority has NO statutory power to assess the planning "
         "'merits' of the proposal, nor to consider local housing need, neighbor perceptions, or political representations. If the proposed use meets "
         "the statutory criteria of Class C3(b), the Council has a mandatory duty to grant the Certificate.")
    ]
    cur_ly = 730
    for l_t, l_d in law_sections:
        p2.set_fill_color(0.10, 0.20, 0.40)
        p2.draw_text(l_t, 46, cur_ly, font="F2", size=7.2)
        cur_ly -= 9
        p2.set_fill_color(0.18, 0.22, 0.28)
        cur_ly = p2.draw_wrapped_text(l_d, 46, cur_ly, p2.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_ly -= 5

    # -------------------------------------------------------------
    # PAGE 3: HIGHWAYS, PARKING & AMENITY ASSESSMENT
    # -------------------------------------------------------------
    p3 = doc.add_page()
    p3.draw_header_banner("S2", "HIGHWAYS, PARKING & RESIDENTIAL AMENITY", "LOCAL PLAN COMPLIANCE")
    
    p3.set_fill_color(0.98, 0.98, 1.0)
    p3.set_stroke_color(0.20, 0.35, 0.60)
    p3.draw_rect(36, 45, p3.cw, 725, fill=True, stroke=True, stroke_w=1.0)
    p3.set_fill_color(0.10, 0.20, 0.40)
    p3.draw_rect(36, 745, p3.cw, 25, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("2. HIGHWAYS, TRANSPORT & NEIGHBOR AMENITY ASSESSMENT (POLICY LLP32)", 46, 753, font="F2", size=8.5)
    
    amenity_sections = [
        ("2.1 LUTON LOCAL PLAN 2011-2031 POLICY LLP32 (PARKING STANDARDS):",
         "Under Appendix 2 of the Luton Local Plan, maximum parking standards for specialist residential accommodation require 1 space per 4 residents "
         "plus 1 space per full-time staff member. Across both properties (8 residents total), the planning standard suggests a requirement for 4-5 "
         "off-street spaces. In reality, 78 and 80 Marston Gardens provide an exceptional off-street parking provision: EIGHT (8) full private vehicle "
         "spaces across twin flanking driveways, plus TWO (2) detached rear garages. There is zero reliance on on-street parking."),
         
        ("2.2 TRIP GENERATION & TRAFFIC FLOW ANALYSIS:",
         "Adults with autism and severe learning disabilities do not operate private motor vehicles. Shift changeovers occur twice daily (08:00 and 20:00), "
         "outside peak residential commuting windows. Frontline staff shifts involve 3-4 carers at 78 and 2 carers at 80. All staff parking is fully "
         "absorbed on-site within private driveways. Commercial food deliveries occur once weekly via domestic delivery vans, identical to standard C3 residential homes."),
         
        ("2.3 NOISE, RESIDENTIAL AMENITY & ZERO ATTACHED NEIGHBORS:",
         "78 and 80 Marston Gardens form a self-contained semi-detached block sharing a central party wall, with absolutely zero attached residential "
         "neighbors on either outer flank. The party wall is entirely internal to ADOV Care Group. High-density acoustic SoundBloc plasterboard and "
         "mineral wool insulation will be installed across the party wall (>43dB airborne sound insulation), ensuring complete sensory regulation."),
         
        ("2.4 DOMESTIC ROUTINES UNDER POSITIVE BEHAVIOURAL SUPPORT (PBS):",
         "Positive Behavioural Support (PBS) relies on highly structured, scheduled domestic living routines, sensory calm, and predictable domestic "
         "activities. Service users engage in community activities, education, and vocational visits during the day, returning home for shared evening "
         "meals. There are no emergency sirens, no antisocial behavior, and no neighborhood disruption."),
         
        ("2.5 CONCLUSION & FORMAL PRAYER FOR CERTIFICATION:",
         "The applicant respectfully submits that the proposed use of 78 Marston Gardens for 5 residents and 80 Marston Gardens for 3 residents "
         "is lawful within the meaning of Section 192 of the Town and Country Planning Act 1990. Luton Borough Council is formally requested to issue "
         "the statutory Certificate of Lawfulness accordingly.")
    ]
    cur_ay3 = 730
    for a_t, a_d in amenity_sections:
        p3.set_fill_color(0.10, 0.20, 0.40)
        p3.draw_text(a_t, 46, cur_ay3, font="F2", size=7.2)
        cur_ay3 -= 9
        p3.set_fill_color(0.18, 0.22, 0.28)
        cur_ay3 = p3.draw_wrapped_text(a_d, 46, cur_ay3, p3.cw - 20, font="F1", size=6.8, leading=8.8)
        cur_ay3 -= 5

    doc.save()

def build_docx():
    filename = "ADOV_Care_Group_Section_192_Planning_Statement.docx"
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

    add_p("TOWN PLANNING STATUTORY SUBMISSION", style="Heading3", bold=True, color="D97706", space_after=60)
    add_p("SECTION 192 PLANNING JUSTIFICATION STATEMENT (CLASS C3b)", style="Heading1", bold=True, color="0F1A2E", space_after=80)
    add_p("Project Planned by AbdullahMamun.com", bold=True, color="D4AF37", space_after=100)
    add_p("Applicant: ADOV Care Group LIMITED // On Behalf of: FAIRYTALES GROUP & ADOV LIMITED", color="555555", space_after=60)
    add_p("Target Sites: 78 & 80 Marston Gardens, Luton, LU2 7DY // Local Authority: Luton Borough Council", color="555555", space_after=180)
    
    add_p("1. STATUTORY LEGISLATIVE BASIS & CLASS C3(b) COMPLIANCE", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("Town and Country Planning Act 1990 s.55(2)(f) explicitly exempts changes of use within the same class from constituting development.")
    add_bullet("Use Class C3(b) encompasses use as a dwellinghouse by not more than six residents living together as a single household where care is provided.")
    add_bullet("78 Marston Gardens accommodates 5 residents; 80 Marston Gardens accommodates 3 residents. Both sit safely below the statutory 6-person ceiling.")
    add_bullet("High Court Binding Precedent: North Devon DC v First Secretary of State [2004] EWHC 587 confirmed that adults living together with visiting care staff constitute a single household under Class C3(b).")
    add_bullet("Court of Appeal: Hossack v Kettering BC [2002] EWCA Civ 886 affirmed domestic routines establish Class C3(b) domestic character.")

    add_p("2. HIGHWAYS, PARKING & AMENITY (LUTON LOCAL PLAN POLICY LLP32)", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_bullet("Highways Provision: 8 dedicated off-street parking spaces (4 on each driveway) plus 2 rear garages completely satisfy Appendix 2 parking standards.")
    add_bullet("Residential Amenity: 78 and 80 form a self-contained semi-detached block with zero attached neighbors on either flank.")
    add_bullet("Acoustics: Approved Document E high-density SoundBloc acoustic insulation (>43dB) installed across internal party wall.")
    add_bullet("Conclusion: The Council has a mandatory statutory duty under Section 192 to grant the Certificate of Lawfulness.")

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
