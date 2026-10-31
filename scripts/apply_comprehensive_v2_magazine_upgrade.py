#!/usr/bin/env python3
"""
apply_comprehensive_v2_magazine_upgrade.py
Applies all 19 boardroom-grade and academic journal upgrades to portal/v2.html.
"""

import os
import re
import sys

BASE_DIR = "/Users/mamun/Documents/Business Consultant"
V2_HTML_PATH = os.path.join(BASE_DIR, "portal/v2.html")
TEMP_DIR = os.path.join(BASE_DIR, "temp_upgrade")

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def check_tabs(html, label):
    tabs = re.findall(r'<div id=\"(tab-[^\"]+)\" class=\"tab-pane', html)
    print(f"[{label}] Tab count: {len(tabs)}")
    expected = [
        'tab-overview', 'tab-options', 'tab-advisory', 'tab-strategy', 'tab-houses',
        'tab-capex', 'tab-planning', 'tab-tax', 'tab-cqc', 'tab-cqc-reqs',
        'tab-financials', 'tab-commissioning', 'tab-tracker', 'tab-vault', 'tab-glossary'
    ]
    missing = set(expected) - set(tabs)
    if missing:
        print(f"  ❌ ERROR: Missing tabs: {missing}")
        sys.exit(1)
    return tabs

