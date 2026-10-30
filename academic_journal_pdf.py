#!/usr/bin/env python3
"""
ADOV Care Group - Academic Research Journal PDF Engine
Production-grade, publication-quality A4 PDF generator designed in the style of 
peer-reviewed university research journals and institutional board monographs.

Standards:
- Standard ISO A4 (595.28 pt x 841.89 pt / 210mm x 297mm)
- 100% Crisp Plain White Paper (Zero ink-wasting dark covers or backgrounds)
- Low-Ink Ergonomics (Thin hairline rules, subtle 2% grey tints, Lancet/AER table styling)
- Type1 PostScript Fonts: /Helvetica, /Helvetica-Bold, /Helvetica-Oblique
- Academic Running Headers & Footers with dynamic 'Page X of Y' pagination
- Vector Figures, Waterfall Charts, Timelines & Multi-Criteria Decision Matrices
"""

import sys, os, zlib

class AcademicJournalPDF:
    def __init__(self, filename, doc_title, doc_ref="REF: ACG-LUTON-2026", journal_name="ADOV HEALTHCARE & SUPPORTED LIVING REVIEW"):
        self.filename = filename
        self.doc_title = doc_title
        self.doc_ref = doc_ref
        self.journal_name = journal_name
        self.pages = []
        self.width = 595.28
        self.height = 841.89
        self.mx = 42.0          # Left and right margin
        self.mt = 42.0          # Top margin
        self.mb = 42.0          # Bottom margin
        self.cw = self.width - 2 * self.mx  # Content width = 511.28 pt

    def add_page(self, is_cover=False, section_title=""):
        page = JournalPage(
            width=self.width,
            height=self.height,
            mx=self.mx,
            mt=self.mt,
            mb=self.mb,
            is_cover=is_cover,
            doc_title=self.doc_title,
            doc_ref=self.doc_ref,
            journal_name=self.journal_name,
            section_title=section_title
        )
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
        print(f"✓ Generated Academic Journal PDF: '{self.filename}' ({len(out):,} bytes, {len(self.pages)} pages).")


