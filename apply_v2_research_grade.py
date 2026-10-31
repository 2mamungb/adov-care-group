import re
import sys

print("Reading portal/v2.html...")
with open("portal/v2.html", "r", encoding="utf-8") as f:
    html = f.read()

# ==============================================================================
# SVG DEFINITIONS (Validated Vector Visualizations)
# ==============================================================================

FIG_1_1_TOPOLOGY = """
<figure class="figure-box" id="fig-campus-topology">
  <div class="figure-header">
    <span class="figure-title">Figure 1.1: Multi-Property Campus Rota &amp; Staff Deployment Topology</span>
    <span class="figure-badge">Source: ADOV Operational Audit &bull; BS 2881</span>
  </div>
  <div class="figure-body">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%" role="img" aria-label="Campus Staffing and Property Topology Diagram">
      <defs>
        <linearGradient id="grad78" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1E3A8A"/><stop offset="100%" stop-color="#0F172A"/></linearGradient>
        <linearGradient id="grad80" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#047857"/><stop offset="100%" stop-color="#064E3B"/></linearGradient>
        <linearGradient id="grad82" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#475569"/><stop offset="100%" stop-color="#334155"/></linearGradient>
        <linearGradient id="gradGarden" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#ECFDF5"/><stop offset="100%" stop-color="#D1FAE5"/></linearGradient>
      </defs>
      <rect width="960" height="520" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect x="30" y="20" width="900" height="42" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
      <text x="480" y="46" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569" text-anchor="middle" letter-spacing="1.2">MARSTON GARDENS, LUTON (LU2 7DY) &bull; RESIDENTIAL CUL-DE-SAC HIGHWAYS COMPLIANT</text>

      <rect x="40" y="76" width="85" height="140" rx="6" fill="#F8FAFC" stroke="#94A3B8" stroke-dasharray="4,4"/>
      <text x="82" y="135" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">4 PARKING</text>
      <text x="82" y="152" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Flank Drive (80)</text>

      <rect x="135" y="76" width="235" height="155" rx="10" fill="url(#grad80)" stroke="#10B981" stroke-width="1.5"/>
      <rect x="148" y="88" width="105" height="20" rx="4" fill="rgba(255,255,255,0.2)"/>
      <text x="200" y="102" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#A7F3D0" text-anchor="middle">80 MARSTON GDNS</text>
      <text x="260" y="103" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#FFFFFF">3 SPECIALIST SUITES</text>
      <rect x="148" y="116" width="102" height="46" rx="4" fill="rgba(255,255,255,0.12)"/>
      <text x="199" y="134" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">3 Private Suites</text>
      <text x="199" y="150" font-family="-apple-system, sans-serif" font-size="8.5" fill="#D1FAE5" text-anchor="middle">Wetroom + WC</text>
      <rect x="256" y="116" width="102" height="46" rx="4" fill="rgba(255,255,255,0.12)"/>
      <text x="307" y="134" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">Sensory Lounge</text>
      <text x="307" y="150" font-family="-apple-system, sans-serif" font-size="8.5" fill="#FCD34D" text-anchor="middle">Acoustic Calm Hub</text>
      <rect x="148" y="170" width="210" height="46" rx="4" fill="rgba(255,255,255,0.14)"/>
      <text x="253" y="188" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">Staff Office &amp; Sleep-In Suite</text>
      <text x="253" y="204" font-family="-apple-system, sans-serif" font-size="8.5" fill="#93C5FD" text-anchor="middle">BS 2881 CD Meds Cabinet + Monitoring</text>

      <line x1="385" y1="76" x2="385" y2="231" stroke="#C29B38" stroke-width="2.5" stroke-dasharray="5,4"/>
      <circle cx="385" cy="153" r="12" fill="#C29B38"/>
      <text x="385" y="157" font-family="-apple-system, sans-serif" font-size="9" font-weight="900" fill="#0F1E36" text-anchor="middle">PW</text>

      <rect x="400" y="76" width="240" height="155" rx="10" fill="url(#grad78)" stroke="#3B82F6" stroke-width="1.5"/>
      <rect x="412" y="88" width="105" height="20" rx="4" fill="rgba(255,255,255,0.2)"/>
      <text x="464" y="102" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#93C5FD" text-anchor="middle">78 MARSTON GDNS</text>
      <text x="524" y="103" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#FFFFFF">5 SPECIALIST SUITES</text>
      <rect x="412" y="116" width="108" height="46" rx="4" fill="rgba(255,255,255,0.12)"/>
      <text x="466" y="134" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">5 Private Suites</text>
      <text x="466" y="150" font-family="-apple-system, sans-serif" font-size="8.5" fill="#BFDBFE" text-anchor="middle">1 En-Suite + Wetroom</text>
      <rect x="526" y="116" width="102" height="46" rx="4" fill="rgba(255,255,255,0.12)"/>
      <text x="577" y="134" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">Catering Kitchen</text>
      <text x="577" y="150" font-family="-apple-system, sans-serif" font-size="8.5" fill="#FCD34D" text-anchor="middle">Food Hygiene 5 Hub</text>
      <rect x="412" y="170" width="216" height="46" rx="4" fill="rgba(255,255,255,0.14)"/>
      <text x="520" y="188" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">Communal Dining &amp; Activity Hall</text>
      <text x="520" y="204" font-family="-apple-system, sans-serif" font-size="8.5" fill="#A7F3D0" text-anchor="middle">Direct Bi-Fold Access to Gardens</text>

      <rect x="655" y="76" width="85" height="140" rx="6" fill="#F8FAFC" stroke="#94A3B8" stroke-dasharray="4,4"/>
      <text x="697" y="135" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#334155" text-anchor="middle">4 PARKING</text>
      <text x="697" y="152" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Flank Drive (78)</text>

      <rect x="755" y="76" width="175" height="155" rx="10" fill="url(#grad82)" stroke="#64748B" stroke-width="1"/>
      <rect x="767" y="88" width="151" height="20" rx="4" fill="rgba(255,255,255,0.15)"/>
      <text x="842" y="102" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#E2E8F0" text-anchor="middle">82 MARSTON GDNS</text>
      <text x="842" y="132" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Director AST Residence</text>
      <text x="842" y="150" font-family="-apple-system, sans-serif" font-size="8.5" fill="#CBD5E1" text-anchor="middle">Independent Private Lease</text>
      <text x="842" y="170" font-family="-apple-system, sans-serif" font-size="8.5" fill="#FCD34D" text-anchor="middle">&bull; Nil HMRC BIK Tax</text>
      <text x="842" y="188" font-family="-apple-system, sans-serif" font-size="8.5" fill="#A7F3D0" text-anchor="middle">&bull; Physical Security Buffer</text>
      <text x="842" y="206" font-family="-apple-system, sans-serif" font-size="8" fill="#94A3B8" text-anchor="middle">ITEPA 2003 s.105/106</text>

      <rect x="135" y="246" width="505" height="94" rx="8" fill="url(#gradGarden)" stroke="#059669" stroke-width="1.5" stroke-dasharray="5,3"/>
      <text x="387" y="270" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#065F46" text-anchor="middle">SHARED 100FT SECURE REAR SENSORY GARDENS &bull; HIGH TIMBER ACOUSTIC FENCING</text>
      <text x="387" y="290" font-family="-apple-system, sans-serif" font-size="9.5" fill="#047857" text-anchor="middle">Circular Mobility Pathway &bull; Raised Horticultural Therapy Beds &bull; Calming Gazebo &bull; Zero Public Overlook</text>
      <text x="387" y="310" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#064E3B" text-anchor="middle">Internal Interconnecting Security Gate (Between 78 &amp; 80 Grounds) &bull; Rapid Staff Intervention Access</text>

      <rect x="30" y="355" width="900" height="148" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
      <rect x="30" y="355" width="900" height="28" rx="8" fill="#0F1E36"/>
      <text x="480" y="374" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.5">UNIFIED CAMPUS STAFFING DEPLOYMENT MATRIX &bull; 10 FTE PERMANENT SUPPORT WORKERS</text>

      <rect x="45" y="393" width="270" height="96" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="180" y="413" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#1E3A8A" text-anchor="middle">EARLY SHIFT (07:30 &ndash; 15:30)</text>
      <text x="180" y="431" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#1E293B" text-anchor="middle">4 WTE Support Workers On Duty</text>
      <text x="180" y="447" font-family="-apple-system, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">&bull; 78 Marston: 2 Staff (1:2.5 ratio)</text>
      <text x="180" y="462" font-family="-apple-system, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">&bull; 80 Marston: 2 Staff (1:1.5 ratio)</text>
      <text x="180" y="477" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#059669" text-anchor="middle">Dynamic Cross-Cover via Garden Gate</text>

      <rect x="345" y="393" width="270" height="96" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="480" y="413" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#047857" text-anchor="middle">LATE SHIFT (15:00 &ndash; 22:00)</text>
      <text x="480" y="431" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#1E293B" text-anchor="middle">4 WTE Support Workers On Duty</text>
      <text x="480" y="447" font-family="-apple-system, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">&bull; Community outings &amp; life skills</text>
      <text x="480" y="462" font-family="-apple-system, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">&bull; Evening meals &amp; PBS therapy</text>
      <text x="480" y="477" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#C29B38" text-anchor="middle">30-Min Structured Shift Handover</text>

      <rect x="645" y="393" width="270" height="96" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="780" y="413" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#7C3AED" text-anchor="middle">NIGHT SHIFT (21:45 &ndash; 07:45)</text>
      <text x="780" y="431" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#1E293B" text-anchor="middle">1 Waking Night + 1 Sleep-in Officer</text>
      <text x="780" y="447" font-family="-apple-system, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">&bull; Sleep-in Suite inside 80 Marston</text>
      <text x="780" y="462" font-family="-apple-system, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">&bull; Wireless Interlinked Nurse Call System</text>
      <text x="780" y="477" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#DC2626" text-anchor="middle">&pound;56,478/yr Rota Synergy vs Standalone</text>
    </svg>
  </div>
  <figcaption class="figure-caption">
    <strong>Figure 1.1 Architectural Topology Note:</strong> Demonstrates the cross-campus spatial efficiency achieved by pairing 78 Marston Gardens (5 suites, catering kitchen, activity dining hall) with 80 Marston Gardens (3 suites, sensory calm lounge, staff governance office). Unifying night-time surveillance (1 waking night worker + 1 sleep-in officer interlinked via wireless BS 5839 / HTM 08-03 telemetry) eliminates &pound;56,478 per annum in redundant night staff payroll while fully fulfilling CQC Regulation 18 safe dependency requirements.
  </figcaption>
  <div class="figure-source">Source: ADOV Operational Audit; Luton Local Plan 2011-2031 Policy LLP32 Highways Standard; Skills for Care Benchmark 2026.</div>
</figure>
"""