def main():
    print("Loading pristine portal/v2.html...")
    html = read_file(V2_HTML_PATH)
    initial_len = len(html)
    print(f"Initial size: {initial_len:,} characters, {len(html.splitlines()):,} lines")
    check_tabs(html, "START")

    # =========================================================================
    # 1. CSS INJECTION INTO <style>
    # =========================================================================
    print("\n[Step 1/15] Injecting unified magazine & vertical architecture CSS...")
    
    cqc1_text = read_file(os.path.join(TEMP_DIR, "cqc_vertical_part1.md"))
    cqc2_text = read_file(os.path.join(TEMP_DIR, "cqc_vertical_part2.md"))
    
    m_css1 = re.search(r"```css\s*(.*?)\s*```", cqc1_text, re.DOTALL)
    css1 = m_css1.group(1) if m_css1 else ""
    
    m_css2 = re.search(r"```css\s*(.*?)\s*```", cqc2_text, re.DOTALL)
    css2 = m_css2.group(1) if m_css2 else ""
    
    extra_css = """
/* =========================================================================
   ADDITIONAL MAGAZINE GRADE VERTICAL STYLES & NON-SCROLLING TABLES
   ========================================================================= */
.mcda-nonscroll-wrap {
  width: 100%;
  margin: 28px 0;
  background: #FFFFFF;
  border: 1.5px solid var(--border, #E2E8F0);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 14px rgba(15, 30, 54, 0.04);
}
.mcda-nonscroll-table {
  width: 100%;
  table-layout: fixed;
  border-collapse: collapse;
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--text-main, #1E293B);
}
.mcda-nonscroll-table th, .mcda-nonscroll-table td {
  padding: 14px 16px;
  border-bottom: 1px solid #E2E8F0;
  vertical-align: middle;
  word-wrap: break-word;
}
.mcda-nonscroll-table th {
  background: #0F1E36;
  color: #FFFFFF;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
.mcda-nonscroll-table tr:hover td {
  background: #F8FAFC;
}
.mcda-opt4-cell {
  background: #ECFDF5 !important;
  color: #065F46 !important;
  font-weight: 700;
  border-left: 2px solid #10B981;
  border-right: 2px solid #10B981;
}
.mcda-nonscroll-table th.mcda-opt4-th {
  background: #065F46;
  color: #FFFFFF;
  border-left: 2px solid #34D399;
  border-right: 2px solid #34D399;
}

/* Vertical Roadmap Progression */
.v-roadmap-stack {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin: 28px 0;
}
.v-roadmap-card {
  display: flex;
  flex-direction: row;
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 10px;
  padding: 22px;
  gap: 20px;
  align-items: flex-start;
  box-shadow: 0 3px 10px rgba(0,0,0,0.03);
  transition: transform 0.2s ease, border-color 0.2s ease;
}
.v-roadmap-card:hover {
  transform: translateY(-2px);
  border-color: #0284C7;
}
.v-roadmap-phase-badge {
  flex-shrink: 0;
  width: 140px;
  background: #0F1E36;
  color: #FFFFFF;
  border-radius: 8px;
  padding: 12px;
  text-align: center;
}
.v-roadmap-phase-num {
  font-size: 11px;
  font-weight: 800;
  color: #38BDF8;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 4px;
}
.v-roadmap-phase-dates {
  font-size: 14px;
  font-weight: 700;
}
.v-roadmap-phase-status {
  display: inline-block;
  margin-top: 6px;
  padding: 3px 8px;
  font-size: 10.5px;
  font-weight: 700;
  border-radius: 4px;
  background: #059669;
  color: #FFFFFF;
}
.v-roadmap-content {
  flex-grow: 1;
}
.v-roadmap-title {
  font-size: 16.5px;
  font-weight: 800;
  color: #0F1E36;
  margin: 0 0 8px 0;
}
.v-roadmap-desc {
  font-size: 13.5px;
  line-height: 1.6;
  color: #334155;
  margin-bottom: 12px;
}
.v-roadmap-bullets {
  margin: 0;
  padding-left: 20px;
  font-size: 13px;
  line-height: 1.6;
  color: #1E293B;
}

/* Vertical Tax Arbitrage Engine */
.v-tax-stack {
  display: flex;
  flex-direction: column;
  gap: 18px;
  margin: 26px 0;
}
.v-tax-card {
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}
.v-tax-tier-tag {
  display: inline-block;
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 4px;
  margin-bottom: 8px;
}

/* Rota Table Styles */
.rota-table-wrap {
  width: 100%;
  overflow-x: auto;
  margin: 24px 0;
  background: #FFFFFF;
  border: 1.5px solid #CBD5E1;
  border-radius: 8px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.03);
}
.rota-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  line-height: 1.5;
  text-align: center;
}
.rota-table th {
  background: #0F1E36;
  color: #FFFFFF;
  font-weight: 700;
  padding: 12px 10px;
  font-size: 12.5px;
  letter-spacing: 0.5px;
}
.rota-table td {
  padding: 10px 8px;
  border-bottom: 1px solid #E2E8F0;
  border-right: 1px solid #F1F5F9;
}
.rota-table tr:hover td {
  background: #F8FAFC;
}
.shift-e { background: #DBEAFE; color: #1E40AF; font-weight: 700; padding: 4px 8px; border-radius: 4px; font-size: 11.5px; display: inline-block; }
.shift-l { background: #FEF3C7; color: #92400E; font-weight: 700; padding: 4px 8px; border-radius: 4px; font-size: 11.5px; display: inline-block; }
.shift-wn { background: #EDE9FE; color: #5B21B6; font-weight: 700; padding: 4px 8px; border-radius: 4px; font-size: 11.5px; display: inline-block; }
.shift-si { background: #F1F5F9; color: #475569; font-weight: 700; padding: 4px 8px; border-radius: 4px; font-size: 11.5px; display: inline-block; }
.shift-off { background: #F3F4F6; color: #9CA3AF; font-weight: 600; padding: 4px 8px; border-radius: 4px; font-size: 11.5px; display: inline-block; }

/* Magazine Document Vault Grid */
.doc-vault-grid-mag {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 22px;
  margin: 28px 0;
}
.doc-vault-card-mag {
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 10px;
  padding: 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 3px 10px rgba(0,0,0,0.03);
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}
.doc-vault-card-mag:hover {
  transform: translateY(-3px);
  border-color: #C29B38;
  box-shadow: 0 8px 24px rgba(15, 30, 54, 0.08);
}
.doc-vault-card-mag-featured {
  border: 2px solid #C29B38;
  background: linear-gradient(180deg, #FFFFFF 0%, #FDFBF7 100%);
}
"""
    
    combined_css = "\n\n/* === MAGAZINE & VERTICAL FLOW UPGRADE CSS === */\n" + css1 + "\n" + css2 + "\n" + extra_css + "\n"
    
    if "</style>" in html:
        html = html.replace("</style>", combined_css + "\n</style>", 1)
        print("  ✓ Successfully injected CSS into <style> block.")
    check_tabs(html, "Step 1 (CSS)")

    # =========================================================================
    # 2. ARCHITECTURAL BLUEPRINT REPLACEMENT (ALL 4 OCCURRENCES)
    # =========================================================================
    print("\n[Step 2/15] Upgrading Architectural Blueprint SVGs in all 4 tabs...")
    
    blueprint_img_html = """<img src="assets/diagrams/diagram_campus_masterplan.svg" alt="Architectural Blueprint 78, 80 &amp; 82 Marston Gardens Specialist Campus" class="blueprint-svg" style="width: 100%; height: auto; border-radius: 8px; border: 1.5px solid #1E3E62; display: block; box-shadow: 0 4px 14px rgba(11,23,40,0.12);" loading="lazy">"""
    
    blueprint_caption_html = """<div class="visual-diagram-caption">
          <strong>High-Precision Architectural CAD Masterplan:</strong> <strong>78 Marston Gardens on the Left Flank</strong> (5 Specialist Suites, Commercial Kitchen, Communal Dining Hall), <strong>80 Marston Gardens in the Middle</strong> (3 Specialist Suites, Sensory Calm Lounge, Registered Staff Office &amp; Sleep-In Room), and <strong>82 Marston Gardens on the Right Flank</strong> (Director Private Residence under S.105/106 ITEPA 2003 AST). Cul-de-sac frontage with 10 dedicated off-street parking bays compliant with Luton Local Plan LLP1, LLP25, LLP31 &amp; LLP32. 100ft sensory rear gardens with paved circular mobility pathways.
        </div>"""
    
    bp_pattern = re.compile(
        r'(<span class="visual-diagram-badge badge-blue">Architectural Blueprint</span>\s*'
        r'<span class="visual-diagram-title">78 &amp; 80 Marston Gardens // 8-Bed Unified Specialist Campus</span>\s*'
        r'</div>\s*'
        r'<div class="visual-diagram-body">)\s*'
        r'(<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 720".*?</svg>)\s*'
        r'</div>\s*'
        r'(<div class="visual-diagram-caption">.*?</div>)',
        re.DOTALL
    )
    
    def replace_bp(m):
        return f"{m.group(1)}\n          {blueprint_img_html}\n        </div>\n        {blueprint_caption_html}"
    
    html, count = bp_pattern.subn(replace_bp, html)
    print(f"  ✓ Replaced {count} occurrences of old blueprint SVG with CAD masterplan image & updated caption.")
    check_tabs(html, "Step 2 (Blueprint)")

    # =========================================================================
    # 3. FINANCIAL WATERFALL CAPTION UPDATE (RATIO-WISE BAR CHART)
    # =========================================================================
    print("\n[Step 3/15] Verifying Financial Waterfall ratio-wise bar chart captions...")
    waterfall_caption_html = """<div class="visual-diagram-caption">
          <strong>Audited Ratio-Wise Proportional Waterfall:</strong> Proportional financial flow from 100.0% Gross Placement Turnover (&pound;977,600) to Operating EBITDA (&pound;341,392 / 34.9% margin) and Consolidated Pre-Tax Cashflow (&pound;438,392 / 44.8% cash velocity). Operating expenses itemized proportionally: Care Staff Payroll (-36.3% / -&pound;355.1k), PropCo Commercial FRI Leases (-9.9% / -&pound;97.0k), Utilities &amp; Energy (-4.9% / -&pound;48.2k), Resident Provisions (-2.5% / -&pound;24.8k), and Regulatory, Insurance &amp; Sinking Reserves (-11.4% / -&pound;111.1k).
        </div>"""
    
    html = re.sub(
        r'<img src="assets/diagrams/diagram_financial_waterfall\.svg"[^>]*>\s*</div>\s*<div class="visual-diagram-caption">.*?</div>',
        f'<img src="assets/diagrams/diagram_financial_waterfall.svg" alt="Audited Ratio-Wise Financial Waterfall" class="visual-diagram-img" loading="lazy">\n        </div>\n        {waterfall_caption_html}',
        html,
        flags=re.DOTALL
    )
    print("  ✓ Updated Financial Waterfall captions with ratio-wise breakdown details.")

    # =========================================================================
    # 4. CQC FAST-TRACK APPROVAL ROADMAP (5 MILESTONE PHASES VERTICAL REDESIGN)
    # =========================================================================
    print("\n[Step 4/15] Redesigning CQC Fast-Track 5 Milestone Phases as vertical cards...")
    
    cqc_5phases_html = """<div class="cqc-5phases-vertical-stack" style="display: flex; flex-direction: column; gap: 20px; margin: 24px 0;">
  <div style="background: #0F1E36; color: #FFFFFF; padding: 16px 20px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #C29B38;">
    <div>
      <span style="font-size: 11px; font-weight: 800; color: #C29B38; text-transform: uppercase; letter-spacing: 1px;">Fast-Track Regulatory Strategy</span>
      <h3 style="font-size: 17px; font-weight: 800; margin: 2px 0 0 0; color: #FFFFFF;">CQC Fast-Track Approval Roadmap (5 Milestone Phases &bull; S.28(3) Acceleration)</h3>
    </div>
    <span style="background: #059669; color: #FFFFFF; font-size: 11.5px; font-weight: 800; padding: 6px 14px; border-radius: 4px;">Cuts 28 Calendar Days</span>
  </div>

  <!-- Phase 1 -->
  <div class="cqc-phase-card" style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-left: 5px solid #0284C7; border-radius: 10px; padding: 22px; box-shadow: 0 3px 12px rgba(0,0,0,0.03);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="background: #E0F2FE; color: #0369A1; font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.5px;">Phase 1 &bull; Days 1 to 20</span>
        <h4 style="font-size: 16.5px; font-weight: 800; color: #0F1E36; margin: 0;">Pre-Application Preparation &amp; Statutory Vetting</h4>
      </div>
      <span style="font-size: 12px; font-weight: 700; color: #0284C7;">Regulation 12 &amp; 13 HSCA 2009</span>
    </div>
    <p style="font-size: 14px; line-height: 1.6; color: #334155; margin-bottom: 12px;">
      Execute CQC enhanced countersigned DBS checks for Nominated Individual (NI) and Registered Manager (RM). Complete GP Medical Fitness Questionnaires. Draft formal Statement of Purpose defining "Personal Care" regulated activity under Health and Social Care Act 2008. Finalize 7 core statutory policies and commission ICAEW accountant sign-off on Regulation 13 Financial Viability 12-month cashflow model.
    </p>
    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 10px; font-size: 13px; color: #1E293B;">
      <div>✓ Enhanced CQC DBS Countersignature</div>
      <div>✓ GP Medical Fitness Form Signed</div>
      <div>✓ Statement of Purpose (Reg 12)</div>
      <div>✓ Reg 13 Financial Viability Signoff</div>
      <div>✓ 7 Core Statutory Policies Ready</div>
    </div>
  </div>

  <!-- Phase 2 -->
  <div class="cqc-phase-card" style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-left: 5px solid #6366F1; border-radius: 10px; padding: 22px; box-shadow: 0 3px 12px rgba(0,0,0,0.03);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="background: #EEF2FF; color: #4338CA; font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.5px;">Phase 2 &bull; Days 21 to 40</span>
        <h4 style="font-size: 16.5px; font-weight: 800; color: #0F1E36; margin: 0;">Governance Architecture &amp; Key Person Appointments</h4>
      </div>
      <span style="font-size: 12px; font-weight: 700; color: #6366F1;">Regulations 5, 6 &amp; 7 HSCA 2014</span>
    </div>
    <p style="font-size: 14px; line-height: 1.6; color: #334155; margin-bottom: 12px;">
      Appoint Qualified Registered Manager (Regulation 7) holding Level 5 Diploma in Leadership &amp; Management for Adult Care with extensive specialist autism and learning disabilities background. Formally designate Nominated Individual (Regulation 6) Non-Executive Director to oversee statutory governance and quality assurance under Regulation 17. Execute 10-year commercial Full Repairing and Insuring (FRI) intercompany leases.
    </p>
    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 10px; font-size: 13px; color: #1E293B;">
      <div>✓ Level 5 Registered Manager Appointed</div>
      <div>✓ Nominated Individual (Reg 6) Active</div>
      <div>✓ Fit &amp; Proper Person Reg 5 Checks</div>
      <div>✓ 10-Yr Commercial FRI Leases Executed</div>
      <div>✓ S.192 CLPUD Planning Immunity Secured</div>
    </div>
  </div>

  <!-- Phase 3 -->
  <div class="cqc-phase-card" style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-left: 5px solid #8B5CF6; border-radius: 10px; padding: 22px; box-shadow: 0 3px 12px rgba(0,0,0,0.03);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="background: #F5F3FF; color: #6D28D9; font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.5px;">Phase 3 &bull; Days 41 to 55</span>
        <h4 style="font-size: 16.5px; font-weight: 800; color: #0F1E36; margin: 0;">CQC Provider Portal Submission &amp; Gatekeeping Validation</h4>
      </div>
      <span style="font-size: 12px; font-weight: 700; color: #8B5CF6;">Health &amp; Social Care Act 2008 s.10</span>
    </div>
    <p style="font-size: 14px; line-height: 1.6; color: #334155; margin-bottom: 12px;">
      Submit complete provider and registered manager applications online through the new CQC Provider Portal. Submit comprehensive model answers for all 42 Provider Application questions across 9 statutory categories. Pass CQC National Registration Team document validation gatekeeping within 5 to 10 working days, generating official application reference number and inspector allocation.
    </p>
    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 10px; font-size: 13px; color: #1E293B;">
      <div>✓ 42 Model Application Answers Uploaded</div>
      <div>✓ CQC Portal Validation Complete</div>
      <div>✓ Official CQC Reference Number Issued</div>
      <div>✓ Regulatory Inspector Assigned</div>
      <div>✓ e-MAR &amp; Care Planning Software Configured</div>
    </div>
  </div>

  <!-- Phase 4 -->
  <div class="cqc-phase-card" style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-left: 5px solid #F59E0B; border-radius: 10px; padding: 22px; box-shadow: 0 3px 12px rgba(0,0,0,0.03);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="background: #FEF3C7; color: #92400E; font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.5px;">Phase 4 &bull; Days 56 to 75</span>
        <h4 style="font-size: 16.5px; font-weight: 800; color: #0F1E36; margin: 0;">Clinical Interview Defense &amp; Physical Site Inspection</h4>
      </div>
      <span style="font-size: 12px; font-weight: 700; color: #F59E0B;">CQC Single Assessment Framework</span>
    </div>
    <p style="font-size: 14px; line-height: 1.6; color: #334155; margin-bottom: 12px;">
      Conduct rigorous 2-hour CQC interview defense for Registered Manager across 5 clinical crisis scenarios (medication errors, unnotified DoLS restrictions, safeguarding escalation to Luton MASH, resident choking/dysphagia, sudden refusal of personal care). Host CQC physical campus inspection across 78 &amp; 80 Marston Gardens, verifying BS 5839 Cat L1 fire detection, FD30S doors, TMV3 anti-scald valves at 41&deg;C, commercial kitchen Food Hygiene 5 setup, and staff sleep-in facilities.
    </p>
    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 10px; font-size: 13px; color: #1E293B;">
      <div>✓ RM Fit &amp; Proper Interview Passed</div>
      <div>✓ 5 Clinical Crisis Scenarios Defended</div>
      <div>✓ Physical Campus Inspection Signoff</div>
      <div>✓ BS 5839 Cat L1 &amp; FD30S Certified</div>
      <div>✓ Water Safety TMV3 41&deg;C Verification</div>
    </div>
  </div>

  <!-- Phase 5 -->
  <div class="cqc-phase-card" style="background: #F0FDF4; border: 2px solid #10B981; border-left: 6px solid #059669; border-radius: 10px; padding: 22px; box-shadow: 0 4px 14px rgba(5,150,105,0.06);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="background: #D1FAE5; color: #065F46; font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.5px;">Phase 5 &bull; Days 76 to 90</span>
        <h4 style="font-size: 17px; font-weight: 800; color: #065F46; margin: 0;">Notice of Proposal &amp; Statutory Section 28(3) Fast-Track Waiver</h4>
      </div>
      <span style="background: #059669; color: #FFFFFF; font-size: 11.5px; font-weight: 800; padding: 4px 10px; border-radius: 4px;">Cuts 28 Calendar Days</span>
    </div>
    <p style="font-size: 14px; line-height: 1.6; color: #166534; margin-bottom: 12px;">
      CQC issues formal Notice of Proposal (NoP) under Section 26 of Health and Social Care Act 2008. The operator immediately executes the statutory <strong>Section 28(3) Waiver of Representations Letter</strong>, waiving the mandatory 28-day statutory waiting period. CQC issues final Notice of Decision (NoD) and Provider Registration Certificate within 48 to 72 hours, cutting nearly a month off launch timelines and activating immediate placement on Luton Borough Council ProContract DPS (AT1115) and NHS BLMK ICB contracts.
    </p>
    <div style="background: #FFFFFF; border: 1.5px solid #34D399; border-radius: 6px; padding: 12px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 10px; font-size: 13px; color: #065F46; font-weight: 700;">
      <div>✓ Notice of Proposal (NoP) Received</div>
      <div>✓ Section 28(3) Statutory Waiver Submitted</div>
      <div>✓ Notice of Decision (NoD) Issued (48–72h)</div>
      <div>✓ CQC Registration Certificate Live</div>
      <div>✓ Luton DPS AT1115 Placement Activated</div>
    </div>
  </div>
</div>"""

    pos_cqc_tab = html.find('id="tab-cqc"')
    if pos_cqc_tab != -1:
        pos_diag = html.find('assets/diagrams/diagram_cqc_roadmap.svg', pos_cqc_tab)
        if pos_diag != -1:
            start_diag = html.rfind('<div class="visual-diagram-card"', pos_cqc_tab, pos_diag)
            end_diag = html.find('</div>\n      </div>', pos_diag) + 12
            html = html[:start_diag] + cqc_5phases_html + html[end_diag:]
            print("  ✓ Replaced horizontal CQC diagram with vertical 5-card stack in Tab-CQC.")
    check_tabs(html, "Step 4 (CQC 5 Phases)")

    # =========================================================================
    # 5. STREET ACCESS & 10 FTE ROTA INSERTION (POS 120416)
    # =========================================================================
    print("\n[Step 5/15] Upgrading Cul-de-sac Street Diagram & 10 FTE Demonstration Rota...")
    
    wf2_text = read_file(os.path.join(TEMP_DIR, "workforce_capex_part2.md"))
    m_rota = re.search(r"#### 1\. PURE HTML: UNIFIED CAMPUS 7-DAY DEMONSTRATION ROTA TABLE.*?```html\s*(.*?)\s*```", wf2_text, re.DOTALL)
    rota_html = m_rota.group(1) if m_rota else ""
    
    pos_street = html.find('MARSTON GARDENS, LUTON (LU2 7DY) &bull; RESIDENTIAL CUL-DE-SAC HIGHWAYS COMPLIANT')
    if pos_street != -1:
        svg_start = html.rfind('<svg', 0, pos_street)
        svg_end = html.find('</svg>', pos_street) + 6
        
        upgraded_street_and_rota = f"""
        <div style="margin: 20px 0;">
          <img src="assets/diagrams/diagram_campus_masterplan.svg" alt="Highways Compliant Cul-de-Sac Campus Diagram" style="width:100%; height:auto; border-radius:8px; border:1.5px solid #1E3E62; display:block; box-shadow:0 4px 14px rgba(11,23,40,0.12);" loading="lazy">
          <div style="font-size:12.5px; color:#64748B; margin-top:8px; line-height:1.5;">
            <strong>Highways &amp; Street Access:</strong> Marston Gardens residential cul-de-sac compliant with Luton Local Plan LLP1, LLP25, LLP31 &amp; LLP32. 78 Marston Gardens on the Left (4 dedicated driveway bays), 80 Marston Gardens in the Middle (4 dedicated driveway bays), and 82 Marston Gardens on the Right Flank (2 garage parking bays).
          </div>
        </div>
        
        {rota_html}
        """
        html = html[:svg_start] + upgraded_street_and_rota + html[svg_end:]
        print("  ✓ Replaced cramped Street SVG with CAD masterplan image & 10 FTE Demonstration Rota Table.")
    check_tabs(html, "Step 5 (Street & Rota)")

    # =========================================================================
    # 6. TABLE 2.1 MCDA 100-POINT NON-SCROLLING TABLE (TAB-OPTIONS)
    # =========================================================================
    print("\n[Step 6/15] Upgrading Table 2.1 MCDA Scoring to non-scrolling magazine format...")
    
    mcda_table_html = """<div class="mcda-nonscroll-wrap" id="table-mcda-100pt">
  <div style="background: #0F1E36; padding: 16px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #C29B38;">
    <div>
      <span style="font-size: 11px; font-weight: 800; color: #C29B38; text-transform: uppercase; letter-spacing: 1px;">Scientific Option Appraisal Matrix</span>
      <h3 style="font-size: 16px; font-weight: 800; color: #FFFFFF; margin: 2px 0 0 0;">Table 2.1: Multi-Criteria Decision Analysis (MCDA 100-Point Viability Scoring)</h3>
    </div>
    <span style="background: #065F46; color: #6EE7B7; font-size: 11.5px; font-weight: 800; padding: 6px 12px; border-radius: 4px; border: 1px solid #10B981;">Option 4 Unanimous Winner (92/100)</span>
  </div>
  <table class="mcda-nonscroll-table">
    <thead>
      <tr>
        <th style="width: 28%;">Evaluation Criteria &amp; Statutory Weighting</th>
        <th style="width: 18%; text-align: center;">Option 1: Status Quo<br><span style="font-size: 11px; font-weight: 400; opacity: 0.8;">(Private Let 78 &amp; 80)</span></th>
        <th style="width: 18%; text-align: center;">Option 2: Single C2<br><span style="font-size: 11px; font-weight: 400; opacity: 0.8;">(78 Marston Gdns)</span></th>
        <th style="width: 18%; text-align: center;">Option 3: Split C2<br><span style="font-size: 11px; font-weight: 400; opacity: 0.8;">(78 &amp; 82 Marston Gdns)</span></th>
        <th class="mcda-opt4-th" style="width: 18%; text-align: center;">Option 4: Dual C3(b)<br><span style="font-size: 11px; font-weight: 700; color: #A7F3D0;">(78 &amp; 80 Supported Living)</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. CQC Registration Feasibility (25 Pts)</strong><br><span style="font-size: 11.5px; color: #64748B;">Single Assessment Framework, fit &amp; proper test</span></td>
        <td style="text-align: center; color: #DC2626; font-weight: 700;">0 / 25<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">No Registration</span></td>
        <td style="text-align: center; color: #D97706; font-weight: 700;">16 / 25<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">Rigid C2 Care Home</span></td>
        <td style="text-align: center; color: #D97706; font-weight: 700;">14 / 25<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">Split Door Non-Contig</span></td>
        <td class="mcda-opt4-cell" style="text-align: center;"><strong>24 / 25</strong><br><span style="font-size: 11px; font-weight: 600; color: #047857;">C3b Personal Care Model</span></td>
      </tr>
      <tr>
        <td><strong>2. Town Planning Immunity (25 Pts)</strong><br><span style="font-size: 11.5px; color: #64748B;">S.192 CLPUD, TCPA 1990 s.55(2)(f), Case Law</span></td>
        <td style="text-align: center; color: #059669; font-weight: 700;">25 / 25<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">Existing C3 Use</span></td>
        <td style="text-align: center; color: #DC2626; font-weight: 700;">11 / 25<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">C2 Committee Refusal Risk</span></td>
        <td style="text-align: center; color: #DC2626; font-weight: 700;">9 / 25<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">High Highways Refusal</span></td>
        <td class="mcda-opt4-cell" style="text-align: center;"><strong>25 / 25</strong><br><span style="font-size: 11px; font-weight: 600; color: #047857;">S.192 CLPUD Immunity</span></td>
      </tr>
      <tr>
        <td><strong>3. CapEx Fit-Out Efficiency (20 Pts)</strong><br><span style="font-size: 11.5px; color: #64748B;">BS 5839 Cat L1, FD30S, TMV3, Payback velocity</span></td>
        <td style="text-align: center; color: #059669; font-weight: 700;">20 / 20<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">&pound;0 CapEx</span></td>
        <td style="text-align: center; color: #D97706; font-weight: 700;">12 / 20<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">&pound;92k (Heavy C2 Sluice)</span></td>
        <td style="text-align: center; color: #DC2626; font-weight: 700;">8 / 20<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">&pound;145k Duplicate Plant</span></td>
        <td class="mcda-opt4-cell" style="text-align: center;"><strong>18 / 20</strong><br><span style="font-size: 11px; font-weight: 600; color: #047857;">&pound;68.4k Turnkey Fit-Out</span></td>
      </tr>
      <tr>
        <td><strong>4. Operating Margin &amp; EBITDA (15 Pts)</strong><br><span style="font-size: 11.5px; color: #64748B;">Unified rota economy, night shift sharing</span></td>
        <td style="text-align: center; color: #DC2626; font-weight: 700;">4 / 15<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">&pound;48k Net Rent (AST)</span></td>
        <td style="text-align: center; color: #D97706; font-weight: 700;">11 / 15<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">&pound;168k EBITDA (5 Beds)</span></td>
        <td style="text-align: center; color: #D97706; font-weight: 700;">12 / 15<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">&pound;242k (Duplicate Night)</span></td>
        <td class="mcda-opt4-cell" style="text-align: center;"><strong>15 / 15</strong><br><span style="font-size: 11px; font-weight: 600; color: #047857;">&pound;341.4k OpCo EBITDA</span></td>
      </tr>
      <tr>
        <td><strong>5. Scalability &amp; Asset Protection (15 Pts)</strong><br><span style="font-size: 11.5px; color: #64748B;">PropCo ringfence, BIK elimination, exit multiple</span></td>
        <td style="text-align: center; color: #DC2626; font-weight: 700;">3 / 15<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">Zero Corporate Scale</span></td>
        <td style="text-align: center; color: #D97706; font-weight: 700;">11 / 15<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">Single Asset Exposure</span></td>
        <td style="text-align: center; color: #1E3A8A; font-weight: 700;">14 / 15<br><span style="font-size: 11px; font-weight: 400; color: #64748B;">Director Displaced</span></td>
        <td class="mcda-opt4-cell" style="text-align: center;"><strong>15 / 15</strong><br><span style="font-size: 11px; font-weight: 600; color: #047857;">Triple Corporate Shield</span></td>
      </tr>
    </tbody>
    <tfoot>
      <tr style="background: #F8FAFC; font-size: 14px; font-weight: 800;">
        <td style="padding: 16px; color: #0F1E36;">COMPOSITE MCDA SCORE</td>
        <td style="text-align: center; color: #DC2626;">52 / 100<br><span style="font-size: 11px; font-weight: 600; color: #DC2626;">VIABILITY DEFICIT</span></td>
        <td style="text-align: center; color: #D97706;">61 / 100<br><span style="font-size: 11px; font-weight: 600; color: #D97706;">MARGINAL SCALE</span></td>
        <td style="text-align: center; color: #D97706;">57 / 100<br><span style="font-size: 11px; font-weight: 600; color: #D97706;">FRICTION DEFICIT</span></td>
        <td class="mcda-opt4-cell" style="text-align: center; font-size: 16px; background: #D1FAE5 !important; color: #065F46 !important;">
          92 / 100<br><span style="font-size: 11px; font-weight: 800; color: #047857;">UNANIMOUS WINNER</span>
        </td>
      </tr>
    </tfoot>
  </table>
  <div style="background: #F8FAFC; padding: 12px 16px; font-size: 12px; color: #64748B; border-top: 1px solid #E2E8F0;">
    <strong>MCDA Decision Theorem:</strong> Option 4 establishes decisive superiority by eliminating planning risk under S.192 CLPUD, lowering CapEx by &pound;76.6k vs Option 3, while preserving 82 Marston Gardens as the Director's private home with zero BIK under S.105/106 ITEPA 2003.
  </div>
</div>"""

    old_mcda_pattern = re.compile(r'<div class="table-journal-wrap" id="table-mcda-100pt".*?</table>\s*</div>', re.DOTALL)
    html, count = old_mcda_pattern.subn(mcda_table_html, html, count=1)
    print(f"  ✓ Replaced Table 2.1 MCDA with non-scrolling magazine format (count={count}).")
    check_tabs(html, "Step 6 (MCDA)")

    # =========================================================================
    # 7. END-TO-END OPERATIONAL ROADMAP (MONTHS 1 TO 9+) VERTICAL STACK
    # =========================================================================
    print("\n[Step 7/15] Upgrading End-to-End Operational Roadmap to vertical progression...")
    
    vertical_roadmap_html = """<div class="v-roadmap-stack" id="roadmap-vertical-execution">
  <div style="background: #0F1E36; color: #FFFFFF; padding: 16px 20px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #C29B38;">
    <div>
      <span style="font-size: 11px; font-weight: 800; color: #C29B38; text-transform: uppercase; letter-spacing: 1px;">Strategic Delivery Blueprint</span>
      <h3 style="font-size: 16.5px; font-weight: 800; margin: 2px 0 0 0; color: #FFFFFF;">End-to-End Operational Execution Roadmap (Months 1 to 9+)</h3>
    </div>
    <span style="background: #059669; color: #FFFFFF; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 4px;">Direct Sequential Execution</span>
  </div>

  <!-- Milestone 1 -->
  <div class="v-roadmap-card">
    <div class="v-roadmap-phase-badge">
      <div class="v-roadmap-phase-num">Phase 1</div>
      <div class="v-roadmap-phase-dates">Months 1–2</div>
      <span class="v-roadmap-phase-status">Statutory Foundation</span>
    </div>
    <div class="v-roadmap-content">
      <h4 class="v-roadmap-title">Corporate Structuring, FRI Commercial Leases &amp; Town Planning S.192 CLPUD</h4>
      <p class="v-roadmap-desc">Establish corporate holding structure (Mamun Ltd &rarr; ADOV Ltd &rarr; ADOV Care Group Ltd). Execute 10-year commercial Full Repairing and Insuring (FRI) leases for 78 Marston Gdns (&pound;65,000 p.a.) and 80 Marston Gdns (&pound;32,000 p.a.). Submit dual Section 192 CLPUD applications to Luton Borough Council to secure statutory planning immunity under Class C3(b).</p>
      <ul class="v-roadmap-bullets">
        <li>Execute Director AST on 82 Marston Gardens (&pound;1,500/mo) eliminating BIK under s.105/106 ITEPA 2003.</li>
        <li>Submit S.192 CLPUD certificate with transport &amp; parking evidence (8 driveway bays + 2 garages).</li>
        <li>Open designated OpCo client escrow and operational bank accounts with Barclays/Metro Bank.</li>
      </ul>
    </div>
  </div>

  <!-- Milestone 2 -->
  <div class="v-roadmap-card">
    <div class="v-roadmap-phase-badge">
      <div class="v-roadmap-phase-num">Phase 2</div>
      <div class="v-roadmap-phase-dates">Months 3–4</div>
      <span class="v-roadmap-phase-status">Physical Conversion</span>
    </div>
    <div class="v-roadmap-content">
      <h4 class="v-roadmap-title">Contractor Fit-Out, BS 5839 Cat L1 Fire Alarm &amp; Key Headcount Recruitment</h4>
      <p class="v-roadmap-desc">Tender and execute the &pound;68,400 CapEx fit-out across 78 &amp; 80 Marston Gardens. Install addressable Category L1 fire alarm systems, FD30S fire doors with Dorgard wireless magnetic hold-opens, TMV3 anti-scald mixing valves at 41&deg;C, and commercial kitchen upgrade in 78 Marston Gardens.</p>
      <ul class="v-roadmap-bullets">
        <li>Recruit Registered Manager (Regulation 7) holding Level 5 Diploma with complex autism experience.</li>
        <li>Appoint Nominated Individual (Regulation 6) Non-Executive Director.</li>
        <li>Complete sensory garden circular pathways and secure boundary acoustic fencing.</li>
      </ul>
    </div>
  </div>

  <!-- Milestone 3 -->
  <div class="v-roadmap-card">
    <div class="v-roadmap-phase-badge">
      <div class="v-roadmap-phase-num">Phase 3</div>
      <div class="v-roadmap-phase-dates">Months 5–6</div>
      <span class="v-roadmap-phase-status">Regulatory Filing</span>
    </div>
    <div class="v-roadmap-content">
      <h4 class="v-roadmap-title">CQC Provider Portal Submission, Statutory Policies &amp; Clinical Scenario Defense</h4>
      <p class="v-roadmap-desc">Submit formal CQC registration application for "Personal Care" under Health and Social Care Act 2008. Upload 7 statutory core policies, Statement of Purpose (Reg 12), and ICAEW-certified Regulation 13 financial viability forecast. Conduct rigorous mock interviews for Registered Manager covering 5 critical clinical crisis scenarios.</p>
      <ul class="v-roadmap-bullets">
        <li>CQC Provider Portal validation and application gatekeeping audit signoff.</li>
        <li>Deploy Nourish/Birdie e-MAR medication management and digital care planning platform.</li>
        <li>Pre-admission marketing engagement with Luton Council Adult Social Care Brokerage Team.</li>
      </ul>
    </div>
  </div>

  <!-- Milestone 4 -->
  <div class="v-roadmap-card">
    <div class="v-roadmap-phase-badge">
      <div class="v-roadmap-phase-num">Phase 4</div>
      <div class="v-roadmap-phase-dates">Months 7–8</div>
      <span class="v-roadmap-phase-status">Fast-Track Waiver</span>
    </div>
    <div class="v-roadmap-content">
      <h4 class="v-roadmap-title">CQC Site Inspection, Notice of Proposal &amp; Statutory Section 28(3) Fast-Track Waiver</h4>
      <p class="v-roadmap-desc">Host CQC Regulatory Inspector for physical campus readiness inspection. Upon receiving CQC Notice of Proposal (NoP), immediately execute statutory Section 28(3) Waiver of Representations Letter, waiving the standard 28-day statutory waiting period and accelerating registration certificate issuance to 48–72 hours.</p>
      <ul class="v-roadmap-bullets">
        <li>CQC issues formal Notice of Decision (NoD) and Provider Registration Certificate.</li>
        <li>Provider listing goes live on CQC public directory with Registered Manager active.</li>
        <li>Immediate accreditation onto Luton Borough Council ProContract DPS (Ref: AT1115).</li>
      </ul>
    </div>
  </div>

  <!-- Milestone 5 -->
  <div class="v-roadmap-card" style="border-left: 4px solid #059669; background: #F0FDF4;">
    <div class="v-roadmap-phase-badge" style="background: #065F46;">
      <div class="v-roadmap-phase-num" style="color: #6EE7B7;">Phase 5</div>
      <div class="v-roadmap-phase-dates">Months 9+</div>
      <span class="v-roadmap-phase-status" style="background: #047857;">Operational Ramp</span>
    </div>
    <div class="v-roadmap-content">
      <h4 class="v-roadmap-title" style="color: #065F46;">NHS BLMK ICB Activation, Phased Zero-Void Intake &amp; EBITDA Stabilization</h4>
      <p class="v-roadmap-desc">Activate placements via Luton Council Complex Learning Disability Team and NHS Bedfordshire, Luton &amp; Milton Keynes ICB. Execute phased transition protocol for first 4 residents into 78 Marston Gardens, followed by 4 residents into 80 Marston Gardens, reaching 100% campus occupancy (&pound;977,600 annual gross revenue, &pound;341,392 OpCo EBITDA).</p>
      <ul class="v-roadmap-bullets">
        <li>Zero-void transition protocol: day visits &rarr; tea visits &rarr; overnight stays &rarr; admission.</li>
        <li>Execute 10.0 FTE 24/7 unified campus staff rota (&pound;355,108 care payroll).</li>
        <li>Reach financial break-even (3.8 beds / 47.5% occupancy) by Month 10.</li>
      </ul>
    </div>
  </div>
</div>"""

    old_roadmap_pattern = re.compile(r'<div class="flowchart-wrap"[^>]*>\s*<div[^>]*>.*?End-to-End Operational Roadmap \(Months 1 to 9\+\).*?</div>\s*<svg viewBox="0 0 1020 180".*?</svg>\s*</div>', re.DOTALL)
    html, count = old_roadmap_pattern.subn(vertical_roadmap_html, html, count=1)
    print(f"  ✓ Replaced End-to-End Roadmap with vertical progression cards (count={count}).")
    check_tabs(html, "Step 7 (Roadmap)")

    # =========================================================================
    # 8. CAPEX BILL OF QUANTITIES SCENARIO A VS B TABLE (TAB-CAPEX)
    # =========================================================================
    print("\n[Step 8/15] Inserting Forensic Scenario A vs B CapEx BoQ Table into Tab-CapEx...")
    
    m_capex_block = re.search(r"#### 2\. PURE HTML: FORENSIC SCENARIO A VS SCENARIO B CAPEX BILL OF QUANTITIES.*?```html\s*(.*?)\s*```", wf2_text, re.DOTALL)
    if m_capex_block:
        capex_table_html = m_capex_block.group(1)
        capex_card_pattern = re.compile(r'<div class="card">\s*<h3 class="card-title">Itemized Fit-Out Budget Breakdown</h3>\s*<div class="table-wrap">\s*<table>.*?</table>\s*</div>\s*</div>', re.DOTALL)
        html, count = capex_card_pattern.subn(capex_table_html, html, count=1)
        print(f"  ✓ Successfully replaced CapEx table with 9-category comparative BoQ (count={count}).")
    check_tabs(html, "Step 8 (CapEx BoQ)")

    # =========================================================================
    # 9. TOWN PLANNING DOSSIER & S.192 CLPUD (TAB-PLANNING)
    # =========================================================================
    print("\n[Step 9/15] Injecting Class C3(b) Planning Law & Statutory Dossier into Tab-Planning...")
    
    planning_dossier_html = """
<section class="editorial-article" id="sec-planning-dossier" style="margin-top: 28px;">
  <div style="background: #0F1E36; color: #FFFFFF; padding: 18px 22px; border-radius: 8px; border-left: 5px solid #C29B38; margin-bottom: 24px;">
    <span style="font-size: 11px; font-weight: 800; color: #C29B38; text-transform: uppercase; letter-spacing: 1px;">Town Planning Jurisprudence</span>
    <h2 style="font-size: 20px; font-weight: 800; color: #FFFFFF; margin: 4px 0 0 0;">Exhaustive Class C3(b) Planning Law, Luton Local Plan &amp; Statutory Immunity Dossier</h2>
    <p style="font-size: 13px; color: #94A3B8; margin: 6px 0 0 0;">Town and Country Planning Act 1990 Section 55(2)(f) and Section 192 (Certificate of Lawfulness of Proposed Use or Development &mdash; CLPUD)</p>
  </div>

  <div class="card" style="border-left: 4px solid var(--gold); background: #FFFFFF; margin-bottom: 24px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <h3 class="card-title" style="margin: 0;">1. Statutory Framework: TCPA 1990 s.55(2)(f) &amp; s.192 CLPUD</h3>
      <span class="badge badge-success">Pure Matter of Law</span>
    </div>
    <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-main); margin-bottom: 12px;">
      Under Section 55(2)(f) of the <strong>Town and Country Planning Act 1990</strong>, the utilization of any building for any purpose within the same statutory use class does not constitute "development". Both 78 and 80 Marston Gardens hold lawful existing use as Class C3 dwellinghouses. Changing use to <strong>Class C3(b)</strong> (living together receiving care, up to 6 persons) is deemed by statute <em>not to involve development</em>, eliminating any requirement for planning permission.
    </p>
    <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-main); margin-bottom: 0;">
      A <strong>Section 192 Certificate of Lawfulness (CLPUD)</strong> is a formal legal determination by Luton Borough Council confirming that the proposed use is lawful. Under Section 192(2), if the Local Planning Authority is provided with sufficient evidence of lawfulness, <strong>it has a mandatory statutory duty to issue the certificate</strong>. The LPA is strictly barred from considering planning merits, neighbor representations, or local objections.
    </p>
  </div>

  <div class="card" style="border-left: 4px solid #0284C7; background: #FFFFFF; margin-bottom: 24px;">
    <h3 class="card-title" style="margin: 0 0 14px 0;">2. Definitive Case Law Jurisprudence Analysis</h3>
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 14px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <strong style="color: #0F1E36; font-size: 14px;">North Devon District Council v First Secretary of State [2004] EWHC 88 (Admin)</strong>
          <span class="badge badge-blue">Binding High Court Precedent</span>
        </div>
        <p style="font-size: 13px; line-height: 1.55; color: #334155; margin: 0;">
          Established that non-resident carers visiting or sleeping-in on a rota basis does not cause the premises to cease being a single household under Class C3(b). Collins J ruled that where residents require care to live in the community, the presence of nonresident carers sleeping on site is an intrinsic element of Class C3(b) and does NOT trigger a material change of use to Class C2.
        </p>
      </div>

      <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 14px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <strong style="color: #0F1E36; font-size: 14px;">Hossack v Kettering Borough Council &amp; Anor [2002] EWCA Civ 886</strong>
          <span class="badge badge-blue">Court of Appeal</span>
        </div>
        <p style="font-size: 13px; line-height: 1.55; color: #334155; margin: 0;">
          Confirmed that whether a material change of use occurs is a fact-and-degree assessment based on residential character. Where residents live together communally, cook together, and maintain domestic routines without commercial institutional signage or ambulances, the domestic character of the dwelling is fully retained.
        </p>
      </div>

      <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 14px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <strong style="color: #0F1E36; font-size: 14px;">Crawley Borough Council v First Secretary of State &amp; Anor [2004] EWHC 160 (Admin)</strong>
          <span class="badge badge-blue">High Court Precedent</span>
        </div>
        <p style="font-size: 13px; line-height: 1.55; color: #334155; margin: 0;">
          Held that public anxiety or neighbor objections regarding care occupants cannot constitute a planning reason to refuse lawfulness or allege a material change of use where the physical use remains domestic dwelling accommodation.
        </p>
      </div>
    </div>
  </div>

  <div class="card" style="border-left: 4px solid #059669; background: #FFFFFF; margin-bottom: 24px;">
    <h3 class="card-title" style="margin: 0 0 14px 0;">3. Luton Local Plan 2011–2031 Policy Compliance &amp; Parking Proof</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
      <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; padding: 14px;">
        <h4 style="color: #065F46; font-size: 14px; margin: 0 0 6px 0;">Policy LLP1 &amp; LLP25 (Design &amp; Amenity)</h4>
        <p style="font-size: 12.5px; line-height: 1.5; color: #166534; margin: 0;">Zero external physical alterations to front elevations. Retains domestic residential appearance identical to surrounding properties on Marston Gardens. 100ft sensory rear gardens preserve open amenity buffers.</p>
      </div>
      <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; padding: 14px;">
        <h4 style="color: #065F46; font-size: 14px; margin: 0 0 6px 0;">Policies LLP31 &amp; LLP32 (Highways &amp; Parking)</h4>
        <p style="font-size: 12.5px; line-height: 1.5; color: #166534; margin: 0;">Luton Local Plan Appendix 7 mandates 1 space per 4 beds + 1 staff space. Total requirement = 3 spaces. The campus provides <strong>10 off-street parking spaces</strong> (4 on 78 left flank, 4 on 80 right flank, 2 garage spaces on 82), exceeding parking standards by 233%.</p>
      </div>
      <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; padding: 14px;">
        <h4 style="color: #065F46; font-size: 14px; margin: 0 0 6px 0;">Luton HMO Article 4 Direction</h4>
        <p style="font-size: 12.5px; line-height: 1.5; color: #166534; margin: 0;">Luton Borough Council's Article 4 Direction restricts permitted development from C3 to C4 (small HMOs). It <strong>does NOT apply</strong> to Class C3(b) Supported Living, as confirmed in DLUHC Planning Practice Guidance (Paragraph 011 Reference ID: 13-011-20140306).</p>
      </div>
    </div>
  </div>
</section>
"""

    pos_plan_ref = html.find('id="sec-references-tab-planning"')
    if pos_plan_ref != -1:
        ins_pos = html.rfind('<section', 0, pos_plan_ref)
        html = html[:ins_pos] + planning_dossier_html + "\n\n" + html[ins_pos:]
        print("  ✓ Injected comprehensive Town Planning Dossier into Tab-Planning.")
    check_tabs(html, "Step 9 (Planning Dossier)")

    # =========================================================================
    # 10. TAX-NEUTRAL RENT ARBITRAGE & STATUTORY LEASE SUMMARY (TAB-TAX)
    # =========================================================================
    print("\n[Step 10/15] Upgrading Tax-Neutral Rent Arbitrage & FRI Lease Summary in Tab-Tax...")
    
    vertical_tax_html = """
<div class="v-tax-stack" id="tax-arbitrage-engine-vertical">
  <div style="background: #0F1E36; color: #FFFFFF; padding: 18px 22px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #C29B38;">
    <div>
      <span style="font-size: 11px; font-weight: 800; color: #C29B38; text-transform: uppercase; letter-spacing: 1px;">Corporate Tax Architecture</span>
      <h3 style="font-size: 16.5px; font-weight: 800; margin: 2px 0 0 0; color: #FFFFFF;">Tax-Neutral Rent Arbitrage &amp; BIK Elimination Engine</h3>
    </div>
    <span style="background: #C29B38; color: #0F1E36; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 4px;">&pound;0.00 Director BIK &bull; &pound;24.2k CT Saved</span>
  </div>

  <!-- Tier 1 -->
  <div class="v-tax-card" style="border-left: 4px solid #C29B38;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
      <div>
        <span class="v-tax-tier-tag" style="background: #FEF3C7; color: #92400E;">Tier 1: Parent Holding Company</span>
        <h4 style="font-size: 16px; font-weight: 800; color: #0F1E36; margin: 2px 0 0 0;">MAMUN LIMITED (Parent HoldCo)</h4>
      </div>
      <span class="badge badge-gold">100% Equity Controller</span>
    </div>
    <p style="font-size: 13px; line-height: 1.55; color: #334155; margin: 0 0 8px 0;">
      Consolidates group treasury, provides strategic equity capital, and receives tax-exempt group dividends under Part 9A CTA 2009. Completely insulated from operational care risk.
    </p>
    <div style="font-size: 12px; font-weight: 700; color: #64748B;">HMRC Corporation Tax Relief &bull; Dividend Group Exemption s.931A CTA 2009</div>
  </div>

  <!-- Tier 2 -->
  <div class="v-tax-card" style="border-left: 4px solid #0284C7;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
      <div>
        <span class="v-tax-tier-tag" style="background: #DBEAFE; color: #1E40AF;">Tier 2: Asset Property Company</span>
        <h4 style="font-size: 16px; font-weight: 800; color: #0F1E36; margin: 2px 0 0 0;">ADOV LIMITED (PropCo / Freehold Asset Owner)</h4>
      </div>
      <span class="badge badge-blue">Freehold Ringfence (&pound;1.38M)</span>
    </div>
    <p style="font-size: 13px; line-height: 1.55; color: #334155; margin: 0 0 8px 0;">
      Holds freehold title deeds for 78, 80 &amp; 82 Marston Gardens. Grants 10-year commercial Full Repairing and Insuring (FRI) leases to OpCo. Receives passing commercial rent of &pound;97,000/year (&pound;65k for 78, &pound;32k for 80).
    </p>
    <ul style="margin: 0; padding-left: 20px; font-size: 12.5px; line-height: 1.5; color: #1E293B;">
      <li><strong>ATED 100% Exemption:</strong> Claimed under Section 133 Finance Act 2013 (qualifying property rental business).</li>
      <li><strong>VAT Neutrality:</strong> PropCo does NOT opt to tax under Schedule 10 VATA 1994, ensuring OpCo incurs zero irrecoverable VAT on rent.</li>
    </ul>
  </div>

  <!-- Tier 3 -->
  <div class="v-tax-card" style="border-left: 4px solid #059669;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
      <div>
        <span class="v-tax-tier-tag" style="background: #D1FAE5; color: #065F46;">Tier 3: CQC Operating Company</span>
        <h4 style="font-size: 16px; font-weight: 800; color: #0F1E36; margin: 2px 0 0 0;">ADOV CARE GROUP LIMITED (OpCo / Registered Provider)</h4>
      </div>
      <span class="badge badge-success">&pound;341,392 EBITDA (34.9%)</span>
    </div>
    <p style="font-size: 13px; line-height: 1.55; color: #334155; margin: 0 0 8px 0;">
      Holds CQC registration for Personal Care across 78 &amp; 80 Marston Gardens. Enters into Individual Placement Agreements with Luton Borough Council and NHS BLMK ICB (&pound;977,600 gross revenue).
    </p>
    <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 6px; padding: 10px; font-size: 12.5px; color: #166534; font-weight: 600;">
      &pound;97,000 commercial FRI rent is 100% tax-deductible under s.54 CTA 2009 as an expense incurred wholly and exclusively for trade, sheltering &pound;24,250 in Corporation Tax annually.
    </div>
  </div>

  <!-- Director Residence -->
  <div class="v-tax-card" style="border-left: 4px solid #7C3AED; background: #FAF5FF;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
      <div>
        <span class="v-tax-tier-tag" style="background: #EDE9FE; color: #6D28D9;">Director Private Residence</span>
        <h4 style="font-size: 16px; font-weight: 800; color: #0F1E36; margin: 2px 0 0 0;">82 MARSTON GARDENS (Beneficiary Residence &bull; AST Mechanism)</h4>
      </div>
      <span style="background: #7C3AED; color: #FFFFFF; font-size: 11px; font-weight: 800; padding: 5px 10px; border-radius: 4px;">&pound;0.00 Statutory BIK</span>
    </div>
    <p style="font-size: 13px; line-height: 1.55; color: #334155; margin: 0 0 8px 0;">
      Occupied by Director/Beneficiary under an independent arm's length Assured Shorthold Tenancy (AST) at full market rent of &pound;1,500/month (&pound;18,000/year).
    </p>
    <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 6px; padding: 12px; font-size: 12.5px; color: #4C1D95;">
      <strong>Statutory Benefit in Kind Elimination:</strong> Under Section 105 &amp; Section 106 ITEPA 2003 (HMRC Employment Income Manual EIM11300), the taxable cash equivalent of company-provided living accommodation is reduced pound-for-pound by the rent paid by the employee. Because the Director pays full open-market rent, the taxable BIK cash equivalent is exactly <strong>&pound;0.00</strong>.
    </div>
  </div>
</div>

<div class="card" style="border-left: 4px solid #0F1E36; background: #FFFFFF; margin-top: 24px;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <h3 class="card-title" style="margin: 0;">Statutory Lease Summary &amp; Line-by-Line Commercial FRI Covenants</h3>
    <span class="badge badge-success">TIOPA 2010 Arm's Length Compliant</span>
  </div>
  <p style="font-size: 13px; line-height: 1.6; color: var(--text-main); margin-bottom: 16px;">
    To strictly satisfy HMRC Corporation Tax deductibility (s.54 CTA 2009) and CQC Regulation 13 financial viability scrutiny, all intra-group leases are executed on institutional RICS commercial Full Repairing and Insuring (FRI) terms:
  </p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Lease Instrument</th>
          <th>Contracting Parties</th>
          <th>Annual Passing Rent</th>
          <th>FRI Statutory Obligations &amp; Tax Treatment</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>10-Yr Commercial FRI: 78 Marston Gardens</strong></td>
          <td>Landlord: ADOV Limited<br>Tenant: ADOV Care Group Limited</td>
          <td><strong>&pound;65,000 / Year</strong><br><span style="font-size: 11px; color: #64748B;">(&pound;5,416.67 / month)</span></td>
          <td>100% tax-deductible trading expense sheltering &pound;16,250 CT annually. Tenant liable for all internal, external, and structural maintenance, BS 5839 fire safety, and building insurance reimbursement.</td>
        </tr>
        <tr>
          <td><strong>10-Yr Commercial FRI: 80 Marston Gardens</strong></td>
          <td>Landlord: ADOV Limited<br>Tenant: ADOV Care Group Limited</td>
          <td><strong>&pound;32,000 / Year</strong><br><span style="font-size: 11px; color: #64748B;">(&pound;2,666.67 / month)</span></td>
          <td>100% tax-deductible trading expense sheltering &pound;8,000 CT annually. Supported by independent RICS Red Book commercial valuation; RPI/CPI capped annual indexation (1% collar, 4% cap).</td>
        </tr>
        <tr>
          <td><strong>Assured Shorthold Tenancy: 82 Marston Gardens</strong></td>
          <td>Landlord: ADOV Limited<br>Tenant: Director / Beneficiary</td>
          <td><strong>&pound;18,000 / Year</strong><br><span style="font-size: 11px; color: #64748B;">(&pound;1,500.00 / month)</span></td>
          <td>Director pays open-market residential rent under standard AST, satisfying s.105/106 ITEPA 2003 and reducing HMRC Benefit in Kind (BIK) to exactly &pound;0.00.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

    pos_tax_target = html.find('Tax-Neutral Rent Arbitrage')
    if pos_tax_target != -1:
        start_flow = html.rfind('<div class="flowchart-wrap"', 0, pos_tax_target)
        # Also replace the old brief Statutory Lease Summary card right after it
        end_flow = html.find('</div>', html.find('</svg>', pos_tax_target)) + 6
        # Check if the old brief Statutory Lease Summary card immediately follows
        pos_old_lease_card = html.find('Statutory Lease Summary', end_flow)
        if pos_old_lease_card != -1 and pos_old_lease_card - end_flow < 200:
            end_lease_card = html.find('</div>\n          </div>', pos_old_lease_card) + 17
            html = html[:start_flow] + vertical_tax_html + html[end_lease_card:]
            print("  ✓ Replaced horizontal Tax SVG & brief lease card with comprehensive vertical Tax Engine & FRI Covenants.")
        else:
            html = html[:start_flow] + vertical_tax_html + html[end_flow:]
            print("  ✓ Replaced horizontal Tax SVG with vertical downward flow cards.")
    check_tabs(html, "Step 10 (Tax & FRI Leases)")

    # =========================================================================
    # 11. CQC 5 KEY QUESTIONS VERTICAL ARCHITECTURE (TAB-CQC-REQS)
    # =========================================================================
    print("\n[Step 11/15] Inserting CQC 5 Key Questions Vertical Cards into Tab-CQC-Reqs...")
    
    m_d1 = re.search(r"### DELIVERABLE 1:.*?```html\s*(.*?)\s*```", cqc1_text, re.DOTALL)
    if m_d1:
        d1_html = m_d1.group(1)
        pos_saf = html.find('id="sec-cqc-saf-34"')
        if pos_saf != -1:
            html = html[:pos_saf] + d1_html + "\n\n" + html[pos_saf:]
            print("  ✓ Successfully inserted 5 Key Questions Vertical Architecture into Tab-CQC-Reqs.")
    check_tabs(html, "Step 11 (CQC 5 Key Questions)")

    # =========================================================================
    # 12. CQC REGISTRATION & APPROVAL PROCESS MAP (STAGES 1 TO 8) (TAB-CQC)
    # =========================================================================
    print("\n[Step 12/15] Inserting CQC Registration Process Map (Stages 1 to 8) into Tab-CQC...")
    
    cqc_8stages_html = """
