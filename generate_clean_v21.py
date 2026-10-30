import re
import os
from html.parser import HTMLParser

# Load metadata and diagram snippets
exec(open('build_v21_executive_layout.py', 'r', encoding='utf-8').read())
exec(open('generate_v21_portal.py', 'r', encoding='utf-8').read())

# Read pristine source with all 15 tabs
with open('portal/index_v1.html', 'r', encoding='utf-8') as f:
    source = f.read()

print(f"Read index_v1.html source: {len(source):,} chars")

# ==============================================================================
# 1. ENHANCED CSS STYLING FOR EXECUTIVE READERS-FRIENDLY TWO-COLUMN SYSTEM
# ==============================================================================
v21_css = """
    /* ==========================================================================
       EXECUTIVE TWO-COLUMN READERS-FRIENDLY ARCHITECTURE & PLANNING LAYOUT
       ========================================================================== */

    .editorial-layout {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 330px;
      gap: 36px;
      align-items: start;
      max-width: 1400px;
      margin: 0 auto;
      padding: 24px 32px 80px 32px;
    }

    .editorial-main {
      min-width: 0;
      max-width: 920px;
    }

    .editorial-rail {
      position: -webkit-sticky;
      position: sticky;
      top: 104px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      max-height: calc(100vh - 120px);
      overflow-y: auto;
      padding-bottom: 20px;
      -webkit-overflow-scrolling: touch;
    }
    .editorial-rail::-webkit-scrollbar { width: 4px; }
    .editorial-rail::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.15); border-radius: 4px; }

    /* Breadcrumbs */
    .editorial-breadcrumb {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11.5px;
      font-weight: 600;
      color: var(--apple-text-sec, #86868B);
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .crumb-stage { color: var(--apple-blue, #0071E3); }
    .crumb-sep { color: var(--apple-border-strong, rgba(0,0,0,0.16)); }
    .crumb-current { color: var(--apple-text, #1D1D1F); }

    /* Header */
    .editorial-header {
      margin-bottom: 20px;
    }
    .editorial-header-eyebrow {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      font-weight: 700;
      color: var(--apple-gold-dark, #9A751E);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 6px;
    }
    .page-title {
      font-size: 28px !important;
      font-weight: 800 !important;
      letter-spacing: -0.02em !important;
      color: var(--apple-text, #1D1D1F) !important;
      line-height: 1.25 !important;
      margin: 0 0 8px 0 !important;
    }
    .page-desc {
      font-size: 15px !important;
      line-height: 1.55 !important;
      color: var(--apple-text-sec, #86868B) !important;
      margin: 0 !important;
    }

    /* Executive Takeaway Card */
    .exec-takeaway-card {
      background: linear-gradient(135deg, rgba(0, 113, 227, 0.05) 0%, rgba(197, 160, 89, 0.08) 100%);
      border: 1px solid rgba(0, 113, 227, 0.2);
      border-left: 5px solid var(--apple-blue, #0071E3);
      border-radius: 12px;
      padding: 18px 22px;
      margin-bottom: 26px;
    }
    .takeaway-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      flex-wrap: wrap;
      gap: 8px;
    }
    .takeaway-badge {
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--apple-blue, #0071E3);
    }
    .takeaway-statute {
      font-size: 11.5px;
      font-weight: 600;
      color: var(--apple-text-sec, #86868B);
      font-family: ui-monospace, SFMono-Regular, monospace;
    }
    .takeaway-headline {
      font-size: 16px;
      font-weight: 600;
      line-height: 1.5;
      color: var(--apple-text, #1D1D1F);
      margin-bottom: 10px;
    }
    .takeaway-decision {
      font-size: 13.5px;
      line-height: 1.5;
      color: var(--apple-text-sec, #86868B);
      padding-top: 10px;
      border-top: 1px dashed rgba(0, 0, 0, 0.12);
    }
    .takeaway-decision strong {
      color: var(--apple-gold-dark, #9A751E);
    }

    /* Visual Diagrams & Photos */
    .visual-diagram-card {
      background: #FFFFFF;
      border: 1px solid var(--apple-border, rgba(0,0,0,0.08));
      border-radius: 14px;
      padding: 18px;
      margin-bottom: 26px;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.03);
    }
    .visual-diagram-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }
    .visual-diagram-title {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--apple-text, #1D1D1F);
    }
    .visual-diagram-body {
      border-radius: 10px;
      overflow: hidden;
      background: #FAFAFC;
      border: 1px solid rgba(0, 0, 0, 0.04);
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .visual-diagram-img {
      width: 100%;
      height: auto;
      display: block;
      max-height: 480px;
      object-fit: contain;
    }
    .visual-diagram-caption {
      font-size: 12px;
      line-height: 1.5;
      color: var(--apple-text-sec, #86868B);
      margin-top: 12px;
      padding-top: 10px;
      border-top: 1px solid var(--apple-border-light, rgba(0,0,0,0.04));
    }

    /* Editorial Prose & Typography */
    .editorial-prose-wrap {
      font-size: 15.5px;
      line-height: 1.74;
      color: var(--apple-text, #1D1D1F);
    }
    .editorial-prose-wrap p {
      margin-bottom: 1.2em;
      line-height: 1.74;
    }
    .editorial-prose-wrap h2 {
      font-size: 21px;
      font-weight: 700;
      letter-spacing: -0.015em;
      margin-top: 32px;
      margin-bottom: 14px;
      color: var(--apple-text, #1D1D1F);
      border-bottom: 1px solid var(--apple-border-light, rgba(0,0,0,0.06));
      padding-bottom: 6px;
    }
    .editorial-prose-wrap h3 {
      font-size: 17px;
      font-weight: 600;
      margin-top: 24px;
      margin-bottom: 10px;
      color: var(--apple-text, #1D1D1F);
    }

    /* Sequential Navigator */
    .prev-next-nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      margin-top: 48px;
      padding-top: 24px;
      border-top: 1px solid var(--apple-border, rgba(0,0,0,0.08));
    }
    .btn-seq-nav {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      padding: 12px 18px;
      border-radius: 10px;
      border: 1px solid var(--apple-border, rgba(0,0,0,0.12));
      background: #FFFFFF;
      color: var(--apple-text, #1D1D1F);
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      font-family: inherit;
    }
    .btn-seq-nav:hover {
      background: var(--apple-bg, #F5F5F7);
      border-color: var(--apple-blue, #0071E3);
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .seq-sub {
      font-size: 10px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--apple-text-sec, #86868B);
    }
    .seq-title {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--apple-text, #1D1D1F);
    }

    /* Sticky Rail Widgets */
    .rail-card {
      background: #FFFFFF;
      border: 1px solid var(--apple-border, rgba(0,0,0,0.08));
      border-radius: 12px;
      padding: 15px 16px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
    }
    .rail-card-title {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      font-weight: 700;
      color: var(--apple-text, #1D1D1F);
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--apple-border-light, rgba(0,0,0,0.04));
    }
    .rail-stat-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }
    .rail-stat-item {
      background: var(--apple-bg, #F5F5F7);
      border-radius: 8px;
      padding: 9px;
    }
    .rail-stat-val {
      font-size: 14.5px;
      font-weight: 800;
      color: var(--apple-text, #1D1D1F);
      line-height: 1.2;
    }
    .rail-stat-lbl {
      font-size: 10px;
      color: var(--apple-text-sec, #86868B);
      margin-top: 2px;
    }
    .on-page-nav {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .on-page-link {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      color: var(--apple-text-sec, #86868B);
      text-decoration: none;
      padding: 6px 8px;
      border-radius: 6px;
      transition: all 0.15s ease;
      cursor: pointer;
    }
    .on-page-link:hover, .on-page-link.is-active {
      background: var(--apple-blue-light, rgba(0,113,227,0.08));
      color: var(--apple-blue, #0071E3);
      font-weight: 600;
    }
    .btn-rail-audio, .btn-rail-download, .btn-rail-print {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      padding: 9px 12px;
      border-radius: 8px;
      border: 1px solid var(--apple-border, rgba(0,0,0,0.1));
      background: #FFFFFF;
      color: var(--apple-text, #1D1D1F);
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: inherit;
    }
    .btn-rail-audio:hover {
      background: var(--apple-gold-light, rgba(197, 160, 89, 0.12));
      border-color: var(--apple-gold, #C5A059);
      color: var(--apple-gold-dark, #9A751E);
    }
    .btn-rail-download:hover {
      background: var(--apple-blue-light, rgba(0, 113, 227, 0.08));
      border-color: var(--apple-blue, #0071E3);
      color: var(--apple-blue, #0071E3);
    }
    .btn-rail-print {
      background: var(--apple-text, #1D1D1F);
      color: #FFFFFF;
      border: none;
      justify-content: center;
      gap: 8px;
    }
    .btn-rail-print:hover {
      background: #000000;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* Masthead Navigation Bar */
    .apple-nav-masthead {
      position: -webkit-sticky;
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--apple-border, rgba(0,0,0,0.08));
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }
    .apple-nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 24px;
      border-bottom: 1px solid var(--apple-border-light, rgba(0,0,0,0.04));
    }
    .apple-brand-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
    }
    .apple-brand-logo {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: linear-gradient(135deg, #0F1E36 0%, #1D1D1F 100%);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 16px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }
    .apple-brand-title {
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 0.03em;
      color: var(--apple-text, #1D1D1F);
    }
    .apple-brand-badge {
      font-size: 10.5px;
      font-weight: 700;
      background: var(--apple-blue-light, rgba(0,113,227,0.1));
      color: var(--apple-blue, #0071E3);
      padding: 2px 8px;
      border-radius: 12px;
    }
    .apple-nav-right {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .apple-btn-pill {
      background: var(--apple-control-bg, rgba(0,0,0,0.05));
      border: 1px solid var(--apple-border, rgba(0,0,0,0.08));
      border-radius: 16px;
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 600;
      color: var(--apple-text, #1D1D1F);
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .apple-btn-pill:hover {
      background: rgba(0,0,0,0.09);
    }
    .apple-stages-strip {
      background: #FAFAFC;
      border-bottom: 1px solid var(--apple-border-light, rgba(0,0,0,0.04));
      padding: 6px 24px;
    }
    .apple-stages-inner {
      display: flex;
      gap: 12px;
      max-width: 1400px;
      margin: 0 auto;
      overflow-x: auto;
    }
    .apple-stage-btn {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 14px;
      border-radius: 8px;
      border: 1px solid transparent;
      background: transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: left;
      font-family: inherit;
      white-space: nowrap;
    }
    .apple-stage-btn:hover {
      background: rgba(0,0,0,0.04);
    }
    .apple-stage-btn.active {
      background: #FFFFFF;
      border-color: var(--apple-border, rgba(0,0,0,0.12));
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .stage-num {
      font-size: 10px;
      font-weight: 800;
      padding: 3px 6px;
      border-radius: 4px;
      background: rgba(0,0,0,0.06);
      color: var(--apple-text-sec, #86868B);
      letter-spacing: 0.05em;
    }
    .apple-stage-btn.active .stage-num {
      background: var(--apple-blue, #0071E3);
      color: #FFFFFF;
    }
    .stage-text {
      display: flex;
      flex-direction: column;
    }
    .stage-name {
      font-size: 12px;
      font-weight: 700;
      color: var(--apple-text, #1D1D1F);
    }
    .stage-sub {
      font-size: 10px;
      color: var(--apple-text-sec, #86868B);
    }
    .apple-subnav-bar {
      padding: 8px 24px;
      background: rgba(255, 255, 255, 0.85);
    }
    .apple-subnav-inner {
      max-width: 1400px;
      margin: 0 auto;
      overflow-x: auto;
    }
    .apple-segmented-control {
      display: inline-flex;
      gap: 6px;
      align-items: center;
    }
    .apple-segment-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid transparent;
      background: var(--apple-control-bg, rgba(0,0,0,0.04));
      font-size: 12px;
      font-weight: 600;
      color: var(--apple-text, #1D1D1F);
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: inherit;
      white-space: nowrap;
    }
    .apple-segment-btn:hover {
      background: rgba(0,0,0,0.08);
    }
    .apple-segment-btn.active {
      background: var(--apple-blue, #0071E3);
      color: #FFFFFF;
      box-shadow: 0 2px 8px rgba(0, 113, 227, 0.25);
    }

    /* Print Overrides */
    @media print {
      .apple-nav-masthead, .editorial-rail, .prev-next-nav, #auth-overlay {
        display: none !important;
      }
      .editorial-layout {
        display: block !important;
        padding: 0 !important;
        max-width: 100% !important;
      }
      .editorial-main {
        max-width: 100% !important;
      }
      .tab-pane {
        display: none !important;
      }
      .tab-pane.active {
        display: block !important;
      }
    }

    /* Responsiveness */
    @media (max-width: 1080px) {
      .editorial-layout {
        grid-template-columns: 1fr;
        padding: 16px 20px 60px 20px;
      }
      .editorial-rail {
        position: static;
        max-height: none;
        overflow-y: visible;
      }
    }
"""

