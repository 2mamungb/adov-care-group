#!/usr/bin/env python3
"""
ADOV CARE GROUP — MASTER LANDSCAPE JOURNAL & BOARDROOM DOCUMENT ENGINE
Unified publication-ready PDF and matching Word (.docx) generation engine.

Specifications:
- ISO A4 Landscape: 841.89 pt x 595.28 pt (PDF) // 16838 dxa x 11906 dxa (Word)
- Low-Ink Plain White Ergonomics (100% white paper, hairlines, 2% grey tints)
- Exact Font Metrics & Mathematical Bounding-Box Layout (Zero text overlaps)
- Dynamic Cell-Wrapping in Tables (Headers and data cells wrap cleanly; dynamic row heights)
- Repeated Table Headers across page boundaries
- Strict Symbol Sanitization (Octal \\243 for £, octal \\225 for bullet, clean arrows and dashes)
- Proportional Leading & Column Spacing across Widescreen Boardroom Canvas
- Unified Data Architecture (PDF and Word document content are 100% synchronized)
- No Page Limit: Formatted for optimal readability, effortless printing, and boardroom presentation
"""

import os
import sys
import zlib
import zipfile

# ==============================================================================
# 1. TYPE 1 HELVETICA FONT METRICS (Standard Adobe Glyph Widths per 1000 units)
# ==============================================================================

HELVETICA_WIDTHS = {
    ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667, "'": 191,
    '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333, '.': 278, '/': 278,
    '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556, '7': 556,
    '8': 556, '9': 556, ':': 278, ';': 278, '<': 584, '=': 584, '>': 584, '?': 556,
    '@': 1015, 'A': 667, 'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778,
    'H': 722, 'I': 278, 'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722, 'O': 778,
    'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469, '_': 556,
    '`': 333, 'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556, 'f': 278, 'g': 556,
    'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222, 'm': 833, 'n': 556, 'o': 556,
    'p': 556, 'q': 556, 'r': 333, 's': 500, 't': 278, 'u': 556, 'v': 500, 'w': 722,
    'x': 500, 'y': 500, 'z': 500, '{': 334, '|': 260, '}': 334, '~': 584,
    '£': 556, '•': 350, '–': 556, '—': 1000
}

def get_text_width(text, font_size=8.5, is_bold=False):
    factor = 1.05 if is_bold else 1.0
    total = sum(HELVETICA_WIDTHS.get(ch, 550) for ch in str(text))
    return (total / 1000.0) * font_size * factor

def wrap_text_exact(text, max_w, font_size=8.5, is_bold=False):
    words = str(text).split()
    if not words:
        return []
    lines = []
    cur_line = []
    for w in words:
        test = " ".join(cur_line + [w]) if cur_line else w
        if get_text_width(test, font_size, is_bold) <= max_w:
            cur_line.append(w)
        else:
            if cur_line:
                lines.append(" ".join(cur_line))
                cur_line = []
            if get_text_width(w, font_size, is_bold) <= max_w:
                cur_line = [w]
            else:
                # Break long word character-by-character to strictly prevent column overflows
                sub_word = ""
                for ch in w:
                    if get_text_width(sub_word + ch, font_size, is_bold) <= max_w:
                        sub_word += ch
                    else:
                        if sub_word:
                            lines.append(sub_word)
                        sub_word = ch
                if sub_word:
                    cur_line = [sub_word]
    if cur_line:
        lines.append(" ".join(cur_line))
    return lines

def escape_pdf(text):
    out = []
    for ch in str(text):
        code = ord(ch)
        if ch == '\\':
            out.append('\\\\')
        elif ch == '(':
            out.append('\\(')
        elif ch == ')':
            out.append('\\)')
        elif ch == '£':
            out.append('\\243')
        elif ch == '•':
            out.append('\\225')
        elif ch == '–':
            out.append('\\226')
        elif ch == '—':
            out.append('\\227')
        elif ch in ("'", "’", "‘"):
            out.append("'")
        elif ch in ('"', '“', '”'):
            out.append('"')
        elif ch == '✓':
            out.append('[PASS]')
        elif ch == '✗':
            out.append('[FAIL]')
        elif ch == '→':
            out.append('->')
        elif 32 <= code <= 126:
            out.append(ch)
        elif code <= 255:
            out.append(f'\\{code:03o}')
        else:
            out.append(' ')
    return ''.join(out)

def xml_escape(text):
    return (str(text).replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;')
                     .replace('"', '&quot;')
                     .replace("'", '&apos;'))

# ==============================================================================
# 2. LANDSCAPE DOCUMENT MODEL
# ==============================================================================

class LandscapeDocument:
    def __init__(self, title, doc_ref, category="BOARDROOM MONOGRAPH", subtitle=""):
        self.title = title
        self.doc_ref = doc_ref
        self.category = category
        self.subtitle = subtitle
        self.meta_items = []
        self.kpis = []
        self.elements = []

    def set_meta(self, items):
        self.meta_items = items

    def set_kpis(self, kpi_list):
        self.kpis = kpi_list

    def add_heading_1(self, text):
        self.elements.append({"type": "h1", "text": text})

    def add_heading_2(self, text):
        self.elements.append({"type": "h2", "text": text})

    def add_heading_3(self, text):
        self.elements.append({"type": "h3", "text": text})

    def add_paragraph(self, text):
        self.elements.append({"type": "p", "text": text})

    def add_page_break(self):
        self.elements.append({"type": "page_break"})

    def add_bullet_list(self, items):
        self.elements.append({"type": "bullets", "items": items})

    def add_callout(self, title, text):
        self.elements.append({"type": "callout", "title": title, "text": text})

    def add_table(self, title, headers, rows, col_pcts=None):
        self.elements.append({
            "type": "table",
            "title": title,
            "headers": headers,
            "rows": rows,
            "col_pcts": col_pcts
        })

    def add_key_value_grid(self, title, items, num_cols=2):
        self.elements.append({
            "type": "grid",
            "title": title,
            "items": items,
            "cols": num_cols
        })

    def add_flow_stages(self, title, stages):
        self.elements.append({
            "type": "flow",
            "title": title,
            "stages": stages
        })

    # ==========================================================================
    # 3. COMPILATION ENGINES
    # ==========================================================================
    def build_pdf(self, filename):
        builder = LandscapePDFBuilder(self, filename)
        return builder.render()

    def build_docx(self, filename):
        builder = LandscapeDocxBuilder(self, filename)
        return builder.render()


# ==============================================================================
# 4. LANDSCAPE PDF BUILDER ENGINE
# ==============================================================================

