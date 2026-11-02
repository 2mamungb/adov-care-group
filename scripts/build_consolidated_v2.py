#!/usr/bin/env python3
"""
Comprehensive production-grade consolidator for portal/v2.html
Generates 7 master executive sections with 0 duplicate diagrams,
simplified 7-pill navigation, and rich decision-making reports & charts.
"""
import re
import os
import subprocess

def main():
    cmd = ['git', 'show', 'HEAD:portal/v2.html']
    html = subprocess.check_output(cmd).decode('utf-8')

    # 1. Extract head
    head_match = re.search(r'([\s\S]*?</head>)', html)
    head_content = head_match.group(1) if head_match else ""

    extra_nav_css = """
/* =========================================================================
   STREAMLINED 7-PILL EXECUTIVE MAIN MENU (SIMPLE & DIRECT)
   ========================================================================= */
.simple-executive-nav {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-wrap: nowrap;
}

.exec-nav-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 11px;
  background: #F1F5F9;
  border: 1px solid #E2E8F0;
  border-radius: 7px;
  color: #1E293B;
  font-size: 11.5px;
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
  white-space: nowrap;
  font-family: inherit;
}

.exec-nav-pill:hover {
  background: #E2E8F0;
  color: #0F2440;
  border-color: #CBD5E1;
  transform: translateY(-1px);
}

.exec-nav-pill.active {
  background: #0F2440 !important;
  color: #FFFFFF !important;
  border-color: #0F2440 !important;
  box-shadow: 0 2px 6px rgba(15, 36, 64, 0.22);
}

.exec-nav-pill .pill-icon {
  font-size: 12.5px;
  line-height: 1;
}

[data-theme="dark"] .exec-nav-pill {
  background: #1E293B;
  border-color: #334155;
  color: #CBD5E1;
}

[data-theme="dark"] .exec-nav-pill:hover {
  background: #334155;
  color: #FFFFFF;
}

[data-theme="dark"] .exec-nav-pill.active {
  background: #C29B38 !important;
  color: #0F2440 !important;
  border-color: #C29B38 !important;
}

/* Mobile dropdown selector for screen widths < 1180px */
.mobile-nav-select {
  display: none;
  padding: 6px 10px;
  font-size: 12px;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid #CBD5E1;
  background: #FFFFFF;
  color: #0F2440;
  cursor: pointer;
}

@media (max-width: 1180px) {
  .simple-executive-nav {
    display: none !important;
  }
  .mobile-nav-select {
    display: inline-block !important;
  }
}
"""
    if '.simple-executive-nav' not in head_content:
        head_content = head_content.replace('</style>', f'{extra_nav_css}\n  </style>')

    # 2. Extract tab bodies & editorial-main contents
    tab_ids = ['tab-overview', 'tab-options', 'tab-advisory', 'tab-strategy', 
               'tab-houses', 'tab-capex', 'tab-planning', 'tab-tax', 
               'tab-cqc', 'tab-cqc-reqs', 'tab-financials', 'tab-commissioning', 
               'tab-tracker', 'tab-vault', 'tab-glossary']

    tab_mains = {}
    tab_rails = {}

    for tid in tab_ids:
        m = re.search(r'id=\"' + tid + r'\"[\s\S]*?(?=<div id=\"tab-|\s*</main>)', html)
        if m:
            full_tab = m.group(0)
            m_main = re.search(r'<div class=\"editorial-main\">([\s\S]*?)</div>\s*<!--\s*/editorial-main\s*-->', full_tab)
            if m_main:
                tab_mains[tid] = m_main.group(1).strip()
            m_rail = re.search(r'(<aside class=\"editorial-rail\"[\s\S]*?</aside>\s*<!--\s*/editorial-rail\s*-->)', full_tab)
            if m_rail:
                tab_rails[tid] = m_rail.group(1).strip()

    print(f"Extracted {len(tab_mains)} editorial-main sections and {len(tab_rails)} editorial-rails.")

    # Helper cleaners
    def remove_diagram_by_src(text, img_src):
        # Splits by '<div class="visual-diagram-card">' and removes any card containing img_src
        parts = text.split('<div class="visual-diagram-card">')
        result = [parts[0]]
        for p in parts[1:]:
            if img_src in p:
                m = re.search(r'</div>\s*</div>', p)
                if m:
                    result.append(p[m.end():])
                else:
                    result.append(p)
            else:
                result.append('<div class="visual-diagram-card">' + p)
        return ''.join(result)

    def remove_figure_by_id(text, fig_id):
        return re.sub(r'<figure[^>]+id=[\"\']' + re.escape(fig_id) + r'[\"\'][\s\S]*?</figure>', '', text)

    def remove_breadcrumbs_and_header(text):
        text = re.sub(r'<nav class=\"editorial-breadcrumb\"[\s\S]*?</nav>', '', text)
        text = re.sub(r'<header class=\"editorial-header\"[\s\S]*?</header>', '', text)
        return text.strip()

    def insert_after_header(main_text, block_to_insert):
        return re.sub(r'(</header>)', r'\1\n' + block_to_insert, main_text, count=1)

    # =========================================================================
    # SECTION 1: tab-investment (Executive Investment Memorandum & Valuation)
    # =========================================================================
    s1_main = tab_mains['tab-overview']
    # Remove duplicate visual diagrams and duplicate Rota/waterfall figures from overview
    s1_main = remove_diagram_by_src(s1_main, 'diagram_campus_masterplan.svg')
    s1_main = remove_diagram_by_src(s1_main, 'diagram_financial_waterfall.svg')
    s1_main = remove_diagram_by_src(s1_main, 'diagram_cqc_roadmap.svg')
    s1_main = remove_figure_by_id(s1_main, 'fig-campus-topology')
    s1_main = remove_figure_by_id(s1_main, 'fig-financial-waterfall')

    s1_main = re.sub(r'<h1 class=\"page-title\">[^<]+</h1>', '<h1 class=\"page-title\">Executive Investment Plan, Valuation &amp; Boardroom Viability Appraisal</h1>', s1_main, count=1)
    s1_main = re.sub(r'<span class=\"crumb-current\">[^<]+</span>', '<span class=\"crumb-current\">1. Investment Plan</span>', s1_main, count=1)
    s1_main = re.sub(r'<span>Stage [0-9]:[^<]+</span>', '<span>Pillar 1: Investment Plan &amp; Procedure // Executive Planning Dossier</span>', s1_main, count=1)

    s1_deal_card = """
              <!-- EXECUTIVE INVESTMENT MEMORANDUM & DEAL STRUCTURE -->
              <div class="card" style="border-left: 4px solid var(--gold); margin-bottom: 24px; background: #FFFFFF; box-shadow: 0 4px 16px rgba(15,36,64,0.06);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                  <div>
                    <span class="badge badge-gold" style="font-size:11px; font-weight:800; text-transform:uppercase;">Institutional Investment Memorandum</span>
                    <h2 style="font-size:20px; font-weight:800; color:var(--navy); margin-top:4px; font-family:'Charter', Georgia, serif;">ADOV Care Group: 8-Bed Specialist Supported Living Campus</h2>
                  </div>
                  <span class="badge badge-success" style="font-size:12px; font-weight:700;">Class C3(b) Planning Law Immune</span>
                </div>
                
                <p style="font-size:14px; line-height:1.65; color:var(--text-main); margin-bottom:16px;">
                  <strong>Transaction Overview:</strong> Comprehensive development and operation of an 8-bed specialist Supported Living facility for adults with Autism and Learning Disabilities across <strong>78 &amp; 80 Marston Gardens, Luton (LU2 7DY)</strong>, with retained Director's private residence at 82 Marston Gardens under an Assured Shorthold Tenancy (AST) at open market rent (strictly achieving <strong>Nil Benefit-in-Kind</strong> under Section 105/106 ITEPA 2003).
                </p>

                <!-- Core Metrics 4-Col Grid -->
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap:12px; margin-bottom:16px;">
                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px 14px;">
                    <div style="font-size:11px; font-weight:700; color:#64748B; text-transform:uppercase;">Gross Annual Turnover</div>
                    <div style="font-size:20px; font-weight:900; color:#0F2440; margin:2px 0;">£977,600</div>
                    <div style="font-size:11px; color:#2563EB; font-weight:600;">8 Beds @ £2,350/wk average</div>
                  </div>
                  <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:8px; padding:12px 14px;">
                    <div style="font-size:11px; font-weight:700; color:#166534; text-transform:uppercase;">OpCo Operating EBITDA</div>
                    <div style="font-size:20px; font-weight:900; color:#059669; margin:2px 0;">£341,392</div>
                    <div style="font-size:11px; color:#047857; font-weight:700;">34.9% Net Operating Margin</div>
                  </div>
                  <div style="background:#FFFBEB; border:1px solid #FDE68A; border-radius:8px; padding:12px 14px;">
                    <div style="font-size:11px; font-weight:700; color:#92400E; text-transform:uppercase;">Group Cashflow (Pre-Tax)</div>
                    <div style="font-size:20px; font-weight:900; color:#B45309; margin:2px 0;">£438,392</div>
                    <div style="font-size:11px; color:#78350F; font-weight:700;">44.8% Cash Velocity (£36.5k/mo)</div>
                  </div>
                  <div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:8px; padding:12px 14px;">
                    <div style="font-size:11px; font-weight:700; color:#1E40AF; text-transform:uppercase;">Enterprise Value (@ 7.5x)</div>
                    <div style="font-size:20px; font-weight:900; color:#1E3A8A; margin:2px 0;">£3,760,000+</div>
                    <div style="font-size:11px; color:#1D4ED8; font-weight:600;">£2.56M OpCo + £1.2M+ Real Estate</div>
                  </div>
                </div>

                <!-- CapEx & Break-Even Ribbon -->
                <div style="display:flex; justify-content:space-between; align-items:center; background:#F1F5F9; border-radius:6px; padding:10px 14px; font-size:12.5px; flex-wrap:wrap; gap:8px;">
                  <div>
                    <strong>CapEx Requirement:</strong> £68,400 (Scenario A) • <strong>Payback Period:</strong> <span style="color:#059669; font-weight:700;">2.4 Months</span>
                  </div>
                  <div>
                    <strong>Fixed Break-Even:</strong> <span style="color:#2563EB; font-weight:700;">3.82 Beds (47.7% Occupancy)</span> • <strong>Margin of Safety:</strong> <span style="color:#059669; font-weight:800;">+52.3% Buffer</span>
                  </div>
                </div>
              </div>

              <!-- BOARDROOM DECISION GATEWAYS TABLE -->
              <div class="card" style="margin-bottom: 24px;">
                <h3 class="card-title" style="margin-bottom: 12px; font-size: 16px;">Boardroom Go / No-Go Decision Gateways (Quantitative Triggers)</h3>
                <div class="table-wrap">
                  <table class="table-journal" style="width:100%;">
                    <thead>
                      <tr>
                        <th style="width:16%;">Gateway Stage</th>
                        <th style="width:28%;">Quantitative Criteria</th>
                        <th style="width:26%;">Trigger / Proof Required</th>
                        <th style="width:30%;">Executive Action Authorized</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>Gate 1: Planning</strong></td>
                        <td>TCPA 1990 S.55(2)(f) / S.192 CLPUD</td>
                        <td>Certificate issued confirming lawful Class C3(b) use</td>
                        <td><span class="badge badge-success">Release £68.4k CapEx Fit-Out</span></td>
                      </tr>
                      <tr>
                        <td><strong>Gate 2: CQC Fast-Track</strong></td>
                        <td>Reg 7 RM Interview &amp; Section 28(3) Waiver</td>
                        <td>Waiver signed cutting 28 days off registration</td>
                        <td><span class="badge badge-primary">Issue CQC Provider Registration ID</span></td>
                      </tr>
                      <tr>
                        <td><strong>Gate 3: Luton DPS</strong></td>
                        <td>ProContract AT1115 DPS Accreditation</td>
                        <td>APL activation &amp; receipt of first mini-competition IPA</td>
                        <td><span class="badge badge-success">Onboard 10.0 FTE Staff &amp; Open Admissions</span></td>
                      </tr>
                      <tr>
                        <td><strong>Gate 4: Break-Even</strong></td>
                        <td>3.82 Beds Stabilized (47.7% Occupancy)</td>
                        <td>Bed 4 admitted (£40,733/mo gross revenue)</td>
                        <td><span class="badge badge-success">Cashflow Neutral; Authorize Beds 5–8</span></td>
                      </tr>
                      <tr>
                        <td><strong>Gate 5: Full Run-Rate</strong></td>
                        <td>8 Beds 100% Occupancy (£81,467/mo)</td>
                        <td>Full campus stabilization with £85k working capital buffer</td>
                        <td><span class="badge badge-gold">Authorize Dividend Extraction to Mamun Ltd</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
    """
    s1_main = insert_after_header(s1_main, s1_deal_card)
    s1_rail = tab_rails.get('tab-overview', '')

    # =========================================================================
    # SECTION 2: tab-market (Care Market Demand & MCDA 4-Options Appraisal)
    # =========================================================================
    s2_main = tab_mains['tab-options']
    s2_main = re.sub(r'<h1 class=\"page-title\">[^<]+</h1>', '<h1 class=\"page-title\">Care Market Demand, Transforming Care Repatriation &amp; 4-Option Strategic Appraisal</h1>', s2_main, count=1)
    s2_main = re.sub(r'<span class=\"crumb-current\">[^<]+</span>', '<span class=\"crumb-current\">2. Market Demand</span>', s2_main, count=1)
    s2_main = re.sub(r'<span>Stage [0-9]:[^<]+</span>', '<span>Pillar 2: Market Intelligence &amp; Strategic Viability // Executive Planning Dossier</span>', s2_main, count=1)

    market_gap_diagram_html = """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-blue">Luton Care Bed Deficit</span>
          <span class="visual-diagram-title">Net Statutory Bed Shortfall Ranges Across Luton &amp; Neighbouring Authorities</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/chart_market_gap_waterfall.svg" alt="Net Care Bed Deficit in Luton" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Luton Social Care Market Shortfall:</strong> Severe structural shortage of adult learning disability and complex autism supported living placements across Luton Borough Council (deficit of 136 specialist beds), creating urgent local authority commissioning demand and zero-void placement stability.
        </div>
      </div>
    """
    s2_main = re.sub(r'(<div class=[\"\']visual-diagram-card[\"\']>[\s\S]*?diagram_4options_mcda\.svg[\s\S]*?</div>\s*</div>\s*(?:</div>)?)', r'\1\n' + market_gap_diagram_html, s2_main, count=1)
    s2_rail = tab_rails.get('tab-options', '')

    # =========================================================================
    # SECTION 3: tab-campus (Campus Architecture, CapEx BoQ, S.192 & Leases)
    # =========================================================================
    s3_main = tab_mains['tab-houses']
    s3_main = re.sub(r'<h1 class=\"page-title\">[^<]+</h1>', '<h1 class=\"page-title\">Architectural Campus Masterplan, CapEx Bill of Quantities &amp; Corporate FRI Leases</h1>', s3_main, count=1)
    s3_main = re.sub(r'<span class=\"crumb-current\">[^<]+</span>', '<span class=\"crumb-current\">3. Campus &amp; CapEx</span>', s3_main, count=1)
    s3_main = re.sub(r'<span>Stage [0-9]:[^<]+</span>', '<span>Pillar 3: Infrastructure, Planning &amp; Commercial Leases // Executive Planning Dossier</span>', s3_main, count=1)

    capex_part = remove_diagram_by_src(tab_mains['tab-capex'], 'diagram_campus_masterplan.svg')
    capex_part = remove_breadcrumbs_and_header(capex_part)

    planning_part = remove_diagram_by_src(tab_mains['tab-planning'], 'diagram_campus_masterplan.svg')
    planning_part = remove_breadcrumbs_and_header(planning_part)

    tax_part = remove_diagram_by_src(tab_mains['tab-tax'], 'diagram_corporate_structure.svg')
    tax_part = remove_breadcrumbs_and_header(tax_part)

    corporate_diag_html = """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-purple">Corporate Legal Architecture</span>
          <span class="visual-diagram-title">Three-Tier Holding, PropCo &amp; OpCo Governance &amp; Tax Structure</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/diagram_corporate_structure.svg" alt="Corporate Structure Diagram" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Asset Ring-Fencing:</strong> Holding Co (Mamun Limited) owns 100% of PropCo (ADOV Limited) which holds freeholds and leases to OpCo (ADOV Care Group Limited) under commercial FRI leases. Director resides at 82 under market AST (BIK = Nil).
        </div>
      </div>
    """

    s3_append = f"""
              <div style="margin-top: 40px; padding-top: 24px; border-top: 2px solid #E2E8F0;">
                <h2 style="font-size: 20px; font-weight: 800; color: var(--navy); margin-bottom: 16px;">Part 2: Capital Expenditure (CapEx) Schedule &amp; Fit-Out Bill of Quantities</h2>
                {capex_part}
              </div>

              <div style="margin-top: 40px; padding-top: 24px; border-top: 2px solid #E2E8F0;">
                <h2 style="font-size: 20px; font-weight: 800; color: var(--navy); margin-bottom: 16px;">Part 3: Town Planning Law Immunity &amp; Section 192 CLPUD Statutory Dossier</h2>
                {planning_part}
              </div>

              <div style="margin-top: 40px; padding-top: 24px; border-top: 2px solid #E2E8F0;">
                <h2 style="font-size: 20px; font-weight: 800; color: var(--navy); margin-bottom: 16px;">Part 4: Corporate Group Architecture, FRI Leases &amp; HMRC BIK Elimination</h2>
                {corporate_diag_html}
                {tax_part}
              </div>
    """
    s3_main += s3_append
    s3_rail = tab_rails.get('tab-houses', '')

    # =========================================================================
    # SECTION 4: tab-financials (Forensic Financial Model, Waterfall & Stress-Testing)
    # =========================================================================
    s4_main = tab_mains['tab-financials']
    s4_main = re.sub(r'<h1 class=\"page-title\">[^<]+</h1>', '<h1 class=\"page-title\">Audited Financial Waterfall, GAAP Operating Budget &amp; Sensitivity Stress-Testing</h1>', s4_main, count=1)
    s4_main = re.sub(r'<span class=\"crumb-current\">[^<]+</span>', '<span class=\"crumb-current\">4. Financial Model</span>', s4_main, count=1)
    s4_main = re.sub(r'<span>Stage [0-9]:[^<]+</span>', '<span>Pillar 4: GAAP Financial Model &amp; Stress-Testing // Executive Planning Dossier</span>', s4_main, count=1)
    s4_rail = tab_rails.get('tab-financials', '')

    # =========================================================================
    # SECTION 5: tab-cqc (Clinical Governance & CQC Single Assessment)
    # =========================================================================
    s5_main = tab_mains['tab-cqc']
    s5_main = re.sub(r'<h1 class=\"page-title\">[^<]+</h1>', '<h1 class=\"page-title\">CQC Single Assessment Framework, Fit &amp; Proper Governance &amp; Day-1 Statutory SOPs</h1>', s5_main, count=1)
    s5_main = re.sub(r'<span class=\"crumb-current\">[^<]+</span>', '<span class=\"crumb-current\">5. Clinical &amp; CQC</span>', s5_main, count=1)
    s5_main = re.sub(r'<span>Stage [0-9]:[^<]+</span>', '<span>Pillar 5: Clinical Governance &amp; Regulatory Strategy // Executive Planning Dossier</span>', s5_main, count=1)

    cqc_reqs_part = remove_diagram_by_src(tab_mains['tab-cqc-reqs'], 'diagram_cqc_roadmap.svg')
    cqc_reqs_part = remove_breadcrumbs_and_header(cqc_reqs_part)

    # Insert CQC Roadmap Diagram right after header if not present
    cqc_roadmap_diag_html = """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-gold">CQC 90-Day Approval Pathway</span>
          <span class="visual-diagram-title">5 Sequential Statutory Milestones &amp; Section 28(3) Fast-Track Waiver</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/diagram_cqc_roadmap.svg" alt="CQC Approval Roadmap" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Fast-Track Acceleration:</strong> Phase 1 Pre-App -&gt; Phase 2 Governance &amp; RM -&gt; Phase 3 Submission -&gt; Phase 4 RM Interview &amp; Site Visit -&gt; Phase 5 S.28(3) Fast-Track Waiver Certificate (cuts 28 calendar days off registration).
        </div>
      </div>
    """
    if 'diagram_cqc_roadmap.svg' not in s5_main:
        s5_main = insert_after_header(s5_main, cqc_roadmap_diag_html)

    s5_append = f"""
              <div style="margin-top: 40px; padding-top: 24px; border-top: 2px solid #E2E8F0;">
                <h2 style="font-size: 20px; font-weight: 800; color: var(--navy); margin-bottom: 16px;">Part 2: CQC 5 Key Questions, 34 Quality Statements &amp; 7 Statutory Day-1 Policies</h2>
                {cqc_reqs_part}
              </div>
    """
    s5_main += s5_append
    s5_rail = tab_rails.get('tab-cqc', '')

    # =========================================================================
    # SECTION 6: tab-operations (Unified Rota & Zero-Void Commissioning SOP)
    # =========================================================================
    s6_main = remove_diagram_by_src(tab_mains['tab-strategy'], 'diagram_campus_masterplan.svg')
    s6_main = re.sub(r'<h1 class=\"page-title\">[^<]+</h1>', '<h1 class=\"page-title\">Unified Campus 24/7 Shift Rota, Cross-Campus Synergies &amp; Zero-Void Intake SOP</h1>', s6_main, count=1)
    s6_main = re.sub(r'<span class=\"crumb-current\">[^<]+</span>', '<span class=\"crumb-current\">6. Operations &amp; Rota</span>', s6_main, count=1)
    s6_main = re.sub(r'<span>Stage [0-9]:[^<]+</span>', '<span>Pillar 6: Operational Rota &amp; Intake Governance // Executive Planning Dossier</span>', s6_main, count=1)

    comm_part = remove_breadcrumbs_and_header(tab_mains['tab-commissioning'])
    comm_part = remove_diagram_by_src(comm_part, 'diagram_intake_pathway.svg')

    intake_diag_html = """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-blue">Clinical Operations SOP</span>
          <span class="visual-diagram-title">Zero-Void Resident Intake Pathway SOP (6 Phased Stages)</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/diagram_intake_pathway.svg" alt="Resident Intake Pathway SOP" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Intake Governance:</strong> Clinical pathway protocol: Referral -&gt; Desk Pre-Screen -&gt; F2F Assessment -&gt; Peer Matching -&gt; Phased Transition Visits -&gt; Tenancy &amp; Personal Care Commencement.
        </div>
      </div>
    """

    s6_append = f"""
              <div style="margin-top: 40px; padding-top: 24px; border-top: 2px solid #E2E8F0;">
                <h2 style="font-size: 20px; font-weight: 800; color: var(--navy); margin-bottom: 16px;">Part 2: Zero-Void Resident Intake SOP, Clinical Matching &amp; Luton DPS Commissioning</h2>
                {intake_diag_html}
                {comm_part}
              </div>
    """
    s6_main += s6_append
    s6_rail = tab_rails.get('tab-strategy', '')

    # =========================================================================
    # SECTION 7: tab-roadmap (180-Day Execution Roadmap, Vault & Verdict)
    # =========================================================================
    s7_main = tab_mains['tab-tracker']
    s7_main = re.sub(r'<h1 class=\"page-title\">[^<]+</h1>', '<h1 class=\"page-title\">180-Day Execution Roadmap, Master Document Vault &amp; Boardroom Investment Verdict</h1>', s7_main, count=1)
    s7_main = re.sub(r'<span class=\"crumb-current\">[^<]+</span>', '<span class=\"crumb-current\">7. Roadmap &amp; Vault</span>', s7_main, count=1)
    s7_main = re.sub(r'<span>Stage [0-9]:[^<]+</span>', '<span>Pillar 7: Execution Critical Path &amp; Archive // Executive Planning Dossier</span>', s7_main, count=1)

    gantt_diagram_html = """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-blue">Delivery Masterplan</span>
          <span class="visual-diagram-title">180-Day Execution Critical Path Gantt (Months 1–6)</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/chart_180day_execution_gantt.svg" alt="180-Day Master Execution Gantt Chart" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Sequential Operational Milestones:</strong> Day 0 Planning Submission -&gt; Month 2 CapEx Fit-Out -&gt; Month 3 CQC S.28(3) Fast-Track Waiver -&gt; Month 4 Luton DPS AT1115 Activation -&gt; Month 5 Phased Move-Ins -&gt; Month 6 Full 8-Bed Capacity (£81,467/month revenue run-rate).
        </div>
      </div>
    """
    s7_main = insert_after_header(s7_main, gantt_diagram_html)

    vault_part = remove_breadcrumbs_and_header(tab_mains['tab-vault'])
    glossary_part = remove_breadcrumbs_and_header(tab_mains['tab-glossary'])

    s7_append = f"""
              <div style="margin-top: 40px; padding-top: 24px; border-top: 2px solid #E2E8F0;">
                <h2 style="font-size: 20px; font-weight: 800; color: var(--navy); margin-bottom: 16px;">Part 2: Master Document Repository &amp; Official Download Archive</h2>
                {vault_part}
              </div>

              <div style="margin-top: 40px; padding-top: 24px; border-top: 2px solid #E2E8F0;">
                <h2 style="font-size: 20px; font-weight: 800; color: var(--navy); margin-bottom: 16px;">Part 3: Comprehensive Statutory, Clinical &amp; Financial Glossary</h2>
                {glossary_part}
              </div>
    """
    s7_main += s7_append
    s7_rail = tab_rails.get('tab-tracker', '')

    # 3. Assemble all 7 Tabs into complete panes
    def wrap_tab_pane(tid, is_active, main_content, rail_content):
        active_class = " active" if is_active else ""
        return f"""
        <!-- TAB PANE: {tid} -->
        <div id="{tid}" class="tab-pane{active_class}">
          <div class="editorial-layout">
            <div class="editorial-main">
              {main_content}
            </div><!-- /editorial-main -->
            {rail_content}
          </div><!-- /editorial-layout -->
        </div><!-- /{tid} -->
        """

    all_7_tabs_html = (
        wrap_tab_pane('tab-investment', True, s1_main, s1_rail) +
        wrap_tab_pane('tab-market', False, s2_main, s2_rail) +
        wrap_tab_pane('tab-campus', False, s3_main, s3_rail) +
        wrap_tab_pane('tab-financials', False, s4_main, s4_rail) +
        wrap_tab_pane('tab-cqc', False, s5_main, s5_rail) +
        wrap_tab_pane('tab-operations', False, s6_main, s6_rail) +
        wrap_tab_pane('tab-roadmap', False, s7_main, s7_rail)
    )

    # 4. Streamlined Header Navigation HTML
    streamlined_header_html = """
    <!-- STICKY PORTAL MASTHEAD (BRAND BAR + SIMPLE 7-PILL EXECUTIVE NAVIGATION) -->
    <header class="apple-nav-masthead" id="mainHeader" style="position:sticky; top:0; z-index:10000; background:rgba(255,255,255,0.98); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); border-bottom:1.5px solid #E2E8F0; box-shadow:0 2px 10px rgba(15,36,64,0.05);">
      
      <div class="apple-nav-inner" style="display:flex; align-items:center; justify-content:space-between; padding:8px 24px; width:100%; max-width:100%; box-sizing:border-box; gap:12px; flex-wrap:nowrap;">
        
        <!-- Left: Brand Logo & Title -->
        <div class="apple-brand-wrap" onclick="switchTab('tab-investment')" style="cursor:pointer; display:flex; align-items:center; gap:8px; flex-shrink:0;" title="ADOV Care Group — Executive Investment Suite">
          <div class="apple-brand-logo" style="width:30px; height:30px; border-radius:7px; background:linear-gradient(135deg, #0F2440 0%, #1E3A5F 100%); color:#FFFFFF; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:15px; box-shadow:0 2px 5px rgba(15,36,64,0.18);">A</div>
          <div style="display:flex; flex-direction:column; line-height:1.15;">
            <div style="display:flex; align-items:center; gap:6px;">
              <span class="apple-brand-title" style="font-size:13.5px; font-weight:800; letter-spacing:0.02em; color:#0F2440; white-space:nowrap;">ADOV CARE GROUP</span>
              <span class="apple-brand-badge" style="font-size:9.5px; font-weight:700; background:rgba(194,155,56,0.14); color:#9A751E; padding:1px 6px; border-radius:8px; border:1px solid rgba(194,155,56,0.35);">V2.0</span>
            </div>
            <span style="font-size:9.5px; font-weight:700; color:#64748B; letter-spacing:0.02em;">Investment Plan &amp; Delivery Roadmap</span>
          </div>
        </div>

        <!-- CENTER: STREAMLINED 7-SECTION EXECUTIVE MAIN MENU (SIMPLE & DIRECT) -->
        <nav class="simple-executive-nav" id="mainNavPills" aria-label="Investment Suite Navigation">
          <button class="exec-nav-pill active" data-tab="tab-investment" onclick="switchTab('tab-investment')">
            <span class="pill-icon">💼</span> 1. Investment Plan
          </button>
          <button class="exec-nav-pill" data-tab="tab-market" onclick="switchTab('tab-market')">
            <span class="pill-icon">📊</span> 2. Market Demand
          </button>
          <button class="exec-nav-pill" data-tab="tab-campus" onclick="switchTab('tab-campus')">
            <span class="pill-icon">🏛️</span> 3. Campus &amp; CapEx
          </button>
          <button class="exec-nav-pill" data-tab="tab-financials" onclick="switchTab('tab-financials')">
            <span class="pill-icon">📈</span> 4. Financial Model
          </button>
          <button class="exec-nav-pill" data-tab="tab-cqc" onclick="switchTab('tab-cqc')">
            <span class="pill-icon">🩺</span> 5. Clinical &amp; CQC
          </button>
          <button class="exec-nav-pill" data-tab="tab-operations" onclick="switchTab('tab-operations')">
            <span class="pill-icon">⚙️</span> 6. Operations &amp; Rota
          </button>
          <button class="exec-nav-pill" data-tab="tab-roadmap" onclick="switchTab('tab-roadmap')">
            <span class="pill-icon">🗺️</span> 7. Roadmap &amp; Vault
          </button>
        </nav>

        <!-- MOBILE / NARROW SCREEN SELECTOR -->
        <select class="mobile-nav-select" id="mobileNavSelect" onchange="switchTab(this.value)" aria-label="Select Section">
          <option value="tab-investment">💼 1. Investment Plan &amp; Returns</option>
          <option value="tab-market">📊 2. Market Demand &amp; Strategy</option>
          <option value="tab-campus">🏛️ 3. Campus Architecture &amp; CapEx</option>
          <option value="tab-financials">📈 4. Financial Model &amp; Waterfall</option>
          <option value="tab-cqc">🩺 5. Clinical Governance &amp; CQC</option>
          <option value="tab-operations">⚙️ 6. Operations, Rota &amp; SOP</option>
          <option value="tab-roadmap">🗺️ 7. 180-Day Roadmap &amp; Vault</option>
        </select>

        <!-- RIGHT QUICK ACTIONS: Active Badge, V1/V2, Gateway Home, Theme & Print -->
        <div class="apple-nav-right" style="display:flex; align-items:center; gap:8px; flex-shrink:0;">
          
          <!-- Active Section Indicator Badge -->
          <div class="current-section-indicator" id="currentSectionIndicator" style="display:inline-flex; align-items:center; gap:5px; font-size:11.5px; font-weight:700; color:#0F2440; background:#F1F5F9; border:1px solid #E2E8F0; padding:4px 9px; border-radius:6px; white-space:nowrap;">
            <span id="currentSectionIcon">💼</span> <span id="currentSectionTitle">1. Investment Plan</span>
          </div>

          <!-- V1 and V2 Toggle -->
          <div class="version-toggle-group" style="display:inline-flex; align-items:center; background:#F1F5F9; border:1px solid #E2E8F0; border-radius:6px; padding:2px;">
            <a href="v1.html" class="v-toggle-btn" title="Switch to Version 1.0 (Operations MIS Dashboard)" style="padding:3px 9px; font-size:11px; font-weight:700; color:#475467; text-decoration:none; border-radius:4px; transition:all 0.18s;">V1</a>
            <a href="v2.html" class="v-toggle-btn active" title="Currently viewing Version 2.0 (Executive Suite)" style="padding:3px 9px; font-size:11px; font-weight:800; color:#FFFFFF; background:#0F2440; text-decoration:none; border-radius:4px; box-shadow:0 1px 3px rgba(15,36,64,0.18);">V2</a>
          </div>

          <!-- Gateway Home Icon -->
          <a href="index.html" class="apple-btn-icon apple-btn-home" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center; width:28px; height:28px; border-radius:6px; border:1px solid #E2E8F0; background:#FFFFFF; color:#0F2440; transition:all 0.18s;" title="Return to Gateway Home">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 9.5L12 3l9 6.5V20a1.5 1.5 0 0 1-1.5 1.5H4.5A1.5 1.5 0 0 1 3 20V9.5z"></path>
              <polyline points="9 21 9 12 15 12 15 21"></polyline>
            </svg>
          </a>

          <!-- Theme Switcher -->
          <button class="apple-btn-pill" onclick="toggleTheme()" title="Toggle Appearance" style="padding:4px 7px; font-size:11px; border-radius:6px; border:1px solid #E2E8F0; background:#FFFFFF; cursor:pointer;">🌓</button>
          
          <!-- Print Dossier Button -->
          <button class="apple-btn-pill" onclick="window.print()" title="Print Current View" style="display:inline-flex; align-items:center; gap:4px; padding:4px 9px; font-size:11.5px; font-weight:700; border-radius:6px; border:1px solid #E2E8F0; background:#FFFFFF; color:#0F2440; cursor:pointer;">🖨️ Print</button>
        </div>

      </div>

    </header>
"""

    # 5. Streamlined Footer HTML
    streamlined_footer_nav = """
        <!-- 7-Pillar Streamlined Footer Navigation -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:20px; margin-top:24px; padding-top:20px; border-top:1px solid rgba(255,255,255,0.1);">
          <div>
            <div style="font-size:11px; font-weight:800; color:#C29B38; text-transform:uppercase; margin-bottom:8px;">Core Investment Plan</div>
            <a href="javascript:void(0)" onclick="switchTab('tab-investment')" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px; margin-bottom:5px;">💼 1. Investment Plan</a>
            <a href="javascript:void(0)" onclick="switchTab('tab-market')" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px; margin-bottom:5px;">📊 2. Market Demand</a>
            <a href="javascript:void(0)" onclick="switchTab('tab-campus')" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px;">🏛️ 3. Campus &amp; CapEx</a>
          </div>
          <div>
            <div style="font-size:11px; font-weight:800; color:#C29B38; text-transform:uppercase; margin-bottom:8px;">Financial &amp; Clinical Model</div>
            <a href="javascript:void(0)" onclick="switchTab('tab-financials')" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px; margin-bottom:5px;">📈 4. Financial Model</a>
            <a href="javascript:void(0)" onclick="switchTab('tab-cqc')" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px; margin-bottom:5px;">🩺 5. Clinical &amp; CQC</a>
            <a href="javascript:void(0)" onclick="switchTab('tab-operations')" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px;">⚙️ 6. Operations &amp; Rota</a>
          </div>
          <div>
            <div style="font-size:11px; font-weight:800; color:#C29B38; text-transform:uppercase; margin-bottom:8px;">Execution &amp; Downloads</div>
            <a href="javascript:void(0)" onclick="switchTab('tab-roadmap')" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px; margin-bottom:5px;">🗺️ 7. 180-Day Roadmap</a>
            <a href="docs/ADOV_Care_Group_Executive_Planning_Dossier_Finance_Magazine.pdf" target="_blank" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px; margin-bottom:5px;">📥 Finance Magazine PDF</a>
            <a href="luton-care-market-report.html" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px;">📈 Care Supply &amp; Demand</a>
          </div>
          <div>
            <div style="font-size:11px; font-weight:800; color:#C29B38; text-transform:uppercase; margin-bottom:8px;">Portal Navigation</div>
            <a href="v1.html" style="display:block; color:#CBD5E1; text-decoration:none; font-size:12.5px; margin-bottom:5px;">V1 Operations MIS</a>
            <a href="index.html" style="display:block; color:#C29B38; font-weight:700; text-decoration:none; font-size:12.5px; margin-bottom:5px;">⌂ Gateway Home</a>
            <span style="display:block; color:#94A3B8; font-size:11px;">Luton Borough Council (LU2 7DY)</span>
          </div>
        </div>
    """

    footer_match = re.search(r'(<footer class=\"portal-footer\"[\s\S]*?</footer>)', html)
    footer_content = footer_match.group(1) if footer_match else ""
    footer_content = re.sub(r'<!-- 4-Column Full Menu Section Navigation -->[\s\S]*?</div>\s*</div>\s*</div>', streamlined_footer_nav, footer_content)

    # 6. Streamlined JavaScript
    streamlined_js = """
<script>
    // =========================================================================
    // STREAMLINED 7-SECTION NAVIGATION CONTROLLER WITH BACKWARD COMPATIBILITY
    // =========================================================================
    const SECTION_MAP = {
      'tab-investment': { title: '1. Investment Plan', icon: '💼' },
      'tab-market': { title: '2. Market Demand', icon: '📊' },
      'tab-campus': { title: '3. Campus & CapEx', icon: '🏛️' },
      'tab-financials': { title: '4. Financial Model', icon: '📈' },
      'tab-cqc': { title: '5. Clinical & CQC', icon: '🩺' },
      'tab-operations': { title: '6. Operations & Rota', icon: '⚙️' },
      'tab-roadmap': { title: '7. Roadmap & Vault', icon: '🗺️' },

      // Backward-compatible mappings
      'tab-overview': 'tab-investment',
      'tab-advisory': 'tab-investment',
      'tab-options': 'tab-market',
      'tab-market-demand': 'tab-market',
      'tab-houses': 'tab-campus',
      'tab-capex': 'tab-campus',
      'tab-planning': 'tab-campus',
      'tab-tax': 'tab-campus',
      'tab-cqc-reqs': 'tab-cqc',
      'tab-strategy': 'tab-operations',
      'tab-commissioning': 'tab-operations',
      'tab-tracker': 'tab-roadmap',
      'tab-vault': 'tab-roadmap',
      'tab-glossary': 'tab-roadmap'
    };

    function switchTab(targetId) {
      let resolvedId = targetId;
      if (typeof SECTION_MAP[targetId] === 'string') {
        resolvedId = SECTION_MAP[targetId];
      }

      // Hide all tabs, activate resolved
      const allPanes = document.querySelectorAll('.tab-pane');
      allPanes.forEach(p => p.classList.remove('active'));

      const activePane = document.getElementById(resolvedId);
      if (activePane) {
        activePane.classList.add('active');
      }

      // Update executive nav pills
      document.querySelectorAll('.exec-nav-pill').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-tab') === resolvedId);
      });

      // Update mobile selector
      const mobileSel = document.getElementById('mobileNavSelect');
      if (mobileSel) {
        mobileSel.value = resolvedId;
      }

      // Update section indicator
      const info = SECTION_MAP[resolvedId];
      if (info && typeof info === 'object') {
        const iconEl = document.getElementById('currentSectionIcon');
        const titleEl = document.getElementById('currentSectionTitle');
        if (iconEl) iconEl.textContent = info.icon;
        if (titleEl) titleEl.textContent = info.title;
      }

      // Scroll to top of content
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // Persist state
      try {
        localStorage.setItem('adov_active_section', resolvedId);
      } catch (e) {}
    }

    // Theme Switcher
    function toggleTheme() {
      const htmlEl = document.documentElement;
      const current = htmlEl.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      htmlEl.setAttribute('data-theme', next);
      try {
        localStorage.setItem('adov_theme', next);
      } catch (e) {}
    }

    // Initialize state on load
    document.addEventListener('DOMContentLoaded', () => {
      // Restore theme
      try {
        const savedTheme = localStorage.getItem('adov_theme');
        if (savedTheme) {
          document.documentElement.setAttribute('data-theme', savedTheme);
        }
      } catch (e) {}

      // Restore active tab
      try {
        const savedTab = localStorage.getItem('adov_active_section');
        if (savedTab && document.getElementById(savedTab)) {
          switchTab(savedTab);
        } else {
          switchTab('tab-investment');
        }
      } catch (e) {
        switchTab('tab-investment');
      }
    });

    // Smooth In-Page Anchor Jump
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
      }
    }
</script>
"""

    # Assemble complete final HTML
    final_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
{head_content}
<body>

  <!-- MAIN PORTAL APP -->
  <div id="portal-app">

{streamlined_header_html}

    <!-- MAIN BODY - FULL WIDTH WORKSPACE -->
    <div class="portal-container">

      <!-- CONTENT DISPLAY (FULL 100% WIDTH CANVAS) -->
      <main class="portal-content">
        
        <!-- PRINT-ONLY RUNNING HEADER -->
        <div class="print-running-header">
          <span class="print-header-brand">ADOV CARE GROUP // EXECUTIVE INVESTMENT PLAN &amp; DELIVERY ROADMAP</span>
          <span class="print-header-date print-date"></span>
        </div>

{all_7_tabs_html}

      </main>

    </div><!-- /portal-container -->

{footer_content}

  </div><!-- /portal-app -->

{streamlined_js}

</body>
</html>
"""

    with open('portal/v2.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Refined portal/v2.html written successfully! ({len(final_html)} bytes, {final_html.count(chr(10)) + 1} lines)")

if __name__ == '__main__':
    main()