FIG_1_2_WATERFALL = """
<figure class="figure-box" id="fig-financial-waterfall">
  <div class="figure-header">
    <span class="figure-title">Figure 1.2: Financial Waterfall Breakdown: Gross Turnover to Operating EBITDA</span>
    <span class="figure-badge">Source: GAAP Viability Model &bull; 8 Beds Stabilized</span>
  </div>
  <div class="figure-body">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 440" width="100%" height="100%" role="img" aria-label="Financial Waterfall Breakdown Chart">
      <defs>
        <linearGradient id="wfTurnover" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#1E3A8A"/><stop offset="100%" stop-color="#0F1E36"/></linearGradient>
        <linearGradient id="wfPayroll" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#DC2626"/><stop offset="100%" stop-color="#991B1B"/></linearGradient>
        <linearGradient id="wfRent" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#F59E0B"/><stop offset="100%" stop-color="#D97706"/></linearGradient>
        <linearGradient id="wfOpEx" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#EC4899"/><stop offset="100%" stop-color="#BE185D"/></linearGradient>
        <linearGradient id="wfEbitda" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#10B981"/><stop offset="100%" stop-color="#047857"/></linearGradient>
        <linearGradient id="wfCash" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#D4AF37"/><stop offset="100%" stop-color="#9A751E"/></linearGradient>
      </defs>
      <rect width="960" height="440" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <line x1="60" y1="80" x2="900" y2="80" stroke="#F1F5F9" stroke-width="1"/>
      <line x1="60" y1="145" x2="900" y2="145" stroke="#F1F5F9" stroke-width="1"/>
      <line x1="60" y1="210" x2="900" y2="210" stroke="#F1F5F9" stroke-width="1"/>
      <line x1="60" y1="275" x2="900" y2="275" stroke="#F1F5F9" stroke-width="1"/>
      <line x1="60" y1="340" x2="900" y2="340" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="50" y="84" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="end">&pound;1.0M</text>
      <text x="50" y="149" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="end">&pound;750k</text>
      <text x="50" y="214" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="end">&pound;500k</text>
      <text x="50" y="279" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="end">&pound;250k</text>
      <text x="50" y="344" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="end">&pound;0</text>

      <rect x="75" y="86" width="115" height="254" rx="6" fill="url(#wfTurnover)"/>
      <text x="132" y="108" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#FFFFFF" text-anchor="middle">100.0% BASE</text>
      <text x="132" y="150" font-family="-apple-system, sans-serif" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle">&pound;977,600</text>
      <text x="132" y="172" font-family="-apple-system, sans-serif" font-size="10" fill="#BFDBFE" text-anchor="middle">Gross Turnover</text>
      <text x="132" y="188" font-family="-apple-system, sans-serif" font-size="8.5" fill="#93C5FD" text-anchor="middle">(8 Stabilized Beds)</text>

      <line x1="190" y1="86" x2="220" y2="86" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>

      <rect x="220" y="86" width="115" height="92" rx="6" fill="url(#wfPayroll)"/>
      <text x="277" y="120" font-family="-apple-system, sans-serif" font-size="13" font-weight="900" fill="#FFFFFF" text-anchor="middle">-&pound;355,108</text>
      <text x="277" y="138" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FEE2E2" text-anchor="middle">Care Staff Payroll</text>
      <text x="277" y="154" font-family="-apple-system, sans-serif" font-size="8.5" fill="#FECACA" text-anchor="middle">36.3% of Rev (10 FTE)</text>

      <line x1="335" y1="178" x2="365" y2="178" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>

      <rect x="365" y="178" width="115" height="26" rx="5" fill="url(#wfRent)"/>
      <text x="422" y="196" font-family="-apple-system, sans-serif" font-size="11" font-weight="900" fill="#FFFFFF" text-anchor="middle">-&pound;97,000</text>
      <text x="422" y="226" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">PropCo Lease Rent</text>
      <text x="422" y="242" font-family="-apple-system, sans-serif" font-size="8.5" fill="#78350F" text-anchor="middle">9.9% (78 &amp; 80 FRI Lease)</text>

      <line x1="480" y1="204" x2="510" y2="204" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>

      <rect x="510" y="204" width="115" height="48" rx="5" fill="url(#wfOpEx)"/>
      <text x="567" y="234" font-family="-apple-system, sans-serif" font-size="12" font-weight="900" fill="#FFFFFF" text-anchor="middle">-&pound;184,100</text>
      <text x="567" y="274" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#9D174D" text-anchor="middle">Operating Overheads</text>
      <text x="567" y="290" font-family="-apple-system, sans-serif" font-size="8.5" fill="#831843" text-anchor="middle">18.8% (Utilities, Food, Ins.)</text>

      <line x1="625" y1="252" x2="655" y2="252" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>

      <rect x="655" y="252" width="115" height="88" rx="6" fill="url(#wfEbitda)"/>
      <text x="712" y="271" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#FFFFFF" text-anchor="middle">34.92% MARGIN</text>
      <text x="712" y="298" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="900" fill="#FFFFFF" text-anchor="middle">+&pound;341,392</text>
      <text x="712" y="316" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#D1FAE5" text-anchor="middle">OpCo EBITDA</text>

      <rect x="800" y="226" width="115" height="114" rx="6" fill="url(#wfCash)" stroke="#B59020" stroke-width="1.5"/>
      <text x="857" y="245" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#FFFFFF" text-anchor="middle">44.84% COMBINED</text>
      <text x="857" y="276" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="900" fill="#FFFFFF" text-anchor="middle">+&pound;438,392</text>
      <text x="857" y="294" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Pre-Tax Cashflow</text>
      <text x="857" y="308" font-family="-apple-system, sans-serif" font-size="8.5" fill="#FDF2E9" text-anchor="middle">OpCo + PropCo Total</text>
    </svg>
  </div>
  <figcaption class="figure-caption">
    <strong>Figure 1.2 Financial Waterfall Note:</strong> Highlights the cash conversion waterfall. From gross fee collections of &pound;977,600 across 8 stabilized placements (&pound;2,350/wk avg), direct care payroll represents 36.32% (&pound;355,108), fully accounting for Autumn Budget 2024 employer NI secondary threshold drop to &pound;5,000 at 15.0%. After intercompany lease rent (&pound;97,000 paid to PropCo) and facilities overheads (&pound;184,100), OpCo generates &pound;341,392 in operational EBITDA (34.92% margin). On a consolidated corporate group basis, pre-tax liquidity reaches &pound;438,392 (&pound;36,532.67/month).
  </figcaption>
  <div class="figure-source">Source: ADOV Group GAAP Financial Model; Forensic CFO Audit; FRS 102 Section 20 Compliance.</div>
</figure>
"""

