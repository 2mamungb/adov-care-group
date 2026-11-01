#!/usr/bin/env python3
"""
scripts/polish_exposed_header_and_body_margins.py

Refines portal/v2.html, portal/luton-care-market-report.html, and portal/v1.html:
1. 4 EXPOSED dropdown menus directly in the header navbar with both full and responsive short labels.
2. Smooth hover + click opening, chevron rotation, bridge pseudo-element.
3. Completely eliminates empty top gap: removes empty divs, comments, and redundant spacing.
4. Generates professional, publication-grade editorial body text margins (centered max-width: 1360px with 28px/16px padding).
5. Ensures synchronization of active stage and section indicator on every tab switch.
"""

import os
import re

def polish_v2():
    v2_path = 'portal/v2.html'
    with open(v2_path, 'r', encoding='utf-8') as f:
        v2 = f.read()

    # 1. New Clean Header with 4 Exposed Stage Dropdowns
    new_header_html = """<header class="apple-nav-masthead" id="mainHeader" style="position:sticky; top:0; z-index:10000; background:rgba(255,255,255,0.98); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); border-bottom:1.5px solid #E2E8F0; box-shadow:0 2px 10px rgba(15,36,64,0.05);">
      
      <div class="apple-nav-inner" style="display:flex; align-items:center; justify-content:space-between; padding:8px 28px; width:100%; max-width:100%; box-sizing:border-box; gap:12px; flex-wrap:nowrap;">
        
        <!-- Left: Brand Logo -->
        <div class="apple-brand-wrap" onclick="switchTab('tab-overview')" style="cursor:pointer; display:flex; align-items:center; gap:8px; flex-shrink:0;" title="ADOV Care Group — Executive Overview">
          <div class="apple-brand-logo" style="width:30px; height:30px; border-radius:7px; background:linear-gradient(135deg, #0F2440 0%, #1E3A5F 100%); color:#FFFFFF; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:15px; box-shadow:0 2px 5px rgba(15,36,64,0.18);">A</div>
          <div style="display:flex; align-items:center; gap:6px;">
            <span class="apple-brand-title" style="font-size:13.5px; font-weight:800; letter-spacing:0.02em; color:#0F2440; white-space:nowrap;">ADOV CARE GROUP</span>
            <span class="apple-brand-badge" style="font-size:9.5px; font-weight:700; background:rgba(194,155,56,0.14); color:#9A751E; padding:1px 6px; border-radius:8px; border:1px solid rgba(194,155,56,0.35);">V2.0</span>
          </div>
        </div>

        <!-- CENTER: EXPOSED DROPDOWN MENUS (ALL 4 STAGES DIRECTLY VISIBLE IN HEADER) -->
        <nav class="exposed-header-nav" id="exposedHeaderNav" aria-label="Executive Stage Navigation" style="display:flex; align-items:center; gap:6px; flex-shrink:0;">

          <!-- STAGE 1 DROPDOWN -->
          <div class="nav-stage-dropdown" id="dropdown-stage1">
            <button class="stage-nav-btn active" id="btnStage1" onclick="toggleStageDropdown('stage1', event)" aria-haspopup="true" aria-expanded="false">
              <span class="stage-full-label">📊 Stage 1: Strategy &amp; Viability</span>
              <span class="stage-short-label">📊 Stage 1</span>
              <svg class="stage-chevron" width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="stage-menu-flyout" id="flyout-stage1">
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-overview')" class="stage-item active">📊 Executive Overview</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-options')" class="stage-item">⚖️ 4-Options Appraisal</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-advisory')" class="stage-item">🎓 Advisory Opinions</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-strategy')" class="stage-item">🏢 Campus Strategy</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-market-demand')" class="stage-item" style="font-weight:700; color:#0F2440; background:rgba(194,155,56,0.12); border-left:3px solid #C29B38;">📈 Care Supply &amp; Demand Monograph</a>
              <div style="border-top:1px solid #F1F5F9; margin:4px 0;"></div>
              <a href="luton-care-market-report.html" target="_blank" class="stage-item" style="color:#C29B38; font-weight:700;">📄 Standalone Monograph ↗</a>
            </div>
          </div>

          <!-- STAGE 2 DROPDOWN -->
          <div class="nav-stage-dropdown" id="dropdown-stage2">
            <button class="stage-nav-btn" id="btnStage2" onclick="toggleStageDropdown('stage2', event)" aria-haspopup="true" aria-expanded="false">
              <span class="stage-full-label">🏡 Stage 2: Property &amp; Law</span>
              <span class="stage-short-label">🏡 Stage 2</span>
              <svg class="stage-chevron" width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="stage-menu-flyout" id="flyout-stage2">
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-houses')" class="stage-item">🏡 Properties &amp; Grounds</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-capex')" class="stage-item">🔨 CapEx Budget</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-planning')" class="stage-item">⚖️ Planning S192 (C3b)</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-tax')" class="stage-item">💼 Tax &amp; FRI Leases</a>
            </div>
          </div>

          <!-- STAGE 3 DROPDOWN -->
          <div class="nav-stage-dropdown" id="dropdown-stage3">
            <button class="stage-nav-btn" id="btnStage3" onclick="toggleStageDropdown('stage3', event)" aria-haspopup="true" aria-expanded="false">
              <span class="stage-full-label">🩺 Stage 3: CQC &amp; Financials</span>
              <span class="stage-short-label">🩺 Stage 3</span>
              <svg class="stage-chevron" width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="stage-menu-flyout" id="flyout-stage3">
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-cqc')" class="stage-item">🩺 CQC Approval Roadmap</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-cqc-reqs')" class="stage-item">📋 10 Statutory Pillars</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-financials')" class="stage-item">📈 Financials &amp; P&amp;L</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-commissioning')" class="stage-item">🤝 Commissioning SOP</a>
            </div>
          </div>

          <!-- STAGE 4 DROPDOWN -->
          <div class="nav-stage-dropdown" id="dropdown-stage4">
            <button class="stage-nav-btn" id="btnStage4" onclick="toggleStageDropdown('stage4', event)" aria-haspopup="true" aria-expanded="false">
              <span class="stage-full-label">✅ Stage 4: Execution &amp; Vault</span>
              <span class="stage-short-label">✅ Stage 4</span>
              <svg class="stage-chevron" width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="stage-menu-flyout" id="flyout-stage4" style="right:0; left:auto;">
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-tracker')" class="stage-item">✅ 90-Day Tracker</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-vault')" class="stage-item">📁 Master Vault (38)</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-glossary')" class="stage-item">📖 Technical Glossary</a>
            </div>
          </div>

        </nav>

        <!-- Right Quick Actions: Active Indicator, V1/V2, Home Icon, Theme & Print -->
        <div class="apple-nav-right" style="display:flex; align-items:center; gap:8px; flex-shrink:0;">
          
          <!-- Active Section Indicator Badge -->
          <div class="current-section-indicator" id="currentSectionIndicator" style="display:inline-flex; align-items:center; gap:5px; font-size:12px; font-weight:700; color:#0F2440; background:#F1F5F9; border:1px solid #E2E8F0; padding:4px 9px; border-radius:6px; white-space:nowrap;">
            <span id="currentSectionIcon">📊</span> <span id="currentSectionTitle">Executive Overview</span>
          </div>

          <!-- V1 and V2 Toggle Switch -->
          <div class="version-toggle-group" style="display:inline-flex; align-items:center; background:#F1F5F9; border:1px solid #E2E8F0; border-radius:6px; padding:2px;">
            <a href="v1.html" class="v-toggle-btn" title="Switch to Version 1.0 (Operations MIS Dashboard)" style="padding:3px 9px; font-size:11px; font-weight:700; color:#475467; text-decoration:none; border-radius:4px; transition:all 0.18s;">V1</a>
            <a href="v2.html" class="v-toggle-btn active" title="Currently viewing Version 2.0 (Research Dossier)" style="padding:3px 9px; font-size:11px; font-weight:800; color:#FFFFFF; background:#0F2440; text-decoration:none; border-radius:4px; box-shadow:0 1px 3px rgba(15,36,64,0.18);">V2</a>
          </div>

          <!-- Just Home Icon for Gateway -->
          <a href="index.html" class="apple-btn-icon apple-btn-home" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center; width:28px; height:28px; border-radius:6px; border:1px solid #E2E8F0; background:#FFFFFF; color:#0F2440; transition:all 0.18s;" title="Return to Gateway Home">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 9.5L12 3l9 6.5V20a1.5 1.5 0 0 1-1.5 1.5H4.5A1.5 1.5 0 0 1 3 20V9.5z"></path>
              <polyline points="9 21 9 12 15 12 15 21"></polyline>
            </svg>
          </a>

          <!-- Appearance Theme Switcher -->
          <button class="apple-btn-pill" onclick="toggleTheme()" title="Toggle Appearance" style="padding:4px 7px; font-size:11px; border-radius:6px; border:1px solid #E2E8F0; background:#FFFFFF; cursor:pointer;">🌓</button>
          
          <!-- Print Dossier Button -->
          <button class="apple-btn-pill" onclick="window.print()" title="Print Current View" style="display:inline-flex; align-items:center; gap:4px; padding:4px 9px; font-size:11.5px; font-weight:700; border-radius:6px; border:1px solid #E2E8F0; background:#FFFFFF; color:#0F2440; cursor:pointer;">🖨️ Print</button>
        </div>

      </div>

    </header>"""

    # Locate and replace old header
    old_h_start = v2.find('<header class="apple-nav-masthead"')
    old_h_end = v2.find('</header>', old_h_start) + len('</header>')
    if old_h_start != -1 and old_h_end != -1:
        v2 = v2[:old_h_start] + new_header_html + v2[old_h_end:]
        print("✓ Replaced <header class='apple-nav-masthead'> with refined exposed navbar.")

    # 2. Clean up any leftover empty lines or comments between </header> and <div class="portal-container">
    v2 = re.sub(
        r'</header>\s*(?:</div>)?\s*(?:<!--[^>]*-->\s*)*<div class="portal-container">',
        '</header>\n\n    <!-- MAIN BODY - FULL WIDTH WORKSPACE -->\n    <div class="portal-container">',
        v2
    )

    # 3. Clean CSS for Exposed Nav and Balanced Body Margins
    clean_css = """
/* =========================================================================
   EXPOSED HEADER STAGE DROPDOWNS & BALANCED EDITORIAL BODY MARGINS
   ========================================================================= */
.exposed-header-nav {
  display: flex;
  align-items: center;
  gap: 6px;
}
.nav-stage-dropdown {
  position: relative;
}
.stage-nav-btn {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 6px 11px;
  background: #F8FAFC;
  border: 1.5px solid #CBD5E1;
  border-radius: 7px;
  font-size: 12px;
  font-weight: 700;
  color: #0F2440;
  cursor: pointer;
  transition: all 0.18s ease;
  white-space: nowrap;
}
.stage-nav-btn:hover,
.nav-stage-dropdown:hover .stage-nav-btn,
.nav-stage-dropdown.is-open .stage-nav-btn {
  background: #0F2440 !important;
  color: #FFFFFF !important;
  border-color: #0F2440 !important;
}
.nav-stage-dropdown.has-active .stage-nav-btn {
  background: #0F2440 !important;
  color: #FFFFFF !important;
  border-color: #0F2440 !important;
  box-shadow: 0 1px 4px rgba(15, 36, 64, 0.2) !important;
}
.stage-chevron {
  transition: transform 0.2s ease;
}
.nav-stage-dropdown:hover .stage-chevron,
.nav-stage-dropdown.is-open .stage-chevron {
  transform: rotate(180deg);
}
.stage-menu-flyout {
  display: none;
  position: absolute;
  top: calc(100% + 4px);
  left: 0;
  min-width: 270px;
  background: #FFFFFF;
  border: 1.5px solid #CBD5E1;
  border-radius: 10px;
  box-shadow: 0 16px 36px rgba(15, 36, 64, 0.16);
  padding: 6px;
  z-index: 99999;
}
.stage-menu-flyout::before {
  content: "";
  position: absolute;
  top: -8px;
  left: 0;
  right: 0;
  height: 8px;
  background: transparent;
}
.nav-stage-dropdown:hover .stage-menu-flyout {
  display: block;
}
.stage-item {
  display: block;
  padding: 7px 11px;
  font-size: 12px;
  font-weight: 600;
  color: #334155;
  text-decoration: none;
  border-radius: 6px;
  transition: all 0.15s ease;
  white-space: nowrap;
}
.stage-item:hover {
  background: #F1F5F9;
  color: #0F2440;
}
.stage-item.active {
  background: rgba(15, 36, 64, 0.08);
  color: #0F2440;
  font-weight: 700;
}

/* Responsive labels */
.stage-full-label { display: inline; }
.stage-short-label { display: none; }

@media (max-width: 1240px) {
  .stage-full-label { display: none !important; }
  .stage-short-label { display: inline !important; }
  .stage-nav-btn { padding: 5px 9px !important; }
}

@media (max-width: 900px) {
  .current-section-indicator { display: none !important; }
}

@media (max-width: 768px) {
  .apple-nav-inner { padding: 6px 12px !important; }
  .exposed-header-nav { overflow-x: auto; -webkit-overflow-scrolling: touch; padding-bottom: 2px; }
  .stage-nav-btn { font-size: 11px !important; padding: 4px 7px !important; }
}

/* PROFESSIONAL EDITORIAL BODY MARGINS (NO EDGE TOUCHING, NO VOID GAP) */
.portal-content {
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 12px 24px 80px 24px !important;
  box-sizing: border-box !important;
  overflow-y: visible;
}

.editorial-layout {
  display: block !important;
  width: 100% !important;
  max-width: 1360px !important;
  margin: 0 auto !important;
  padding: 4px 16px 60px 16px !important;
  box-sizing: border-box !important;
}

@media (max-width: 1200px) {
  .portal-content { padding: 10px 16px 60px 16px !important; }
  .editorial-layout { padding: 4px 8px 50px 8px !important; }
}

@media (max-width: 640px) {
  .portal-content { padding: 8px 10px 40px 10px !important; }
  .editorial-layout { padding: 2px 4px 30px 4px !important; }
}

/* Tight Header & Title Spacing */
.editorial-breadcrumb {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  font-size: 11.5px !important;
  font-weight: 600 !important;
  color: var(--apple-text-sec, #86868B) !important;
  margin-top: 0 !important;
  margin-bottom: 4px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
}

.editorial-header {
  margin-top: 0 !important;
  margin-bottom: 12px !important;
}

.editorial-header-eyebrow {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  color: var(--apple-gold-dark, #9A751E) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  margin-top: 0 !important;
  margin-bottom: 3px !important;
}

.page-title {
  margin-top: 0 !important;
  margin-bottom: 4px !important;
  font-size: 25px !important;
  font-weight: 800 !important;
  line-height: 1.25 !important;
  letter-spacing: -0.015em !important;
}

.page-desc {
  margin-top: 0 !important;
  margin-bottom: 10px !important;
  font-size: 14px !important;
  line-height: 1.5 !important;
  color: var(--apple-text-sec, #64748B) !important;
}
"""
    # Replace old exposed navigation CSS block or append
    old_css_idx = v2.find('/* =========================================================================\n   EXPOSED HEADER NAVIGATION')
    if old_css_idx != -1:
        end_css_idx = v2.find('</style>', old_css_idx)
        v2 = v2[:old_css_idx] + clean_css.strip() + "\n" + v2[end_css_idx:]
    else:
        v2 = v2.replace('</style>', f'{clean_css}\n</style>')

    # 4. Fix inline style in tab-market-demand
    v2 = v2.replace(
        '<div class="editorial-layout" style="display:block; width:100%; max-width:100%; padding:4px 0 60px 0;">',
        '<div class="editorial-layout" style="display:block; width:100%; max-width:1360px; margin:0 auto; padding:4px 16px 60px 16px;">'
    )

    # 5. Add Synchronized switchTab and switchTabAndClose JS
    js_sync = """
    // =========================================================================
    // EXPOSED HEADER STAGE DROPDOWNS & SYNC CONTROLLER
    // =========================================================================
    const STAGE_MAP = {
      'tab-overview': 'stage1', 'tab-options': 'stage1', 'tab-advisory': 'stage1', 'tab-strategy': 'stage1', 'tab-market-demand': 'stage1',
      'tab-houses': 'stage2', 'tab-capex': 'stage2', 'tab-planning': 'stage2', 'tab-tax': 'stage2',
      'tab-cqc': 'stage3', 'tab-cqc-reqs': 'stage3', 'tab-financials': 'stage3', 'tab-commissioning': 'stage3',
      'tab-tracker': 'stage4', 'tab-vault': 'stage4', 'tab-glossary': 'stage4'
    };

    function toggleStageDropdown(stageId, event) {
      if (event) {
        event.stopPropagation();
        event.preventDefault();
      }
      const targetFlyout = document.getElementById('flyout-' + stageId);
      const isVisible = targetFlyout && targetFlyout.style.display === 'block';

      closeAllStageDropdowns();

      if (!isVisible && targetFlyout) {
        targetFlyout.style.display = 'block';
        const parentDropdown = targetFlyout.closest('.nav-stage-dropdown');
        if (parentDropdown) parentDropdown.classList.add('is-open');
      }
    }

    function closeAllStageDropdowns() {
      document.querySelectorAll('.stage-menu-flyout').forEach(f => f.style.display = 'none');
      document.querySelectorAll('.nav-stage-dropdown').forEach(d => d.classList.remove('is-open'));
    }

    document.addEventListener('click', function(e) {
      if (!e.target.closest('.nav-stage-dropdown')) {
        closeAllStageDropdowns();
      }
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeAllStageDropdowns();
    });

    function syncStageNavbar(tabId) {
      const activeStage = STAGE_MAP[tabId] || 'stage1';
      document.querySelectorAll('.stage-nav-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.nav-stage-dropdown').forEach(d => d.classList.remove('has-active'));
      
      const activeBtn = document.getElementById('btn' + activeStage.charAt(0).toUpperCase() + activeStage.slice(1));
      const activeDropdown = document.getElementById('dropdown-' + activeStage);
      if (activeBtn) activeBtn.classList.add('active');
      if (activeDropdown) activeDropdown.classList.add('has-active');

      document.querySelectorAll('.stage-item').forEach(item => {
        const itemOnClick = item.getAttribute('onclick') || '';
        if (itemOnClick.includes("'" + tabId + "'") || itemOnClick.includes('"' + tabId + '"')) {
          item.classList.add('active');
        } else {
          item.classList.remove('active');
        }
      });

      const iconEl = document.getElementById('currentSectionIcon');
      const titleEl = document.getElementById('currentSectionTitle');
      const info = TAB_SECTION_INFO[tabId];
      if (info) {
        if (iconEl) iconEl.textContent = info.icon;
        if (titleEl) titleEl.textContent = info.name;
      }
    }

    function switchTabAndClose(tabId) {
      closeAllStageDropdowns();
      switchTab(tabId);
    }
"""
    # Replace old JS block or inject
    old_js_idx = v2.find('// =========================================================================\n    // EXPOSED HEADER STAGE DROPDOWNS')
    if old_js_idx != -1:
        end_js_idx = v2.find('function switchTab(tabId, btn) {', old_js_idx)
        v2 = v2[:old_js_idx] + js_sync.strip() + "\n\n    " + v2[end_js_idx:]
    else:
        v2 = v2.replace('function switchTab(tabId, btn) {', f'{js_sync}\n    function switchTab(tabId, btn) {{')

    # Ensure syncStageNavbar(tabId) is called inside switchTab
    if 'syncStageNavbar(tabId);' not in v2:
        v2 = v2.replace(
            'target.classList.add("active");',
            'target.classList.add("active");\n        syncStageNavbar(tabId);'
        )

    with open(v2_path, 'w', encoding='utf-8') as f:
        f.write(v2)
    print("✓ Successfully polished portal/v2.html.")

def polish_market_report():
    report_path = 'portal/luton-care-market-report.html'
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r'\.report-wrapper\s*\{[^}]*\}',
        '''.report-wrapper {
      width: 100%;
      max-width: 1360px;
      margin: 0 auto;
      padding: 12px 24px 80px 24px;
      box-sizing: border-box;
    }''',
        content
    )
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully polished portal/luton-care-market-report.html.")

def polish_v1():
    v1_path = 'portal/v1.html'
    with open(v1_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r'\.portal-content\s*\{[^}]*max-width:\s*[0-9]+px;[^}]*\}',
        '''.portal-content {
      width: 100%;
      max-width: 1360px;
      margin: 0 auto;
      padding: 12px 24px 80px 24px;
      box-sizing: border-box;
      overflow-y: visible;
    }''',
        content
    )
    with open(v1_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully polished portal/v1.html.")

if __name__ == '__main__':
    polish_v2()
    polish_market_report()
    polish_v1()