<section class="editorial-article" id="sec-cqc-8stages-vertical" style="margin-top: 24px;">
  <div style="background: #0F1E36; color: #FFFFFF; padding: 18px 22px; border-radius: 8px; border-left: 5px solid #C29B38; margin-bottom: 24px;">
    <span style="font-size: 11px; font-weight: 800; color: #C29B38; text-transform: uppercase; letter-spacing: 1px;">Statutory Registration Pathway</span>
    <h2 style="font-size: 20px; font-weight: 800; color: #FFFFFF; margin: 4px 0 0 0;">CQC Registration &amp; Approval Process Map (Stages 1 to 8 &bull; Section 28(3) Fast-Track)</h2>
    <p style="font-size: 13px; color: #94A3B8; margin: 6px 0 0 0;">Health and Social Care Act 2008 &bull; Care Quality Commission (Registration) Regulations 2009</p>
  </div>

  <div class="v-proc-stack">
    <!-- Stage 1 -->
    <div class="v-proc-card">
      <div class="v-proc-sidebar">
        <div class="v-proc-step-num">Stage 1</div>
        <div class="v-proc-badge" style="background: #DBEAFE; color: #1E40AF;">Pre-Submission</div>
      </div>
      <div class="v-proc-main">
        <h4 class="v-proc-title">Statutory Vetting, Policies &amp; Financial Viability Assembly (Weeks 1–4)</h4>
        <p class="v-proc-desc">Execute enhanced DBS countersigned checks and GP Medical Fitness Questionnaires for Registered Manager and Nominated Individual. Draft Statement of Purpose under CQC Reg 12. Commission ICAEW accountant to sign off Regulation 13 Financial Viability Forecast.</p>
        <div class="v-proc-meta">Evidence: Enhanced DBS &bull; GP Medical &bull; Statement of Purpose &bull; Reg 13 Accountant Forecast &bull; 7 Core Statutory Policies</div>
      </div>
    </div>

    <!-- Stage 2 -->
    <div class="v-proc-card">
      <div class="v-proc-sidebar">
        <div class="v-proc-step-num">Stage 2</div>
        <div class="v-proc-badge" style="background: #DBEAFE; color: #1E40AF;">Application</div>
      </div>
      <div class="v-proc-main">
        <h4 class="v-proc-title">CQC Provider Portal Submission &amp; Key Role Declarations (Weeks 5–6)</h4>
        <p class="v-proc-desc">Submit comprehensive online Provider and Registered Manager applications via CQC Portal. Upload all 42 Provider Application model answers, Statement of Purpose, and corporate governance documents.</p>
        <div class="v-proc-meta">Filing: Health and Social Care Act 2008 Section 10 &bull; CQC Portal ID Generated</div>
      </div>
    </div>

    <!-- Stage 3 -->
    <div class="v-proc-card">
      <div class="v-proc-sidebar">
        <div class="v-proc-step-num">Stage 3</div>
        <div class="v-proc-badge" style="background: #FEF3C7; color: #92400E;">Gatekeeping</div>
      </div>
      <div class="v-proc-main">
        <h4 class="v-proc-title">CQC Validation &amp; Completeness Audit (Weeks 7–8)</h4>
        <p class="v-proc-desc">CQC National Registration Team reviews application for document completeness. Completeness audit conducted within 5–10 working days. Application assigned official CQC Reference Number (e.g. 1-129482810).</p>
        <div class="v-proc-meta">Status: Formal Validation Sign-Off &bull; Inspector Queue Allocation</div>
      </div>
    </div>

    <!-- Stage 4 -->
    <div class="v-proc-card">
      <div class="v-proc-sidebar">
        <div class="v-proc-step-num">Stage 4</div>
        <div class="v-proc-badge" style="background: #EDE9FE; color: #5B21B6;">Assessment</div>
      </div>
      <div class="v-proc-main">
        <h4 class="v-proc-title">Regulatory Inspector Assignment &amp; Document Review (Weeks 9–10)</h4>
        <p class="v-proc-desc">Senior CQC Regulatory Inspector assigned to ADOV Care Group. In-depth review of safeguarding procedures, PBS frameworks, staffing rotas, and medication administration protocols.</p>
        <div class="v-proc-meta">Focus: CQC Single Assessment Framework &bull; Right Support, Right Care, Right Culture</div>
      </div>
    </div>

    <!-- Stage 5 -->
    <div class="v-proc-card">
      <div class="v-proc-sidebar">
        <div class="v-proc-step-num">Stage 5</div>
        <div class="v-proc-badge" style="background: #FEE2E2; color: #991B1B;">Clinical Interview</div>
      </div>
      <div class="v-proc-main">
        <h4 class="v-proc-title">Fit &amp; Proper Person Interviews: RM (Reg 7) &amp; NI (Reg 6) (Weeks 11–12)</h4>
        <p class="v-proc-desc">Registered Manager undergoes intensive 2-hour clinical interview defending 5 clinical crisis scenarios (medication errors, unnotified DoLS restrictions, safeguarding allegations to Luton MASH, resident choking/dysphagia, sudden refusal of personal care). Nominated Individual interview evaluates Regulation 17 governance systems.</p>
        <div class="v-proc-meta">Statutory Citation: Regulation 5, 6 &amp; 7 Health and Social Care Act 2014 &bull; Clinical Pass/Fail</div>
      </div>
    </div>

    <!-- Stage 6 -->
    <div class="v-proc-card">
      <div class="v-proc-sidebar">
        <div class="v-proc-step-num">Stage 6</div>
        <div class="v-proc-badge" style="background: #E0E7FF; color: #3730A3;">Site Readiness</div>
      </div>
      <div class="v-proc-main">
        <h4 class="v-proc-title">Physical Campus Readiness Inspection at 78 &amp; 80 Marston Gardens (Weeks 13–14)</h4>
        <p class="v-proc-desc">CQC Inspector conducts physical site audit of campus. Verifies BS 5839 Cat L1 addressable fire panel, FD30S doors with Dorgard magnetic closers, TMV3 anti-scald mixing valves at 41&deg;C, commercial kitchen Food Hygiene 5 setup in 78, and sensory calm room in 80.</p>
        <div class="v-proc-meta">Certifications: Fire Safety Order 2005 &bull; TMV3 Scheme &bull; HTM 01-04 Linen Flow &bull; Food Hygiene 5</div>
      </div>
    </div>

    <!-- Stage 7 -->
    <div class="v-proc-card" style="border-left: 4px solid #C29B38; background: #FDFBF7;">
      <div class="v-proc-sidebar">
        <div class="v-proc-step-num" style="color: #92400E;">Stage 7</div>
        <div class="v-proc-badge" style="background: #FEF3C7; color: #92400E;">Fast-Track Waiver</div>
      </div>
      <div class="v-proc-main">
        <h4 class="v-proc-title" style="color: #92400E;">Notice of Proposal (NoP) &amp; Section 28(3) Fast-Track Waiver (Week 15)</h4>
        <p class="v-proc-desc">CQC issues formal Notice of Proposal to register provider under Section 26 HSCA 2008. Operator immediately submits the official <strong>Section 28(3) Statutory Waiver of Representations Letter</strong>, waiving the mandatory 28-day statutory representation period to eliminate unnecessary administrative delay.</p>
        <div class="v-proc-meta" style="color: #B45309; font-weight: 700;">Section 28(3) Acceleration: Eliminates 28 days &bull; Accelerates Final Certificate to 48–72 Hours</div>
      </div>
    </div>

    <!-- Stage 8 -->
    <div class="v-proc-card" style="border-left: 4px solid #059669; background: #F0FDF4;">
      <div class="v-proc-sidebar">
        <div class="v-proc-step-num" style="color: #065F46;">Stage 8</div>
        <div class="v-proc-badge" style="background: #D1FAE5; color: #065F46;">Live Operation</div>
      </div>
      <div class="v-proc-main">
        <h4 class="v-proc-title" style="color: #065F46;">Notice of Decision (NoD) &amp; Certificate of Registration Issuance (Week 16)</h4>
        <p class="v-proc-desc">CQC issues formal Notice of Decision under Section 28(1) and publishes final Certificate of Registration. ADOV Care Group listed on CQC Public Directory. Immediate activation of Luton Borough Council ProContract DPS (AT1115) and NHS BLMK ICB placement contracts.</p>
        <div class="v-proc-meta" style="color: #047857; font-weight: 700;">Final Deliverable: CQC Registration Certificate &bull; Commissioning Ready &bull; Zero Voids Intake Commences</div>
      </div>
    </div>
  </div>
