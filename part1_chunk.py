#!/usr/bin/env python3
"""
ADOV Care Group - Strategic Campus Location & Operational Appraisal
Unified Campus (78 & 80 Marston Gardens) vs. Disconnected Properties (78 & 82 Marston Gardens)

Author / Strategic Attribution: Project Planned by AbdullahMamun.com
Holding Entity: FAIRYTALES GROUP (Trading Name of Mamun Limited)
Asset Company: ADOV LIMITED
Operating Care Company: ADOV Care Group LIMITED
Target Assets: 78, 80 & 82 Marston Gardens, Luton, Bedfordshire, LU2 7DY

Format: Plain University / Scholarly Working Paper Monograph (Oxford/Cambridge Style).
Printer Ink Friendly: Pure white background, zero dark blocks, clean hairline rules (0.5-0.8pt),
traditional Booktabs tables, zero overlapping text, generous vertical leading, 10 spacious pages.
Integrated Clean Vector Schematics: Figures 1, 2, 3, and 4.
Produces:
1. ADOV_Care_Group_Campus_Strategy_Appraisal.pdf (10 Pages)
2. ADOV_Care_Group_Campus_Strategy_Appraisal.docx (Matching Academic Companion)
"""

import os
import sys
import zlib
import zipfile

# ==============================================================================
# PDF GENERATOR ENGINE (PURE PYTHON, ZERO EXTERNAL DEPENDENCIES)
# ==============================================================================