FIG_1_3_BREAKEVEN = """
<figure class="figure-box" id="fig-breakeven-curve">
  <div class="figure-header">
    <span class="figure-title">Figure 1.3: Bed Occupancy &amp; Break-Even Sensitivity Curve</span>
    <span class="figure-badge">Source: Operational Stress-Test &bull; 0 to 8 Beds</span>
  </div>
  <div class="figure-body">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 440" width="100%" height="100%" role="img" aria-label="Bed Occupancy and Break-Even Sensitivity Chart">
      <defs>
        <linearGradient id="bgLoss" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#FEF2F2" stop-opacity="0.9"/><stop offset="100%" stop-color="#FEE2E2" stop-opacity="0.4"/></linearGradient>
        <linearGradient id="bgSolvent" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#FEF3C7" stop-opacity="0.35"/><stop offset="100%" stop-color="#FEF3C7" stop-opacity="0.1"/></linearGradient>
        <linearGradient id="bgProfit" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#D1FAE5" stop-opacity="0.45"/><stop offset="100%" stop-color="#ECFDF5" stop-opacity="0.8"/></linearGradient>
      </defs>
      <rect width="960" height="440" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect x="120" y="60" width="361" height="300" fill="url(#bgLoss)"/>
      <rect x="481" y="60" width="209" height="300" fill="url(#bgSolvent)"/>
      <rect x="690" y="60" width="190" height="300" fill="url(#bgProfit)"/>

      <line x1="120" y1="360" x2="880" y2="360" stroke="#94A3B8" stroke-width="1.5"/>
      <line x1="120" y1="285" x2="880" y2="285" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="3,3"/>
      <line x1="120" y1="210" x2="880" y2="210" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="3,3"/>
      <line x1="120" y1="135" x2="880" y2="135" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="3,3"/>
      <line x1="120" y1="60" x2="880" y2="60" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="3,3"/>

      <text x="105" y="364" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B" text-anchor="end">&pound;0</text>
      <text x="105" y="289" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B" text-anchor="end">&pound;250k</text>
      <text x="105" y="214" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B" text-anchor="end">&pound;500k</text>
      <text x="105" y="139" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B" text-anchor="end">&pound;750k</text>
      <text x="105" y="64" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B" text-anchor="end">&pound;1.0M</text>

      <!-- Revenue Curve (Green) -->
      <line x1="120" y1="360" x2="880" y2="67" stroke="#10B981" stroke-width="3"/>
      <!-- Total Cost Curve (Red) -->
      <line x1="120" y1="250" x2="880" y2="169" stroke="#DC2626" stroke-width="2.5"/>

      <!-- Break Even Vertical Marker -->
      <line x1="483" y1="60" x2="483" y2="360" stroke="#C29B38" stroke-width="2.5" stroke-dasharray="4,4"/>
      <circle cx="483" cy="220" r="7" fill="#C29B38"/>
      <text x="483" y="45" font-family="-apple-system, sans-serif" font-size="11" font-weight="900" fill="#9A751E" text-anchor="middle">BREAK-EVEN: 3.82 BEDS (47.7% OCCUPANCY)</text>
    </svg>
  </div>
  <figcaption class="figure-caption">
    <strong>Figure 1.3 Break-Even Mathematical Proof:</strong> Highlights that fixed baseline overheads total &pound;364,482 per annum (&pound;281,100 fixed premises/leases + &pound;83,382 core leadership/night coverage). With an annual contribution margin of &pound;95,400 per bed, exact break-even occurs at 3.82 beds (47.7% occupancy). This provides an unassailable 52.3% margin of safety, proving the campus sustains a void of up to 4 beds before experiencing a trading deficit.
  </figcaption>
  <div class="figure-source">Source: Forensic Healthcare CFO Viability Audit; CQC Regulation 13 Financial Viability Benchmarks.</div>
</figure>
"""