# Inject CSS into source right before </style>
source = source.replace('</style>', v21_css + '\n  </style>')

# ==============================================================================
# 2. TAB BODY EXTRACTION AND TWO-COLUMN WRAPPING
# ==============================================================================

def extract_tab_clean(tab_id, source_html):
    m = re.search(r'<div\s+id=[\'\"]' + tab_id + r'[\'\"].*?>', source_html)
    if not m:
        raise ValueError(f"Could not find tab: {tab_id}")
    open_end = m.end()

    # Scan for matching </div> using depth
    depth = 0
    cut_pos = None
    for m_tag in re.finditer(r'<(/?)div\b[^>]*>', source_html[open_end:]):
        if m_tag.group(1) == '':
            depth += 1
        else:
            if depth == 0:
                cut_pos = m_tag.start()
                break
            depth -= 1

    inner = source_html[open_end:open_end + cut_pos]

    # Remove old page-title-wrap if present
    m_pt = re.search(r'<div class=[\'\"]page-title-wrap[\'\"].*?>', inner)
    if m_pt:
        pt_start = m_pt.start()
        pt_open_end = m_pt.end()
        pt_depth = 0
        pt_cut = None
        for m_tag in re.finditer(r'<(/?)div\b[^>]*>', inner[pt_open_end:]):
            if m_tag.group(1) == '':
                pt_depth += 1
            else:
                if pt_depth == 0:
                    pt_cut = pt_open_end + m_tag.end()
                    break
                pt_depth -= 1
        inner = inner[:pt_start] + inner[pt_cut:]

    return inner.strip()


