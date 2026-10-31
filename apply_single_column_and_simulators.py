import re
import os

HTML_PATH = 'portal/v2.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

print('Initial v2.html length:', len(content))

# =========================================================================
# 1. READ GENERATED ARCHITECTURAL BLUEPRINT SVG
# =========================================================================
with open('portal/assets/diagrams/diagram_campus_masterplan.svg', 'r', encoding='utf-8') as f:
    blueprint_svg = f.read()

# Replace img tags referencing diagram_campus_masterplan.svg with inline SVG
img_pattern = r'<img\s+src=[\'"]assets/diagrams/diagram_campus_masterplan\.svg[\'"][^>]*>'
matches = list(re.finditer(img_pattern, content))
print(f'Found {len(matches)} occurrences of diagram_campus_masterplan.svg img tag.')

if matches:
    content = re.sub(img_pattern, blueprint_svg, content)
    print('Replaced all occurrences with inline Architectural Blueprint SVG!')

# =========================================================================
# 2. ENHANCE FIGURE 1.1, 1.2, 1.3 FONT SIZES & CLARITY
# =========================================================================
# In Figure 1.1 (Campus Topology)
def upscale_topology_fonts(text):
    # Upscale 8, 8.5, 9, 9.5 -> 12.5; 10, 10.5 -> 13.5; 11, 11.5 -> 14.5; 12 -> 15
    text = re.sub(r'font-size=[\'"](?:8|8\.5|9|9\.5)[\'"]', 'font-size="12.5"', text)
    text = re.sub(r'font-size=[\'"](?:10|10\.5)[\'"]', 'font-size="13.5"', text)
    text = re.sub(r'font-size=[\'"](?:11|11\.5)[\'"]', 'font-size="14.5"', text)
    return text

# In Figure 1.2 (Financial Waterfall)
def upscale_waterfall_fonts(text):
    text = re.sub(r'font-size=[\'"](?:8\.5|9|9\.5)[\'"]', 'font-size="12.5"', text)
    text = re.sub(r'font-size=[\'"](?:10|10\.5)[\'"]', 'font-size="13.5"', text)
    text = re.sub(r'font-size=[\'"](?:11|12)[\'"]', 'font-size="14.5"', text)
    return text

# In Figure 1.3 (Break-Even Curve)
def upscale_breakeven_fonts(text):
    text = re.sub(r'font-size=[\'"](?:9\.5|10)[\'"]', 'font-size="13"', text)
    text = re.sub(r'font-size=[\'"](?:11|11\.5)[\'"]', 'font-size="14.5"', text)
    return text

# Apply font upscaling to the three figures
fig1_match = re.search(r'(<figure class="figure-box" id="fig-campus-topology">[\s\S]*?</figure>)', content)
if fig1_match:
    old_f1 = fig1_match.group(1)
    new_f1 = upscale_topology_fonts(old_f1)
    content = content.replace(old_f1, new_f1, 1)
    print('Upscaled fonts in Figure 1.1 (Campus Topology)!')

fig2_matches = list(re.finditer(r'(<figure class="figure-box" id="fig-financial-waterfall">[\s\S]*?</figure>)', content))
for m in fig2_matches:
    old_f2 = m.group(1)
    new_f2 = upscale_waterfall_fonts(old_f2)
    content = content.replace(old_f2, new_f2, 1)
print(f'Upscaled fonts in Figure 1.2 ({len(fig2_matches)} occurrences)!')

fig3_match = re.search(r'(<figure class="figure-box" id="fig-breakeven-curve">[\s\S]*?</figure>)', content)
if fig3_match:
    old_f3 = fig3_match.group(1)
    new_f3 = upscale_breakeven_fonts(old_f3)
    content = content.replace(old_f3, new_f3, 1)
    print('Upscaled fonts in Figure 1.3 (Break-Even Curve)!')