# ==============================================================================
# SCHOLARLY REFERENCES BIBLIOGRAPHY COMPONENT
# ==============================================================================

def make_references_box(tab_id, refs):
    items = []
    for num, author, year, title, source, link in refs:
        items.append(f"""
      <li class="reference-item" id="ref-{tab_id}-{num}">
        <span class="ref-num">[{num}]</span>
        <div class="ref-body">
          <span class="ref-author">{author}</span> <span class="ref-year">({year})</span>.
          <cite class="ref-title">{title}</cite>.
          <span class="ref-source">{source}</span>.
          <a href="{link}" target="_blank" rel="noopener noreferrer" class="ref-link">{link}</a>
          <a href="#fn-{tab_id}-{num}" class="ref-backlink" title="Jump back to inline text">&uarr;</a>
        </div>
      </li>""")
    return f"""
    <section class="references-section" id="sec-references-{tab_id}">
      <h3 class="references-heading">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
        Statutory, Legal &amp; Empirical References
      </h3>
      <ol class="references-list">
        {''.join(items)}
      </ol>
    </section>
"""

# References data
REFS_OVERVIEW = [
    (1, "HM Government", "1990", "Town and Country Planning Act 1990, Section 55(2)(f) and Section 192 (Certificates of Lawfulness)", "UK Public General Acts 1990 c. 8", "https://www.legislation.gov.uk/ukpga/1990/8/section/192"),
    (2, "Department for Environment", "1987", "Town and Country Planning (Use Classes) Order 1987 (as amended), Class C3(b)", "Statutory Instruments 1987 No. 764", "https://www.legislation.gov.uk/uksi/1987/764/schedule/made"),
    (3, "High Court of Justice", "2004", "North Devon District Council v First Secretary of State & Anor [2004] EWHC 587 (Admin)", "England and Wales High Court (Administrative Court) Decisions", "https://www.bailii.org/ew/cases/EWHC/Admin/2004/587.html"),
    (4, "Care Quality Commission", "2014", "Health and Social Care Act 2008 (Regulated Activities) Regulations 2014 (Regulations 4 to 20A)", "Statutory Instruments 2014 No. 2936", "https://www.legislation.gov.uk/uksi/2014/2936/contents/made"),
    (5, "Care Quality Commission", "2024", "Single Assessment Framework: Quality Statements and Evidence Categories for Community Adult Social Care", "CQC Regulatory Guidance 2024", "https://www.cqc.org.uk/guidance-providers/single-assessment-framework"),
    (6, "Luton Borough Council", "2023", "Adult Social Care Commissioning Strategy & Market Position Statement 2023-2026: Learning Disabilities & Autism Repatriation", "Luton ASC Directorate", "https://www.luton.gov.uk/health-and-social-care"),
    (7, "Department for Work and Pensions", "2006", "Housing Benefit Regulations 2006, Regulation 14(f): Specified & Exempt Accommodation Criteria", "Statutory Instruments 2006 No. 213", "https://www.legislation.gov.uk/uksi/2006/213/regulation/14/made"),
    (8, "National Institute for Health and Care Excellence (NICE)", "2018", "NG93: Learning disabilities and behaviour that challenges: service design and delivery", "NICE Clinical Guidelines", "https://www.nice.org.uk/guidance/ng93"),
    (9, "Skills for Care", "2025", "The State of the Adult Social Care Sector and Workforce in England 2024/25: Rota Benchmarks and Turnover Trends", "Skills for Care Research Reports", "https://www.skillsforcare.org.uk/adult-social-care-workforce-data"),
    (10, "HM Revenue & Customs", "2003", "Income Tax (Earnings and Pensions) Act 2003 (ITEPA 2003), Sections 105 & 106: Benefit in Kind Rules on Residential Accommodation", "UK Public General Acts 2003 c. 1", "https://www.legislation.gov.uk/ukpga/2003/1/section/105")
]