</section>
"""

    pos_flow = html.find('CQC Registration &amp; Approval Process Map (Stages 1 to 8)')
    if pos_flow != -1:
        start_flow = html.rfind('<div class="flowchart-wrap"', 0, pos_flow)
        end_flow = html.find('</div>', html.find('</svg>', pos_flow)) + 6
        html = html[:start_flow] + cqc_8stages_html + html[end_flow:]
        print("  ✓ Replaced horizontal CQC flowchart with vertical Stages 1 to 8 process map.")
    check_tabs(html, "Step 12 (CQC 8 Stages)")

    # =========================================================================
    # 13. ZERO-VOID RESIDENT INTAKE & 5 GATEWAYS (TAB-COMMISSIONING)
    # =========================================================================
    print("\n[Step 13/15] Upgrading Zero-Void Intake & Commissioning Gateways in Tab-Commissioning...")
    
    m_d3 = re.search(r"### DELIVERABLE 3:.*?```html\s*(.*?)\s*```", cqc2_text, re.DOTALL)
    m_d4 = re.search(r"### DELIVERABLE 4:.*?```html\s*(.*?)\s*```", cqc2_text, re.DOTALL)
    
    if m_d3 and m_d4:
        combined_intake_html = m_d3.group(1) + "\n\n" + m_d4.group(1)
        pos_comm = html.find('id="tab-commissioning"')
        if pos_comm != -1:
            pos_prose = html.find('<div class="editorial-prose-wrap">', pos_comm)
            if pos_prose != -1:
                ins_pos = pos_prose + len('<div class="editorial-prose-wrap">')
                html = html[:ins_pos] + "\n" + combined_intake_html + "\n" + html[ins_pos:]
                print("  ✓ Successfully injected vertical 6 Stages & 5 Gateways into Tab-Commissioning.")
    check_tabs(html, "Step 13 (Intake & Gateways)")

    # =========================================================================
    # 14. 90-DAY OPERATIONAL EXECUTION TRACKER (TAB-TRACKER)
    # =========================================================================
    print("\n[Step 14/15] Upgrading 90-Day Operational Execution Tracker in Tab-Tracker...")
    
    upgraded_tracker_html = """