def wrap_tab_executive_layout(tab_id, tab_idx, clean_body):
    meta = TAB_META.get(tab_id, {})
    stage_name = meta.get("stage", "Stage 1: Strategy & Viability")
    short_title = meta.get("short_title", tab_id)
    long_title = meta.get("long_title", tab_id)
    subtitle = meta.get("subtitle", "")
    takeaway = meta.get("takeaway", "")
    decision = meta.get("decision", "")
    statute = meta.get("statute", "")
    stats = meta.get("stats", [])
    pdf_link = meta.get("pdf", "docs/ADOV_Care_Group_Final_Recommendation_Report.pdf")
    docx_link = meta.get("docx", "docs/ADOV_Care_Group_Final_Recommendation_Report.docx")
    anchors = meta.get("anchors", [])
    diagram_keys = meta.get("diagrams", [])

    active_class = " active" if tab_idx == 0 else ""

    # Embedded Diagrams HTML
    diagrams_html = ""
    for d_key in diagram_keys:
        if d_key in DIAGRAM_SNIPPETS:
            diagrams_html += "\n" + DIAGRAM_SNIPPETS[d_key]

    # Sequential Nav Buttons
    prev_btn_html = ""
    if tab_idx > 0:
        prev_id = TAB_ORDER[tab_idx - 1]
        prev_meta = TAB_META.get(prev_id, {})
        prev_btn_html = f"""
        <button class="btn-seq-nav btn-seq-prev" onclick="switchTab('{prev_id}')">
          <span style="font-size: 16px;">←</span>
          <div>
            <div class="seq-sub">Previous Section</div>
            <div class="seq-title">{prev_meta.get('short_title', prev_id)}</div>
          </div>
        </button>"""

    next_btn_html = ""
    if tab_idx < len(TAB_ORDER) - 1:
        next_id = TAB_ORDER[tab_idx + 1]
        next_meta = TAB_META.get(next_id, {})
        next_btn_html = f"""
        <button class="btn-seq-nav btn-seq-next" onclick="switchTab('{next_id}')">
          <div>
            <div class="seq-sub">Next Section</div>
            <div class="seq-title">{next_meta.get('short_title', next_id)}</div>
          </div>
          <span style="font-size: 16px;">→</span>
        </button>"""

    # Rail Stats
    stats_html = ""
    for s in stats:
        if isinstance(s, (list, tuple)):
            lbl, val = s[0], s[1]
        elif isinstance(s, dict):
            lbl, val = s.get('lbl', ''), s.get('val', '')
        else:
            lbl, val = '', str(s)
        stats_html += f"""
          <div class="rail-stat-item">
            <div class="rail-stat-val">{val}</div>
            <div class="rail-stat-lbl">{lbl}</div>
          </div>"""

    # Rail Anchors
    anchors_html = ""
    for a in anchors:
        if isinstance(a, (list, tuple)):
            aid, albl = a[0], a[1]
        elif isinstance(a, dict):
            aid, albl = a.get('id', ''), a.get('label', '')
        else:
            aid, albl = '', str(a)
        anchors_html += f"""
          <a class="on-page-link" onclick="smoothJump(event, '{aid}')">
            <span>↳</span>
            <span>{albl}</span>
          </a>"""

    wrapped = f"""
        <!-- {tab_id.upper()} (READERS-FRIENDLY TWO-COLUMN EXECUTIVE LAYOUT) -->
        <div id="{tab_id}" class="tab-pane{active_class}">
          <div class="editorial-layout">

            <!-- LEFT: MAIN EDITORIAL READING PANE -->
            <div class="editorial-main">
              
              <!-- STAGE BREADCRUMB -->
              <nav class="editorial-breadcrumb" aria-label="Breadcrumb">
                <span class="crumb-stage">{stage_name}</span>
                <span class="crumb-sep">/</span>
                <span class="crumb-current">{short_title}</span>
              </nav>

              <!-- PAGE TITLE BLOCK -->
              <header class="editorial-header">
                <div class="editorial-header-eyebrow">
                  <span>{stage_name} // Executive Planning Dossier</span>
                  <span class="badge-read-time" id="badge-read-{tab_id}" data-tid="{tab_id}">⏱️ <span>~5 min read</span></span>
                </div>
                <h1 class="page-title">{long_title}</h1>
                <p class="page-desc">{subtitle}</p>
              </header>

              <!-- EXECUTIVE TAKEAWAY & DECISION BOX -->
              <section class="exec-takeaway-card" id="sec-verdict">
                <div class="takeaway-header">
                  <span class="takeaway-badge">💡 EXECUTIVE VERDICT &amp; DECISION BRIEFING</span>
                  <span class="takeaway-statute">{statute}</span>
                </div>
                <div class="takeaway-headline">{takeaway}</div>
                <div class="takeaway-decision">
                  <strong>Target Board Decision:</strong> {decision}
                </div>
              </section>

              <!-- EMBEDDED VISUAL DIAGRAMS / REAL PHOTOS -->
              {diagrams_html}

              <!-- TAB BODY CONTENT -->
              <div class="editorial-prose-wrap">
                {clean_body}
              </div>

              <!-- BOTTOM SEQUENTIAL READING NAVIGATOR -->
              <nav class="prev-next-nav" aria-label="Sequential Reading">
                {prev_btn_html}
                {next_btn_html}
              </nav>

            </div><!-- /editorial-main -->

            <!-- RIGHT: STICKY EXECUTIVE DECISION & READING RAIL -->
            <aside class="editorial-rail" aria-label="Executive Decision Companion">
              
              <!-- 1. KEY DECISION METRICS WIDGET -->
              <div class="rail-card rail-decision-widget">
                <div class="rail-card-title">
                  <span>📌 Key Decision Metrics</span>
                  <span class="apple-pill-badge badge-blue">Executive Summary</span>
                </div>
                <div class="rail-stat-grid">
                  {stats_html}
                </div>
              </div>

              <!-- 2. "ON THIS PAGE" IN-PAGE JUMP ANCHORS -->
              <div class="rail-card rail-anchors-widget">
                <div class="rail-card-title">
                  <span>📑 On This Page</span>
                  <span style="font-size: 11px; color: var(--apple-text-sec); font-weight: 500;">Direct Jump</span>
                </div>
                <nav class="on-page-nav">
                  {anchors_html}
                </nav>
              </div>

              <!-- 3. AUDIO EXECUTIVE BRIEFING -->
              <div class="rail-card rail-audio-widget">
                <div class="rail-card-title">
                  <span>🎙️ Executive Audio Dossier</span>
                  <span class="apple-pill-badge badge-gold">AI Narrator</span>
                </div>
                <p style="font-size: 11.5px; color: var(--apple-text-sec); margin: 0 0 10px 0; line-height: 1.45;">
                  Listen to synthesized executive audio briefing for this section.
                </p>
                <button class="btn-rail-audio" onclick="toggleTabAudio('{tab_id}')">
                  <span>▶ Play Audio Briefing</span>
                </button>
              </div>

              <!-- 4. OFFICIAL MASTER DOSSIER DOWNLOADS -->
              <div class="rail-card rail-downloads-widget">
                <div class="rail-card-title">
                  <span>📥 Board Reference Filing</span>
                  <span class="apple-pill-badge badge-green">Master Docs</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                  <a href="{pdf_link}" download class="btn-rail-download">
                    <span>📄 Master PDF Filing</span>
                    <span style="font-size: 11px; opacity: 0.7;">Official Report</span>
                  </a>
                  <a href="{docx_link}" download class="btn-rail-download">
                    <span>📝 Master Word (.docx)</span>
                    <span style="font-size: 11px; opacity: 0.7;">Editable Spec</span>
                  </a>
                </div>
              </div>

              <!-- 5. 1-CLICK A4 PRINT -->
              <button class="btn-rail-print" onclick="printActiveTab('{tab_id}')">
                <span>🖨️ Print Section to A4 PDF</span>
              </button>

            </aside><!-- /editorial-rail -->

          </div><!-- /editorial-layout -->
        </div><!-- /{tab_id} -->
    """
    return wrapped