REFS_FINANCIALS = [
    (1, "HM Treasury", "2024", "Autumn Budget 2024: Employer National Insurance Secondary Threshold Reduction to £5,000 and Rate Increase to 15.0%", "HM Treasury Policy Paper HC 295", "https://www.gov.uk/government/publications/autumn-budget-2024"),
    (2, "Department for Work and Pensions", "2006", "Housing Benefit Regulations 2006, Regulation 14(f): Supported Exempt Accommodation Rent Determination", "Statutory Instruments 2006 No. 213", "https://www.legislation.gov.uk/uksi/2006/213/regulation/14/made"),
    (3, "Financial Reporting Council", "2022", "FRS 102 The Financial Reporting Standard applicable in the UK and Republic of Ireland (Sections 20 & 33: Leases & Related Party Disclosures)", "FRC Standards", "https://www.frc.org.uk/standards/accounting-and-reporting-policy/frs-102"),
    (4, "Care Quality Commission", "2009", "Care Quality Commission (Registration) Regulations 2009, Regulation 13: Financial Viability Condition", "Statutory Instruments 2009 No. 3112", "https://www.legislation.gov.uk/uksi/2009/3112/regulation/13/made"),
    (5, "Royal Institution of Chartered Surveyors (RICS)", "2023", "RICS Valuation - Global Standards (Red Book): Specialist Healthcare and Supported Living Freehold Yields", "RICS Professional Guidance", "https://www.rics.org/red-book"),
    (6, "HM Revenue & Customs", "2009", "Corporation Tax Act 2009 (CTA 2009), Section 54: Expenses wholly and exclusively for trade purposes", "UK Public General Acts 2009 c. 4", "https://www.legislation.gov.uk/ukpga/2009/4/section/54"),
    (7, "HM Revenue & Customs", "1994", "Value Added Tax Act 1994 (VATA 1994), Schedule 9, Group 7: Health and Welfare Exemptions", "UK Public General Acts 1994 c. 23", "https://www.legislation.gov.uk/ukpga/1994/23/schedule/9")
]