class LandscapePDFPage:
    def __init__(self, width, height, mx, mt, mb, is_cover, doc_title, doc_ref, category):
        self.width = width
        self.height = height
        self.mx = mx
        self.mt = mt
        self.mb = mb
        self.cw = width - 2 * mx
        self.is_cover = is_cover
        self.doc_title = doc_title
        self.doc_ref = doc_ref
        self.category = category
        self.ops = []

    def set_fill(self, r, g, b):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")

    def set_stroke(self, r, g, b, stroke_w=0.75):
        self.ops.append(f"{r:.3f} {g:.3f} {b:.3f} RG {stroke_w:.2f} w")

    def draw_rect(self, x, y, w, h, fill=True, stroke=False, stroke_w=0.5):
        if stroke:
            self.ops.append(f"{stroke_w:.2f} w")
        op = "B" if (fill and stroke) else ("f" if fill else "S")
        self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}")

    def draw_line(self, x1, y1, x2, y2, stroke_w=0.75):
        self.ops.append(f"{stroke_w:.2f} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")

    def draw_text(self, text, x, y, font="F1", size=8.5):
        safe = escape_pdf(text)
        self.ops.append(f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({safe}) Tj ET")

    def render(self, page_num, total_pages):
        header_footer = []
        if not self.is_cover:
            # Running Header
            header_footer.append("0.780 0.820 0.880 RG 0.50 w")
            header_footer.append(f"{self.mx:.2f} {self.height - 24:.2f} m {self.width - self.mx:.2f} {self.height - 24:.2f} l S")
            header_footer.append(f"BT /F2 7.0 Tf 0.080 0.160 0.280 rg {self.mx:.2f} {self.height - 18:.2f} Td ({escape_pdf(self.doc_title[:70])}) Tj ET")
            header_footer.append(f"BT /F1 6.5 Tf 0.400 0.450 0.520 rg {self.width - self.mx - 240:.2f} {self.height - 18:.2f} Td (ADOV CARE GROUP // LUTON CAMPUS // {escape_pdf(self.doc_ref)}) Tj ET")

            # Running Footer
            header_footer.append("0.780 0.820 0.880 RG 0.50 w")
            header_footer.append(f"{self.mx:.2f} 24.00 m {self.width - self.mx:.2f} 24.00 l S")
            header_footer.append(f"BT /F1 6.5 Tf 0.400 0.450 0.520 rg {self.mx:.2f} 15.00 Td (CONFIDENTIAL // PREPARED FOR THE BOARD OF DIRECTORS, REGISTERED MANAGER & CQC COMMISSIONING) Tj ET")
            page_str = f"Page {page_num} of {total_pages}"
            header_footer.append(f"BT /F2 7.0 Tf 0.080 0.160 0.280 rg {self.width - self.mx - 65:.2f} 15.00 Td ({page_str}) Tj ET")
        else:
            # Minimal Cover Footer
            header_footer.append("0.780 0.820 0.880 RG 0.50 w")
            header_footer.append(f"{self.mx:.2f} 24.00 m {self.width - self.mx:.2f} 24.00 l S")
            header_footer.append(f"BT /F1 6.5 Tf 0.400 0.450 0.520 rg {self.mx:.2f} 15.00 Td (OFFICIAL BOARDROOM EDITION // ISO A4 LANDSCAPE // LOW-INK ACADEMIC MONOGRAPH) Tj ET")
            page_str = f"Page {page_num} of {total_pages}"
            header_footer.append(f"BT /F2 7.0 Tf 0.080 0.160 0.280 rg {self.width - self.mx - 65:.2f} 15.00 Td ({page_str}) Tj ET")

        return "\n".join(header_footer + self.ops)


class LandscapePDFBuilder:
    def __init__(self, doc_model, filename):
        self.doc = doc_model
        self.filename = filename
        self.width = 841.89  # ISO A4 Landscape
        self.height = 595.28
        self.mx = 42.0
        self.mt = 38.0
        self.mb = 36.0
        self.cw = self.width - 2 * self.mx
        self.pages = []
        self.cur_page = None
        self.cur_y = 0.0

    def new_page(self, is_cover=False):
        page = LandscapePDFPage(
            self.width, self.height, self.mx, self.mt, self.mb,
            is_cover, self.doc.title, self.doc.doc_ref, self.doc.category
        )
        self.pages.append(page)
        self.cur_page = page
        self.cur_y = self.height - self.mt - (0 if is_cover else 18)
        return page

    def ensure_space(self, needed_h):
        if self.cur_page is None or (self.cur_y - needed_h < self.mb):
            self.new_page(is_cover=False)

    def render(self):
        # 1. PAGE 1: COVER & MASTHEAD
        p1 = self.new_page(is_cover=True)
        self.draw_masthead(p1)

        # 2. RENDER ELEMENTS WITH STRICT FLOW CONTROL & NO PAGE LIMIT
        for el in self.doc.elements:
            el_type = el["type"]
            if el_type == "h1":
                self.render_heading_1(el["text"])
            elif el_type == "h2":
                self.render_heading_2(el["text"])
            elif el_type == "h3":
                self.render_heading_3(el["text"])
            elif el_type == "p":
                self.render_paragraph(el["text"])
            elif el_type == "bullets":
                self.render_bullets(el["items"])
            elif el_type == "callout":
                self.render_callout(el["title"], el["text"])
            elif el_type == "table":
                self.render_table(el["title"], el["headers"], el["rows"], el.get("col_pcts"))
            elif el_type == "grid":
                self.render_grid(el["title"], el["items"], el.get("cols", 2))
            elif el_type == "flow":
                self.render_flow(el["title"], el["stages"])
            elif el_type == "page_break":
                self.new_page(is_cover=False)

        # 3. COMPILE PDF OBJECTS & XREF
        return self.save_pdf()

    def draw_masthead(self, page):
        y = self.height - 30
        # Working paper series banner
        page.set_fill(0.400, 0.450, 0.550)
        page.draw_text("WORKING PAPER SERIES IN HEALTHCARE GOVERNANCE & SOCIAL CARE INFRASTRUCTURE", self.mx, y, font="F2", size=7.0)
        page.draw_text(f"MONOGRAPH REF: {self.doc.doc_ref} // {self.doc.category}", self.width - self.mx - 260, y, font="F2", size=7.0)

        # Oxford Double Rule
        y -= 6
        page.set_stroke(0.080, 0.160, 0.280, stroke_w=1.2)
        page.draw_line(self.mx, y, self.width - self.mx, y, stroke_w=1.2)
        page.set_stroke(0.780, 0.820, 0.880, stroke_w=0.5)
        page.draw_line(self.mx, y - 2.5, self.width - self.mx, y - 2.5, stroke_w=0.5)

        # Main Title & Subtitle
        y -= 22
        page.set_fill(0.060, 0.120, 0.220)
        page.draw_text(self.doc.title, self.mx, y, font="F2", size=15.5)

        if self.doc.subtitle:
            y -= 13
            page.set_fill(0.350, 0.400, 0.500)
            page.draw_text(self.doc.subtitle, self.mx, y, font="F3", size=8.8)

        # Metadata Card (2-column key metrics across landscape width)
        if self.doc.meta_items:
            y -= 10
            meta_h = (len(self.doc.meta_items) + 1) // 2 * 12.0 + 8.0
            page.set_fill(0.975, 0.982, 0.992)
            page.set_stroke(0.820, 0.850, 0.900, stroke_w=0.5)
            page.draw_rect(self.mx, y - meta_h, self.cw, meta_h, fill=True, stroke=True, stroke_w=0.5)

            # Left accent bar
            page.set_fill(0.080, 0.160, 0.280)
            page.draw_rect(self.mx, y - meta_h, 3.0, meta_h, fill=True)

            mid_idx = (len(self.doc.meta_items) + 1) // 2
            left_col = self.doc.meta_items[:mid_idx]
            right_col = self.doc.meta_items[mid_idx:]

            cur_my = y - 10.0
            for lbl, val in left_col:
                page.set_fill(0.080, 0.160, 0.280)
                page.draw_text(lbl, self.mx + 8, cur_my, font="F2", size=7.2)
                page.set_fill(0.200, 0.250, 0.320)
                page.draw_text(val, self.mx + 130, cur_my, font="F1", size=7.2)
                cur_my -= 12.0

            cur_my = y - 10.0
            col2_x = self.mx + self.cw / 2.0 + 10
            for lbl, val in right_col:
                page.set_fill(0.080, 0.160, 0.280)
                page.draw_text(lbl, col2_x, cur_my, font="F2", size=7.2)
                page.set_fill(0.200, 0.250, 0.320)
                page.draw_text(val, col2_x + 130, cur_my, font="F1", size=7.2)
                cur_my -= 12.0

            y -= (meta_h + 10.0)

        # KPI Ribbon Cards (5 cards across landscape width)
        if self.doc.kpis:
            n_kpis = len(self.doc.kpis)
            gap = 8.0
            card_w = (self.cw - (n_kpis - 1) * gap) / n_kpis
            card_h = 36.0

            for i, (fig, lbl, sub) in enumerate(self.doc.kpis):
                cx = self.mx + i * (card_w + gap)
                cy = y - card_h

                page.set_fill(0.965, 0.972, 0.985)
                page.set_stroke(0.820, 0.850, 0.900, stroke_w=0.5)
                page.draw_rect(cx, cy, card_w, card_h, fill=True, stroke=True, stroke_w=0.5)

                page.set_fill(0.080, 0.160, 0.280)
                page.draw_rect(cx, cy + card_h - 2.5, card_w, 2.5, fill=True)

                page.set_fill(0.060, 0.120, 0.220)
                page.draw_text(fig, cx + 6, cy + 22, font="F2", size=11.0)

                page.set_fill(0.300, 0.350, 0.420)
                page.draw_text(lbl, cx + 6, cy + 11.5, font="F2", size=6.5)

                page.set_fill(0.450, 0.500, 0.580)
                page.draw_text(sub, cx + 6, cy + 3.5, font="F1", size=5.8)

            y -= (card_h + 14.0)

        self.cur_y = y

    def render_heading_1(self, text):
        self.ensure_space(38.0)
        self.cur_y -= 10.0
        p = self.cur_page

        # Subtle background pill
        p.set_fill(0.960, 0.968, 0.980)
        p.set_stroke(0.820, 0.850, 0.900, stroke_w=0.5)
        p.draw_rect(self.mx, self.cur_y - 16.0, self.cw, 18.0, fill=True, stroke=True, stroke_w=0.5)

        # Left accent pill
        p.set_fill(0.080, 0.160, 0.280)
        p.draw_rect(self.mx, self.cur_y - 16.0, 3.5, 18.0, fill=True)

        p.set_fill(0.080, 0.160, 0.280)
        p.draw_text(text.upper(), self.mx + 8, self.cur_y - 11.5, font="F2", size=9.5)
        self.cur_y -= 24.0

    def render_heading_2(self, text):
        self.ensure_space(28.0)
        self.cur_y -= 8.0
        p = self.cur_page
        p.set_fill(0.080, 0.160, 0.280)
        p.draw_text(text, self.mx, self.cur_y, font="F2", size=8.8)
        p.set_stroke(0.780, 0.820, 0.880, stroke_w=0.5)
        p.draw_line(self.mx, self.cur_y - 3.0, self.mx + 220, self.cur_y - 3.0, stroke_w=0.5)
        self.cur_y -= 12.0

    def render_heading_3(self, text):
        self.ensure_space(22.0)
        self.cur_y -= 6.0
        p = self.cur_page
        p.set_fill(0.100, 0.180, 0.300)
        p.draw_text(text, self.mx, self.cur_y, font="F2", size=8.0)
        self.cur_y -= 10.0

    def render_paragraph(self, text):
        font_size = 8.5
        leading = 12.5
        lines = wrap_text_exact(text, self.cw, font_size=font_size, is_bold=False)
        for line in lines:
            self.ensure_space(leading)
            self.cur_page.set_fill(0.120, 0.160, 0.220)
            self.cur_page.draw_text(line, self.mx, self.cur_y, font="F1", size=font_size)
            self.cur_y -= leading
        self.cur_y -= 6.0

    def render_bullets(self, items):
        font_size = 8.2
        leading = 12.0
        for item in items:
            lines = wrap_text_exact(item, self.cw - 18.0, font_size=font_size, is_bold=False)
            self.ensure_space(len(lines) * leading + 4.0)
            p = self.cur_page

            # Bullet dot
            p.set_fill(0.080, 0.160, 0.280)
            p.draw_text("\\225", self.mx + 4, self.cur_y, font="F2", size=font_size)

            for i, line in enumerate(lines):
                p.set_fill(0.120, 0.160, 0.220)
                p.draw_text(line, self.mx + 16, self.cur_y, font="F1", size=font_size)
                self.cur_y -= leading
            self.cur_y -= 3.0

    def render_callout(self, title, text):
        font_size = 8.0
        leading = 11.5
        lines = wrap_text_exact(text, self.cw - 24.0, font_size=font_size, is_bold=False)
        box_h = 18.0 + len(lines) * leading + 8.0
        self.ensure_space(box_h + 8.0)

        p = self.cur_page
        cy = self.cur_y - box_h

        # Tinted Box
        p.set_fill(0.970, 0.978, 0.988)
        p.set_stroke(0.820, 0.850, 0.900, stroke_w=0.5)
        p.draw_rect(self.mx, cy, self.cw, box_h, fill=True, stroke=True, stroke_w=0.5)

        # 3.5pt Oxford Navy left accent
        p.set_fill(0.080, 0.160, 0.280)
        p.draw_rect(self.mx, cy, 3.5, box_h, fill=True)

        # Title
        p.set_fill(0.080, 0.160, 0.280)
        p.draw_text(title.upper(), self.mx + 10, self.cur_y - 12.0, font="F2", size=8.5)

        # Body text
        cur_ty = self.cur_y - 23.0
        p.set_fill(0.150, 0.200, 0.280)
        for line in lines:
            p.draw_text(line, self.mx + 10, cur_ty, font="F1", size=font_size)
            cur_ty -= leading

        self.cur_y = cy - 10.0

    def render_table(self, title, headers, rows, col_pcts=None):
        n_cols = len(headers)
        if col_pcts and len(col_pcts) == n_cols:
            col_widths = [self.cw * (p / 100.0) for p in col_pcts]
        else:
            col_widths = [self.cw / n_cols] * n_cols

        cell_font_size = 7.5
        cell_leading = 10.5
        cell_pad_x = 5.0
        cell_pad_y = 5.0

        header_font_size = 7.5
        header_leading = 10.5
        header_pad_x = 5.0
        header_pad_y = 5.0

        # Pre-wrap headers to eliminate horizontal collision
        h_lines_per_col = []
        for i, h_txt in enumerate(headers):
            avail_w = col_widths[i] - 2 * header_pad_x
            lines = wrap_text_exact(str(h_txt), avail_w, font_size=header_font_size, is_bold=True)
            if not lines:
                lines = [str(h_txt)]
            h_lines_per_col.append(lines)
        max_h_lines = max(len(l) for l in h_lines_per_col)
        header_h = max_h_lines * header_leading + 2 * header_pad_y

        if title:
            self.ensure_space(32.0 + header_h)
            p = self.cur_page
            p.set_fill(0.080, 0.160, 0.280)
            p.draw_text(title, self.mx, self.cur_y, font="F2", size=8.5)
            self.cur_y -= 12.0

        def draw_tbl_header():
            p = self.cur_page
            # Top rule
            p.set_stroke(0.080, 0.160, 0.280, stroke_w=1.2)
            p.draw_line(self.mx, self.cur_y, self.width - self.mx, self.cur_y, stroke_w=1.2)
            
            # Header background fill
            p.set_fill(0.950, 0.958, 0.970)
            p.draw_rect(self.mx, self.cur_y - header_h, self.cw, header_h, fill=True)

            # Draw header text lines
            col_x = self.mx
            for i, lines in enumerate(h_lines_per_col):
                cur_x = col_x + header_pad_x
                p.set_fill(0.080, 0.160, 0.280)
                for l_idx, line in enumerate(lines):
                    line_y = self.cur_y - header_pad_y - 0.75 * header_font_size - l_idx * header_leading
                    p.draw_text(line, cur_x, line_y, font="F2", size=header_font_size)
                col_x += col_widths[i]

            # Bottom rule of header
            p.set_stroke(0.080, 0.160, 0.280, stroke_w=0.8)
            p.draw_line(self.mx, self.cur_y - header_h, self.width - self.mx, self.cur_y - header_h, stroke_w=0.8)
            self.cur_y -= header_h

        self.ensure_space(header_h + 30.0)
        draw_tbl_header()

        for r_idx, row in enumerate(rows):
            # Pre-wrap each cell in this row to strictly prevent text overlap
            row_lines_per_col = []
            for c_idx, val in enumerate(row):
                avail_w = col_widths[c_idx] - 2 * cell_pad_x
                is_bold = (c_idx == 0 or ("£" in str(val) and c_idx >= len(row) - 2))
                lines = wrap_text_exact(str(val), avail_w, font_size=cell_font_size, is_bold=is_bold)
                if not lines:
                    lines = [str(val)]
                row_lines_per_col.append(lines)

            max_lines = max(len(l) for l in row_lines_per_col)
            row_h = max_lines * cell_leading + 2 * cell_pad_y

            # Check if this row fits on current page; if not, wrap cleanly to next page
            if self.cur_y - row_h < self.mb + 10.0:
                p = self.cur_page
                p.set_stroke(0.080, 0.160, 0.280, stroke_w=0.8)
                p.draw_line(self.mx, self.cur_y, self.width - self.mx, self.cur_y, stroke_w=0.8)

                self.new_page(is_cover=False)
                if title:
                    p = self.cur_page
                    p.set_fill(0.080, 0.160, 0.280)
                    p.draw_text(f"{title} (Continued)", self.mx, self.cur_y, font="F2", size=8.0)
                    self.cur_y -= 12.0
                draw_tbl_header()

            p = self.cur_page
            y_top = self.cur_y

            # Alternating row background
            bg = (0.975, 0.982, 0.992) if (r_idx % 2 == 1) else (1.0, 1.0, 1.0)
            p.set_fill(*bg)
            p.draw_rect(self.mx, y_top - row_h, self.cw, row_h, fill=True)

            # Draw cell text lines
            col_x = self.mx
            for c_idx, lines in enumerate(row_lines_per_col):
                val = row[c_idx]
                is_bold = (c_idx == 0 or ("£" in str(val) and c_idx >= len(row) - 2))
                f_use = "F2" if is_bold else "F1"
                c_use = (0.080, 0.160, 0.280) if is_bold else (0.150, 0.200, 0.280)
                p.set_fill(*c_use)
                cur_x = col_x + cell_pad_x
                for l_idx, line in enumerate(lines):
                    line_y = y_top - cell_pad_y - 0.75 * cell_font_size - l_idx * cell_leading
                    p.draw_text(line, cur_x, line_y, font=f_use, size=cell_font_size)
                col_x += col_widths[c_idx]

            # Row bottom separator rule
            p.set_stroke(0.880, 0.900, 0.930, stroke_w=0.4)
            p.draw_line(self.mx, y_top - row_h, self.width - self.mx, y_top - row_h, stroke_w=0.4)

            self.cur_y = y_top - row_h

        # Final table bottom rule
        p = self.cur_page
        p.set_stroke(0.080, 0.160, 0.280, stroke_w=1.2)
        p.draw_line(self.mx, self.cur_y, self.width - self.mx, self.cur_y, stroke_w=1.2)
        self.cur_y -= 14.0

    def render_grid(self, title, items, num_cols=2):
        col_w = (self.cw - (num_cols - 1) * 12.0) / num_cols
        n_rows = (len(items) + num_cols - 1) // num_cols

        if title:
            self.ensure_space(34.0)
            p = self.cur_page
            p.set_fill(0.080, 0.160, 0.280)
            p.draw_text(title, self.mx, self.cur_y, font="F2", size=8.5)
            self.cur_y -= 10.0

        for r in range(n_rows):
            row_items = items[r * num_cols : (r + 1) * num_cols]
            # Pre-wrap both key and value
            wrapped_items = []
            for k, v in row_items:
                k_lines = wrap_text_exact(k.upper(), col_w - 16.0, font_size=7.5, is_bold=True)
                v_lines = wrap_text_exact(v, col_w - 16.0, font_size=7.2, is_bold=False)
                wrapped_items.append((k_lines, v_lines))

            max_box_h = max(len(kl) * 11.0 + len(vl) * 10.2 + 16.0 for kl, vl in wrapped_items)
            self.ensure_space(max_box_h + 10.0)

            p = self.cur_page
            cy = self.cur_y - max_box_h

            for c, (k_lines, v_lines) in enumerate(wrapped_items):
                cx = self.mx + c * (col_w + 12.0)

                p.set_fill(0.975, 0.982, 0.992)
                p.set_stroke(0.820, 0.850, 0.900, stroke_w=0.5)
                p.draw_rect(cx, cy, col_w, max_box_h, fill=True, stroke=True, stroke_w=0.5)

                p.set_fill(0.080, 0.160, 0.280)
                p.draw_rect(cx, cy, 3.0, max_box_h, fill=True)

                # Key lines
                cur_ty = self.cur_y - 12.0
                p.set_fill(0.080, 0.160, 0.280)
                for kl in k_lines:
                    p.draw_text(kl, cx + 8, cur_ty, font="F2", size=7.5)
                    cur_ty -= 11.0

                # Value lines
                p.set_fill(0.200, 0.250, 0.320)
                cur_ty -= 2.0
                for vl in v_lines:
                    p.draw_text(vl, cx + 8, cur_ty, font="F1", size=7.2)
                    cur_ty -= 10.2

            self.cur_y = cy - 10.0
        self.cur_y -= 6.0

    def render_flow(self, title, stages):
        n = len(stages)
        box_w = (self.cw - (n - 1) * 8.0) / n

        # Pre-wrap all stages
        wrapped_stages = []
        for stage_num, stage_title, stage_desc in stages:
            t_lines = wrap_text_exact(f"STAGE {stage_num}: {stage_title}".upper(), box_w - 12.0, font_size=6.8, is_bold=True)
            d_lines = wrap_text_exact(stage_desc, box_w - 12.0, font_size=6.2, is_bold=False)
            wrapped_stages.append((t_lines, d_lines))

        max_box_h = max(len(tl) * 10.0 + len(dl) * 8.8 + 18.0 for tl, dl in wrapped_stages)
        max_box_h = max(max_box_h, 55.0)

        self.ensure_space(max_box_h + 24.0)
        p = self.cur_page

        if title:
            p.set_fill(0.080, 0.160, 0.280)
            p.draw_text(title, self.mx, self.cur_y, font="F2", size=8.5)
            self.cur_y -= 10.0

        by = self.cur_y - max_box_h

        for i, (t_lines, d_lines) in enumerate(wrapped_stages):
            bx = self.mx + i * (box_w + 8.0)

            p.set_fill(0.975, 0.982, 0.992)
            p.set_stroke(0.820, 0.850, 0.900, stroke_w=0.5)
            p.draw_rect(bx, by, box_w, max_box_h, fill=True, stroke=True, stroke_w=0.5)

            p.set_fill(0.080, 0.160, 0.280)
            p.draw_rect(bx, by + max_box_h - 2.5, box_w, 2.5, fill=True)

            cur_ty = by + max_box_h - 12.0
            p.set_fill(0.080, 0.160, 0.280)
            for tl in t_lines:
                p.draw_text(tl, bx + 6, cur_ty, font="F2", size=6.8)
                cur_ty -= 10.0

            cur_ty -= 2.0
            p.set_fill(0.200, 0.250, 0.320)
            for dl in d_lines:
                p.draw_text(dl, bx + 6, cur_ty, font="F1", size=6.2)
                cur_ty -= 8.8

        self.cur_y = by - 12.0

    def save_pdf(self):
        objects = []
        objects.append("<< /Type /Catalog /Pages 2 0 R >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>")

        current_obj_id = 6
        page_obj_ids = []
        content_obj_ids = []

        total_pages = len(self.pages)
        for i, page in enumerate(self.pages):
            page_obj_id = current_obj_id
            content_obj_id = current_obj_id + 1
            current_obj_id += 2
            page_obj_ids.append(page_obj_id)
            content_obj_ids.append(content_obj_id)

            stream_data = page.render(page_num=i+1, total_pages=total_pages)
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
        print(f"✓ Generated Landscape A4 PDF: '{self.filename}' ({len(out):,} bytes, {total_pages} pages).")
        return len(out)


# ==============================================================================
# 5. MATCHING WORD (.DOCX) BUILDER ENGINE (ISO A4 LANDSCAPE)
# ==============================================================================

class LandscapeDocxBuilder:
    def __init__(self, doc_model, filename):
        self.doc = doc_model
        self.filename = filename

    def render(self):
        # OpenXML document structure: ISO A4 Landscape
        body_xml = []

        # 1. Header Masthead
        body_xml.append(f'''
        <w:p>
            <w:pPr>
                <w:pBdr><w:bottom w:val="single" w:sz="18" w:space="4" w:color="0F2440"/></w:pBdr>
                <w:spacing w:before="0" w:after="120"/>
            </w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica"/><w:b/><w:sz w:val="16"/><w:color w:val="667085"/></w:rPr>
            <w:t>WORKING PAPER SERIES IN HEALTHCARE GOVERNANCE // {xml_escape(self.doc.category)}</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:before="80" w:after="60"/></w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica"/><w:b/><w:sz w:val="36"/><w:color w:val="0F2440"/></w:rPr>
            <w:t>{xml_escape(self.doc.title)}</w:t></w:r>
        </w:p>
        ''')

        if self.doc.subtitle:
            body_xml.append(f'''
            <w:p>
                <w:pPr><w:spacing w:before="0" w:after="180"/></w:pPr>
                <w:r><w:rPr><w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica"/><w:i/><w:sz w:val="21"/><w:color w:val="475467"/></w:rPr>
                <w:t>{xml_escape(self.doc.subtitle)}</w:t></w:r>
            </w:p>
            ''')

        # 2. Metadata Table
        if self.doc.meta_items:
            mid = (len(self.doc.meta_items) + 1) // 2
            left_col = self.doc.meta_items[:mid]
            right_col = self.doc.meta_items[mid:]

            rows_xml = []
            for i in range(max(len(left_col), len(right_col))):
                l_item = left_col[i] if i < len(left_col) else ("", "")
                r_item = right_col[i] if i < len(right_col) else ("", "")
                rows_xml.append(f'''
                <w:tr>
                    <w:trPr><w:cantSplit/></w:trPr>
                    <w:tc><w:tcPr><w:tcW w:w="2600" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/></w:tcPr>
                        <w:p><w:pPr><w:spacing w:after="40"/></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="17"/><w:color w:val="0F2440"/></w:rPr><w:t>{xml_escape(l_item[0])}</w:t></w:r></w:p>
                    </w:tc>
                    <w:tc><w:tcPr><w:tcW w:w="4685" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/></w:tcPr>
                        <w:p><w:pPr><w:spacing w:after="40"/></w:pPr><w:r><w:rPr><w:sz w:val="17"/><w:color w:val="344054"/></w:rPr><w:t>{xml_escape(l_item[1])}</w:t></w:r></w:p>
                    </w:tc>
                    <w:tc><w:tcPr><w:tcW w:w="2600" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/></w:tcPr>
                        <w:p><w:pPr><w:spacing w:after="40"/></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="17"/><w:color w:val="0F2440"/></w:rPr><w:t>{xml_escape(r_item[0])}</w:t></w:r></w:p>
                    </w:tc>
                    <w:tc><w:tcPr><w:tcW w:w="4685" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/></w:tcPr>
                        <w:p><w:pPr><w:spacing w:after="40"/></w:pPr><w:r><w:rPr><w:sz w:val="17"/><w:color w:val="344054"/></w:rPr><w:t>{xml_escape(r_item[1])}</w:t></w:r></w:p>
                    </w:tc>
                </w:tr>
                ''')

            body_xml.append(f'''
            <w:tbl>
                <w:tblPr>
                    <w:tblW w:w="14570" w:type="dxa"/>
                    <w:tblBorders>
                        <w:top w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                        <w:left w:val="single" w:sz="18" w:space="0" w:color="0F2440"/>
                        <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                        <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                        <w:insideH w:val="single" w:sz="2" w:space="0" w:color="EAECF0"/>
                        <w:insideV w:val="none"/>
                    </w:tblBorders>
                    <w:tblCellMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tblCellMar>
                </w:tblPr>
                {"".join(rows_xml)}
            </w:tbl>
            <w:p><w:pPr><w:spacing w:before="80" w:after="120"/></w:pPr></w:p>
            ''')

        # 3. KPI Ribbon Table
        if self.doc.kpis:
            kpi_cols = []
            col_w = 14570 // len(self.doc.kpis)
            for fig, lbl, sub in self.doc.kpis:
                kpi_cols.append(f'''
                <w:tc>
                    <w:tcPr>
                        <w:tcW w:w="{col_w}" w:type="dxa"/>
                        <w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/>
                    </w:tcPr>
                    <w:p>
                        <w:pPr><w:spacing w:before="60" w:after="20"/></w:pPr>
                        <w:r><w:rPr><w:b/><w:sz w:val="26"/><w:color w:val="0F2440"/></w:rPr><w:t>{xml_escape(fig)}</w:t></w:r>
                    </w:p>
                    <w:p>
                        <w:pPr><w:spacing w:before="0" w:after="20"/></w:pPr>
                        <w:r><w:rPr><w:b/><w:sz w:val="16"/><w:color w:val="475467"/></w:rPr><w:t>{xml_escape(lbl)}</w:t></w:r>
                    </w:p>
                    <w:p>
                        <w:pPr><w:spacing w:before="0" w:after="60"/></w:pPr>
                        <w:r><w:rPr><w:sz w:val="14"/><w:color w:val="667085"/></w:rPr><w:t>{xml_escape(sub)}</w:t></w:r>
                    </w:p>
                </w:tc>
                ''')

            body_xml.append(f'''
            <w:tbl>
                <w:tblPr>
                    <w:tblW w:w="14570" w:type="dxa"/>
                    <w:tblBorders>
                        <w:top w:val="single" w:sz="18" w:space="0" w:color="0F2440"/>
                        <w:left w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                        <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                        <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                        <w:insideH w:val="none"/>
                        <w:insideV w:val="single" w:sz="4" w:space="0" w:color="EAECF0"/>
                    </w:tblBorders>
                    <w:tblCellMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tblCellMar>
                </w:tblPr>
                <w:tr><w:trPr><w:cantSplit/></w:trPr>{"".join(kpi_cols)}</w:tr>
            </w:tbl>
            <w:p><w:pPr><w:spacing w:before="80" w:after="160"/></w:pPr></w:p>
            ''')

        # 4. Elements
        for el in self.doc.elements:
            el_type = el["type"]
            if el_type == "h1":
                body_xml.append(f'''
                <w:p>
                    <w:pPr>
                        <w:pBdr><w:left w:val="single" w:sz="24" w:space="10" w:color="0F2440"/></w:pBdr>
                        <w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/>
                        <w:spacing w:before="260" w:after="120"/>
                    </w:pPr>
                    <w:r><w:rPr><w:b/><w:sz w:val="24"/><w:color w:val="0F2440"/></w:rPr>
                    <w:t>{xml_escape(el["text"].upper())}</w:t></w:r>
                </w:p>
                ''')
            elif el_type == "h2":
                body_xml.append(f'''
                <w:p>
                    <w:pPr><w:spacing w:before="180" w:after="80"/></w:pPr>
                    <w:r><w:rPr><w:b/><w:sz w:val="21"/><w:color w:val="0F2440"/></w:rPr>
                    <w:t>{xml_escape(el["text"])}</w:t></w:r>
                </w:p>
                ''')
            elif el_type == "h3":
                body_xml.append(f'''
                <w:p>
                    <w:pPr><w:spacing w:before="140" w:after="60"/></w:pPr>
                    <w:r><w:rPr><w:b/><w:sz w:val="18"/><w:color w:val="1E3A8A"/></w:rPr>
                    <w:t>{xml_escape(el["text"])}</w:t></w:r>
                </w:p>
                ''')
            elif el_type == "page_break":
                body_xml.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
            elif el_type == "p":
                body_xml.append(f'''
                <w:p>
                    <w:pPr><w:spacing w:before="0" w:after="120" w:line="276" w:lineRule="auto"/></w:pPr>
                    <w:r><w:rPr><w:sz w:val="20"/><w:color w:val="1D2939"/></w:rPr>
                    <w:t>{xml_escape(el["text"])}</w:t></w:r>
                </w:p>
                ''')
            elif el_type == "bullets":
                for it in el["items"]:
                    body_xml.append(f'''
                    <w:p>
                        <w:pPr>
                            <w:ind w:left="420" w:hanging="260"/>
                            <w:spacing w:before="0" w:after="80"/>
                        </w:pPr>
                        <w:r><w:rPr><w:b/><w:sz w:val="20"/><w:color w:val="0F2440"/></w:rPr><w:t>•   </w:t></w:r>
                        <w:r><w:rPr><w:sz w:val="20"/><w:color w:val="1D2939"/></w:rPr><w:t>{xml_escape(it)}</w:t></w:r>
                    </w:p>
                    ''')
            elif el_type == "callout":
                body_xml.append(f'''
                <w:p>
                    <w:pPr>
                        <w:pBdr><w:left w:val="single" w:sz="24" w:space="14" w:color="0F2440"/></w:pBdr>
                        <w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/>
                        <w:spacing w:before="160" w:after="40"/>
                    </w:pPr>
                    <w:r><w:rPr><w:b/><w:sz w:val="19"/><w:color w:val="0F2440"/></w:rPr>
                    <w:t>{xml_escape(el["title"].upper())}</w:t></w:r>
                </w:p>
                <w:p>
                    <w:pPr>
                        <w:pBdr><w:left w:val="single" w:sz="24" w:space="14" w:color="0F2440"/></w:pBdr>
                        <w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/>
                        <w:spacing w:before="0" w:after="160" w:line="276" w:lineRule="auto"/>
                    </w:pPr>
                    <w:r><w:rPr><w:sz w:val="18"/><w:color w:val="344054"/></w:rPr>
                    <w:t>{xml_escape(el["text"])}</w:t></w:r>
                </w:p>
                ''')
            elif el_type == "table":
                t_title = el["title"]
                headers = el["headers"]
                rows = el["rows"]
                col_pcts = el.get("col_pcts") or [100.0 / len(headers)] * len(headers)
                col_dxas = [int(14570 * (p / 100.0)) for p in col_pcts]

                if t_title:
                    body_xml.append(f'''
                    <w:p>
                        <w:pPr><w:spacing w:before="180" w:after="80"/></w:pPr>
                        <w:r><w:rPr><w:b/><w:sz w:val="19"/><w:color w:val="0F2440"/></w:rPr>
                        <w:t>{xml_escape(t_title)}</w:t></w:r>
                    </w:p>
                    ''')

                t_rows = []
                # Header row with tblHeader so Word automatically repeats on page break
                h_cells = []
                for i, h_txt in enumerate(headers):
                    h_cells.append(f'''
                    <w:tc>
                        <w:tcPr><w:tcW w:w="{col_dxas[i]}" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="0F2440"/></w:tcPr>
                        <w:p><w:pPr><w:spacing w:before="60" w:after="60"/></w:pPr>
                        <w:r><w:rPr><w:b/><w:sz w:val="17"/><w:color w:val="FFFFFF"/></w:rPr><w:t>{xml_escape(h_txt)}</w:t></w:r></w:p>
                    </w:tc>
                    ''')
                joined_h = "".join(h_cells)
                t_rows.append(f"<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>{joined_h}</w:tr>")

                for r_idx, row in enumerate(rows):
                    r_cells = []
                    bg = "F8FAFC" if (r_idx % 2 == 1) else "FFFFFF"
                    for c_idx, val in enumerate(row):
                        is_bold = (c_idx == 0 or ("£" in str(val) and c_idx >= len(row) - 2))
                        b_tag = "<w:b/>" if is_bold else ""
                        c_color = "0F2440" if is_bold else "344054"
                        r_cells.append(f'''
                        <w:tc>
                            <w:tcPr><w:tcW w:w="{col_dxas[c_idx]}" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="{bg}"/></w:tcPr>
                            <w:p><w:pPr><w:spacing w:before="50" w:after="50"/></w:pPr>
                            <w:r><w:rPr>{b_tag}<w:sz w:val="17"/><w:color w:val="{c_color}"/></w:rPr><w:t>{xml_escape(val)}</w:t></w:r></w:p>
                        </w:tc>
                        ''')
                    joined_r = "".join(r_cells)
                    t_rows.append(f"<w:tr><w:trPr><w:cantSplit/></w:trPr>{joined_r}</w:tr>")

                body_xml.append(f'''
                <w:tbl>
                    <w:tblPr>
                        <w:tblW w:w="14570" w:type="dxa"/>
                        <w:tblBorders>
                            <w:top w:val="single" w:sz="18" w:space="0" w:color="0F2440"/>
                            <w:left w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                            <w:bottom w:val="single" w:sz="18" w:space="0" w:color="0F2440"/>
                            <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="EAECF0"/>
                            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="EAECF0"/>
                        </w:tblBorders>
                        <w:tblCellMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tblCellMar>
                    </w:tblPr>
                    {"".join(t_rows)}
                </w:tbl>
                <w:p><w:pPr><w:spacing w:before="80" w:after="160"/></w:pPr></w:p>
                ''')
            elif el_type == "grid":
                g_title = el["title"]
                items = el["items"]
                num_cols = el.get("cols", 2)
                col_w = 14570 // num_cols

                if g_title:
                    body_xml.append(f'''
                    <w:p>
                        <w:pPr><w:spacing w:before="180" w:after="80"/></w:pPr>
                        <w:r><w:rPr><w:b/><w:sz w:val="19"/><w:color w:val="0F2440"/></w:rPr>
                        <w:t>{xml_escape(g_title)}</w:t></w:r>
                    </w:p>
                    ''')

                g_rows = []
                n_rows = (len(items) + num_cols - 1) // num_cols
                for r in range(n_rows):
                    row_items = items[r * num_cols : (r + 1) * num_cols]
                    cells = []
                    for c_idx in range(num_cols):
                        if c_idx < len(row_items):
                            k, v = row_items[c_idx]
                            cells.append(f'''
                            <w:tc>
                                <w:tcPr><w:tcW w:w="{col_w}" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/></w:tcPr>
                                <w:p><w:pPr><w:spacing w:before="50" w:after="30"/></w:pPr>
                                <w:r><w:rPr><w:b/><w:sz w:val="17"/><w:color w:val="0F2440"/></w:rPr><w:t>{xml_escape(k)}</w:t></w:r></w:p>
                                <w:p><w:pPr><w:spacing w:before="0" w:after="50"/></w:pPr>
                                <w:r><w:rPr><w:sz w:val="17"/><w:color w:val="344054"/></w:rPr><w:t>{xml_escape(v)}</w:t></w:r></w:p>
                            </w:tc>
                            ''')
                        else:
                            cells.append(f'<w:tc><w:tcPr><w:tcW w:w="{col_w}" w:type="dxa"/></w:tcPr><w:p/></w:tc>')
                    joined_c = "".join(cells)
                    g_rows.append(f"<w:tr><w:trPr><w:cantSplit/></w:trPr>{joined_c}</w:tr>")

                body_xml.append(f'''
                <w:tbl>
                    <w:tblPr>
                        <w:tblW w:w="14570" w:type="dxa"/>
                        <w:tblBorders>
                            <w:top w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                            <w:left w:val="single" w:sz="18" w:space="0" w:color="0F2440"/>
                            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                            <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="EAECF0"/>
                            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="EAECF0"/>
                        </w:tblBorders>
                        <w:tblCellMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tblCellMar>
                    </w:tblPr>
                    {"".join(g_rows)}
                </w:tbl>
                <w:p><w:pPr><w:spacing w:before="80" w:after="160"/></w:pPr></w:p>
                ''')
            elif el_type == "flow":
                f_title = el["title"]
                stages = el["stages"]
                col_w = 14570 // len(stages)

                if f_title:
                    body_xml.append(f'''
                    <w:p>
                        <w:pPr><w:spacing w:before="180" w:after="80"/></w:pPr>
                        <w:r><w:rPr><w:b/><w:sz w:val="19"/><w:color w:val="0F2440"/></w:rPr>
                        <w:t>{xml_escape(f_title)}</w:t></w:r>
                    </w:p>
                    ''')

                cells = []
                for s_num, s_title, s_desc in stages:
                    cells.append(f'''
                    <w:tc>
                        <w:tcPr><w:tcW w:w="{col_w}" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/></w:tcPr>
                        <w:p><w:pPr><w:spacing w:before="50" w:after="20"/></w:pPr>
                        <w:r><w:rPr><w:b/><w:sz w:val="15"/><w:color w:val="0F2440"/></w:rPr><w:t>STAGE {xml_escape(s_num)}: {xml_escape(s_title)}</w:t></w:r></w:p>
                        <w:p><w:pPr><w:spacing w:before="0" w:after="50"/></w:pPr>
                        <w:r><w:rPr><w:sz w:val="14"/><w:color w:val="344054"/></w:rPr><w:t>{xml_escape(s_desc)}</w:t></w:r></w:p>
                    </w:tc>
                    ''')

                body_xml.append(f'''
                <w:tbl>
                    <w:tblPr>
                        <w:tblW w:w="14570" w:type="dxa"/>
                        <w:tblBorders>
                            <w:top w:val="single" w:sz="18" w:space="0" w:color="0F2440"/>
                            <w:left w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                            <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
                            <w:insideH w:val="none"/>
                            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="EAECF0"/>
                        </w:tblBorders>
                        <w:tblCellMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tblCellMar>
                    </w:tblPr>
                    <w:tr><w:trPr><w:cantSplit/></w:trPr>{"".join(cells)}</w:tr>
                </w:tbl>
                <w:p><w:pPr><w:spacing w:before="80" w:after="160"/></w:pPr></w:p>
                ''')

        # Section Properties: Landscape A4
        sect_pr = '''
        <w:sectPr>
            <w:headerReference w:type="default" r:id="rId6"/>
            <w:footerReference w:type="default" r:id="rId7"/>
            <w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/>
            <w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="720" w:footer="720"/>
            <w:cols w:space="720"/>
            <w:docGrid w:linePitch="360"/>
        </w:sectPr>
        '''

        document_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
                    xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
            <w:body>
                {"".join(body_xml)}
                {sect_pr}
            </w:body>
        </w:document>
        '''

        header_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:p>
                <w:pPr>
                    <w:pBdr><w:bottom w:val="single" w:sz="4" w:space="4" w:color="D0D7DE"/></w:pBdr>
                    <w:spacing w:before="0" w:after="0"/>
                </w:pPr>
                <w:r><w:rPr><w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica"/><w:b/><w:sz w:val="15"/><w:color w:val="0F2440"/></w:rPr>
                <w:t>{xml_escape(self.doc.title)} // {xml_escape(self.doc.doc_ref)}</w:t></w:r>
            </w:p>
        </w:hdr>
        '''

        footer_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:p>
                <w:pPr>
                    <w:pBdr><w:top w:val="single" w:sz="4" w:space="4" w:color="D0D7DE"/></w:pBdr>
                    <w:spacing w:before="0" w:after="0"/>
                </w:pPr>
                <w:r><w:rPr><w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica"/><w:sz w:val="14"/><w:color w:val="667085"/></w:rPr>
                <w:t>CONFIDENTIAL // FOR INTERNAL BOARD DIRECTORS &amp; REGISTERED MANAGER USE ONLY</w:t></w:r>
                <w:r><w:rPr><w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica"/><w:b/><w:sz w:val="14"/><w:color w:val="0F2440"/></w:rPr>
                <w:tab/><w:t>PAGE </w:t></w:r>
                <w:fldSimple w:instr="PAGE"/>
                <w:r><w:rPr><w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica"/><w:sz w:val="14"/><w:color w:val="0F2440"/></w:rPr><w:t> OF </w:t></w:r>
                <w:fldSimple w:instr="NUMPAGES"/>
            </w:p>
        </w:ftr>
        '''

        content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
            <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
            <Default Extension="xml" ContentType="application/xml"/>
            <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
            <Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>
            <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
        </Types>
        '''

        pkg_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
            <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
        </Relationships>
        '''

        doc_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <Relationships xmlns="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
            <Relationship Id="rId6" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>
            <Relationship Id="rId7" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
        </Relationships>
        '''

        with zipfile.ZipFile(self.filename, 'w', zipfile.ZIP_DEFLATED) as docx:
            docx.writestr('[Content_Types].xml', content_types.strip())
            docx.writestr('_rels/.rels', pkg_rels.strip())
            docx.writestr('word/_rels/document.xml.rels', doc_rels.strip())
            docx.writestr('word/header1.xml', header_xml.strip())
            docx.writestr('word/footer1.xml', footer_xml.strip())
            docx.writestr('word/document.xml', document_xml.strip())

        print(f"✓ Generated Landscape A4 Word (.docx): '{self.filename}'.")
        return os.path.getsize(self.filename)

print("Landscape Journal Engine loaded successfully.")
