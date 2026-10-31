#!/usr/bin/env python3
"""
scripts/finalize_v2_clean_layout.py
Comprehensive Finalization of portal/v2.html:
1. Complete elimination of all robotic audio read options (HTML, JS, CSS, widgets, docks).
2. Dropdown Main Menu CSS & JavaScript injection with dark-mode & responsive support.
3. Dynamic active section indicator syncing across all navigation channels.
4. 100% full-width responsive layout for body webpage across desktop, tablet, and mobile.
5. V1/V2 segmented buttons, Home icon, and minimal header polish.
"""

import os
import re
import sys

def main():
    v2_path = "portal/v2.html"
    if not os.path.exists(v2_path):
        print(f"Error: {v2_path} does not exist!")
        sys.exit(1)

    with open(v2_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Starting portal/v2.html: {len(content):,} bytes, {content.count(chr(10))} lines.")

    # =========================================================================
    # 1. REMOVE REMAINING AUDIO HTML WIDGETS
    # =========================================================================
    # Remove 15 leftover rail audio snippets
    rail_audio_pattern = re.compile(
        r'\s*<p style="font-size:\s*11\.5px;\s*color:\s*var\(--apple-text-sec\);\s*margin:\s*0\s+0\s+10px\s+0;\s*line-height:\s*1\.45;">\s*Listen to synthesized executive audio briefing for this section\.\s*</p>\s*<button class="btn-rail-audio"[^>]*>.*?▶ Play Audio Briefing.*?</button>\s*</div>',
        re.DOTALL
    )
    matches_rail = rail_audio_pattern.findall(content)
    print(f"Found {len(matches_rail)} leftover rail audio snippets.")
    content = rail_audio_pattern.sub('', content)

    # Remove any stray .btn-rail-audio button blocks
    content = re.sub(
        r'\s*<button class="btn-rail-audio"[^>]*>.*?</button>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )

    # Remove trailing audio dock at end of file
    dock_pattern = re.compile(
        r'<!--\s*=+\s*EXECUTIVE MALE AUDIO BRIEFING PLAYER DOCK[\s\S]*?</div>\s*</div>\s*(?=</body>)',
        re.DOTALL
    )
    if dock_pattern.search(content):
        content = dock_pattern.sub('\n', content)
        print("✓ Trailing audio player dock HTML removed.")

    # Remove any other executive-audio-dock or player remnants
    content = re.sub(
        r'<div id="executive-audio-(?:player|dock)"[\s\S]*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # =========================================================================
    # 2. REMOVE AUDIO JAVASCRIPT & SPEECH SYNTHESIS ENGINE
    # =========================================================================
    # Remove ExecutiveAudioEngine block
    audio_js_pattern = re.compile(
        r'// 12\. EXECUTIVE AUDIO BRIEFING ENGINE[\s\S]*?(?=// 13\. MASTER INITIALIZATION)',
        re.DOTALL
    )
    if audio_js_pattern.search(content):
        content = audio_js_pattern.sub('\n    // 12. [Audio Briefing Engine Removed per User Request]\n\n    ', content)
        print("✓ ExecutiveAudioEngine JavaScript removed.")

    # Remove safe audio briefing pause in switchTab
    content = re.sub(
        r'// 1\. Safe audio briefing pause\s*try\s*\{\s*if\s*\(window\.ExecutiveAudioEngine[\s\S]*?\}\s*\}\s*catch\s*\(e\)\s*\{\}',
        '// 1. [Audio pause check removed]',
        content
    )

    # Remove init call: try { ExecutiveAudioEngine.init(); } catch (e) {}
    content = re.sub(
        r'try\s*\{\s*ExecutiveAudioEngine\.init\(\);\s*\}\s*catch\s*\(e\)\s*\{\}',
        '// ExecutiveAudioEngine removed',
        content
    )

    # Remove any leftover toggleTabAudio or audio button onclicks
    content = content.replace("toggleTabAudio(", "// toggleTabAudio(")

    # =========================================================================
    # 3. REMOVE AUDIO CSS
    # =========================================================================
    # Remove header audio CSS list in print / hide styles
    content = content.replace(".btn-audio-listen,\n      #executive-audio-player,\n      .audio-wave-bars,\n      .audio-player-dock,\n      .audio-reading-active,\n", "")
    content = content.replace(".btn-rail-audio, .btn-rail-download, .btn-rail-print", ".btn-rail-download, .btn-rail-print")
    
    # Remove main audio CSS block from /* Tab Header Listen Audio Button */ to before .editorial-layout
    audio_css_pattern = re.compile(
        r'/\*\s*Tab Header Listen Audio Button\s*\*[\s\S]*?(?=/\*\s*=+[\r\n]+\s*EXECUTIVE TWO-COLUMN)',
        re.DOTALL
    )
    if audio_css_pattern.search(content):
        content = audio_css_pattern.sub('\n', content)
        print("✓ Audio styling CSS removed.")

    # Also remove any leftover .btn-rail-audio:hover rules
    content = re.sub(r'\.btn-rail-audio:hover\s*\{[^}]*\}', '', content)

    # =========================================================================
    # 4. FULL-WIDTH RESPONSIVE BODY WEBPAGE & EDITORIAL LAYOUT
    # =========================================================================
    # Ensure .portal-content is 100% full width and responsive
    old_portal_content_css = re.compile(
        r'\.portal-content\s*\{\s*width:\s*100%;\s*max-width:\s*1480px;\s*margin:\s*0\s+auto;\s*padding:\s*24px\s+32px\s+80px\s+32px;\s*overflow-y:\s*visible;\s*\}'
    )
    new_portal_content_css = """.portal-content {
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 !important;
      padding: 24px 44px 80px 44px !important;
      box-sizing: border-box !important;
      overflow-y: visible;
    }
    @media (max-width: 1024px) {
      .portal-content {
        padding: 20px 24px 60px 24px !important;
      }
    }
    @media (max-width: 640px) {
      .portal-content {
        padding: 16px 14px 40px 14px !important;
      }
    }"""
    if old_portal_content_css.search(content):
        content = old_portal_content_css.sub(new_portal_content_css, content)
        print("✓ Updated .portal-content to 100% responsive full-width.")

    # Ensure .editorial-layout is 100% full width
    content = re.sub(
        r'\.editorial-layout\s*\{\s*display:\s*block\s*!important;\s*max-width:\s*1060px\s*!important;.*?\}',
        """.editorial-layout {
  display: block !important;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 24px 0 100px 0 !important;
  box-sizing: border-box !important;
}""",
        content,
        flags=re.DOTALL
    )

    # Update any earlier .editorial-layout rule
    content = re.sub(
        r'\.editorial-layout\s*\{\s*width:\s*100%;\s*max-width:\s*100%;\s*margin:\s*0;\s*padding:\s*28px\s+48px\s+100px\s+48px;\s*box-sizing:\s*border-box;\s*\}',
        """.editorial-layout {
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 20px 0 80px 0 !important;
  box-sizing: border-box !important;
}""",
        content
    )

    # =========================================================================
    # 5. INJECT COMPREHENSIVE DROPDOWN MENU & MINIMAL HEADER CSS
    # =========================================================================
    minimal_header_css = """
    /* =========================================================================
       MINIMAL DROPDOWN MAIN MENU & EXECUTIVE HEADER STYLES (LIGHT & DARK)
       ========================================================================= */
    .apple-nav-masthead {
      position: sticky;
      top: 0;
      z-index: 10000;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid #E2E8F0;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
      transition: background 0.25s, border-color 0.25s;
    }
    [data-theme="dark"] .apple-nav-masthead {
      background: rgba(15, 23, 42, 0.96);
      border-bottom-color: #334155;
      box-shadow: 0 1px 6px rgba(0, 0, 0, 0.35);
    }

    .apple-nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 9px 36px;
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      gap: 16px;
    }
    @media (max-width: 768px) {
      .apple-nav-inner {
        padding: 8px 14px;
        gap: 8px;
      }
    }

    /* Brand Logo & Title */
    .apple-brand-wrap {
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      user-select: none;
      flex-shrink: 0;
    }
    .apple-brand-logo {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: linear-gradient(135deg, #0F2440 0%, #1E3A5F 100%);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 15px;
      box-shadow: 0 2px 6px rgba(15, 36, 64, 0.18);
    }
    [data-theme="dark"] .apple-brand-logo {
      background: linear-gradient(135deg, #C29B38 0%, #9A7B2C 100%);
      color: #0F2440;
    }
    .apple-brand-title {
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 0.02em;
      color: #0F2440;
    }
    [data-theme="dark"] .apple-brand-title {
      color: #F8FAFC;
    }
    .apple-brand-badge {
      font-size: 10.5px;
      font-weight: 700;
      background: rgba(194, 155, 56, 0.12);
      color: #C29B38;
      padding: 2px 8px;
      border-radius: 12px;
      border: 1px solid rgba(194, 155, 56, 0.35);
    }

    /* Dropdown Main Menu Button */
    .nav-dropdown-wrapper {
      position: relative;
    }
    .btn-main-dropdown {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      background: #F8FAFC;
      border: 1.5px solid #CBD5E1;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      color: #0F2440;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .btn-main-dropdown:hover,
    .btn-main-dropdown[aria-expanded="true"] {
      background: #FFFFFF;
      border-color: #0F2440;
      color: #0F2440;
      box-shadow: 0 2px 8px rgba(15, 36, 64, 0.12);
    }
    [data-theme="dark"] .btn-main-dropdown {
      background: #1E293B;
      border-color: #334155;
      color: #F8FAFC;
    }
    [data-theme="dark"] .btn-main-dropdown:hover,
    [data-theme="dark"] .btn-main-dropdown[aria-expanded="true"] {
      background: #283548;
      border-color: #C29B38;
      color: #FFFFFF;
    }

    /* Flyout Panel */
    .menu-dropdown-flyout {
      position: absolute;
      top: calc(100% + 8px);
      left: 0;
      width: 840px;
      max-width: 95vw;
      background: #FFFFFF;
      border: 1.5px solid #CBD5E1;
      border-radius: 14px;
      box-shadow: 0 24px 50px -10px rgba(15, 36, 64, 0.22), 0 0 1px rgba(0,0,0,0.1);
      padding: 22px 24px;
      z-index: 99999;
      animation: flyoutSlideDown 0.18s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes flyoutSlideDown {
      from { opacity: 0; transform: translateY(-6px); }
      to { opacity: 1; transform: translateY(0); }
    }
    [data-theme="dark"] .menu-dropdown-flyout {
      background: #0F172A;
      border-color: #334155;
      box-shadow: 0 24px 50px -10px rgba(0, 0, 0, 0.65), 0 0 1px rgba(255,255,255,0.1);
    }

    .dropdown-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }
    @media (max-width: 960px) {
      .menu-dropdown-flyout {
        width: 640px;
      }
      .dropdown-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
      }
    }
    @media (max-width: 680px) {
      .menu-dropdown-flyout {
        position: fixed;
        top: 56px;
        left: 4vw;
        width: 92vw;
        max-height: 82vh;
        overflow-y: auto;
        padding: 16px;
      }
      .dropdown-grid {
        grid-template-columns: 1fr;
        gap: 14px;
      }
    }

    .dropdown-stage-col {
      display: flex;
      flex-direction: column;
    }
    .dropdown-stage-header {
      margin-bottom: 8px;
      padding-bottom: 5px;
      border-bottom: 1.5px solid #F1F5F9;
    }
    [data-theme="dark"] .dropdown-stage-header {
      border-bottom-color: #1E293B;
    }
    .dropdown-stage-tag {
      display: block;
      font-size: 9px;
      font-weight: 800;
      color: #C29B38;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }
    .dropdown-stage-title {
      font-size: 11.5px;
      font-weight: 700;
      color: #0F2440;
    }
    [data-theme="dark"] .dropdown-stage-title {
      color: #F8FAFC;
    }

    .dropdown-item {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 6px 9px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      color: #334155;
      text-decoration: none;
      transition: all 0.15s ease;
    }
    .dropdown-item:hover {
      background: #F1F5F9;
      color: #0F2440;
      font-weight: 700;
      transform: translateX(2px);
    }
    [data-theme="dark"] .dropdown-item {
      color: #CBD5E1;
    }
    [data-theme="dark"] .dropdown-item:hover {
      background: #1E293B;
      color: #FFFFFF;
    }

    /* Active Section Indicator Badge */
    .current-section-indicator {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 700;
      color: #0F2440;
      background: #F1F5F9;
      border: 1px solid #E2E8F0;
      padding: 5px 12px;
      border-radius: 8px;
      user-select: none;
    }
    [data-theme="dark"] .current-section-indicator {
      background: #1E293B;
      color: #F8FAFC;
      border-color: #334155;
    }
    @media (max-width: 900px) {
      .current-section-indicator {
        display: none !important;
      }
    }

    /* V1 and V2 Segmented Switch */
    .version-toggle-group {
      display: inline-flex;
      align-items: center;
      background: #F1F5F9;
      border: 1px solid #CBD5E1;
      border-radius: 8px;
      padding: 2px;
    }
    [data-theme="dark"] .version-toggle-group {
      background: #1E293B;
      border-color: #334155;
    }
    .v-toggle-btn {
      padding: 4px 11px;
      font-size: 12px;
      font-weight: 700;
      color: #475467;
      text-decoration: none;
      border-radius: 6px;
      transition: all 0.15s ease;
    }
    .v-toggle-btn:hover {
      color: #0F2440;
    }
    .v-toggle-btn.active {
      font-weight: 800;
      color: #FFFFFF !important;
      background: #0F2440 !important;
      box-shadow: 0 1px 3px rgba(15,36,64,0.18);
    }
    [data-theme="dark"] .v-toggle-btn {
      color: #94A3B8;
    }
    [data-theme="dark"] .v-toggle-btn.active {
      background: #C29B38 !important;
      color: #0F2440 !important;
    }

    /* Home Icon Button */
    .apple-btn-home {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background: #FFFFFF;
      color: #0F2440;
      text-decoration: none;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .apple-btn-home:hover {
      background: #0F2440;
      color: #FFFFFF;
      border-color: #0F2440;
      box-shadow: 0 2px 6px rgba(15, 36, 64, 0.15);
      transform: translateY(-1px);
    }
    [data-theme="dark"] .apple-btn-home {
      background: #1E293B;
      border-color: #334155;
      color: #F8FAFC;
    }
    [data-theme="dark"] .apple-btn-home:hover {
      background: #C29B38;
      border-color: #C29B38;
      color: #0F2440;
    }
    """

    # Inject CSS into </style> if not already present
    if "/* MINIMAL DROPDOWN MAIN MENU & EXECUTIVE HEADER STYLES" not in content:
        content = content.replace("</style>", f"{minimal_header_css}\n</style>", 1)
        print("✓ Injected Minimal Header & Dropdown CSS rules.")

    # =========================================================================
    # 6. INJECT ROBUST JAVASCRIPT FOR DROPDOWN & ACTIVE SECTION SYNC
    # =========================================================================
    dropdown_js = """
    // =========================================================================
    // MINIMAL DROPDOWN MAIN MENU & DYNAMIC SECTION INDICATOR (ROBUST)
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
      if (e) {
        e.stopPropagation();
        e.preventDefault();
      }
      const flyout = document.getElementById('menuDropdownFlyout');
      const btn = document.getElementById('btnMainDropdown');
      if (!flyout) return;
      const isOpen = flyout.style.display === 'block';
      flyout.style.display = isOpen ? 'none' : 'block';
      if (btn) btn.setAttribute('aria-expanded', !isOpen);
    }

    function switchTabAndClose(tabId) {
      if (typeof switchTab === 'function') {
        switchTab(tabId);
      }
      const flyout = document.getElementById('menuDropdownFlyout');
      const btn = document.getElementById('btnMainDropdown');
      if (flyout) flyout.style.display = 'none';
      if (btn) btn.setAttribute('aria-expanded', 'false');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function updateSectionIndicator(tabId) {
      const iconEl = document.getElementById('currentSectionIcon');
      const titleEl = document.getElementById('currentSectionTitle');
      const info = TAB_SECTION_INFO[tabId];
      if (info) {
        if (iconEl) iconEl.textContent = info.icon;
        if (titleEl) titleEl.textContent = info.name;
      }
    }

    // Global listener to close dropdown on click outside
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

    // Close on Escape key
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

    // Sync section indicator with switchTab
    (function hookSwitchTab() {
      const prevSwitchTab = window.switchTab;
      window.switchTab = function(tabId, el) {
        if (typeof prevSwitchTab === 'function') {
          prevSwitchTab(tabId, el);
        }
        updateSectionIndicator(tabId);
      };
    })();
    """

    # Check if `function toggleMainMenu` definition exists
    if "function toggleMainMenu(e)" not in content:
        # Place it right before the closing </script>
        last_script_idx = content.rfind("</script>")
        if last_script_idx != -1:
            content = content[:last_script_idx] + f"\n{dropdown_js}\n" + content[last_script_idx:]
            print("✓ Injected Dropdown Navigation & Indicator JavaScript.")

    # In initApp, make sure updateSectionIndicator is called
    content = content.replace(
        'switchTab(startTab);',
        'switchTab(startTab);\n      try { updateSectionIndicator(startTab); } catch (e) {}'
    )

    with open(v2_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✓ Saved finalized portal/v2.html ({len(content):,} bytes, {content.count(chr(10))} lines).")

if __name__ == "__main__":
    main()