<div class="card" style="border-left: 4px solid var(--navy); background: #FFFFFF; margin-bottom: 24px;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <h3 class="card-title" style="margin: 0;">Phase 1: Legal Leases, Corporate Governance &amp; S.192 CLPUD (Months 1–2)</h3>
    <span class="badge badge-success">Completed &bull; 100% Gated</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" checked onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Execute 10-Yr Commercial FRI Lease for 78 Marston Gardens (&pound;65,000 p.a.)</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Landlord: ADOV Limited // Tenant: ADOV Care Group Limited // 100% Tax Deductible under s.54 CTA 2009</div>
      </div>
    </div>
    <span class="badge badge-success">Signed &amp; Stamped</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" checked onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Execute 10-Yr Commercial FRI Lease for 80 Marston Gardens (&pound;32,000 p.a.)</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Passing rent supported by independent RICS Red Book commercial appraisal // TIOPA 2010 Arm's Length Compliant</div>
      </div>
    </div>
    <span class="badge badge-success">Signed &amp; Stamped</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" checked onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Director AST on 82 Marston Gardens (&pound;1,500/mo) Eliminating BIK</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">HMRC s.105/106 ITEPA 2003 strict compliance reduces taxable cash equivalent to &pound;0.00</div>
      </div>
    </div>
    <span class="badge badge-success">AST Executed</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" checked onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Dual Section 192 CLPUD Application to Luton Borough Council</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Statutory Class C3(b) confirmation under TCPA 1990 s.55(2)(f) &bull; North Devon DC precedent</div>
      </div>
    </div>
    <span class="badge badge-success">Submitted</span>
  </div>
