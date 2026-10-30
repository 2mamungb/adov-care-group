#!/usr/bin/env python3
"""
ADOV Care Group & Fairytales Group - Private Project Prospectus & Investment Masterplan
Statutory Feasibility, Corporate Governance, Physical Infrastructure,
4-Sector Comparative Appraisal, Commissioning & Zero-Void Execution Plan.
Target Assets: 78, 80 & 82 Marston Gardens, Luton, LU2 7DY.
Project Planned by AbdullahMamun.com
"""

import os
import sys
import zlib
import zipfile

# ==============================================================================
# PDF ENGINE (PURE PYTHON / ZERO EXTERNAL DEPENDENCIES)
# ==============================================================================

class PDFDocument:
    def __init__(self, filename="ADOV_Care_Group_Private_Project_Prospectus.pdf"):
        self.filename = filename
        self.pages = []
        self.width = 595.28
        self.height = 841.89
        self.margin_x = 36.0
        self.margin_top = 36.0
        self.margin_bottom = 36.0
        self.content_w = self.width - 2 * self.margin_x

    def add_page(self):
        page = PDFPage(self.width, self.height, self.margin_x, self.margin_top, self.margin_bottom)
        self.pages.append(page)
        return page

    def save(self):
        objects = []
        objects.append("<< /Type /Catalog /Pages 2 0 R >>")
        font_helv = 3
        font_bold = 4
        font_oblique = 5
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
                f"/Resources << /Font << /F1 {font_helv} 0 R /F2 {font_bold} 0 R /F3 {font_oblique} 0 R >> >> "
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
        print(f"Generated Prospectus PDF '{self.filename}' ({len(out)} bytes, {len(self.pages)} pages).")


class PDFPage:
    def __init__(self, width, height, mx, mt, mb):
        self.width = width
        self.height = height
        self.mx = mx
        self.mt = mt
        self.mb = mb
        self.cw = width - 2 * mx
        self.ops = []
        self.is_cover = False

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
            '✗': '[NO]'
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

    def set_fill_color(self, r, g, b):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")

    def set_stroke_color(self, r, g, b):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} RG")

    def draw_rect(self, x, y, w, h, fill=True, stroke=False, stroke_w=1.0):
        if stroke:
            self.ops.append(f"{stroke_w:.2f} w")
        op = "B" if (fill and stroke) else ("f" if fill else "S")
        self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}")

    def draw_line(self, x1, y1, x2, y2, stroke_w=1.0):
        self.ops.append(f"{stroke_w:.2f} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")

    def draw_text(self, text, x, y, font="F1", size=10, align="left", max_w=None):
        safe = self.escape(text)
        if align == "center" and max_w:
            approx_w = len(text) * size * 0.50
            x = x + max(0, (max_w - approx_w) / 2)
        elif align == "right" and max_w:
            approx_w = len(text) * size * 0.50
            x = x + max_w - approx_w
        self.ops.append(f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({safe}) Tj ET")

    def draw_wrapped_text(self, text, x, y, max_w, font="F1", size=7.8, leading=10.2):
        words = text.split()
        lines = []
        current_line = []
        char_w = size * 0.48
        max_chars = int(max_w / char_w)
        
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

    def render(self, page_num, total_pages):
        res = []
        if not self.is_cover:
            # Header
            res.append("0.15 0.25 0.40 RG 0.75 w")
            res.append(f"{self.mx:.2f} {self.height - 26:.2f} m {self.width - self.mx:.2f} {self.height - 26:.2f} l S")
            res.append(f"BT /F2 6.5 Tf 0.10 0.18 0.32 rg {self.mx:.2f} {self.height - 20:.2f} Td (PRIVATE PROJECT PROSPECTUS // FAIRYTALES GROUP & ADOV CARE GROUP // LUTON, UK) Tj ET")
            res.append(f"BT /F1 6.5 Tf 0.40 0.50 0.60 rg {self.width - self.mx - 165:.2f} {self.height - 20:.2f} Td (PRIVATE & CONFIDENTIAL // COMMERCIAL MASTERPLAN) Tj ET")
            
            # Footer
            res.append("0.80 0.85 0.90 RG 0.5 w")
            res.append(f"{self.mx:.2f} 28.00 m {self.width - self.mx:.2f} 28.00 l S")
            res.append(f"BT /F1 6.5 Tf 0.40 0.45 0.55 rg {self.mx:.2f} 18.00 Td (Private Project Prospectus & Investment Masterplan // Planned by AbdullahMamun.com // 78, 80 & 82 Marston Gdns) Tj ET")
            page_str = f"Page {page_num} of {total_pages}"
            res.append(f"BT /F2 6.5 Tf 0.10 0.18 0.32 rg {self.width - self.mx - 55:.2f} 18.00 Td ({page_str}) Tj ET")
            
        res.extend(self.ops)
        return "\n".join(res)

print("PDF Engine Class Defined.")