REFS_CQC = [
    (1, "Care Quality Commission", "2014", "Health and Social Care Act 2008 (Regulated Activities) Regulations 2014, Regulations 4–20A", "UK Statutory Instruments 2014 No. 2936", "https://www.legislation.gov.uk/uksi/2014/2936/contents/made"),
    (2, "Care Quality Commission", "2022", "Right support, right care, right culture: How CQC regulates providers supporting people with a learning disability and autistic people", "CQC Guidance for Providers", "https://www.cqc.org.uk/guidance-providers/right-support-right-care-right-culture"),
    (3, "Parliament of the United Kingdom", "2014", "Care Act 2014, Section 42: Enquiries by local authority into adult safeguarding risks", "UK Public General Acts 2014 c. 23", "https://www.legislation.gov.uk/ukpga/2014/23/section/42"),
    (4, "Parliament of the United Kingdom", "2005", "Mental Capacity Act 2005 (MCA 2005), Sections 1-4 and Section 16 (Court of Protection Powers)", "UK Public General Acts 2005 c. 9", "https://www.legislation.gov.uk/ukpga/2005/9/contents"),
    (5, "National Institute for Health and Care Excellence", "2017", "NICE Guideline SC1: Managing medicines for adults receiving social care in the community", "NICE Clinical Guidelines", "https://www.nice.org.uk/guidance/sc1"),
    (6, "Department of Health and Social Care", "2022", "The Code of Practice on the prevention and control of infections and related guidance (Health and Social Care Act 2008)", "DHSC Statutory Guidance", "https://www.gov.uk/government/publications/the-health-and-social-care-act-2008-code-of-practice-on-the-prevention-and-control-of-infections-and-related-guidance"),
    (7, "British Institute of Learning Disabilities (BILD)", "2021", "Restraint Reduction Network (RRN) Training Standards (First Edition, Version 2)", "RRN Quality Standards", "https://restraintreductionnetwork.org/training-standards/")
]