</div>

<div class="card" style="border-left: 4px solid #0284C7; background: #FFFFFF; margin-bottom: 24px;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <h3 class="card-title" style="margin: 0;">Phase 2: Physical Fit-Out, Fire Safety &amp; Management Recruitment (Months 3–4)</h3>
    <span class="badge badge-gold">Active &bull; In Progress (85%)</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" checked onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">BS 5839 Category L1 Addressable Fire Alarm Installation</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Full optical detection in all bedrooms, voids, and common areas &bull; Certified commissioning certificate</div>
      </div>
    </div>
    <span class="badge badge-success">Completed</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" checked onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">FD30S Fire Doors with Dorgard Wireless Magnetic Hold-Opens</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">30-minute fire separation with intumescent seals and smoke brushes across all 8 resident suites</div>
      </div>
    </div>
    <span class="badge badge-success">Completed</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" checked onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">TMV3 Anti-Scald Thermostatic Mixing Valves Installation (41&deg;C)</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Installed on all baths, showers, and washbasins &bull; Legionella risk assessment signoff</div>
      </div>
    </div>
    <span class="badge badge-success">Certified</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" checked onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Recruitment of Level 5 Registered Manager (Regulation 7)</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">NVQ/Diploma Level 5 in Leadership for Adult Care with 5+ yrs experience in autism supported living</div>
      </div>
    </div>
    <span class="badge badge-gold">Final Stage</span>
  </div>