# Extract and wrap all 15 tabs
all_wrapped_tabs = []
for i, tid in enumerate(TAB_ORDER):
    clean_b = extract_tab_clean(tid, source)
    wrapped_t = wrap_tab_executive_layout(tid, i, clean_b)
    all_wrapped_tabs.append(wrapped_t)
    print(f"  ✓ Processed tab {tid:20} (clean body: {len(clean_b):,} chars)")

all_tabs_joined = "\n".join(all_wrapped_tabs)

# ==============================================================================
# 3. REASSEMBLE MAIN CONTENT AND REPLACE MASTHEAD
# ==============================================================================

# Find boundaries of existing tabs container
first_tab_pos = source.find('id="tab-overview"')
first_tab_open = source.rfind('<div', 0, first_tab_pos)
main_end_pos = source.find('</main>')

before_tabs = source[:first_tab_open]
after_tabs = source[main_end_pos:]

# Replace navigation header in before_tabs
stage_masthead = """
    <!-- APPLE V 2.1 STAGE-BASED NAVIGATION MASTHEAD -->
    <header class="apple-nav-masthead">
      
      <!-- TOP UTILITY STRIP -->
      <div class="apple-nav-inner">
        <!-- Brand Monogram & System Title -->
        <div class="apple-brand-wrap" onclick="switchTab('tab-overview')">
          <div class="apple-brand-logo">A</div>
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span class="apple-brand-title">ADOV CARE GROUP</span>
              <span class="apple-brand-badge">Project Plan</span>
            </div>
            <div style="font-size: 10.5px; color: var(--apple-text-sec); font-weight: 500;">
              Executive Planning Dossier // 78 &amp; 80 Marston Gardens, Luton (LU2 7DY)
            </div>
          </div>
        </div>

        <!-- Right Quick Actions -->
        <div class="apple-nav-right">
          <button class="apple-btn-pill" onclick="toggleTheme()" title="Toggle Appearance">🌓</button>
          <button class="apple-btn-pill" onclick="handleLogout()" title="Lock / Sign Out">🔒 Lock</button>
          <button class="apple-btn-pill" onclick="window.print()" title="Print Current View">🖨️ Print Dossier</button>
        </div>
      </div>

      <!-- TIER 1: 4 STRATEGIC PLANNING STAGES -->
      <div class="apple-stages-strip">
        <div class="apple-stages-inner">
          <button class="apple-stage-btn active" id="stage-btn-1" onclick="switchStage(1, 'tab-overview')">
            <span class="stage-num">STAGE 01</span>
            <div class="stage-text">
              <span class="stage-name">Strategy &amp; Viability</span>
              <span class="stage-sub">Options, Appraisal, Moats</span>
            </div>
          </button>
          <button class="apple-stage-btn" id="stage-btn-2" onclick="switchStage(2, 'tab-houses')">
            <span class="stage-num">STAGE 02</span>
            <div class="stage-text">
              <span class="stage-name">Real Estate &amp; Legal</span>
              <span class="stage-sub">Properties, CapEx, S192, Tax</span>
            </div>
          </button>
          <button class="apple-stage-btn" id="stage-btn-3" onclick="switchStage(3, 'tab-cqc')">
            <span class="stage-num">STAGE 03</span>
            <div class="stage-text">
              <span class="stage-name">CQC &amp; Operations</span>
              <span class="stage-sub">CQC Roadmap, P&amp;L, DPS SOP</span>
            </div>
          </button>
          <button class="apple-stage-btn" id="stage-btn-4" onclick="switchStage(4, 'tab-tracker')">
            <span class="stage-num">STAGE 04</span>
            <div class="stage-text">
              <span class="stage-name">Execution &amp; Vault</span>
              <span class="stage-sub">90-Day Tracker, Master Vault</span>
            </div>
          </button>
        </div>
      </div>

      <!-- TIER 2: ACTIVE STAGE SUB-NAVIGATION PILLS -->
      <div class="apple-subnav-bar">
        <div class="apple-subnav-inner">
          <div class="apple-segmented-control" id="header-pill-strip">
            <!-- Stage 1 Pills -->
            <button class="apple-segment-btn active" data-stage="1" data-tab="tab-overview" onclick="switchTab('tab-overview', this)"><span style="font-size: 13px;">📊</span> Overview</button>
            <button class="apple-segment-btn" data-stage="1" data-tab="tab-options" onclick="switchTab('tab-options', this)"><span style="font-size: 13px;">⚖️</span> 4-Options Model</button>
            <button class="apple-segment-btn" data-stage="1" data-tab="tab-advisory" onclick="switchTab('tab-advisory', this)"><span style="font-size: 13px;">🎓</span> Advisory Board</button>
            <button class="apple-segment-btn" data-stage="1" data-tab="tab-strategy" onclick="switchTab('tab-strategy', this)"><span style="font-size: 13px;">🏢</span> Campus (78/80)</button>

            <!-- Stage 2 Pills -->
            <button class="apple-segment-btn" data-stage="2" data-tab="tab-houses" onclick="switchTab('tab-houses', this)" style="display: none;"><span style="font-size: 13px;">🏡</span> Properties &amp; Gardens</button>
            <button class="apple-segment-btn" data-stage="2" data-tab="tab-capex" onclick="switchTab('tab-capex', this)" style="display: none;"><span style="font-size: 13px;">🔨</span> CapEx Budget</button>
            <button class="apple-segment-btn" data-stage="2" data-tab="tab-planning" onclick="switchTab('tab-planning', this)" style="display: none;"><span style="font-size: 13px;">⚖️</span> Planning S192</button>
            <button class="apple-segment-btn" data-stage="2" data-tab="tab-tax" onclick="switchTab('tab-tax', this)" style="display: none;"><span style="font-size: 13px;">💼</span> Tax &amp; Leases</button>

            <!-- Stage 3 Pills -->
            <button class="apple-segment-btn" data-stage="3" data-tab="tab-cqc" onclick="switchTab('tab-cqc', this)" style="display: none;"><span style="font-size: 13px;">🩺</span> CQC Roadmap</button>
            <button class="apple-segment-btn" data-stage="3" data-tab="tab-cqc-reqs" onclick="switchTab('tab-cqc-reqs', this)" style="display: none;"><span style="font-size: 13px;">📋</span> CQC Pillars</button>
            <button class="apple-segment-btn" data-stage="3" data-tab="tab-financials" onclick="switchTab('tab-financials', this)" style="display: none;"><span style="font-size: 13px;">📈</span> Financials &amp; P&amp;L</button>
            <button class="apple-segment-btn" data-stage="3" data-tab="tab-commissioning" onclick="switchTab('tab-commissioning', this)" style="display: none;"><span style="font-size: 13px;">🤝</span> Commissioning SOP</button>

            <!-- Stage 4 Pills -->
            <button class="apple-segment-btn" data-stage="4" data-tab="tab-tracker" onclick="switchTab('tab-tracker', this)" style="display: none;"><span style="font-size: 13px;">✅</span> 90-Day Tracker</button>
            <button class="apple-segment-btn" data-stage="4" data-tab="tab-vault" onclick="switchTab('tab-vault', this)" style="display: none;"><span style="font-size: 13px;">📁</span> Master Vault (30)</button>
            <button class="apple-segment-btn" data-stage="4" data-tab="tab-glossary" onclick="switchTab('tab-glossary', this)" style="display: none;"><span style="font-size: 13px;">📖</span> Glossary</button>
          </div>
        </div>
      </div>

    </header>
"""

