#!/usr/bin/env python3
"""
scripts/update_v2_minimal_header_footer_layout.py
Applies User-Requested Clean Minimalist Design to portal/v2.html:
1. Remove 'Executive Planning Dossier // 78 & 80 Marston Gardens, Luton (LU2 7DY)' from header.
2. Add high-contrast buttons for 'V1' and 'V2'.
3. Create just Home Icon for Gateway.
4. Replace heavy stacked stage/pill bars with clean minimal Dropdown Main Menu.
5. Make body webpage full width (width: 100%, max-width: 100%) and responsive to all screen sizes.
6. In footer, add comprehensive site navigation with all 15 sections across all 4 stages.
7. Remove robotic audio read options completely (rail audio widgets, floating audio player dock, audio JS).
"""

import re
import os
import sys

def update_v2():
    v2_path = "portal/v2.html"
    if not os.path.exists(v2_path):
        print(f"Error: {v2_path} not found!")
        sys.exit(1)

    with open(v2_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Original portal/v2.html size: {len(content):,} bytes, {content.count(chr(10))} lines.")

    # -------------------------------------------------------------------------
    # 1. REMOVE ROBOTIC AUDIO READ OPTIONS
    # -------------------------------------------------------------------------
    # Remove all 15 <div class="rail-card rail-audio-widget">...</div> blocks
    audio_widget_pattern = re.compile(
        r'<!--\s*3\.\s*AUDIO EXECUTIVE BRIEFING\s*-->\s*<div class="rail-card rail-audio-widget">.*?</div>\s*</div>',
        re.DOTALL
    )
    # Also handle standard div closure
    audio_widget_pattern_fallback = re.compile(
        r'<div class="rail-card rail-audio-widget">.*?</div>',
        re.DOTALL
    )
    
    # Let's count and remove rail audio widgets
    matches = list(re.finditer(r'<div class="rail-card rail-audio-widget">.*?</div>', content, re.DOTALL))
    print(f"Found {len(matches)} rail-audio-widget blocks.")
    
    # Precision removal of each rail audio widget block including its comment
    content = re.sub(
        r'\s*<!--\s*3\.\s*AUDIO EXECUTIVE BRIEFING\s*-->\s*<div class="rail-card rail-audio-widget">.*?</div>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'\s*<div class="rail-card rail-audio-widget">.*?</div>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )

    # Remove the bottom dock: <div id="executive-audio-player" ...>...</div>
    content = re.sub(
        r'\s*<!--\s*EXECUTIVE MALE AUDIO BRIEFING PLAYER DOCK\s*-->\s*<div id="executive-audio-player".*?</div>\s*</div>\s*</div>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'\s*<div id="executive-audio-player".*?</div>\s*</div>\s*</div>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )

    # Remove listen audio button on tab headers if any
    content = re.sub(
        r'<button class="btn-audio-listen".*?</button>',
        '',
        content,
        flags=re.DOTALL
    )

    # -------------------------------------------------------------------------
    # 2. FULL-WIDTH BODY WEBPAGE & RESPONSIVE LAYOUT
    # -------------------------------------------------------------------------
    # Replace the 1060px constraint with 100% full-width fluid layout
    old_layout_css = """/* =========================================================================
   1-COLUMN ACADEMIC RESEARCH JOURNAL ARCHITECTURE & ENHANCED TYPOGRAPHY
   ========================================================================= */
.editorial-layout {
  display: block !important;
  max-width: 1060px !important;
  margin: 0 auto !important;
  padding: 36px 32px 100px 32px !important;
}"""

    new_layout_css = """/* =========================================================================
   FULL-WIDTH RESPONSIVE EDITORIAL ARCHITECTURE & ENHANCED TYPOGRAPHY
   ========================================================================= */
.editorial-layout {
  display: block !important;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 28px 48px 100px 48px !important;
  box-sizing: border-box !important;
}

@media (max-width: 1200px) {
  .editorial-layout {
    padding: 24px 28px 80px 28px !important;
  }
}

@media (max-width: 768px) {
  .editorial-layout {
    padding: 16px 16px 60px 16px !important;
  }
}"""

    if old_layout_css in content:
        content = content.replace(old_layout_css, new_layout_css)
        print("✓ Replaced 1060px constraint with 100% full-width layout CSS.")
    else:
        # Fallback regex replacement
        content = re.sub(
            r'\.editorial-layout\s*\{\s*display:\s*block\s*!important;\s*max-width:\s*1060px\s*!important;.*?\}',
            new_layout_css,
            content,
            flags=re.DOTALL
        )
        print("✓ Applied full-width layout via regex.")

    # Also update the original .editorial-layout rule at line ~1916
    content = re.sub(
        r'\.editorial-layout\s*\{\s*display:\s*grid;\s*grid-template-columns:\s*minmax\(0,\s*1fr\)\s*330px;\s*gap:\s*36px;\s*align-items:\s*start;\s*max-width:\s*1400px;.*?\}',
        """.editorial-layout {
  width: 100%;
  max-width: 100%;
  margin: 0;
  padding: 28px 48px 100px 48px;
  box-sizing: border-box;
}""",
        content,
        flags=re.DOTALL
    )

    content = re.sub(
        r'\.editorial-main\s*\{\s*min-width:\s*0;\s*max-width:\s*920px;\s*\}',
        '.editorial-main { min-width: 0; width: 100%; max-width: 100%; }',
        content
    )

    # -------------------------------------------------------------------------
    # 3. REDESIGN HEADER MASTHEAD (CLEAN, MINIMAL, DROPDOWN, V1/V2, HOME ICON)
    # -------------------------------------------------------------------------
    # Target the header block from <header class="apple-nav-masthead"> to </header>
    old_header_pattern = re.compile(
        r'<header class="apple-nav-masthead">.*?</header>',
        re.DOTALL
    )

    new_header_html = """<header class="apple-nav-masthead" style="position:sticky; top:0; z-index:10000; background:rgba(255,255,255,0.96); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); border-bottom:1px solid #E2E8F0; box-shadow:0 1px 4px rgba(0,0,0,0.03);">
      
      <!-- MINIMAL EXECUTIVE UTILITY STRIP -->
      <div class="apple-nav-inner" style="display:flex; align-items:center; justify-content:space-between; padding:10px 36px; width:100%; max-width:100%; box-sizing:border-box;">
        
        <!-- Left: Brand Logo & Minimal Dropdown Menu -->
        <div style="display:flex; align-items:center; gap:16px;">
          
          <!-- Brand Logo & Name (Removed secondary subheader text) -->
          <div class="apple-brand-wrap" onclick="switchTab('tab-overview')" style="cursor:pointer; display:flex; align-items:center; gap:10px;" title="ADOV Care Group — Executive Overview">
            <div class="apple-brand-logo" style="width:32px; height:32px; border-radius:8px; background:linear-gradient(135deg, #0F2440 0%, #1E3A5F 100%); color:#FFFFFF; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:16px; box-shadow:0 2px 6px rgba(15,36,64,0.15);">A</div>
            <div style="display:flex; align-items:center; gap:8px;">
              <span class="apple-brand-title" style="font-size:14px; font-weight:800; letter-spacing:0.03em; color:#0F2440;">ADOV CARE GROUP</span>
              <span class="apple-brand-badge" style="font-size:10.5px; font-weight:700; background:rgba(194,155,56,0.12); color:#C29B38; padding:2px 8px; border-radius:12px; border:1px solid rgba(194,155,56,0.3);">Project Plan</span>
            </div>
          </div>

          <!-- Vertical Divider -->
          <div style="width:1px; height:22px; background:#E2E8F0;"></div>

          <!-- DROPDOWN MAIN MENU -->
          <div class="nav-dropdown-wrapper" style="position:relative;">
            <button class="btn-main-dropdown" id="btnMainDropdown" onclick="toggleMainMenu(event)" aria-haspopup="true" aria-expanded="false" style="display:inline-flex; align-items:center; gap:7px; padding:6px 14px; background:#F8FAFC; border:1.5px solid #CBD5E1; border-radius:8px; font-size:13px; font-weight:700; color:#0F2440; cursor:pointer; transition:all 0.2s;">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
              <span>Sections Menu</span>
              <svg id="menuChevron" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>

            <!-- Dropdown Flyout Panel (4 Clean Columns) -->
            <div class="menu-dropdown-flyout" id="menuDropdownFlyout" style="display:none; position:absolute; top:calc(100% + 8px); left:0; width:820px; max-width:94vw; background:#FFFFFF; border:1.5px solid #CBD5E1; border-radius:14px; box-shadow:0 24px 50px -10px rgba(15,36,64,0.2); padding:24px; z-index:99999;">
              <div class="dropdown-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:18px;">
                
                <!-- Stage 1 -->
                <div class="dropdown-stage-col">
                  <div style="margin-bottom:10px; padding-bottom:5px; border-bottom:1.5px solid #F1F5F9;">
                    <span style="display:block; font-size:9.5px; font-weight:800; color:#C29B38; text-transform:uppercase; letter-spacing:0.8px;">STAGE 01</span>
                    <span style="font-size:12px; font-weight:700; color:#0F2440;">Strategy &amp; Viability</span>
                  </div>
                  <div style="display:flex; flex-direction:column; gap:3px;">
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-overview')" class="dropdown-item">📊 Executive Overview</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-options')" class="dropdown-item">⚖️ 4-Options Appraisal</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-advisory')" class="dropdown-item">🎓 Advisory Opinions</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-strategy')" class="dropdown-item">🏢 Campus Strategy</a>
                  </div>
                </div>

                <!-- Stage 2 -->
                <div class="dropdown-stage-col">
                  <div style="margin-bottom:10px; padding-bottom:5px; border-bottom:1.5px solid #F1F5F9;">
                    <span style="display:block; font-size:9.5px; font-weight:800; color:#C29B38; text-transform:uppercase; letter-spacing:0.8px;">STAGE 02</span>
                    <span style="font-size:12px; font-weight:700; color:#0F2440;">Real Estate &amp; Law</span>
                  </div>
                  <div style="display:flex; flex-direction:column; gap:3px;">
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-houses')" class="dropdown-item">🏡 Properties &amp; Grounds</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-capex')" class="dropdown-item">🔨 CapEx Bill of Quantities</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-planning')" class="dropdown-item">⚖️ Planning S192</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-tax')" class="dropdown-item">💼 Tax-Neutral Leases &amp; BIK</a>
                  </div>
                </div>

                <!-- Stage 3 -->
                <div class="dropdown-stage-col">
                  <div style="margin-bottom:10px; padding-bottom:5px; border-bottom:1.5px solid #F1F5F9;">
                    <span style="display:block; font-size:9.5px; font-weight:800; color:#C29B38; text-transform:uppercase; letter-spacing:0.8px;">STAGE 03</span>
                    <span style="font-size:12px; font-weight:700; color:#0F2440;">CQC &amp; Financials</span>
                  </div>
                  <div style="display:flex; flex-direction:column; gap:3px;">
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-cqc')" class="dropdown-item">🩺 CQC Approval Roadmap</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-cqc-reqs')" class="dropdown-item">📋 10 Statutory Pillars</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-financials')" class="dropdown-item">📈 Forensic Financials &amp; P&amp;L</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-commissioning')" class="dropdown-item">🤝 Commissioning SOP</a>
                  </div>
                </div>

                <!-- Stage 4 -->
                <div class="dropdown-stage-col">
                  <div style="margin-bottom:10px; padding-bottom:5px; border-bottom:1.5px solid #F1F5F9;">
                    <span style="display:block; font-size:9.5px; font-weight:800; color:#C29B38; text-transform:uppercase; letter-spacing:0.8px;">STAGE 04</span>
                    <span style="font-size:12px; font-weight:700; color:#0F2440;">Execution &amp; Vault</span>
                  </div>
                  <div style="display:flex; flex-direction:column; gap:3px;">
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-tracker')" class="dropdown-item">✅ 90-Day Tracker</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-vault')" class="dropdown-item">📁 Master Vault (38)</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-glossary')" class="dropdown-item">📖 Technical Glossary</a>
                  </div>
                </div>

              </div>
            </div>
          </div>

          <!-- Active Section Indicator Badge -->
          <div class="current-section-indicator" id="currentSectionIndicator" style="display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:700; color:#0F2440; background:#F1F5F9; border:1px solid #E2E8F0; padding:5px 12px; border-radius:8px;">
            <span id="currentSectionIcon">📊</span> <span id="currentSectionTitle">Executive Overview</span>
          </div>

        </div>

        <!-- Right Quick Actions: V1 / V2 Switch, Home Icon, Theme & Print -->
        <div class="apple-nav-right" style="display:flex; align-items:center; gap:8px;">
          
          <!-- V1 and V2 Toggle Switch -->
          <div class="version-toggle-group" style="display:inline-flex; align-items:center; background:#F1F5F9; border:1px solid #E2E8F0; border-radius:8px; padding:2px;">
            <a href="v1.html" class="v-toggle-btn" title="Switch to Version 1.0 (Operations MIS Dashboard)" style="padding:4px 11px; font-size:12px; font-weight:700; color:#475467; text-decoration:none; border-radius:6px; transition:all 0.2s;">V1</a>
            <a href="v2.html" class="v-toggle-btn active" title="Currently viewing Version 2.0 (Research Dossier)" style="padding:4px 11px; font-size:12px; font-weight:800; color:#FFFFFF; background:#0F2440; text-decoration:none; border-radius:6px; box-shadow:0 1px 3px rgba(15,36,64,0.15);">V2</a>
          </div>

          <!-- Just Home Icon for Gateway -->
          <a href="../index.html" class="apple-btn-icon" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center; width:32px; height:32px; border-radius:8px; border:1px solid #E2E8F0; background:#FFFFFF; color:#0F2440; transition:all 0.2s;" title="Return to Gateway Home">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 9.5L12 3l9 6.5V20a1.5 1.5 0 0 1-1.5 1.5H4.5A1.5 1.5 0 0 1 3 20V9.5z"></path>
              <polyline points="9 21 9 12 15 12 15 21"></polyline>
            </svg>
          </a>

          <!-- Appearance Theme Switcher -->
          <button class="apple-btn-pill" onclick="toggleTheme()" title="Toggle Appearance" style="padding:5px 10px; font-size:12px; border-radius:8px; border:1px solid #E2E8F0; background:#FFFFFF; cursor:pointer;">🌓</button>
          
          <!-- Print Dossier Button -->
          <button class="apple-btn-pill" onclick="window.print()" title="Print Current View" style="display:inline-flex; align-items:center; gap:5px; padding:5px 12px; font-size:12px; font-weight:700; border-radius:8px; border:1px solid #E2E8F0; background:#FFFFFF; color:#0F2440; cursor:pointer;">🖨️ Print</button>
        </div>

      </div>

    </header>"""

    if old_header_pattern.search(content):
        content = old_header_pattern.sub(new_header_html, content)
        print("✓ Replaced header with clean minimal Dropdown Menu, V1/V2 buttons, and Home Icon.")
    else:
        print("Warning: old header pattern not matched!")

    # -------------------------------------------------------------------------
    # 4. COMPREHENSIVE MULTI-COLUMN FOOTER NAVIGATION
    # -------------------------------------------------------------------------
    old_footer_pattern = re.compile(
        r'<footer class="portal-footer">.*?</footer>',
        re.DOTALL
    )

    new_footer_html = """<footer class="portal-footer" style="background:#0F2440; color:#FFFFFF; padding:48px 40px 32px 40px; margin-top:60px; border-top:3px solid #C29B38;">
      <div style="width:100%; max-width:100%; box-sizing:border-box;">
        
        <!-- Footer Top Brand & Purpose -->
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:20px; padding-bottom:28px; border-bottom:1px solid rgba(255,255,255,0.12); margin-bottom:32px;">
          <div>
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
              <div style="width:28px; height:28px; border-radius:6px; background:#C29B38; color:#0F2440; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:15px;">A</div>
              <span style="font-size:18px; font-weight:800; letter-spacing:0.5px; color:#FFFFFF;">ADOV CARE GROUP</span>
              <span style="font-size:10px; font-weight:700; background:rgba(194,155,56,0.2); color:#C29B38; padding:2px 8px; border-radius:10px; border:1px solid rgba(194,155,56,0.4);">Project Plan</span>
            </div>
            <p style="font-size:12.5px; color:#94A3B8; max-width:620px; line-height:1.5;">
              Executive Planning Dossier &amp; Strategic Monograph for 78 &amp; 80 Marston Gardens, Luton (LU2 7DY). Specialist Supported Living Campus under Class C3(b) with Retained Executive Family Residence at 82 Marston Gardens.
            </p>
          </div>
          
          <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap;">
            <a href="v1.html" style="display:inline-flex; align-items:center; gap:6px; padding:8px 14px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-radius:8px; color:#FFFFFF; text-decoration:none; font-size:12.5px; font-weight:700; transition:all 0.2s;">
              Switch to V1.0 Dashboard &rarr;
            </a>
            <a href="../index.html" style="display:inline-flex; align-items:center; gap:6px; padding:8px 14px; background:#C29B38; border:1px solid #C29B38; border-radius:8px; color:#0F2440; text-decoration:none; font-size:12.5px; font-weight:800; transition:all 0.2s;">
              ⌂ Gateway Home
            </a>
          </div>
        </div>

        <!-- 4-Column Full Menu Section Navigation -->
        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:28px; margin-bottom:36px;">
          
          <!-- Column 1: Stage 1 -->
          <div>
            <h4 style="font-size:11px; font-weight:800; color:#C29B38; text-transform:uppercase; letter-spacing:0.8px; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px;">Stage 01: Strategy &amp; Viability</h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="javascript:void(0)" onclick="switchTab('tab-overview'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">📊 Executive Overview</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-options'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">⚖️ 4-Options Model</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-advisory'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">🎓 Advisory Board Opinions</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-strategy'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">🏢 Campus Strategy (78/80)</a></li>
            </ul>
          </div>

          <!-- Column 2: Stage 2 -->
          <div>
            <h4 style="font-size:11px; font-weight:800; color:#C29B38; text-transform:uppercase; letter-spacing:0.8px; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px;">Stage 02: Real Estate &amp; Legal</h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="javascript:void(0)" onclick="switchTab('tab-houses'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">🏡 Properties &amp; Grounds</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-capex'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">🔨 CapEx Bill of Quantities</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-planning'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">⚖️ Class C3(b) Planning S192</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-tax'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">💼 Tax-Neutral Leases &amp; BIK</a></li>
            </ul>
          </div>

          <!-- Column 3: Stage 3 -->
          <div>
            <h4 style="font-size:11px; font-weight:800; color:#C29B38; text-transform:uppercase; letter-spacing:0.8px; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px;">Stage 03: CQC &amp; Financials</h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="javascript:void(0)" onclick="switchTab('tab-cqc'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">🩺 CQC Approval Roadmap</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-cqc-reqs'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">📋 10 Statutory CQC Pillars</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-financials'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">📈 Forensic Financials &amp; P&amp;L</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-commissioning'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">🤝 Commissioning SOP</a></li>
            </ul>
          </div>

          <!-- Column 4: Stage 4 & Publications -->
          <div>
            <h4 style="font-size:11px; font-weight:800; color:#C29B38; text-transform:uppercase; letter-spacing:0.8px; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px;">Stage 04: Execution &amp; Vault</h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="javascript:void(0)" onclick="switchTab('tab-tracker'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">✅ 90-Day Execution Tracker</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-vault'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">📁 Master Document Vault (38)</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-glossary'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">📖 Technical Statutory Glossary</a></li>
              <li><a href="docs/ADOV_Care_Group_Executive_Planning_Dossier_Finance_Magazine.pdf" target="_blank" style="color:#C29B38; font-weight:700; text-decoration:none; font-size:13px; transition:all 0.2s;">📄 Master PDF Dossier (16 Pgs)</a></li>
              <li><a href="docs/ADOV_Care_Group_Executive_Planning_Dossier_Finance_Magazine.docx" download style="color:#C29B38; font-weight:700; text-decoration:none; font-size:13px; transition:all 0.2s;">📝 Master Word Monograph</a></li>
            </ul>
          </div>

        </div>

        <!-- Footer Bottom Bar -->
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; padding-top:20px; border-top:1px solid rgba(255,255,255,0.08); font-size:11.5px; color:#64748B;">
          <p style="margin:0;">
            &copy; 2026 Fairytales Group &bull; ADOV Limited &bull; ADOV Care Group Limited &bull; Project Planned by AbdullahMamun.com
          </p>
          <div style="display:flex; gap:16px; align-items:center;">
            <span>Luton, LU2 7DY</span>
            <span>&bull;</span>
            <a href="javascript:void(0)" onclick="window.scrollTo({top:0, behavior:'smooth'})" style="color:#C29B38; text-decoration:none; font-weight:700;">↑ Return to Top</a>
          </div>
        </div>

      </div>
    </footer>"""

    if old_footer_pattern.search(content):
        content = old_footer_pattern.sub(new_footer_html, content)
        print("✓ Replaced footer with comprehensive 4-stage multi-column navigation menu.")
    else:
        print("Warning: old footer pattern not matched!")

    # -------------------------------------------------------------------------
    # 5. INJECT JAVASCRIPT FOR DROPDOWN MAIN MENU & SECTION INDICATOR
    # -------------------------------------------------------------------------
    dropdown_js = """
    // =========================================================================
    // MINIMAL DROPDOWN MAIN MENU & DYNAMIC SECTION INDICATOR
    // =========================================================================
    const TAB_SECTION_INFO = {
      'tab-overview': { icon: '📊', name: 'Executive Overview' },
      'tab-options': { icon: '⚖️', name: '4-Options Appraisal' },
      'tab-advisory': { icon: '🎓', name: 'Advisory Opinions' },
      'tab-strategy': { icon: '🏢', name: 'Campus Strategy' },
      'tab-houses': { icon: '🏡', name: 'Properties & Grounds' },
      'tab-capex': { icon: '🔨', name: 'CapEx Budget' },
      'tab-planning': { icon: '⚖️', name: 'Planning S192' },
      'tab-tax': { icon: '💼', name: 'Tax & Leases' },
      'tab-cqc': { icon: '🩺', name: 'CQC Roadmap' },
      'tab-cqc-reqs': { icon: '📋', name: '10 Statutory Pillars' },
      'tab-financials': { icon: '📈', name: 'Financials & P&L' },
      'tab-commissioning': { icon: '🤝', name: 'Commissioning SOP' },
      'tab-tracker': { icon: '✅', name: '90-Day Tracker' },
      'tab-vault': { icon: '📁', name: 'Master Vault (38)' },
      'tab-glossary': { icon: '📖', name: 'Technical Glossary' }
    };

    function toggleMainMenu(e) {
      if (e) e.stopPropagation();
      const flyout = document.getElementById('menuDropdownFlyout');
      const btn = document.getElementById('btnMainDropdown');
      if (!flyout) return;
      const isOpen = flyout.style.display === 'block';
      flyout.style.display = isOpen ? 'none' : 'block';
      if (btn) btn.setAttribute('aria-expanded', !isOpen);
    }

    function switchTabAndClose(tabId) {
      switchTab(tabId);
      const flyout = document.getElementById('menuDropdownFlyout');
      const btn = document.getElementById('btnMainDropdown');
      if (flyout) flyout.style.display = 'none';
      if (btn) btn.setAttribute('aria-expanded', 'false');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Close dropdown on click outside
    document.addEventListener('click', function(e) {
      const flyout = document.getElementById('menuDropdownFlyout');
      const btn = document.getElementById('btnMainDropdown');
      if (flyout && flyout.style.display === 'block') {
        if (!flyout.contains(e.target) && !btn.contains(e.target)) {
          flyout.style.display = 'none';
          if (btn) btn.setAttribute('aria-expanded', 'false');
        }
      }
    });

    // Close on Escape
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        const flyout = document.getElementById('menuDropdownFlyout');
        const btn = document.getElementById('btnMainDropdown');
        if (flyout && flyout.style.display === 'block') {
          flyout.style.display = 'none';
          if (btn) btn.setAttribute('aria-expanded', 'false');
        }
      }
    });

    // Hook into switchTab to update current section indicator badge
    const originalSwitchTab = window.switchTab;
    window.switchTab = function(tabId, el) {
      if (typeof originalSwitchTab === 'function') {
        originalSwitchTab(tabId, el);
      } else {
        document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
        const target = document.getElementById(tabId);
        if (target) target.classList.add('active');
      }

      // Update indicator
      const iconEl = document.getElementById('currentSectionIcon');
      const titleEl = document.getElementById('currentSectionTitle');
      const info = TAB_SECTION_INFO[tabId];
      if (info) {
        if (iconEl) iconEl.textContent = info.icon;
        if (titleEl) titleEl.textContent = info.name;
      }
    };
"""

    # Inject JS before closing </script>
    if "toggleMainMenu" not in content:
        content = content.replace("</script>", f"{dropdown_js}\n</script>")
        print("✓ Injected Dropdown Navigation JavaScript.")

    # Neutralize any remaining audio calls
    content = content.replace("toggleTabAudio(", "// toggleTabAudio(")

    with open(v2_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✓ Saved updated portal/v2.html ({len(content):,} bytes, {content.count(chr(10))} lines).")

if __name__ == "__main__":
    update_v2()
