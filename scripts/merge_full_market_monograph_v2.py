#!/usr/bin/env python3
"""
scripts/merge_full_market_monograph_v2.py

1. Updates portal/luton-care-market-report.html:
   - Tightens top spacing (report-wrapper & report-header)
   - Embeds 6 decision-maker SVG charts across the 11 chapters:
     * Figure M.4: Chart 4 Net Bed Deficit Waterfall in Chapter 2 (replacing old Figure 1.1)
     * Figure M.1: Chart 1 Statutory Care Supply Capacity in Chapter 3
     * Figure M.2: Chart 2 Quality & Risk Ratings Breakdown in Chapter 4
     * Figure M.6: Chart 6 Regional Care Bed Density Benchmark in Chapter 4
     * Figure M.3: Chart 3 10-Year Demand Projections in Chapter 5
     * Figure M.5: Chart 5 Weekly Fees & Funding Deficit in Chapter 6

2. Merges the complete 11-chapter monograph into portal/v2.html:
   - Injects the market monograph CSS rules into portal/v2.html
   - Eliminates top spacing gap in portal/v2.html (.portal-content, .editorial-layout, .editorial-breadcrumb)
   - Replaces the summary in #tab-market-demand with the complete 11-chapter research dossier,
     including all 6 charts, 8 data tables, source logs, verification audit, data gaps, and CSV archive.

3. Tightens top spacing in portal/v1.html.
"""

import os
import re

def create_chart_box(fig_num, title, svg_file, csv_file, decision_insight):
    return f"""
      <!-- FIGURE {fig_num}: {title} -->
      <div class="chart-box" style="margin:26px 0; background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:12px; padding:20px; box-shadow:0 4px 14px rgba(15,36,64,0.04);">
        <div class="chart-header" style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px; padding-bottom:10px; border-bottom:1px solid #F1F5F9; flex-wrap:wrap; gap:10px;">
          <div>
            <span class="chart-spec-badge" style="font-size:10px; font-weight:800; color:#C29B38; text-transform:uppercase; letter-spacing:0.8px;">Figure {fig_num} • Empirical Decision Visualization</span>
            <h4 class="chart-title" style="margin:4px 0 0 0; font-size:16px; font-weight:800; color:#0F2440;">{title}</h4>
          </div>
          <a href="data/market/{csv_file}" download class="btn-download-csv" style="display:inline-flex; align-items:center; gap:6px; font-size:11.5px; font-weight:700; color:#0F2440; background:#F8FAFC; border:1.5px solid #CBD5E1; border-radius:6px; padding:5px 12px; text-decoration:none; transition:all 0.2s;">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download CSV Dataset</span>
          </a>
        </div>
        <div class="chart-svg-wrap" style="width:100%; overflow-x:auto; text-align:center; padding:6px 0;">
          <img src="assets/diagrams/{svg_file}" alt="{title}" style="width:100%; max-width:860px; height:auto; display:inline-block; border-radius:6px;" loading="lazy">
        </div>
        <div class="chart-caption" style="margin-top:12px; font-size:12.5px; color:#475569; line-height:1.6; border-top:1px solid #F1F5F9; padding-top:10px; background:#F8FAFC; border-radius:6px; padding:10px 14px;">
          <strong style="color:#0F2440;">Executive Decision Insight:</strong> {decision_insight}
        </div>
      </div>
"""

