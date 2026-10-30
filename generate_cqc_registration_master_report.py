import os
import sys
import zlib
import zipfile

class SimplePDF:
    def __init__(self, filename, title="ADOV CARE GROUP // CQC REGISTRATION & REGULATORY DOSSIER"):
        self.filename = filename
        self.doc_title = title
        self.pages = []
        self.width = 595.28  # A4 width in pt
        self.height = 841.89 # A4 height in pt
        self.mx = 40.0       # Left/Right margin in pt
        self.cw = self.width - 2 * self.mx # 515.28 pt

    def add_page(self, is_cover=False, page_label=""):
        page = SimplePDFPage(self.width, self.height, self.mx, is_cover, self.doc_title, page_label)
        self.pages.append(page)
        return page

    def save(self):
        objects = []
        objects.append("<< /Type /Catalog /Pages 2 0 R >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>")
        
        page_refs = []
        page_obj_start = 5
        total_p = len(self.pages)
        
        for idx in range(total_p):
            p_obj_num = page_obj_start + idx * 2
            c_obj_num = p_obj_num + 1
            page_refs.append(f"{p_obj_num} 0 R")
            
        kids_str = " ".join(page_refs)
        objects.insert(1, f"<< /Type /Pages /Kids [ {kids_str} ] /Count {total_p} >>")
        
        for idx, page in enumerate(self.pages):
            p_num = idx + 1
            p_obj_num = page_obj_start + idx * 2
            c_obj_num = p_obj_num + 1
            
            p_dict = (
                f"<< /Type /Page /Parent 2 0 R "
                f"/MediaBox [0 0 {self.width:.2f} {self.height:.2f}] "
                f"/Contents {c_obj_num} 0 R "
                f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> >>"
            )
            objects.append(p_dict)
            
            content_stream = page.render(p_num, total_p)
            comp_stream = zlib.compress(content_stream.encode('latin1'))
            c_dict = (
                f"<< /Length {len(comp_stream)} /Filter /FlateDecode >>\n"
                f"stream\n"
            )
            objects.append((c_dict, comp_stream))

        with open(self.filename, 'wb') as f:
            f.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
            xref_offsets = []
            
            for idx, obj in enumerate(objects):
                xref_offsets.append(f.tell())
                obj_num = idx + 1
                if isinstance(obj, tuple):
                    header, stream_bytes = obj
                    f.write(f"{obj_num} 0 obj\n{header}".encode('latin1'))
                    f.write(stream_bytes)
                    f.write(b"\nendstream\nendobj\n")
                else:
                    f.write(f"{obj_num} 0 obj\n{obj}\nendobj\n".encode('latin1'))
                    
            xref_pos = f.tell()
            num_objs = len(objects) + 1
            f.write(f"xref\n0 {num_objs}\n0000000000 65535 f \n".encode('latin1'))
            for off in xref_offsets:
                f.write(f"{off:010d} 00000 n \n".encode('latin1'))
            
            f.write(
                f"trailer\n<< /Size {num_objs} /Root 1 0 R >>\n"
                f"startxref\n{xref_pos}\n%%EOF\n".encode('latin1')
            )
        print(f"Generated Academic PDF: {self.filename} ({os.path.getsize(self.filename)} bytes, {total_p} pages)")


class SimplePDFPage:
    def __init__(self, width, height, mx, is_cover, doc_title, page_label=""):
        self.width = width
        self.height = height
        self.mx = mx
        self.cw = width - 2 * mx
        self.is_cover = is_cover
        self.doc_title = doc_title
        self.page_label = page_label
        self.ops = []

    def set_stroke_color(self, r, g, b):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} RG")

    def set_fill_color(self, r, g, b):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")

    def draw_rect(self, x, y, w, h, fill=True, stroke=False, stroke_w=1.0):
        op = "re"
        if fill and stroke:
            paint = "B"
        elif fill:
            paint = "f"
        elif stroke:
            paint = "S"
        else:
            return
        if stroke:
            self.ops.append(f"{stroke_w:.2f} w")
        self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} {op} {paint}")

    def draw_line(self, x1, y1, x2, y2, stroke_w=1.0):
        self.ops.append(f"{stroke_w:.2f} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")

    def escape(self, text):
        s = str(text).replace("\u2022", "-").replace("\u2014", "-").replace("\u2013", "-").replace("\u2019", "'").replace("\u2018", "'")
        s = s.replace(chr(92), chr(92)+chr(92)).replace("(", chr(92)+"(").replace(")", chr(92)+")")
        return s
    def draw_text(self, text, x, y, font="F1", size=10, align="left", max_w=None):
        safe = self.escape(text)
        if align == "left" or max_w is None:
            self.ops.append(f"BT /{font} {size:.2f} Tf 1 0 0 1 {x:.2f} {y:.2f} Tm ({safe}) Tj ET")
        elif align == "center":
            char_w = size * 0.49
            approx_w = len(str(text)) * char_w
            adj_x = x + (max_w - approx_w) / 2.0
            self.ops.append(f"BT /{font} {size:.2f} Tf 1 0 0 1 {adj_x:.2f} {y:.2f} Tm ({safe}) Tj ET")
        elif align == "right":
            char_w = size * 0.49
            approx_w = len(str(text)) * char_w
            adj_x = x + max_w - approx_w
            self.ops.append(f"BT /{font} {size:.2f} Tf 1 0 0 1 {adj_x:.2f} {y:.2f} Tm ({safe}) Tj ET")

    def draw_wrapped_text(self, text, x, y, max_w, font="F1", size=7.1, leading=9.2):
        paragraphs = text.split("\n")
        cur_y = y
        char_w = size * 0.49
        max_chars = int(max_w / char_w)
        
        for p_idx, para in enumerate(paragraphs):
            para = para.strip()
            if not para:
                cur_y -= leading * 0.5
                continue
            words = para.split()
            lines = []
            current_line = []
            for w in words:
                test_line = " ".join(current_line + [w])
                if len(test_line) > max_chars and current_line:
                    lines.append(" ".join(current_line))
                    current_line = [w]
                else:
                    current_line.append(w)
            if current_line:
                lines.append(" ".join(current_line))
                
            for line in lines:
                safe = self.escape(line)
                self.ops.append(f"BT /{font} {size:.2f} Tf {x:.2f} {cur_y:.2f} Td ({safe}) Tj ET")
                cur_y -= leading
        return cur_y

    def draw_academic_header(self, section_num, section_title, page_category="REGULATORY POLICY"):
        self.set_stroke_color(0.20, 0.25, 0.32)
        self.draw_line(self.mx, self.height - 32, self.width - self.mx, self.height - 32, stroke_w=0.6)
        self.set_fill_color(0.40, 0.45, 0.55)
        self.draw_text(f"{page_category} // {self.doc_title}", self.mx, self.height - 27, font="F2", size=6.5)
        self.draw_text("WORKING PAPER NO. 2026-MG-05", self.width - self.mx - 150, self.height - 27, font="F2", size=6.5)
        
        self.set_stroke_color(0.76, 0.61, 0.22)
        self.draw_line(self.mx, self.height - 35, self.mx + 45, self.height - 35, stroke_w=1.2)

    def draw_section_heading(self, code, title, y):
        cur_y = y
        self.set_fill_color(0.76, 0.61, 0.22)
        self.draw_rect(self.mx, cur_y - 2, 2.5, 9.5, fill=True)
        self.set_fill_color(0.08, 0.14, 0.24)
        full_title = f"{code} {title}".upper()
        self.draw_text(full_title, self.mx + 7, cur_y, font="F2", size=7.8)
        return cur_y - 12.0

    def draw_academic_callout(self, title, text, y, h=40):
        self.set_fill_color(0.985, 0.99, 1.0)
        self.set_stroke_color(0.70, 0.78, 0.88)
        self.draw_rect(self.mx, y - h, self.cw, h, fill=True, stroke=True, stroke_w=0.6)
        self.set_fill_color(0.76, 0.61, 0.22)
        self.draw_rect(self.mx, y - h, 2.5, h, fill=True)
        self.set_fill_color(0.08, 0.14, 0.24)
        self.draw_text(title, self.mx + 8, y - 10, font="F2", size=7.2)
        self.set_fill_color(0.15, 0.20, 0.28)
        self.draw_wrapped_text(text, self.mx + 8, y - 19, self.cw - 16, font="F1", size=6.5, leading=8.2)
        return y - h - 8

    def draw_booktabs_table(self, title, cols, rows, y, row_h=10.8, font_size=6.1):
        cur_y = y
        if title:
            self.set_fill_color(0.08, 0.14, 0.24)
            self.draw_text(title, self.mx, cur_y, font="F2", size=7.3)
            cur_y -= 5
            
        self.set_stroke_color(0.08, 0.14, 0.24)
        self.draw_line(self.mx, cur_y, self.width - self.mx, cur_y, stroke_w=1.0)
        cur_y -= 8
        
        cur_x = self.mx + 4
        for h_txt, h_w in cols:
            self.set_fill_color(0.08, 0.14, 0.24)
            self.draw_text(h_txt, cur_x, cur_y, font="F2", size=font_size + 0.3)
            cur_x += h_w
        cur_y -= 4
        self.draw_line(self.mx, cur_y, self.width - self.mx, cur_y, stroke_w=0.5)
        cur_y -= 2
        
        for r_idx, r_data in enumerate(rows):
            cur_y -= row_h
            bg = (0.975, 0.985, 0.995) if (r_idx % 2 == 1) else (1.0, 1.0, 1.0)
            self.set_fill_color(*bg)
            self.draw_rect(self.mx, cur_y - 2, self.cw, row_h, fill=True, stroke=False)
            
            cur_x = self.mx + 4
            for c_idx, val in enumerate(r_data):
                f_use = "F2" if (c_idx == 0 or (len(r_data) > 2 and c_idx == len(r_data)-1 and "£" in str(val))) else "F1"
                c_use = (0.08, 0.14, 0.24) if f_use == "F2" else (0.15, 0.20, 0.28)
                self.set_fill_color(*c_use)
                self.draw_text(str(val), cur_x, cur_y + 1.5, font=f_use, size=font_size)
                cur_x += cols[c_idx][1]
                
        self.set_stroke_color(0.08, 0.14, 0.24)
        self.draw_line(self.mx, cur_y - 2, self.width - self.mx, cur_y - 2, stroke_w=1.0)
        return cur_y - 6

    def render(self, page_num, total_pages):
        res = []
        # Background: pure white paper
        res.append(f"1.000 1.000 1.000 rg 0 0 {self.width:.2f} {self.height:.2f} re f")
        
        # Running Footer
        res.append(f"0.70 0.78 0.88 RG 0.5 w {self.mx:.2f} 38.00 m {self.width - self.mx:.2f} 38.00 l S")
        res.append(f"BT /F1 6.2 Tf 0.35 0.40 0.50 rg {self.mx:.2f} 26.00 Td (Working Paper Series in Health Economics & Regulatory Policy  |  Monograph No. 2026-MG-05) Tj ET")
        page_str = f"Page {page_num} of {total_pages}"
        res.append(f"BT /F2 6.5 Tf 0.10 0.15 0.25 rg {self.width - self.mx - 65:.2f} 26.00 Td ({page_str}) Tj ET")
        
        res.extend(self.ops)
        return "\n".join(res)


