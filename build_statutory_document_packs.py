#!/usr/bin/env python3
"""
ADOV Care Group - Master Statutory & Operational Document Pack Generator
Generates print-ready PDFs and Word DOCX documents in the style of 
peer-reviewed university research journals and institutional board monographs.

Standards:
- Standard ISO A4 (595.28 pt x 841.89 pt / 210mm x 297mm)
- 100% Crisp Plain White Paper (Zero ink-wasting dark covers or backgrounds)
- Low-Ink Ergonomics (Thin hairline rules, subtle 2% grey tints, Lancet/AER table styling)
- Type1 PostScript Fonts: /Helvetica, /Helvetica-Bold, /Helvetica-Oblique
- Academic Running Headers & Footers with dynamic 'Page X of Y' pagination
- Zero Duplication, Highly Readable, Board Meeting Ready
"""

import os
import sys
import zlib
import zipfile

class SimplePDF:
    def __init__(self, filename, title="ADOV CARE GROUP - STATUTORY DOCUMENT"):
        self.filename = filename
        self.doc_title = title
        self.pages = []
        self.width = 595.28
        self.height = 841.89
        self.mx = 40.0
        self.mt = 40.0
        self.mb = 40.0
        self.cw = self.width - 2 * self.mx

    def add_page(self, is_cover=False, page_label=""):
        page = SimplePDFPage(self.width, self.height, self.mx, self.mt, self.mb, is_cover, self.doc_title, page_label)
        self.pages.append(page)
        return page

    def save(self):
        objects = []
        objects.append("<< /Type /Catalog /Pages 2 0 R >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>")
        
        current_obj_id = 6
        page_obj_ids = []
        content_obj_ids = []
        
        for i, page in enumerate(self.pages):
            page_obj_id = current_obj_id
            content_obj_id = current_obj_id + 1
            current_obj_id += 2
            page_obj_ids.append(page_obj_id)
            content_obj_ids.append(content_obj_id)
            
            stream_data = page.render(page_num=i+1, total_pages=len(self.pages))
            compressed = zlib.compress(stream_data.encode('cp1252', errors='replace'))
            content_obj = f"<< /Length {len(compressed)} /Filter /FlateDecode >>\nstream\n".encode('latin1') + compressed + b"\nendstream"
            
            page_dict = (
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.width:.2f} {self.height:.2f}] "
                f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> "
                f"/Contents {content_obj_id} 0 R >>"
            )
            objects.append(page_dict)
            objects.append(content_obj)
            
        kids_str = " ".join([f"{pid} 0 R" for pid in page_obj_ids])
        pages_dict = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(page_obj_ids)} >>"
        
        out = bytearray()
        out.extend(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = {}
        
        offsets[1] = len(out)
        out.extend(f"1 0 obj\n{objects[0]}\nendobj\n".encode('latin1'))
        
        offsets[2] = len(out)
        out.extend(f"2 0 obj\n{pages_dict}\nendobj\n".encode('latin1'))
        
        for font_id, font_str in [(3, objects[1]), (4, objects[2]), (5, objects[3])]:
            offsets[font_id] = len(out)
            out.extend(f"{font_id} 0 obj\n{font_str}\nendobj\n".encode('latin1'))
            
        obj_idx = 4
        for obj_id in range(6, current_obj_id):
            item = objects[obj_idx]
            offsets[obj_id] = len(out)
            if isinstance(item, bytes):
                out.extend(f"{obj_id} 0 obj\n".encode('latin1'))
                out.extend(item)
                out.extend(b"\nendobj\n")
            else:
                out.extend(f"{obj_id} 0 obj\n{item}\nendobj\n".encode('latin1'))
            obj_idx += 1
            
        xref_offset = len(out)
        out.extend(f"xref\n0 {current_obj_id}\n".encode('latin1'))
        out.extend(b"0000000000 65535 f \n")
        for i in range(1, current_obj_id):
            offset = offsets[i]
            out.extend(f"{offset:010d} 00000 n \n".encode('latin1'))
            
        out.extend(f"trailer\n<< /Size {current_obj_id} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode('latin1'))
        
        with open(self.filename, "wb") as f:
            f.write(out)
        print(f"✓ Generated Academic Journal PDF '{self.filename}' ({len(out):,} bytes, {len(self.pages)} pages).")


class SimplePDFPage:
    def __init__(self, width, height, mx, mt, mb, is_cover, doc_title, page_label):
        self.width = width
        self.height = height
        self.mx = mx
        self.mt = mt
        self.mb = mb
        self.cw = width - 2 * mx
        self.is_cover = is_cover
        self.doc_title = doc_title
        self.page_label = page_label
        self.ops = []
        self.curr_fill = (0.10, 0.14, 0.20)
        self.curr_stroke = (0.08, 0.16, 0.28)

    @property
    def margin_x(self):
        return self.mx

    @property
    def margin_top(self):
        return self.mt

    @property
    def margin_bottom(self):
        return self.mb

    @property
    def content_w(self):
        return self.cw

    @property
    def page_type(self):
        return "cover" if self.is_cover else "content"

    @page_type.setter
    def page_type(self, val):
        self.is_cover = (val == "cover")

    def escape(self, text):
        replacements = {
            '\u2022': chr(149),
            '\u2013': '-',
            '\u2014': '--',
            '\u2018': "'",
            '\u2019': "'",
            '\u201c': '"',
            '\u201d': '"',
            '£': chr(163),
            '≥': '>=',
            '≤': '<=',
            '→': '->',
            '✓': '[YES]',
            '✗': '[NO]',
            '☐': '[ ]',
            '☑': '[X]',
            '•': chr(149)
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

    def set_fill_color(self, r, g, b):
        self.curr_fill = (r, g, b)

    def set_stroke_color(self, r, g, b):
        if r > 0.7 and g > 0.5 and b < 0.3:
            r, g, b = 0.08, 0.16, 0.28
        self.curr_stroke = (r, g, b)
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} RG")

    def draw_rect(self, x, y, w, h, fill=True, stroke=False, stroke_w=0.75):
        # 1. Suppress full page dark background fills on cover or interior
        if fill and w >= (self.width - 20) and h >= (self.height - 20):
            return

        # 1b. Suppress top/bottom edge color stripes
        if (y >= self.height - 16 or y <= 4) and w >= (self.width - 20):
            return

        # 2. Suppress heavy decorative double gold border boxes or full frames on cover
        if (stroke and not fill and (w >= self.width - 70 and h >= self.height - 70)) or \
           (self.is_cover and w >= (self.width - 100) and h >= (self.height - 120)):
            return

        r, g, b = self.curr_fill
        lum = 0.299 * r + 0.587 * g + 0.114 * b

        # 3. If filling a dark rectangle (banner, card, or table header):
        if fill and lum < 0.40:
            r, g, b = 0.965, 0.972, 0.982
            self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")
            self.ops.append("0.820 0.850 0.900 RG 0.50 w")
            self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re B")
            if w > 120 and h > 25:
                self.ops.append("0.080 0.160 0.280 rg")
                self.ops.append(f"{x:.2f} {y:.2f} 2.50 {h:.2f} re f")
            return

        # 4. If filling a gold box/pill:
        if fill and (r > 0.7 and g > 0.5 and b < 0.3):
            r, g, b = 0.950, 0.955, 0.965
            self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")
            self.ops.append("0.080 0.160 0.280 RG 0.50 w")
            self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re B")
            return

        # Standard rect
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")
        if stroke:
            self.ops.append(f"{stroke_w:.2f} w")
        op = "B" if (fill and stroke) else ("f" if fill else "S")
        self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}")

    def draw_line(self, x1, y1, x2, y2, stroke_w=0.75):
        self.ops.append(f"{stroke_w:.2f} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")

    def draw_text(self, text, x, y, font="F1", size=10, align="left", max_w=None):
        r, g, b = self.curr_fill
        lum = 0.299 * r + 0.587 * g + 0.114 * b

        if lum > 0.80:
            r, g, b = 0.10, 0.14, 0.20 # Charcoal
        elif (r > 0.7 and g > 0.5 and b < 0.3): # gold
            r, g, b = 0.08, 0.16, 0.28 # Oxford Navy

        safe = self.escape(text)
        if align == "center" and max_w:
            approx_w = len(text) * size * 0.49
            x = x + max(0, (max_w - approx_w) / 2)
        elif align == "right" and max_w:
            approx_w = len(text) * size * 0.49
            x = x + max_w - approx_w

        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")
        self.ops.append(f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({safe}) Tj ET")

    def draw_wrapped_text(self, text, x, y, max_w, font="F1", size=7.8, leading=10.2):
        r, g, b = self.curr_fill
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        if lum > 0.80:
            r, g, b = 0.12, 0.16, 0.22
        elif (r > 0.7 and g > 0.5 and b < 0.3):
            r, g, b = 0.08, 0.16, 0.28

        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")

        words = text.split()
        lines = []
        current_line = []
        char_w = size * 0.48
        max_chars = max(1, int(max_w / char_w))

        for w in words:
            test_line = " ".join(current_line + [w])
            if len(test_line) > max_chars and current_line:
                lines.append(" ".join(current_line))
                current_line = [w]
            else:
                current_line.append(w)
        if current_line:
            lines.append(" ".join(current_line))

        cur_y = y
        for line in lines:
            safe = self.escape(line)
            self.ops.append(f"BT /{font} {size:.2f} Tf {x:.2f} {cur_y:.2f} Td ({safe}) Tj ET")
            cur_y -= leading
        return cur_y

    def draw_header_banner(self, num_or_code, title, category="STATUTORY DOCUMENT"):
        y = self.height - 52
        
        self.ops.append("0.965 0.972 0.982 rg")
        self.ops.append("0.820 0.850 0.900 RG 0.50 w")
        self.ops.append(f"{self.mx:.2f} {y:.2f} {self.cw:.2f} 26.00 re B")
        
        self.ops.append("0.080 0.160 0.280 rg")
        self.ops.append(f"{self.mx:.2f} {y:.2f} 2.50 26.00 re f")
        
        self.ops.append("0.920 0.935 0.955 rg")
        self.ops.append("0.080 0.160 0.280 RG 0.50 w")
        self.ops.append(f"{self.mx + 8:.2f} {y + 5:.2f} 24.00 16.00 re B")
        
        self.ops.append("0.080 0.160 0.280 rg")
        safe_code = self.escape(str(num_or_code))
        self.ops.append(f"BT /F2 7.5 Tf {self.mx + 11:.2f} {y + 10:.2f} Td ({safe_code}) Tj ET")
        
        self.ops.append("0.080 0.140 0.240 rg")
        safe_title = self.escape(title)
        self.ops.append(f"BT /F2 9.0 Tf {self.mx + 38:.2f} {y + 10:.2f} Td ({safe_title}) Tj ET")
        
        self.ops.append("0.400 0.450 0.520 rg")
        safe_cat = self.escape(category)
        approx_w = len(category) * 7.0 * 0.49
        cat_x = self.width - self.mx - approx_w - 8
        self.ops.append(f"BT /F1 7.0 Tf {cat_x:.2f} {y + 10:.2f} Td ({safe_cat}) Tj ET")

    def draw_header(self, title):
        parts = title.split(". ", 1)
        code = parts[0] if len(parts) > 1 else "ADV"
        t_text = parts[1] if len(parts) > 1 else title
        self.draw_header_banner(code, t_text, category=self.doc_title[:30])

    def draw_academic_header(self, section_num, section_title, page_category="REGULATORY POLICY"):
        self.set_stroke_color(0.20, 0.25, 0.32)
        self.draw_line(self.mx, self.height - 32, self.width - self.mx, self.height - 32, stroke_w=0.6)
        self.set_fill_color(0.40, 0.45, 0.55)
        self.draw_text(f"{page_category} // {self.doc_title}", self.mx, self.height - 27, font="F2", size=6.5)
        self.draw_text("WORKING PAPER NO. 2026-MG-05", self.width - self.mx - 150, self.height - 27, font="F2", size=6.5)
        self.set_stroke_color(0.08, 0.16, 0.28)
        self.draw_line(self.mx, self.height - 35, self.mx + 45, self.height - 35, stroke_w=1.2)

    def draw_section_heading(self, code, title, y):
        cur_y = y
        self.set_fill_color(0.08, 0.16, 0.28)
        self.draw_rect(self.mx, cur_y - 2, 2.5, 9.5, fill=True)
        self.set_fill_color(0.08, 0.14, 0.24)
        full_title = f"{code} {title}".upper()
        self.draw_text(full_title, self.mx + 7, cur_y, font="F2", size=7.8)
        return cur_y - 12.0

    def draw_academic_callout(self, title, text, y, h=40):
        self.set_fill_color(0.965, 0.972, 0.982)
        self.set_stroke_color(0.820, 0.850, 0.900)
        self.draw_rect(self.mx, y - h, self.cw, h, fill=True, stroke=True, stroke_w=0.5)
        self.set_fill_color(0.080, 0.160, 0.280)
        self.draw_rect(self.mx, y - h, 2.5, h, fill=True)
        self.set_fill_color(0.080, 0.160, 0.280)
        self.draw_text(title, self.mx + 8, y - 10, font="F2", size=7.2)
        self.set_fill_color(0.12, 0.16, 0.22)
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
            bg = (0.965, 0.972, 0.982) if (r_idx % 2 == 1) else (1.0, 1.0, 1.0)
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
        if not self.is_cover:
            # 1. Academic Running Header
            res.append("0.780 0.820 0.880 RG 0.50 w")
            res.append(f"{self.mx:.2f} {self.height - 24:.2f} m {self.width - self.mx:.2f} {self.height - 24:.2f} l S")
            res.append(f"BT /F2 6.5 Tf 0.080 0.160 0.280 rg {self.mx:.2f} {self.height - 20:.2f} Td ({self.escape(self.doc_title)}) Tj ET")
            res.append(f"BT /F1 6.2 Tf 0.400 0.450 0.520 rg {self.width - self.mx - 180:.2f} {self.height - 20:.2f} Td (78, 80 & 82 MARSTON GDNS, LUTON) Tj ET")
            
            # 2. Academic Running Footer
            res.append("0.780 0.820 0.880 RG 0.50 w")
            res.append(f"{self.mx:.2f} 28.00 m {self.width - self.mx:.2f} 28.00 l S")
            res.append(f"BT /F1 6.2 Tf 0.400 0.450 0.520 rg {self.mx:.2f} 18.00 Td (CONFIDENTIAL // PREPARED FOR THE BOARD OF DIRECTORS & REGISTERED MANAGER) Tj ET")
            page_str = f"Page {page_num} of {total_pages}"
            res.append(f"BT /F2 6.5 Tf 0.080 0.160 0.280 rg {self.width - self.mx - 52:.2f} 18.00 Td ({page_str}) Tj ET")
        else:
            # Cover page academic double header rule
            res.append("0.080 0.160 0.280 RG 1.20 w")
            res.append(f"{self.mx:.2f} {self.height - 36:.2f} m {self.width - self.mx:.2f} {self.height - 36:.2f} l S")
            res.append("0.780 0.820 0.880 RG 0.50 w")
            res.append(f"{self.mx:.2f} {self.height - 38.5:.2f} m {self.width - self.mx:.2f} {self.height - 38.5:.2f} l S")
            res.append(f"BT /F2 7.0 Tf 0.080 0.160 0.280 rg {self.mx:.2f} {self.height - 48:.2f} Td (ADOV HEALTHCARE & SUPPORTED LIVING REVIEW // BOARDROOM IN-DEPTH DOSSIER) Tj ET")
            res.append(f"BT /F1 6.5 Tf 0.400 0.450 0.520 rg {self.width - self.mx - 180:.2f} {self.height - 48:.2f} Td (REF: ACG-LUTON-2026-SL // OFFICIAL SENSITIVE) Tj ET")
            
            # Cover page minimal footer
            res.append("0.780 0.820 0.880 RG 0.50 w")
            res.append(f"{self.mx:.2f} 28.00 m {self.width - self.mx:.2f} 28.00 l S")
            res.append(f"BT /F1 6.2 Tf 0.400 0.450 0.520 rg {self.mx:.2f} 18.00 Td (OFFICIAL BOARD COMMISSIONING DOSSIER // A4 UNIVERSITY RESEARCH JOURNAL SPECIFICATION) Tj ET")
            page_str = f"Page {page_num} of {total_pages}"
            res.append(f"BT /F2 6.5 Tf 0.080 0.160 0.280 rg {self.width - self.mx - 52:.2f} 18.00 Td ({page_str}) Tj ET")
            
        res.extend(self.ops)
        return "\n".join(res)

PDFDocument = SimplePDF
PDFPage = SimplePDFPage
LuxuryPDFDocument = SimplePDF
LuxuryPDFPage = SimplePDFPage

print("SimplePDF Academic Journal Engine initialized.")