# =========================================================================
# 3. SINGLE-COLUMN ACADEMIC RESEARCH CSS INJECTION
# =========================================================================
SINGLE_COLUMN_CSS = '''
/* =========================================================================
   1-COLUMN ACADEMIC RESEARCH JOURNAL ARCHITECTURE & ENHANCED TYPOGRAPHY
   ========================================================================= */
.editorial-layout {
  display: block !important;
  max-width: 1060px !important;
  margin: 0 auto !important;
  padding: 36px 32px 100px 32px !important;
}

.editorial-main {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}

/* Full-width Academic Companion Grid at Base of Single-Column Reading */
.editorial-rail {
  position: static !important;
  top: auto !important;
  max-height: none !important;
  overflow: visible !important;
  margin-top: 52px !important;
  margin-bottom: 28px !important;
  padding: 26px 30px !important;
  background: #F8FAFC !important;
  border: 1.5px solid var(--border, #E2E8F0) !important;
  border-radius: 12px !important;
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
  gap: 22px !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03) !important;
}

[data-theme="dark"] .editorial-rail {
  background: #141E33 !important;
  border-color: #334155 !important;
}

.editorial-rail .rail-card {
  margin-bottom: 0 !important;
  height: 100% !important;
}

/* Academic Research Typography Standards */
.editorial-prose-wrap,
.editorial-body,
.card-body,
.tab-pane p,
.tab-pane li {
  font-size: 16.5px !important;
  line-height: 1.76 !important;
  color: var(--text-main, #1E293B) !important;
  letter-spacing: -0.008em;
}

[data-theme="dark"] .editorial-prose-wrap,
[data-theme="dark"] .editorial-body,
[data-theme="dark"] .card-body,
[data-theme="dark"] .tab-pane p,
[data-theme="dark"] .tab-pane li {
  color: #E2E8F0 !important;
}

.page-title {
  font-family: "Charter", "Iowan Old Style", "Georgia", "Merriweather", serif !important;
  font-size: 30px !important;
  font-weight: 800 !important;
  line-height: 1.25 !important;
  color: var(--navy, #0F1E36) !important;
  letter-spacing: -0.02em !important;
}

[data-theme="dark"] .page-title {
  color: #F8FAFC !important;
}

.editorial-prose-wrap h2,
.card-title {
  font-family: "Charter", "Iowan Old Style", "Georgia", "Merriweather", serif !important;
  font-size: 22px !important;
  font-weight: 700 !important;
  color: var(--navy, #0F1E36) !important;
  margin-top: 36px !important;
  margin-bottom: 14px !important;
  line-height: 1.35 !important;
}

[data-theme="dark"] .editorial-prose-wrap h2,
[data-theme="dark"] .card-title {
  color: #F1F5F9 !important;
}

.editorial-prose-wrap h3 {
  font-size: 18.5px !important;
  font-weight: 700 !important;
  color: var(--navy, #0F1E36) !important;
  margin-top: 26px !important;
  margin-bottom: 12px !important;
}

[data-theme="dark"] .editorial-prose-wrap h3 {
  color: #93C5FD !important;
}

/* Academic Tables Readability */
.table-wrap table {
  font-size: 14.5px !important;
  line-height: 1.6 !important;
}

.table-wrap th {
  font-size: 14px !important;
  font-weight: 700 !important;
  padding: 12px 16px !important;
  letter-spacing: 0.02em !important;
}

.table-wrap td {
  padding: 13px 16px !important;
}

/* Architectural Blueprint Responsive Frame */
.blueprint-svg {
  width: 100% !important;
  height: auto !important;
  min-height: 480px;
  border: 1px solid #1E3E62;
  border-radius: 10px;
}
'''

if '/* 1-COLUMN ACADEMIC RESEARCH JOURNAL ARCHITECTURE' not in content:
    content = content.replace('</style>', SINGLE_COLUMN_CSS + '\n</style>', 1)
    print('Injected 1-Column Academic Research CSS!')