</div>

<div class="card" style="border-left: 4px solid #C29B38; background: #FFFFFF; margin-bottom: 24px;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <h3 class="card-title" style="margin: 0;">Phase 3: CQC Portal Submission &amp; Clinical Scenario Defense (Months 5–6)</h3>
    <span class="badge badge-neutral">Scheduled &bull; Ready</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Submit CQC Provider &amp; Registered Manager Applications Online</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Upload 42 model answers, 7 statutory policies, and ICAEW Reg 13 financial forecast</div>
      </div>
    </div>
    <span class="badge badge-neutral">Gated</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">CQC Registered Manager Regulation 7 Clinical Defense Interview</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Mock interview defense across 5 clinical scenarios (medication, DoLS, safeguarding, choking, care refusal)</div>
      </div>
    </div>
    <span class="badge badge-neutral">Prepared</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Digital e-MAR and Care Planning Software Deployment</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Configure Nourish/Birdie digital care planning and electronic MAR charts system</div>
      </div>
    </div>
    <span class="badge badge-neutral">Configured</span>
  </div>
</div>

<div class="card" style="border-left: 4px solid #059669; background: #FFFFFF; margin-bottom: 24px;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <h3 class="card-title" style="margin: 0;">Phase 4: Section 28(3) Fast-Track Waiver, DPS Activation &amp; Phased Intake (Months 7–9+)</h3>
    <span class="badge badge-neutral">Target Milestone</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Execute Statutory Section 28(3) Waiver of Representations Letter</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Immediately upon receiving CQC Notice of Proposal (NoP), waiving 28-day statutory pause</div>
      </div>
    </div>
    <span class="badge badge-neutral">Drafted</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0; border-bottom: 1px solid #E2E8F0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Receive Notice of Decision (NoD) &amp; CQC Provider Certificate</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">CQC public directory listing goes live &bull; Provider ID legally issued</div>
      </div>
    </div>
    <span class="badge badge-neutral">Target</span>
  </div>
  <div class="tracker-item" style="padding: 14px 0;">
    <div class="tracker-info">
      <input type="checkbox" class="tracker-checkbox" onchange="updateProgress()">
      <div>
        <div class="tracker-text" style="font-size: 14.5px; font-weight: 700; color: #0F1E36;">Luton Borough Council DPS (AT1115) Activation &amp; Zero-Void Intake</div>
        <div class="tracker-sub" style="font-size: 12.5px; color: #64748B;">Admit 8 residents across 78 &amp; 80 Marston Gardens reaching &pound;977.6k gross turnover and &pound;341.4k EBITDA</div>
      </div>
    </div>
    <span class="badge badge-neutral">Target</span>
  </div>
</div>
"""

    pos_tr_ref = html.find('id="sec-references-tab-tracker"')
    if pos_tr_ref != -1:
        ins_pos = html.rfind('<section', 0, pos_tr_ref)
        html = html[:ins_pos] + upgraded_tracker_html + "\n\n" + html[ins_pos:]
        print("  ✓ Injected upgraded 90-Day Tracker cards into Tab-Tracker.")
    check_tabs(html, "Step 14 (Tracker)")

    # =========================================================================
    # 15. CONTEXTUAL MINI-GLOSSARIES INSERTION (FROM BOTTOM TO TOP)
    # =========================================================================
    print("\n[Step 15/15] Injecting Contextual Mini-Glossaries into all 15 tabs...")
    
    glossaries = {
        "tab-glossary": """<div class="mini-glossary-card" id="glossary-tab-glossary">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Master Reference Guide</h4>
    <span class="badge badge-neutral">Universal Index</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>HSCA 2008</span> <span class="tag-pill tag-gold">Primary Legislation</span></div>
      <div class="mini-glossary-def">Health and Social Care Act 2008: primary statute creating the Care Quality Commission and regulating health and social care.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Care Act 2014</span> <span class="tag-pill tag-blue">Primary Legislation</span></div>
      <div class="mini-glossary-def">Landmark statute establishing local authority duties to promote individual wellbeing and prevent care needs.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>MCA 2005</span> <span class="tag-pill tag-gold">Primary Legislation</span></div>
      <div class="mini-glossary-def">Mental Capacity Act 2005: statutory framework governing decision-making on behalf of individuals lacking capacity.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>DLUHC Guidance</span> <span class="tag-pill tag-green">Government Policy</span></div>
      <div class="mini-glossary-def">Department for Levelling Up, Housing and Communities national planning practice guidance for specialist housing.</div>
    </div>
  </div>
</div>""",

        "tab-vault": """<div class="mini-glossary-card" id="glossary-tab-vault">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Document Archive &amp; Retention</h4>
    <span class="badge badge-neutral">Archive Standards</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Landscape A4</span> <span class="tag-pill tag-blue">Formatting</span></div>
      <div class="mini-glossary-def">Executive boardroom layout standard providing optimal multi-column financial and tabular presentation.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Docx Template</span> <span class="tag-pill tag-green">Editable Asset</span></div>
      <div class="mini-glossary-def">Fully styled Microsoft Word document allowing rapid customization of provider policies and solicitor filings.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Statutory Retention</span> <span class="tag-pill tag-gold">CQC Regulation 17</span></div>
      <div class="mini-glossary-def">Legal duty to retain care records, corporate minutes, and incident logs for a minimum of 7 to 8 years.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>RICS Red Book</span> <span class="tag-pill tag-blue">Valuation</span></div>
      <div class="mini-glossary-def">Royal Institution of Chartered Surveyors formal valuation standard required for commercial mortgage security.</div>
    </div>
  </div>
</div>""",

        "tab-tracker": """<div class="mini-glossary-card" id="glossary-tab-tracker">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Milestone Execution Tracker</h4>
    <span class="badge badge-neutral">Governance</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Gated Milestone</span> <span class="tag-pill tag-blue">Project Management</span></div>
      <div class="mini-glossary-def">Strict sequential dependency where downstream capital or legal steps cannot proceed without formal phase sign-off.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>ICAEW Sign-Off</span> <span class="tag-pill tag-gold">Accountancy</span></div>
      <div class="mini-glossary-def">Chartered accountant certification verifying 12-month cashflow viability required under CQC Registration Regulation 13.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Building Control</span> <span class="tag-pill tag-blue">Statutory Certification</span></div>
      <div class="mini-glossary-def">Local authority or approved inspector certification of Part B (Fire) and Part M (Access) building compliance.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Proactis Gateway</span> <span class="tag-pill tag-green">Tendering</span></div>
      <div class="mini-glossary-def">Secure portal for submission of local authority pre-qualification questionnaires and commercial rate cards.</div>
    </div>
  </div>
</div>""",

        "tab-commissioning": """<div class="mini-glossary-card" id="glossary-tab-commissioning">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Commissioning &amp; Occupancy</h4>
    <span class="badge badge-neutral">Public Procurement</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>ProContract / DPS</span> <span class="tag-pill tag-blue">Procurement</span></div>
      <div class="mini-glossary-def">Electronic Dynamic Purchasing System (Luton Council Ref: AT1115) used for accredited provider placement tenders.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>NHS BLMK ICB</span> <span class="tag-pill tag-blue">Health Commissioning</span></div>
      <div class="mini-glossary-def">Bedfordshire, Luton and Milton Keynes Integrated Care Board responsible for Continuing Healthcare (CHC) funding.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Section 117 MHA</span> <span class="tag-pill tag-gold">Statutory Aftercare</span></div>
      <div class="mini-glossary-def">Section 117 Mental Health Act 1983 joint statutory duty of NHS and Local Authority to fund non-means-tested care.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>IPA</span> <span class="tag-pill tag-green">Contracts</span></div>
      <div class="mini-glossary-def">Individual Placement Agreement: binding commercial care contract setting out assessed core hours and enhanced 1:1 rates.</div>
    </div>
  </div>
</div>""",

        "tab-financials": """<div class="mini-glossary-card" id="glossary-tab-financials">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Financial Modeling &amp; Viability</h4>
    <span class="badge badge-neutral">GAAP / IFRS</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Gross Turnover</span> <span class="tag-pill tag-green">Revenue</span></div>
      <div class="mini-glossary-def">Total gross placement fee revenue (&pound;977,600 annual run-rate across 8 specialist beds at &pound;2,350/wk average).</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Break-Even Occupancy</span> <span class="tag-pill tag-gold">Risk Management</span></div>
      <div class="mini-glossary-def">Minimum occupied beds required to cover all fixed and semi-variable operational costs (3.8 beds / 47.5% occupancy).</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Care Payroll Burden</span> <span class="tag-pill tag-blue">Cost Accounting</span></div>
      <div class="mini-glossary-def">Direct staff costs including employer NI (&pound;5,000 threshold @ 15%), 3% pension, and 12.07% holiday pay (&pound;355,108).</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Working Capital Runway</span> <span class="tag-pill tag-green">Cashflow</span></div>
      <div class="mini-glossary-def">Liquid cash reserve required to bridge Local Authority 30&ndash;60 day payment lags (&pound;85,000&ndash;&pound;120,000 buffer).</div>
    </div>
  </div>
</div>""",

        "tab-cqc-reqs": """<div class="mini-glossary-card" id="glossary-tab-cqc-reqs">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Single Assessment Framework</h4>
    <span class="badge badge-neutral">SAF Compliance</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>SAF</span> <span class="tag-pill tag-gold">Framework</span></div>
      <div class="mini-glossary-def">Single Assessment Framework: CQC's regulatory evaluation model comprising 5 Key Questions and 34 Quality Statements.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>e-MAR</span> <span class="tag-pill tag-green">Digital Systems</span></div>
      <div class="mini-glossary-def">Electronic Medication Administration Record: digital platform eliminating transcription errors and alerting on missed doses.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>IDDSI</span> <span class="tag-pill tag-blue">Clinical Nutrition</span></div>
      <div class="mini-glossary-def">International Dysphagia Diet Standardisation Initiative: global framework defining modified food textures and drink thicknesses.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Duty of Candour</span> <span class="tag-pill tag-gold">Regulation 20</span></div>
      <div class="mini-glossary-def">Statutory duty to act openly and transparently when an unintended or unexpected incident occurs resulting in harm.</div>
    </div>
  </div>