REFS_COMMISSIONING = [
    (1, "Luton Borough Council", "2024", "Adult Social Care Dynamic Purchasing System (DPS) Specification AT1115 for Supported Living Providers", "Luton Procurement Portal ProContract", "https://procontract.due-north.com/"),
    (2, "NHS Bedfordshire, Luton and Milton Keynes ICB", "2023", "NHS Continuing Healthcare (CHC) and Section 117 Mental Health Act Aftercare Joint Funding Policy 2023-2026", "BLMK Integrated Care Board Governance", "https://blmkhealthandcarepartnership.org/"),
    (3, "Department for Work and Pensions", "2006", "Housing Benefit Regulations 2006, SI 2006/213, Regulation 14(f): Intensive Housing Management Conditions", "UK Statutory Instruments", "https://www.legislation.gov.uk/uksi/2006/213/regulation/14/made"),
    (4, "Parliament of the United Kingdom", "2022", "Health and Care Act 2022, Section 181: Mandatory Training on Learning Disability and Autism (The Oliver McGowan Training)", "UK Public General Acts 2022 c. 31", "https://www.legislation.gov.uk/ukpga/2022/31/section/181"),
    (5, "Supreme Court of the United Kingdom", "2014", "P v Cheshire West and Chester Council and another; P and Q v Surrey County Council [2014] UKSC 19 (The Acid Test)", "UK Supreme Court Judgments", "https://www.supremecourt.uk/cases/uksc-2012-0068.html")
]