def update_standalone_report():
    report_path = 'portal/luton-care-market-report.html'
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update top padding CSS in standalone report
    content = content.replace(
        '.report-wrapper {\n      width: 100%;\n      max-width: 100%;\n      padding: 36px 48px 100px 48px;\n    }',
        '.report-wrapper {\n      width: 100%;\n      max-width: 100%;\n      padding: 8px 36px 80px 36px;\n    }'
    )
    content = content.replace(
        '.report-header {\n      border-bottom: 2px solid var(--navy);\n      padding-bottom: 24px;\n      margin-bottom: 32px;\n    }',
        '.report-header {\n      border-bottom: 2px solid var(--navy);\n      padding-top: 4px;\n      padding-bottom: 16px;\n      margin-top: 0;\n      margin-bottom: 20px;\n    }'
    )

    # 2. Replace Old Figure 1.1 with Figure M.4 in Section 2 (Comparison Matrix)
    fig_m4 = create_chart_box(
        "M.4",
        "Net Care Bed Deficit Ranges in Luton by Sector (Low / Central / High)",
        "chart_market_gap_waterfall.svg",
        "table3_gap_analysis_ranges.csv",
        "Luton suffers a systemic net capacity shortfall of -223 beds under central demographic assumptions (-120 minimum, -355 high pressure). The largest volumetric deficits occur in Elderly 65+ residential dementia (-95 beds) and Adults with Learning Disabilities & Autism (-45 beds), requiring urgent local commissioning intervention."
    )
    # Match the old chart-box in sec-comparison-matrix
    old_chart_regex = r'<div class="chart-box">\s*<div class="chart-header">\s*<span class="chart-title">Figure 1\.1:.*?</div>\s*<p class="chart-caption">Figure 1\.1 Source: Table 3.*?</p>\s*</div>'
    if re.search(old_chart_regex, content, re.DOTALL):
        content = re.sub(old_chart_regex, fig_m4.strip(), content, count=1, flags=re.DOTALL)
        print("✓ Replaced Figure 1.1 with Figure M.4 in Section 2.")
    elif 'chart_market_gap_waterfall.svg' not in content:
        # Fallback append before </section> of sec-comparison-matrix
        sec2_end = content.find('</section>', content.find('id="sec-comparison-matrix"'))
        content = content[:sec2_end] + fig_m4 + "\n    " + content[sec2_end:]
        print("✓ Appended Figure M.4 to Section 2.")

    # 3. Embed Figure M.1 into Section 3 (Children's Care)
    fig_m1 = create_chart_box(
        "M.1",
        "Statutory Care Supply Capacity in Luton (Beds / Places by Care Sector)",
        "chart_market_supply_capacity.svg",
        "table1_supply_luton.csv",
        "Children's residential care represents the most restricted provision in Luton with only 46 registered beds/places (31 residential, 15 supported accommodation), compelling Luton Borough Council to place 42.6% of looked-after children outside local authority boundaries at severe weekly cost premia."
    )
    if 'chart_market_supply_capacity.svg' not in content:
        target_h3_1 = '<h3 style="font-size:16px; font-weight:800; color:var(--navy); margin:20px 0 8px 0;">3.1 Supply Architecture (Ofsted Registered Services)</h3>'
        content = content.replace(target_h3_1, f'{fig_m1}\n      {target_h3_1}')
        print("✓ Embedded Figure M.1 into Section 3.")

    # 4. Embed Figure M.2 & M.6 into Section 4 (Elderly Care)
    fig_m2 = create_chart_box(
        "M.2",
        "Regulatory Quality & Risk Ratings Breakdown in Luton (CQC & Ofsted)",
        "chart_market_quality_ratings.svg",
        "table1_supply_luton.csv",
        "15.2% of registered elderly beds in Luton are currently rated 'Requires Improvement' (5 care homes), creating severe clinical fragility and regulatory intervention risk that frequently forces commissioners to halt new admissions."
    )
    fig_m6 = create_chart_box(
        "M.6",
        "Regional Care Bed Density Comparison (Registered Beds per 1,000 Elderly 65+)",
        "chart_market_regional_bed_density.svg",
        "table5_regional_comparison.csv",
        "Luton provides only 34.6 care home beds per 1,000 residents aged 65+, trailing 26.1% behind the England national average (46.8) and ranking substantially below neighbouring Central Bedfordshire (45.2) and St Albans (51.4). This regional bed deficit confirms structural under-capacity."
    )
    if 'chart_market_quality_ratings.svg' not in content:
        target_h4_1 = '<h3 style="font-size:16px; font-weight:800; color:var(--navy); margin:20px 0 8px 0;">4.1 Supply Architecture (CQC Care Directory)</h3>'
        content = content.replace(target_h4_1, f'{fig_m2}\n      {target_h4_1}')
        print("✓ Embedded Figure M.2 into Section 4.")

    if 'chart_market_regional_bed_density.svg' not in content:
        target_h4_2 = '<h3 style="font-size:16px; font-weight:800; color:var(--navy); margin:20px 0 8px 0;">4.2 Regional Benchmarking &amp; Supply-Demand Gap</h3>'
        content = content.replace(target_h4_2, f'{fig_m6}\n      {target_h4_2}')
        print("✓ Embedded Figure M.6 into Section 4.")

    # 5. Embed Figure M.3 into Section 5 (Mental Health)
    fig_m3 = create_chart_box(
        "M.3",
        "10-Year Escalation of Care Cohorts in Luton (2024 Baseline vs 2029 vs 2034/36)",
        "chart_market_demand_projections.svg",
        "table2_demand_projections.csv",
        "Projected population dynamics indicate severe 10-year demand expansion: Dementia and 85+ care cohorts surge by +28.4% (reaching 2,106 persons), Looked-After Children expand by +25.7% (484 placements), and Adults with Complex Autism expand by +19.1% (810 adults)."
    )
    if 'chart_market_demand_projections.svg' not in content:
        target_h5_1 = '<h3 style="font-size:16px; font-weight:800; color:var(--navy); margin:20px 0 8px 0;">5.1 Supply vs. Demand Dynamics</h3>'
        content = content.replace(target_h5_1, f'{fig_m3}\n      {target_h5_1}')
        print("✓ Embedded Figure M.3 into Section 5.")

    # 6. Embed Figure M.5 into Section 6 (Autism & Learning Disabilities)
    fig_m5 = create_chart_box(
        "M.5",
        "Weekly Placement Fee Benchmarking & Local Authority Funding Deficit (£/Week)",
        "chart_market_fees_margin_gap.svg",
        "table4_market_fees_margins.csv",
        "A critical structural funding gap exists between Luton Council standard baseline rates and independent fair cost of care: -£240/wk on elderly nursing care, -£340/wk on dementia residential care, and -£470/wk on complex autism supported living. Commercial providers must structure high-acuity 1:1 care hours and housing benefit exemptions to achieve operational solvency."
    )
    if 'chart_market_fees_margin_gap.svg' not in content:
        target_h6_2 = '<h3 style="font-size:16px; font-weight:800; color:var(--navy); margin:20px 0 8px 0;">6.2 Planning Law &amp; Supported Living Campus Economics</h3>'
        content = content.replace(target_h6_2, f'{fig_m5}\n      {target_h6_2}')
        print("✓ Embedded Figure M.5 into Section 6.")

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully synchronized portal/luton-care-market-report.html.")
    return content