class SimplePDF:
    def __init__(self, filename, title="ADOV CARE GROUP // STRATEGIC APPRAISAL MONOGRAPH"):
        self.filename = filename
        self.doc_title = title
        self.pages = []
        self.width = 595.28  # A4 width in pt
        self.height = 841.89 # A4 height in pt
        self.mx = 40.0       # Left/Right margin (academic standard)
        self.cw = self.width - 2 * self.mx

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
        
        out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
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
        out.extend(f"xref\n0 {current_obj_id}\n0000000000 65535 f \n".encode('latin1'))
        for i in range(1, current_obj_id):
            out.extend(f"{offsets[i]:010d} 00000 n \n".encode('latin1'))
            
        out.extend(f"trailer\n<< /Size {current_obj_id} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode('latin1'))
        
        with open(self.filename, "wb") as f:
            f.write(out)
        print(f"Generated Academic PDF: {self.filename} ({len(out)} bytes, {len(self.pages)} pages)")


class SimplePDFPage:
    def __init__(self, width, height, mx, is_cover, doc_title, page_label):
        self.width = width
        self.height = height
        self.mx = mx
        self.cw = width - 2 * mx
        self.is_cover = is_cover
        self.doc_title = doc_title
        self.page_label = page_label
        self.ops = []

    def escape(self, text):
        return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    def set_fill_color(self, r, g, b):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")

    def set_stroke_color(self, r, g, b):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} RG")

    def draw_rect(self, x, y, w, h, fill=True, stroke=False, stroke_w=0.8):
        if stroke:
            self.ops.append(f"{stroke_w:.2f} w")
        op = "B" if (fill and stroke) else ("f" if fill else "S")
        self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}")

    def draw_line(self, x1, y1, x2, y2, stroke_w=0.8):
        self.ops.append(f"{stroke_w:.2f} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")

    def draw_text(self, text, x, y, font="F1", size=10, align="left", max_w=None):
        safe = self.escape(text)
        if align == "center" and max_w:
            approx_w = len(text) * size * 0.49
            x = x + max(0, (max_w - approx_w) / 2)
        elif align == "right" and max_w:
            approx_w = len(text) * size * 0.49
            x = x + max_w - approx_w
        self.ops.append(f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({safe}) Tj ET")

    def draw_wrapped_text(self, text, x, y, max_w, font="F1", size=7.3, leading=9.8):
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

    def draw_academic_header(self, section_num, section_title, page_category="WORKING PAPER"):
        self.set_stroke_color(0.20, 0.25, 0.32)
        self.draw_line(self.mx, self.height - 32, self.width - self.mx, self.height - 32, stroke_w=0.6)
        self.set_fill_color(0.40, 0.45, 0.55)
        self.draw_text(f"{page_category} // {self.doc_title}", self.mx, self.height - 27, font="F2", size=6.5)
        self.draw_text(f"{section_num}: {section_title}", self.width - self.mx, self.height - 27, font="F1", size=6.5, align="right", max_w=240)

    def draw_section_heading(self, num, title, y):
        self.set_fill_color(0.08, 0.14, 0.24)
        full_title = f"{num}  {title}" if num else title
        self.draw_text(full_title, self.mx, y, font="F2", size=8.8)
        self.set_stroke_color(0.76, 0.61, 0.22)
        self.draw_line(self.mx, y - 4, self.width - self.mx, y - 4, stroke_w=0.8)
        return y - 16

    def draw_academic_callout(self, title, text, y, h=50):
        self.set_fill_color(0.985, 0.99, 1.0)
        self.set_stroke_color(0.70, 0.78, 0.88)
        self.draw_rect(self.mx, y - h, self.cw, h, fill=True, stroke=True, stroke_w=0.6)
        self.set_fill_color(0.76, 0.61, 0.22)
        self.draw_rect(self.mx, y - h, 2.5, h, fill=True)
        self.set_fill_color(0.08, 0.14, 0.24)
        self.draw_text(title, self.mx + 8, y - 11, font="F2", size=7.4)
        self.set_fill_color(0.15, 0.20, 0.28)
        self.draw_wrapped_text(text, self.mx + 8, y - 22, self.cw - 16, font="F1", size=6.7, leading=8.6)
        return y - h - 10

    def draw_booktabs_table(self, title, cols, rows, y, row_h=12.0, font_size=6.4):
        cur_y = y
        if title:
            self.set_fill_color(0.08, 0.14, 0.24)
            self.draw_text(title, self.mx, cur_y, font="F2", size=7.6)
            cur_y -= 6
            
        self.set_stroke_color(0.08, 0.14, 0.24)
        self.draw_line(self.mx, cur_y, self.width - self.mx, cur_y, stroke_w=1.1)
        cur_y -= 10
        
        cur_x = self.mx + 4
        for h_txt, h_w in cols:
            self.set_fill_color(0.08, 0.14, 0.24)
            self.draw_text(h_txt, cur_x, cur_y, font="F2", size=font_size + 0.4)
            cur_x += h_w
        cur_y -= 4
        self.draw_line(self.mx, cur_y, self.width - self.mx, cur_y, stroke_w=0.6)
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
                self.draw_text(str(val), cur_x, cur_y + 1, font=f_use, size=font_size)
                cur_x += cols[c_idx][1]
                
        cur_y -= 2
        self.set_stroke_color(0.08, 0.14, 0.24)
        self.draw_line(self.mx, cur_y, self.width - self.mx, cur_y, stroke_w=1.1)
        return cur_y - 10

    def render(self, page_num, total_pages):
        res = []
        if not self.is_cover:
            res.append("0.400 0.450 0.550 RG")
            res.append(f"0.50 w {self.mx:.2f} 38.00 m {self.width - self.mx:.2f} 38.00 l S")
            res.append("0.400 0.450 0.550 rg")
            res.append(f"BT /F1 6.80 Tf {self.mx:.2f} 26.00 Td (ADOV CARE GROUP // STRATEGIC CAMPUS LOCATION APPRAISAL) Tj ET")
            res.append(f"BT /F2 6.80 Tf {self.width - self.mx - 140:.2f} 26.00 Td (Page {page_num} of {total_pages}) Tj ET")
            res.append(f"BT /F3 6.00 Tf {self.mx + 220:.2f} 26.00 Td (Project Planned by AbdullahMamun.com) Tj ET")
        return "\n".join(self.ops + res)
