#!/usr/bin/env python3
"""
scripts/fix_exposed_menu_and_spacing.py

1. Replaces the collapsed single 'Sections Menu' in portal/v2.html with 4 EXPOSED dropdown menus directly in the header navbar:
   - Stage 1: Strategy & Viability ▾
   - Stage 2: Property & Law ▾
   - Stage 3: CQC & Financials ▾
   - Stage 4: Execution & Vault ▾
   Plus active section indicator, V1/V2 toggle, Home icon, theme toggle, and print button.

2. Fixes the big gap from header to body and empty space on top across all pages:
   - Removes redundant nested <div class="portal-masthead"> wrapper around <header class="apple-nav-masthead">
   - Removes empty spacer tags and redundant spacing
   - Tightens editorial-header, breadcrumb, page-title, and page-desc margins

3. Provides professional, balanced editorial margin space for body text:
   - Centers content with max-width: 1360px and margin: 0 auto
   - Sets balanced 28px/16px side padding so text is never crammed or stretched edge-to-edge
   - Synchronizes portal/luton-care-market-report.html and portal/v1.html
"""

import os
import re

def update_v2():
    v2_path = 'portal/v2.html'
    with open(v2_path, 'r', encoding='utf-8') as f:
        v2 = f.read()

    # 1. Update Header HTML with 4 EXPOSED dropdown menus
    old_header_start = v2.find('<header class="apple-nav-masthead"')
    old_header_end = v2.find('</header>', old_header_start) + len('</header>')
    if old_header_start == -1 or old_header_end == -1:
        raise ValueError("Could not find <header class='apple-nav-masthead'> in v2.html")

    new_header_html = """<header class="apple-nav-masthead" id="mainHeader" style="position:sticky; top:0; z-index:10000; background:rgba(255,255,255,0.98); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); border-bottom:1.5px solid #E2E8F0; box-shadow:0 2px 10px rgba(15,36,64,0.05);">
      
      <div class="apple-nav-inner" style="display:flex; align-items:center; justify-content:space-between; padding:8px 32px; width:100%; max-width:100%; box-sizing:border-box; gap:14px; flex-wrap:wrap;">
        
        <!-- Left: Brand Logo -->
        <div class="apple-brand-wrap" onclick="switchTab('tab-overview')" style="cursor:pointer; display:flex; align-items:center; gap:9px; flex-shrink:0;" title="ADOV Care Group — Executive Overview">
          <div class="apple-brand-logo" style="width:32px; height:32px; border-radius:8px; background:linear-gradient(135deg, #0F2440 0%, #1E3A5F 100%); color:#FFFFFF; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:16px; box-shadow:0 2px 6px rgba(15,36,64,0.18);">A</div>
          <div style="display:flex; align-items:center; gap:7px;">
            <span class="apple-brand-title" style="font-size:14px; font-weight:800; letter-spacing:0.02em; color:#0F2440;">ADOV CARE GROUP</span>
            <span class="apple-brand-badge" style="font-size:10px; font-weight:700; background:rgba(194,155,56,0.14); color:#9A751E; padding:2px 7px; border-radius:10px; border:1px solid rgba(194,155,56,0.35);">V2.0</span>
          </div>
        </div>

        <!-- CENTER: EXPOSED DROPDOWN MENUS (ALL 4 STAGES DIRECTLY VISIBLE IN HEADER) -->
        <nav class="exposed-header-nav" id="exposedHeaderNav" aria-label="Executive Stage Navigation" style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">

          <!-- STAGE 1 DROPDOWN -->
          <div class="nav-stage-dropdown" id="dropdown-stage1" style="position:relative;">
            <button class="stage-nav-btn active" id="btnStage1" onclick="toggleStageDropdown('stage1', event)" aria-haspopup="true" aria-expanded="false" style="display:inline-flex; align-items:center; gap:6px; padding:6px 12px; background:#F8FAFC; border:1.5px solid #CBD5E1; border-radius:7px; font-size:12.5px; font-weight:700; color:#0F2440; cursor:pointer; transition:all 0.18s; white-space:nowrap;">
              <span>📊 Strategy &amp; Viability</span>
              <svg class="stage-chevron" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="stage-menu-flyout" id="flyout-stage1" style="display:none; position:absolute; top:calc(100% + 6px); left:0; min-width:280px; background:#FFFFFF; border:1.5px solid #CBD5E1; border-radius:10px; box-shadow:0 18px 40px rgba(15,36,64,0.18); padding:7px; z-index:99999;">
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
          <div class="nav-stage-dropdown" id="dropdown-stage2" style="position:relative;">
            <button class="stage-nav-btn" id="btnStage2" onclick="toggleStageDropdown('stage2', event)" aria-haspopup="true" aria-expanded="false" style="display:inline-flex; align-items:center; gap:6px; padding:6px 12px; background:#F8FAFC; border:1.5px solid #CBD5E1; border-radius:7px; font-size:12.5px; font-weight:700; color:#0F2440; cursor:pointer; transition:all 0.18s; white-space:nowrap;">
              <span>🏡 Property &amp; Planning</span>
              <svg class="stage-chevron" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="stage-menu-flyout" id="flyout-stage2" style="display:none; position:absolute; top:calc(100% + 6px); left:0; min-width:260px; background:#FFFFFF; border:1.5px solid #CBD5E1; border-radius:10px; box-shadow:0 18px 40px rgba(15,36,64,0.18); padding:7px; z-index:99999;">
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-houses')" class="stage-item">🏡 Properties &amp; Grounds</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-capex')" class="stage-item">🔨 CapEx Budget</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-planning')" class="stage-item">⚖️ Planning S192 (C3b)</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-tax')" class="stage-item">💼 Tax &amp; FRI Leases</a>
            </div>
          </div>

          <!-- STAGE 3 DROPDOWN -->
          <div class="nav-stage-dropdown" id="dropdown-stage3" style="position:relative;">
            <button class="stage-nav-btn" id="btnStage3" onclick="toggleStageDropdown('stage3', event)" aria-haspopup="true" aria-expanded="false" style="display:inline-flex; align-items:center; gap:6px; padding:6px 12px; background:#F8FAFC; border:1.5px solid #CBD5E1; border-radius:7px; font-size:12.5px; font-weight:700; color:#0F2440; cursor:pointer; transition:all 0.18s; white-space:nowrap;">
              <span>🩺 CQC &amp; Financials</span>
              <svg class="stage-chevron" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="stage-menu-flyout" id="flyout-stage3" style="display:none; position:absolute; top:calc(100% + 6px); left:0; min-width:270px; background:#FFFFFF; border:1.5px solid #CBD5E1; border-radius:10px; box-shadow:0 18px 40px rgba(15,36,64,0.18); padding:7px; z-index:99999;">
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-cqc')" class="stage-item">🩺 CQC Approval Roadmap</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-cqc-reqs')" class="stage-item">📋 10 Statutory Pillars</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-financials')" class="stage-item">📈 Financials &amp; P&amp;L</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-commissioning')" class="stage-item">🤝 Commissioning SOP</a>
            </div>
          </div>

          <!-- STAGE 4 DROPDOWN -->
          <div class="nav-stage-dropdown" id="dropdown-stage4" style="position:relative;">
            <button class="stage-nav-btn" id="btnStage4" onclick="toggleStageDropdown('stage4', event)" aria-haspopup="true" aria-expanded="false" style="display:inline-flex; align-items:center; gap:6px; padding:6px 12px; background:#F8FAFC; border:1.5px solid #CBD5E1; border-radius:7px; font-size:12.5px; font-weight:700; color:#0F2440; cursor:pointer; transition:all 0.18s; white-space:nowrap;">
              <span>✅ Execution &amp; Vault</span>
              <svg class="stage-chevron" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="stage-menu-flyout" id="flyout-stage4" style="display:none; position:absolute; top:calc(100% + 6px); right:0; min-width:250px; background:#FFFFFF; border:1.5px solid #CBD5E1; border-radius:10px; box-shadow:0 18px 40px rgba(15,36,64,0.18); padding:7px; z-index:99999;">
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-tracker')" class="stage-item">✅ 90-Day Tracker</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-vault')" class="stage-item">📁 Master Vault (38)</a>
              <a href="javascript:void(0)" onclick="switchTabAndClose('tab-glossary')" class="stage-item">📖 Technical Glossary</a>
            </div>
          </div>

        </nav>

        <!-- Right Quick Actions: Active Indicator, V1/V2, Home Icon, Theme & Print -->
        <div class="apple-nav-right" style="display:flex; align-items:center; gap:8px; flex-shrink:0;">
          
          <!-- Active Section Indicator Badge -->
          <div class="current-section-indicator" id="currentSectionIndicator" style="display:inline-flex; align-items:center; gap:5px; font-size:12px; font-weight:700; color:#0F2440; background:#F1F5F9; border:1px solid #E2E8F0; padding:5px 10px; border-radius:7px;">
            <span id="currentSectionIcon">📊</span> <span id="currentSectionTitle">Executive Overview</span>
          </div>

          <!-- V1 and V2 Toggle Switch -->
          <div class="version-toggle-group" style="display:inline-flex; align-items:center; background:#F1F5F9; border:1px solid #E2E8F0; border-radius:7px; padding:2px;">
            <a href="v1.html" class="v-toggle-btn" title="Switch to Version 1.0 (Operations MIS Dashboard)" style="padding:4px 10px; font-size:11.5px; font-weight:700; color:#475467; text-decoration:none; border-radius:5px; transition:all 0.18s;">V1</a>
            <a href="v2.html" class="v-toggle-btn active" title="Currently viewing Version 2.0 (Research Dossier)" style="padding:4px 10px; font-size:11.5px; font-weight:800; color:#FFFFFF; background:#0F2440; text-decoration:none; border-radius:5px; box-shadow:0 1px 3px rgba(15,36,64,0.18);">V2</a>
          </div>

          <!-- Just Home Icon for Gateway -->
          <a href="index.html" class="apple-btn-icon apple-btn-home" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center; width:30px; height:30px; border-radius:7px; border:1px solid #E2E8F0; background:#FFFFFF; color:#0F2440; transition:all 0.18s;" title="Return to Gateway Home">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 9.5L12 3l9 6.5V20a1.5 1.5 0 0 1-1.5 1.5H4.5A1.5 1.5 0 0 1 3 20V9.5z"></path>
              <polyline points="9 21 9 12 15 12 15 21"></polyline>
            </svg>
          </a>

          <!-- Appearance Theme Switcher -->
          <button class="apple-btn-pill" onclick="toggleTheme()" title="Toggle Appearance" style="padding:5px 8px; font-size:12px; border-radius:7px; border:1px solid #E2E8F0; background:#FFFFFF; cursor:pointer;">🌓</button>
          
          <!-- Print Dossier Button -->
          <button class="apple-btn-pill" onclick="window.print()" title="Print Current View" style="display:inline-flex; align-items:center; gap:5px; padding:5px 10px; font-size:12px; font-weight:700; border-radius:7px; border:1px solid #E2E8F0; background:#FFFFFF; color:#0F2440; cursor:pointer;">🖨️ Print</button>
        </div>

      </div>

    </header>"""

    # Remove the wrapper <div class="portal-masthead"> and </div>
    # Find the transition around header
    masthead_open = v2.find('<div class="portal-masthead">')
    if masthead_open != -1 and masthead_open < old_header_start:
        v2 = v2[:masthead_open] + v2[old_header_start:old_header_end] + v2[old_header_end:]
        # Remove the closing </div> of portal-masthead right after </header>
        hdr_end_pos = v2.find('</header>') + len('</header>')
        # Find next </div>
        next_div_end = v2.find('</div>', hdr_end_pos)
        if next_div_end != -1 and next_div_end - hdr_end_pos < 50:
            v2 = v2[:next_div_end] + v2[next_div_end + len('</div>'):]

    # Now replace the header with the new exposed header
    old_header_start = v2.find('<header class="apple-nav-masthead"')
    old_header_end = v2.find('</header>', old_header_start) + len('</header>')
    v2 = v2[:old_header_start] + new_header_html + v2[old_header_end:]
    print("✓ Replaced header with 4 EXPOSED dropdown menus.")

    # 2. Add / Update CSS rules for exposed menus and proper body text margins
    layout_css = """
/* =========================================================================
   EXPOSED HEADER NAVIGATION & EDITORIAL BODY MARGINS
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
  transition: all 0.18s ease;
}
.stage-nav-btn:hover,
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
.stage-item {
  display: block;
  padding: 8px 12px;
  font-size: 12.5px;
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
[data-theme="dark"] .stage-menu-flyout {
  background: #141E33 !important;
  border-color: #334155 !important;
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.5) !important;
}
[data-theme="dark"] .stage-item {
  color: #CBD5E1;
}
[data-theme="dark"] .stage-item:hover {
  background: #1E293B;
  color: #FFFFFF;
}
[data-theme="dark"] .stage-nav-btn {
  background: #1E293B !important;
  border-color: #334155 !important;
  color: #F8FAFC !important;
}

/* PROFESSIONAL EDITORIAL BODY TEXT MARGINS & CONTAINER CENTERING */
.portal-content {
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 14px 28px 80px 28px !important;
  box-sizing: border-box !important;
  overflow-y: visible;
}

.editorial-layout {
  display: block !important;
  width: 100% !important;
  max-width: 1360px !important;
  margin: 0 auto !important;
  padding: 6px 16px 60px 16px !important;
  box-sizing: border-box !important;
}

@media (max-width: 1200px) {
  .portal-content {
    padding: 12px 18px 60px 18px !important;
  }
  .editorial-layout {
    padding: 6px 10px 50px 10px !important;
  }
}

@media (max-width: 768px) {
  .portal-content {
    padding: 10px 12px 50px 12px !important;
  }
  .editorial-layout {
    padding: 4px 6px 40px 6px !important;
  }
  .current-section-indicator {
    display: none !important;
  }
  .stage-nav-btn span {
    font-size: 11.5px;
  }
}

/* Breadcrumb and Header Tight Spacing */
.editorial-breadcrumb {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  font-size: 11.5px !important;
  font-weight: 600 !important;
  color: var(--apple-text-sec, #86868B) !important;
  margin-top: 0 !important;
  margin-bottom: 6px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
}

.editorial-header {
  margin-top: 0 !important;
  margin-bottom: 14px !important;
}

.editorial-header-eyebrow {
  margin-bottom: 4px !important;
}

.page-title {
  margin-top: 0 !important;
  margin-bottom: 6px !important;
  font-size: 26px !important;
  line-height: 1.25 !important;
}

.page-desc {
  margin-top: 0 !important;
  margin-bottom: 12px !important;
  line-height: 1.5 !important;
  font-size: 14px !important;
}
"""
    if 'EXPOSED HEADER NAVIGATION' not in v2:
        v2 = v2.replace('</style>', f'{layout_css}\n</style>')
    else:
        # Replace existing block
        pass

    # 3. Add JavaScript handlers for Exposed Stage Dropdowns
    js_exposed_menus = """
    // =========================================================================
    // EXPOSED HEADER STAGE DROPDOWNS INTERACTIVITY
    // =========================================================================
    function toggleStageDropdown(stageId, event) {
      if (event) {
        event.stopPropagation();
        event.preventDefault();
      }
      const targetFlyout = document.getElementById('flyout-' + stageId);
      const targetBtn = document.getElementById('btnStage' + stageId.replace('stage', ''));
      const isVisible = targetFlyout && targetFlyout.style.display === 'block';

      // Close all flyouts
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

    // Close when clicking anywhere outside
    document.addEventListener('click', function(e) {
      if (!e.target.closest('.nav-stage-dropdown')) {
        closeAllStageDropdowns();
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeAllStageDropdowns();
      }
    });

    // Enhanced switchTabAndClose for exposed stage dropdowns
    function switchTabAndClose(tabId) {
      closeAllStageDropdowns();
      switchTab(tabId);
      
      // Update active stage button styling
      const STAGE_MAP = {
        'tab-overview': 'stage1', 'tab-options': 'stage1', 'tab-advisory': 'stage1', 'tab-strategy': 'stage1', 'tab-market-demand': 'stage1',
        'tab-houses': 'stage2', 'tab-capex': 'stage2', 'tab-planning': 'stage2', 'tab-tax': 'stage2',
        'tab-cqc': 'stage3', 'tab-cqc-reqs': 'stage3', 'tab-financials': 'stage3', 'tab-commissioning': 'stage3',
        'tab-tracker': 'stage4', 'tab-vault': 'stage4', 'tab-glossary': 'stage4'
      };
      
      const activeStage = STAGE_MAP[tabId] || 'stage1';
      document.querySelectorAll('.stage-nav-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.nav-stage-dropdown').forEach(d => d.classList.remove('has-active'));
      
      const activeBtn = document.getElementById('btn' + activeStage.charAt(0).toUpperCase() + activeStage.slice(1));
      const activeDropdown = document.getElementById('dropdown-' + activeStage);
      if (activeBtn) activeBtn.classList.add('active');
      if (activeDropdown) activeDropdown.classList.add('has-active');

      // Update active item inside flyouts
      document.querySelectorAll('.stage-item').forEach(item => {
        const itemOnClick = item.getAttribute('onclick') || '';
        if (itemOnClick.includes("'" + tabId + "'") || itemOnClick.includes('"' + tabId + '"')) {
          item.classList.add('active');
        } else {
          item.classList.remove('active');
        }
      });
    }
"""
    if 'function toggleStageDropdown' not in v2:
        v2 = v2.replace('function switchTab(tabId, btn) {', f'{js_exposed_menus}\n    function switchTab(tabId, btn) {{')
        print("✓ Injected JavaScript handlers for exposed stage dropdowns.")

    with open(v2_path, 'w', encoding='utf-8') as f:
        f.write(v2)
    print("✓ Successfully updated portal/v2.html.")

def update_standalone_report():
    report_path = 'portal/luton-care-market-report.html'
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r'\.report-wrapper\s*\{[^}]*\}',
        '''.report-wrapper {
      width: 100%;
      max-width: 1360px;
      margin: 0 auto;
      padding: 14px 28px 80px 28px;
      box-sizing: border-box;
    }''',
        content
    )

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully updated portal/luton-care-market-report.html body margins.")

def update_v1():
    v1_path = 'portal/v1.html'
    with open(v1_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r'\.portal-content\s*\{[^}]*max-width:\s*[0-9]+px;[^}]*\}',
        '''.portal-content {
      width: 100%;
      max-width: 1360px;
      margin: 0 auto;
      padding: 14px 28px 80px 28px;
      box-sizing: border-box;
      overflow-y: visible;
    }''',
        content
    )
    with open(v1_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully updated portal/v1.html body margins.")

if __name__ == '__main__':
    update_v2()
    update_standalone_report()
    update_v1()