class JournalPage:
    def __init__(self, width, height, mx, mt, mb, is_cover, doc_title, doc_ref, journal_name, section_title):
        self.width = width
        self.height = height
        self.mx = mx
        self.mt = mt
        self.mb = mb
        self.cw = width - 2 * mx
        self.is_cover = is_cover
        self.doc_title = doc_title
        self.doc_ref = doc_ref
        self.journal_name = journal_name
        self.section_title = section_title
        self.ops = []
        
        # Cursor tracking
        self.y = self.height - self.mt

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

    # --- Basic Graphics Operations ---
    def set_fill_color(self, r, g, b):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")

    def set_stroke_color(self, r, g, b):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} RG")

    def draw_rect(self, x, y, w, h, fill=True, stroke=False, stroke_w=0.75):
        if stroke:
            self.ops.append(f"{stroke_w:.2f} w")
        op = "B" if (fill and stroke) else ("f" if fill else "S")
        self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}")

    def draw_line(self, x1, y1, x2, y2, stroke_w=0.75):
        self.ops.append(f"{stroke_w:.2f} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")

    def draw_text(self, text, x, y, font="F1", size=9.0, align="left", max_w=None):
        safe = self.escape(text)
        if align == "center" and max_w:
            approx_w = len(text) * size * 0.49
            x = x + max(0, (max_w - approx_w) / 2)
        elif align == "right" and max_w:
            approx_w = len(text) * size * 0.49
            x = x + max_w - approx_w
        self.ops.append(f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({safe}) Tj ET")

    def draw_wrapped_text(self, text, x, y, max_w, font="F1", size=8.5, leading=11.5, col=None):
        if col:
            self.set_fill_color(*col)
        words = text.split()
        lines = []
        current_line = []
        char_w = size * 0.49
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

    # --- University Research Journal Layout Elements ---

    def draw_journal_cover_masthead(self, title, subtitle, authors, date_str="OCTOBER 2026", target_asset="78, 80 & 82 MARSTON GARDENS, LUTON"):
        """Draws a prestigious Academic Journal Masthead at top of Page 1"""
        y = self.height - 38
        
        # 1. Top Double Rule (Oxford / Cambridge Academic Style)
        self.set_stroke_color(0.08, 0.16, 0.28) # Deep Oxford Navy
        self.draw_line(self.mx, y, self.width - self.mx, y, stroke_w=1.5)
        self.draw_line(self.mx, y - 2.5, self.width - self.mx, y - 2.5, stroke_w=0.5)
        
        # 2. Journal Metadata Banner
        y -= 14
        self.set_fill_color(0.20, 0.26, 0.35)
        self.draw_text(self.journal_name.upper(), self.mx, y, font="F2", size=7.5)
        self.set_fill_color(0.40, 0.45, 0.52)
        self.draw_text(f"{self.doc_ref}  |  BOARDROOM POLICY DOSSIER  |  {date_str}", self.width - self.mx - 240, y, font="F1", size=7.0, align="right", max_w=240)
        
        # 3. Hairline Rule
        y -= 6
        self.set_stroke_color(0.78, 0.82, 0.88)
        self.draw_line(self.mx, y, self.width - self.mx, y, stroke_w=0.5)
        
        # 4. Main Paper Title (Bold, High-Contrast Black/Charcoal)
        y -= 22
        self.set_fill_color(0.08, 0.12, 0.18)
        self.draw_text(title, self.mx, y, font="F2", size=16.0)
        
        # 5. Subtitle
        y -= 14
        self.set_fill_color(0.30, 0.35, 0.42)
        self.draw_text(subtitle, self.mx, y, font="F1", size=9.0)
        
        # 6. Author Bylines & Institutional Affiliation
        y -= 16
        self.set_stroke_color(0.85, 0.88, 0.92)
        self.draw_line(self.mx, y, self.width - self.mx, y, stroke_w=0.5)
        
        y -= 11
        self.set_fill_color(0.15, 0.20, 0.28)
        authors_str = " • ".join(authors) if isinstance(authors, list) else authors
        self.draw_text(f"AUTHORS & INQUIRY AUDITORS: {authors_str}", self.mx, y, font="F2", size=7.0)
        
        y -= 10
        self.set_fill_color(0.40, 0.45, 0.52)
        self.draw_text(f"FACILITY LOCATION: {target_asset}  |  HOLDING: MAMUN LIMITED  |  PROPCO: ADOV LIMITED  |  OPCO: ADOV CARE GROUP", self.mx, y, font="F1", size=6.5)
        
        y -= 7
        self.set_stroke_color(0.08, 0.16, 0.28)
        self.draw_line(self.mx, y, self.width - self.mx, y, stroke_w=1.0)
        
        self.y = y - 12
        return self.y

    def draw_abstract_card(self, headline, key_findings, target_decision="Approve recommendations"):
        """Draws an authoritative academic Abstract / Executive Summary Box (low ink, 2% grey fill)"""
        box_y = self.y
        box_w = self.cw
        
        # Estimate height needed
        num_bullets = len(key_findings)
        est_h = 32 + num_bullets * 13.5 + 24
        
        # Subtle 2% Grey Fill + 0.5pt Border
        self.set_fill_color(0.975, 0.980, 0.988) # Ultra-light grey tint
        self.set_stroke_color(0.82, 0.85, 0.90)
        self.draw_rect(self.mx, box_y - est_h, box_w, est_h, fill=True, stroke=True, stroke_w=0.6)
        
        # 2.5pt Deep Navy Accent on Left Edge (Dignified Academic Touch)
        self.set_fill_color(0.08, 0.16, 0.28)
        self.draw_rect(self.mx, box_y - est_h, 3.0, est_h, fill=True, stroke=False)
        
        # Header inside box
        self.set_fill_color(0.08, 0.16, 0.28)
        self.draw_text("EXECUTIVE ABSTRACT & BOARD DECISION SUMMARY", self.mx + 12, box_y - 14, font="F2", size=8.5)
        
        self.set_fill_color(0.40, 0.45, 0.52)
        self.draw_text("STATUTORY BOARD DECISION GATING // TCPA 1990 S.192 • HSCA 2008 REGS 2014", self.mx + box_w - 240, box_y - 14, font="F1", size=6.5, align="right", max_w=230)
        
        # Headline in bold charcoal
        self.set_fill_color(0.12, 0.15, 0.20)
        cur_y = self.draw_wrapped_text(headline, self.mx + 12, box_y - 28, box_w - 24, font="F2", size=8.0, leading=10.5)
        
        # Bullet findings
        cur_y -= 4
        for bf in key_findings:
            self.set_fill_color(0.08, 0.16, 0.28)
            self.draw_text(chr(149), self.mx + 14, cur_y, font="F2", size=9.0)
            
            # Check if has bold prefix
            if ":" in bf:
                parts = bf.split(":", 1)
                self.set_fill_color(0.10, 0.14, 0.20)
                self.draw_text(parts[0] + ":", self.mx + 22, cur_y, font="F2", size=7.5)
                prefix_w = len(parts[0] + ":") * 7.5 * 0.49
                self.set_fill_color(0.20, 0.24, 0.30)
                self.draw_text(parts[1], self.mx + 22 + prefix_w + 3, cur_y, font="F1", size=7.5)
            else:
                self.set_fill_color(0.20, 0.24, 0.30)
                self.draw_text(bf, self.mx + 22, cur_y, font="F1", size=7.5)
            cur_y -= 13.0
            
        # Target Board Action
        self.set_stroke_color(0.85, 0.88, 0.92)
        self.draw_line(self.mx + 12, cur_y + 4, self.mx + box_w - 12, cur_y + 4, stroke_w=0.4)
        
        self.set_fill_color(0.08, 0.16, 0.28)
        self.draw_text("TARGET BOARD SANCTION:", self.mx + 14, cur_y - 5, font="F2", size=7.0)
        self.set_fill_color(0.15, 0.20, 0.28)
        self.draw_text(target_decision, self.mx + 130, cur_y - 5, font="F1", size=7.0)
        
        self.y = box_y - est_h - 14
        return self.y

    def draw_section_heading(self, code_num, title):
        """Draws an authoritative academic section heading with underline rule"""
        y = self.y
        self.set_fill_color(0.08, 0.16, 0.28)
        full_title = f"{code_num}  {title.upper()}"
        self.draw_text(full_title, self.mx, y, font="F2", size=10.0)
        
        # Clean 0.5pt Underline Rule
        self.set_stroke_color(0.08, 0.16, 0.28)
        self.draw_line(self.mx, y - 4, self.width - self.mx, y - 4, stroke_w=0.6)
        
        self.y = y - 16
        return self.y

    def draw_subsection_heading(self, num_str, title):
        """Draws a clean subsection heading"""
        y = self.y
        self.set_fill_color(0.12, 0.18, 0.28)
        self.draw_text(f"{num_str} {title}", self.mx, y, font="F2", size=8.8)
        self.y = y - 13
        return self.y

    def draw_academic_table(self, headers, rows, col_widths=None, table_title=None, source_note=None):
        """Draws a Lancet / American Economic Review style academic table (Low Ink, Thin Rules)"""
        y = self.y
        
        if table_title:
            self.set_fill_color(0.10, 0.14, 0.20)
            self.draw_text(table_title, self.mx, y, font="F2", size=8.0)
            y -= 10
            
        n_cols = len(headers)
        if not col_widths:
            col_widths = [self.cw / n_cols] * n_cols
            
        # 1. Top Rule (Solid 1.0pt Navy)
        self.set_stroke_color(0.08, 0.16, 0.28)
        self.draw_line(self.mx, y, self.width - self.mx, y, stroke_w=1.0)
        
        # 2. Header Row Background (Subtle 3% Grey Tint - Saves Toner)
        self.set_fill_color(0.955, 0.962, 0.975)
        self.draw_rect(self.mx, y - 16, self.cw, 16, fill=True, stroke=False)
        
        # 3. Header Texts
        self.set_fill_color(0.08, 0.14, 0.24)
        cur_x = self.mx + 4
        for h, w in zip(headers, col_widths):
            self.draw_text(h, cur_x, y - 11.5, font="F2", size=7.0)
            cur_x += w
            
        # 4. Header Bottom Rule (0.6pt)
        y -= 16
        self.set_stroke_color(0.08, 0.16, 0.28)
        self.draw_line(self.mx, y, self.width - self.mx, y, stroke_w=0.6)
        
        # 5. Data Rows
        row_h = 13.5
        for r_idx, row in enumerate(rows):
            # Alternating ultra-subtle tint on even rows
            if r_idx % 2 == 1:
                self.set_fill_color(0.982, 0.986, 0.992)
                self.draw_rect(self.mx, y - row_h, self.cw, row_h, fill=True, stroke=False)
                
            cur_x = self.mx + 4
            for c_idx, cell in enumerate(row):
                w = col_widths[c_idx]
                cell_str = str(cell)
                # Bold first column or summary rows
                is_bold = (c_idx == 0 and not cell_str.startswith(" ")) or "TOTAL" in str(row[0]).upper() or "EBITDA" in str(row[0]).upper()
                font = "F2" if is_bold else "F1"
                col = (0.08, 0.12, 0.18) if is_bold else (0.22, 0.26, 0.32)
                self.set_fill_color(*col)
                
                # Right align numbers / monetary
                align = "right" if any(char in cell_str for char in ['£', '%', 'k', 'M']) and c_idx > 0 else "left"
                self.draw_text(cell_str, cur_x, y - 9.5, font=font, size=7.0, align=align, max_w=w - 8)
                cur_x += w
                
            # Hairline divider between rows
            self.set_stroke_color(0.90, 0.92, 0.95)
            self.draw_line(self.mx, y - row_h, self.width - self.mx, y - row_h, stroke_w=0.3)
            y -= row_h
            
        # 6. Bottom Rule (Solid 1.0pt Navy)
        self.set_stroke_color(0.08, 0.16, 0.28)
        self.draw_line(self.mx, y, self.width - self.mx, y, stroke_w=1.0)
        
        # 7. Source / Methodology Note
        if source_note:
            y -= 9
            self.set_fill_color(0.45, 0.50, 0.58)
            self.draw_text(f"Note: {source_note}", self.mx, y, font="F3", size=6.5)
            
        self.y = y - 12
        return self.y

    def draw_metric_grid(self, metrics):
        """Draws clean, low-ink metric callout cards (3 or 4 per row)"""
        y = self.y
        n = len(metrics)
        card_w = (self.cw - (n - 1) * 8) / n
        card_h = 44
        
        for i, m in enumerate(metrics):
            cx = self.mx + i * (card_w + 8)
            # White background with 0.5pt subtle border
            self.set_fill_color(0.985, 0.990, 0.995)
            self.set_stroke_color(0.82, 0.86, 0.90)
            self.draw_rect(cx, y - card_h, card_w, card_h, fill=True, stroke=True, stroke_w=0.5)
            
            # Left accent pip
            self.set_fill_color(0.08, 0.16, 0.28)
            self.draw_rect(cx, y - card_h, 2.0, card_h, fill=True, stroke=False)
            
            # Label
            self.set_fill_color(0.40, 0.45, 0.52)
            self.draw_text(m[0].upper(), cx + 8, y - 11, font="F2", size=6.2)
            
            # Value (Bold & Large)
            self.set_fill_color(0.08, 0.12, 0.18)
            self.draw_text(m[1], cx + 8, y - 24, font="F2", size=10.5)
            
            # Sub-caption
            if len(m) > 2:
                self.set_fill_color(0.45, 0.50, 0.58)
                self.draw_text(m[2], cx + 8, y - 36, font="F1", size=6.0)
                
        self.y = y - card_h - 12
        return self.y

    def draw_vector_waterfall_chart(self, title, items, total_val=977600):
        """Draws an institutional publication-grade financial waterfall chart using pure vector lines"""
        y = self.y
        chart_h = 75
        chart_y = y - chart_h
        
        # Bounding box with hairline rule
        self.set_fill_color(0.99, 0.995, 1.0)
        self.set_stroke_color(0.85, 0.88, 0.92)
        self.draw_rect(self.mx, chart_y, self.cw, chart_h, fill=True, stroke=True, stroke_w=0.5)
        
        # Title
        self.set_fill_color(0.08, 0.16, 0.28)
        self.draw_text(f"FIGURE: {title.upper()}", self.mx + 8, y - 12, font="F2", size=7.2)
        
        # Draw columns
        n_items = len(items)
        col_w = (self.cw - 24) / n_items
        base_line = chart_y + 16
        
        for idx, (label, val, col_type) in enumerate(items):
            bx = self.mx + 12 + idx * col_w
            bw = col_w - 10
            
            # Height normalized to 40pt
            norm_h = min(40, max(8, (abs(val) / total_val) * 40))
            by = base_line
            
            if col_type == "revenue":
                # Deep Navy outline with light tint
                self.set_fill_color(0.92, 0.94, 0.98)
                self.set_stroke_color(0.08, 0.16, 0.28)
                self.draw_rect(bx, by, bw, norm_h, fill=True, stroke=True, stroke_w=0.6)
            elif col_type == "ebitda":
                # Forest green subtle tint with dark green outline
                self.set_fill_color(0.92, 0.97, 0.94)
                self.set_stroke_color(0.12, 0.45, 0.22)
                self.draw_rect(bx, by, bw, norm_h, fill=True, stroke=True, stroke_w=0.6)
            else: # deduction
                # Subtle slate tint
                self.set_fill_color(0.96, 0.96, 0.97)
                self.set_stroke_color(0.40, 0.45, 0.52)
                self.draw_rect(bx, by, bw, norm_h, fill=True, stroke=True, stroke_w=0.5)
                
            # Value label above
            val_str = f"£{abs(val)/1000:.1f}k" if abs(val) >= 1000 else f"£{abs(val):.0f}"
            if val < 0: val_str = f"-{val_str}"
            self.set_fill_color(0.08, 0.12, 0.18)
            self.draw_text(val_str, bx, by + norm_h + 3, font="F2", size=6.5, align="center", max_w=bw)
            
            # Bottom category label
            self.set_fill_color(0.35, 0.40, 0.48)
            self.draw_text(label, bx, base_line - 9, font="F1", size=5.8, align="center", max_w=bw)
            
        # Ground base rule
        self.set_stroke_color(0.75, 0.80, 0.85)
        self.draw_line(self.mx + 8, base_line, self.mx + self.cw - 8, base_line, stroke_w=0.5)
        
        self.y = chart_y - 12
        return self.y

    def render(self, page_num, total_pages):
        res = []
        if not self.is_cover:
            # 1. Academic Running Header
            res.append("0.78 0.82 0.88 RG 0.50 w")
            res.append(f"{self.mx:.2f} {self.height - 24:.2f} m {self.width - self.mx:.2f} {self.height - 24:.2f} l S")
            res.append(f"BT /F2 6.5 Tf 0.10 0.16 0.28 rg {self.mx:.2f} {self.height - 20:.2f} Td ({self.escape(self.journal_name.upper())}) Tj ET")
            
            sec_tag = f"{self.doc_ref}  |  {self.section_title.upper()}" if self.section_title else self.doc_ref
            res.append(f"BT /F1 6.2 Tf 0.45 0.50 0.58 rg {self.width - self.mx - 220:.2f} {self.height - 20:.2f} Td ({self.escape(sec_tag)}) Tj ET")
            
            # 2. Academic Running Footer
            res.append("0.78 0.82 0.88 RG 0.50 w")
            res.append(f"{self.mx:.2f} 28.00 m {self.width - self.mx:.2f} 28.00 l S")
            res.append(f"BT /F1 6.2 Tf 0.45 0.50 0.58 rg {self.mx:.2f} 18.00 Td (CONFIDENTIAL // PREPARED FOR THE BOARD OF DIRECTORS & REGISTERED MANAGER) Tj ET")
            page_str = f"Page {page_num} of {total_pages}"
            res.append(f"BT /F2 6.5 Tf 0.10 0.16 0.28 rg {self.width - self.mx - 52:.2f} 18.00 Td ({page_str}) Tj ET")
        else:
            # Cover page minimal footer
            res.append("0.78 0.82 0.88 RG 0.50 w")
            res.append(f"{self.mx:.2f} 28.00 m {self.width - self.mx:.2f} 28.00 l S")
            res.append(f"BT /F1 6.2 Tf 0.45 0.50 0.58 rg {self.mx:.2f} 18.00 Td (OFFICIAL BOARD OF DIRECTORS COMMISSIONING DOSSIER // A4 SPECIFICATION // LOW-INK PRINTER FRIENDLY) Tj ET")
            page_str = f"Page {page_num} of {total_pages}"
            res.append(f"BT /F2 6.5 Tf 0.10 0.16 0.28 rg {self.width - self.mx - 52:.2f} 18.00 Td ({page_str}) Tj ET")
            
        res.extend(self.ops)
        return "\n".join(res)

print("AcademicJournalPDF engine initialized.")