# --- PAGE 1 ---
def add_p1(pdf):
    p1 = pdf.add_page(is_cover=True)
    
    # Academic Header Masthead
    p1.set_fill_color(0.40, 0.45, 0.55)
    p1.draw_text("WORKING PAPER SERIES IN HEALTH ECONOMICS & REGULATORY POLICY", p1.mx, p1.height - 30, font="F2", size=6.5)
    p1.draw_text("MONOGRAPH NO. 2026-MG-05 // REGULATORY COMPLIANCE DOSSIER", p1.width - p1.mx - 220, p1.height - 30, font="F2", size=6.5)
    
    p1.set_stroke_color(0.08, 0.14, 0.24)
    p1.draw_line(p1.mx, p1.height - 35, p1.width - p1.mx, p1.height - 35, stroke_w=1.0)
    p1.set_stroke_color(0.76, 0.61, 0.22)
    p1.draw_line(p1.mx, p1.height - 38, p1.mx + 80, p1.height - 38, stroke_w=1.5)
    
    # Title & Subtitle
    p1.set_fill_color(0.08, 0.14, 0.24)
    p1.draw_text("CQC PROVIDER & REGISTERED MANAGER REGISTRATION MASTER DOSSIER", p1.mx, p1.height - 52, font="F2", size=11.2)
    p1.set_fill_color(0.35, 0.40, 0.50)
    p1.draw_text("Statutory Application Architecture, Single Assessment Framework Alignment & Fast-Track Commissioning Strategy", p1.mx, p1.height - 64, font="F3", size=7.5)
    
    # Meta Details Box
    cur_ay = p1.height - 72
    p1.set_fill_color(0.985, 0.99, 1.0)
    p1.set_stroke_color(0.70, 0.78, 0.88)
    p1.draw_rect(p1.mx, cur_ay - 48, p1.cw, 48, fill=True, stroke=True, stroke_w=0.6)
    p1.set_fill_color(0.76, 0.61, 0.22)
    p1.draw_rect(p1.mx, cur_ay - 48, 2.5, 48, fill=True)
    
    meta_left = [
        ("Applicant Legal Entity:", "ADOV Care Group LIMITED (Company No. 14289650)"),
        ("Ultimate Parent Group:", "FAIRYTALES GROUP (Trading Name of Mamun Limited)"),
        ("Asset Holding Entity:", "ADOV LIMITED (Freehold Property Company)"),
        ("Operational Campus:", "78 & 80 Marston Gardens, Luton, Bedfordshire, LU2 7DY")
    ]
    meta_right = [
        ("Regulated Activity:", "Personal Care (Supported Living / Use Class C3b)"),
        ("Statutory Standards:", "Health and Social Care Act 2008 & 2014 Regs"),
        ("Strategic Advisory Lead:", "Project Planned by AbdullahMamun.com"),
        ("Dossier Publication Status:", "Print-Ready Scholarly University Edition (Oct 2026)")
    ]
    
    y_m = cur_ay - 11
    for lbl, val in meta_left:
        p1.set_fill_color(0.08, 0.14, 0.24)
        p1.draw_text(lbl, p1.mx + 8, y_m, font="F2", size=6.2)
        p1.set_fill_color(0.25, 0.30, 0.38)
        p1.draw_text(val, p1.mx + 98, y_m, font="F1", size=6.2)
        y_m -= 9
        
    y_m = cur_ay - 11
    for lbl, val in meta_right:
        p1.set_fill_color(0.08, 0.14, 0.24)
        p1.draw_text(lbl, p1.mx + 265, y_m, font="F2", size=6.2)
        p1.set_fill_color(0.25, 0.30, 0.38)
        p1.draw_text(val, p1.mx + 360, y_m, font="F1", size=6.2)
        y_m -= 9
        
    cur_ay -= 54
    
    # Section 1.0 Heading
    cur_ay = p1.draw_section_heading("1.0", "EXECUTIVE SUMMARY & STATUTORY MANDATE", cur_ay)
    
    p1_abstract = (
        "This regulatory monograph establishes the definitive legal, clinical, and financial architecture for the registration of "
        "ADOV Care Group Limited as a CQC-registered provider of Personal Care under the Health and Social Care Act 2008 (Regulated "
        "Activities) Regulations 2014. Operating across 78 and 80 Marston Gardens, Luton, the campus delivers bespoke supported living "
        "for eight working-age adults presenting with severe autism, sensory processing differences, and complex challenging behaviours. "
        "This dossier codifies absolute statutory separation between freehold housing management and regulated care delivery, establishes "
        "fit and proper person credentials for the Nominated Individual and Registered Manager, proves Regulation 13 financial viability "
        "via a ring-fenced £150,000 cash liquidity buffer, and mandates the execution of a Section 28(3) representation waiver to fast-track "
        "commissioning onboarding across Luton Borough Council and the Bedfordshire, Luton and Milton Keynes Integrated Care Board (BLMK ICB)."
    )
    cur_ay = p1.draw_wrapped_text(p1_abstract, p1.mx, cur_ay, p1.cw, font="F1", size=6.7, leading=8.6)
    cur_ay -= 3
    
    # Table 1.0: Core Registration Parameters (Booktabs)
    t1_cols = [("Statutory Dimension", 125), ("Corporate & Clinical Specification", 195), ("Regulatory Assurance & Legal Basis", 195)]
    t1_rows = [
        ("Applicant Legal Entity", "ADOV Care Group LIMITED", "Registered Provider under HSCA 2008 s.10"),
        ("Ultimate Parent Company", "FAIRYTALES GROUP (Mamun Limited)", "100% Shareholder & Financial Sponsor"),
        ("Freehold Property Owner", "ADOV LIMITED (Asset SPV)", "Separate Landlord issuing open-market ASTs"),
        ("Service Delivery Model", "Supported Living (Housing with Care)", "CQC Housing with Care Doctrine Compliant"),
        ("CQC Regulated Activity", "Personal Care (Sole Regulated Activity)", "Health & Social Care Act 2008 Schedule 1"),
        ("Operational Campus", "78 & 80 Marston Gardens, Luton, LU2 7DY", "Class C3b Supported Living (CLEUD s.192)"),
        ("Registered Capacity", "8 Specialist En-Suite Placements (4 + 4)", "Max 6 per house preserves C3b status"),
        ("Clinical Specialism", "Severe Autism, Learning Disability & PBS", "Right Support, Right Care, Right Culture"),
        ("Liquid Working Capital", "£150,000 Ring-Fenced Cash Reserve", "Regulation 13 Financial Viability Mandate"),
        ("Commissioning Target", "Luton DPS (AT1115) & BLMK ICB", "£3,200/bed/wk blended CHC placement fee")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.0: CORE REGISTRATION PARAMETERS & STATUTORY SPECIFICATIONS", t1_cols, t1_rows, cur_ay, row_h=9.6, font_size=5.7)
    cur_ay -= 2
    
    # Strategic Directive Callout
    callout_txt = (
        "STATUTORY BOARD UNDERTAKING // CQC REGISTRATION COMMITMENT: The Board of Directors of FAIRYTALES GROUP and ADOV Care Group LIMITED "
        "hereby unreservedly commits to maintaining absolute regulatory integrity across all operations. The service will strictly adhere "
        "to the Care Quality Commission Fundamental Standards, the Oliver McGowan Code of Practice, and the statutory Housing with Care doctrine, "
        "guaranteeing complete separation between tenancy rights and personal care delivery."
    )
    cur_ay = p1.draw_academic_callout("STATUTORY BOARD UNDERTAKING // CQC REGISTRATION COMMITMENT", callout_txt, cur_ay, h=30)
    cur_ay -= 2
    
    t11_cols = [("Assurance Domain", 125), ("Lead Independent Advisor", 195), ("Statutory Standard / Scope", 195)]
    t11_rows = [
        ("Clinical Governance Lead", "Registered Manager Nominee (Level 5 L&M)", "CQC Regulation 7 & 17 Fit & Proper Standard"),
        ("Corporate Governance Lead", "Nominated Individual / Managing Director", "CQC Regulation 5 & 6 Board Accountability"),
        ("Legal & Tenancy Counsel", "Specialist Healthcare Regulatory Counsel", "CQC Housing with Care & Landlord Separation"),
        ("Chartered Financial Auditor", "Chartered Certified Accountants (FCCA)", "Regulation 13 Financial Viability & Form FV1")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.1: MULTI-DISCIPLINARY REGULATORY ASSURANCE PANEL", t11_cols, t11_rows, cur_ay, row_h=9.4, font_size=5.6)
    cur_ay -= 2
    
    t12_cols = [("Primary Legislation / Regulation", 135), ("Statutory Enactment", 185), ("Regulatory Application to ADOV", 195)]
    t12_rows = [
        ("Health & Social Care Act 2008", "Primary Act of Parliament (c.14)", "Establishes CQC registration & offence regime"),
        ("Regulated Activities Regulations 2014", "Statutory Instrument 2014/2936", "Defines Fundamental Standards (Regs 4 to 20A)"),
        ("CQC (Registration) Regulations 2009", "Statutory Instrument 2009/3112", "Mandates Statement of Purpose & Financial Viability"),
        ("Health and Care Act 2022 s.181", "Statutory Instrument 2022 c.31", "Mandates Tier 1 & 2 Oliver McGowan Training")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.2: PRIMARY STATUTORY CODIFICATION & REGULATORY INSTRUMENTS", t12_cols, t12_rows, cur_ay, row_h=9.4, font_size=5.6)
    cur_ay -= 2
    
    t13_cols = [("Dossier Control Vector", 130), ("Operational Parameter", 195), ("Regulatory Assurance Standard", 190)]
    t13_rows = [
        ("Monograph Version & Status", "Version 2.4 (Definitive Master Dossier)", "Print-Ready Scholarly University Edition"),
        ("Disclosure & Privacy Status", "COMMERCIAL-IN-CONFIDENCE // REGULATORY", "CQC Registration Inspectorate & Board Only"),
        ("Local Authority Jurisdiction", "Luton Borough Council (Bedfordshire)", "DPS Contract AT1115 & Adult Safeguarding"),
        ("Strategic Implementation Target", "16-Week Fast-Track Registration Sequence", "Execution of Section 28(3) Representation Waiver")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.3: MONOGRAPH GOVERNANCE & DOCUMENT CONTROL REGISTER", t13_cols, t13_rows, cur_ay, row_h=9.4, font_size=5.6)
    cur_ay -= 2
    
    t14_cols = [("Statutory Evidence Base", 130), ("Data Source / Benchmark", 195), ("Analytical Objective", 190)]
    t14_rows = [
        ("NHS CHC Tariff Benchmarks", "Bedfordshire ICB Complex Autism Framework", "Validates £3,200/wk fee rate at 100% occupancy"),
        ("Luton Local Plan 2011-2031", "Policies LLP31 & LLP32 (Parking & Access)", "Evidences zero adverse traffic or parking impact"),
        ("HMRC Employment Income Manual", "EIM11300 et seq. (Living Accommodation)", "Certifies complete living accommodation BIK neutrality"),
        ("Building the Right Support Guidance", "DHSC National Service Model Standards", "Mandates community integration & sensory de-escalation"),
        ("Social Value Act 2012 Standards", "Public Services (Social Value) Framework", "Demonstrates local economic and community reinvestment")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.4: STATUTORY EVIDENCE & REGULATORY BENCHMARKING LEDGER", t14_cols, t14_rows, cur_ay, row_h=9.4, font_size=5.6)
    cur_ay -= 2
    
    t15_cols = [("CQC Key Question", 110), ("Regulatory Benchmark Target", 180), ("Statutory Assurance Protocol", 225)]
    rows_t15 = [
        ("1. Safe", "Zero unmanaged safeguarding incidents", "2:1 PBS crisis coverage, robust medication management, L1 fire alarm"),
        ("2. Effective", "100% positive behaviour outcomes", "Tier 2 Oliver McGowan trained staff, person-centred sensory integration"),
        ("3. Caring", "Full dignity, human rights & autonomy", "Article 8 ECHR domestic privacy, absolute resident advocacy empowerment"),
        ("4. Responsive", "Adaptive personalized support plans", "Quarterly multidisciplinary reviews, active family liaison & co-production"),
        ("5. Well-Led", "CQC Outstanding governance rating", "Fit and Proper person verified leadership, digital audit trail, open candour"),
        ("6. Sufficiency Need", "64 out-of-area Luton placements", "Immediate local repatriation pipeline under Luton DPS AT1115 framework"),
        ("7. Oliver McGowan", "100% Tier 2 certified frontline team", "Positive behavioural support & sensory de-escalation embedded"),
        ("8. Fiduciary Solvency", "£150,000 ring-fenced liquid buffer", "Regulation 13 CQC Form FV1 chartered accountant verified solvency")
    ]
    cur_ay = p1.draw_booktabs_table("TABLE 1.5: CQC SINGLE ASSESSMENT FRAMEWORK GOVERNANCE BENCHMARKS", t15_cols, rows_t15, cur_ay, row_h=9.4, font_size=5.6)
    cur_ay -= 3
    p1.set_stroke_color(0.75, 0.80, 0.88)
    p1.draw_line(p1.mx, cur_ay, p1.width - p1.mx, cur_ay, stroke_w=0.6)
    cur_ay -= 8
    p1.set_fill_color(0.35, 0.40, 0.50)
    p1_foot_txt = (
        "STATUTORY METHODOLOGICAL DECLARATION // WORKING PAPER NO. 2026-MG-05: This regulatory monograph has been prepared in accordance "
        "with the Health and Social Care Act 2008, CQC Single Assessment Framework guidance, and HM Treasury Green Book appraisal principles. "
        "All clinical and financial models have been independently certified for CQC Provider Portal submission and senior lender underwriting."
    )
    cur_ay = p1.draw_wrapped_text(p1_foot_txt, p1.mx, cur_ay, p1.cw, font="F3", size=5.5, leading=7.2)
    print("Page 1 final y =", cur_ay)
    return p1


# --- PAGE 2 ---
def add_p2(pdf):
    p2 = pdf.add_page()
    p2.draw_academic_header("SECTION 2.0", "HOUSING VS CARE STATUTORY SEPARATION")
    
    y = p2.height - 48
    y = p2.draw_section_heading("2.0", "STATUTORY SEPARATION: HOUSING MANAGEMENT VS PERSONAL CARE", y)
    
    p2_txt = (
        "Under the Health and Social Care Act 2008 (Regulated Activities) Regulations 2014, operating an unregistered care home "
        "constitutes a strict liability criminal offence under Section 10 of the Act. The Care Quality Commission's statutory guidance, "
        "'Housing with Care' (October 2015, updated under the Single Assessment Framework), establishes that supported living schemes "
        "remain lawfully classified as housing rather than a care home only if there is a real, operational, and legal separation "
        "between the provision of accommodation (housing management) and the delivery of regulated personal care."
    )
    y = p2.draw_wrapped_text(p2_txt, p2.mx, y, p2.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    y = p2.draw_section_heading("2.1", "Tripartite Corporate Architecture & Landlord-Provider Decoupling", y)
    p2_tri = (
        "FAIRYTALES GROUP enforces statutory non-contamination through two distinct corporate entities: ADOV LIMITED (Asset SPV), "
        "which owns the freeholds of 78 and 80 Marston Gardens and acts exclusively as commercial landlord issuing open-market Assured "
        "Shorthold Tenancies (ASTs); and ADOV Care Group LIMITED (Care OpCo), which applies solely for the regulated activity of Personal Care. "
        "Tenants possess exclusive possession of their private en-suite accommodation and can freely change care providers without losing their home."
    )
    y = p2.draw_wrapped_text(p2_tri, p2.mx, y, p2.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # FIGURE 1: VECTOR SCHEMATIC (INK-FRIENDLY)
    p2.set_fill_color(0.08, 0.14, 0.24)
    p2.draw_text("FIGURE 1: STATUTORY SEPARATION ARCHITECTURE // HOUSING SPV VS CARE OPCO", p2.mx, y, font="F2", size=7.2)
    y -= 5
    
    fig1_h = 96
    fig1_y = y - fig1_h
    p2.set_fill_color(0.99, 0.995, 1.0)
    p2.set_stroke_color(0.70, 0.78, 0.88)
    p2.draw_rect(p2.mx, fig1_y, p2.cw, fig1_h, fill=True, stroke=True, stroke_w=0.8)
    
    # Top Parent Box
    bw_top = 180
    bh_top = 20
    bx_top = p2.mx + p2.cw/2 - bw_top/2
    by_top = fig1_y + fig1_h - 23
    p2.set_fill_color(0.96, 0.97, 0.99)
    p2.set_stroke_color(0.20, 0.25, 0.35)
    p2.draw_rect(bx_top, by_top, bw_top, bh_top, fill=True, stroke=True, stroke_w=0.8)
    p2.set_fill_color(0.08, 0.14, 0.24)
    p2.draw_text("FAIRYTALES GROUP (HOLDING COMPANY)", bx_top + 10, by_top + 11.5, font="F2", size=6.8)
    p2.set_fill_color(0.40, 0.45, 0.55)
    p2.draw_text("100% Shareholder & Capital Sponsor", bx_top + 28, by_top + 3.5, font="F1", size=5.8)
    
    # Left Box: Housing PropCo
    bw_sub = 220
    bh_sub = 50
    bx_prop = p2.mx + 15
    by_sub = fig1_y + 14
    p2.set_fill_color(0.97, 0.98, 1.0)
    p2.set_stroke_color(0.10, 0.25, 0.45)
    p2.draw_rect(bx_prop, by_sub, bw_sub, bh_sub, fill=True, stroke=True, stroke_w=0.8)
    p2.set_fill_color(0.10, 0.25, 0.45)
    p2.draw_text("HOUSING ASSET SPV: ADOV LIMITED", bx_prop + 8, by_sub + bh_sub - 11, font="F2", size=6.8)
    p2.set_fill_color(0.25, 0.30, 0.38)
    p2.draw_text("- Freehold Owner of 78 & 80 Marston Gardens", bx_prop + 8, by_sub + bh_sub - 20, font="F1", size=5.8)
    p2.draw_text("- Issues Assured Shorthold Tenancies (ASTs)", bx_prop + 8, by_sub + bh_sub - 29, font="F1", size=5.8)
    p2.draw_text("- Collects £350/wk Housing Benefit Exempt Rent", bx_prop + 8, by_sub + bh_sub - 38, font="F1", size=5.8)
    p2.set_fill_color(0.12, 0.45, 0.22)
    p2.draw_text("Landlord Function Only // Unregulated Entity", bx_prop + 8, by_sub + bh_sub - 47, font="F2", size=5.8)
    
    # Right Box: Regulated Care OpCo
    bx_opco = p2.mx + p2.cw - bw_sub - 15
    p2.set_fill_color(0.98, 0.96, 0.96)
    p2.set_stroke_color(0.65, 0.20, 0.20)
    p2.draw_rect(bx_opco, by_sub, bw_sub, bh_sub, fill=True, stroke=True, stroke_w=0.8)
    p2.set_fill_color(0.65, 0.20, 0.20)
    p2.draw_text("REGULATED CARE OPCO: ADOV CARE GROUP LTD", bx_opco + 8, by_sub + bh_sub - 11, font="F2", size=6.8)
    p2.set_fill_color(0.35, 0.20, 0.20)
    p2.draw_text("- CQC Applicant for Regulated Activity: Personal Care", bx_opco + 8, by_sub + bh_sub - 20, font="F1", size=5.8)
    p2.draw_text("- Individual Support & PBS Service Contracts", bx_opco + 8, by_sub + bh_sub - 29, font="F1", size=5.8)
    p2.draw_text("- Commissioned by Luton DPS & BLMK ICB (£3,200/wk)", bx_opco + 8, by_sub + bh_sub - 38, font="F1", size=5.8)
    p2.set_fill_color(0.10, 0.25, 0.45)
    p2.draw_text("Regulated Provider Only // Zero Tenancy Control", bx_opco + 8, by_sub + bh_sub - 47, font="F2", size=5.8)
    
    # Center Demarcation Line
    p2.set_stroke_color(0.76, 0.61, 0.22)
    p2.draw_line(p2.mx + p2.cw/2, by_sub - 2, p2.mx + p2.cw/2, by_top - 2, stroke_w=1.0)
    
    # Bottom Result Banner
    p2.set_fill_color(0.94, 0.96, 0.98)
    p2.set_stroke_color(0.76, 0.61, 0.22)
    p2.draw_rect(p2.mx + 15, fig1_y + 3, p2.cw - 30, 8.5, fill=True, stroke=True, stroke_w=0.5)
    p2.set_fill_color(0.08, 0.14, 0.24)
    p2.draw_text("CQC HOUSING WITH CARE DOCTRINE: ABSOLUTE SEPARATION PREVENTS UNREGISTERED CARE HOME OFFENCE (HSCA 2008 s.10)", p2.mx + 20, fig1_y + 5.5, font="F2", size=5.5)
    
    y = fig1_y - 6
    
    # Table 2.0: Demarcation Matrix
    cols_t20 = [("Operational Function", 125), ("ADOV LIMITED (Housing SPV)", 195), ("ADOV Care Group LIMITED (Care OpCo)", 195)]
    rows_t20 = [
        ("Primary Legal Instrument", "Assured Shorthold Tenancy (AST) Agreement", "Regulated Personal Care & Support Contract"),
        ("Remuneration / Funding", "Exempt Accommodation Housing Benefit (£350/wk)", "NHS Continuing Healthcare (CHC) / Luton Council (£3,200/wk)"),
        ("Premises Maintenance", "Structural maintenance, gas safety, roof, windows", "Sensory calming pods, PBS de-escalation equipment"),
        ("Key Governance Control", "Tenants hold exclusive possession & locking doors", "Care delivery tailored to assessed needs; zero eviction powers"),
        ("Provider Substitution", "Tenant retains tenancy if care provider changes", "Care package re-tenderable without jeopardizing accommodation")
    ]
    y = p2.draw_booktabs_table("TABLE 2.0: HOUSING MANAGEMENT VS REGULATED PERSONAL CARE DEMARCATION", cols_t20, rows_t20, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 2.1: AST vs Care Plan Separation
    cols_t21 = [("Statutory Document", 125), ("Governing Legislation", 195), ("Mandatory Statutory Safeguard", 195)]
    rows_t21 = [
        ("Tenancy Agreement (AST)", "Housing Act 1988 & Landlord and Tenant Act 1985", "Guarantees quiet enjoyment, tenant rights, standard notice periods"),
        ("Care & Support Plan", "Health & Social Care Act 2008 (Regs 9 & 12)", "Person-centred care plan co-produced with resident & family"),
        ("De-Linking Clause", "CQC Housing with Care Guidance (October 2015)", "Explicit covenant: care contract termination does not terminate AST")
    ]
    y = p2.draw_booktabs_table("TABLE 2.1: TENANCY AGREEMENT (AST) VS CARE PLAN STATUTORY SEPARATION", cols_t21, rows_t21, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 2.2: Town Planning Use Class C3b vs C2
    cols_t22 = [("Town Planning Vector", 125), ("Statutory Standard (Class C3b)", 195), ("Operational Application to 78 & 80 Marston", 195)]
    rows_t22 = [
        ("Use Classes Order 1987", "Town and Country Planning (Use Classes) Order 1987", "Class C3b permits up to 6 residents living as single household"),
        ("Case Law Authority", "North Devon DC v First Secretary of State [2004]", "Confirmed carer presence does not convert C3b into institutional C2"),
        ("Luton Council CLEUD", "Section 192 Town and Country Planning Act 1990", "CLEUD certificate confirms permitted development; zero planning risk")
    ]
    y = p2.draw_booktabs_table("TABLE 2.2: TOWN PLANNING USE CLASS C3b VS C2 STATUTORY COMPLIANCE", cols_t22, rows_t22, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 2.3: Exempt Accommodation Rent Justification
    cols_t23 = [("Exempt Rent Element", 125), ("Weekly Rent Benchmark", 195), ("Housing Benefit Statutory Justification", 195)]
    rows_t23 = [
        ("Core Accommodation Rent", "£185.00 / bed / week", "Based on open market capital value of high-specification bedrooms"),
        ("Intensive Housing Management", "£125.00 / bed / week", "Covers 24/7 building security, higher wear & tear, concierge oversight"),
        ("Specialist Communal Facilities", "£40.00 / bed / week", "Depreciation of communal sensory gardens, lounges, commercial laundry"),
        ("Total Eligible Housing Cost", "£350.00 / bed / week", "Fully verified under Housing Benefit (General) Regs 2006 Schedule 1")
    ]
    y = p2.draw_booktabs_table("TABLE 2.3: EXEMPT ACCOMMODATION HOUSING BENEFIT COST BREAKDOWN", cols_t23, rows_t23, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 2.4: Dual Contract Safeguards
    cols_t24 = [("Safeguard Vector", 125), ("Statutory Standard / Instrument", 195), ("Operational Assurance at Marston Campus", 195)]
    rows_t24 = [
        ("Independent Advocacy Representation", "Care Act 2014 Section 67", "Luton Independent Advocacy Partnership appointed for all tenants"),
        ("Separate Invoicing Streams", "Consumer Rights Act 2015", "Housing Benefit pays Landlord; ICB/Luton pays Care OpCo directly"),
        ("Absolute Tenancy Continuity", "Housing Act 1988 Part 1", "Tenancy remains secure even if care contract is varied or terminated"),
        ("Resident Keyholder Autonomy", "Article 8 ECHR & Reg 10 HSCA", "Residents hold front door keys & lockable private bedroom access")
    ]
    y = p2.draw_booktabs_table("TABLE 2.4: DUAL CONTRACT SAFEGUARDS & INDEPENDENT ADVOCACY AUDIT", cols_t24, rows_t24, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 2.5: Intensive Housing Management (IHM) Breakdown
    cols_t25 = [("IHM Service Component", 125), ("Housing Benefit Eligibility Classification", 195), ("Weekly Allocation / Resident", 195)]
    rows_t25 = [
        ("24/7 Concierge & Security Oversight", "Eligible Housing Management Charge", "£55.00 / week (CCTV, access control & intercom)"),
        ("Enhanced Fabric Maintenance Reserve", "Eligible Property Sinking Fund", "£40.00 / week (Cyclic repairs for complex sensory needs)"),
        ("Communal Utilities & Tenancy Liaison", "Eligible Communal & Housing Support", "£75.00 / week (Sensory grounds & council tax interface)")
    ]
    y = p2.draw_booktabs_table("TABLE 2.5: INTENSIVE HOUSING MANAGEMENT (IHM) SERVICE CHARGE SCHEDULE", cols_t25, rows_t25, y, row_h=9.4, font_size=5.6)
    y -= 2

    # Table 2.6: CQC Housing with Care Checklist
    cols_t26 = [("CQC Inspection Focus", 125), ("Housing with Care Statutory Benchmark", 195), ("Auditable Document at Marston Gardens", 195)]
    rows_t26 = [
        ("Provider Choice Freedom", "Tenant free to select alternative domiciliary care", "CQC Statement of Purpose & Resident Welcome Charter"),
        ("Domestic Non-Clinical Ambience", "Zero institutional signage or hospital features", "Domestic furniture, sensory acoustic panelling throughout"),
        ("Office Function Demarcation", "Care office separate from housing management", "Dedicated staff break hub decoupled from tenant living areas")
    ]
    y = p2.draw_booktabs_table("TABLE 2.6: CQC HOUSING WITH CARE STATUTORY INSPECTION CHECKLIST", cols_t26, rows_t26, y, row_h=9.4, font_size=5.6)
    y -= 2

    # Table 2.7: Human Rights Act & Article 8 ECHR
    cols_t27 = [("Human Rights Vector", 125), ("Article 8 Statutory Standard", 195), ("Campus Operational Mechanism", 195)]
    rows_t27 = [
        ("Right to Private Life & Sanctum", "Unrestricted family contact and bedroom privacy", "Zero institutional curfews; private lockable en-suites"),
        ("Respect for the Domestic Home", "Staff must knock and obtain consent prior to entry", "Mandatory staff entry protocol codified in handbook")
    ]
    y = p2.draw_booktabs_table("TABLE 2.7: HUMAN RIGHTS ACT 1998 (ARTICLE 8) & DOMESTIC PRIVACY AUDIT", cols_t27, rows_t27, y, row_h=9.4, font_size=5.6)
    y -= 2

    p2_callout = (
        "STATUTORY NON-CONTAMINATION GUARANTEE: ADOV Care Group Limited certifies that housing management and care delivery are legally "
        "and operationally autonomous. Supported living residents sign independent ASTs with ADOV LIMITED and hold statutory security of tenure. "
        "Personal care is delivered under a distinct contract, guaranteeing zero risk of an unregistered care home prosecution under HSCA 2008 s.10."
    )
    y = p2.draw_academic_callout("STATUTORY NON-CONTAMINATION GUARANTEE", p2_callout, y, h=30)
    print("Page 2 final y =", y)
    return p2


# --- PAGE 3 ---
def add_p3(pdf):
    p3 = pdf.add_page()
    p3.draw_academic_header("SECTION 3.0", "PRIMARY LEGISLATION & STATUTORY REGULATIONS")
    
    y = p3.height - 48
    y = p3.draw_section_heading("3.0", "PRIMARY LEGISLATION & REGULATORY COMPLIANCE ARCHITECTURE", y)
    
    p3_txt = (
        "Operating as a registered social care provider in England requires rigorous, verifiable compliance with an intricate hierarchy "
        "of primary and secondary legislation. The regulatory architecture governing ADOV Care Group Limited is established under Part 1 of "
        "the Health and Social Care Act 2008, codified through the Health and Social Care Act 2008 (Regulated Activities) Regulations 2014 "
        "(Statutory Instrument 2014/2936), the Care Quality Commission (Registration) Regulations 2009 (SI 2009/3112), and the mandatory "
        "training provisions enacted under Section 181 of the Health and Care Act 2022."
    )
    y = p3.draw_wrapped_text(p3_txt, p3.mx, y, p3.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # Table 3.0: 2014 Regulations Master Ledger (12 Fundamental Standards)
    cols_t30 = [("2014 Regulation", 115), ("Statutory Standard / Title", 165), ("Operational Assurance & Clinical Implementation", 235)]
    rows_t30 = [
        ("Regulation 9", "Person-Centred Care", "Individual PBS care plans co-produced with resident, family & clinical specialists."),
        ("Regulation 10", "Dignity and Respect", "Private lockable en-suites, domestic environment, absolute Article 8 ECHR autonomy."),
        ("Regulation 11", "Need for Consent", "Two-stage mental capacity assessments; Best Interests balance sheets under s.4 MCA 2005."),
        ("Regulation 12", "Safe Care and Treatment", "Certified Restraint Reduction Network breakaway training; clinical risk assessments."),
        ("Regulation 13", "Safeguarding from Abuse", "Zero-tolerance abuse policy; mandatory multi-agency Section 42 Care Act reporting."),
        ("Regulation 14", "Nutrition and Hydration", "Speech and Language Therapy (SALT) approved modified diets, IDDSI framework."),
        ("Regulation 15", "Premises and Equipment", "Part B L1 fire loop, acoustic RW3 insulation, specialist DDA wetrooms at 80 Marston."),
        ("Regulation 16", "Complaints Handling", "Accessible pictorial complaints procedure; guaranteed 20-day formal investigation."),
        ("Regulation 17", "Good Governance", "Independent monthly Regulation 17 clinical quality audits; digital incident logs."),
        ("Regulation 18", "Staffing Rota Sufficiency", "2:1 daytime staffing; unified 1 Waking + 1 Sleep-in night hub across 78 & 80 Marston."),
        ("Regulation 19", "Fit & Proper Staff Employed", "Enhanced DBS with barred list check, 2 professional references, verified work history."),
        ("Regulation 20", "Duty of Candour", "Written statutory notification and apology within 10 days of any notifiable safety incident.")
    ]
    y = p3.draw_booktabs_table("TABLE 3.0: HEALTH AND SOCIAL CARE ACT 2008 (REGULATED ACTIVITIES) REGULATIONS 2014 COMPLIANCE LEDGER", cols_t30, rows_t30, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    y = p3.draw_section_heading("3.1", "CQC Enforcement Hierarchy & Criminal Offence Thresholds", y)
    p3_enf_txt = (
        "Breaches of the Fundamental Standards carry immediate statutory penalties. Regulations 11, 12, 13(1-4), 14, 16(3), 17(3), "
        "and 20 constitute prosecutable criminal offences under Regulation 22 without prior warning notice requirements. ADOV Care Group "
        "maintains defensible clinical audit trails and statutory policies that guarantee complete legal and operational compliance."
    )
    y = p3.draw_wrapped_text(p3_enf_txt, p3.mx, y, p3.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # Table 3.1: Enforcement Powers
    cols_t31 = [("CQC Enforcement Tool", 125), ("Statutory Trigger Level", 195), ("Corporate Mitigation & Defence Protocol", 195)]
    rows_t31 = [
        ("Section 29 Warning Notice", "Identified breach of Regulations 9-19", "Immediate 14-day rectification plan overseen by Nominated Individual"),
        ("Section 31 Urgent Condition", "Serious risk to life, health or well-being", "Pre-emptive 2:1 staffing ratios and live CCTV monitoring of common areas"),
        ("Section 30 Urgent Cancellation", "Critical systemic failure or harm", "Dual-registered clinical manager governance preventing single-point failure"),
        ("Regulation 22 Prosecution", "Strict liability breach of criminal regulations", "Comprehensive auditable policies establishing all reasonable precautions defence")
    ]
    y = p3.draw_booktabs_table("TABLE 3.1: CQC ENFORCEMENT HIERARCHY & STATUTORY DEFENCE MECHANISMS", cols_t31, rows_t31, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 3.2: Oliver McGowan
    cols_t32 = [("Oliver McGowan Tier", 125), ("Statutory Standard (HCA 2022 s.181)", 195), ("Mandatory Compliance Cadence at ADOV", 195)]
    rows_t32 = [
        ("Tier 1: General Awareness", "All non-care staff (admin, maintenance)", "Completed within 30 days of appointment; annual refresh"),
        ("Tier 2: Direct Care Practice", "All frontline support workers, RM, and NI", "1-day interactive session co-delivered by experts with lived experience"),
        ("PBS & Restraint Reduction", "BILD certified Positive Behavioural Support", "Mandatory pre-placement induction; bi-annual practical breakaway drills")
    ]
    y = p3.draw_booktabs_table("TABLE 3.2: HEALTH AND CARE ACT 2022 SECTION 181 OLIVER MCGOWAN MANDATE", cols_t32, rows_t32, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 3.3: MCA & Safeguarding
    cols_t33 = [("Legislative Instrument", 125), ("Statutory Standard / Scope", 195), ("Campus Governance Standard", 195)]
    rows_t33 = [
        ("Mental Capacity Act 2005", "Presumption of capacity; Section 4 Best Interests", "Formal MCA assessments documented on digital clinical portal"),
        ("Care Act 2014 (Section 42)", "Duty to make safeguarding enquiries", "Immediate 2-hour notification to Luton Safeguarding Adults Board"),
        ("Deprivation of Liberty (DoLS)", "Article 5 ECHR lawful detention review", "Pre-placement DoLS applications submitted to Luton Supervisory Body")
    ]
    y = p3.draw_booktabs_table("TABLE 3.3: MENTAL CAPACITY ACT 2005 & SECTION 42 SAFEGUARDING GOVERNANCE", cols_t33, rows_t33, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p3.draw_section_heading("3.2", "CQC (Registration) Regulations 2009 Statutory Notifications (Reg 12-19)", y)
    p3_reg09_txt = (
        "The CQC (Registration) Regulations 2009 (SI 2009/3112) impose strict statutory notification duties on the Registered Manager "
        "and Nominated Individual. Failure to notify the Commission without delay constitutes a summary criminal offence punishable "
        "by fixed penalty notice or prosecution under Regulation 25."
    )
    y = p3.draw_wrapped_text(p3_reg09_txt, p3.mx, y, p3.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 3.4: 2009 Notifications
    cols_t34 = [("2009 Regulation", 100), ("Statutory Trigger Event", 190), ("Mandatory Notification Protocol & Timeline", 225)]
    rows_t34 = [
        ("Regulation 12", "Statement of Purpose Variation", "28 days prior written notification submitted via CQC Provider Portal"),
        ("Regulation 14", "Registered Manager Absence >28 Days", "Written notice prior to planned leave; emergency notice within 5 days"),
        ("Regulation 15", "Corporate Officer / Director Change", "14 days statutory notice of appointment, cessation, or address update"),
        ("Regulation 16", "Death of Service User", "Immediate electronic notification to CQC without delay; Coroner liaison"),
        ("Regulation 18(2)(a)", "Serious Injury to Service User", "Immediate SN18 notice for fractures, burns, deep lacerations or sensory loss"),
        ("Regulation 18(2)(e)", "Allegation of Abuse or Neglect", "Immediate notification to CQC, Police, and Luton Safeguarding Adults Board")
    ]
    y = p3.draw_booktabs_table("TABLE 3.4: CQC (REGISTRATION) REGULATIONS 2009 STATUTORY NOTIFICATION LEDGER", cols_t34, rows_t34, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p3.draw_section_heading("3.3", "Care Act 2014 & Public Sector Equality Duty (Equality Act 2010)", y)
    p3_care_txt = (
        "Statutory integration under Section 3 of the Care Act 2014 mandates active partnership with the Bedfordshire, Luton and Milton "
        "Keynes ICB and local NHS Trusts. In parallel, Section 149 of the Equality Act 2010 and the NHS Accessible Information Standard "
        "require proactive reasonable adjustments, easy-read care plans, and specialized sensory communication tools."
    )
    y = p3.draw_wrapped_text(p3_care_txt, p3.mx, y, p3.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 3.5: Care Act 2014 Duties
    cols_t35 = [("Care Act 2014 Section", 125), ("Statutory Standard / Principle", 195), ("Campus Operational Assurance Standard", 195)]
    rows_t35 = [
        ("Section 1 (Wellbeing Duty)", "Promoting individual dignity, control & wellbeing", "Person-centred outcomes tracked via daily digital support logs"),
        ("Section 3 (Care Integration)", "Duty to integrate health, social care & housing", "Integrated working with Luton community learning disability teams"),
        ("Section 9 (Needs Assessment)", "Eligibility & multi-disciplinary care assessment", "Robust pre-admission compatibility screening protocol"),
        ("Section 42 (Safeguarding)", "Multi-agency adult protection enquiry mandate", "Designated Safeguarding Lead with 24/7 incident response capability")
    ]
    y = p3.draw_booktabs_table("TABLE 3.5: CARE ACT 2014 STATUTORY PRINCIPLES & WELLBEING ALIGNMENT", cols_t35, rows_t35, y, row_h=9.4, font_size=5.6)
    y -= 3

    # Table 3.6: Equality Act 2010
    cols_t36 = [("Equality & Information Vector", 125), ("Statutory Standard (s.149 / AIS)", 195), ("Operational Mechanism at Marston Gardens", 195)]
    rows_t36 = [
        ("Protected Characteristics", "Zero discrimination based on disability, race, religion", "Inclusive admissions policy & cultural diversity support plans"),
        ("Accessible Information Standard", "Mandatory easy-read and non-verbal formats", "PECS visual cards, Makaton signage, and sensory touch boards"),
        ("Reasonable Adjustments Duty", "Anticipatory environmental adaptations", "Acoustic stud lining, circadian lighting, and weighted sensory tools")
    ]
    y = p3.draw_booktabs_table("TABLE 3.6: PUBLIC SECTOR EQUALITY DUTY & ACCESSIBLE INFORMATION AUDIT", cols_t36, rows_t36, y, row_h=9.4, font_size=5.6)
    y -= 2

    p3_callout = (
        "STATUTORY REGULATORY UNDERTAKING // ZERO COMPLIANCE DEFICIT: ADOV Care Group Limited operates in strict accordance with the "
        "Health and Social Care Act 2008 and the 2014 Regulated Activities Regulations. Every fundamental standard is embedded into "
        "daily shift routines, supervised by a qualified Level 5 Registered Manager, and audited quarterly by an independent care governance inspector."
    )
    y = p3.draw_academic_callout("STATUTORY REGULATORY UNDERTAKING // ZERO COMPLIANCE DEFICIT", p3_callout, y, h=30)
    print("Page 3 final y =", y)
    return p3


# --- PAGE 4 ---
def add_p4(pdf):
    p4 = pdf.add_page()
    p4.draw_academic_header("SECTION 4.0", "STATEMENT OF PURPOSE (SoP) MASTER SPECIFICATION")
    
    y = p4.height - 48
    y = p4.draw_section_heading("4.0", "CQC STATEMENT OF PURPOSE MASTER SPECIFICATION (REGULATION 12)", y)
    
    p4_txt = (
        "Under Regulation 12 of the Care Quality Commission (Registration) Regulations 2009, every registered provider must compile "
        "and maintain an accurate Statement of Purpose (SoP). The Statement of Purpose represents a legally binding statutory contract "
        "between the provider, the Commission, service users, and commissioning bodies. Operating outside the stated scope, client bands, "
        "or registered locations constitutes a criminal offence under Section 10 of the Health and Social Care Act 2008."
    )
    y = p4.draw_wrapped_text(p4_txt, p4.mx, y, p4.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    y = p4.draw_section_heading("4.1", "The Four-Part Statutory Architecture (CQC Prescribed Format)", y)
    p4_arch_txt = (
        "The Commission prescribes a rigid four-part structure for the Statement of Purpose: Part 1 (Provider Details), Part 2 (Aims and "
        "Objectives), Part 3 (Location Details), and Part 4 (Registered Manager and Nominated Individual details). The specifications below "
        "reflect the final, validated submission entries uploaded to the CQC Provider Portal."
    )
    y = p4.draw_wrapped_text(p4_arch_txt, p4.mx, y, p4.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # Table 4.0: SoP Parts 1 & 2
    cols_t40 = [("SoP Dimension", 125), ("Statutory Portal Specification", 195), ("Regulatory Assurance & Legal Basis", 195)]
    rows_t40 = [
        ("Part 1: Legal Entity Name", "ADOV Care Group LIMITED (Co. No. 14289650)", "Private limited company incorporated in England & Wales"),
        ("Part 1: Provider Address", "78 Marston Gardens, Luton, Bedfordshire, LU2 7DY", "Principal registered office & operational headquarters"),
        ("Part 2: Core Service Aims", "High-dependency supported living for autistic adults", "Aligns with Right Support, Right Care, Right Culture"),
        ("Part 2: Therapeutic Ethos", "Positive Behavioural Support (PBS) & sensory integration", "Restraint Reduction Network (RRN) compliant culture"),
        ("Part 2: Regulated Activity", "Personal Care (Sole regulated activity applied for)", "Health and Social Care Act 2008 Schedule 1 Part 1")
    ]
    y = p4.draw_booktabs_table("TABLE 4.0: STATEMENT OF PURPOSE PART 1 (PROVIDER) & PART 2 (AIMS & OBJECTIVES)", cols_t40, rows_t40, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 4.1: SoP Part 3 Location
    cols_t41 = [("Location Parameter", 125), ("Campus Specification (78 & 80 Marston Gardens)", 195), ("Environmental & Statutory Standard", 195)]
    rows_t41 = [
        ("Registered Location Name", "Marston Gardens Supported Living Campus", "Unified location comprising contiguous 78 and 80"),
        ("Accommodation Capacity", "8 Specialist En-Suite Bedrooms (4 in 78, 4 in 80)", "Individual private tenancies under Class C3b (CLEUD s.192)"),
        ("Communal Therapeutic Space", "Sensory calming suite, life skills kitchen, lounge", "Acoustically isolated; tunable circadian LED lighting"),
        ("External Amenity Curtilage", "24.5m secure south-facing enclosed garden", "2.1m acoustic timber fencing; de-escalation zones"),
        ("Fire & Building Safety", "Integrated Cat L1 addressable loop across 78 & 80", "FD30S fire doors, emergency lighting, Part B compliant")
    ]
    y = p4.draw_booktabs_table("TABLE 4.1: STATEMENT OF PURPOSE PART 3 (LOCATION SPECIFICATION & ENVIRONMENTAL SCHEDULE)", cols_t41, rows_t41, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 4.2: SoP Part 4 Governance
    cols_t42 = [("Statutory Role (Part 4)", 125), ("Designated Individual & Credentials", 195), ("Statutory Fitness & CQC Experience", 195)]
    rows_t42 = [
        ("Nominated Individual (Reg 6)", "Director / Operations Lead (FAIRYTALES GROUP)", "Supervises management; direct accountability to Board"),
        ("Registered Manager (Reg 7)", "Level 5 Diploma in Leadership for Health & Social Care", "12 years autism experience; certified PBS practitioner"),
        ("Clinical Governance Lead", "Independent Nurse Consultant (Learning Disability)", "Conducts quarterly external Regulation 17 clinical audits")
    ]
    y = p4.draw_booktabs_table("TABLE 4.2: STATEMENT OF PURPOSE PART 4 (NOMINATED INDIVIDUAL & REGISTERED MANAGER)", cols_t42, rows_t42, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    y = p4.draw_section_heading("4.2", "Service User Bands, Inclusion Criteria & Compatibility Screening", y)
    p4_user_txt = (
        "The Statement of Purpose explicitly circumscribes the service user band to adults aged 18 to 65 presenting with a primary diagnosis "
        "of autism spectrum condition, learning disabilities, and associated sensory processing sensitivities. A rigorous pre-admission "
        "compatibility screening protocol ensures that newly admitted tenants harmonize with existing residents."
    )
    y = p4.draw_wrapped_text(p4_user_txt, p4.mx, y, p4.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # Table 4.3: Inclusion / Exclusion
    cols_t43 = [("Clinical Assessment Category", 125), ("Mandatory Admission Criteria", 195), ("Absolute Exclusion Threshold", 195)]
    rows_t43 = [
        ("Primary Diagnostic Profile", "Diagnosis of autism, Asperger's, or learning disability", "Primary dementia, organic brain injury, or acute psychosis"),
        ("Behavioural Presentation", "Behaviours of concern manageable via Tier 2 PBS plans", "Active arson, unmanageable sexual offending, weapon use"),
        ("Substance Use & Addictions", "Zero tolerance; voluntary substance-free lifestyle", "Active alcohol or illicit substance dependency"),
        ("Age Range & Legal Status", "Working-age adults (18 - 65 years); informal or DoLS", "Individuals detained under Section 3 Mental Health Act 1983")
    ]
    y = p4.draw_booktabs_table("TABLE 4.3: SERVICE USER INCLUSION, COMPATIBILITY & EXCLUSION MATRIX", cols_t43, rows_t43, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 4.4: Transition Pathway
    cols_t44 = [("Transition Stage", 110), ("Statutory Protocol & Actions", 205), ("Lead Decision-Maker / Sign-Off", 200)]
    rows_t44 = [
        ("Stage 1: Pre-Admission Referral", "Multi-disciplinary review of EHCP, PBS plan & CHC notes", "Registered Manager & Nominated Individual"),
        ("Stage 2: Sensory Compatibility", "Day visits, tea visits, sensory profile assessment", "Specialist PBS Lead & Existing Tenants"),
        ("Stage 3: AST & Care Contract", "Separate execution of AST with PropCo & care agreement", "Resident Advocate (IMCA) & Legal Lead"),
        ("Stage 4: Phased Move-In (Wk 1-4)", "Gradual transition; 2:1 dedicated keyworker support", "Registered Manager & Luton Social Worker")
    ]
    y = p4.draw_booktabs_table("TABLE 4.4: FOUR-STAGE PLANNED TRANSITION PATHWAY & ADMISSION PROTOCOL", cols_t44, rows_t44, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 4.5: Physical Safety Standards
    cols_t45 = [("Environmental Fixture", 125), ("Specialist Autism Specification", 195), ("Building Regs & Health & Safety Mandate", 195)]
    rows_t45 = [
        ("Anti-Ligature Ironmongery", "Concealed hinges, load-release anti-ligature door handles", "Health and Safety Executive (HSE) guidance compliance"),
        ("Thermostatic Mixing Valves", "Type 3 TMV blending valves capping hot water at 41C", "Approved Document G & Regulation 15 HSE anti-scalding"),
        ("Acoustic Flanking Dampening", "Rockwool RW3 insulation in party walls (>55dB rating)", "Approved Document E (Resistance to the passage of sound)")
    ]
    y = p4.draw_booktabs_table("TABLE 4.5: SPECIALIST ENVIRONMENTAL SAFETY STANDARDS & PREMISES AUDIT", cols_t45, rows_t45, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p4.draw_section_heading("4.3", "Right Support, Right Care, Right Culture (RSRCRC) Statutory Benchmarking", y)
    p4_rsrcrc_txt = (
        "CQC's 'Right Support, Right Care, Right Culture' guidance underpins all registration assessments for autism and learning disability "
        "services. 78 and 80 Marston Gardens embodies this doctrine by providing small-scale, domestic homes within an ordinary suburban "
        "community, completely avoiding institutional congregate care models."
    )
    y = p4.draw_wrapped_text(p4_rsrcrc_txt, p4.mx, y, p4.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 4.6: RSRCRC Matrix
    cols_t46 = [("RSRCRC Core Principle", 125), ("Statutory Intent & CQC Expectation", 195), ("Campus Implementation (78 & 80 Marston)", 195)]
    rows_t46 = [
        ("Right Support (Design & Model)", "Location and design promote choice, control and local inclusion", "Small 4-bed domestic houses in suburban street; zero clinical signage"),
        ("Right Care (Person-Centred)", "Care promotes dignity, human rights, autonomy and equality", "Independent advocacy, co-produced PBS plans, locking private en-suites"),
        ("Right Culture (Staff Values)", "Staff embody empathy, respect, and positive behavioural ethos", "100% Tier 2 Oliver McGowan trained team, active candour, zero blame"),
        ("Personal Emergency Evacuation", "Individual PEEP schedules tailored to sensory panic triggers", "Progressive horizontal evacuation across 30-min fire compartment zones")
    ]
    y = p4.draw_booktabs_table("TABLE 4.6: RIGHT SUPPORT, RIGHT CARE, RIGHT CULTURE STATUTORY ALIGNMENT", cols_t46, rows_t46, y, row_h=9.4, font_size=5.6)
    y -= 2

    cols_t47 = [("Engagement Channel", 125), ("Cadence", 80), ("Statutory Assurance & Co-Production Objective", 310)]
    rows_t47 = [
        ("Resident House Meetings", "Bi-Weekly", "Empowers resident choices regarding meals, weekend outings, and shared space decor"),
        ("Family Partnership Forum", "Quarterly", "Formal feedback loop on dignity, staff communication, and care plan progress"),
        ("Independent Advocacy & MDT", "Monthly", "Luton Advocacy visits & NHS learning disability nurse multidisciplinary reviews")
    ]
    y = p4.draw_booktabs_table("TABLE 4.7: CO-PRODUCTION, FAMILY ENGAGEMENT & MDT AUDIT CADENCE", cols_t47, rows_t47, y, row_h=9.4, font_size=5.6)
    y -= 2

    p4_callout = (
        "LEGAL ENFORCEABILITY OF STATEMENT OF PURPOSE: The Board of ADOV Care Group Limited formally ratifies this Statement of Purpose. "
        "Any proposed amendment to service scope, bed capacity, or registered location will be notified to the Care Quality Commission at least "
        "28 days prior to implementation in strict accordance with Regulation 12(3) of the CQC (Registration) Regulations 2009."
    )
    y = p4.draw_academic_callout("LEGAL ENFORCEABILITY OF STATEMENT OF PURPOSE", p4_callout, y, h=26)
    print("Page 4 final y =", y)
    return p4


# --- PAGE 5 ---
def add_p5(pdf):
    p5 = pdf.add_page()
    p5.draw_academic_header("SECTION 5.0", "CLINICAL GOVERNANCE & SINGLE ASSESSMENT FRAMEWORK")
    
    y = p5.height - 48
    y = p5.draw_section_heading("5.0", "CLINICAL GOVERNANCE ARCHITECTURE & SINGLE ASSESSMENT FRAMEWORK", y)
    
    p5_txt = (
        "The Care Quality Commission's Single Assessment Framework (SAF) evaluates providers across five core Key Questions "
        "(Safe, Effective, Caring, Responsive, and Well-Led) underpinned by 34 Quality Statements and six evidence categories. "
        "ADOV Care Group Limited deploys a dual-tier statutory leadership structure separating strategic board-level governance "
        "(Nominated Individual under Regulation 6) from frontline clinical command (Registered Manager under Regulation 7). "
        "Both statutory officers satisfy the Fit and Proper Person Requirements (FPPR) codified under Regulation 5."
    )
    y = p5.draw_wrapped_text(p5_txt, p5.mx, y, p5.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # FIGURE 2: VECTOR SCHEMATIC (INK-FRIENDLY)
    p5.set_fill_color(0.08, 0.14, 0.24)
    p5.draw_text("FIGURE 2: CQC SINGLE ASSESSMENT FRAMEWORK & CLINICAL GOVERNANCE FLOW", p5.mx, y, font="F2", size=7.2)
    y -= 5
    
    fig2_h = 100
    fig2_y = y - fig2_h
    p5.set_fill_color(0.99, 0.995, 1.0)
    p5.set_stroke_color(0.70, 0.78, 0.88)
    p5.draw_rect(p5.mx, fig2_y, p5.cw, fig2_h, fill=True, stroke=True, stroke_w=0.8)
    
    # Governance Left Boxes (Vertical Chain)
    bw_gov = 180
    bh_box = 18
    bx_gov = p5.mx + 15
    
    # Board
    by_board = fig2_y + fig2_h - 22
    p5.set_fill_color(0.96, 0.97, 0.99)
    p5.set_stroke_color(0.10, 0.25, 0.45)
    p5.draw_rect(bx_gov, by_board, bw_gov, bh_box, fill=True, stroke=True, stroke_w=0.8)
    p5.set_fill_color(0.08, 0.14, 0.24)
    p5.draw_text("BOARD OF DIRECTORS // FAIRYTALES GROUP", bx_gov + 8, by_board + 6, font="F2", size=6.2)
    
    # Arrow down
    p5.set_stroke_color(0.76, 0.61, 0.22)
    p5.draw_line(bx_gov + bw_gov/2, by_board, bx_gov + bw_gov/2, by_board - 6, stroke_w=1.0)
    
    # Nominated Individual
    by_ni = by_board - 24
    p5.set_fill_color(0.98, 0.97, 0.95)
    p5.set_stroke_color(0.76, 0.61, 0.22)
    p5.draw_rect(bx_gov, by_ni, bw_gov, bh_box, fill=True, stroke=True, stroke_w=0.8)
    p5.set_fill_color(0.76, 0.61, 0.22)
    p5.draw_text("NOMINATED INDIVIDUAL (CQC REGULATION 6)", bx_gov + 8, by_ni + 6, font="F2", size=6.2)
    
    # Arrow down
    p5.set_stroke_color(0.76, 0.61, 0.22)
    p5.draw_line(bx_gov + bw_gov/2, by_ni, bx_gov + bw_gov/2, by_ni - 6, stroke_w=1.0)
    
    # Registered Manager
    by_rm = by_ni - 24
    p5.set_fill_color(0.95, 0.98, 0.96)
    p5.set_stroke_color(0.12, 0.45, 0.22)
    p5.draw_rect(bx_gov, by_rm, bw_gov, bh_box, fill=True, stroke=True, stroke_w=0.8)
    p5.set_fill_color(0.12, 0.45, 0.22)
    p5.draw_text("REGISTERED MANAGER (LEVEL 5 / REGULATION 7)", bx_gov + 8, by_rm + 6, font="F2", size=6.2)
    
    # Arrow down
    p5.set_stroke_color(0.76, 0.61, 0.22)
    p5.draw_line(bx_gov + bw_gov/2, by_rm, bx_gov + bw_gov/2, by_rm - 6, stroke_w=1.0)
    
    # Frontline Team
    by_team = by_rm - 24
    p5.set_fill_color(0.96, 0.97, 0.99)
    p5.set_stroke_color(0.20, 0.30, 0.45)
    p5.draw_rect(bx_gov, by_team, bw_gov, bh_box, fill=True, stroke=True, stroke_w=0.8)
    p5.set_fill_color(0.10, 0.25, 0.45)
    p5.draw_text("FRONTLINE TEAM: 2 SHIFT LEADS + 12 CARERS", bx_gov + 8, by_team + 6, font="F2", size=6.2)
    
    # Right Side: 5 CQC Key Questions Panel
    bx_saf = p5.mx + 215
    bw_saf = p5.cw - 230
    by_saf = fig2_y + 8
    bh_saf = fig2_h - 16
    p5.set_fill_color(0.98, 0.985, 0.995)
    p5.set_stroke_color(0.20, 0.25, 0.35)
    p5.draw_rect(bx_saf, by_saf, bw_saf, bh_saf, fill=True, stroke=True, stroke_w=0.8)
    
    p5.set_fill_color(0.08, 0.14, 0.24)
    p5.draw_text("CQC SINGLE ASSESSMENT FRAMEWORK (SAF) AUDIT DOMAINS", bx_saf + 8, by_saf + bh_saf - 12, font="F2", size=6.5)
    p5.set_stroke_color(0.76, 0.61, 0.22)
    p5.draw_line(bx_saf + 8, by_saf + bh_saf - 15, bx_saf + bw_saf - 8, by_saf + bh_saf - 15, stroke_w=0.6)
    
    saf_items = [
        ("1. SAFE:", "PBS de-escalation, safeguarding s.42, L1 fire loop, 2:1 crisis coverage"),
        ("2. EFFECTIVE:", "Tier 2 Oliver McGowan, salt modified diets, MCA best interests"),
        ("3. CARING:", "Dignity, human rights autonomy, private domestic lockable en-suites"),
        ("4. RESPONSIVE:", "Adaptive care plans, sensory de-escalation pods, family co-production"),
        ("5. WELL-LED:", "Fit and Proper Person leadership, open duty of candour, digital audit")
    ]
    y_saf = by_saf + bh_saf - 26
    for k_lbl, k_desc in saf_items:
        p5.set_fill_color(0.08, 0.14, 0.24)
        p5.draw_text(k_lbl, bx_saf + 8, y_saf, font="F2", size=5.8)
        p5.set_fill_color(0.25, 0.30, 0.38)
        p5.draw_text(k_desc, bx_saf + 58, y_saf, font="F1", size=5.8)
        y_saf -= 11.5
        
    y = fig2_y - 6
    
    # Table 5.0: NI vs RM
    cols_t50 = [("Statutory Vector", 125), ("Nominated Individual (Regulation 6)", 195), ("Registered Manager (Regulation 7)", 195)]
    rows_t50 = [
        ("Legal Accountability", "Board-level statutory officer; liaises with CQC", "Direct operational responsibility for regulated care delivery"),
        ("Primary CQC Focus", "Regulation 5 FPPR compliance, capital sufficiency", "Day-to-day staff supervision, PBS implementation, medication"),
        ("Qualifications Required", "Proven corporate leadership & regulatory track record", "Level 5 Diploma in Leadership for Health & Social Care"),
        ("Supervisory Frequency", "Monthly formal quality review of clinical audit logs", "Continuous daily presence; direct oversight of 14 FTEs")
    ]
    y = p5.draw_booktabs_table("TABLE 5.0: NOMINATED INDIVIDUAL (REG 6) VS REGISTERED MANAGER (REG 7) STATUTORY DEMARCATION", cols_t50, rows_t50, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 5.1: FPPR
    cols_t51 = [("FPPR Criterion (Reg 5)", 125), ("Statutory Verification Standard", 195), ("Verified Evidence Dossier for NI & RM", 195)]
    rows_t51 = [
        ("Good Character", "Enhanced DBS with adults barred list check", "Clean disclosure countersigned by CQC; zero criminal record"),
        ("Competence & Skills", "Certified qualifications & management experience", "Level 5 Diploma verified; 12 years specialist autism leadership"),
        ("Physical & Mental Fitness", "Occupational Health declaration of fitness", "Certified medically fit; annual OH review scheduled"),
        ("Financial Probity", "Insolvency & bankruptcy register search", "Zero bankruptcy, zero disqualification under CDDA 1986")
    ]
    y = p5.draw_booktabs_table("TABLE 5.1: CQC REGULATION 5 (FIT AND PROPER PERSONS REQUIREMENT) EVIDENCE DOSSIER", cols_t51, rows_t51, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 5.2: 34 Quality Statements
    cols_t52 = [("SAF Quality Category", 125), ("Core Quality Statements Evaluated", 195), ("Auditable Operational Evidence at Campus", 195)]
    rows_t52 = [
        ("Learning Culture (Safe)", "Safety events, safeguarding & infection prevention", "Automated incident logging software; root-cause analysis"),
        ("Delivering Outcomes (Effective)", "Assessing needs, delivering care & consent", "Co-produced PBS care plans; quarterly MDT outcome reviews"),
        ("Treating People (Caring)", "Dignity, treating staff well, human rights", "Article 8 ECHR compliance; domestic sanctum privacy protocol")
    ]
    y = p5.draw_booktabs_table("TABLE 5.2: SINGLE ASSESSMENT FRAMEWORK 34 QUALITY STATEMENTS AUDIT MATRIX", cols_t52, rows_t52, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 5.3: Meeting Cadence
    cols_t53 = [("Governance Forum", 125), ("Frequency / Cadence", 110), ("Mandatory Statutory Agenda / Output", 280)]
    rows_t53 = [
        ("Clinical Governance Committee", "Monthly", "Reviews medication errors, PBS restrictive practices, safeguarding logs"),
        ("Regulation 17 Quality Audit", "Quarterly", "Independent inspector unannounced audit measuring Fundamental Standards"),
        ("Safeguarding & Restraint Review", "Monthly", "Lead PBS Specialist & RM review of all restrictive practice incident logs"),
        ("Frontline Team Supervision", "Bi-Weekly", "1-to-1 reflective supervision, PBS de-escalation practice, well-being check")
    ]
    y = p5.draw_booktabs_table("TABLE 5.3: CLINICAL GOVERNANCE COMMITTEE & QUALITY ASSURANCE CADENCE", cols_t53, rows_t53, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p5.draw_section_heading("5.1", "Staffing Establishment, 14 FTE Shift Roster & Lone-Working Elimination", y)
    p5_staff_txt = (
        "CQC Regulation 18 requires sufficient numbers of suitably qualified staff. Operating 78 and 80 Marston Gardens as an "
        "integrated campus deploys 14 full-time equivalent (FTE) staff, eliminating isolated lone-working and guaranteeing 2:1 crisis coverage."
    )
    y = p5.draw_wrapped_text(p5_staff_txt, p5.mx, y, p5.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 5.4: Staffing Establishment Roster
    cols_t54 = [("Shift Designation", 110), ("Operating Hours", 100), ("Staff Deployment (78 & 80)", 155), ("Mandatory Training Level", 150)]
    rows_t54 = [
        ("Early Shift", "07:30 - 15:30", "4 Care Workers + 1 Shift Leader", "Level 3 Health & Social Care + Oliver McGowan Tier 2"),
        ("Late Shift", "15:00 - 22:00", "4 Care Workers + 1 Shift Leader", "Certified PBS practitioner + Buccal Midazolam"),
        ("Waking Night Hub", "21:45 - 07:45", "1 Waking Carer + 1 Sleep-In Hub", "Immediate 2:1 physical de-escalation response"),
        ("Registered Manager", "08:30 - 17:00", "Full-time on-site clinical leadership", "Level 5 Diploma in Leadership & Management"),
        ("Weekend Activity Team", "08:00 - 20:00", "4 Care Workers + 1 Senior Carer", "Specialist community inclusion & travel training")
    ]
    y = p5.draw_booktabs_table("TABLE 5.4: OPERATIONAL ROSTER & 14 FTE STAFFING ESTABLISHMENT SCHEDULE", cols_t54, rows_t54, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p5.draw_section_heading("5.2", "Single Assessment Framework Quality Statements: Responsive & Well-Led", y)
    p5_saf2_txt = (
        "The remaining SAF domains evaluate responsiveness to individual needs and robust organizational leadership. ADOV Care Group "
        "embeds continuous clinical audit trails, accessible pictorial information, and proactive whistleblowing protections."
    )
    y = p5.draw_wrapped_text(p5_saf2_txt, p5.mx, y, p5.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 5.5: Responsive & Well-Led
    cols_t55 = [("SAF Core Domain", 110), ("Quality Statement Code", 160), ("Auditable Operational Evidence at Campus", 245)]
    rows_t55 = [
        ("Responsive Domain", "Person-Centred Care Planning", "Daily individualized activity schedules; sensory de-escalation routines"),
        ("Responsive Domain", "Accessible Information Standard", "Makaton visual cards, PECS communication boards, easy-read documents"),
        ("Well-Led Domain", "Shared Direction and Culture", "Compassionate leadership, active duty of candour, zero-retaliation ethos"),
        ("Well-Led Domain", "Governance, Management & Sustainability", "Cloud-based clinical incident logs; unannounced quarterly external audits")
    ]
    y = p5.draw_booktabs_table("TABLE 5.5: SINGLE ASSESSMENT FRAMEWORK (RESPONSIVE & WELL-LED) AUDIT MATRIX", cols_t55, rows_t55, y, row_h=9.4, font_size=5.6)
    y -= 3

    # Table 5.6: Training Matrix
    cols_t56 = [("Training Module", 125), ("Audience Target", 130), ("Recertification Cadence", 125), ("Accreditation Standard", 135)]
    rows_t56 = [
        ("Oliver McGowan Tier 2", "100% Frontline Staff & RM", "Annual Mandatory Refresher", "Skills for Care / NHS England"),
        ("PBS & Restraint Reduction", "All Care Staff & Shift Leads", "Annual Practical Drills", "BILD / RRN Certified Training"),
        ("Emergency Medication / Epilepsy", "All Designated Carers", "Bi-Annual Clinical Simulation", "Accredited Pharmacist Assessed"),
        ("Safeguarding Level 3", "Registered Manager & NI", "Annual Statutory Review", "Luton Safeguarding Adults Board")
    ]
    y = p5.draw_booktabs_table("TABLE 5.6: MANDATORY WORKFORCE STATUTORY TRAINING & COMPETENCY SCHEDULE", cols_t56, rows_t56, y, row_h=9.4, font_size=5.6)
    y -= 2

    p5_callout = (
        "FIT AND PROPER PERSONS STATUTORY ATTESTATION: The Board of ADOV Care Group Limited certifies that both the Nominated Individual "
        "and Registered Manager nominee satisfy all criteria under Regulation 5 of the Health and Social Care Act 2008 (Regulated Activities) "
        "Regulations 2014. Enhanced DBS certificates, verified qualifications, and occupational health fitness sign-offs are archived in the CQC portal."
    )
    y = p5.draw_academic_callout("FIT AND PROPER PERSONS STATUTORY ATTESTATION", p5_callout, y, h=30)
    print("Page 5 final y =", y)
    return p5


# --- PAGE 6 ---
def add_p6(pdf):
    p6 = pdf.add_page()
    p6.draw_academic_header("SECTION 6.0", "REGISTERED MANAGER CLINICAL COMPETENCY")
    
    y = p6.height - 48
    y = p6.draw_section_heading("6.0", "REGISTERED MANAGER COMPETENCY: THE 5 STATUTORY CLINICAL SCENARIOS", y)
    
    p6_txt = (
        "During the formal CQC Registration Interview under Regulation 7, the Registered Manager applicant is subjected to an exhaustive "
        "competency assessment. The inspector evaluates the manager's ability to navigate high-risk clinical dilemmas, enforce statutory "
        "regulations under pressure, uphold human rights, and maintain clinical safety. Below are the five mandatory clinical examination "
        "scenarios, complete with statutory triggers, legislative authorities, and model regulatory responses."
    )
    y = p6.draw_wrapped_text(p6_txt, p6.mx, y, p6.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # Table 6.0: The 5 Master Clinical Scenarios
    cols_t60 = [("Clinical Examination Scenario", 115), ("Statutory Trigger & Presentation", 165), ("RM Mandatory Regulatory & Operational Action", 235)]
    rows_t60 = [
        ("Scenario 1: Severe PBS Distress", "Resident in violent distress, property damage, self-injury risk", "Deploy Tier 2 PBS de-escalation; zero unauthorised restraint; 2:1 low-arousal approach."),
        ("Scenario 2: Section 42 Safeguarding", "Unexplained bruising discovered during personal care", "Immediate medical triage; 2-hr Section 42 Care Act referral to Luton Council & Police."),
        ("Scenario 3: Covert Medication / MCA", "Resident repeatedly refusing life-critical epilepsy medication", "Two-stage MCA capacity assessment; multidisciplinary Best Interests meeting under s.4 MCA."),
        ("Scenario 4: Duty of Candour (Reg 20)", "Missed morning antiepileptic dose resulting in minor seizure", "Immediate clinical triage; statutory Regulation 20 written apology & open disclosure within 10 days."),
        ("Scenario 5: Frontline Whistleblowing", "Support worker reports peer using verbal intimidation", "Immediate suspension of accused staff; PIDA 1998 protection; formal CQC & LSAB notification.")
    ]
    y = p6.draw_booktabs_table("TABLE 6.0: THE 5 STATUTORY CLINICAL EXAMINATION SCENARIOS & MODEL RM RESPONSES", cols_t60, rows_t60, y, row_h=9.6, font_size=5.6)
    y -= 3
    
    y = p6.draw_section_heading("6.1", "Positive Behaviour Support (PBS) & Restraint Reduction Framework", y)
    p6_pbs_txt = (
        "Under the Restraint Reduction Network (RRN) Training Standards, physical restraint is strictly an emergency measure of last "
        "resort. ADOV Care Group implements a three-tier proactive PBS architecture designed to eliminate restrictive practices."
    )
    y = p6.draw_wrapped_text(p6_pbs_txt, p6.mx, y, p6.cw, font="F1", size=6.6, leading=8.4)
    y -= 3
    
    # Table 6.1: PBS Hierarchy
    cols_t61 = [("PBS Hierarchy Level", 125), ("Clinical Focus & Techniques", 195), ("Auditable Practice at Marston Campus", 195)]
    rows_t61 = [
        ("Tier 1: Primary Proactive Support", "Predictable routines, sensory diets, preferred activities", "Reduces baseline anxiety; sensory calming room utilization"),
        ("Tier 2: Secondary De-Escalation", "Early trigger identification, distraction, low-arousal verbal tone", "Redirecting to quiet garden buffer; non-demanding stance"),
        ("Tier 3: Tertiary Reactive Crisis", "Last resort breakaway techniques; minimum force for shortest duration", "Immediate incident debrief; root-cause analysis; PBS plan update")
    ]
    y = p6.draw_booktabs_table("TABLE 6.1: POSITIVE BEHAVIOURAL SUPPORT (PBS) THREE-TIER DE-ESCALATION HIERARCHY", cols_t61, rows_t61, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    y = p6.draw_section_heading("6.2", "Mental Capacity Act 2005 & Covert Medication Governance", y)
    p6_mca_txt = (
        "The Mental Capacity Act 2005 presumes capacity unless proven otherwise. Covert medication administration represents an extreme "
        "interference with Article 8 rights and requires rigorous statutory governance under Section 4 Best Interests rules."
    )
    y = p6.draw_wrapped_text(p6_mca_txt, p6.mx, y, p6.cw, font="F1", size=6.6, leading=8.4)
    y -= 3
    
    # Table 6.2: MCA & Covert Meds
    cols_t62 = [("MCA Assessment Step", 125), ("Statutory Standard (MCA 2005)", 195), ("Clinical Governance Protocol at ADOV", 195)]
    rows_t62 = [
        ("Step 1: Two-Stage Test", "Does impairment of mind prevent understanding/weighing?", "Documented by Registered Manager & Learning Disability Nurse"),
        ("Step 2: Best Interests Meeting", "Section 4 checklist; consult family, advocate & GP", "Formal multidisciplinary meeting; explores all less restrictive options"),
        ("Step 3: Pharmacist Consultation", "Ensure drug safety when crushed or concealed in food", "Written dispensing guidance from supplying Community Pharmacist"),
        ("Step 4: Time-Limited Review", "Covert medication authorisations expire within 30 days", "Mandatory monthly clinical review; DoLS supervisory body informed")
    ]
    y = p6.draw_booktabs_table("TABLE 6.2: MENTAL CAPACITY ACT 2005 & COVERT MEDICATION STATUTORY CHECKLIST", cols_t62, rows_t62, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 6.3: Duty of Candour Timeline
    cols_t63 = [("Duty of Candour Stage", 115), ("Statutory Requirement (Regulation 20)", 195), ("Mandatory Execution Timeline", 205)]
    rows_t63 = [
        ("Stage 1: Identification & Triage", "Identify Notifiable Safety Incident (moderate harm or above)", "Within 2 hours of incident discovery"),
        ("Stage 2: Verbal Notification", "Inform service user and/or family; provide true account", "Without delay; within 24 hours of confirmation"),
        ("Stage 3: Written Apology", "Formal written notification offering sincere, unreserved apology", "Delivered within 10 operational days"),
        ("Stage 4: Root-Cause Investigation", "Independent clinical review; actions taken to prevent recurrence", "Completed and shared with family within 28 days")
    ]
    y = p6.draw_booktabs_table("TABLE 6.3: CQC REGULATION 20 STATUTORY DUTY OF CANDOUR PROTOCOL & TIMELINE", cols_t63, rows_t63, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 6.4: Whistleblowing
    cols_t64 = [("Whistleblowing Vector", 125), ("Statutory Standard (PIDA 1998)", 195), ("Operational Protection at Marston Campus", 195)]
    rows_t64 = [
        ("Designated Speak Up Guardian", "Independent officer outside direct management chain", "Direct 24/7 confidential reporting to Non-Executive Director"),
        ("Statutory Immunity", "Public Interest Disclosure Act 1998 protections", "Zero detriment policy; contractual disciplinary penalty for retaliation"),
        ("External Regulatory Escalation", "Unrestricted right to contact CQC Inspectorate directly", "CQC whistleblowing hotline displayed prominently in staff hub")
    ]
    y = p6.draw_booktabs_table("TABLE 6.4: WHISTLEBLOWING & PUBLIC INTEREST DISCLOSURE ACT (PIDA 1998) SAFEGUARDS", cols_t64, rows_t64, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p6.draw_section_heading("6.3", "STOMP Principles: Stopping Over-Medication of Autistic People", y)
    p6_stomp_txt = (
        "ADOV Care Group rigorously adheres to the national STOMP pledge (Stopping Over-Medication of People with a Learning Disability "
        "and Autistic People). Psychotropic medication is never used as chemical restraint or a substitute for skilled behavioural support."
    )
    y = p6.draw_wrapped_text(p6_stomp_txt, p6.mx, y, p6.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 6.5: STOMP Matrix
    cols_t65 = [("STOMP Governance Pillar", 125), ("Clinical Standard & NICE NG11 Benchmark", 195), ("Operational Practice at Marston Campus", 195)]
    rows_t65 = [
        ("Routine Psychotropic Audit", "Quarterly medication review with Consultant Psychiatrist", "Formal reduction plan for any sedative or anxiolytic drug"),
        ("Non-Pharmacological First Line", "Sensory diets, environmental calming, and PBS plans", "Primary proactive PBS reduces behavioural arousal naturally"),
        ("PRN Administration Protocol", "Clear behavioural thresholds & strict daily maximums", "Individual PRN protocols; mandatory debrief after each use"),
        ("Side-Effect Monitoring", "Formal screening for extrapyramidal symptoms & weight", "Monthly physical health checks and GP clinical reviews")
    ]
    y = p6.draw_booktabs_table("TABLE 6.5: STOMP GOVERNANCE & PSYCHOTROPIC MEDICATION REDUCTION MATRIX", cols_t65, rows_t65, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p6.draw_section_heading("6.4", "Root-Cause Analysis (RCA) & CQC Fit & Proper Interview Rubric", y)
    p6_rca_txt = (
        "Every safety event undergoes structured Root-Cause Analysis (RCA) utilizing 5-Whys and Fishbone methodologies to drive "
        "continuous institutional learning. Candidate performance across CQC interview domains is audited against strict regulatory rubrics."
    )
    y = p6.draw_wrapped_text(p6_rca_txt, p6.mx, y, p6.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 6.6: RCA
    cols_t66 = [("Incident Severity Tier", 125), ("Investigation Protocol & Tool", 195), ("Governance Output & Reporting Destination", 195)]
    rows_t66 = [
        ("Level 1: Minor Sensory Distress", "Shift-level low-arousal debrief", "Updated individual sensory profile in digital care record"),
        ("Level 2: Physical Restraint Event", "Registered Manager review within 24 hours", "PBS plan revision; BILD debrief log; clinical supervision"),
        ("Level 3: Notifiable Safety Incident", "Full multidisciplinary RCA investigation (7 days)", "Statutory Duty of Candour report to CQC, ICB, and Family"),
        ("Level 4: Section 42 Safeguarding", "Multi-agency investigation led by Local Authority", "Formal report submitted to Luton Safeguarding Adults Board")
    ]
    y = p6.draw_booktabs_table("TABLE 6.6: CLINICAL INCIDENT ROOT-CAUSE ANALYSIS (RCA) & GOVERNANCE LEDGER", cols_t66, rows_t66, y, row_h=9.4, font_size=5.6)
    y -= 3

    # Table 6.7: Interview Rubric
    cols_t67 = [("CQC Interview Competency Domain", 130), ("Regulatory Benchmark Standard", 185), ("Assessed Candidate Demonstration Level", 200)]
    rows_t67 = [
        ("Fundamental Standards (Regs 4-20A)", "Instant command of primary and secondary regulations", "Outstanding: 100% accurate legal citations and thresholds"),
        ("Safeguarding Leadership (Care Act s.42)", "Decisive multi-agency isolation of harm", "Exemplary: Immediate clinical triage and statutory notice"),
        ("PBS & Well-Led Duty of Candour", "Mastery of low-arousal methods & open candour", "Expert: Certified BILD practitioner; proven candour ethics")
    ]
    y = p6.draw_booktabs_table("TABLE 6.7: REGISTERED MANAGER CQC FIT & PROPER INTERVIEW SCORING RUBRIC", cols_t67, rows_t67, y, row_h=9.4, font_size=5.6)
    y -= 2

    p6_callout = (
        "REGISTERED MANAGER CLINICAL COMPETENCY CERTIFICATION: The candidate Registered Manager has successfully completed rigorous "
        "mock interview simulations covering all five statutory clinical scenarios. The candidate demonstrates uncompromised regulatory mastery, "
        "exemplary safeguarding ethics, and decisive operational command in full alignment with CQC Fit and Proper Person standards."
    )
    y = p6.draw_academic_callout("REGISTERED MANAGER CLINICAL COMPETENCY CERTIFICATION", p6_callout, y, h=27)
    print("Page 6 final y =", y)
    return p6


# --- PAGE 7 ---
def add_p7(pdf):
    p7 = pdf.add_page()
    p7.draw_academic_header("SECTION 7.0", "REGULATION 13 FINANCIAL VIABILITY & SOLVENCY")
    
    y = p7.height - 48
    y = p7.draw_section_heading("7.0", "FINANCIAL VIABILITY MANDATE: CQC REGULATION 13", y)
    
    p7_txt = (
        "Regulation 13 of the Care Quality Commission (Registration) Regulations 2009 (SI 2009/3112) establishes a mandatory statutory "
        "duty: the service provider must take all reasonable steps to carry on the regulated activity in such a manner as to ensure "
        "the financial viability of the carrying on of that activity. A provider unable to demonstrate adequate working capital faces "
        "summary refusal of registration under Section 12 of the Health and Social Care Act 2008. ADOV Care Group Limited maintains a "
        "ring-fenced £150,000 liquid cash reserve alongside a robust 3-year operating surplus."
    )
    y = p7.draw_wrapped_text(p7_txt, p7.mx, y, p7.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # FIGURE 4: VECTOR FINANCIAL BAR CHART (INK-FRIENDLY)
    p7.set_fill_color(0.08, 0.14, 0.24)
    p7.draw_text("FIGURE 4: PRO-FORMA OPERATIONAL CASHFLOW & FINANCIAL VIABILITY MODEL (YEARS 1 - 3)", p7.mx, y, font="F2", size=7.2)
    y -= 5
    
    fig4_h = 82
    fig4_y = y - fig4_h
    p7.set_fill_color(0.99, 0.995, 1.0)
    p7.set_stroke_color(0.70, 0.78, 0.88)
    p7.draw_rect(p7.mx, fig4_y, p7.cw, fig4_h, fill=True, stroke=True, stroke_w=0.8)
    
    chart_x = p7.mx + 45
    chart_w = p7.cw - 90
    chart_y = fig4_y + 16
    
    p7.set_stroke_color(0.70, 0.78, 0.88)
    p7.draw_line(chart_x, chart_y, chart_x + chart_w, chart_y, stroke_w=0.8)
    
    years_data = [
        ("Year 1 (62.5% Occ)", 832, 567, 265, chart_x + 25),
        ("Year 2 (87.5% Occ)", 1165, 717, 448, chart_x + chart_w/2 - 45),
        ("Year 3 (100% Occ)", 1331, 790, 541, chart_x + chart_w - 115)
    ]
    
    for lbl, rev, opex, ebitda, gx in years_data:
        scale = 42.0 / 1400.0
        h_rev = rev * scale
        h_op = opex * scale
        h_eb = ebitda * scale
        
        # Revenue bar
        p7.set_fill_color(0.10, 0.25, 0.45)
        p7.draw_rect(gx, chart_y, 22, h_rev, fill=True)
        p7.set_fill_color(0.10, 0.25, 0.45)
        p7.draw_text(f"£{rev}k", gx - 1, chart_y + h_rev + 2, font="F2", size=5.5)
        
        # OpEx bar
        p7.set_fill_color(0.70, 0.25, 0.25)
        p7.draw_rect(gx + 25, chart_y, 22, h_op, fill=True)
        p7.set_fill_color(0.70, 0.25, 0.25)
        p7.draw_text(f"£{opex}k", gx + 24, chart_y + h_op + 2, font="F2", size=5.5)
        
        # EBITDA bar
        p7.set_fill_color(0.12, 0.45, 0.22)
        p7.draw_rect(gx + 50, chart_y, 22, h_eb, fill=True)
        p7.set_fill_color(0.12, 0.45, 0.22)
        p7.draw_text(f"£{ebitda}k", gx + 49, chart_y + h_eb + 2, font="F2", size=5.5)
        
        p7.set_fill_color(0.20, 0.25, 0.35)
        p7.draw_text(lbl, gx + 2, chart_y - 10, font="F2", size=5.6)
        
    leg_x = p7.mx + p7.cw - 180
    leg_y = fig4_y + fig4_h - 14
    
    p7.set_fill_color(0.10, 0.25, 0.45)
    p7.draw_rect(leg_x, leg_y, 8, 5, fill=True)
    p7.draw_text("Gross Revenue", leg_x + 11, leg_y + 0.5, font="F2", size=5.4)
    
    p7.set_fill_color(0.70, 0.25, 0.25)
    p7.draw_rect(leg_x + 60, leg_y, 8, 5, fill=True)
    p7.draw_text("Operating Costs", leg_x + 71, leg_y + 0.5, font="F2", size=5.4)
    
    p7.set_fill_color(0.12, 0.45, 0.22)
    p7.draw_rect(leg_x + 125, leg_y, 8, 5, fill=True)
    p7.draw_text("EBITDA", leg_x + 136, leg_y + 0.5, font="F2", size=5.4)
    
    y = fig4_y - 6
    
    # Table 7.0: 3-Year P&L Waterfall
    cols_t70 = [("Financial Line Item", 125), ("Year 1 (62.5% Occ)", 95), ("Year 2 (87.5% Occ)", 95), ("Year 3 (100% Occ)", 95), ("3-Year Cumulative", 105)]
    rows_t70 = [
        ("Gross Placement Fees (£3.2k/wk)", "£832,000", "£1,164,800", "£1,331,200", "£3,328,000 Total Fees"),
        ("Frontline Day Care Staffing", "-£244,600", "-£342,440", "-£391,360", "-£978,400 Care Wages"),
        ("Unified Waking Night Hub Rota", "-£140,400", "-£147,420", "-£154,790", "-£442,610 Night Hub"),
        ("Specialist PBS & Clinical Cover", "-£41,600", "-£58,240", "-£66,560", "-£166,400 Clinical"),
        ("Commercial Lease Rent (80 Marston)", "-£50,000", "-£52,500", "-£55,130", "-£157,630 Facility Lease"),
        ("Operating Overheads & Utilities", "-£90,400", "-£116,200", "-£122,360", "-£328,960 Admin & OpEx"),
        ("OPERATING EBITDA SURPLUS", "£265,000 (31.8%)", "£448,000 (38.5%)", "£541,000 (40.6%)", "£1,254,000 (37.7%)")
    ]
    y = p7.draw_booktabs_table("TABLE 7.0: THREE-YEAR PRO-FORMA FINANCIAL STATEMENT & CASHFLOW WATERFALL", cols_t70, rows_t70, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    y = p7.draw_section_heading("7.1", "Ring-Fenced £150,000 Working Capital Ledger & Bank Covenants", y)
    p7_cap_txt = (
        "To guarantee uninterrupted service continuity during the initial resident intake phase, FAIRYTALES GROUP has ring-fenced "
        "an unencumbered £150,000 cash liquidity facility in an interest-bearing escrow account held with Barclays Bank UK PLC. This provides "
        "over 3.2 months of fixed operating overhead coverage under zero-revenue assumptions."
    )
    y = p7.draw_wrapped_text(p7_cap_txt, p7.mx, y, p7.cw, font="F1", size=6.6, leading=8.4)
    y -= 3
    
    # Table 7.1: Working Capital Buffer
    cols_t71 = [("Liquidity Reserve Component", 125), ("Committed Capital", 110), ("Statutory Viability Purpose", 280)]
    rows_t71 = [
        ("Ring-Fenced Cash Escrow", "£150,000", "Dedicated cash buffer guaranteeing frontline payroll during intake ramp-up"),
        ("Parent Group Equity Guarantee", "£100,000", "Legally binding parental solvency undertaking executed by FAIRYTALES GROUP"),
        ("Pre-Commencement CapEx Ringfence", "£143,000", "Fully paid capital works covering DDA wetrooms, fire loop, and sensory fit-out")
    ]
    y = p7.draw_booktabs_table("TABLE 7.1: RING-FENCED WORKING CAPITAL BUFFER & CAPITAL SOLVENCY LEDGER", cols_t71, rows_t71, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 7.2: Breakeven & Stress Testing
    cols_t72 = [("Economic Stress Vector", 125), ("Threshold / Shock Level", 130), ("Enterprise Financial Outcome & Viability Buffer", 260)]
    rows_t72 = [
        ("Breakeven Occupancy Threshold", "48.2% (3.8 Resident Beds)", "All fixed operating costs & lease covered; zero insolvency risk"),
        ("Commissioning Fee Squeeze (-10%)", "£2,880 / bed / week tariff", "Generates £180k operating surplus; debt covenants remain compliant"),
        ("Wage Inflation Shock (+12% Pay)", "Living Wage surge absorption", "Absorbed comfortably via £265k Year 1 EBITDA buffer")
    ]
    y = p7.draw_booktabs_table("TABLE 7.2: BREAKEVEN OCCUPANCY ANALYSIS & FINANCIAL STRESS-TESTING", cols_t72, rows_t72, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 7.3: Accountant's Statement
    cols_t73 = [("CQC Form FV1 Audit Vector", 125), ("Statutory Verification Standard", 195), ("Auditor Certification & Sign-Off", 195)]
    rows_t73 = [
        ("Form FV1 Certified Sign-Off", "CQC (Registration) Regs 2009 Reg 13", "Signed by Fellow Chartered Certified Accountant (FCCA)"),
        ("Bank Statement Verification", "Barclays Bank UK PLC escrow confirmation", "Verified cleared funds of £150,000 archived in CQC portal"),
        ("Going Concern Attestation", "ISA (UK) 570 Going Concern principles", "Confirmed 24-month operational solvency with zero material uncertainty")
    ]
    y = p7.draw_booktabs_table("TABLE 7.3: ACCOUNTANT'S FINANCIAL VIABILITY STATEMENT (CQC FORM FV1 AUDIT)", cols_t73, rows_t73, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p7.draw_section_heading("7.2", "Free Cash Flow (FCF) Waterfall & Senior Debt Amortisation Capacity", y)
    p7_fcf_txt = (
        "Operating EBITDA translates into strong Free Cash Flow to Equity (FCFE) after accounting for maintenance sinking funds, "
        "lease obligations, and corporate tax. Over the initial three-year horizon, cumulative FCFE reaches £950,955, funding continuous "
        "clinical investment and de-leveraging."
    )
    y = p7.draw_wrapped_text(p7_fcf_txt, p7.mx, y, p7.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 7.4: FCFE Waterfall
    cols_t74 = [("Cashflow Line Item", 125), ("Year 1", 90), ("Year 2", 90), ("Year 3", 90), ("3-Yr Cumulative", 120)]
    rows_t74 = [
        ("Operating EBITDA Surplus", "£265,000", "£448,000", "£541,000", "£1,254,000 Total EBITDA"),
        ("Maintenance Sinking Fund (2%)", "-£16,640", "-£23,296", "-£26,624", "-£66,560 Capital Reserve"),
        ("Corporation Tax Liability (25%)", "-£43,340", "-£84,926", "-£108,219", "-£236,485 Tax Provision"),
        ("Free Cash Flow to Equity (FCFE)", "£205,020", "£339,778", "£406,157", "£950,955 Net Surplus Cash")
    ]
    y = p7.draw_booktabs_table("TABLE 7.4: THREE-YEAR FREE CASH FLOW TO EQUITY (FCFE) WATERFALL", cols_t74, rows_t74, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p7.draw_section_heading("7.3", "Senior Debt Underwriting Profile & Downside Stress-Testing", y)
    p7_stress_txt = (
        "Senior debt underwriting metrics satisfy institutional tier-1 care standards. Downside sensitivity simulations confirm that "
        "even under compound shocks of reduced occupancy and wage inflation, the service maintains complete solvency."
    )
    y = p7.draw_wrapped_text(p7_stress_txt, p7.mx, y, p7.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 7.5: Debt Covenants
    cols_t75 = [("Banking Underwriting Metric", 145), ("Campus Financial Standard", 185), ("Lender Covenant Threshold", 185)]
    rows_t75 = [
        ("Debt Service Coverage Ratio (DSCR)", "2.85x DSCR (Strong Coverage)", "Minimum 1.35x covenant required"),
        ("Loan to Value (LTV) Ratio", "58.0% LTV on freehold value", "Maximum 65.0% LTV permitted"),
        ("Working Capital Liquidity Buffer", "£150,000 ring-fenced escrow", "Minimum 3.0 months fixed OpEx covenant")
    ]
    y = p7.draw_booktabs_table("TABLE 7.5: SENIOR LENDER UNDERWRITING PROFILE & BANKING COVENANTS", cols_t75, rows_t75, y, row_h=9.4, font_size=5.6)
    y -= 3

    # Table 7.6: Downside Stress Tests
    cols_t76 = [("Macroeconomic Stress Shock", 125), ("Scenario Impact on ADOV", 195), ("Solvency & CQC Viability Outcome", 195)]
    rows_t76 = [
        ("70% Occupancy (5.6 Beds)", "Revenue £931k; EBITDA £182k", "Solvency preserved; covers all debt service and lease costs"),
        ("15% Care Worker Wage Surge", "Headcount cost increases by £58k/yr", "Absorbed comfortably via £265k Year 1 EBITDA buffer"),
        ("10% Commissioning Tariff Cut", "Net placement revenue reduced by £133k", "Retains £132k net cash surplus; zero risk of insolvency")
    ]
    y = p7.draw_booktabs_table("TABLE 7.6: DOWNSIDE ECONOMIC STRESS-TESTING & SOLVENCY SIMULATION", cols_t76, rows_t76, y, row_h=9.4, font_size=5.6)
    y -= 2

    p7_callout = (
        "REGULATION 13 FINANCIAL VIABILITY CERTIFICATION: The Board of ADOV Care Group Limited and the Group Chief Financial Officer "
        "hereby certify that the provider holds sufficient financial resources to provide care services in full compliance with the Statement "
        "of Purpose. Cleared funds of £150,000 are ring-fenced and certified under CQC Form FV1 by an independent Chartered Certified Accountant."
    )
    y = p7.draw_academic_callout("REGULATION 13 FINANCIAL VIABILITY CERTIFICATION", p7_callout, y, h=26)
    print("Page 7 final y =", y)
    return p7


# --- PAGE 8 ---
def add_p8(pdf):
    p8 = pdf.add_page()
    p8.draw_academic_header("SECTION 8.0", "6-PHASE CQC REGISTRATION & APPROVAL ROADMAP")
    
    y = p8.height - 48
    y = p8.draw_section_heading("8.0", "THE SIX-PHASE CQC REGISTRATION MASTER PROGRAMME", y)
    
    p8_txt = (
        "Securing CQC provider and manager registration requires an orchestrated statutory programme spanning 16 weeks. "
        "Each phase represents a binding regulatory gateway under the Health and Social Care Act 2008. The sequence below codifies "
        "the critical path from initial DBS countersignatures, portal uploads, document validation, and fit & proper interviews, "
        "culminating in the Section 28(3) statutory waiver that compresses the representation period to secure rapid certification."
    )
    y = p8.draw_wrapped_text(p8_txt, p8.mx, y, p8.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # FIGURE 3: VECTOR TIMELINE (INK-FRIENDLY)
    p8.set_fill_color(0.08, 0.14, 0.24)
    p8.draw_text("FIGURE 3: THE 6-PHASE CQC REGISTRATION & SECTION 28(3) FAST-TRACK TIMELINE", p8.mx, y, font="F2", size=7.2)
    y -= 5
    
    fig3_h = 88
    fig3_y = y - fig3_h
    p8.set_fill_color(0.99, 0.995, 1.0)
    p8.set_stroke_color(0.70, 0.78, 0.88)
    p8.draw_rect(p8.mx, fig3_y, p8.cw, fig3_h, fill=True, stroke=True, stroke_w=0.8)
    
    # Draw 6 phase boxes
    phases_f3 = [
        ("PHASE 1", "Pre-App & DBS", "Wks 1 - 4", (0.96, 0.97, 0.99), (0.20, 0.30, 0.45)),
        ("PHASE 2", "Portal Uploads", "Wks 5 - 7", (0.97, 0.98, 1.0), (0.10, 0.25, 0.45)),
        ("PHASE 3", "Validation Hold", "Wks 8 - 10", (0.98, 0.985, 0.995), (0.40, 0.45, 0.55)),
        ("PHASE 4", "CQC Interviews", "Wks 11 - 14", (0.98, 0.97, 0.95), (0.76, 0.61, 0.22)),
        ("PHASE 5", "s.28(3) Waiver", "Wks 14 - 15", (0.95, 0.98, 0.96), (0.12, 0.45, 0.22)),
        ("PHASE 6", "Certificate Issued", "Wks 16 - 17", (0.94, 0.97, 0.95), (0.10, 0.40, 0.20))
    ]
    
    bw_box = 78
    bh_box = 48
    bx_cur = p8.mx + 10
    by_box = fig3_y + 24
    
    for p_num, p_name, p_time, bg_c, strk_c in phases_f3:
        p8.set_fill_color(*bg_c)
        p8.set_stroke_color(*strk_c)
        p8.draw_rect(bx_cur, by_box, bw_box, bh_box, fill=True, stroke=True, stroke_w=0.8)
        
        p8.set_fill_color(*strk_c)
        p8.draw_text(p_num, bx_cur + 6, by_box + bh_box - 11, font="F2", size=6.5)
        p8.set_fill_color(0.08, 0.14, 0.24)
        p8.draw_text(p_name, bx_cur + 6, by_box + bh_box - 22, font="F2", size=5.8)
        p8.set_fill_color(0.35, 0.40, 0.50)
        p8.draw_text(p_time, bx_cur + 6, by_box + bh_box - 33, font="F1", size=5.5)
        
        # small check indicator
        p8.set_fill_color(*strk_c)
        p8.draw_rect(bx_cur + 6, by_box + 5, bw_box - 12, 4, fill=True)
        
        bx_cur += bw_box + 6.5
        
    # Connecting timeline rule
    p8.set_stroke_color(0.76, 0.61, 0.22)
    p8.draw_line(p8.mx + 10, by_box - 8, p8.mx + p8.cw - 10, by_box - 8, stroke_w=1.2)
    
    # Fast track banner
    p8.set_fill_color(0.95, 0.98, 0.96)
    p8.set_stroke_color(0.12, 0.45, 0.22)
    p8.draw_rect(p8.mx + 20, fig3_y + 4, p8.cw - 40, 9, fill=True, stroke=True, stroke_w=0.6)
    p8.set_fill_color(0.12, 0.45, 0.22)
    p8.draw_text("FAST-TRACK ADVANTAGE: SECTION 28(3) REPRESENTATION WAIVER ELIMINATES 28-DAY STATUTORY HOLD PERIOD", p8.mx + 25, fig3_y + 6.5, font="F2", size=5.5)
    
    y = fig3_y - 6
    
    # Table 8.0: Detailed 6-Phase Roadmap
    cols_t80 = [("Programme Phase", 95), ("Statutory Workstream & Key Deliverables", 215), ("Lead Responsible Owner", 100), ("Statutory Gateway Sign-Off", 105)]
    rows_t80 = [
        ("Phase 1: Pre-App Governance", "Enhanced DBS countersignature; Form FV1 financial sign-off; SoP drafting", "Nominated Individual & RM", "DBS Barred List Clearance"),
        ("Phase 2: Portal Submission", "Submit Provider & Manager applications via CQC Portal; upload 24 core files", "Registered Manager", "CQC Acknowledgement Letter"),
        ("Phase 3: Validation Period", "CQC National Customer Service Centre checks completeness; allocation to team", "CQC Registration Team", "Application Formally Validated"),
        ("Phase 4: CQC Interviews", "Fit & Proper Person interviews with Inspector; site assessment of 78 & 80", "CQC Lead Inspector & RM", "Successful Competency Rating"),
        ("Phase 5: Section 26 NOP & Waiver", "CQC issues Notice of Proposal to register; ADOV executes Section 28(3) waiver", "Board of Directors", "28-Day Representation Waived"),
        ("Phase 6: Notice of Decision", "Final Notice of Decision (NOD) & Certificate of Registration issued", "CQC Chief Inspector", "Full Legal Authority to Care")
    ]
    y = p8.draw_booktabs_table("TABLE 8.0: SIX-PHASE CQC REGISTRATION CRITICAL PATH & STATUTORY MILESTONES", cols_t80, rows_t80, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 8.1: Document Inventory
    cols_t81 = [("CQC Upload Category", 125), ("Mandatory Document Description", 195), ("Statutory Regulatory Instrument", 195)]
    rows_t81 = [
        ("Statement of Purpose (4 Parts)", "Complete specification for 78 & 80 Marston Gardens", "CQC (Registration) Regulations 2009 Reg 12"),
        ("Financial Viability Statement", "Accountant certified Form FV1 + £150k bank statement", "CQC (Registration) Regulations 2009 Reg 13"),
        ("Safeguarding & PBS Policies", "Multi-agency Section 42 Care Act & Tier 2 PBS manuals", "Regulated Activities Regulations 2014 Regs 12 & 13"),
        ("Governance & Audit Framework", "Monthly Regulation 17 audit tools, risk registers, DoC", "Regulated Activities Regulations 2014 Regs 17 & 20"),
        ("Building Safety & Planning Docs", "Section 192 CLEUD, L1 fire alarm certificate, DDA layout", "Approved Documents B, E, M & RRFSO 2005")
    ]
    y = p8.draw_booktabs_table("TABLE 8.1: PRE-SUBMISSION MANDATORY DOCUMENT INVENTORY & EVIDENCE AUDIT", cols_t81, rows_t81, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 8.2: Interview Bank
    cols_t82 = [("CQC Interview Competency", 125), ("Statutory Examination Question", 195), ("Required Model Response Threshold", 195)]
    rows_t82 = [
        ("Duty of Candour (Reg 20)", "How do you respond when a carer drops a medication blister?", "Immediate clinical triage; open disclosure & apology in 10 days"),
        ("Safeguarding Section 42", "What is your action if an allegation involves a senior carer?", "Instant suspension; 2-hr notice to Luton Council, Police & CQC"),
        ("Restraint Reduction Network", "When is physical restraint legally defensible in your service?", "Strict emergency last resort; minimum force for shortest duration")
    ]
    y = p8.draw_booktabs_table("TABLE 8.2: REGISTERED MANAGER FIT & PROPER INTERVIEW EXAMINATION RUBRIC", cols_t82, rows_t82, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 8.3: NOP Conditions
    cols_t83 = [("Standard Registration Condition", 125), ("Statutory Scope & Limitation", 195), ("Compliance Status at Marston Campus", 195)]
    rows_t83 = [
        ("Location-Specific Condition", "Personal Care provided only from 78 & 80 Marston Gardens", "Fully accepted; aligns with Statement of Purpose Part 3"),
        ("Nominated Manager Condition", "Registered Manager must be registered within 3 months", "Candidate manager concurrently applying; zero vacancy risk"),
        ("Age Range Condition", "Services provided only to persons aged 18 to 65 years", "Fully codified in admission criteria and commissioning terms")
    ]
    y = p8.draw_booktabs_table("TABLE 8.3: CQC SECTION 26 NOTICE OF PROPOSAL (NOP) STATUTORY CONDITIONS", cols_t83, rows_t83, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p8.draw_section_heading("8.1", "Requests for Further Information (RFI) Fast-Response Protocol", y)
    p8_rfi_txt = (
        "During document validation and assessment, inspectors frequently issue Requests for Further Information (RFIs). "
        "ADOV Care Group enforces a strict 48-hour submission SLA, utilizing pre-audited evidence dossiers to prevent application stalls."
    )
    y = p8.draw_wrapped_text(p8_rfi_txt, p8.mx, y, p8.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 8.4: RFI Protocol
    cols_t84 = [("Typical CQC RFI Focus", 125), ("Inspector Clarification Trigger", 195), ("Pre-Audited 48-Hour Evidence Submission", 195)]
    rows_t84 = [
        ("Landlord-Care Separation", "Clarification of AST versus care package terms", "Executed commercial head lease, sample AST, de-linking clause"),
        ("Night Hub Lone-Working", "Safety of shared night staff across 78 & 80", "Unified night risk assessment, L1 alarm interconnect cert"),
        ("Working Capital Verification", "Evidence of cleared unencumbered funds", "Live Barclays Bank escrow certificate showing cleared £150,000"),
        ("Premises Fire Sign-Off", "Building control and fire service approvals", "Approved Inspector completion cert and L1 commissioning sign-off")
    ]
    y = p8.draw_booktabs_table("TABLE 8.4: CQC REQUEST FOR FURTHER INFORMATION (RFI) FAST-RESPONSE PROTOCOL", cols_t84, rows_t84, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p8.draw_section_heading("8.2", "Section 28(3) Fast-Track Waiver vs Standard 28-Day Representation", y)
    p8_waiver_txt = (
        "Under Section 27 and 28 of the Health and Social Care Act 2008, providers are entitled to a 28-day window to make written "
        "representations against an NOP. Section 28(3) permits providers to waive this period in writing, enabling CQC to issue the final "
        "Notice of Decision immediately, saving up to four weeks."
    )
    y = p8.draw_wrapped_text(p8_waiver_txt, p8.mx, y, p8.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 8.5: Waiver Comparison
    cols_t85 = [("Procedural Stage", 125), ("Standard Section 27/28 Route", 195), ("Fast-Track Section 28(3) Waiver Route", 195)]
    rows_t85 = [
        ("Statutory Hold Period", "Mandatory 28-day statutory waiting period", "Hold period completely eliminated upon receipt of written waiver"),
        ("Notice of Decision (NOD)", "Issued 4 to 6 weeks after NOP receipt", "Issued within 48 to 72 hours of waiver delivery to inspectorate"),
        ("Commissioning Activation", "Delayed to Month 5 (incurring idle costs)", "Activated in Month 4; accelerates £110k in placement fees"),
        ("Conditions Acceptance", "Implied acceptance upon expiry of 28 days", "Formal unconditional acceptance executed immediately by Board")
    ]
    y = p8.draw_booktabs_table("TABLE 8.5: STATUTORY REPRESENTATION WAIVER (SECTION 28(3)) IMPACT AUDIT", cols_t85, rows_t85, y, row_h=9.4, font_size=5.6)
    y -= 3

    # Table 8.6: Post-Registration Checklist
    cols_t86 = [("Post-Registration Action", 125), ("Statutory Timescale", 110), ("Regulatory Destination & Compliance Goal", 280)]
    rows_t86 = [
        ("Display of Certificate", "Within 24 hours of receipt", "Prominently displayed in campus entrance and on public website"),
        ("Luton Council DPS Notice", "Within 48 hours", "Uplifts provider status on AT1115 supported living dynamic framework"),
        ("Statement of Purpose Circulation", "Immediate", "Archived in staff hub; distributed to residents, families & commissioners"),
        ("First Resident Intake", "Month 4 (Weeks 16 - 17)", "Phased intake of first 2 residents under 1:1 transition plans")
    ]
    y = p8.draw_booktabs_table("TABLE 8.6: POST-REGISTRATION STATUTORY NOTIFICATION & ACTIVATION CHECKLIST", cols_t86, rows_t86, y, row_h=9.4, font_size=5.6)
    y -= 2

    p8_callout = (
        "CRITICAL PATH EXECUTION DIRECTIVE: The Board of ADOV Care Group Limited mandates immediate adherence to the 16-week registration "
        "programme. All 24 core evidence files are pre-audited and ready for portal upload. The Registered Manager and Nominated Individual "
        "are instructed to execute the Section 28(3) waiver immediately upon receipt of the Section 26 Notice of Proposal to expedite activation."
    )
    y = p8.draw_academic_callout("CRITICAL PATH EXECUTION DIRECTIVE", p8_callout, y, h=30)
    print("Page 8 final y =", y)
    return p8


# --- PAGE 9 ---
def add_p9(pdf):
    p9 = pdf.add_page()
    p9.draw_academic_header("SECTION 9.0", "SECTION 28(3) FAST-TRACK & COMMISSIONING")
    
    y = p9.height - 48
    y = p9.draw_section_heading("9.0", "SECTION 28(3) FAST-TRACK STATUTORY REPRESENTATION WAIVER PROCEDURE", y)
    
    p9_txt = (
        "Under Section 26 of the Health and Social Care Act 2008, when the Care Quality Commission proposes to grant an application "
        "for registration subject to conditions, it must serve a formal Notice of Proposal (NOP). Normally, Section 27 and 28 afford "
        "the applicant a 28-day statutory window to submit written representations. However, Section 28(3) provides a critical "
        "fast-track mechanism: if the applicant informs the Commission in writing that it does not intend to make representations, "
        "the Commission is legally empowered to issue the final Notice of Decision (NOD) and Certificate of Registration immediately. "
        "This statutory waiver compresses the registration timeline by four full weeks, preventing £110,000 in idle holding costs."
    )
    y = p9.draw_wrapped_text(p9_txt, p9.mx, y, p9.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # FORMAL SECTION 28(3) WAIVER LETTER BOX (Academic Framed Style)
    p9.set_fill_color(0.08, 0.14, 0.24)
    p9.draw_text("STATUTORY INSTRUMENT: FORMAL SECTION 28(3) REPRESENTATION WAIVER LETTER", p9.mx, y, font="F2", size=7.2)
    y -= 5
    
    box_h = 86
    box_y = y - box_h
    p9.set_fill_color(0.985, 0.99, 1.0)
    p9.set_stroke_color(0.08, 0.14, 0.24)
    p9.draw_rect(p9.mx, box_y, p9.cw, box_h, fill=True, stroke=True, stroke_w=0.8)
    
    # Header bar
    p9.set_fill_color(0.08, 0.14, 0.24)
    p9.draw_text("TO: THE REGISTRATION INSPECTORATE // CARE QUALITY COMMISSION (NATIONAL REGISTRATION TEAM)", p9.mx + 10, box_y + box_h - 12, font="F2", size=6.6)
    p9.set_stroke_color(0.76, 0.61, 0.22)
    p9.draw_line(p9.mx + 10, box_y + box_h - 15, p9.mx + p9.cw - 10, box_y + box_h - 15, stroke_w=0.6)
    
    waiver_body = (
        "APPLICATION REFERENCE: CQC-APP-2026-MG05 // APPLICANT: ADOV CARE GROUP LIMITED (CO. NO. 14289650)\n"
        "LOCATION: 78 & 80 MARSTON GARDENS, LUTON, BEDFORDSHIRE, LU2 7DY // REGULATED ACTIVITY: PERSONAL CARE\n\n"
        "FORMAL STATUTORY NOTICE UNDER SECTION 28(3) OF THE HEALTH AND SOCIAL CARE ACT 2008:\n"
        "1. UNCONDITIONAL ACCEPTANCE: ADOV Care Group Limited hereby confirms receipt of the Section 26 Notice of Proposal (NOP) "
        "and unreservedly accepts all standard and location-specific registration conditions contained therein without amendment.\n"
        "2. IRREVOCABLE WAIVER OF REPRESENTATIONS: Pursuant to Section 28(3) of the Health and Social Care Act 2008, the applicant "
        "hereby gives formal written notice that it does not intend to submit written representations under Section 27 of the Act.\n"
        "3. REQUEST FOR IMMEDIATE NOTICE OF DECISION: The Commission is respectfully requested to dispense with the remaining 28-day "
        "statutory hold period and issue the final Notice of Decision under Section 28(1) and Certificate of Registration forthwith."
    )
    p9.set_fill_color(0.12, 0.16, 0.24)
    p9.draw_wrapped_text(waiver_body, p9.mx + 10, box_y + box_h - 23, p9.cw - 20, font="F1", size=5.8, leading=7.4)
    
    # Signatures
    p9.set_stroke_color(0.70, 0.78, 0.88)
    p9.draw_line(p9.mx + 10, box_y + 12, p9.mx + 200, box_y + 12, stroke_w=0.6)
    p9.draw_line(p9.mx + 250, box_y + 12, p9.mx + 440, box_y + 12, stroke_w=0.6)
    p9.set_fill_color(0.08, 0.14, 0.24)
    p9.draw_text("Director / Nominated Individual (Reg 6)", p9.mx + 10, box_y + 4, font="F2", size=5.6)
    p9.draw_text("Registered Manager Nominee (Reg 7)", p9.mx + 250, box_y + 4, font="F2", size=5.6)
    
    y = box_y - 6
    
    y = p9.draw_section_heading("9.1", "Commissioning Activation: Luton Borough Council DPS & BLMK ICB", y)
    p9_comm_txt = (
        "Upon receipt of the CQC Certificate of Registration, ADOV Care Group Limited immediately activates its approved status on the "
        "Luton Borough Council Dynamic Purchasing System (DPS Contract Ref: AT1115) for Supported Living. In parallel, direct spot-purchasing "
        "contracts are activated with the Bedfordshire, Luton and Milton Keynes Integrated Care Board (BLMK ICB) for complex Continuing Healthcare (CHC)."
    )
    y = p9.draw_wrapped_text(p9_comm_txt, p9.mx, y, p9.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # Table 9.0: Procurement Activation
    cols_t90 = [("Commissioning Body", 125), ("Framework / Procurement Route", 185), ("Target Client Group & Placement Type", 200)]
    rows_t90 = [
        ("Luton Borough Council", "DPS Framework Contract Ref: AT1115", "Adults with autism & severe learning disability (Supported Living)"),
        ("Bedfordshire, Luton & MK ICB", "NHS Continuing Healthcare (CHC) Spot Contract", "High-dependency complex autism with 2:1 daytime PBS requirements"),
        ("Central Bedfordshire Council", "Cross-Borders Specialist Placement Framework", "Repatriation of complex young adults placed in out-of-county units"),
        ("Bedford Borough Council", "Inter-Authority Spot Commissioning Agreement", "Bespoke individual packages for adults with severe sensory distress")
    ]
    y = p9.draw_booktabs_table("TABLE 9.0: STATUTORY COMMISSIONING PROCUREMENT ACTIVATION MATRIX", cols_t90, rows_t90, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 9.1: Tariff Tiers
    cols_t91 = [("Placement Tariff Tier", 110), ("Assessed Dependency Level", 185), ("Frontline Staffing Ratio", 115), ("Weekly Placement Fee", 100)]
    rows_t91 = [
        ("Tier 1: Core Supported Living", "Moderate autism, basic life-skills prompting", "1:1 shared daytime cover", "£2,450 / bed / week"),
        ("Tier 2: Enhanced Autism Support", "High sensory sensitivity, verbal distress", "1:1 dedicated daytime cover", "£2,950 / bed / week"),
        ("Tier 3: Complex PBS High-Need", "Severe challenging behaviour, active PBS plan", "2:1 dedicated daytime cover", "£3,600 / bed / week"),
        ("Tier 4: Exceptional CHC Tariff", "Profound distress, dual medical/sensory needs", "2:1 continuous 24/7 staffing", "£4,250 / bed / week")
    ]
    y = p9.draw_booktabs_table("TABLE 9.1: HIGH-DEPENDENCY PLACEMENT FEE SCHEDULE & TARIFF STRUCTURE", cols_t91, rows_t91, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 9.2: Contractual KPIs
    cols_t92 = [("Commissioning KPI Vector", 125), ("Luton DPS Contract AT1115 Standard", 195), ("Campus Performance Assurance Mechanism", 195)]
    rows_t92 = [
        ("Safeguarding Incident Threshold", "Zero preventable severe harm incidents", "2:1 low-arousal de-escalation; immediate s.42 notification"),
        ("Oliver McGowan Compliance", "100% staff Tier 2 certified prior to care delivery", "Certified training records verified in commissioning portal"),
        ("Placement Stability & Retention", "Zero unplanned placement breakdowns or evictions", "Structured 4-stage transition pathway and dedicated PBS lead"),
        ("CQC Quality Rating Benchmark", "Maintain minimum CQC Good rating across all 5 SAF keys", "Quarterly independent Regulation 17 audits; digital audit logs")
    ]
    y = p9.draw_booktabs_table("TABLE 9.2: COMMISSIONING KEY PERFORMANCE INDICATORS (KPIS) & QUALITY METRICS", cols_t92, rows_t92, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p9.draw_section_heading("9.2", "Initial Resident Referral Pipeline, Repatriation & Compatibility Screening", y)
    p9_pipe_txt = (
        "In close collaboration with Luton Borough Council Adult Social Care and the BLMK ICB, 12 potential placement candidates "
        "have been pre-screened for local repatriation from distant out-of-county facilities. The phased move-in schedule guarantees "
        "compatibility and steady revenue onboarding."
    )
    y = p9.draw_wrapped_text(p9_pipe_txt, p9.mx, y, p9.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 9.3: Referral Pipeline
    cols_t93 = [("Candidate Code", 100), ("Current Out-of-Area Placement", 155), ("Funding Authority", 130), ("Tariff Tier & Planned Intake", 125)]
    rows_t93 = [
        ("Candidate A (Age 22)", "Northamptonshire independent unit", "Luton Borough Council", "Tier 3 PBS (£3,600/wk) // Month 4"),
        ("Candidate B (Age 26)", "Hertfordshire specialist hospital", "BLMK ICB (NHS CHC)", "Tier 4 Complex (£4,250/wk) // Month 4"),
        ("Candidate C (Age 29)", "Cambridgeshire residential facility", "Luton Borough Council", "Tier 2 Enhanced (£2,950/wk) // Month 5"),
        ("Candidate D (Age 24)", "Milton Keynes out-of-area home", "BLMK ICB (NHS CHC)", "Tier 3 PBS (£3,600/wk) // Month 5")
    ]
    y = p9.draw_booktabs_table("TABLE 9.3: INITIAL RESIDENT REPATRIATION PIPELINE & INTAKE TIMETABLE", cols_t93, rows_t93, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p9.draw_section_heading("9.3", "Social Value Act 2012 & Annual Price Indexation Governance", y)
    p9_soc_txt = (
        "ADOV Care Group delivers measurable social value in Luton through local recruitment, living wage commitments, and apprenticeships. "
        "Annual contract indexation clauses safeguard operational margins against inflation."
    )
    y = p9.draw_wrapped_text(p9_soc_txt, p9.mx, y, p9.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 9.4: Social Value
    cols_t94 = [("Social Value Vector", 125), ("Statutory Standard (Social Value Act 2012)", 195), ("Contractual Commitment at Marston Campus", 195)]
    rows_t94 = [
        ("Local Employment Generation", "85% workforce recruited within 5 miles of campus", "Creates 14 permanent care jobs; Real Living Wage employer"),
        ("Specialist Care Apprenticeships", "Partnership with local Bedfordshire colleges", "2 fully funded Level 3 Adult Social Care apprentice roles"),
        ("Local Supply Chain Retention", "Refurbishment, food, and maintenance local spend", "Over £120,000 annual reinvestment into local Luton businesses")
    ]
    y = p9.draw_booktabs_table("TABLE 9.4: SOCIAL VALUE ACT 2012 LOCAL COMMUNITY & ECONOMIC CONTRIBUTION", cols_t94, rows_t94, y, row_h=9.4, font_size=5.6)
    y -= 3

    # Table 9.5: Indexation
    cols_t95 = [("Contract Indexation Vector", 125), ("Statutory Formula / Benchmark", 195), ("Fiduciary Protection for ADOV Care Group", 195)]
    rows_t95 = [
        ("Annual Staff Wage Uprating", "Real Living Wage percentage uplift formula", "Guaranteed fee adjustment covering frontline wage inflation"),
        ("Facility Operational Costs", "Consumer Price Index (CPI) annual adjustment", "Protects food, utility, and maintenance operating budgets"),
        ("Clinical Dependency Re-banding", "Formal review of assessed PBS care hours", "Immediate upward fee re-banding if resident needs escalate")
    ]
    y = p9.draw_booktabs_table("TABLE 9.5: ANNUAL COMMISSIONING PRICE REVIEW & INFLATION INDEXATION", cols_t95, rows_t95, y, row_h=9.4, font_size=5.6)
    y -= 2

    # Table 9.6: Dispute Resolution
    cols_t96 = [("Dispute Escalation Tier", 125), ("Contractual Forum & Mechanism", 195), ("Statutory Resolution Protocol", 195)]
    rows_t96 = [
        ("Tier 1: Operational Disagreement", "Informal meeting between RM & Social Worker", "5-day operational resolution SLA; mutual action plan"),
        ("Tier 2: Legal / Contractual Impasse", "Centre for Effective Dispute Resolution (CEDR)", "Binding independent arbitration; care continuity protected")
    ]
    y = p9.draw_booktabs_table("TABLE 9.6: CONTRACTUAL DISPUTE RESOLUTION & ESCALATION FRAMEWORK", cols_t96, rows_t96, y, row_h=9.4, font_size=5.6)
    y -= 2

    p9_callout = (
        "FAST-TRACK ACTIVATION MANDATE: The Board instructs the Nominated Individual to execute the Section 28(3) waiver on the day "
        "of NOP receipt. Concurrently, the Registered Manager will submit the Certificate of Registration to Luton Borough Council and "
        "the BLMK ICB to activate placement intake, achieving full 8-bed occupancy and positive cashflow by Month 4."
    )
    y = p9.draw_academic_callout("FAST-TRACK ACTIVATION MANDATE", p9_callout, y, h=30)
    print("Page 9 final y =", y)
    return p9


# --- PAGE 10 ---
def add_p10(pdf):
    p10 = pdf.add_page()
    p10.draw_academic_header("SECTION 10.0", "STATUTORY BOARD RATIFICATION & AUDIT SIGN-OFF")
    
    y = p10.height - 48
    y = p10.draw_section_heading("10.0", "STATUTORY CORPORATE RATIFICATION UNDER COMPANIES ACT 2006", y)
    
    p10_txt = (
        "In accordance with Chapter 2 of Part 13 of the Companies Act 2006 and Regulation 17 of the Health and Social Care Act 2008 "
        "(Regulated Activities) Regulations 2014, the Board of Directors of ADOV Care Group Limited has formally reviewed and ratified "
        "this Master Registration Dossier. The resolutions below establish binding corporate undertakings, ring-fence statutory working "
        "capital, and authorize executive execution of all regulatory filings."
    )
    y = p10.draw_wrapped_text(p10_txt, p10.mx, y, p10.cw, font="F1", size=6.8, leading=8.7)
    y -= 3
    
    # FORMAL STATUTORY BOARD RESOLUTION BOX
    y = p10.draw_section_heading("10.1", "Unanimous Written Resolutions of the Board of Directors", y)
    
    res_h = 115
    res_y = y - res_h
    p10.set_fill_color(0.985, 0.99, 1.0)
    p10.set_stroke_color(0.08, 0.14, 0.24)
    p10.draw_rect(p10.mx, res_y, p10.cw, res_h, fill=True, stroke=True, stroke_w=0.8)
    
    p10.set_fill_color(0.08, 0.14, 0.24)
    p10.draw_text("UNANIMOUS WRITTEN RESOLUTION OF THE BOARD OF DIRECTORS // ADOV CARE GROUP LIMITED (CO. NO. 14289650)", p10.mx + 8, res_y + res_h - 11, font="F2", size=6.8)
    p10.set_stroke_color(0.76, 0.61, 0.22)
    p10.draw_line(p10.mx + 8, res_y + res_h - 14, p10.mx + p10.cw - 8, res_y + res_h - 14, stroke_w=0.6)
    
    res_text = (
        "PASSED PURSUANT TO CHAPTER 2 OF PART 13 OF THE COMPANIES ACT 2006 AND ARTICLE 8 OF THE ARTICLES OF ASSOCIATION:\n\n"
        "1. ADOPTION OF MASTER REGISTRATION DOSSIER: The Board formally approves and adopts this Master Registration Dossier (Monograph "
        "No. 2026-MG-05) as the definitive corporate standard for the CQC Provider and Registered Manager applications.\n"
        "2. RATIFICATION OF STATEMENT OF PURPOSE: The four-part Statement of Purpose for 78 & 80 Marston Gardens, specifying 8 specialist "
        "supported living placements under the regulated activity of Personal Care, is hereby formally approved and signed.\n"
        "3. CONFIRMATION OF NOMINATED INDIVIDUAL & REGISTERED MANAGER: The appointment of the Nominated Individual (Regulation 6) and the "
        "sponsorship of the candidate Registered Manager (Regulation 7) are hereby ratified under Regulation 5 Fit and Proper Person criteria.\n"
        "4. RING-FENCING OF £150,000 WORKING CAPITAL: The allocation and ring-fencing of £150,000 in unencumbered liquid funds in Barclays "
        "Bank UK PLC is formally ratified in full satisfaction of CQC Regulation 13 and Form FV1 solvency requirements.\n"
        "5. MANDATE TO EXECUTE SECTION 28(3) WAIVER: Management is irrevocably instructed to execute the statutory representation waiver "
        "under Section 28(3) of the Health and Social Care Act 2008 immediately upon receipt of the CQC Section 26 Notice of Proposal."
    )
    p10.set_fill_color(0.12, 0.16, 0.24)
    p10.draw_wrapped_text(res_text, p10.mx + 8, res_y + res_h - 22, p10.cw - 16, font="F1", size=5.8, leading=7.3)
    y = res_y - 4
    
    y = p10.draw_section_heading("10.2", "Statutory Signatory Register & Executive Ratification", y)
    
    # Table 10.0: Signatory Register
    cols_t100 = [("Corporate Officer / Signatory", 130), ("Capacity & Legal Role", 135), ("Statutory Endorsement", 150), ("Execution Date", 100)]
    rows_t100 = [
        ("Managing Director & Shareholder", "FAIRYTALES GROUP / ADOV LIMITED", "Adopted on behalf of the Ultimate Parent Board", "29th October 2026"),
        ("Nominated Individual (Reg 6)", "ADOV Care Group LIMITED", "Statutory Board Accountability Confirmed", "29th October 2026"),
        ("Registered Manager Nominee (Reg 7)", "Level 5 Leadership & Management", "Clinical Governance & Operational Assent", "29th October 2026"),
        ("Chartered Certified Accountant", "Fellow Chartered Accountant (FCCA)", "Regulation 13 Form FV1 Solvency Certified", "29th October 2026")
    ]
    y = p10.draw_booktabs_table("TABLE 10.0: STATUTORY SIGNATORY REGISTER & CORPORATE ENDORSEMENT", cols_t100, rows_t100, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 10.1: Continuous Audit Schedule
    cols_t101 = [("Audit Vector", 115), ("Statutory Frequency", 90), ("Independent Auditor / Lead", 135), ("Mandated Regulatory Standard", 175)]
    rows_t101 = [
        ("CQC Regulation 17 Quality Audit", "Quarterly", "Independent Care Consultant", "Comprehensive mock inspection under 34 Quality Statements"),
        ("PBS & Restrictive Practice Audit", "Bi-Annual", "BILD Certified Behaviour Analyst", "Zero unauthorized restraint verification & RRN review"),
        ("Fire Safety Part B & PEEP Review", "Annual", "Accredited Fire Safety Assessor", "Regulatory Reform (Fire Safety) Order 2005 compliance"),
        ("Medication & STOMP Audit", "Quarterly", "Specialist Learning Disability Pharmacist", "NICE Guideline NG11 psychotropic drug reduction audit")
    ]
    y = p10.draw_booktabs_table("TABLE 10.1: CONTINUOUS REGULATION 17 QUALITY ASSURANCE & AUDIT SCHEDULE", cols_t101, rows_t101, y, row_h=9.4, font_size=5.6)
    y -= 3
    
    # Table 10.2: Five-Year Horizon
    cols_t102 = [("Strategic Milestone Horizon", 110), ("Operational & Quality Target", 180), ("Lead Governance Entity", 100), ("Statutory Fiduciary Target", 125)]
    rows_t102 = [
        ("Year 1 (2026-2027)", "Campus launch; 100% 8-bed occupancy; CQC Good rating", "Registered Manager & Board", "Break-even achieved in Month 4"),
        ("Year 2 (2027-2028)", "CQC Outstanding benchmark rating; £25k asset sinking fund", "Clinical Governance Board", "Zero compliance breach notices"),
        ("Year 3 (2028-2029)", "First statutory contract review under Luton DPS AT1115", "Nominated Individual / RM", "3-Year cumulative EBITDA £1.254m"),
        ("Year 5 (2030-2031)", "Refinancing & regional supported living expansion review", "Board of Directors", "Multi-site quality governance framework")
    ]
    y = p10.draw_booktabs_table("TABLE 10.2: FIVE-YEAR REGULATORY HORIZON & SINGLE ASSESSMENT FRAMEWORK TARGETS", cols_t102, rows_t102, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p10.draw_section_heading("10.3", "Statutory Corporate Filings & Companies House Notification Register", y)
    p10_filings_txt = (
        "Statutory compliance under the Companies Act 2006 is integrated with CQC notification regimes. All corporate filings, "
        "charges, and register entries are maintained at the registered office."
    )
    y = p10.draw_wrapped_text(p10_filings_txt, p10.mx, y, p10.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 10.3: Filings Register
    cols_t103 = [("Filing Instrument", 125), ("Statutory Authority", 110), ("Mandated Legal Standard", 155), ("Statutory Filing Deadline", 125)]
    rows_t103 = [
        ("Form PSC01 (Significant Control)", "Companies House", "Companies Act 2006 Part 21A", "Within 14 days of appointment"),
        ("Form MR01 (Charge Registration)", "Companies House", "Companies Act 2006 Part 25", "Within 21 days of lender facility"),
        ("Section 15 SoP Notification", "Care Quality Commission", "CQC (Registration) Regs Reg 12", "28 days prior to variation"),
        ("Form FV1 Financial Viability", "Care Quality Commission", "CQC (Registration) Regs Reg 13", "Accompanying initial submission"),
        ("CT600 Corporation Tax Return", "HM Revenue & Customs", "CTA 2009 s.54 & FA 2003", "Within 12 months of period end")
    ]
    y = p10.draw_booktabs_table("TABLE 10.3: STATUTORY CORPORATE FILINGS & REGULATORY REGISTER", cols_t103, rows_t103, y, row_h=9.4, font_size=5.6)
    y -= 3

    y = p10.draw_section_heading("10.4", "Master Regulatory Policy Suite & Continuous Quality Audits", y)
    p10_pol_txt = (
        "The Board ratifies a master suite of 38 operational care policies reviewed annually. Independent quarterly Regulation 17 "
        "audits ensure continuous alignment with the CQC Single Assessment Framework."
    )
    y = p10.draw_wrapped_text(p10_pol_txt, p10.mx, y, p10.cw, font="F1", size=6.6, leading=8.4)
    y -= 3

    # Table 10.4: Master Policies
    cols_t104 = [("Core Regulatory Policy", 130), ("Statutory Regulation Reference", 160), ("Lead Policy Reviewer", 115), ("Review Cadence", 110)]
    rows_t104 = [
        ("Safeguarding Adults at Risk", "HSCA 2014 Reg 13 & Care Act s.42", "Registered Manager", "Annual Mandatory Review"),
        ("Positive Behaviour Support (PBS)", "HSCA 2014 Reg 12 & RRN Standards", "PBS Specialist Lead", "Annual Mandatory Review"),
        ("Medication & STOMP Protocol", "HSCA 2014 Reg 12 & NICE SC1", "Community Pharmacist", "Annual Mandatory Review"),
        ("Regulation 20 Duty of Candour", "HSCA 2014 Reg 20", "Nominated Individual", "Annual Mandatory Review")
    ]
    y = p10.draw_booktabs_table("TABLE 10.4: MASTER REGULATORY POLICY SUITE & ANNUAL REVIEW CADENCE", cols_t104, rows_t104, y, row_h=9.4, font_size=5.6)
    y -= 3

    # Table 10.5: Post-Reg Audit Cadence
    cols_t105 = [("Governance Audit Domain", 125), ("Statutory Frequency", 110), ("Reporting Destination & Compliance Purpose", 280)]
    rows_t105 = [
        ("Independent Regulation 17 Audit", "Quarterly", "Board of Directors & CQC Single Assessment Framework evidence file"),
        ("Oliver McGowan Competency Review", "Bi-Annual", "Luton Borough Council Commissioning Portal & Skills for Care"),
        ("Fire Safety Part B & PEEP Review", "Annual", "Bedfordshire Fire & Rescue Service Statutory Compliance Logbook"),
        ("STOMP Psychotropic Drug Audit", "Quarterly", "Consultant Psychiatrist & Luton NHS Learning Disability Team"),
        ("Resident Advocacy & DoLS Review", "Bi-Annual", "Independent Mental Capacity Advocate & Luton Safeguarding Board")
    ]
    y = p10.draw_booktabs_table("TABLE 10.5: POST-REGISTRATION CONTINUOUS GOVERNANCE AUDIT MATRIX", cols_t105, rows_t105, y, row_h=9.4, font_size=5.6)
    y -= 4

    # Formal Attestation Block / Seal
    attest_h = 28
    attest_y = y - attest_h
    p10.set_fill_color(0.985, 0.99, 1.0)
    p10.set_stroke_color(0.70, 0.78, 0.88)
    p10.draw_rect(p10.mx, attest_y, p10.cw, attest_h, fill=True, stroke=True, stroke_w=0.6)
    
    p10.set_fill_color(0.08, 0.14, 0.24)
    p10.draw_text("FINAL EXECUTIVE RATIFICATION & CERTIFICATE OF STATUTORY AUTHENTICITY", p10.mx + 8, attest_y + attest_h - 9, font="F2", size=6.5)
    p10.set_stroke_color(0.76, 0.61, 0.22)
    p10.draw_line(p10.mx + 8, attest_y + attest_h - 12, p10.mx + p10.cw - 8, attest_y + attest_h - 12, stroke_w=0.5)
    
    p10_auth = (
        "IN WITNESS WHEREOF, this Master Registration Dossier (Monograph No. 2026-MG-05) has been formally ratified by the Board of Directors "
        "as an authoritative, print-ready corporate instrument. All clinical governance protocols, Statement of Purpose schedules, and financial "
        "viability statements contained herein constitute binding regulatory representations submitted to the Care Quality Commission."
    )
    p10.set_fill_color(0.15, 0.20, 0.28)
    p10.draw_wrapped_text(p10_auth, p10.mx + 8, attest_y + attest_h - 19, p10.cw - 16, font="F1", size=5.5, leading=7.0)
    y = attest_y - 6
    
    # Attribution / Footer Rule
    p10.set_stroke_color(0.70, 0.78, 0.88)
    p10.draw_line(p10.mx, y, p10.width - p10.mx, y, stroke_w=0.6)
    y -= 7
    
    p10.set_fill_color(0.35, 0.40, 0.48)
    attestation = (
        "CONFIDENTIAL & PROPRIETARY // MONOGRAPH NO. 2026-MG-05 // ADOV CARE GROUP LIMITED (CO. NO. 14289650). ALL RIGHTS RESERVED. "
        "Registered Office: 78 Marston Gardens, Luton, Bedfordshire, LU2 7DY. Certified print-ready for CQC Provider Portal submission & senior lender review."
    )
    y = p10.draw_wrapped_text(attestation, p10.mx, y, p10.cw, font="F3", size=5.5, leading=7.0)
    print("Page 10 final y =", y)
    return p10



# ==============================================================================
# COMPANION DOCX GENERATOR (OPENXML ACADEMIC MONOGRAPH)
# ==============================================================================

def build_docx():
    filename = "ADOV_Care_Group_CQC_Registration_Master_Report.docx"
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
        '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:rPr><w:b/><w:color w:val="0F1E36"/><w:sz w:val="32"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:rPr><w:b/><w:color w:val="1E3A8A"/><w:sz w:val="24"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:rPr><w:b/><w:color w:val="C29B38"/><w:sz w:val="20"/></w:rPr></w:style>'
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
        p = f'<w:p><w:pPr><w:pStyle w:val="ListParagraph"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr><w:spacing w:after="80"/></w:pPr><w:r><w:t>- {safe}</w:t></w:r></w:p>'
        doc_body.append(p)

    add_p("WORKING PAPER SERIES IN HEALTH ECONOMICS & REGULATORY POLICY // MONOGRAPH NO. 2026-MG-05", style="Heading3", bold=True, color="C29B38", space_after=60)
    add_p("CQC PROVIDER & REGISTERED MANAGER REGISTRATION MASTER DOSSIER", style="Heading1", bold=True, color="0F1E36", space_after=80)
    add_p("Statutory Application Architecture, Single Assessment Framework Alignment & Fast-Track Commissioning Strategy", style="Heading2", bold=True, color="1E3A8A", space_after=100)
    add_p("Author / Advisory Lead: Project Planned by AbdullahMamun.com", bold=True, color="C29B38", space_after=60)
    add_p("Holding Entity: FAIRYTALES GROUP (Trading Name of Mamun Limited) // Asset Co: ADOV LIMITED // OpCo: ADOV Care Group LIMITED", color="475569", space_after=60)
    add_p("Target Assets: 78 & 80 Marston Gardens, Luton, LU2 7DY // Supported Living (Class C3b)", color="475569", space_after=180)
    
    sections = [
        ("1.0 EXECUTIVE SUMMARY & STATUTORY PURPOSE", [
            "Comprehensive statutory application pack for CQC Provider and Registered Manager registration.",
            "Service Model: 8-bed specialist supported living for adults with severe autism, learning disability, and PBS needs.",
            "Statutory Regulated Activity: Personal Care (sole regulated activity applied for under HSCA 2008 Schedule 1).",
            "Financial Viability: £150,000 ring-fenced working capital buffer certified under CQC Form FV1.",
            "Fast-Track Strategy: Section 28(3) representation waiver saving 28 days of dead time."
        ]),
        ("2.0 HOUSING VS CARE STATUTORY SEPARATION", [
            "Strict compliance with CQC 'Housing with Care' doctrine (October 2015, updated under SAF).",
            "ADOV LIMITED (Asset SPV) acts as commercial landlord issuing independent Assured Shorthold Tenancies (ASTs).",
            "Eligible Exempt Accommodation housing benefit (£350/wk) covers core rent, intensive housing management, and communal facilities.",
            "ADOV Care Group LIMITED provides personal care under separate care contract; residents can change care provider without losing tenancy.",
            "Town Planning Class C3b (Supported Living) confirmed via Section 192 CLEUD; zero unregistered care home risk under HSCA 2008 s.10.",
            "Integrated Schematic: Figure 1 (Statutory Separation Architecture: Housing SPV vs Care OpCo)."
        ]),
        ("3.0 PRIMARY LEGISLATION & STATUTORY REGULATIONS", [
            "Health and Social Care Act 2008 (Regulated Activities) Regulations 2014 Fundamental Standards (Regulations 4 to 20A).",
            "Care Quality Commission (Registration) Regulations 2009 (Regulations 12 to 19 notifications).",
            "Health and Care Act 2022 Section 181 Oliver McGowan Code of Practice compliance (100% Tier 2 frontline certified).",
            "Human Rights Act 1998 (Article 8 ECHR domestic privacy) and Care Act 2014 Section 42 safeguarding enquiries."
        ]),
        ("4.0 STATEMENT OF PURPOSE (SoP) MASTER SPECIFICATION", [
            "Four-Part statutory structure: Part 1 (Provider Details), Part 2 (Aims & Objectives), Part 3 (Locations), Part 4 (Managers).",
            "Location: Contiguous 78 & 80 Marston Gardens, Luton (8 en-suite bedrooms, sensory calming pods, 24.5m garden curtilage).",
            "Inclusion Criteria: Working-age adults (18-65) with autism, learning disabilities, and sensory differences.",
            "Right Support, Right Care, Right Culture (RSRCRC) benchmarking embedded into all service delivery schedules."
        ]),
        ("5.0 GOVERNANCE ARCHITECTURE & SINGLE ASSESSMENT FRAMEWORK", [
            "Dual statutory leadership: Nominated Individual (Regulation 6) and Registered Manager (Regulation 7).",
            "CQC Regulation 5 Fit and Proper Persons Requirements (FPPR) certified with clean enhanced DBS and OH fitness declarations.",
            "14 FTE operating establishment deploying 2:1 daytime support and unified 1 Waking + 1 Sleep-in night hub.",
            "Integrated Schematic: Figure 2 (CQC Single Assessment Framework & Clinical Governance Flowchart)."
        ]),
        ("6.0 REGISTERED MANAGER CLINICAL SCENARIOS & COMPETENCY", [
            "Rigorous CQC Fit & Proper interview preparation across the 5 mandatory clinical scenarios:",
            "1. Severe Behavioural Escalation: Tier 2 PBS de-escalation; Restraint Reduction Network breakaway methods.",
            "2. Section 42 Safeguarding: Immediate clinical triage and 2-hour notification to Luton Council and Police.",
            "3. Mental Capacity Act 2005: Two-stage capacity test and Section 4 Best Interests meeting for covert medication.",
            "4. Regulation 20 Duty of Candour: Written apology and root-cause disclosure within 10 operational days.",
            "5. Whistleblowing & PIDA 1998: Independent Speak Up Guardian, zero detriment, and direct CQC escalation."
        ]),
        ("7.0 REGULATION 13 FINANCIAL VIABILITY & WORKING CAPITAL", [
            "Statutory compliance with CQC Regulation 13 financial solvency requirements.",
            "Unencumbered £150,000 cash reserve ring-fenced in Barclays Bank UK PLC escrow account (covering 3.2 months fixed OpEx).",
            "Year 1 Revenue: £832,000 | Year 1 EBITDA: £265,000 (31.8%) | Year 3 EBITDA: £541,000 (40.6%).",
            "Breakeven Occupancy: 48.2% (3.8 beds), ensuring debt service and lease commitments are fully covered under all stresses.",
            "Integrated Visualizer: Figure 4 (Pro-Forma Operational Cashflow & Financial Viability Bar Chart)."
        ]),
        ("8.0 SIX-PHASE REGISTRATION & APPROVAL ROADMAP", [
            "End-to-end 16-week critical path sequence from pre-application DBS checks to final Certificate of Registration.",
            "Phase 1: Pre-App Governance -> Phase 2: Portal Uploads (24 files) -> Phase 3: Validation Hold -> Phase 4: CQC Interviews.",
            "Phase 5: Section 26 Notice of Proposal & Section 28(3) Waiver -> Phase 6: Certificate of Registration Issued.",
            "Integrated Schematic: Figure 3 (The 6-Phase CQC Registration & Section 28(3) Fast-Track Timeline)."
        ]),
        ("9.0 SECTION 28(3) WAIVER & COMMISSIONING ACTIVATION", [
            "Statutory Section 28(3) representation waiver letter dispensing with 28-day holding period.",
            "Commissioning Activation: Luton Borough Council Supported Living DPS (Contract Ref: AT1115).",
            "BLMK ICB spot purchasing for complex Continuing Healthcare (CHC) placements (£2,800 to £4,250/bed/week).",
            "Pre-screened referral pipeline: 12 potential candidates identified for local repatriation, achieving Month 4 break-even."
        ]),
        ("10.0 STATUTORY BOARD RATIFICATION & AUDIT SIGN-OFF", [
            "Unanimous Written Resolutions of the Board of Directors of ADOV Care Group Limited under Companies Act 2006.",
            "Ratification of Statement of Purpose, Nominated Individual, Registered Manager, and £150,000 liquidity buffer.",
            "Mandate to execute Section 28(3) representation waiver immediately upon receipt of NOP.",
            "Continuous Regulation 17 Quality Audit schedule and 5-year single assessment framework performance milestones."
        ])
    ]

    for sec_title, bullets in sections:
        add_p(sec_title, style="Heading2", bold=True, color="0F1E36", space_after=80)
        for b in bullets:
            add_bullet(b)

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
    print(f"Generated Academic DOCX '{filename}'.")


def build_pdf():
    pdf_filename = "ADOV_Care_Group_CQC_Registration_Master_Report.pdf"
    pdf = SimplePDF(pdf_filename)
    add_p1(pdf)
    add_p2(pdf)
    add_p3(pdf)
    add_p4(pdf)
    add_p5(pdf)
    add_p6(pdf)
    add_p7(pdf)
    add_p8(pdf)
    add_p9(pdf)
    add_p10(pdf)
    pdf.save()
    print(f"Master CQC Registration PDF compiled successfully: {pdf_filename}")


if __name__ == "__main__":
    build_pdf()
    build_docx()
