#!/usr/bin/env python3
"""
scripts/generate_market_svg_charts.py
Generates 6 publication-grade SVG charts representing all CSV datasets for decision-makers:
1. chart_market_supply_capacity.svg (Table 1: Bed Capacity by Sector)
2. chart_market_quality_ratings.svg (Table 1: Inspection Ratings Breakdown)
3. chart_market_demand_projections.svg (Table 2: 10-Year Demand Trajectories)
4. chart_market_gap_waterfall.svg (Table 3: Net Bed Deficit Ranges)
5. chart_market_fees_margin_gap.svg (Table 4: Council vs Private vs Fair Cost Fees)
6. chart_market_regional_bed_density.svg (Table 5: Beds per 1,000 Pop 65+ Benchmark)
"""

import os

def generate_svgs():
    dirs = ["portal/assets/diagrams", "assets/diagrams"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

    # -------------------------------------------------------------------------
    # CHART 1: SUPPLY CAPACITY (TABLE 1)
    # -------------------------------------------------------------------------
    chart1_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="340" viewBox="0 0 860 340" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect width="860" height="340" fill="#FFFFFF" rx="8"/>
  <text x="30" y="32" font-size="15" font-weight="800" fill="#0F2440">Chart 1: Registered Bed &amp; Placement Capacity in Luton by Sector (2024)</text>
  <text x="30" y="50" font-size="11.5" fill="#64748B">Source: Table 1 (table1_supply_luton.csv) • CQC Care Directory &amp; Ofsted Children's Social Care</text>

  <!-- Grid lines -->
  <line x1="260" y1="80" x2="810" y2="80" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="260" y1="125" x2="810" y2="125" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="260" y1="170" x2="810" y2="170" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="260" y1="215" x2="810" y2="215" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="260" y1="260" x2="810" y2="260" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="260" y1="300" x2="810" y2="300" stroke="#CBD5E1" stroke-width="1.5"/>

  <!-- Ticks -->
  <text x="260" y="316" font-size="10" fill="#64748B" text-anchor="middle">0</text>
  <text x="397" y="316" font-size="10" fill="#64748B" text-anchor="middle">150</text>
  <text x="535" y="316" font-size="10" fill="#64748B" text-anchor="middle">300</text>
  <text x="672" y="316" font-size="10" fill="#64748B" text-anchor="middle">450</text>
  <text x="810" y="316" font-size="10" fill="#64748B" text-anchor="middle">600 Beds</text>

  <!-- Bar 1: Older People Residential (527 beds) -->
  <text x="245" y="96" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">OP Residential (16 Homes)</text>
  <rect x="260" y="82" width="483" height="22" fill="#0F2440" rx="4"/>
  <text x="752" y="98" font-size="11" font-weight="800" fill="#0F2440">527 Beds (19.99/1k 65+)</text>

  <!-- Bar 2: Older People Nursing (368 beds) -->
  <text x="245" y="141" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">OP Nursing (7 Homes)</text>
  <rect x="260" y="127" width="337" height="22" fill="#1E3A5F" rx="4"/>
  <text x="607" y="143" font-size="11" font-weight="800" fill="#1E3A5F">368 Beds (13.96/1k 65+)</text>

  <!-- Bar 3: Autism & Learning Disability (148 places) -->
  <text x="245" y="186" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Autism &amp; LD (19 Services)</text>
  <rect x="260" y="172" width="135" height="22" fill="#C29B38" rx="4"/>
  <text x="405" y="188" font-size="11" font-weight="800" fill="#8C6A17">148 Places (1.05/1k 18-64)</text>

  <!-- Bar 4: Mental Health Rehab (112 places) -->
  <text x="245" y="231" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Mental Health (14 Services)</text>
  <rect x="260" y="217" width="102" height="22" fill="#2563EB" rx="4"/>
  <text x="372" y="233" font-size="11" font-weight="800" fill="#1D4ED8">112 Places (0.80/1k 18-64)</text>

  <!-- Bar 5: Children's Residential & Supported (62 places) -->
  <text x="245" y="276" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Children (0-25) (17 Services)</text>
  <rect x="260" y="262" width="57" height="22" fill="#166534" rx="4"/>
  <text x="327" y="278" font-size="11" font-weight="800" fill="#166534">62 Places (38 Res + 24 Supp)</text>
</svg>"""

    # -------------------------------------------------------------------------
    # CHART 2: REGULATORY RATINGS BREAKDOWN (TABLE 1)
    # -------------------------------------------------------------------------
    chart2_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="280" viewBox="0 0 860 280" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect width="860" height="280" fill="#FFFFFF" rx="8"/>
  <text x="30" y="30" font-size="15" font-weight="800" fill="#0F2440">Chart 2: Quality &amp; Regulatory Risk Breakdown by Sector (% Ratings)</text>
  <text x="30" y="48" font-size="11.5" fill="#64748B">Source: Table 1 (table1_supply_luton.csv) • CQC Directory (Oct 2024) &amp; Ofsted SCCIF Inspection Reports</text>

  <!-- Legend -->
  <rect x="260" y="62" width="12" height="12" fill="#166534" rx="2"/><text x="278" y="72" font-size="11" fill="#334155">Outstanding</text>
  <rect x="370" y="62" width="12" height="12" fill="#0F2440" rx="2"/><text x="388" y="72" font-size="11" fill="#334155">Good</text>
  <rect x="445" y="62" width="12" height="12" fill="#D97706" rx="2"/><text x="463" y="72" font-size="11" fill="#334155">Requires Improvement</text>
  <rect x="615" y="62" width="12" height="12" fill="#DC2626" rx="2"/><text x="633" y="72" font-size="11" fill="#334155">Inadequate / Special Measures</text>

  <!-- Row 1: OP Residential -->
  <text x="245" y="112" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">OP Residential</text>
  <rect x="260" y="98" width="34" height="20" fill="#166534" rx="2"/>
  <rect x="295" y="98" width="371" height="20" fill="#0F2440"/>
  <rect x="667" y="98" width="102" height="20" fill="#D97706"/>
  <rect x="770" y="98" width="34" height="20" fill="#DC2626" rx="2"/>
  <text x="812" y="113" font-size="10.5" font-weight="700" fill="#DC2626">25% Risk</text>

  <!-- Row 2: OP Nursing -->
  <text x="245" y="152" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">OP Nursing</text>
  <rect x="260" y="138" width="386" height="20" fill="#0F2440" rx="2"/>
  <rect x="647" y="138" width="155" height="20" fill="#D97706" rx="2"/>
  <text x="812" y="153" font-size="10.5" font-weight="700" fill="#D97706">28.6% RI</text>

  <!-- Row 3: Autism & Learning Dis. -->
  <text x="245" y="192" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Autism &amp; LD</text>
  <rect x="260" y="178" width="57" height="20" fill="#166534" rx="2"/>
  <rect x="318" y="178" width="427" height="20" fill="#0F2440"/>
  <rect x="746" y="178" width="57" height="20" fill="#D97706" rx="2"/>
  <text x="812" y="193" font-size="10.5" font-weight="700" fill="#166534">89.4% Safe</text>

  <!-- Row 4: Children's Homes -->
  <text x="245" y="232" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Children's Homes (Ofsted)</text>
  <rect x="260" y="218" width="49" height="20" fill="#166534" rx="2"/>
  <rect x="310" y="218" width="344" height="20" fill="#0F2440"/>
  <rect x="655" y="218" width="98" height="20" fill="#D97706"/>
  <rect x="754" y="218" width="49" height="20" fill="#DC2626" rx="2"/>
  <text x="812" y="233" font-size="10.5" font-weight="700" fill="#DC2626">27.3% Risk</text>
</svg>"""

    # -------------------------------------------------------------------------
    # CHART 3: DEMAND PROJECTIONS (TABLE 2)
    # -------------------------------------------------------------------------
    chart3_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="320" viewBox="0 0 860 320" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect width="860" height="320" fill="#FFFFFF" rx="8"/>
  <text x="30" y="30" font-size="15" font-weight="800" fill="#0F2440">Chart 3: 10-Year Escalation of Care Cohorts in Luton (2024 vs 2029 vs 2034)</text>
  <text x="30" y="48" font-size="11.5" fill="#64748B">Source: Table 2 (table2_demand_projections.csv) • ONS Census 2021 &amp; Luton POPGROUP Cohort Projections</text>

  <!-- Legend -->
  <rect x="320" y="62" width="12" height="12" fill="#0F2440" rx="2"/><text x="338" y="72" font-size="11" fill="#334155">Current (2024 Baseline)</text>
  <rect x="495" y="62" width="12" height="12" fill="#C29B38" rx="2"/><text x="513" y="72" font-size="11" fill="#334155">5-Year Need (2029)</text>
  <rect x="655" y="62" width="12" height="12" fill="#DC2626" rx="2"/><text x="673" y="72" font-size="11" fill="#334155">10-Year Need (2034)</text>

  <!-- Scale Line -->
  <line x1="260" y1="275" x2="810" y2="275" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="260" y="292" font-size="10" fill="#64748B" text-anchor="middle">0</text>
  <text x="397" y="292" font-size="10" fill="#64748B" text-anchor="middle">400</text>
  <text x="535" y="292" font-size="10" fill="#64748B" text-anchor="middle">800</text>
  <text x="672" y="292" font-size="10" fill="#64748B" text-anchor="middle">1,200</text>
  <text x="810" y="292" font-size="10" fill="#64748B" text-anchor="middle">1,600 People</text>

  <!-- Group 1: Elderly Bed Demand -->
  <text x="245" y="112" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Elderly Bed Need (65+)</text>
  <rect x="260" y="92" width="358" height="11" fill="#0F2440" rx="2"/>
  <rect x="260" y="105" width="434" height="11" fill="#C29B38" rx="2"/>
  <rect x="260" y="118" width="522" height="11" fill="#DC2626" rx="2"/>
  <text x="790" y="128" font-size="10" font-weight="800" fill="#DC2626">+45.5% (1,520)</text>

  <!-- Group 2: Adults with Learning Disability -->
  <text x="245" y="166" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Funded Adults LD Cohort</text>
  <rect x="260" y="146" width="168" height="11" fill="#0F2440" rx="2"/>
  <rect x="260" y="159" width="183" height="11" fill="#C29B38" rx="2"/>
  <rect x="260" y="172" width="204" height="11" fill="#DC2626" rx="2"/>
  <text x="472" y="182" font-size="10" font-weight="800" fill="#0F2440">489 &rarr; 595</text>

  <!-- Group 3: Looked After Children (CLA) -->
  <text x="245" y="220" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Looked After Children</text>
  <rect x="260" y="200" width="128" height="11" fill="#0F2440" rx="2"/>
  <rect x="260" y="213" width="135" height="11" fill="#C29B38" rx="2"/>
  <rect x="260" y="226" width="146" height="11" fill="#DC2626" rx="2"/>
  <text x="414" y="236" font-size="10" font-weight="800" fill="#0F2440">374 &rarr; 425</text>
</svg>"""

    # -------------------------------------------------------------------------
    # CHART 4: GAP WATERFALL RANGES (TABLE 3)
    # -------------------------------------------------------------------------
    chart4_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="300" viewBox="0 0 860 300" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect width="860" height="300" fill="#FFFFFF" rx="8"/>
  <text x="30" y="30" font-size="15" font-weight="800" fill="#0F2440">Chart 4: Supply-Demand Net Deficit Ranges by Care Sector (Beds)</text>
  <text x="30" y="48" font-size="11.5" fill="#64748B">Source: Table 3 (table3_gap_analysis_ranges.csv) • Sensitivity Bounds: Low, Central, and High Scenarios</text>

  <!-- Legend -->
  <rect x="360" y="62" width="12" height="12" fill="#FCA5A5" rx="2"/><text x="378" y="72" font-size="11" fill="#334155">Low Deficit</text>
  <rect x="475" y="62" width="12" height="12" fill="#EF4444" rx="2"/><text x="493" y="72" font-size="11" fill="#334155">Central Gap</text>
  <rect x="590" y="62" width="12" height="12" fill="#991B1B" rx="2"/><text x="608" y="72" font-size="11" fill="#334155">High Deficit (Severe)</text>

  <!-- Scale Line -->
  <line x1="260" y1="255" x2="810" y2="255" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="260" y="272" font-size="10" fill="#64748B" text-anchor="middle">0</text>
  <text x="397" y="272" font-size="10" fill="#64748B" text-anchor="middle">-60</text>
  <text x="535" y="272" font-size="10" fill="#64748B" text-anchor="middle">-120</text>
  <text x="672" y="272" font-size="10" fill="#64748B" text-anchor="middle">-180</text>
  <text x="810" y="272" font-size="10" fill="#64748B" text-anchor="middle">-240 Bed Deficit</text>

  <!-- Sector 1: Elderly (85 to 225) -->
  <text x="245" y="104" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Elderly Care (65+)</text>
  <rect x="260" y="86" width="194" height="9" fill="#FCA5A5" rx="2"/>
  <rect x="260" y="97" width="343" height="9" fill="#EF4444" rx="2"/>
  <rect x="260" y="108" width="514" height="9" fill="#991B1B" rx="2"/>
  <text x="782" y="103" font-size="10.5" font-weight="800" fill="#991B1B">Gap: -150 (-85 to -225)</text>

  <!-- Sector 2: Mental Health (45 to 110) -->
  <text x="245" y="146" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Mental Health Rehab</text>
  <rect x="260" y="128" width="103" height="9" fill="#FCA5A5" rx="2"/>
  <rect x="260" y="139" width="167" height="9" fill="#EF4444" rx="2"/>
  <rect x="260" y="150" width="251" height="9" fill="#991B1B" rx="2"/>
  <text x="520" y="145" font-size="10.5" font-weight="800" fill="#991B1B">Gap: -73 (-45 to -110)</text>

  <!-- Sector 3: Autism & LD (38 to 95) -->
  <text x="245" y="188" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Autism &amp; Learning Dis.</text>
  <rect x="260" y="170" width="87" height="9" fill="#FCA5A5" rx="2"/>
  <rect x="260" y="181" width="153" height="9" fill="#EF4444" rx="2"/>
  <rect x="260" y="192" width="217" height="9" fill="#991B1B" rx="2"/>
  <text x="485" y="187" font-size="10.5" font-weight="800" fill="#991B1B">Gap: -67 (-38 to -95)</text>

  <!-- Sector 4: Children (18 to 38) -->
  <text x="245" y="230" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Children (0-25)</text>
  <rect x="260" y="212" width="41" height="9" fill="#FCA5A5" rx="2"/>
  <rect x="260" y="223" width="59" height="9" fill="#EF4444" rx="2"/>
  <rect x="260" y="234" width="87" height="9" fill="#991B1B" rx="2"/>
  <text x="355" y="229" font-size="10.5" font-weight="800" fill="#991B1B">Gap: -26 (-18 to -38)</text>
</svg>"""

    # -------------------------------------------------------------------------
    # CHART 5: MARKET FEES & DEFICITS (TABLE 4)
    # -------------------------------------------------------------------------
    chart5_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="310" viewBox="0 0 860 310" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect width="860" height="310" fill="#FFFFFF" rx="8"/>
  <text x="30" y="30" font-size="15" font-weight="800" fill="#0F2440">Chart 5: Weekly Fee Structure &amp; Operating Cost Gaps (£ / Week)</text>
  <text x="30" y="48" font-size="11.5" fill="#64748B">Source: Table 4 (table4_market_fees_margins.csv) • Luton Scales of Charges, DHSC Fair Cost &amp; NAO</text>

  <!-- Legend -->
  <rect x="350" y="62" width="12" height="12" fill="#0F2440" rx="2"/><text x="368" y="72" font-size="11" fill="#334155">Council Base Rate</text>
  <rect x="495" y="62" width="12" height="12" fill="#C29B38" rx="2"/><text x="513" y="72" font-size="11" fill="#334155">Fair Cost / Benchmark</text>
  <rect x="660" y="62" width="12" height="12" fill="#166534" rx="2"/><text x="678" y="72" font-size="11" fill="#334155">Private / Market Rate</text>

  <!-- Scale Line -->
  <line x1="260" y1="265" x2="810" y2="265" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="260" y="282" font-size="10" fill="#64748B" text-anchor="middle">£0</text>
  <text x="397" y="282" font-size="10" fill="#64748B" text-anchor="middle">£1,750</text>
  <text x="535" y="282" font-size="10" fill="#64748B" text-anchor="middle">£3,500</text>
  <text x="672" y="282" font-size="10" fill="#64748B" text-anchor="middle">£5,250</text>
  <text x="810" y="282" font-size="10" fill="#64748B" text-anchor="middle">£7,000 / Wk</text>

  <!-- Row 1: Children's Residential Home (£6,100 avg) -->
  <text x="245" y="104" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Children's Residential</text>
  <rect x="260" y="88" width="434" height="10" fill="#0F2440" rx="2"/>
  <rect x="260" y="101" width="479" height="10" fill="#C29B38" rx="2"/>
  <rect x="260" y="114" width="510" height="10" fill="#166534" rx="2"/>
  <text x="780" y="112" font-size="10.5" font-weight="800" fill="#0F2440">£6,100 (NAO)</text>

  <!-- Row 2: Autism & LD Supported Living (£2,350 blended) -->
  <text x="245" y="158" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Autism &amp; LD Campus</text>
  <rect x="260" y="142" width="176" height="10" fill="#0F2440" rx="2"/>
  <rect x="260" y="155" width="185" height="10" fill="#C29B38" rx="2"/>
  <rect x="260" y="168" width="220" height="10" fill="#166534" rx="2"/>
  <text x="490" y="166" font-size="10.5" font-weight="800" fill="#0F2440">£2,350/wk Avg</text>

  <!-- Row 3: Older People Residential (£947 vs £1,055 fair cost) -->
  <text x="245" y="212" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">OP Residential (65+)</text>
  <rect x="260" y="196" width="74" height="10" fill="#0F2440" rx="2"/>
  <rect x="260" y="209" width="83" height="10" fill="#C29B38" rx="2"/>
  <rect x="260" y="222" width="105" height="10" fill="#166534" rx="2"/>
  <text x="375" y="220" font-size="10.5" font-weight="800" fill="#DC2626">-£191 Deficit</text>
</svg>"""

    # -------------------------------------------------------------------------
    # CHART 6: REGIONAL BED DENSITY BENCHMARK (TABLE 5)
    # -------------------------------------------------------------------------
    chart6_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="340" viewBox="0 0 860 340" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect width="860" height="340" fill="#FFFFFF" rx="8"/>
  <text x="30" y="30" font-size="15" font-weight="800" fill="#0F2440">Chart 6: Care Home Bed Density Benchmark (Beds per 1,000 Population 65+)</text>
  <text x="30" y="48" font-size="11.5" fill="#64748B">Source: Table 5 (table5_regional_benchmarks.csv) • ONS Census 2021 &amp; CQC Local Authority Profiles</text>

  <!-- National England Target Line -->
  <line x1="680" y1="75" x2="680" y2="290" stroke="#DC2626" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="680" y="70" font-size="10.5" font-weight="800" fill="#DC2626" text-anchor="middle">England Average: 43.5 Beds / 1k</text>

  <!-- Scale Line -->
  <line x1="260" y1="290" x2="810" y2="290" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="260" y="306" font-size="10" fill="#64748B" text-anchor="middle">0</text>
  <text x="397" y="306" font-size="10" fill="#64748B" text-anchor="middle">12.5</text>
  <text x="535" y="306" font-size="10" fill="#64748B" text-anchor="middle">25.0</text>
  <text x="672" y="306" font-size="10" fill="#64748B" text-anchor="middle">37.5</text>
  <text x="810" y="306" font-size="10" fill="#64748B" text-anchor="middle">50.0 Beds / 1k</text>

  <!-- Row 1: Luton (33.95) -->
  <text x="245" y="102" font-size="11.5" font-weight="800" fill="#DC2626" text-anchor="end">Luton Borough Council</text>
  <rect x="260" y="88" width="373" height="20" fill="#DC2626" rx="3"/>
  <text x="640" y="103" font-size="11" font-weight="800" fill="#DC2626">33.95 (Severe Deficit: -22.0%)</text>

  <!-- Row 2: Central Beds (36.0) -->
  <text x="245" y="137" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Central Bedfordshire</text>
  <rect x="260" y="123" width="396" height="20" fill="#0F2440" rx="3"/>
  <text x="663" y="138" font-size="11" font-weight="700" fill="#0F2440">36.00</text>

  <!-- Row 3: Bedford Borough (36.8) -->
  <text x="245" y="172" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Bedford Borough</text>
  <rect x="260" y="158" width="405" height="20" fill="#1E3A5F" rx="3"/>
  <text x="672" y="173" font-size="11" font-weight="700" fill="#1E3A5F">36.80</text>

  <!-- Row 4: North Hertfordshire (39.6) -->
  <text x="245" y="207" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">North Hertfordshire</text>
  <rect x="260" y="193" width="436" height="20" fill="#475467" rx="3"/>
  <text x="703" y="208" font-size="11" font-weight="700" fill="#475467">39.60</text>

  <!-- Row 5: Dacorum (40.3) -->
  <text x="245" y="242" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">Dacorum (Herts)</text>
  <rect x="260" y="228" width="443" height="20" fill="#475467" rx="3"/>
  <text x="710" y="243" font-size="11" font-weight="700" fill="#475467">40.30</text>

  <!-- Row 6: St Albans (43.1) -->
  <text x="245" y="277" font-size="11.5" font-weight="700" fill="#0F2440" text-anchor="end">St Albans (Herts)</text>
  <rect x="260" y="263" width="474" height="20" fill="#166534" rx="3"/>
  <text x="741" y="278" font-size="11" font-weight="700" fill="#166534">43.10</text>
</svg>"""

    charts = [
        ("chart_market_supply_capacity.svg", chart1_svg),
        ("chart_market_quality_ratings.svg", chart2_svg),
        ("chart_market_demand_projections.svg", chart3_svg),
        ("chart_market_gap_waterfall.svg", chart4_svg),
        ("chart_market_fees_margin_gap.svg", chart5_svg),
        ("chart_market_regional_bed_density.svg", chart6_svg)
    ]

    for d in dirs:
        for fname, svg in charts:
            fpath = os.path.join(d, fname)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(svg)
            print(f"✓ Wrote {fpath}")

if __name__ == "__main__":
    generate_svgs()
