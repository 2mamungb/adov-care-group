#!/usr/bin/env python3
"""
Fairytales SMM - Executive All-in-One Business Plan PDF Generator
Produces a high-resolution, print-ready, boardroom-grade PDF document for the CEO.
"""

import sys
import zlib

class PDFDocument:
    def __init__(self, filename="Fairytales_SMM_Executive_All_In_One_Business_Plan.pdf"):
        self.filename = filename
        self.pages = []  # List of streams
        self.width = 595.28   # A4 width in pt
        self.height = 841.89  # A4 height in pt
        self.margin_x = 45.0
        self.margin_top = 45.0
        self.margin_bottom = 45.0
        self.content_w = self.width - 2 * self.margin_x

    def add_page(self):
        page = PDFPage(self.width, self.height, self.margin_x, self.margin_top, self.margin_bottom)
        self.pages.append(page)
        return page

    def save(self):
        objects = []
        
        # 1: Catalog
        objects.append("<< /Type /Catalog /Pages 2 0 R >>")
        
        # 2: Pages container (placeholder, filled later)
        pages_obj_index = 2
        
        # We will create Font objects
        # 3: Helvetica
        # 4: Helvetica-Bold
        # 5: Helvetica-Oblique
        font_helv = 3
        font_bold = 4
        font_oblique = 5
        
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
        objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>")
        
        # Next object IDs will be Pages and Page contents
        current_obj_id = 6
        page_obj_ids = []
        content_obj_ids = []
        
        for i, page in enumerate(self.pages):
            page_obj_id = current_obj_id
            content_obj_id = current_obj_id + 1
            current_obj_id += 2
            
            page_obj_ids.append(page_obj_id)
            content_obj_ids.append(content_obj_id)
            
            # Generate stream
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
            
        # Now define object 2 (Pages)
        kids_str = " ".join([f"{pid} 0 R" for pid in page_obj_ids])
        pages_dict = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(page_obj_ids)} >>"
        
        # Assemble final PDF byte array
        out = bytearray()
        out.extend(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        
        offsets = {}
        
        # Object 1: Catalog
        offsets[1] = len(out)
        out.extend(f"1 0 obj\n{objects[0]}\nendobj\n".encode('latin1'))
        
        # Object 2: Pages
        offsets[2] = len(out)
        out.extend(f"2 0 obj\n{pages_dict}\nendobj\n".encode('latin1'))
        
        # Fonts
        for font_id, font_str in [(3, objects[1]), (4, objects[2]), (5, objects[3])]:
            offsets[font_id] = len(out)
            out.extend(f"{font_id} 0 obj\n{font_str}\nendobj\n".encode('latin1'))
            
        # Pages and contents
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
            
        # Cross-reference table
        xref_offset = len(out)
        out.extend(f"xref\n0 {current_obj_id}\n".encode('latin1'))
        out.extend(b"0000000000 65535 f \n")
        for i in range(1, current_obj_id):
            offset = offsets[i]
            out.extend(f"{offset:010d} 00000 n \n".encode('latin1'))
            
        # Trailer
        out.extend(f"trailer\n<< /Size {current_obj_id} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode('latin1'))
        
        with open(self.filename, "wb") as f:
            f.write(out)
        print(f"Generated PDF '{self.filename}' with {len(self.pages)} pages ({len(out)} bytes).")


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
            '\u2022': chr(149), # Windows-1252 bullet
            '\u2013': '-',
            '\u2014': '--',
            '\u2018': "'",
            '\u2019': "'",
            '\u201c': '"',
            '\u201d': '"',
            '£': chr(163),
            '≥': '>=',
            '≤': '<=',
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
            approx_w = len(text) * size * 0.52
            x = x + max(0, (max_w - approx_w) / 2)
        elif align == "right" and max_w:
            approx_w = len(text) * size * 0.52
            x = x + max_w - approx_w
            
        self.ops.append(f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({safe}) Tj ET")

    def draw_wrapped_text(self, text, x, y, max_w, font="F1", size=9.5, leading=13.0):
        words = text.split()
        lines = []
        current_line = []
        
        char_w = size * 0.50
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
            # Running Header
            res.append("0.45 0.55 0.65 RG 0.5 w")
            res.append(f"{self.mx:.2f} {self.height - 35:.2f} m {self.width - self.mx:.2f} {self.height - 35:.2f} l S")
            res.append(f"BT /F2 8.0 Tf 0.3 0.4 0.5 rg {self.mx:.2f} {self.height - 30:.2f} Td (FAIRYTALES SMM // EXECUTIVE ALL-IN-ONE BUSINESS PLAN) Tj ET")
            res.append(f"BT /F1 8.0 Tf 0.5 0.6 0.7 rg {self.width - self.mx - 150:.2f} {self.height - 30:.2f} Td (CODICOTE HQ // CONFIDENTIAL) Tj ET")
            
            # Running Footer
            res.append("0.85 0.88 0.92 RG 0.5 w")
            res.append(f"{self.mx:.2f} 40.00 m {self.width - self.mx:.2f} 40.00 l S")
            res.append(f"BT /F1 8.0 Tf 0.45 0.50 0.58 rg {self.mx:.2f} 28.00 Td (High Heath Farm, Whitwell Rd, Codicote, SG4 8SZ) Tj ET")
            page_str = f"Page {page_num} of {total_pages}"
            res.append(f"BT /F2 8.0 Tf 0.25 0.35 0.50 rg {self.width - self.mx - 65:.2f} 28.00 Td ({page_str}) Tj ET")
            
        res.extend(self.ops)
        return "\n".join(res)


def create_all_in_one_business_plan():
    doc = PDFDocument("Fairytales_SMM_Executive_All_In_One_Business_Plan.pdf")
    
    # -------------------------------------------------------------
    # PAGE 1: COVER PAGE
    # -------------------------------------------------------------
    p1 = doc.add_page()
    p1.is_cover = True
    
    # Background Navy Accent Block
    p1.set_fill_color(0.06, 0.09, 0.16) # #0F172A
    p1.draw_rect(0, 0, p1.width, p1.height)
    
    # Gold decorative top stripe
    p1.set_fill_color(0.85, 0.55, 0.13) # Gold #D97706
    p1.draw_rect(0, p1.height - 14, p1.width, 14)
    
    # Inner framed container
    p1.set_fill_color(0.10, 0.15, 0.26)
    p1.set_stroke_color(0.20, 0.28, 0.45)
    p1.draw_rect(40, 45, p1.width - 80, p1.height - 110, fill=True, stroke=True, stroke_w=1.5)
    
    # Agency Brand Pill
    p1.set_fill_color(0.85, 0.55, 0.13)
    p1.draw_rect(70, p1.height - 120, 160, 24, fill=True)
    p1.draw_text("FAIRYTALES SMM", 82, p1.height - 105, font="F2", size=11, align="left")
    
    # Main Titles
    p1.set_fill_color(1.0, 1.0, 1.0)
    p1.draw_text("EXECUTIVE ALL-IN-ONE", 70, p1.height - 165, font="F2", size=26)
    p1.draw_text("BUSINESS PLAN & GOVERNANCE SOP", 70, p1.height - 198, font="F2", size=22)
    
    p1.set_fill_color(0.85, 0.55, 0.13)
    p1.draw_text("Multi-Channel E-Commerce // Standalone Agency // Pan-European Scale", 70, p1.height - 228, font="F2", size=11.5)
    
    # White horizontal divider
    p1.set_stroke_color(0.35, 0.45, 0.65)
    p1.draw_line(70, p1.height - 245, p1.width - 70, p1.height - 245, stroke_w=1.2)
    
    # Subtitle Paragraph
    p1.set_fill_color(0.82, 0.88, 0.95)
    desc = (
        "A comprehensive, boardroom-ready operating masterplan establishing the 3-Year growth "
        "strategy from the Codicote Headquarters into a 15.2M ARR pan-European multinational agency. "
        "Incorporates multi-channel marketplace distribution (Amazon FBA/FBM/SFP & Vendor Central, "
        "TikTok Shop, Temu, B&Q, DTC, and Wholesale), immediate Christmas/Q4 sprint execution, "
        "and executive Standard Operating Procedures for the CEO and Managing Partner."
    )
    p1.draw_wrapped_text(desc, 70, p1.height - 270, p1.width - 140, font="F1", size=10.0, leading=15.0)
    
    # Metadata Presentation Card
    card_y = 100
    p1.set_fill_color(0.07, 0.11, 0.20)
    p1.set_stroke_color(0.85, 0.55, 0.13)
    p1.draw_rect(70, card_y, p1.width - 140, 240, fill=True, stroke=True, stroke_w=1.2)
    
    p1.set_fill_color(0.85, 0.55, 0.13)
    p1.draw_text("EXECUTIVE ENTERPRISE DIRECTORY & METADATA", 90, card_y + 215, font="F2", size=11)
    
    meta_items = [
        ("Entity Name:", "Fairytales SMM (Standalone Limited Agency & Brand Group)"),
        ("Corporate Address:", "High Heath Farm, Whitwell Road, Codicote, Hertfordshire, SG4 8SZ"),
        ("Executive Leadership:", "Chief Executive Officer (CEO) & Managing Partner"),
        ("Effective Period:", "Fiscal Years 2026 - 2029 (Q4 Blitz through Pan-European Year 3)"),
        ("Primary Advisory Unit:", "Strategic Management Director & Marketplace Operations Lead"),
        ("Headquarters Role:", "Executive Command Center & In-House Content Studio Campus"),
        ("Classification:", "BOARDROOM CONFIDENTIAL // READY TO PRINT & EXECUTE"),
    ]
    
    cur_my = card_y + 190
    for label, val in meta_items:
        p1.set_fill_color(0.55, 0.68, 0.85)
        p1.draw_text(label, 90, cur_my, font="F2", size=9.0)
        p1.set_fill_color(1.0, 1.0, 1.0)
        p1.draw_text(val, 225, cur_my, font="F1", size=9.0)
        cur_my -= 24
        
    p1.set_fill_color(0.50, 0.60, 0.75)
    p1.draw_text("Prepared for official review and execution by the Board of Directors.", 70, 70, font="F3", size=8.5)

    # -------------------------------------------------------------
    # PAGE 2: EXECUTIVE SUMMARY & DUAL-ENGINE ARCHITECTURE
    # -------------------------------------------------------------
    p2 = doc.add_page()
    
    # Section Header
    p2.set_fill_color(0.06, 0.09, 0.16)
    p2.draw_text("1. EXECUTIVE SUMMARY & DUAL-ENGINE ARCHITECTURE", 45, 785, font="F2", size=15)
    p2.set_stroke_color(0.85, 0.55, 0.13)
    p2.draw_line(45, 775, p2.width - 45, 775, stroke_w=1.5)
    
    # Vision Text
    p2.set_fill_color(0.15, 0.20, 0.28)
    summary_text = (
        "Fairytales SMM is engineered as an agile, high-margin, dual-engine enterprise operating "
        "from High Heath Farm, Codicote. Traditional agencies suffer from high client churn because they "
        "rely on theoretical marketing without skin in the game. Fairytales SMM eliminates this vulnerability "
        "by pairing an in-house e-commerce testing lab with an elite external B2B client agency."
    )
    p2.draw_wrapped_text(summary_text, 45, 755, p2.cw, font="F1", size=9.5, leading=14.0)
    
    # Dual Engine Comparison Table/Boxes
    box_w = (p2.cw - 15) / 2
    # Left Box: In-House Brands
    p2.set_fill_color(0.96, 0.98, 1.0)
    p2.set_stroke_color(0.15, 0.35, 0.75)
    p2.draw_rect(45, 595, box_w, 130, fill=True, stroke=True, stroke_w=1.2)
    p2.set_fill_color(0.10, 0.25, 0.65)
    p2.draw_text("ENGINE 1: IN-HOUSE PRODUCT LINES", 55, 705, font="F2", size=10)
    inhouse_pts = [
        "• Real-time testing lab for viral UGC & ad hooks.",
        "• Omnichannel distribution across Amazon 3P/1P,",
        "  TikTok Shop, Temu Semi-Managed, B&Q, & DTC.",
        "• Zero-guesswork conversion feedback loop.",
        "• Complete asset ownership and high gross margins."
    ]
    cur_y = 685
    for pt in inhouse_pts:
        p2.draw_text(pt, 55, cur_y, font="F1", size=8.5)
        cur_y -= 16

    # Right Box: Standalone Agency
    p2.set_fill_color(0.98, 0.98, 0.95)
    p2.set_stroke_color(0.85, 0.55, 0.13)
    p2.draw_rect(45 + box_w + 15, 595, box_w, 130, fill=True, stroke=True, stroke_w=1.2)
    p2.set_fill_color(0.70, 0.40, 0.05)
    p2.draw_text("ENGINE 2: STANDALONE B2B AGENCY", 55 + box_w + 15, 705, font="F2", size=10)
    agency_pts = [
        "• External client retainers (2,250 to 8,500/mo).",
        "• Pre-vetted creator network (100-point rubric).",
        "• 7-Day rapid creative turnaround SLAs.",
        "• Paid social amplification via Spark Ads & Meta.",
        "• High EBITDA margins (24% to 27%) and recurring ARR."
    ]
    cur_y = 685
    for pt in agency_pts:
        p2.draw_text(pt, 55 + box_w + 15, cur_y, font="F1", size=8.5)
        cur_y -= 16
        
    # Strategic Value Chain
    p2.set_fill_color(0.06, 0.09, 0.16)
    p2.draw_text("STRATEGIC CORE OBJECTIVES (2026 - 2029)", 45, 565, font="F2", size=11)
    
    objectives = [
        ("1. Immediate Q4 Holiday Sprint (Days 1 - 60):", "Capture peak Christmas shopping revenue across both in-house brands and external e-commerce clients seeking rapid 7-day holiday UGC and creator seedings."),
        ("2. Multi-Channel E-Commerce Dominance:", "Establish operational mastery across Amazon (FBA, FBM, SFP, Vendor Central), TikTok Shop, Temu Semi-Managed, B&Q Mirakl, DTC, and Wholesale."),
        ("3. High Heath Farm Production Campus:", "Transform the Codicote headquarters into a dedicated high-volume content house and physical creator testing studio."),
        ("4. Pan-European Expansion (3-Year Plan):", "Scale operations into Germany (DACH hub), France (Paris hub), and Benelux/Dublin, crossing 15.2M ARR with 75+ active enterprise retainers.")
    ]
    
    cur_oy = 540
    for title, desc in objectives:
        p2.set_fill_color(0.10, 0.25, 0.60)
        p2.draw_text(title, 45, cur_oy, font="F2", size=9.2)
        p2.set_fill_color(0.20, 0.25, 0.35)
        p2.draw_wrapped_text(desc, 45, cur_oy - 14, p2.cw, font="F1", size=8.8, leading=12.0)
        cur_oy -= 42

    # Executive Governance Callout
    p2.set_fill_color(0.94, 0.96, 0.98)
    p2.set_stroke_color(0.20, 0.40, 0.80)
    p2.draw_rect(45, 120, p2.cw, 75, fill=True, stroke=True, stroke_w=1.0)
    p2.set_fill_color(0.10, 0.20, 0.50)
    p2.draw_text("EXECUTIVE GOVERNANCE ALIGNMENT", 60, 175, font="F2", size=10)
    gov_text = (
        "The leadership duo operates with strict accountability: the CEO commands External Growth, "
        "Enterprise Sales, and European Strategy; the Managing Partner commands Internal Campaign "
        "Execution, SLA Enforcement, and Profitability. Full governance SOP detailed on Pages 7 & 8."
    )
    p2.draw_wrapped_text(gov_text, 60, 158, p2.cw - 30, font="F1", size=8.5, leading=12.0)

    # -------------------------------------------------------------
    # PAGE 3: MULTI-CHANNEL E-COMMERCE ECOSYSTEM
    # -------------------------------------------------------------
    p3 = doc.add_page()
    p3.set_fill_color(0.06, 0.09, 0.16)
    p3.draw_text("2. MULTI-CHANNEL E-COMMERCE ARCHITECTURE", 45, 785, font="F2", size=15)
    p3.set_stroke_color(0.85, 0.55, 0.13)
    p3.draw_line(45, 775, p3.width - 45, 775, stroke_w=1.5)
    
    p3.set_fill_color(0.15, 0.20, 0.28)
    intro_p3 = (
        "To maximize retail volume, eliminate platform dependency, and maintain high margin resilience, "
        "the in-house brand operates across seven distinct distribution channels coordinated through a "
        "central Order Management System (Linnworks/ChannelEngine) and 3PL fulfillment network."
    )
    p3.draw_wrapped_text(intro_p3, 45, 755, p3.cw, font="F1", size=9.5, leading=14.0)
    
    # Channel Matrix Table
    table_y = 700
    p3.set_fill_color(0.06, 0.09, 0.16)
    p3.draw_rect(45, table_y, p3.cw, 22, fill=True)
    p3.set_fill_color(1.0, 1.0, 1.0)
    p3.draw_text("CHANNEL", 50, table_y + 7, font="F2", size=8.5)
    p3.draw_text("MODEL", 125, table_y + 7, font="F2", size=8.5)
    p3.draw_text("DISPATCH SLA", 200, table_y + 7, font="F2", size=8.5)
    p3.draw_text("TARGET MARGIN", 285, table_y + 7, font="F2", size=8.5)
    p3.draw_text("KEY OPERATIONAL MANDATE", 380, table_y + 7, font="F2", size=8.5)
    
    rows = [
        ("Amazon FBA", "3P Prime", "Amazon standard", "22% - 30% Net", "IPI > 500, Vine reviews, A+ Brand Story"),
        ("Amazon FBM", "3P Merchant", "Same-day / 24h", "30% - 40% Net", "VTR > 95%, Late Shipment Rate < 4%"),
        ("Amazon SFP", "Seller Prime", "Nationwide 1-2 day", "28% - 38% Net", "Buy Shipping API, weekend shipping ops"),
        ("Vendor Central", "1P Wholesale", "Weekly PO window", "18% - 25% Net", "EDI 856 ASN compliance, zero chargebacks"),
        ("TikTok Shop", "Social Comm", "48h dispatch", "25% - 35% Net", "Affiliate open/targeted collabs, Spark Ads"),
        ("Temu", "Semi-Managed", "24-48h domestic", "20% - 30% Net", "Fast local 3PL dispatch, volume scale"),
        ("B&Q (Mirakl)", "UK Retail", "48h dispatch", "25% - 35% Net", "GTIN categorization, UKCA/CE compliance"),
        ("DTC Website", "Shopify Plus", "24h dispatch", "45% - 60% Net", "Klaviyo retention flows, 1-click checkout"),
        ("B2B Wholesale", "Trade Desk", "Pallet / LTL", "35% - 45% Net", "Strict MAP policy, Proforma & Net 30/60")
    ]
    
    cur_ty = table_y - 18
    for i, (ch, mod, sla, marg, mand) in enumerate(rows):
        bg = (0.96, 0.97, 0.99) if (i % 2 == 0) else (1.0, 1.0, 1.0)
        p3.set_fill_color(*bg)
        p3.draw_rect(45, cur_ty, p3.cw, 18, fill=True)
        
        p3.set_fill_color(0.10, 0.15, 0.25)
        p3.draw_text(ch, 50, cur_ty + 5, font="F2", size=8.0)
        p3.draw_text(mod, 125, cur_ty + 5, font="F1", size=8.0)
        p3.draw_text(sla, 200, cur_ty + 5, font="F1", size=8.0)
        p3.draw_text(marg, 285, cur_ty + 5, font="F1", size=8.0)
        p3.draw_text(mand, 380, cur_ty + 5, font="F1", size=7.8)
        cur_ty -= 18
        
    # Deep Dive: Amazon 1P & 3P Strategic Integration
    p3.set_fill_color(0.06, 0.09, 0.16)
    p3.draw_text("AMAZON HYBRID GOVERNANCE & LOGISTICS INVENTORY BUFFERING", 45, cur_ty - 15, font="F2", size=10.5)
    
    p3_body = (
        "1. Amazon Hybrid Model: Operating both 3P (Seller Central) and 1P (Vendor Central) ensures complete "
        "catalog protection. If Amazon temporarily pauses 1P wholesale Purchase Orders, 3P FBA/FBM listings "
        "automatically win the Buy Box without lost sales rank. Never offer discounts to 1P that violate MAP.\n\n"
        "2. Centralized Inventory Buffer Rules: To prevent overselling and protect Seller Fulfilled Prime (SFP) "
        "and TikTok Shop SLAs, a virtual buffer of -3 units is dynamically held back on high-velocity social "
        "channels whenever warehouse stock drops below 15 units. Sync frequency set to every 5 minutes."
    )
    p3.draw_wrapped_text(p3_body, 45, cur_ty - 35, p3.cw, font="F1", size=8.8, leading=13.0)

    # B2B Wholesale Desk Highlight
    p3.set_fill_color(0.96, 0.98, 0.95)
    p3.set_stroke_color(0.20, 0.60, 0.30)
    p3.draw_rect(45, 125, p3.cw, 70, fill=True, stroke=True, stroke_w=1.0)
    p3.set_fill_color(0.10, 0.40, 0.15)
    p3.draw_text("B2B WHOLESALE TRADE DESK & MAP ENFORCEMENT", 60, 175, font="F2", size=9.5)
    w_text = (
        "Wholesale accounts are structured across 3 tiers (Boutique 40% off, Regional Distributor 50% off, "
        "National Chains 55-60% off). All wholesale partners MUST sign the legally binding Minimum Advertised "
        "Price (MAP) Agreement strictly prohibiting unauthorized resale on Amazon, TikTok Shop, or Temu."
    )
    p3.draw_wrapped_text(w_text, 60, 158, p3.cw - 30, font="F1", size=8.2, leading=11.5)

    # -------------------------------------------------------------
    # PAGE 4: FAIRYTALES SMM STANDALONE AGENCY BLUEPRINT
    # -------------------------------------------------------------
    p4 = doc.add_page()
    p4.set_fill_color(0.06, 0.09, 0.16)
    p4.draw_text("3. STANDALONE FAIRYTALES SMM AGENCY & CREATOR ENGINE", 45, 785, font="F2", size=15)
    p4.set_stroke_color(0.85, 0.55, 0.13)
    p4.draw_line(45, 775, p4.width - 45, 775, stroke_w=1.5)
    
    p4.set_fill_color(0.15, 0.20, 0.28)
    intro_p4 = (
        "Fairytales SMM is incorporated as a standalone agency providing high-impact creator marketing, "
        "UGC video production, and social commerce retainers to external corporate clients. Our core differentiator "
        "is performance: every creative is engineered with 3-second hook variations and whitelisted for paid ad scale."
    )
    p4.draw_wrapped_text(intro_p4, 45, 755, p4.cw, font="F1", size=9.5, leading=14.0)
    
    # Retainer Packages Table
    p4.set_fill_color(0.06, 0.09, 0.16)
    p4.draw_rect(45, 680, p4.cw, 22, fill=True)
    p4.set_fill_color(1.0, 1.0, 1.0)
    p4.draw_text("PACKAGE TIER", 55, 687, font="F2", size=8.5)
    p4.draw_text("INVESTMENT", 150, 687, font="F2", size=8.5)
    p4.draw_text("DIRECT COGS", 235, 687, font="F2", size=8.5)
    p4.draw_text("GROSS MARGIN", 325, 687, font="F2", size=8.5)
    p4.draw_text("CORE DELIVERABLES & SCOPE", 415, 687, font="F2", size=8.5)
    
    tiers = [
        ("Tier 1: UGC Creative Suite", "2,250 / mo", "1,100 (48.9%)", "1,150 (51.1%)", "8 UGC ad videos, 24 hook variations, Spark codes"),
        ("Tier 2: Seeding & TikTok Shop", "4,500 / mo", "2,150 (47.8%)", "2,350 (52.2%)", "30 Creator seedings, affiliate management, reporting"),
        ("Tier 3: Omnipresence Retainer", "8,500 / mo", "4,250 (50.0%)", "4,250 (50.0%)", "Tier 1+2, Celebrity ambassadorship, Paid Meta/TikTok ads")
    ]
    
    cur_ty = 658
    for i, (name, inv, cogs, gm, scope) in enumerate(tiers):
        bg = (0.97, 0.98, 1.0) if (i % 2 == 0) else (1.0, 1.0, 1.0)
        p4.set_fill_color(*bg)
        p4.draw_rect(45, cur_ty, p4.cw, 22, fill=True)
        p4.set_fill_color(0.10, 0.15, 0.25)
        p4.draw_text(name, 55, cur_ty + 7, font="F2", size=8.0)
        p4.draw_text(inv, 150, cur_ty + 7, font="F1", size=8.0)
        p4.draw_text(cogs, 235, cur_ty + 7, font="F1", size=8.0)
        p4.draw_text(gm, 325, cur_ty + 7, font="F1", size=8.0)
        p4.draw_text(scope, 415, cur_ty + 7, font="F1", size=7.5)
        cur_ty -= 22
        
    # The 100-Point Creator Vetting Scorecard
    p4.set_fill_color(0.06, 0.09, 0.16)
    p4.draw_text("PROPRIETARY 100-POINT CREATOR VETTING SCORECARD", 45, cur_ty - 20, font="F2", size=10.5)
    
    scorecard_intro = (
        "Before any product samples or paid deposits are dispatched, talent scouts evaluate influencers "
        "across five mandatory 20-point pillars. Minimum required threshold for paid booking: 85/100."
    )
    p4.draw_wrapped_text(scorecard_intro, 45, cur_ty - 38, p4.cw, font="F1", size=8.8, leading=12.0)
    
    pillars = [
        ("1. Audience Authenticity (20 pts):", "> 80% real audience score (fraud/bot audit via Modash/HypeAuditor). Target geo > 60% UK/US/EU."),
        ("2. Engagement & Consistency (20 pts):", "Engagement rate >= 3.5% with consistent rolling median video view velocity across last 10 posts."),
        ("3. Visual Pacing & Lighting (20 pts):", "Crisp 1080p+ 9:16 vertical filming, studio-grade lighting, crystal clear audio, high natural charisma."),
        ("4. Hook & Script Execution (20 pts):", "Delivers punchy verbal/visual hook in < 3s; natural problem-solution flow without sounding rehearsed."),
        ("5. Commercial Compliance (20 pts):", "Fast responsiveness (< 24h); mandatory agreement to grant 90-365 day Spark Ad & Meta whitelisting codes.")
    ]
    
    cur_py = cur_ty - 75
    for pil, pdesc in pillars:
        p4.set_fill_color(0.15, 0.35, 0.70)
        p4.draw_text(pil, 45, cur_py, font="F2", size=8.5)
        p4.set_fill_color(0.20, 0.25, 0.35)
        p4.draw_text(pdesc, 230, cur_py, font="F1", size=8.2)
        cur_py -= 18

    # The 3-Second UGC Formula Box
    p4.set_fill_color(0.95, 0.96, 0.98)
    p4.set_stroke_color(0.85, 0.55, 0.13)
    p4.draw_rect(45, 115, p4.cw, 80, fill=True, stroke=True, stroke_w=1.0)
    p4.set_fill_color(0.70, 0.40, 0.05)
    p4.draw_text("THE 3-SECOND VIRAL UGC CONVERSION FORMULA", 60, 180, font="F2", size=9.5)
    formula_text = (
        "[0:00-0:03] Pattern-Interrupt Hook (Visual shock, controversial question, or relatable pain-point)\n"
        "[0:03-0:15] Agitation & Discovery (Introducing hero product as the effortless solution)\n"
        "[0:15-0:30] Social Proof & Real-World Utility (Demonstrating key features, overcoming consumer objections)\n"
        "[0:30-0:45] Irresistible Call to Action (Exclusive TikTok Shop pinned discount code, shipping urgency guarantee)"
    )
    p4.draw_wrapped_text(formula_text, 60, 165, p4.cw - 30, font="F1", size=8.0, leading=11.5)

    # -------------------------------------------------------------
    # PAGE 5: IMMEDIATE CHRISTMAS & Q4 BLITZKRIEG SPRINT
    # -------------------------------------------------------------
    p5 = doc.add_page()
    p5.set_fill_color(0.06, 0.09, 0.16)
    p5.draw_text("4. IMMEDIATE CHRISTMAS & Q4 BLITZKRIEG SPRINT", 45, 785, font="F2", size=15)
    p5.set_stroke_color(0.85, 0.55, 0.13)
    p5.draw_line(45, 775, p5.width - 45, 775, stroke_w=1.5)
    
    p5.set_fill_color(0.15, 0.20, 0.28)
    intro_p5 = (
        "With Christmas 7 weeks away and Black Friday / Cyber Monday (BFCM) in 4 weeks, e-commerce brands "
        "have allocated their largest budgets of the year, yet suffer severe ad creative fatigue. "
        "Fairytales SMM deploys an immediate sprint model starting tomorrow morning to capture rapid cash flow."
    )
    p5.draw_wrapped_text(intro_p5, 45, 755, p5.cw, font="F1", size=9.5, leading=14.0)
    
    # Fast Closing Holiday Packages
    p5.set_fill_color(0.06, 0.09, 0.16)
    p5.draw_rect(45, 680, p5.cw, 22, fill=True)
    p5.set_fill_color(1.0, 1.0, 1.0)
    p5.draw_text("HOLIDAY SPRINT PACKAGE", 55, 687, font="F2", size=8.5)
    p5.draw_text("PRICE & TERMS", 190, 687, font="F2", size=8.5)
    p5.draw_text("TURNAROUND", 290, 687, font="F2", size=8.5)
    p5.draw_text("DELIVERABLES & STRATEGY", 390, 687, font="F2", size=8.5)
    
    sprints = [
        ("7-Day Holiday UGC Sprint", "1,950 (100% upfront)", "7 Business Days", "6 Festive UGC ads, 18 hooks, 90-day Spark rights"),
        ("Christmas Seeding Rush", "3,950 (50/50 terms)", "14 Business Days", "25-35 Confirmed seedings, holiday gift guides"),
        ("Full Q4 Omnipresence Blitz", "6,950 / month", "Nov - Dec Sprint", "Complete UGC + Influencers + Meta/TikTok paid ad buying")
    ]
    
    cur_ty = 658
    for i, (name, pr, sla, sc) in enumerate(sprints):
        bg = (0.98, 0.98, 0.95) if (i % 2 == 0) else (1.0, 1.0, 1.0)
        p5.set_fill_color(*bg)
        p5.draw_rect(45, cur_ty, p5.cw, 22, fill=True)
        p5.set_fill_color(0.10, 0.15, 0.25)
        p5.draw_text(name, 55, cur_ty + 7, font="F2", size=8.0)
        p5.draw_text(pr, 190, cur_ty + 7, font="F1", size=8.0)
        p5.draw_text(sla, 290, cur_ty + 7, font="F1", size=8.0)
        p5.draw_text(sc, 390, cur_ty + 7, font="F1", size=7.8)
        cur_ty -= 22
        
    # The 48-Hour Outbound B2B Pipeline
    p5.set_fill_color(0.06, 0.09, 0.16)
    p5.draw_text("THE 48-HOUR OUTBOUND CLIENT ACQUISITION CADENCE", 45, cur_ty - 20, font="F2", size=10.5)
    
    p5_outbound = (
        "1. Meta Ad Library Audit: Identify e-commerce brands spending heavily on paid ads who are running generic, "
        "non-festive creatives. Record a personalized 45-second Loom showing 3 specific Christmas gifting hooks.\n"
        "2. Direct Outreach: Send audit via cold email and Instagram brand DM. Offer frictionless 7-day turnaround.\n"
        "3. 15-Minute Close: Conduct quick strategy zoom call, present Package 1 (1,950) or Package 2 (3,950), "
        "and dispatch sample briefs to our pre-vetted creator network within 24 hours of invoice clearance."
    )
    p5.draw_wrapped_text(p5_outbound, 45, cur_ty - 40, p5.cw, font="F1", size=8.8, leading=13.0)

    # Day by Day Countdown Calendar
    p5.set_fill_color(0.06, 0.09, 0.16)
    p5.draw_text("DAY-BY-DAY COUNTDOWN TO CHRISTMAS (OCTOBER 23 - DECEMBER 24)", 45, cur_ty - 110, font="F2", size=10.5)
    
    calendar = [
        ("Oct 23 - Oct 31:", "Launch outbound audits to 50 target brands/day; seed 25 holiday creators for in-house brands."),
        ("Nov 01 - Nov 15:", "Close first 3-5 external clients; dispatch Christmas PR boxes; launch TikTok Shop holiday showcase."),
        ("Nov 16 - Nov 30 (BFCM):", "Deliver all external UGC packs; scale winning Spark Ads with 3x-5x budget during Black Friday."),
        ("Dec 01 - Dec 15:", "Christmas Shipping Cutoff push ('Order by Dec 18 for guaranteed delivery'); host weekly brand LIVEs."),
        ("Dec 16 - Dec 24:", "Post-cutoff digital gift card push; Boxing Day clearance launch; sign Q1 2027 retainer renewals.")
    ]
    
    cur_cy = cur_ty - 130
    for dates, details in calendar:
        p5.set_fill_color(0.85, 0.55, 0.13)
        p5.draw_text(dates, 45, cur_cy, font="F2", size=8.5)
        p5.set_fill_color(0.20, 0.25, 0.35)
        p5.draw_text(details, 185, cur_cy, font="F1", size=8.2)
        cur_cy -= 18

    # Parallel In-House Brand Actions
    p5.set_fill_color(0.94, 0.96, 0.98)
    p5.set_stroke_color(0.15, 0.35, 0.70)
    p5.draw_rect(45, 115, p5.cw, 75, fill=True, stroke=True, stroke_w=1.0)
    p5.set_fill_color(0.10, 0.25, 0.60)
    p5.draw_text("PARALLEL IN-HOUSE BRAND ACTIONS (IMMEDIATE DEPLOYMENT)", 60, 175, font="F2", size=9.5)
    inh_text = (
        "• Holiday Product Bundling: Create 2-3 product bundles with festive gift packaging to boost AOV by 35%.\n"
        "• TikTok Shop Affiliate Bounty: Set 20% commission with hashtags #ChristmasGiftIdeas and #TikTokMadeMeBuyIt.\n"
        "• Prominent PDP Guarantees: Add 'Guaranteed Christmas Delivery if ordered by Dec 18' on all DTC and marketplace listings."
    )
    p5.draw_wrapped_text(inh_text, 60, 160, p5.cw - 30, font="F1", size=8.0, leading=11.5)

    # -------------------------------------------------------------
    # PAGE 6: 3-YEAR PAN-EUROPEAN EXPANSION ROADMAP
    # -------------------------------------------------------------
    p6 = doc.add_page()
    p6.set_fill_color(0.06, 0.09, 0.16)
    p6.draw_text("5. 3-YEAR PAN-EUROPEAN EXPANSION ROADMAP (2026 - 2029)", 45, 785, font="F2", size=15)
    p6.set_stroke_color(0.85, 0.55, 0.13)
    p6.draw_line(45, 775, p6.width - 45, 775, stroke_w=1.5)
    
    p6.set_fill_color(0.15, 0.20, 0.28)
    intro_p6 = (
        "To build a truly defensible, enterprise-grade business valuation, Fairytales SMM executes a structured "
        "geographic rollout from our Codicote headquarters into major continental European e-commerce economies. "
        "Target: Scale from UK foundation (2.1M ARR) to 15.2M ARR across 4 European operating hubs in 36 months."
    )
    p6.draw_wrapped_text(intro_p6, 45, 755, p6.cw, font="F1", size=9.5, leading=14.0)
    
    # 3-Year Phase Breakdown
    phases = [
        ("YEAR 1 (2026-2027): UK DOMESTIC DOMINANCE & CODICOTE CAMPUS", [
            "• Headquarters & Studio: Build out the High Heath Farm, Codicote campus into a multi-set filming hub.",
            "• Market Focus: UK DTC startups, Amazon power brands, and TikTok Shop UK power sellers.",
            "• Scale Target: 1.8M - 2.4M ARR; 18-25 active retainers; 400+ vetted UK creator database.",
            "• Operational Objective: Perfect the 7-day delivery SLA and establish automated billing & reporting."
        ]),
        ("YEAR 2 (2027-2028): DACH EXPANSION (GERMANY, AUSTRIA, SWITZERLAND)", [
            "• Regional Satellite Hub: Establish Fairytales SMM GmbH in Berlin or Munich.",
            "• Strategic Logic: Germany is Europe's largest e-commerce market with high buying power and low creative agility.",
            "• Team & Roster: Hire bilingual DACH Managing Director + 3 native talent scouts; onboard 400+ German creators.",
            "• Scale Target: 6.4M ARR; 45 active retainers across UK and DACH; EU 3PL sample hub in Frankfurt."
        ]),
        ("YEAR 3 (2028-2029): PAN-EUROPEAN SCALE (FRANCE, BENELUX & SOUTHERN EUROPE)", [
            "• Regional Hubs: Paris Office (Beauty, Fashion, Luxury vertical) & Amsterdam/Dublin (Enterprise TikTok/Meta).",
            "• Strategic M&A: Execute 1-2 bolt-on acquisitions of boutique creator agencies (300k-750k deal size).",
            "• Multilingual Engine: Coordinate synchronized single-day product launches across EN, DE, FR, IT, ES.",
            "• Scale Target: 15.2M ARR; 75+ enterprise retainers; 2,500+ vetted European creators; 27% EBITDA margin."
        ])
    ]
    
    cur_phase_y = 690
    for header, bullets in phases:
        p6.set_fill_color(0.96, 0.97, 1.0)
        p6.set_stroke_color(0.15, 0.35, 0.75)
        p6.draw_rect(45, cur_phase_y - 70, p6.cw, 80, fill=True, stroke=True, stroke_w=1.0)
        p6.set_fill_color(0.10, 0.20, 0.50)
        p6.draw_text(header, 55, cur_phase_y - 8, font="F2", size=9.2)
        
        cur_by = cur_phase_y - 24
        p6.set_fill_color(0.15, 0.20, 0.30)
        for b in bullets:
            p6.draw_text(b, 55, cur_by, font="F1", size=7.8)
            cur_by -= 13
        cur_phase_y -= 95
        
    # Pan-European Legal & Tax Framework
    p6.set_fill_color(0.06, 0.09, 0.16)
    p6.draw_text("PAN-EUROPEAN CORPORATE, VAT & REGULATORY ARCHITECTURE", 45, cur_phase_y - 15, font="F2", size=10.5)
    
    p6_tax = (
        "• Holding Company: Fairytales SMM UK Ltd (Codicote HQ) serves as TopCo holding equity in regional EU operating "
        "subsidiaries (Fairytales GmbH in Germany, Fairytales SAS in France).\n"
        "• EU VAT & One-Stop-Shop (OSS): Single EU VAT registration handling cross-border agency retainers and sample dispatch.\n"
        "• GDPR & Creator Data Privacy: Strict data handling compliant with UK & EU GDPR for creator database storage.\n"
        "• Advertising Standards Compliance: Mandatory standardized disclosures adhering to UK ASA and German Wettbewerbszentrale."
    )
    p6.draw_wrapped_text(p6_tax, 45, cur_phase_y - 35, p6.cw, font="F1", size=8.5, leading=12.5)

    # -------------------------------------------------------------
    # PAGE 7: EXECUTIVE LEADERSHIP SOP: CEO & MANAGING PARTNER
    # -------------------------------------------------------------
    p7 = doc.add_page()
    p7.set_fill_color(0.06, 0.09, 0.16)
    p7.draw_text("6. STANDARD OPERATING PROCEDURES: CEO & MANAGING PARTNER", 45, 785, font="F2", size=15)
    p7.set_stroke_color(0.85, 0.55, 0.13)
    p7.draw_line(45, 775, p7.width - 45, 775, stroke_w=1.5)
    
    p7.set_fill_color(0.15, 0.20, 0.28)
    intro_p7 = (
        "To ensure decisive corporate governance, eliminate managerial overlap, and maintain rapid execution, "
        "this Standard Operating Procedure codifies the division of responsibilities, RACI decision rights, "
        "and operational cadences between the Chief Executive Officer (CEO) and the Managing Partner."
    )
    p7.draw_wrapped_text(intro_p7, 45, 755, p7.cw, font="F1", size=9.5, leading=14.0)
    
    # Division of Responsibilities Box
    rbox_w = (p7.cw - 15) / 2
    # Left: CEO
    p7.set_fill_color(0.96, 0.98, 1.0)
    p7.set_stroke_color(0.15, 0.35, 0.70)
    p7.draw_rect(45, 595, rbox_w, 130, fill=True, stroke=True, stroke_w=1.2)
    p7.set_fill_color(0.10, 0.20, 0.50)
    p7.draw_text("CHIEF EXECUTIVE OFFICER (CEO)", 55, 705, font="F2", size=9.5)
    p7.set_fill_color(0.85, 0.55, 0.13)
    p7.draw_text("EXTERNAL GROWTH, STRATEGY & ENTERPRISE", 55, 692, font="F2", size=7.5)
    ceo_duties = [
        "• Vision, 3-year European roadmap & expansion.",
        "• Closing enterprise retainers (> 10,000/month).",
        "• Treasury management & capital allocations > 5k.",
        "• Macro-celebrity talent & strategic PR alliances.",
        "• Public brand ambassadorship & board leadership."
    ]
    cur_y = 672
    p7.set_fill_color(0.15, 0.20, 0.30)
    for d in ceo_duties:
        p7.draw_text(d, 55, cur_y, font="F1", size=8.0)
        cur_y -= 15

    # Right: Managing Partner
    p7.set_fill_color(0.98, 0.98, 0.95)
    p7.set_stroke_color(0.85, 0.55, 0.13)
    p7.draw_rect(45 + rbox_w + 15, 595, rbox_w, 130, fill=True, stroke=True, stroke_w=1.2)
    p7.set_fill_color(0.60, 0.35, 0.05)
    p7.draw_text("MANAGING PARTNER (COO / DELIVERY)", 55 + rbox_w + 15, 705, font="F2", size=9.5)
    p7.set_fill_color(0.10, 0.35, 0.70)
    p7.draw_text("INTERNAL OPERATIONS, SLAS & PROFITABILITY", 55 + rbox_w + 15, 692, font="F2", size=7.5)
    mp_duties = [
        "• Daily campaign execution & 7-day turnaround SLAs.",
        "• Creator vetting (100-pt scorecard) & gifting dispatch.",
        "• UGC scripting, editing QA, & Spark code collection.",
        "• Client account management & retention (NRR > 115%).",
        "• Staffing: video editors, talent scouts, toolstack."
    ]
    cur_y = 672
    p7.set_fill_color(0.15, 0.20, 0.30)
    for d in mp_duties:
        p7.draw_text(d, 55 + rbox_w + 15, cur_y, font="F1", size=8.0)
        cur_y -= 15

    # RACI Decision Rights Matrix
    p7.set_fill_color(0.06, 0.09, 0.16)
    p7.draw_text("EXECUTIVE RACI DECISION RIGHTS MATRIX", 45, 570, font="F2", size=10.5)
    
    raci_y = 545
    p7.set_fill_color(0.06, 0.09, 0.16)
    p7.draw_rect(45, raci_y, p7.cw, 20, fill=True)
    p7.set_fill_color(1.0, 1.0, 1.0)
    p7.draw_text("KEY DECISION AREA", 55, raci_y + 6, font="F2", size=8.0)
    p7.draw_text("CEO", 260, raci_y + 6, font="F2", size=8.0)
    p7.draw_text("MANAGING PARTNER", 335, raci_y + 6, font="F2", size=8.0)
    p7.draw_text("OPERATIONS STAFF", 445, raci_y + 6, font="F2", size=8.0)
    
    raci_rows = [
        ("Pan-European Expansion & International Hubs", "ACCOUNTABLE (A)", "Consulted (C)", "Informed (I)"),
        ("Enterprise Client Retainer Closing (> 10k/mo)", "ACCOUNTABLE (A)", "Responsible (R)", "Informed (I)"),
        ("Standard Retainer Scopes & Pricing (< 10k/mo)", "Consulted (C)", "ACCOUNTABLE (A)", "Responsible (R)"),
        ("Senior Director & Executive Level Hiring", "ACCOUNTABLE (A)", "Responsible (R)", "Consulted (C)"),
        ("Operational Staff Hiring (Editors, Talent Scouts)", "Informed (I)", "ACCOUNTABLE (A)", "Responsible (R)"),
        ("Creator Rate Cards & Payout Authorizations", "Informed (I)", "ACCOUNTABLE (A)", "Responsible (R)"),
        ("Software Tools & CRM Infrastructure Selection", "Consulted (C)", "ACCOUNTABLE (A)", "Responsible (R)"),
        ("Capital Expenditures Exceeding 5,000", "ACCOUNTABLE (A)", "Responsible (R)", "Informed (I)")
    ]
    
    cur_ry = raci_y - 17
    for i, (area, c_role, m_role, s_role) in enumerate(raci_rows):
        bg = (0.97, 0.98, 0.99) if (i % 2 == 0) else (1.0, 1.0, 1.0)
        p7.set_fill_color(*bg)
        p7.draw_rect(45, cur_ry, p7.cw, 17, fill=True)
        p7.set_fill_color(0.10, 0.15, 0.25)
        p7.draw_text(area, 55, cur_ry + 5, font="F2", size=7.5)
        p7.draw_text(c_role, 260, cur_ry + 5, font="F1", size=7.5)
        p7.draw_text(m_role, 335, cur_ry + 5, font="F1", size=7.5)
        p7.draw_text(s_role, 445, cur_ry + 5, font="F1", size=7.5)
        cur_ry -= 17

    # Escalation & Conflict Resolution Box
    p7.set_fill_color(0.96, 0.96, 0.98)
    p7.set_stroke_color(0.40, 0.50, 0.65)
    p7.draw_rect(45, 120, p7.cw, 75, fill=True, stroke=True, stroke_w=1.0)
    p7.set_fill_color(0.15, 0.25, 0.45)
    p7.draw_text("CONFLICT RESOLUTION & ESCALATION PROTOCOL", 60, 175, font="F2", size=9.5)
    esc_text = (
        "1. Client At-Risk Escalation: Managing Partner must engage at-risk accounts within 2 hours. If unresolved "
        "within 48 hours, CEO joins an executive alignment call to protect the commercial relationship.\n"
        "2. Executive Disagreements: Internal operational, delivery, and staffing disputes defer to the Managing Partner. "
        "International expansion, strategic positioning, and corporate capital allocations defer to the CEO."
    )
    p7.draw_wrapped_text(esc_text, 60, 158, p7.cw - 30, font="F1", size=8.0, leading=11.5)

    # -------------------------------------------------------------
    # PAGE 8: PRO FORMA FINANCIAL MODEL & ENTERPRISE VALUATION
    # -------------------------------------------------------------
    p8 = doc.add_page()
    p8.set_fill_color(0.06, 0.09, 0.16)
    p8.draw_text("7. 3-YEAR PRO FORMA FINANCIAL MODEL & ENTERPRISE VALUATION", 45, 785, font="F2", size=15)
    p8.set_stroke_color(0.85, 0.55, 0.13)
    p8.draw_line(45, 775, p8.width - 45, 775, stroke_w=1.5)
    
    p8.set_fill_color(0.15, 0.20, 0.28)
    intro_p8 = (
        "The following financial statement outlines the consolidated pro forma income statement for Fairytales SMM "
        "from Year 1 launch through Year 3 pan-European expansion, detailing revenue streams, direct delivery COGS, "
        "personnel overhead, and net EBITDA operating profit."
    )
    p8.draw_wrapped_text(intro_p8, 45, 755, p8.cw, font="F1", size=9.5, leading=14.0)
    
    # Financial Statement Table
    fin_y = 705
    p8.set_fill_color(0.06, 0.09, 0.16)
    p8.draw_rect(45, fin_y, p8.cw, 22, fill=True)
    p8.set_fill_color(1.0, 1.0, 1.0)
    p8.draw_text("FINANCIAL LINE ITEM", 55, fin_y + 7, font="F2", size=8.5)
    p8.draw_text("YEAR 1 (UK BASE)", 200, fin_y + 7, font="F2", size=8.5)
    p8.draw_text("YEAR 2 (+ DACH)", 310, fin_y + 7, font="F2", size=8.5)
    p8.draw_text("YEAR 3 (PAN-EUROPE)", 420, fin_y + 7, font="F2", size=8.5)
    
    fin_data = [
        ("Active Client Retainers", "18 - 25 Accounts", "45 Accounts", "75+ Enterprise Accounts"),
        ("Average Monthly Revenue Run-Rate", "175,000 / mo", "533,000 / mo", "1,266,000 / mo"),
        ("GROSS REVENUE", "2,100,000", "6,400,000", "15,200,000"),
        ("Creator Payouts & Seeding Samples", "520,000 (24.8%)", "1,600,000 (25.0%)", "3,800,000 (25.0%)"),
        ("Video Editing & Creative Production", "380,000 (18.1%)", "1,150,000 (18.0%)", "2,700,000 (17.8%)"),
        ("Software Tools (Modash, Motion, Frame)", "65,000 (3.1%)", "190,000 (3.0%)", "450,000 (3.0%)"),
        ("TOTAL DIRECT DELIVERY COGS", "965,000 (46.0%)", "2,940,000 (45.9%)", "6,950,000 (45.7%)"),
        ("GROSS PROFIT", "1,135,000 (54.0%)", "3,460,000 (54.1%)", "8,250,000 (54.3%)"),
        ("Personnel & Regional Hub Overhead", "480,000 (22.9%)", "1,450,000 (22.7%)", "3,200,000 (21.1%)"),
        ("Sales, Marketing & Acquisition (CAC)", "150,000 (7.1%)", "420,000 (6.6%)", "950,000 (6.3%)"),
        ("EBITDA (NET OPERATING PROFIT)", "505,000 (24.0%)", "1,590,000 (24.8%)", "4,100,000 (27.0%)")
    ]
    
    cur_fy = fin_y - 18
    for i, (item, y1, y2, y3) in enumerate(fin_data):
        is_highlight = "REVENUE" in item or "PROFIT" in item or "EBITDA" in item
        if is_highlight:
            bg = (0.92, 0.95, 0.99)
            font_use = "F2"
        else:
            bg = (0.98, 0.98, 0.99) if (i % 2 == 0) else (1.0, 1.0, 1.0)
            font_use = "F1"
            
        p8.set_fill_color(*bg)
        p8.draw_rect(45, cur_fy, p8.cw, 18, fill=True)
        p8.set_fill_color(0.10, 0.15, 0.25)
        p8.draw_text(item, 55, cur_fy + 5, font=font_use, size=7.8)
        p8.draw_text(y1, 200, cur_fy + 5, font=font_use, size=7.8)
        p8.draw_text(y2, 310, cur_fy + 5, font=font_use, size=7.8)
        p8.draw_text(y3, 420, cur_fy + 5, font=font_use, size=7.8)
        cur_fy -= 18
        
    # Enterprise Valuation Summary Box
    p8.set_fill_color(0.96, 0.98, 0.95)
    p8.set_stroke_color(0.85, 0.55, 0.13)
    p8.draw_rect(45, cur_fy - 75, p8.cw, 80, fill=True, stroke=True, stroke_w=1.2)
    p8.set_fill_color(0.70, 0.40, 0.05)
    p8.draw_text("ENTERPRISE VALUATION & EXIT MULTIPLE ANALYSIS", 60, cur_fy - 12, font="F2", size=9.5)
    
    val_text = (
        "At Year 3 scale (15.2M ARR with 4.1M EBITDA across the UK, Germany, and France), next-generation social "
        "commerce and creator agencies command enterprise multiples of 8x to 12x EBITDA, or 2.5x to 3.5x ARR.\n"
        "• Projected Enterprise Valuation: 32.8M to 49.2M.\n"
        "• Strategic Buyer Targets: Global advertising conglomerates (WPP, Publicis, Omnicom) or major private "
        "equity consolidators acquiring creator-led commerce engines."
    )
    p8.draw_wrapped_text(val_text, 60, cur_fy - 28, p8.cw - 30, font="F1", size=8.2, leading=11.5)

    # Formal Board Sign-Off
    p8.set_fill_color(0.06, 0.09, 0.16)
    p8.draw_text("OFFICIAL BOARDROOM AUTHORIZATION & SIGN-OFF", 45, 130, font="F2", size=10)
    
    sign_y = 60
    p8.set_fill_color(0.96, 0.97, 0.99)
    p8.set_stroke_color(0.75, 0.80, 0.88)
    p8.draw_rect(45, sign_y, p8.cw, 55, fill=True, stroke=True, stroke_w=0.8)
    
    p8.set_fill_color(0.15, 0.20, 0.30)
    p8.draw_text("CHIEF EXECUTIVE OFFICER (CEO)", 60, sign_y + 38, font="F2", size=8.5)
    p8.draw_text("Signature: __________________________________", 60, sign_y + 20, font="F1", size=8.0)
    p8.draw_text("Date: ______________", 60, sign_y + 7, font="F1", size=8.0)
    
    p8.draw_text("MANAGING PARTNER", 310, sign_y + 38, font="F2", size=8.5)
    p8.draw_text("Signature: __________________________________", 310, sign_y + 20, font="F1", size=8.0)
    p8.draw_text("Date: ______________", 310, sign_y + 7, font="F1", size=8.0)

    # Save
    doc.save()

if __name__ == "__main__":
    create_all_in_one_business_plan()