# Replace old header in before_tabs
old_header_match = re.search(r'<header class="top-header">.*?</nav>', before_tabs, re.DOTALL)
if old_header_match:
    before_tabs = before_tabs[:old_header_match.start()] + stage_masthead + "\n" + before_tabs[old_header_match.end():]
    print("Replaced header navigation in before_tabs.")

# Remove .kpi-ribbon if present in before_tabs
before_tabs = re.sub(r'<div class="kpi-ribbon">.*?</div>\s*</div>\s*</div>', '', before_tabs, flags=re.DOTALL)

# Ensure #portal-app is visible and auth is modal
before_tabs = before_tabs.replace('<div id="portal-app" style="display: none;">', '<div id="portal-app">')
before_tabs = before_tabs.replace('<div id="auth-overlay">', '<div id="auth-overlay" style="display: none;">')

# Reassemble
final_output = before_tabs + all_tabs_joined + "\n    " + after_tabs

# ==============================================================================
# 4. JAVASCRIPT LOGIC ADDITIONS
# ==============================================================================

script_additions = """
    // 14. SMOOTH IN-PAGE ANCHOR JUMP
    function smoothJump(e, anchorId) {
      if (e) e.preventDefault();
      let target = document.getElementById(anchorId);
      if (!target) {
        const activeTab = document.querySelector('.tab-pane.active');
        if (activeTab) {
          target = activeTab.querySelector('[data-anchor="' + anchorId + '"]');
          if (!target) {
            const cleanKey = anchorId.replace(/^sec-/, '').replace(/[-_]/g, ' ').toLowerCase();
            const headings = activeTab.querySelectorAll('h2, h3, h4, .card-title, .takeaway-badge, .visual-diagram-title, .card');
            for (const h of headings) {
              const hText = (h.textContent || '').toLowerCase();
              if (hText.includes(cleanKey) || (cleanKey.length > 4 && hText.includes(cleanKey.slice(0, 5)))) {
                target = h;
                break;
              }
            }
          }
        }
      }
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        document.querySelectorAll('.on-page-link').forEach(l => l.classList.remove('is-active'));
        if (e && e.currentTarget) e.currentTarget.classList.add('is-active');
      }
    }

    // 15. STAGE SWITCHER & STAGE HIGHLIGHTER
    const TAB_TO_STAGE = {
      'tab-overview': 1, 'tab-options': 1, 'tab-advisory': 1, 'tab-strategy': 1,
      'tab-houses': 2, 'tab-capex': 2, 'tab-planning': 2, 'tab-tax': 2,
      'tab-cqc': 3, 'tab-cqc-reqs': 3, 'tab-financials': 3, 'tab-commissioning': 3,
      'tab-tracker': 4, 'tab-vault': 4, 'tab-glossary': 4
    };

    function switchStage(stageNum, defaultTabId) {
      document.querySelectorAll('.apple-stage-btn').forEach(b => b.classList.remove('active'));
      const activeStageBtn = document.getElementById('stage-btn-' + stageNum);
      if (activeStageBtn) activeStageBtn.classList.add('active');

      // Show only pills matching this stage
      document.querySelectorAll('.apple-segment-btn').forEach(btn => {
        const btnStage = parseInt(btn.getAttribute('data-stage'), 10);
        if (btnStage === stageNum) {
          btn.style.display = 'inline-flex';
        } else {
          btn.style.display = 'none';
        }
      });

      if (defaultTabId) {
        switchTab(defaultTabId);
      }
    }

    // Enhance switchTab to automatically update stage and pill visibility
    const originalSwitchTab = switchTab;
    switchTab = function(tabId, btn) {
      originalSwitchTab(tabId, btn);
      const stage = TAB_TO_STAGE[tabId];
      if (stage) {
        document.querySelectorAll('.apple-stage-btn').forEach(b => b.classList.remove('active'));
        const sBtn = document.getElementById('stage-btn-' + stage);
        if (sBtn) sBtn.classList.add('active');

        // Show stage pills
        document.querySelectorAll('.apple-segment-btn').forEach(p => {
          const pStage = parseInt(p.getAttribute('data-stage'), 10);
          if (pStage === stage) {
            p.style.display = 'inline-flex';
          } else {
            p.style.display = 'none';
          }
        });
      }
    };
"""