# =========================================================================
# 4. REPLACE SIMULATORS IN TAB-FINANCIALS
# =========================================================================
# New Combined Simulators HTML
SIMULATORS_HTML = '''
          <!-- =========================================================================
               1. ADVANCED DYNAMIC PLACEMENT FEE & BED OCCUPANCY SIMULATOR
               ========================================================================= -->
          <div class="card" id="sec-fin-simulator" style="border: 2px solid #2563EB; box-shadow: 0 4px 20px rgba(37, 99, 235, 0.08); margin-bottom: 36px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
              <div>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span class="badge" style="background:#2563EB; color:#FFFFFF; font-weight:800; font-size:12px;">SIMULATOR 01 // REVENUE ENGINE</span>
                  <h3 class="card-title" style="margin: 0; font-size: 22px;">Dynamic Placement Fee &amp; Bed Occupancy Simulator</h3>
                </div>
                <p style="font-size: 14.5px; color: var(--text-muted, #475569); margin-top: 6px;">
                  Adjust placement variables below to stress-test weekly fee compositions, occupancy thresholds, and annualized gross turnover:
                </p>
              </div>
              <span class="badge" style="background: #ECFDF5; color: #047857; border: 1px solid #10B981; font-weight: 700; font-size: 13px; padding: 6px 12px;">
                Campus Capacity: 8 Beds
              </span>
            </div>

            <div class="calc-card" style="background: #FAFAFC; border: 1.5px solid #E2E8F0; border-radius: 10px; padding: 22px;">
              <!-- Row 1: Bed Occupancy -->
              <div class="calc-row" style="margin-bottom: 18px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="beds-slider" style="display: block; font-weight: 700; font-size: 14.5px; color: #0F1E36;">
                    1. Occupied Campus Beds (1 to 8):
                  </label>
                  <span style="font-size: 12px; color: #64748B;">78 Marston Gdns (5 beds) + 80 Marston Gdns (3 beds)</span>
                </div>
                <input type="range" id="beds-slider" class="calc-slider" min="1" max="8" step="1" value="8" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="beds-val" class="calc-val-box" style="font-weight: 800; font-size: 16px; min-width: 125px; text-align: center; background: #2563EB; color: #FFF; padding: 6px 14px; border-radius: 6px;">8 Beds (100%)</span>
              </div>

              <!-- Row 2: Core Care Fee -->
              <div class="calc-row" style="margin-bottom: 18px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="core-fee-slider" style="display: block; font-weight: 700; font-size: 14.5px; color: #0F1E36;">
                    2. Core Care Weekly Fee (£ / res / wk):
                  </label>
                  <span style="font-size: 12px; color: #64748B;">Luton Council / NHS BLMK ICB standard core care fee</span>
                </div>
                <input type="range" id="core-fee-slider" class="calc-slider" min="800" max="1800" step="25" value="1100" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="core-fee-val" class="calc-val-box" style="font-weight: 800; font-size: 16px; min-width: 125px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 14px; border-radius: 6px;">£1,100 / wk</span>
              </div>

              <!-- Row 3: Commissioned 1:1 Care Hours -->
              <div class="calc-row" style="margin-bottom: 18px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="hours-1to1-slider" style="display: block; font-weight: 700; font-size: 14.5px; color: #0F1E36;">
                    3. Commissioned 1:1 Hours (hrs / res / wk):
                  </label>
                  <span style="font-size: 12px; color: #64748B;">Complex autism / PBS assessed 1:1 care hours</span>
                </div>
                <input type="range" id="hours-1to1-slider" class="calc-slider" min="0" max="60" step="1" value="35" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="hours-1to1-val" class="calc-val-box" style="font-weight: 800; font-size: 16px; min-width: 125px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 14px; border-radius: 6px;">35 hrs / wk</span>
              </div>

              <!-- Row 4: 1:1 Hourly Billing Rate -->
              <div class="calc-row" style="margin-bottom: 18px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="rate-1to1-slider" style="display: block; font-weight: 700; font-size: 14.5px; color: #0F1E36;">
                    4. 1:1 Hourly Billing Rate (£ / hr):
                  </label>
                  <span style="font-size: 12px; color: #64748B;">Luton DPS AT1115 contracted 1:1 hourly rate</span>
                </div>
                <input type="range" id="rate-1to1-slider" class="calc-slider" min="20.00" max="35.00" step="0.50" value="25.71" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="rate-1to1-val" class="calc-val-box" style="font-weight: 800; font-size: 16px; min-width: 125px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 14px; border-radius: 6px;">£25.71 / hr</span>
              </div>

              <!-- Row 5: Supported Exempt Housing Benefit -->
              <div class="calc-row" style="margin-bottom: 22px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="hb-slider" style="display: block; font-weight: 700; font-size: 14.5px; color: #0F1E36;">
                    5. Exempt Accommodation Housing Benefit (£ / res / wk):
                  </label>
                  <span style="font-size: 12px; color: #64748B;">Paid under Housing Benefit Regulations 2006 Reg 14(f)</span>
                </div>
                <input type="range" id="hb-slider" class="calc-slider" min="250" max="450" step="10" value="350" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="hb-val" class="calc-val-box" style="font-weight: 800; font-size: 16px; min-width: 125px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 14px; border-radius: 6px;">£350 / wk</span>
              </div>

              <!-- Dynamic Output KPI Cards -->
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; margin-top: 10px;">
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 14px; text-align: center;">
                  <div style="font-size: 12px; font-weight: 700; color: #64748B; text-transform: uppercase;">Weekly Fee / Bed</div>
                  <div id="sim-fee-per-bed" style="font-size: 24px; font-weight: 900; color: #0F1E36; margin-top: 4px;">£2,350</div>
                  <div id="sim-fee-breakdown" style="font-size: 11px; color: #475569; margin-top: 2px;">£1,100 + £900 + £350</div>
                </div>
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 14px; text-align: center;">
                  <div style="font-size: 12px; font-weight: 700; color: #64748B; text-transform: uppercase;">Weekly Campus Gross</div>
                  <div id="sim-weekly-rev" style="font-size: 24px; font-weight: 900; color: #2563EB; margin-top: 4px;">£18,800</div>
                  <div id="sim-weekly-sub" style="font-size: 11px; color: #475569; margin-top: 2px;">8 Beds Active (100% Cap)</div>
                </div>
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 14px; text-align: center;">
                  <div style="font-size: 12px; font-weight: 700; color: #64748B; text-transform: uppercase;">Monthly Campus Gross</div>
                  <div id="sim-monthly-rev" style="font-size: 24px; font-weight: 900; color: #047857; margin-top: 4px;">£81,467</div>
                  <div style="font-size: 11px; color: #475569; margin-top: 2px;">52 Weeks &divide; 12 Months</div>
                </div>
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 14px; text-align: center;">
                  <div style="font-size: 12px; font-weight: 700; color: #64748B; text-transform: uppercase;">Annualized Turnover</div>
                  <div id="sim-annual-rev" style="font-size: 24px; font-weight: 900; color: #D97706; margin-top: 4px;">£977,600</div>
                  <div id="sim-annual-sub" style="font-size: 11px; color: #475569; margin-top: 2px;">100% Stabilized Run-Rate</div>
                </div>
              </div>
            </div>
          </div>

          <!-- =========================================================================
               2. ITEMIZED MONTHLY RUNNING COST MODEL BY CATEGORY (OPEX BREAKDOWN) SIMULATOR
               ========================================================================= -->
          <div class="card" id="sec-fin-opex-simulator" style="border: 2px solid #059669; box-shadow: 0 4px 20px rgba(5, 150, 105, 0.08); margin-bottom: 36px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
              <div>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span class="badge" style="background:#059669; color:#FFFFFF; font-weight:800; font-size:12px;">SIMULATOR 02 // COST &amp; PROFIT ENGINE</span>
                  <h3 class="card-title" style="margin: 0; font-size: 22px;">Itemized Monthly Running Cost Model by Category (OpEx Breakdown)</h3>
                </div>
                <p style="font-size: 14.5px; color: var(--text-muted, #475569); margin-top: 6px;">
                  Adjust each monthly cost category slider to calculate live operating expenses, OpCo EBITDA profit, PropCo rental income, and consolidated group cashflow:
                </p>
              </div>
              <button type="button" onclick="resetToBoardroomBaseline()" style="background: #FFFFFF; border: 1.5px solid #059669; color: #059669; font-weight: 700; font-size: 13px; padding: 8px 16px; border-radius: 6px; cursor: pointer; transition: all 0.2s;">
                ↺ Reset to Boardroom Baseline
              </button>
            </div>

            <div class="calc-card" style="background: #FAFAFC; border: 1.5px solid #E2E8F0; border-radius: 10px; padding: 22px;">
              <!-- 7 Itemized Category Sliders -->
              <!-- Cat 1: Care Payroll -->
              <div class="calc-row" style="margin-bottom: 16px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="cat1-slider" style="display: block; font-weight: 700; font-size: 14px; color: #0F1E36;">
                    1. Direct Care Staffing &amp; Payroll:
                  </label>
                  <span style="font-size: 11.5px; color: #64748B;">10.0 FTE Staff, Autumn 2024 NI (£5k threshold @ 15%), Pension, Holiday &amp; Agency buffer</span>
                </div>
                <input type="range" id="cat1-slider" class="calc-slider" min="20000" max="45000" step="250" value="29592" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="cat1-val" class="calc-val-box" style="font-weight: 800; font-size: 15px; min-width: 120px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 12px; border-radius: 6px;">£29,592 / mo</span>
              </div>

              <!-- Cat 2: Leases -->
              <div class="calc-row" style="margin-bottom: 16px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="cat2-slider" style="display: block; font-weight: 700; font-size: 14px; color: #0F1E36;">
                    2. Property Commercial FRI Leases:
                  </label>
                  <span style="font-size: 11.5px; color: #64748B;">78 Marston Gdns (£5,417/mo) + 80 Marston Gdns (£2,667/mo) paid to PropCo</span>
                </div>
                <input type="range" id="cat2-slider" class="calc-slider" min="5000" max="14000" step="250" value="8083" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="cat2-val" class="calc-val-box" style="font-weight: 800; font-size: 15px; min-width: 120px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 12px; border-radius: 6px;">£8,083 / mo</span>
              </div>

              <!-- Cat 3: Utilities -->
              <div class="calc-row" style="margin-bottom: 16px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="cat3-slider" style="display: block; font-weight: 700; font-size: 14px; color: #0F1E36;">
                    3. Utilities &amp; Overheads:
                  </label>
                  <span style="font-size: 11.5px; color: #64748B;">Commercial dual-fuel gas/electricity, water rates, HTM 07-01 waste, telecare</span>
                </div>
                <input type="range" id="cat3-slider" class="calc-slider" min="2500" max="7000" step="100" value="4017" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="cat3-val" class="calc-val-box" style="font-weight: 800; font-size: 15px; min-width: 120px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 12px; border-radius: 6px;">£4,017 / mo</span>
              </div>

              <!-- Cat 4: Provisions -->
              <div class="calc-row" style="margin-bottom: 16px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="cat4-slider" style="display: block; font-weight: 700; font-size: 14px; color: #0F1E36;">
                    4. Resident Provisions &amp; Housekeeping:
                  </label>
                  <span style="font-size: 11.5px; color: #64748B;">Fresh nutrition (£59.60/res/wk), PPE, COSHH infection control chemicals</span>
                </div>
                <input type="range" id="cat4-slider" class="calc-slider" min="1200" max="4500" step="100" value="2067" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="cat4-val" class="calc-val-box" style="font-weight: 800; font-size: 15px; min-width: 120px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 12px; border-radius: 6px;">£2,067 / mo</span>
              </div>

              <!-- Cat 5: Regulatory & Insurance -->
              <div class="calc-row" style="margin-bottom: 16px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="cat5-slider" style="display: block; font-weight: 700; font-size: 14px; color: #0F1E36;">
                    5. Regulatory Fees, £10M Insurance &amp; Legal:
                  </label>
                  <span style="font-size: 11.5px; color: #64748B;">CQC provider fees, Medical Malpractice/Public Liability, Citation retained legal</span>
                </div>
                <input type="range" id="cat5-slider" class="calc-slider" min="1000" max="3500" step="50" value="1550" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="cat5-val" class="calc-val-box" style="font-weight: 800; font-size: 15px; min-width: 120px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 12px; border-radius: 6px;">£1,550 / mo</span>
              </div>

              <!-- Cat 6: Digital & Training -->
              <div class="calc-row" style="margin-bottom: 16px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="cat6-slider" style="display: block; font-weight: 700; font-size: 14px; color: #0F1E36;">
                    6. Digital Systems &amp; Mandatory Training:
                  </label>
                  <span style="font-size: 11.5px; color: #64748B;">Nourish e-MAR digital care suite, Oliver McGowan Autism training, PMVA certification</span>
                </div>
                <input type="range" id="cat6-slider" class="calc-slider" min="1000" max="3500" step="50" value="1875" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="cat6-val" class="calc-val-box" style="font-weight: 800; font-size: 15px; min-width: 120px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 12px; border-radius: 6px;">£1,875 / mo</span>
              </div>

              <!-- Cat 7: Sinking Fund -->
              <div class="calc-row" style="margin-bottom: 22px; display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1.2; min-width: 220px;">
                  <label for="cat7-slider" style="display: block; font-weight: 700; font-size: 14px; color: #0F1E36;">
                    7. Sinking Fund &amp; Contingency Reserve:
                  </label>
                  <span style="font-size: 11.5px; color: #64748B;">Reactive building fabric repair fund (£1,667/mo) + Working capital buffer (£4,167/mo)</span>
                </div>
                <input type="range" id="cat7-slider" class="calc-slider" min="2000" max="12000" step="250" value="5833" oninput="updateSimulators()" style="flex: 2; margin: 0 16px;">
                <span id="cat7-val" class="calc-val-box" style="font-weight: 800; font-size: 15px; min-width: 120px; text-align: center; background: #0F1E36; color: #FFF; padding: 6px 12px; border-radius: 6px;">£5,833 / mo</span>
              </div>

              <!-- Segmented Visual Proportion Bar -->
              <div style="margin: 22px 0 16px 0;">
                <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; color: #64748B; margin-bottom: 6px;">
                  <span>MONTHLY OPEX DISTRIBUTION BY CATEGORY</span>
                  <span id="sim-opex-bar-label">Total Monthly OpEx: £53,017 / mo</span>
                </div>
                <div style="height: 18px; width: 100%; border-radius: 9px; overflow: hidden; display: flex; background: #E2E8F0;">
                  <div id="bar-cat1" title="Care Payroll" style="width: 55.8%; background: #DC2626;"></div>
                  <div id="bar-cat2" title="Commercial Leases" style="width: 15.2%; background: #F59E0B;"></div>
                  <div id="bar-cat3" title="Utilities" style="width: 7.6%; background: #3B82F6;"></div>
                  <div id="bar-cat4" title="Provisions" style="width: 3.9%; background: #10B981;"></div>
                  <div id="bar-cat5" title="Regulatory/Insurance" style="width: 2.9%; background: #8B5CF6;"></div>
                  <div id="bar-cat6" title="Digital/Training" style="width: 3.5%; background: #EC4899;"></div>
                  <div id="bar-cat7" title="Sinking Fund" style="width: 11.0%; background: #64748B;"></div>
                </div>
                <div style="display: flex; flex-wrap: wrap; gap: 12px; font-size: 11px; color: #475569; margin-top: 8px;">
                  <span><span style="display:inline-block;width:10px;height:10px;background:#DC2626;border-radius:2px;margin-right:4px;"></span>Payroll: <strong id="pct-cat1">55.8%</strong></span>
                  <span><span style="display:inline-block;width:10px;height:10px;background:#F59E0B;border-radius:2px;margin-right:4px;"></span>Leases: <strong id="pct-cat2">15.2%</strong></span>
                  <span><span style="display:inline-block;width:10px;height:10px;background:#3B82F6;border-radius:2px;margin-right:4px;"></span>Utilities: <strong id="pct-cat3">7.6%</strong></span>
                  <span><span style="display:inline-block;width:10px;height:10px;background:#10B981;border-radius:2px;margin-right:4px;"></span>Provisions: <strong id="pct-cat4">3.9%</strong></span>
                  <span><span style="display:inline-block;width:10px;height:10px;background:#8B5CF6;border-radius:2px;margin-right:4px;"></span>Regulatory: <strong id="pct-cat5">2.9%</strong></span>
                  <span><span style="display:inline-block;width:10px;height:10px;background:#EC4899;border-radius:2px;margin-right:4px;"></span>Digital: <strong id="pct-cat6">3.5%</strong></span>
                  <span><span style="display:inline-block;width:10px;height:10px;background:#64748B;border-radius:2px;margin-right:4px;"></span>Sinking Fund: <strong id="pct-cat7">11.0%</strong></span>
                </div>
              </div>

              <!-- Live Performance & Profit Dashboard -->
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; margin-top: 18px;">
                <!-- Total Monthly OpEx -->
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 14px; text-align: center;">
                  <div style="font-size: 12px; font-weight: 700; color: #64748B; text-transform: uppercase;">Total Monthly OpEx</div>
                  <div id="sim-monthly-opex" style="font-size: 24px; font-weight: 900; color: #DC2626; margin-top: 4px;">£53,017</div>
                  <div id="sim-annual-opex" style="font-size: 11px; color: #475569; margin-top: 2px;">£636,204 / Year</div>
                </div>

                <!-- Monthly OpCo EBITDA -->
                <div style="background: #FFFFFF; border: 2px solid #10B981; border-radius: 8px; padding: 14px; text-align: center; background: #F0FDF4;">
                  <div style="font-size: 12px; font-weight: 700; color: #047857; text-transform: uppercase;">Monthly OpCo EBITDA</div>
                  <div id="sim-monthly-ebitda" style="font-size: 24px; font-weight: 900; color: #047857; margin-top: 4px;">+£28,450</div>
                  <div id="sim-annual-ebitda" style="font-size: 11px; font-weight: 700; color: #065F46; margin-top: 2px;">£341,396 / Year (34.9%)</div>
                </div>

                <!-- PropCo Rent -->
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 14px; text-align: center;">
                  <div style="font-size: 12px; font-weight: 700; color: #64748B; text-transform: uppercase;">PropCo Monthly Rent</div>
                  <div id="sim-propco-rent" style="font-size: 24px; font-weight: 900; color: #0F1E36; margin-top: 4px;">£8,083</div>
                  <div style="font-size: 11px; color: #475569; margin-top: 2px;">£97,000 / Year (Tax-deductible)</div>
                </div>

                <!-- Consolidated Cashflow -->
                <div style="background: #FFFFFF; border: 2px solid #D97706; border-radius: 8px; padding: 14px; text-align: center; background: #FFFBEB;">
                  <div style="font-size: 12px; font-weight: 700; color: #92400E; text-transform: uppercase;">Consolidated Net Cashflow</div>
                  <div id="sim-group-cashflow" style="font-size: 24px; font-weight: 900; color: #B45309; margin-top: 4px;">+£36,533</div>
                  <div id="sim-group-annual" style="font-size: 11px; font-weight: 700; color: #78350F; margin-top: 2px;">£438,396 / Year Total</div>
                </div>
              </div>

              <!-- Live Solvency & Break-Even Metric Callout -->
              <div style="margin-top: 18px; padding: 14px 18px; background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                  <span style="font-size: 13px; font-weight: 800; color: #0F1E36;">DYNAMIC BREAK-EVEN OCCUPANCY:</span>
                  <span id="sim-breakeven-beds" style="font-size: 16px; font-weight: 900; color: #2563EB; margin-left: 8px;">3.82 Beds (47.7% Occupancy)</span>
                  <span style="font-size: 12px; color: #64748B; margin-left: 8px;">(Margin of Safety: <strong id="sim-margin-safety" style="color:#047857;">+52.3%</strong>)</span>
                </div>
                <div id="sim-status-badge" style="background: #D1FAE5; color: #065F46; font-size: 12px; font-weight: 800; padding: 6px 14px; border-radius: 20px; border: 1px solid #10B981;">
                  ● SOLVENT: 34.9% EBITDA MARGIN
                </div>
              </div>
            </div>
          </div>
'''

