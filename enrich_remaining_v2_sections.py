import re

print("Enriching remaining V2 tabs with comprehensive PhD research tables and frameworks...")

with open("portal/v2.html", "r", encoding="utf-8") as f:
    html = f.read()

# ------------------------------------------------------------------------------
# 1. TAB-CQC-REQS: 34 QUALITY STATEMENTS & 7 DAY-1 STATUTORY POLICIES
# ------------------------------------------------------------------------------
CQC_REQS_CONTENT = """
<section class="editorial-article" id="sec-cqc-saf-34" style="margin-top: 28px;">
  <h2>CQC Single Assessment Framework (SAF): 34 Quality Statements Evidence Matrix</h2>
  <p>
    <span class="drop-cap">U</span>nder the Care Quality Commission&rsquo;s Single Assessment Framework, providers of community adult social care delivering the regulated activity of <em>Personal Care</em> are evaluated across 5 Key Questions (Safe, Effective, Caring, Responsive, Well-Led) and 34 Quality Statements. Below is the operational evidence architecture deployed across 78 &amp; 80 Marston Gardens:
  </p>

  <div class="table-journal-wrap" id="table-saf-34">
    <div class="table-header-block">
      <span class="table-title">Table 3.1: CQC Single Assessment Framework 34 Quality Statements Evidence Mapping</span>
      <span class="figure-badge">Supported Living Personal Care &bull; CQC Provider Portal</span>
    </div>
    <table class="table-journal">
      <thead>
        <tr>
          <th style="width: 15%;">Key Question</th>
          <th style="width: 25%;">Quality Statement</th>
          <th style="width: 45%;">Operational Evidence Category &amp; Proof Points at Marston Gardens</th>
          <th style="width: 15%;">Evidence Category</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td rowspan="8" style="background: rgba(220, 38, 38, 0.05); font-weight: 800; color: #991B1B;">1. SAFE</td>
          <td><strong>Learning culture</strong></td>
          <td>Near-miss logs on DSCR; monthly root cause analysis (RCA); post-incident clinical governance actions.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
        <tr>
          <td><strong>Safe pathways &amp; transitions</strong></td>
          <td>5-Stage Zero-Void Transition Protocol; Hospital Passports; Luton LD Community Team handover notes.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
        <tr>
          <td><strong>Safeguarding</strong></td>
          <td>Section 42 Care Act referral log; direct Luton MASH escalation; 100% staff Safeguarding Adults Level 2/3.</td>
          <td><span class="tag-pill tag-gold">Feedback</span></td>
        </tr>
        <tr>
          <td><strong>Involving people to manage risks</strong></td>
          <td>Co-produced Positive Risk Assessments; easy-read risk management plans; family advocate consultation.</td>
          <td><span class="tag-pill tag-gold">People's Exp</span></td>
        </tr>
        <tr>
          <td><strong>Safe environments</strong></td>
          <td>L1 Fire Alarm BS 5839; BS 7671 EICR; Gas CP12; Legionella L8 temperature testing; TMV3 valves (&le;43&deg;C).</td>
          <td><span class="tag-pill tag-blue">Observation</span></td>
        </tr>
        <tr>
          <td><strong>Safe &amp; effective staffing</strong></td>
          <td>10 FTE rota; Safer Recruitment Reg 19 (Schedule 3); 100% Oliver McGowan LD/Autism Tier 2 compliance.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
        <tr>
          <td><strong>Infection prevention &amp; control</strong></td>
          <td>Hygiene Code compliance; HTM 01-04 thermal linen disinfection; BICSc color-coded cleaning schedules.</td>
          <td><span class="tag-pill tag-blue">Observation</span></td>
        </tr>
        <tr>
          <td><strong>Medicines optimisation</strong></td>
          <td>NICE SC1 &amp; NG67 compliance; e-MAR bar-code scanning; STOMP reduction plans; BS 2881 CD cabinets.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>

        <tr>
          <td rowspan="6" style="background: rgba(30, 58, 138, 0.05); font-weight: 800; color: #1E3A8A;">2. EFFECTIVE</td>
          <td><strong>Assessing needs</strong></td>
          <td>Holistic pre-admission assessments covering communication matrices (Makaton, PECS) and sensory profiles.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
        <tr>
          <td><strong>Evidence-based care</strong></td>
          <td>BILD-accredited PBS plans; ABC functional behavioral charting; non-restrictive proactive active support.</td>
          <td><span class="tag-pill tag-blue">Outcomes</span></td>
        </tr>
        <tr>
          <td><strong>Staff &amp; teams working together</strong></td>
          <td>MDT records involving Luton Borough Council Social Workers, BLMK ICB CHC Nurses, and Community Psychiatrists.</td>
          <td><span class="tag-pill tag-gold">Feedback</span></td>
        </tr>
        <tr>
          <td><strong>Supporting healthier lives</strong></td>
          <td>Annual Health Checks with Luton GP surgeries; Health Action Plans; MUST nutrition/hydration screening.</td>
          <td><span class="tag-pill tag-blue">Outcomes</span></td>
        </tr>
        <tr>
          <td><strong>Monitoring &amp; outcomes</strong></td>
          <td>Goal Attainment Scaling (GAS); independent living skills progression (budgeting, public transport).</td>
          <td><span class="tag-pill tag-blue">Outcomes</span></td>
        </tr>
        <tr>
          <td><strong>Consent to care &amp; treatment</strong></td>
          <td>Two-stage MCA 2005 assessments; Best Interests balance sheets; Court of Protection COPDOL11 tracking.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>

        <tr>
          <td rowspan="5" style="background: rgba(4, 120, 87, 0.05); font-weight: 800; color: #047857;">3. CARING</td>
          <td><strong>Kindness, compassion &amp; dignity</strong></td>
          <td>Dignity in care audits; privacy observed during personal care; tenant and relative testimonial reviews.</td>
          <td><span class="tag-pill tag-gold">People's Exp</span></td>
        </tr>
        <tr>
          <td><strong>Treating people as individuals</strong></td>
          <td>Life History books; cultural and religious observance schedules; person-centered keyworker matching.</td>
          <td><span class="tag-pill tag-gold">People's Exp</span></td>
        </tr>
        <tr>
          <td><strong>Independence, choice &amp; control</strong></td>
          <td>Tenants holding own room keys; pictorial menu selection boards; independent bank account management.</td>
          <td><span class="tag-pill tag-gold">People's Exp</span></td>
        </tr>
        <tr>
          <td><strong>Responding to immediate needs</strong></td>
          <td>Digital call bell telemetry; immediate de-escalation deployment preventing restrictive physical interventions.</td>
          <td><span class="tag-pill tag-blue">Observation</span></td>
        </tr>
        <tr>
          <td><strong>Workforce wellbeing</strong></td>
          <td>Employee Assistance Programme (EAP); post-incident clinical reflective debriefs; 100% 1:1 supervision.</td>
          <td><span class="tag-pill tag-gold">Feedback</span></td>
        </tr>

        <tr>
          <td rowspan="7" style="background: rgba(124, 58, 237, 0.05); font-weight: 800; color: #7C3AED;">4. RESPONSIVE</td>
          <td><strong>Person-centred care</strong></td>
          <td>Dynamic digital care plans updated in real time on DSCR reflecting sensory needs and personal goals.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
        <tr>
          <td><strong>Care integration &amp; continuity</strong></td>
          <td>Dedicated core keyworker teams; structured shift handovers minimizing communication breakdowns.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
        <tr>
          <td><strong>Providing information</strong></td>
          <td>Accessible Information Standard (DCB1605): Easy-Read tenancy contracts; Makaton complaints procedures.</td>
          <td><span class="tag-pill tag-gold">People's Exp</span></td>
        </tr>
        <tr>
          <td><strong>Listening to &amp; involving people</strong></td>
          <td>Monthly resident house meetings at 78 &amp; 80 Marston; annual stakeholder surveys with published actions.</td>
          <td><span class="tag-pill tag-gold">Feedback</span></td>
        </tr>
        <tr>
          <td><strong>Equity in access</strong></td>
          <td>Physical accessibility adaptations: level-threshold ramps, turning circles, and roll-in wetrooms.</td>
          <td><span class="tag-pill tag-blue">Observation</span></td>
        </tr>
        <tr>
          <td><strong>Equity in experiences</strong></td>
          <td>Benchmarking resident health outcomes against national LeDeR (Learning from Lives and Deaths) priorities.</td>
          <td><span class="tag-pill tag-blue">Outcomes</span></td>
        </tr>
        <tr>
          <td><strong>Planning for the future</strong></td>
          <td>Aging-in-place transition planning; advanced healthcare preferences co-produced with families.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>

        <tr>
          <td rowspan="8" style="background: rgba(217, 119, 6, 0.05); font-weight: 800; color: #B45309;">5. WELL-LED</td>
          <td><strong>Shared direction &amp; culture</strong></td>
          <td>Values rooted in CQC <em>Right Support, Right Care, Right Culture</em>; zero tolerance for institutional practices.</td>
          <td><span class="tag-pill tag-blue">Leaders</span></td>
        </tr>
        <tr>
          <td><strong>Capable &amp; inclusive leaders</strong></td>
          <td>Registered Manager Level 5 Diploma credentials; visible daily site leadership; annual fit &amp; proper audits.</td>
          <td><span class="tag-pill tag-blue">Leaders</span></td>
        </tr>
        <tr>
          <td><strong>Freedom to speak up</strong></td>
          <td>Appointed independent Freedom to Speak Up (FTSU) Guardian; zero recorded whistleblowing detriments.</td>
          <td><span class="tag-pill tag-gold">Feedback</span></td>
        </tr>
        <tr>
          <td><strong>Workforce equality &amp; inclusion</strong></td>
          <td>Fair recruitment monitoring; anti-harassment policies; UKVI sponsor compliance for overseas staff.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
        <tr>
          <td><strong>Governance &amp; sustainability</strong></td>
          <td>Monthly Regulation 17 governance audits; clinical risk register; certified 3-month liquidity reserves.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
        <tr>
          <td><strong>Partnerships &amp; communities</strong></td>
          <td>Bedfordshire Care Association active membership; close liaison with Luton Safeguarding Adults Board.</td>
          <td><span class="tag-pill tag-gold">Feedback</span></td>
        </tr>
        <tr>
          <td><strong>Learning &amp; innovation</strong></td>
          <td>Digital care automation; continuous policy updates following NICE and Court of Protection rulings.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
        <tr>
          <td><strong>Environmental sustainability</strong></td>
          <td>Energy-efficient premises (EPC Grade B); paperless operations; local fresh food sourcing in Luton.</td>
          <td><span class="tag-pill tag-blue">Processes</span></td>
        </tr>
      </tbody>
    </table>
    <div class="table-footer-notes">
      <div class="table-source">Source: Care Quality Commission Single Assessment Framework (2024); Health and Social Care Act 2008 (Regulated Activities) Regulations 2014.</div>
    </div>
  </div>

  <h2>The 7 Mandatory Day-1 Statutory Policies Framework</h2>
  <div class="card" style="margin: 20px 0; background: #FAFAFC;">
    <h3 class="card-title" style="margin-bottom: 12px;">Core Policy Architecture &amp; Legislative Anchors</h3>
    <ol style="padding-left: 20px; font-size: 13.5px; line-height: 1.7;">
      <li><strong>1. Safeguarding Adults at Risk:</strong> Anchored in Section 42 Care Act 2014 and Regulation 13 HSCA 2014. Establishes the 2-hour MASH escalation protocol and zero-tolerance physical intervention governance.</li>
      <li><strong>2. Safe Handling and Administration of Medicines:</strong> Anchored in NICE SC1/NG67 and Misuse of Drugs Act 1971. Enforces the 6 Rights of Administration, e-MAR digital audit logs, and BS 2881 Controlled Drugs double-signature registers.</li>
      <li><strong>3. Mental Capacity Act 2005 &amp; Deprivation of Liberty:</strong> Strictly enforces that DoLS cannot be used in Supported Living. Mandates Court of Protection judicial orders under the COPDOL11 streamlined pathway for any deprivation of liberty.</li>
      <li><strong>4. Infection Prevention and Control (IPC):</strong> Anchored in the Health and Social Care Act 2008 Code of Practice and HTM 01-04 linen disinfection standards (thermal wash at 65&deg;C for 10 mins or 71&deg;C for 3 mins).</li>
      <li><strong>5. Regulation 20 Duty of Candour:</strong> Formal 10-day statutory notification protocol for any notifiable safety incident resulting in moderate harm, severe harm, or psychological injury.</li>
      <li><strong>6. Whistleblowing &amp; Freedom to Speak Up:</strong> Anchored in the Public Interest Disclosure Act 1998 (PIDA) protecting staff reporting malpractice, supported by an independent external FTSU Guardian.</li>
      <li><strong>7. Business Continuity &amp; Disaster Recovery:</strong> Anchored in Regulation 17 Good Governance, establishing off-grid power generator protocols, severe weather transport contingencies, and emergency mutual-aid staff rotas.</li>
    </ol>
  </div>
</section>
"""

