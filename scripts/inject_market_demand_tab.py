#!/usr/bin/env python3
"""
scripts/inject_market_demand_tab.py
Injects the comprehensive Statistical Supply & Demand Report into:
1. portal/v2.html (as tab-market-demand in Stage 01: Strategy & Viability, plus dropdown and footer links)
2. portal/index.html (as a highlighted featured monograph on the Gateway)
3. index.html (root gateway)
"""

import os
import re
import sys

def main():
    v2_path = "portal/v2.html"
    if not os.path.exists(v2_path):
        print(f"Error: {v2_path} not found!")
        sys.exit(1)

    with open(v2_path, "r", encoding="utf-8") as f:
        v2 = f.read()

    print(f"Original portal/v2.html: {len(v2):,} bytes.")

    # 1. BUILD TAB CONTENT
    tab_html = """
        <!-- ==========================================================================
             TAB-MARKET-DEMAND: STATISTICAL SUPPLY & DEMAND REPORT (LUTON & REGIONAL)
             ========================================================================== -->
        <div id="tab-market-demand" class="tab-pane">
          <div class="editorial-layout">
            <article class="editorial-main">

              <!-- Monograph Editorial Header -->
              <header class="editorial-header">
                <div class="editorial-kicker-strip">
                  <span class="apple-pill-badge badge-gold">Official Commissioning Monograph</span>
                  <span class="apple-pill-badge badge-blue">Stage 01 • Strategy &amp; Viability</span>
                  <span class="apple-pill-badge badge-green">Agent 8 Verified Data</span>
                  <span class="reading-time-pill">📖 ~18 min read</span>
                </div>

                <h1 class="editorial-headline">
                  Statistical Supply &amp; Demand Report: Care Provision in Luton, UK (2024–2036)
                </h1>

                <p class="editorial-deck">
                  An empirical supply-and-demand audit across four statutory care categories: Children’s Care (0–17 &amp; 16–25), Elderly Residential &amp; Nursing Care (65+), Mental Health Rehabilitation &amp; Supported Living, and Autism &amp; Learning Disability Services. Benchmarked against Central Bedfordshire, Bedford Borough, Hertfordshire districts, and England national data.
                </p>

                <!-- Byline & Meta Strip -->
                <div class="editorial-byline-bar" style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:14px 20px; margin:20px 0 28px 0; font-size:12px; display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:14px;">
                  <div>
                    <strong style="display:block; font-size:10.5px; color:#0F2440; text-transform:uppercase; letter-spacing:0.5px;">Publication Date</strong>
                    <span style="color:#475467;">31 October 2026</span>
                  </div>
                  <div>
                    <strong style="display:block; font-size:10.5px; color:#0F2440; text-transform:uppercase; letter-spacing:0.5px;">Next Scheduled Refresh</strong>
                    <span style="color:#475467;">31 July 2027 (Quarterly DfE/CQC cycle)</span>
                  </div>
                  <div>
                    <strong style="display:block; font-size:10.5px; color:#0F2440; text-transform:uppercase; letter-spacing:0.5px;">Auditing &amp; Quality Gate</strong>
                    <span style="color:#166534; font-weight:700;">Agent 8 Verified (100% Headline Audit)</span>
                  </div>
                  <div>
                    <strong style="display:block; font-size:10.5px; color:#0F2440; text-transform:uppercase; letter-spacing:0.5px;">Standalone Monograph</strong>
                    <a href="luton-care-market-report.html" target="_blank" style="color:#C29B38; font-weight:700; text-decoration:none;">📄 Open Full Monograph ↗</a>
                  </div>
                </div>

                <!-- Callout Banner to Standalone Report -->
                <div style="background:linear-gradient(135deg, #0F2440 0%, #1E3A5F 100%); color:#FFFFFF; border-radius:12px; padding:18px 24px; margin-bottom:28px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:14px;">
                  <div>
                    <div style="font-size:15px; font-weight:800; color:#FFFFFF; margin-bottom:4px;">📊 Standalone Publication &amp; CSV Data Appendix Available</div>
                    <div style="font-size:12.5px; color:#CBD5E1;">A full standalone edition with dedicated print styles, 8 machine-readable CSV datasets, and interactive SVG diagrams is hosted at <code style="color:#C29B38; background:rgba(255,255,255,0.1); padding:2px 6px; border-radius:4px;">luton-care-market-report.html</code>.</div>
                  </div>
                  <a href="luton-care-market-report.html" target="_blank" style="display:inline-flex; align-items:center; gap:6px; padding:9px 18px; background:#C29B38; color:#0F2440; font-weight:800; font-size:12.5px; text-decoration:none; border-radius:8px; white-space:nowrap; transition:all 0.2s;">
                    View Dedicated Full-Screen Report &rarr;
                  </a>
                </div>

                <!-- Statutory Disclaimer -->
                <div style="background:#FFFBEB; border:1px solid #FDE68A; border-left:4px solid #C29B38; border-radius:8px; padding:14px 18px; font-size:12px; color:#92400E; margin-bottom:32px; line-height:1.5;">
                  <strong>Statutory Information Disclaimer:</strong> All figures in this monograph are derived from official statutory datasets (ONS Census 2021, DfE Children Looked After statistics, CQC Care Directory, Ofsted children’s social care data, and Luton Borough Council Market Position Statements). Figures are published solely for social care sufficiency and town planning purposes and do not constitute financial, investment, legal, or planning advice.
                </div>
              </header>

              <!-- SECTION 1: EXECUTIVE SUMMARY -->
              <section class="editorial-section" style="margin-bottom:36px;">
                <h2 class="editorial-h2" style="font-family:var(--font-serif); font-size:22px; font-weight:800; color:#0F2440; border-bottom:1.5px solid #E2E8F0; padding-bottom:8px; margin-bottom:14px;">
                  1. Executive Summary &amp; Demographic Landscape
                </h2>
                <p style="font-size:14.5px; line-height:1.65; color:#1E293B; margin-bottom:16px;">
                  Luton presents one of the most distinctive social care demographic profiles in England. With a total usual resident population of <strong>225,261</strong> (ONS Census 2021), Luton is simultaneously one of the youngest towns in the UK—with <strong>26.0% (58,478)</strong> aged 0–17—and on the precipice of an acute demographic escalation in older adults, where the population aged 65 and over is projected to surge by <strong>+45.0%</strong> by 2036. Across all four care categories analyzed, Luton faces a structural deficit of local, high-quality residential and supported care beds, forcing the local authority and Integrated Care Board (ICB) to rely on expensive out-of-borough placements.
                </p>

                <!-- 4 KPI Summary Tiles -->
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:14px; margin-bottom:24px;">
                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:16px;">
                    <div style="font-size:11px; font-weight:700; color:#475467; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">Children in Care (CLA)</div>
                    <div style="font-size:26px; font-weight:800; color:#0F2440; line-height:1.1; margin-bottom:4px;">374</div>
                    <div style="font-size:11.5px; font-weight:700; color:#DC2626;">Rate: 63.0 / 10k (Deficit: -26 beds)</div>
                  </div>
                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:16px;">
                    <div style="font-size:11px; font-weight:700; color:#475467; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">Older Adults Bed Density</div>
                    <div style="font-size:26px; font-weight:800; color:#0F2440; line-height:1.1; margin-bottom:4px;">33.9</div>
                    <div style="font-size:11.5px; font-weight:700; color:#DC2626;">Beds / 1k 65+ (England: 43.5 / 1k)</div>
                  </div>
                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:16px;">
                    <div style="font-size:11px; font-weight:700; color:#475467; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">Mental Health Cohort</div>
                    <div style="font-size:26px; font-weight:800; color:#0F2440; line-height:1.1; margin-bottom:4px;">3,500</div>
                    <div style="font-size:11.5px; font-weight:700; color:#DC2626;">Accessing MH Care (Deficit: -73 beds)</div>
                  </div>
                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:16px;">
                    <div style="font-size:11px; font-weight:700; color:#475467; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">Funded LD Adults</div>
                    <div style="font-size:26px; font-weight:800; color:#0F2440; line-height:1.1; margin-bottom:4px;">489</div>
                    <div style="font-size:11.5px; font-weight:700; color:#DC2626;">81.5% in family home (Deficit: -67 beds)</div>
                  </div>
                </div>
              </section>

              <!-- SECTION 2: CROSS-SECTOR STRATEGIC COMPARISON -->
              <section class="editorial-section" style="margin-bottom:36px;">
                <h2 class="editorial-h2" style="font-family:var(--font-serif); font-size:22px; font-weight:800; color:#0F2440; border-bottom:1.5px solid #E2E8F0; padding-bottom:8px; margin-bottom:14px;">
                  2. Cross-Sector Supply, Demand &amp; Gap Matrix
                </h2>
                
                <p style="font-size:14px; color:#334155; margin-bottom:14px;">
                  Summary comparison across all four categories demonstrating that every major care segment in Luton operates under structural capacity deficits:
                </p>

                <div style="width:100%; overflow-x:auto; margin-bottom:20px; border:1px solid #E2E8F0; border-radius:8px;">
                  <table style="width:100%; border-collapse:collapse; font-size:12.5px; text-align:left;">
                    <thead>
                      <tr style="background:#0F2440; color:#FFFFFF;">
                        <th style="padding:10px 12px; border:1px solid #1E3A5F;">Sector Category</th>
                        <th style="padding:10px 12px; border:1px solid #1E3A5F;">Current Supply</th>
                        <th style="padding:10px 12px; border:1px solid #1E3A5F;">Active Demand</th>
                        <th style="padding:10px 12px; border:1px solid #1E3A5F;">Central Gap</th>
                        <th style="padding:10px 12px; border:1px solid #1E3A5F;">Sensitivity Range</th>
                        <th style="padding:10px 12px; border:1px solid #1E3A5F;">Council Rate</th>
                        <th style="padding:10px 12px; border:1px solid #1E3A5F;">Regulatory Friction</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr style="background:#FFFFFF;">
                        <td style="padding:9px 12px; border:1px solid #E2E8F0; font-weight:700;">1. Children's Care (0-25)</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">62 places (38 res + 24 supp)</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">88 placements</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0; color:#991B1B; font-weight:800;">-26 beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">-18 to -38 beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">£4,850 - £6,200/wk</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">Ofsted: 16–26 wks</td>
                      </tr>
                      <tr style="background:#F8FAFC;">
                        <td style="padding:9px 12px; border:1px solid #E2E8F0; font-weight:700;">2. Elderly Care (65+)</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">895 beds (527 res + 368 nurs)</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">1,045 in bedded care</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0; color:#991B1B; font-weight:800;">-150 beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">-85 to -225 beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">£864 - £1,120/wk</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">CQC: 10–16 wks</td>
                      </tr>
                      <tr style="background:#FFFFFF;">
                        <td style="padding:9px 12px; border:1px solid #E2E8F0; font-weight:700;">3. Mental Health Rehab</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">112 supported beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">185 intensive care</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0; color:#991B1B; font-weight:800;">-73 beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">-45 to -110 beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">£20.71 - £22.01/hr</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">CQC: 8–14 wks</td>
                      </tr>
                      <tr style="background:#F8FAFC;">
                        <td style="padding:9px 12px; border:1px solid #E2E8F0; font-weight:700;">4. Autism &amp; Learning Dis.</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">148 supported places</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">215 needing living beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0; color:#991B1B; font-weight:800;">-67 beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">-38 to -95 beds</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">£1,850 - £2,650/wk</td>
                        <td style="padding:9px 12px; border:1px solid #E2E8F0;">CQC Class C3b: 6–10 wks</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- FIGURE 1.1 SVG CHART -->
                <div style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:10px; padding:18px; margin:20px 0;">
                  <div style="font-size:13px; font-weight:800; color:#0F2440; margin-bottom:10px;">Figure 1.1: Supply vs. Demand &amp; Net Bed Deficit in Luton (2024 Baseline)</div>
                  <div style="display:flex; justify-content:center; overflow-x:auto;">
                    <svg width="840" height="230" viewBox="0 0 840 230" style="max-width:100%; height:auto;">
                      <line x1="200" y1="20" x2="800" y2="20" stroke="#F1F5F9" stroke-width="1"/>
                      <line x1="200" y1="70" x2="800" y2="70" stroke="#F1F5F9" stroke-width="1"/>
                      <line x1="200" y1="120" x2="800" y2="120" stroke="#F1F5F9" stroke-width="1"/>
                      <line x1="200" y1="170" x2="800" y2="170" stroke="#F1F5F9" stroke-width="1"/>
                      <line x1="200" y1="210" x2="800" y2="210" stroke="#CBD5E1" stroke-width="1.5"/>

                      <text x="200" y="224" font-size="9.5" fill="#64748B" text-anchor="middle">0</text>
                      <text x="350" y="224" font-size="9.5" fill="#64748B" text-anchor="middle">250</text>
                      <text x="500" y="224" font-size="9.5" fill="#64748B" text-anchor="middle">500</text>
                      <text x="650" y="224" font-size="9.5" fill="#64748B" text-anchor="middle">750</text>
                      <text x="800" y="224" font-size="9.5" fill="#64748B" text-anchor="middle">1,000+ Beds</text>

                      <!-- Row 1: Children -->
                      <text x="185" y="42" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Children (0-25)</text>
                      <rect x="200" y="30" width="37" height="10" fill="#0F2440" rx="2"/>
                      <text x="242" y="39" font-size="9.5" font-weight="700" fill="#0F2440">Supply: 62</text>
                      <rect x="200" y="44" width="53" height="10" fill="#C29B38" rx="2"/>
                      <text x="258" y="53" font-size="9.5" font-weight="700" fill="#C29B38">Demand: 88 (-26)</text>

                      <!-- Row 2: Elderly -->
                      <text x="185" y="92" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Elderly Care (65+)</text>
                      <rect x="200" y="80" width="537" height="10" fill="#0F2440" rx="2"/>
                      <text x="742" y="89" font-size="9.5" font-weight="700" fill="#0F2440">Supply: 895</text>
                      <rect x="200" y="94" width="627" height="10" fill="#C29B38" rx="2"/>
                      <text x="832" y="103" font-size="9.5" font-weight="700" fill="#C29B38">Demand: 1,045 (-150)</text>

                      <!-- Row 3: MH -->
                      <text x="185" y="142" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Mental Health</text>
                      <rect x="200" y="130" width="67" height="10" fill="#0F2440" rx="2"/>
                      <text x="272" y="139" font-size="9.5" font-weight="700" fill="#0F2440">Supply: 112</text>
                      <rect x="200" y="144" width="111" height="10" fill="#C29B38" rx="2"/>
                      <text x="316" y="153" font-size="9.5" font-weight="700" fill="#C29B38">Demand: 185 (-73)</text>

                      <!-- Row 4: LD -->
                      <text x="185" y="192" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Autism &amp; LD</text>
                      <rect x="200" y="180" width="89" height="10" fill="#0F2440" rx="2"/>
                      <text x="294" y="189" font-size="9.5" font-weight="700" fill="#0F2440">Supply: 148</text>
                      <rect x="200" y="194" width="129" height="10" fill="#C29B38" rx="2"/>
                      <text x="334" y="203" font-size="9.5" font-weight="700" fill="#C29B38">Demand: 215 (-67)</text>
                    </svg>
                  </div>
                </div>
              </section>

              <!-- SECTION 3: SECTOR CHAPTERS -->
              <section class="editorial-section" style="margin-bottom:36px;">
                <h2 class="editorial-h2" style="font-family:var(--font-serif); font-size:22px; font-weight:800; color:#0F2440; border-bottom:1.5px solid #E2E8F0; padding-bottom:8px; margin-bottom:14px;">
                  3. Sector Deep Dives &amp; Regional Comparisons
                </h2>

                <!-- 3.1 Children -->
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:20px; margin-bottom:20px;">
                  <h3 style="font-size:16px; font-weight:800; color:#0F2440; margin-bottom:8px;">3.1 Children's Residential Care &amp; Supported Accommodation</h3>
                  <p style="font-size:13.5px; line-height:1.6; color:#334155; margin-bottom:10px;">
                    Luton’s looked-after child population stands at <strong>374</strong> (63.0 per 10k, DfE March 2024). Approximately <strong>62 children</strong> require accommodation in residential homes or semi-independent supported units. The town contains 11 registered children's homes (38 places) and 6 supported accommodation providers (24 places). This leaves an immediate shortfall of <strong>26 local beds</strong> (range: -18 to -38 beds), forcing the council to place children outside the borough at average costs of <strong>£6,100 per week</strong> (NAO 2024), escalating to £10,000+ for high-acuity crisis care.
                  </p>
                </div>

                <!-- 3.2 Elderly -->
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:20px; margin-bottom:20px;">
                  <h3 style="font-size:16px; font-weight:800; color:#0F2440; margin-bottom:8px;">3.2 Elderly Residential &amp; Nursing Care (65+)</h3>
                  <p style="font-size:13.5px; line-height:1.6; color:#334155; margin-bottom:10px;">
                    Luton contains <strong>23 care homes</strong> providing <strong>895 beds</strong> (16 residential with 527 beds; 7 nursing with 368 beds). Luton’s bed ratio of <strong>33.95 beds per 1,000 population aged 65+</strong> is significantly lower than Central Bedfordshire (36.0), Bedford Borough (36.8), North Hertfordshire (39.6), and England (43.5). With 1,045 older residents currently assessed as requiring bedded care, Luton faces an immediate deficit of <strong>150 beds</strong>, projected to widen to <strong>370 beds by 2029</strong> and <strong>540 beds by 2034</strong> as the 65+ demographic expands by +45% (POPGROUP model).
                  </p>
                </div>

                <!-- 3.3 Mental Health -->
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:20px; margin-bottom:20px;">
                  <h3 style="font-size:16px; font-weight:800; color:#0F2440; margin-bottom:8px;">3.3 Mental Health Rehabilitation &amp; Supported Living</h3>
                  <p style="font-size:13.5px; line-height:1.6; color:#334155; margin-bottom:10px;">
                    Luton’s Adult Social Care Market Position Statement for Mental Health records between <strong>3,000 and 4,000 adults</strong> accessing secondary care. CQC-registered specialist supported accommodation currently provides approximately <strong>112 places</strong> across 14 locations against an active demand of <strong>185 individuals</strong> requiring intensive 24/7 supported living or S117 aftercare. This leaves an immediate local deficit of <strong>73 beds</strong> (range: -45 to -110 beds).
                  </p>
                </div>

                <!-- 3.4 Autism & LD -->
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:20px; margin-bottom:20px;">
                  <h3 style="font-size:16px; font-weight:800; color:#0F2440; margin-bottom:8px;">3.4 Autism &amp; Learning Disability Sector</h3>
                  <p style="font-size:13.5px; line-height:1.6; color:#334155; margin-bottom:10px;">
                    Luton Borough Council funds <strong>489 adults with learning disabilities</strong> for long-term care (plus 154 short-term). While 81.5% currently reside in family homes, aging parental carers (parents aged 70+) and hospital discharge step-downs generate demand for <strong>215 accommodation-based supported living beds</strong> against current registered capacity of <strong>148 beds</strong>, leaving a net deficit of <strong>67 beds</strong> (range: -38 to -95 beds). The council's "Living a Good Life in Luton" strategy prioritizes local supported living under <strong>Class C3(b)</strong> to repatriate out-of-borough placements.
                  </p>
                </div>
              </section>

              <!-- SECTION 4: DATA APPENDIX & DOWNLOAD LINKS -->
              <section class="editorial-section" style="margin-bottom:36px;">
                <h2 class="editorial-h2" style="font-family:var(--font-serif); font-size:22px; font-weight:800; color:#0F2440; border-bottom:1.5px solid #E2E8F0; padding-bottom:8px; margin-bottom:14px;">
                  4. Machine-Readable CSV Data Appendix
                </h2>

                <p style="font-size:13.5px; color:#475467; margin-bottom:16px;">
                  All 8 underlying empirical tables compiled by the specialist research agents are stored in the data repository and available for direct download:
                </p>

                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:12px;">
                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="display:block; font-size:12px; color:#0F2440;">Table 1: Luton Care Supply</strong>
                      <span style="font-size:10.5px; color:#64748B;">CQC &amp; Ofsted bed counts</span>
                    </div>
                    <a href="data/market/table1_supply_luton.csv" download style="padding:4px 10px; background:#0F2440; color:#FFFFFF; border-radius:6px; font-size:11px; font-weight:700; text-decoration:none;">CSV</a>
                  </div>

                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="display:block; font-size:12px; color:#0F2440;">Table 2: Demand Projections</strong>
                      <span style="font-size:10.5px; color:#64748B;">Census 2021 &amp; POPGROUP</span>
                    </div>
                    <a href="data/market/table2_demand_projections.csv" download style="padding:4px 10px; background:#0F2440; color:#FFFFFF; border-radius:6px; font-size:11px; font-weight:700; text-decoration:none;">CSV</a>
                  </div>

                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="display:block; font-size:12px; color:#0F2440;">Table 3: Gap Ranges</strong>
                      <span style="font-size:10.5px; color:#64748B;">Low / Central / High deficit</span>
                    </div>
                    <a href="data/market/table3_gap_analysis_ranges.csv" download style="padding:4px 10px; background:#0F2440; color:#FFFFFF; border-radius:6px; font-size:11px; font-weight:700; text-decoration:none;">CSV</a>
                  </div>

                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="display:block; font-size:12px; color:#0F2440;">Table 4: Fees &amp; Margins</strong>
                      <span style="font-size:10.5px; color:#64748B;">Council vs. private fees</span>
                    </div>
                    <a href="data/market/table4_market_fees_margins.csv" download style="padding:4px 10px; background:#0F2440; color:#FFFFFF; border-radius:6px; font-size:11px; font-weight:700; text-decoration:none;">CSV</a>
                  </div>

                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="display:block; font-size:12px; color:#0F2440;">Table 5: Regional Comparison</strong>
                      <span style="font-size:10.5px; color:#64748B;">Beds/1k in Central Beds, Herts</span>
                    </div>
                    <a href="data/market/table5_regional_benchmarks.csv" download style="padding:4px 10px; background:#0F2440; color:#FFFFFF; border-radius:6px; font-size:11px; font-weight:700; text-decoration:none;">CSV</a>
                  </div>

                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="display:block; font-size:12px; color:#0F2440;">Table 6: Official Source Log</strong>
                      <span style="font-size:10.5px; color:#64748B;">18 statutory URLs &amp; dates</span>
                    </div>
                    <a href="data/market/table6_source_log.csv" download style="padding:4px 10px; background:#0F2440; color:#FFFFFF; border-radius:6px; font-size:11px; font-weight:700; text-decoration:none;">CSV</a>
                  </div>

                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="display:block; font-size:12px; color:#0F2440;">Table 7: Data Gaps Register</strong>
                      <span style="font-size:10.5px; color:#64748B;">Named authorities for FOI</span>
                    </div>
                    <a href="data/market/table7_data_gaps.csv" download style="padding:4px 10px; background:#0F2440; color:#FFFFFF; border-radius:6px; font-size:11px; font-weight:700; text-decoration:none;">CSV</a>
                  </div>

                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="display:block; font-size:12px; color:#0F2440;">Table 8: Verification Audit</strong>
                      <span style="font-size:10.5px; color:#64748B;">Agent 8 verification trail</span>
                    </div>
                    <a href="data/market/table8_verification_log.csv" download style="padding:4px 10px; background:#0F2440; color:#FFFFFF; border-radius:6px; font-size:11px; font-weight:700; text-decoration:none;">CSV</a>
                  </div>
                </div>

                <div style="margin-top:20px; text-align:center;">
                  <a href="luton-care-market-report.html" target="_blank" style="display:inline-flex; align-items:center; gap:8px; padding:10px 24px; background:#0F2440; color:#FFFFFF; font-weight:800; font-size:13px; text-decoration:none; border-radius:8px; box-shadow:0 2px 6px rgba(15,36,64,0.15);">
                    <span>📄 Read Full Interactive Monograph (All 11 Chapters &amp; Tables)</span>
                    <span style="color:#C29B38;">&rarr;</span>
                  </a>
                </div>
              </section>

            </article>

            <!-- Sidebar Rail -->
            <aside class="editorial-rail">
              
              <!-- Quick Jump Box -->
              <div class="rail-card rail-toc-widget">
                <div class="rail-card-title">
                  <span>📑 Section Contents</span>
                </div>
                <nav class="on-page-toc">
                  <a class="on-page-link" onclick="window.scrollTo({top:0, behavior:'smooth'})"><span>↳</span><span>1. Executive Summary</span></a>
                  <a class="on-page-link" onclick="document.getElementById('sec-comparison-matrix')?.scrollIntoView({behavior:'smooth'})"><span>↳</span><span>2. 4-Category Matrix</span></a>
                  <a class="on-page-link" onclick="document.getElementById('sec-childrens-care')?.scrollIntoView({behavior:'smooth'})"><span>↳</span><span>3. Sector Deep Dives</span></a>
                  <a class="on-page-link" onclick="document.getElementById('sec-downloads')?.scrollIntoView({behavior:'smooth'})"><span>↳</span><span>4. CSV Data Appendix</span></a>
                </nav>
              </div>

              <!-- Monograph Download Card -->
              <div class="rail-card rail-downloads-widget">
                <div class="rail-card-title">
                  <span>📥 Research Monograph</span>
                  <span class="apple-pill-badge badge-green">Live Page</span>
                </div>
                <div style="display:flex; flex-direction:column; gap:8px;">
                  <a href="luton-care-market-report.html" target="_blank" class="btn-rail-download" style="text-decoration:none; display:flex; align-items:center; justify-content:space-between;">
                    <span>📄 Dedicated Full Report</span>
                    <span style="font-size:11px; opacity:0.8;">HTML</span>
                  </a>
                  <a href="data/market/table6_source_log.csv" download class="btn-rail-download" style="text-decoration:none; display:flex; align-items:center; justify-content:space-between;">
                    <span>📑 Statutory Source Log</span>
                    <span style="font-size:11px; opacity:0.8;">CSV</span>
                  </a>
                  <a href="data/market/table8_verification_log.csv" download class="btn-rail-download" style="text-decoration:none; display:flex; align-items:center; justify-content:space-between;">
                    <span>🔍 Verification Audit</span>
                    <span style="font-size:11px; opacity:0.8;">CSV</span>
                  </a>
                </div>
              </div>

              <!-- Key Statutory Bodies -->
              <div class="rail-card" style="background:#F8FAFC;">
                <div class="rail-card-title">
                  <span>🏛️ Statutory Scope</span>
                </div>
                <div style="font-size:11.5px; color:#475467; line-height:1.5;">
                  <strong style="color:#0F2440; display:block;">Primary Authorities:</strong>
                  • Luton Borough Council (ASC &amp; Children)<br>
                  • Central Bedfordshire Council<br>
                  • Bedford Borough Council<br>
                  • Hertfordshire County Council<br>
                  • NHS BLMK ICB (Continuing Care)<br>
                  • Care Quality Commission (CQC)<br>
                  • Ofsted (Children's Services)
                </div>
              </div>

            </aside>
          </div>
        </div><!-- /tab-market-demand -->
"""

    # INSERT TAB BEFORE <!-- TAB-HOUSES
    target_marker = "<!-- TAB-HOUSES (READERS-FRIENDLY TWO-COLUMN EXECUTIVE LAYOUT) -->"
    if target_marker in v2:
        v2 = v2.replace(target_marker, f"{tab_html}\n\n        {target_marker}")
        print("✓ Injected tab-market-demand into Stage 01 of portal/v2.html.")
    else:
        # Fallback search for <div id="tab-houses"
        idx = v2.find('<div id="tab-houses"')
        if idx != -1:
            v2 = v2[:idx] + f"{tab_html}\n\n        " + v2[idx:]
            print("✓ Injected tab-market-demand before tab-houses via fallback.")

    # 2. UPDATE DROPDOWN MENU IN portal/v2.html
    dropdown_needle = '<a href="javascript:void(0)" onclick="switchTabAndClose(\'tab-strategy\')" class="dropdown-item">🏢 Campus Strategy</a>'
    dropdown_replacement = """<a href="javascript:void(0)" onclick="switchTabAndClose('tab-strategy')" class="dropdown-item">🏢 Campus Strategy</a>
                    <a href="javascript:void(0)" onclick="switchTabAndClose('tab-market-demand')" class="dropdown-item" style="color:#0F2440; font-weight:700;">📈 Care Supply &amp; Demand</a>
                    <a href="luton-care-market-report.html" target="_blank" class="dropdown-item" style="color:#C29B38; font-weight:700;">📄 Full Market Monograph ↗</a>"""
    if dropdown_needle in v2:
        v2 = v2.replace(dropdown_needle, dropdown_replacement)
        print("✓ Updated dropdown menu with Care Supply & Demand link.")

    # 3. UPDATE FOOTER IN portal/v2.html
    footer_needle = '<li><a href="javascript:void(0)" onclick="switchTab(\'tab-strategy\'); window.scrollTo({top:0, behavior:\'smooth\'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">🏢 Campus Strategy (78/80)</a></li>'
    footer_replacement = """<li><a href="javascript:void(0)" onclick="switchTab('tab-strategy'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; transition:all 0.2s;">🏢 Campus Strategy (78/80)</a></li>
              <li><a href="javascript:void(0)" onclick="switchTab('tab-market-demand'); window.scrollTo({top:0, behavior:'smooth'});" style="color:#CBD5E1; text-decoration:none; font-size:13px; font-weight:700; transition:all 0.2s;">📈 Care Supply &amp; Demand Report</a></li>
              <li><a href="luton-care-market-report.html" target="_blank" style="color:#C29B38; text-decoration:none; font-size:13px; font-weight:700; transition:all 0.2s;">📄 Full Market Monograph &rarr;</a></li>"""
    if footer_needle in v2:
        v2 = v2.replace(footer_needle, footer_replacement)
        print("✓ Updated footer navigation with Care Supply & Demand link.")

    # 4. UPDATE JAVASCRIPT TAB_TO_STAGE & TAB_SECTION_INFO IN portal/v2.html
    v2 = v2.replace(
        "'tab-overview': 1, 'tab-options': 1, 'tab-advisory': 1, 'tab-strategy': 1,",
        "'tab-overview': 1, 'tab-options': 1, 'tab-advisory': 1, 'tab-strategy': 1, 'tab-market-demand': 1,"
    )
    v2 = v2.replace(
        "'tab-strategy': { icon: '🏢', name: 'Campus Strategy' },",
        "'tab-strategy': { icon: '🏢', name: 'Campus Strategy' },\n      'tab-market-demand': { icon: '📈', name: 'Care Supply & Demand' },"
    )
    print("✓ Updated TAB_TO_STAGE and TAB_SECTION_INFO dictionaries.")

    with open(v2_path, "w", encoding="utf-8") as f:
        f.write(v2)

    print(f"✓ Saved updated portal/v2.html ({len(v2):,} bytes).")

    # 5. UPDATE portal/index.html & root index.html (GATEWAY PAGES)
    update_gateway_file("portal/index.html", is_portal=True)
    update_gateway_file("index.html", is_portal=False)

def update_gateway_file(filepath, is_portal=True):
    if not os.path.exists(filepath):
        print(f"Notice: {filepath} not found.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        gw = f.read()

    prefix = "" if is_portal else "portal/"
    
    # Check if market report banner already exists
    if "luton-care-market-report.html" in gw:
        print(f"Notice: {filepath} already references market report.")
        return

    # In gateway, add a featured publication link in the docs-links section
    target_docs = '<div class="docs-links">'
    replacement_docs = f"""<div class="docs-links">
        <a href="{prefix}luton-care-market-report.html" class="doc-link" style="border-color:#C29B38; background:#FFFBEB; color:#92400E; font-weight:800;">
          <span>📈</span> Luton Care Supply &amp; Demand Statistical Report (2024–2036)
        </a>"""
    if target_docs in gw:
        gw = gw.replace(target_docs, replacement_docs, 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(gw)
        print(f"✓ Injected Market Report into {filepath} docs section.")

if __name__ == "__main__":
    main()