# Find the old simulator card in tab-financials
old_sim_start = content.find('Dynamic Placement Fee & Bed Occupancy Simulator')
if old_sim_start != -1:
    # Find start of card containing this
    card_start = content.rfind('<div class="card"', 0, old_sim_start)
    # Find where the 3-Year Operating Waterfall Statement starts
    waterfall_start = content.find('3-Year Operating Waterfall Statement', old_sim_start)
    card_waterfall = content.rfind('<div class="card"', 0, waterfall_start)
    
    if card_start != -1 and card_waterfall != -1:
        # Replace the first simulator card
        content = content[:card_start] + SIMULATORS_HTML + '\n\n          ' + content[card_waterfall:]
        print('Injected new dual simulators into tab-financials successfully!')
    else:
        print('Could not find card boundaries for simulator replacement!')
else:
    print('Dynamic Placement Fee & Bed Occupancy Simulator not found!')


# =========================================================================
# 5. JAVASCRIPT SIMULATION COMPUTATION ENGINE INJECTION
# =========================================================================
SIMULATION_JS = '''
    // =========================================================================
    // DYNAMIC FINANCIAL & ITEMIZED OPEX SIMULATOR ENGINE (LINKED REAL-TIME MODEL)
    // =========================================================================
    function updateSimulators() {
      // 1. Placement Fee & Revenue Variables
      const beds = parseInt(document.getElementById("beds-slider")?.value || 8);
      const coreFee = parseFloat(document.getElementById("core-fee-slider")?.value || 1100);
      const hours1to1 = parseFloat(document.getElementById("hours-1to1-slider")?.value || 35);
      const rate1to1 = parseFloat(document.getElementById("rate-1to1-slider")?.value || 25.71);
      const hbFee = parseFloat(document.getElementById("hb-slider")?.value || 350);

      // Display inputs
      const bedsVal = document.getElementById("beds-val");
      if (bedsVal) bedsVal.innerText = beds + " Beds (" + ((beds / 8) * 100).toFixed(0) + "%)";
      const coreVal = document.getElementById("core-fee-val");
      if (coreVal) coreVal.innerText = "£" + Math.round(coreFee).toLocaleString() + " / wk";
      const hoursVal = document.getElementById("hours-1to1-val");
      if (hoursVal) hoursVal.innerText = hours1to1 + " hrs / wk";
      const rateVal = document.getElementById("rate-1to1-val");
      if (rateVal) rateVal.innerText = "£" + rate1to1.toFixed(2) + " / hr";
      const hbVal = document.getElementById("hb-val");
      if (hbVal) hbVal.innerText = "£" + Math.round(hbFee).toLocaleString() + " / wk";

      // Revenue Calculations
      const weekly1to1 = hours1to1 * rate1to1;
      const weeklyPerBed = coreFee + weekly1to1 + hbFee;
      const weeklyCampusRev = weeklyPerBed * beds;
      const monthlyCampusRev = (weeklyCampusRev * 52) / 12;
      const annualRev = weeklyCampusRev * 52;

      document.getElementById("sim-fee-per-bed") && (document.getElementById("sim-fee-per-bed").innerText = "£" + Math.round(weeklyPerBed).toLocaleString());
      document.getElementById("sim-fee-breakdown") && (document.getElementById("sim-fee-breakdown").innerText = "£" + Math.round(coreFee).toLocaleString() + " + £" + Math.round(weekly1to1).toLocaleString() + " + £" + Math.round(hbFee).toLocaleString());
      document.getElementById("sim-weekly-rev") && (document.getElementById("sim-weekly-rev").innerText = "£" + Math.round(weeklyCampusRev).toLocaleString());
      document.getElementById("sim-weekly-sub") && (document.getElementById("sim-weekly-sub").innerText = beds + " Beds Active (" + ((beds / 8) * 100).toFixed(0) + "% Cap)");
      document.getElementById("sim-monthly-rev") && (document.getElementById("sim-monthly-rev").innerText = "£" + Math.round(monthlyCampusRev).toLocaleString());
      document.getElementById("sim-annual-rev") && (document.getElementById("sim-annual-rev").innerText = "£" + Math.round(annualRev).toLocaleString());

      // 2. Itemized Monthly OpEx Variables
      const cat1 = parseFloat(document.getElementById("cat1-slider")?.value || 29592);
      const cat2 = parseFloat(document.getElementById("cat2-slider")?.value || 8083);
      const cat3 = parseFloat(document.getElementById("cat3-slider")?.value || 4017);
      const cat4 = parseFloat(document.getElementById("cat4-slider")?.value || 2067);
      const cat5 = parseFloat(document.getElementById("cat5-slider")?.value || 1550);
      const cat6 = parseFloat(document.getElementById("cat6-slider")?.value || 1875);
      const cat7 = parseFloat(document.getElementById("cat7-slider")?.value || 5833);

      // Display OpEx inputs
      document.getElementById("cat1-val") && (document.getElementById("cat1-val").innerText = "£" + Math.round(cat1).toLocaleString() + " / mo");
      document.getElementById("cat2-val") && (document.getElementById("cat2-val").innerText = "£" + Math.round(cat2).toLocaleString() + " / mo");
      document.getElementById("cat3-val") && (document.getElementById("cat3-val").innerText = "£" + Math.round(cat3).toLocaleString() + " / mo");
      document.getElementById("cat4-val") && (document.getElementById("cat4-val").innerText = "£" + Math.round(cat4).toLocaleString() + " / mo");
      document.getElementById("cat5-val") && (document.getElementById("cat5-val").innerText = "£" + Math.round(cat5).toLocaleString() + " / mo");
      document.getElementById("cat6-val") && (document.getElementById("cat6-val").innerText = "£" + Math.round(cat6).toLocaleString() + " / mo");
      document.getElementById("cat7-val") && (document.getElementById("cat7-val").innerText = "£" + Math.round(cat7).toLocaleString() + " / mo");

      // Calculations OpEx & Profit
      const totalMonthlyOpEx = cat1 + cat2 + cat3 + cat4 + cat5 + cat6 + cat7;
      const totalAnnualOpEx = totalMonthlyOpEx * 12;

      const monthlyEbitda = monthlyCampusRev - totalMonthlyOpEx;
      const annualEbitda = monthlyEbitda * 12;
      const ebitdaMargin = annualRev > 0 ? ((annualEbitda / annualRev) * 100).toFixed(1) : 0;

      const propCoRent = cat2;
      const groupMonthlyCash = monthlyEbitda + propCoRent;
      const groupAnnualCash = groupMonthlyCash * 12;

      // Segmented Bar Percentages
      const p1 = ((cat1 / totalMonthlyOpEx) * 100).toFixed(1);
      const p2 = ((cat2 / totalMonthlyOpEx) * 100).toFixed(1);
      const p3 = ((cat3 / totalMonthlyOpEx) * 100).toFixed(1);
      const p4 = ((cat4 / totalMonthlyOpEx) * 100).toFixed(1);
      const p5 = ((cat5 / totalMonthlyOpEx) * 100).toFixed(1);
      const p6 = ((cat6 / totalMonthlyOpEx) * 100).toFixed(1);
      const p7 = ((cat7 / totalMonthlyOpEx) * 100).toFixed(1);

      document.getElementById("bar-cat1") && (document.getElementById("bar-cat1").style.width = p1 + "%");
      document.getElementById("bar-cat2") && (document.getElementById("bar-cat2").style.width = p2 + "%");
      document.getElementById("bar-cat3") && (document.getElementById("bar-cat3").style.width = p3 + "%");
      document.getElementById("bar-cat4") && (document.getElementById("bar-cat4").style.width = p4 + "%");
      document.getElementById("bar-cat5") && (document.getElementById("bar-cat5").style.width = p5 + "%");
      document.getElementById("bar-cat6") && (document.getElementById("bar-cat6").style.width = p6 + "%");
      document.getElementById("bar-cat7") && (document.getElementById("bar-cat7").style.width = p7 + "%");

      document.getElementById("pct-cat1") && (document.getElementById("pct-cat1").innerText = p1 + "%");
      document.getElementById("pct-cat2") && (document.getElementById("pct-cat2").innerText = p2 + "%");
      document.getElementById("pct-cat3") && (document.getElementById("pct-cat3").innerText = p3 + "%");
      document.getElementById("pct-cat4") && (document.getElementById("pct-cat4").innerText = p4 + "%");
      document.getElementById("pct-cat5") && (document.getElementById("pct-cat5").innerText = p5 + "%");
      document.getElementById("pct-cat6") && (document.getElementById("pct-cat6").innerText = p6 + "%");
      document.getElementById("pct-cat7") && (document.getElementById("pct-cat7").innerText = p7 + "%");
      document.getElementById("sim-opex-bar-label") && (document.getElementById("sim-opex-bar-label").innerText = "Total Monthly OpEx: £" + Math.round(totalMonthlyOpEx).toLocaleString() + " / mo");

      // Outputs
      document.getElementById("sim-monthly-opex") && (document.getElementById("sim-monthly-opex").innerText = "£" + Math.round(totalMonthlyOpEx).toLocaleString());
      document.getElementById("sim-annual-opex") && (document.getElementById("sim-annual-opex").innerText = "£" + Math.round(totalAnnualOpEx).toLocaleString() + " / Year");

      const elEbitda = document.getElementById("sim-monthly-ebitda");
      if (elEbitda) {
        elEbitda.innerText = (monthlyEbitda >= 0 ? "+£" : "-£") + Math.abs(Math.round(monthlyEbitda)).toLocaleString();
        elEbitda.style.color = monthlyEbitda >= 0 ? "#047857" : "#DC2626";
      }
      const elAnnualEbitda = document.getElementById("sim-annual-ebitda");
      if (elAnnualEbitda) {
        elAnnualEbitda.innerText = (annualEbitda >= 0 ? "£" : "-£") + Math.abs(Math.round(annualEbitda)).toLocaleString() + " / Year (" + ebitdaMargin + "%)";
      }

      document.getElementById("sim-propco-rent") && (document.getElementById("sim-propco-rent").innerText = "£" + Math.round(propCoRent).toLocaleString());

      const elGroupCash = document.getElementById("sim-group-cashflow");
      if (elGroupCash) {
        elGroupCash.innerText = (groupMonthlyCash >= 0 ? "+£" : "-£") + Math.abs(Math.round(groupMonthlyCash)).toLocaleString();
        elGroupCash.style.color = groupMonthlyCash >= 0 ? "#B45309" : "#DC2626";
      }
      document.getElementById("sim-group-annual") && (document.getElementById("sim-group-annual").innerText = (groupAnnualCash >= 0 ? "£" : "-£") + Math.abs(Math.round(groupAnnualCash)).toLocaleString() + " / Year Total");

      // Dynamic Break-Even Occupancy
      const monthlyRevPerBed = (weeklyPerBed * 52) / 12;
      const variableCostPerBed = (cat4 / 8) + (cat1 * 0.45 / 8);
      const contributionMarginPerBed = monthlyRevPerBed - variableCostPerBed;
      const fixedOverheadsMonthly = totalMonthlyOpEx - (variableCostPerBed * beds);
      const breakEvenBeds = contributionMarginPerBed > 0 ? (fixedOverheadsMonthly / contributionMarginPerBed).toFixed(2) : "N/A";
      const breakEvenPct = contributionMarginPerBed > 0 ? ((breakEvenBeds / 8) * 100).toFixed(1) : 0;
      const safetyMargin = (100 - breakEvenPct).toFixed(1);

      const elBe = document.getElementById("sim-breakeven-beds");
      if (elBe) elBe.innerText = breakEvenBeds + " Beds (" + breakEvenPct + "% Occupancy)";
      const elSafe = document.getElementById("sim-margin-safety");
      if (elSafe) elSafe.innerText = "+" + safetyMargin + "%";

      const elStatus = document.getElementById("sim-status-badge");
      if (elStatus) {
        if (monthlyEbitda > 10000) {
          elStatus.innerText = "● SOLVENT: " + ebitdaMargin + "% EBITDA MARGIN";
          elStatus.style.background = "#D1FAE5";
          elStatus.style.color = "#065F46";
          elStatus.style.borderColor = "#10B981";
        } else if (monthlyEbitda >= 0) {
          elStatus.innerText = "● MODERATE SURPLUS: " + ebitdaMargin + "% MARGIN";
          elStatus.style.background = "#FEF3C7";
          elStatus.style.color = "#92400E";
          elStatus.style.borderColor = "#F59E0B";
        } else {
          elStatus.innerText = "● OPERATING DEFICIT: VOID SENSITIVITY TRIGGERED";
          elStatus.style.background = "#FEE2E2";
          elStatus.style.color = "#991B1B";
          elStatus.style.borderColor = "#EF4444";
        }
      }
    }

    function resetToBoardroomBaseline() {
      document.getElementById("beds-slider") && (document.getElementById("beds-slider").value = 8);
      document.getElementById("core-fee-slider") && (document.getElementById("core-fee-slider").value = 1100);
      document.getElementById("hours-1to1-slider") && (document.getElementById("hours-1to1-slider").value = 35);
      document.getElementById("rate-1to1-slider") && (document.getElementById("rate-1to1-slider").value = 25.71);
      document.getElementById("hb-slider") && (document.getElementById("hb-slider").value = 350);

      document.getElementById("cat1-slider") && (document.getElementById("cat1-slider").value = 29592);
      document.getElementById("cat2-slider") && (document.getElementById("cat2-slider").value = 8083);
      document.getElementById("cat3-slider") && (document.getElementById("cat3-slider").value = 4017);
      document.getElementById("cat4-slider") && (document.getElementById("cat4-slider").value = 2067);
      document.getElementById("cat5-slider") && (document.getElementById("cat5-slider").value = 1550);
      document.getElementById("cat6-slider") && (document.getElementById("cat6-slider").value = 1875);
      document.getElementById("cat7-slider") && (document.getElementById("cat7-slider").value = 5833);

      updateSimulators();
    }

    // Connect updateCalculator fallback to updateSimulators
    function updateCalculator() {
      updateSimulators();
    }
'''

# Replace old updateCalculator in script
calc_match = re.search(r'function updateCalculator\(\)\s*\{[\s\S]*?\}\s*(?=\n\s*//|\n\s*function|\n\s*<\/script>)', content)
if calc_match:
    old_calc = calc_match.group(0)
    content = content.replace(old_calc, SIMULATION_JS, 1)
    print('Replaced updateCalculator with full dual simulator JavaScript engine!')
else:
    # Append inside script tag
    script_close = content.rfind('</script>')
    content = content[:script_close] + '\n' + SIMULATION_JS + '\n  ' + content[script_close:]
    print('Appended dual simulator JavaScript engine to <script>!')

# Make sure updateSimulators is called on load
init_call = 'try { updateSimulators(); } catch(e) {}'
if 'updateSimulators();' not in content:
    content = content.replace('window.addEventListener("DOMContentLoaded", function() {', 'window.addEventListener("DOMContentLoaded", function() {\n      ' + init_call, 1)

# Save updated HTML
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Successfully updated {HTML_PATH}! New length: {len(content)} bytes')