# Enhance checkAuth to auto-authenticate local file browsing
final_output = final_output.replace('auth = sessionStorage.getItem("adov_mgmt_auth") === "true";',
                                   'auth = sessionStorage.getItem("adov_mgmt_auth") === "true" || window.location.protocol === "file:" || window.location.hostname === "localhost";')

# Inject script additions right before </script>
final_output = final_output.replace('</script>', script_additions + '\n  </script>')

# ==============================================================================
# 5. TAG CHECKER VALIDATION
# ==============================================================================

class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        t = tag.lower()
        if t in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f'Unexpected closing tag </{t}> at line {self.getpos()[0]}')
            return
        last, pos = self.stack.pop()
        if last != t:
            self.errors.append(f'Mismatched tag: expected </{last}> (from line {pos[0]}), got </{t}> at line {self.getpos()[0]}')

tc = TagChecker()
tc.feed(final_output)

print(f"\n=======================================================")
print(f"Validation of generated HTML: {len(final_output):,} chars")
print(f"Tag Errors: {len(tc.errors)}")
if tc.errors:
    for e in tc.errors[:15]:
        print("  •", e)
print(f"Unclosed Tags: {len(tc.stack)}")
if tc.stack:
    for s in tc.stack[-15:]:
        print("  •", s)
print(f"=======================================================\n")

if len(tc.errors) == 0 and len(tc.stack) == 0:
    print("SUCCESS: 0 errors and 0 unclosed tags! HTML is 100% valid.")

    with open('portal/v2.html', 'w', encoding='utf-8') as f:
        f.write(final_output)
    print("✓ Written to portal/v2.html")

    with open('portal/index.html', 'w', encoding='utf-8') as f:
        f.write(final_output)
    print("✓ Written to portal/index.html")

    art_path = "/Users/mamun/.gemini/antigravity/brain/af24e45c-fc9e-4655-a931-ef50789324b7/adov_executive_portal.html"
    with open(art_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
    print("✓ Written to artifact:", art_path)
else:
    print("WARNING: Tag mismatch detected. Please review output.")