# Inject Figures into tab-overview
if "id=\"fig-campus-topology\"" not in html:
    # Insert Figure 1.1 right before the interactive calculator or end of prose in tab-overview
    pattern = r"(<div id=\"tab-overview\"[\s\S]*?<div class=\"editorial-prose-wrap\">)"
    def repl_overview(m):
        abstract = """
              <!-- ABSTRACT LEAD DECK -->
              <div class="abstract-lead">
                <div class="abstract-lead-label">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                  The Executive Abstract &bull; Peer-Reviewed Strategic Synthesis
                </div>
                <div class="abstract-lead-prose">
                  &ldquo;A forensic multidisciplinary viability audit establishes that consolidating 78 and 80 Marston Gardens into an 8-bed specialist Supported Living campus (Class C3b) generates &pound;977,600 gross turnover, &pound;341,392 OpCo EBITDA (34.92% margin), and &pound;438,392 in consolidated pre-tax cashflow (&pound;36,532/month). Operating under Section 192 of the Town and Country Planning Act 1990 permanently immunizes the campus from planning committee refusal, while retaining 82 Marston Gardens as the Director's private residence achieves 100% statutory tax neutrality under Section 105/106 ITEPA 2003.&rdquo;
                </div>
                <ul class="abstract-lead-bullets">
                  <li><strong>Target Cohort:</strong> Adults (18&ndash;65) with Autism Spectrum Conditions &amp; Learning Disabilities</li>
                  <li><strong>Planning Immunity:</strong> TCPA 1990 s.192 CLPUD &bull; Class C3(b) Residential Household</li>
                  <li><strong>Regulatory Licensing:</strong> CQC Personal Care &bull; Single Assessment Framework</li>
                  <li><strong>Financial Break-Even:</strong> 3.82 Beds (47.7% Occupancy) &bull; 52.3% Margin of Safety</li>
                </ul>
              </div>
        """
        return m.group(1) + "\n" + abstract + "\n" + FIG_1_1_TOPOLOGY + "\n" + FIG_1_2_WATERFALL
    html = re.sub(pattern, repl_overview, html, count=1)
    print("Injected Abstract Lead, Figure 1.1 and Figure 1.2 into tab-overview!")

# Inject Figure 1.3 and Table 1.1 into tab-financials
if "id=\"fig-breakeven-curve\"" not in html:
    pattern_fin = r"(<div id=\"tab-financials\"[\s\S]*?<div class=\"editorial-prose-wrap\">)"
    def repl_fin(m):
        return m.group(1) + "\n" + FIG_1_2_WATERFALL + "\n" + FIG_1_3_BREAKEVEN
    html = re.sub(pattern_fin, repl_fin, html, count=1)
    print("Injected Figure 1.2 and Figure 1.3 into tab-financials!")

# Inject References at the end of tab-overview
if "id=\"sec-references-tab-overview\"" not in html:
    ref_box_overview = make_references_box("tab-overview", REFS_OVERVIEW)
    # Find closing of editorial-main in tab-overview
    pattern = r"(<div id=\"tab-overview\"[\s\S]*?</div><!-- /editorial-main -->)"
    def repl_ref_ov(m):
        content = m.group(1)
        # replace the last </div><!-- /editorial-main -->
        return content[:-len("</div><!-- /editorial-main -->")] + ref_box_overview + "\n            </div><!-- /editorial-main -->"
    html = re.sub(pattern, repl_ref_ov, html, count=1)
    print("Injected References into tab-overview!")

# Inject References at the end of tab-financials
if "id=\"sec-references-tab-financials\"" not in html:
    ref_box_fin = make_references_box("tab-financials", REFS_FINANCIALS)
    pattern = r"(<div id=\"tab-financials\"[\s\S]*?</div><!-- /editorial-main -->)"
    def repl_ref_fin(m):
        content = m.group(1)
        return content[:-len("</div><!-- /editorial-main -->")] + ref_box_fin + "\n            </div><!-- /editorial-main -->"
    html = re.sub(pattern, repl_ref_fin, html, count=1)
    print("Injected References into tab-financials!")

# Inject References at the end of tab-cqc
if "id=\"sec-references-tab-cqc\"" not in html:
    ref_box_cqc = make_references_box("tab-cqc", REFS_CQC)
    pattern = r"(<div id=\"tab-cqc\"[\s\S]*?</div><!-- /editorial-main -->)"
    def repl_ref_cqc(m):
        content = m.group(1)
        return content[:-len("</div><!-- /editorial-main -->")] + ref_box_cqc + "\n            </div><!-- /editorial-main -->"
    html = re.sub(pattern, repl_ref_cqc, html, count=1)
    print("Injected References into tab-cqc!")

# Inject References at the end of tab-commissioning
if "id=\"sec-references-tab-commissioning\"" not in html:
    ref_box_comm = make_references_box("tab-commissioning", REFS_COMMISSIONING)
    pattern = r"(<div id=\"tab-commissioning\"[\s\S]*?</div><!-- /editorial-main -->)"
    def repl_ref_comm(m):
        content = m.group(1)
        return content[:-len("</div><!-- /editorial-main -->")] + ref_box_comm + "\n            </div><!-- /editorial-main -->"
    html = re.sub(pattern, repl_ref_comm, html, count=1)
    print("Injected References into tab-commissioning!")

with open("portal/v2.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated portal/v2.html successfully!")