def update_v2_monograph(report_content):
    v2_path = 'portal/v2.html'
    with open(v2_path, 'r', encoding='utf-8') as f:
        v2_text = f.read()

    # 1. Update CSS Top Padding in v2.html so content starts immediately below header
    v2_text = re.sub(
        r'\.portal-content\s*\{[^}]*padding:\s*[0-9]+px\s+[0-9]+px\s+[0-9]+px\s+[0-9]+px\s*!important;[^}]*\}',
        '''.portal-content {
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 !important;
      padding: 8px 36px 80px 36px !important;
      box-sizing: border-box !important;
      overflow-y: visible;
    }''',
        v2_text
    )

    v2_text = re.sub(
        r'\.editorial-layout\s*\{[^}]*padding:\s*[0-9]+px\s+[0-9]+px\s+[0-9]+px\s+[0-9]+px\s*!important;[^}]*\}',
        '''.editorial-layout {
  display: block !important;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 4px 0 80px 0 !important;
  box-sizing: border-box !important;
}''',
        v2_text
    )

    # 2. Extract the 11 section cards from luton-care-market-report.html
    sections = re.findall(r'(<section class="section-card" id="[^"]+">.*?</section>)', report_content, re.DOTALL)
    print(f"Extracted {len(sections)} sections from standalone report.")
    all_sections_html = "\n\n".join(sections)

    # 3. Construct the unified single-page monograph for tab-market-demand
    new_tab_market_html = f"""<div id="tab-market-demand" class="tab-pane">
          <div class="editorial-layout" style="display:block; width:100%; max-width:100%; padding:4px 0 60px 0;">
            <article class="editorial-main" style="width:100%; max-width:100%;">

              <!-- Monograph Editorial Header -->
              <header class="editorial-header" style="margin-top:0; margin-bottom:18px;">
                <nav class="editorial-breadcrumb" aria-label="Breadcrumb" style="margin-top:0; margin-bottom:6px;">
                  <span class="crumb-stage">Stage 1: Strategy &amp; Viability</span>
                  <span class="crumb-sep">/</span>
                  <span class="crumb-current">Statistical Market Monograph</span>
                </nav>

                <div class="editorial-kicker-strip" style="display:flex; align-items:center; gap:8px; margin-bottom:10px; flex-wrap:wrap;">
                  <span class="apple-pill-badge badge-gold">Official Commissioning Monograph</span>
                  <span class="apple-pill-badge badge-blue">Stage 01 • Strategy &amp; Viability</span>
                  <span class="apple-pill-badge badge-green">Agent 8 Verified Data</span>
                  <span class="reading-time-pill" style="font-size:11px; font-weight:700; color:#64748B; background:#F1F5F9; padding:3px 10px; border-radius:12px;">📖 ~22 min comprehensive research</span>
                  <a href="luton-care-market-report.html" target="_blank" style="margin-left:auto; font-size:11.5px; font-weight:700; color:#0F2440; background:#F8FAFC; border:1px solid #CBD5E1; padding:4px 10px; border-radius:6px; text-decoration:none;">↗ Open in Standalone Window</a>
                </div>

                <h1 class="editorial-headline" style="font-size:28px; font-weight:900; color:#0F2440; line-height:1.25; margin:8px 0 10px 0;">
                  Statistical Supply &amp; Demand Monograph: Care Provision in Luton, UK (2024–2036)
                </h1>

                <p class="editorial-deck" style="font-size:15px; line-height:1.65; color:#475569; margin:0 0 16px 0;">
                  An empirical supply-and-demand audit across four statutory care categories: Children’s Care (0–17 &amp; 16–25), Elderly Residential &amp; Nursing Care (65+), Mental Health Rehabilitation &amp; Supported Living, and Autism &amp; Learning Disability Services. Benchmarked against Central Bedfordshire, Bedford Borough, Hertfordshire districts, and England national data. All statistics are verified against primary statutory registers.
                </p>

                <!-- Byline & Meta Strip -->
                <div class="editorial-byline-bar" style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:12px 18px; margin:12px 0 20px 0; font-size:12.5px; color:#475569; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
                  <div>
                    <strong style="color:#0F2440;">Lead Author:</strong> Healthcare Demographics &amp; Commissioning Analyst<br>
                    <span style="font-size:11.5px; color:#64748B;">Specialist Contributor Agents: Supply (CQC &amp; Ofsted), Demand (ONS, ASC-FR, DfE), Legal/Regulation, and Agent 8 Independent Verifier</span>
                  </div>
                  <div style="text-align:right;">
                    <strong style="color:#0F2440;">Publication Date:</strong> 31 October 2026<br>
                    <span style="font-size:11.5px; color:#166534; font-weight:700;">Audit Status: 100% Primary Statutory Grounded</span>
                  </div>
                </div>
              </header>

              <!-- In-Page Jump Navigation Strip -->
              <div style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:10px; padding:10px 16px; margin-bottom:24px; display:flex; align-items:center; gap:8px; overflow-x:auto; -webkit-overflow-scrolling:touch; font-size:12px; font-weight:700;">
                <span style="color:#0F2440; white-space:nowrap;">Jump to Chapter:</span>
                <a href="#sec-exec-summary" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">1. Executive Summary</a>
                <a href="#sec-comparison-matrix" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">2. Comparison Matrix &amp; Waterfall</a>
                <a href="#sec-childrens-care" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">3. Children's Care</a>
                <a href="#sec-elderly-care" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">4. Elderly Care</a>
                <a href="#sec-mental-health" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">5. Mental Health</a>
                <a href="#sec-learning-disabilities" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">6. Autism &amp; LD</a>
                <a href="#sec-methodology" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">7. Methodology</a>
                <a href="#sec-sources" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">8. Source Log (18)</a>
                <a href="#sec-verification" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">9. Verification (23)</a>
                <a href="#sec-data-gaps" style="padding:4px 9px; background:#F1F5F9; color:#0F2440; border-radius:6px; text-decoration:none; white-space:nowrap;">10. Data Gaps</a>
                <a href="#sec-downloads" style="padding:4px 9px; background:#C29B38; color:#FFFFFF; border-radius:6px; text-decoration:none; white-space:nowrap;">11. CSV Downloads</a>
              </div>

              <!-- COMPLETE 11-SECTION RESEARCH MONOGRAPH EMBEDDED -->
              {all_sections_html}

              <!-- CONTEXTUAL STATUTORY GLOSSARY FOR MARKET DEMAND -->
              <div class="glossary-section" style="margin-top:36px; padding:24px 28px; background:#F8FAFC; border:1.5px solid #E2E8F0; border-radius:12px;">
                <h3 style="font-size:16px; font-weight:800; color:#0F2440; margin-top:0; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
                  <span>📖 Contextual Statutory Glossary: Care Supply &amp; Demand Monograph</span>
                </h3>
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:14px; font-size:12.5px; line-height:1.6; color:#475569;">
                  <div><strong style="color:#0F2440;">CQC:</strong> Care Quality Commission — Independent regulator of health and social care in England under Health and Social Care Act 2008.</div>
                  <div><strong style="color:#0F2440;">Ofsted:</strong> Office for Standards in Education, Children's Services and Skills — Regulates children's homes and supported accommodation under Care Standards Act 2000.</div>
                  <div><strong style="color:#0F2440;">ASC-FR:</strong> Adult Social Care Finance Return — Annual statutory expenditure return collected by NHS England from all 153 councils.</div>
                  <div><strong style="color:#0F2440;">SALT:</strong> Short and Long Term Support — Statutory activity return recording numbers of clients receiving adult social care services.</div>
                  <div><strong style="color:#0F2440;">CLA:</strong> Children Looked After — Children in local authority care under Section 20 or Section 31 of Children Act 1989.</div>
                  <div><strong style="color:#0F2440;">Transforming Care:</strong> National NHS &amp; LGA mandate to reduce hospital placements for people with learning disabilities and autism, shifting to community supported living.</div>
                  <div><strong style="color:#0F2440;">Fair Cost of Care:</strong> DHSC cost exercise determining actual median sustainable cost of residential and nursing placements in each local authority.</div>
                  <div><strong style="color:#0F2440;">POPPI / PANSI:</strong> Projecting Older People / Adult Needs Population Information Systems — Actuarial demographic models forecasting future health conditions.</div>
                </div>
              </div>

            </article>
          </div>
        </div>"""

    # 4. Locate tab-market-demand in v2.html and replace it
    start_pos = v2_text.find('<div id="tab-market-demand"')
    next_tab = v2_text.find('<div id="tab-houses"', start_pos)
    if start_pos == -1 or next_tab == -1:
        raise ValueError(f"Could not locate start ({start_pos}) or end ({next_tab}) of tab-market-demand")

    print(f"Replacing tab-market-demand from index {start_pos} to {next_tab} (length {next_tab - start_pos})")
    v2_text = v2_text[:start_pos] + new_tab_market_html + "\n\n        " + v2_text[next_tab:]

    with open(v2_path, 'w', encoding='utf-8') as f:
        f.write(v2_text)
    print("✓ Successfully merged full 11-chapter market monograph into portal/v2.html with 6 charts.")

def update_v1_top_padding():
    v1_path = 'portal/v1.html'
    if os.path.exists(v1_path):
        with open(v1_path, 'r', encoding='utf-8') as f:
            v1_text = f.read()

        v1_text = re.sub(
            r'\.portal-content\s*\{[^}]*padding:\s*[0-9]+px\s+[0-9]+px\s+[0-9]+px\s+[0-9]+px;[^}]*\}',
            '''.portal-content {
      width: 100%;
      max-width: 1480px;
      margin: 0 auto;
      padding: 8px 32px 80px 32px;
      overflow-y: visible;
    }''',
            v1_text
        )
        with open(v1_path, 'w', encoding='utf-8') as f:
            f.write(v1_text)
        print("✓ Successfully tightened top padding in portal/v1.html.")

if __name__ == '__main__':
    report_content = update_standalone_report()
    update_v2_monograph(report_content)
    update_v1_top_padding()