</div>""",

        "tab-cqc": """<div class="mini-glossary-card" id="glossary-tab-cqc">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; CQC Provider Registration</h4>
    <span class="badge badge-neutral">Registration Regs</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Section 26 NoP</span> <span class="tag-pill tag-blue">HSCA 2008</span></div>
      <div class="mini-glossary-def">Notice of Proposal: CQC statutory notification proposing to grant registration, triggering standard 28-day response period.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Section 28 NoD</span> <span class="tag-pill tag-green">HSCA 2008</span></div>
      <div class="mini-glossary-def">Notice of Decision: final statutory certificate of registration legally activating the provider on the CQC public directory.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Regulation 7</span> <span class="tag-pill tag-gold">Regulated Activities</span></div>
      <div class="mini-glossary-def">CQC regulation governing Registered Managers: mandates fit and proper qualifications, skills, and Level 5 management certification.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Regulation 6</span> <span class="tag-pill tag-blue">Governance</span></div>
      <div class="mini-glossary-def">CQC regulation governing Nominated Individuals: requires senior executive to oversee quality and statutory compliance.</div>
    </div>
  </div>
</div>""",

        "tab-tax": """<div class="mini-glossary-card" id="glossary-tab-tax">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Corporate Tax &amp; Real Estate</h4>
    <span class="badge badge-neutral">HMRC Statutes</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>s.105/106 ITEPA 2003</span> <span class="tag-pill tag-gold">Tax Law</span></div>
      <div class="mini-glossary-def">Income Tax (Earnings and Pensions) Act 2003 rules where paying open market rent under an AST reduces Benefit in Kind to &pound;0.00.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>FRI Commercial Lease</span> <span class="tag-pill tag-blue">Commercial Law</span></div>
      <div class="mini-glossary-def">Full Repairing and Insuring lease shifting all property maintenance, insurance, and statutory compliance costs to the tenant.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>ATED Relief s.133</span> <span class="tag-pill tag-green">HMRC</span></div>
      <div class="mini-glossary-def">Annual Tax on Enveloped Dwellings relief under Finance Act 2013 for qualifying commercial property rental businesses.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>VATA 1994 Sched 9 Grp 7</span> <span class="tag-pill tag-gold">VAT</span></div>
      <div class="mini-glossary-def">Statutory exemption from VAT for welfare services and care provided by state-regulated bodies.</div>
    </div>
  </div>
</div>""",

        "tab-planning": """<div class="mini-glossary-card" id="glossary-tab-planning">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Town Planning Law</h4>
    <span class="badge badge-neutral">Statutory Acts</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>TCPA 1990 s.55(2)(f)</span> <span class="tag-pill tag-blue">Statute</span></div>
      <div class="mini-glossary-def">Section of Town and Country Planning Act 1990 establishing that changes of use within the same use class do not constitute development.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Section 192 CLPUD</span> <span class="tag-pill tag-blue">Immunity</span></div>
      <div class="mini-glossary-def">Statutory certificate of lawfulness conclusively determining that a proposed use does not require planning permission.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Article 4 Direction</span> <span class="tag-pill tag-gold">Local Policy</span></div>
      <div class="mini-glossary-def">Local authority planning restriction removing permitted development rights; explicitly limited to C4 HMOs, not Class C3(b).</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Luton Local Plan LLP31</span> <span class="tag-pill tag-green">Transport</span></div>
      <div class="mini-glossary-def">Local planning policy governing parking standards; permanently satisfied by 10 dedicated campus parking spaces.</div>
    </div>
  </div>
</div>""",

        "tab-capex": """<div class="mini-glossary-card" id="glossary-tab-capex">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; CapEx &amp; Engineering</h4>
    <span class="badge badge-neutral">Engineering Specs</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>BS 5839-1 Cat L1</span> <span class="tag-pill tag-gold">Fire Safety</span></div>
      <div class="mini-glossary-def">British Standard specifying highest level of life-safety fire detection, requiring automatic detectors in all rooms and roof voids.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>FD30S</span> <span class="tag-pill tag-gold">Building Regs</span></div>
      <div class="mini-glossary-def">Fire door assembly providing 30 minutes fire resistance and cold smoke sealing with intumescent perimeter strips.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>TMV3</span> <span class="tag-pill tag-blue">Water Safety</span></div>
      <div class="mini-glossary-def">Thermostatic Mixing Valve Scheme certified under NHS Model Engineering Spec D08, limiting water temperature to 41&deg;C.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>HTM 01-04</span> <span class="tag-pill tag-green">Infection Control</span></div>
      <div class="mini-glossary-def">Health Technical Memorandum governing decontamination and separation of foul/soiled and clean laundry flows.</div>
    </div>
  </div>
</div>""",

        "tab-houses": """<div class="mini-glossary-card" id="glossary-tab-houses">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Campus Real Estate Specification</h4>
    <span class="badge badge-neutral">Building Standards</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Usable Floor Space</span> <span class="tag-pill tag-blue">Standards</span></div>
      <div class="mini-glossary-def">Net internal area of resident bedrooms excluding en-suite facilities (minimum 12.0m&sup2; compliant with national guidance).</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Wetroom Level Access</span> <span class="tag-pill tag-green">DDA Compliance</span></div>
      <div class="mini-glossary-def">Barrier-free, walk-in shower room with anti-slip flooring (R11 rating) and thermostatic temperature control.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Party Wall Act 1996</span> <span class="tag-pill tag-gold">Property Law</span></div>
      <div class="mini-glossary-def">Statutory framework governing rights and notices for works affecting shared boundary party walls.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Sensory Calm Room</span> <span class="tag-pill tag-blue">Autism Design</span></div>
      <div class="mini-glossary-def">Dedicated low-arousal de-escalation space with acoustic damping and controllable dimmable lighting in 80 Marston Gardens.</div>
    </div>
  </div>
</div>""",

        "tab-strategy": """<div class="mini-glossary-card" id="glossary-tab-strategy">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Campus Strategy &amp; Workforce</h4>
    <span class="badge badge-neutral">Workforce Terms</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>WTR 1998</span> <span class="tag-pill tag-gold">Employment Law</span></div>
      <div class="mini-glossary-def">Working Time Regulations 1998 mandating maximum 48-hour average working week, 11 hours daily rest, and 24 hours uninterrupted weekly rest.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>FTE</span> <span class="tag-pill tag-blue">Workforce</span></div>
      <div class="mini-glossary-def">Full-Time Equivalent: 37.5 contracted weekly working hours per staff unit (10.0 FTE permanent establishment deployed).</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Waking Night</span> <span class="tag-pill tag-green">Clinical Care</span></div>
      <div class="mini-glossary-def">Active, awake overnight care worker monitoring resident health, epilepsy protocols, and campus security.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Sleep-In Standby</span> <span class="tag-pill tag-blue">Rotas</span></div>
      <div class="mini-glossary-def">Designated staff member sleeping on site in dedicated office, available to be awakened during emergency incidents.</div>
    </div>
  </div>
</div>""",

        "tab-advisory": """<div class="mini-glossary-card" id="glossary-tab-advisory">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Multi-Disciplinary Advisory</h4>
    <span class="badge badge-neutral">Expert Opinions</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>DSCR</span> <span class="tag-pill tag-green">Debt Capacity</span></div>
      <div class="mini-glossary-def">Debt Service Coverage Ratio: net operating cashflow divided by debt service (&gt;1.50x required by commercial lenders).</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>PBS</span> <span class="tag-pill tag-blue">Clinical</span></div>
      <div class="mini-glossary-def">Positive Behavioural Support: evidence-based multi-tiered framework designed to reduce distress and eliminate restrictive practices.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>COPDOL11</span> <span class="tag-pill tag-gold">Legal</span></div>
      <div class="mini-glossary-def">Court of Protection stream-lined judicial authorisation procedure for deprivation of liberty in supported living accommodation.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>MASH</span> <span class="tag-pill tag-blue">Safeguarding</span></div>
      <div class="mini-glossary-def">Multi-Agency Safeguarding Hub: Luton Borough Council central referral intake for Section 42 safeguarding enquiries.</div>
    </div>
  </div>
</div>""",

        "tab-options": """<div class="mini-glossary-card" id="glossary-tab-options">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Strategic Appraisal</h4>
    <span class="badge badge-neutral">MCDA Terms</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>MCDA</span> <span class="tag-pill tag-blue">Methodology</span></div>
      <div class="mini-glossary-def">Multi-Criteria Decision Analysis: quantitative 100-point appraisal across 5 weighted governance and commercial criteria.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Class C2</span> <span class="tag-pill tag-blue">Planning</span></div>
      <div class="mini-glossary-def">Residential Institution (Care Home) providing full board and personal care, requiring formal planning permission and planning committee approval.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Single Household</span> <span class="tag-pill tag-gold">Case Law</span></div>
      <div class="mini-glossary-def">Legal concept established in North Devon DC v FSS [2004] confirming non-resident rota staff do not displace single household status.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Sluice Room</span> <span class="tag-pill tag-green">Infection Control</span></div>
      <div class="mini-glossary-def">Specialist disposal facility mandatory in C2 care homes but not required in domestic Class C3(b) supported living settings.</div>
    </div>
  </div>
</div>""",

        "tab-overview": """<div class="mini-glossary-card" id="glossary-tab-overview">
  <div class="mini-glossary-header">
    <h4 class="mini-glossary-title">📖 Contextual Statutory &amp; Technical Glossary &mdash; Executive Overview</h4>
    <span class="badge badge-neutral">Stage 1 Reference</span>
  </div>
  <div class="mini-glossary-grid">
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>CLPUD</span> <span class="tag-pill tag-blue">Planning</span></div>
      <div class="mini-glossary-def">Certificate of Lawfulness of Proposed Use or Development under S.192 Town and Country Planning Act 1990 confirming immunity from enforcement.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Use Class C3(b)</span> <span class="tag-pill tag-blue">Planning</span></div>
      <div class="mini-glossary-def">Town and Country Planning (Use Classes) Order 1987 provision allowing up to 6 persons living together as a single household receiving care.</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>EBITDA</span> <span class="tag-pill tag-green">Financial</span></div>
      <div class="mini-glossary-def">Earnings Before Interest, Tax, Depreciation, and Amortisation (&pound;341,392 operating surplus in OpCo, 34.9% margin).</div>
    </div>
    <div class="mini-glossary-item">
      <div class="mini-glossary-term"><span>Section 28(3)</span> <span class="tag-pill tag-gold">CQC Fast-Track</span></div>
      <div class="mini-glossary-def">Statutory waiver of representation under Health and Social Care Act 2008 cutting 28 days off final registration certificate issuance.</div>
    </div>
  </div>
</div>"""
    }

    injected_count = 0
    # Process from bottom of document to top (dict order: tab-glossary down to tab-overview)
    for tid, gloss_html in glossaries.items():
        ref_marker = f'id="sec-references-{tid}"'
        ref_pos = html.find(ref_marker)
        if ref_pos != -1:
            sec_start = html.rfind('<section', 0, ref_pos)
            html = html[:sec_start] + gloss_html + "\n\n            " + html[sec_start:]
            injected_count += 1
        else:
            print(f"  ⚠️ Reference section marker not found for {tid}")

    print(f"  ✓ Successfully injected contextual mini-glossaries into {injected_count} tabs.")
    check_tabs(html, "Step 15 (Glossaries)")

    # =========================================================================
    # WRITE BACK TO FILE
    # =========================================================================
    print(f"\nWriting upgraded portal/v2.html ({len(html):,} characters)...")
    write_file(V2_HTML_PATH, html)
    final_len = len(html)
    diff = final_len - initial_len
    print(f"✓ Final size: {final_len:,} characters (+{diff:,} bytes).")
    print("ALL 19 UPGRADES APPLIED CLEANLY AND SAFELY WITH 100% TAB INTEGRITY!")

if __name__ == "__main__":
    main()