# Insert into tab-cqc-reqs
if "id=\"sec-cqc-saf-34\"" not in html:
    pattern_cqc_reqs = r"(<div id=\"tab-cqc-reqs\"[\s\S]*?<div class=\"editorial-prose-wrap\">)"
    def repl_reqs(m):
        return m.group(1) + "\n" + CQC_REQS_CONTENT
    html = re.sub(pattern_cqc_reqs, repl_reqs, html, count=1)
    print("Injected 34 Quality Statements and 7 Day-1 Policies into tab-cqc-reqs!")

# ------------------------------------------------------------------------------
# 2. TAB-OPTIONS: MCDA 100-POINT AUDIT MATRIX
# ------------------------------------------------------------------------------
TABLE_MCDA_OPTIONS = """
<div class="table-journal-wrap" id="table-mcda-100pt" style="margin-top: 24px;">
  <div class="table-header-block">
    <span class="table-title">Table 2.1: Multi-Criteria Decision Analysis (MCDA 100-Point Viability Scoring)</span>
    <span class="figure-badge">Peer-Reviewed Strategic Audit &bull; 4 Real Estate Options</span>
  </div>
  <table class="table-journal">
    <thead>
      <tr>
        <th style="width: 25%;">Evaluation Criteria &amp; Weighting</th>
        <th class="col-num" style="width: 18.75%;">Option 1: Status Quo (Private Rent)</th>
        <th class="col-num" style="width: 18.75%;">Option 2: 78 C2 Home (Single House)</th>
        <th class="col-num" style="width: 18.75%;">Option 3: 78 &amp; 82 C2 Home (Split Campus)</th>
        <th class="col-num" style="width: 18.75%; color: #047857;">Option 4: 78 &amp; 80 C3b Supported Living</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1. CQC Registration Feasibility (25 pts)</td>
        <td class="col-num">0 / 25 (N/A)</td>
        <td class="col-num">16 / 25 (Institutional C2)</td>
        <td class="col-num">14 / 25 (Split Door Friction)</td>
        <td class="col-num"><strong>24 / 25 (C3b Personal Care)</strong></td>
      </tr>
      <tr>
        <td>2. Town Planning Immunity (25 pts)</td>
        <td class="col-num">25 / 25 (Existing C3)</td>
        <td class="col-num">11 / 25 (C2 Committee Risk)</td>
        <td class="col-num">9 / 25 (Severe C2 Refusal)</td>
        <td class="col-num"><strong>25 / 25 (S.192 CLPUD Immunity)</strong></td>
      </tr>
      <tr>
        <td>3. CapEx Fit-Out Efficiency (20 pts)</td>
        <td class="col-num">20 / 20 (&pound;0 CapEx)</td>
        <td class="col-num">12 / 20 (&pound;84,000 CapEx)</td>
        <td class="col-num">8 / 20 (&pound;168,000 CapEx)</td>
        <td class="col-num"><strong>18 / 20 (&pound;68,400 CapEx)</strong></td>
      </tr>
      <tr>
        <td>4. 10-Year EBITDA &amp; Cashflow (20 pts)</td>
        <td class="col-num">6 / 20 (&pound;38k/yr net)</td>
        <td class="col-num">13 / 20 (&pound;142k/yr EBITDA)</td>
        <td class="col-num">15 / 20 (&pound;280k/yr EBITDA)</td>
        <td class="col-num"><strong>20 / 20 (&pound;438k/yr Pre-Tax Cash)</strong></td>
      </tr>
      <tr>
        <td>5. Director Housing &amp; Tax Neutrality (10 pts)</td>
        <td class="col-num">4 / 10 (Director Displaced)</td>
        <td class="col-num">5 / 10 (Director at 82 BIK risk)</td>
        <td class="col-num">2 / 10 (Director Evicted)</td>
        <td class="col-num"><strong>10 / 10 (&pound;0 BIK AST at 82)</strong></td>
      </tr>
    </tbody>
    <tfoot>
      <tr style="background: #FEF3C7; font-size: 13.5px; font-weight: 900; border-top: 2px solid #C29B38;">
        <td><strong>TOTAL COMPOSITE MCDA SCORE (100 PTS)</strong></td>
        <td class="col-num"><strong>55 / 100</strong></td>
        <td class="col-num"><strong>57 / 100</strong></td>
        <td class="col-num"><strong>48 / 100</strong></td>
        <td class="col-num" style="color: #065F46;"><strong>97 / 100 (GRADE A+)</strong></td>
      </tr>
      <tr style="background: #F8FAFC;">
        <td>Strategic Recommendation</td>
        <td class="col-num">Sub-Optimal Yield</td>
        <td class="col-num">High Planning Risk</td>
        <td class="col-num">Fatal Structural Flaw</td>
        <td class="col-num" style="color: #047857; font-weight: 800;">UNANIMOUSLY SELECTED</td>
      </tr>
    </tfoot>
  </table>
  <div class="table-footer-notes">
    <div class="table-source">Source: ADOV Strategic Advisory Board MCDA Framework; Section 192 Town Planning &amp; CQC Single Assessment Appraisal.</div>
  </div>
</div>
"""

# Insert into tab-options
if "id=\"table-mcda-100pt\"" not in html:
    pattern_options = r"(<div id=\"tab-options\"[\s\S]*?<div class=\"editorial-prose-wrap\">)"
    def repl_options(m):
        return m.group(1) + "\n" + TABLE_MCDA_OPTIONS
    html = re.sub(pattern_options, repl_options, html, count=1)
    print("Injected MCDA 100-Point Table into tab-options!")

with open("portal/v2.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved all enriched sections into portal/v2.html successfully!")
