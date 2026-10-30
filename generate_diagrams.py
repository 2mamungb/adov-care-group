import os

os.makedirs('portal/assets/diagrams', exist_ok=True)

# 1. Campus Masterplan Diagram
svg_campus = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <linearGradient id="gradSky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F1F5F9" />
      <stop offset="100%" stop-color="#E2E8F0" />
    </linearGradient>
    <linearGradient id="grad78" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="grad80" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#047857" />
      <stop offset="100%" stop-color="#064E3B" />
    </linearGradient>
    <linearGradient id="grad82" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569" />
      <stop offset="100%" stop-color="#334155" />
    </linearGradient>
    <linearGradient id="gradGarden" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#D1FAE5" />
      <stop offset="100%" stop-color="#A7F3D0" />
    </linearGradient>
    <filter id="shadowCard" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-opacity="0.12" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="960" height="480" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5" />

  <!-- Road / Front Access -->
  <rect x="40" y="40" width="880" height="42" rx="8" fill="#E2E8F0" stroke="#CBD5E1" stroke-width="1" />
  <text x="480" y="66" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#64748B" text-anchor="middle" letter-spacing="1.5">MARSTON GARDENS (RESIDENTIAL CUL-DE-SAC // HIGHWAYS COMPLIANT)</text>

  <!-- PARKING DRIVEWAYS -->
  <!-- Flank Left Parking (80) -->
  <rect x="60" y="96" width="100" height="110" rx="8" fill="#F1F5F9" stroke="#94A3B8" stroke-dasharray="4,4" />
  <text x="110" y="145" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">4 CARS</text>
  <text x="110" y="162" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Outer Flank Driveway</text>

  <!-- Flank Right Parking (78) -->
  <rect x="800" y="96" width="100" height="110" rx="8" fill="#F1F5F9" stroke="#94A3B8" stroke-dasharray="4,4" />
  <text x="850" y="145" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">4 CARS</text>
  <text x="850" y="162" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Outer Flank Driveway</text>

  <!-- HOUSES ROW -->
  <!-- 80 Marston Gardens (Left House) -->
  <g filter="url(#shadowCard)">
    <rect x="180" y="96" width="280" height="160" rx="12" fill="url(#grad80)" stroke="#10B981" stroke-width="2" />
    <rect x="195" y="112" width="110" height="22" rx="4" fill="rgba(255,255,255,0.18)" />
    <text x="250" y="127" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#A7F3D0" text-anchor="middle">80 MARSTON GDNS</text>
    <text x="320" y="128" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#FFFFFF">3 SPECIALIST SUITES</text>

    <!-- Rooms Breakdown inside 80 -->
    <rect x="195" y="145" width="125" height="46" rx="6" fill="rgba(255,255,255,0.1)" />
    <text x="257" y="163" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">3 Ground/1st Beds</text>
    <text x="257" y="179" font-family="-apple-system, sans-serif" font-size="9" fill="#D1FAE5" text-anchor="middle">Large Wetroom + Sep WC</text>

    <rect x="330" y="145" width="115" height="46" rx="6" fill="rgba(255,255,255,0.1)" />
    <text x="387" y="163" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Sensory Lounge</text>
    <text x="387" y="179" font-family="-apple-system, sans-serif" font-size="9" fill="#FCD34D" text-anchor="middle">Calm Sensory Hub</text>

    <rect x="195" y="200" width="250" height="42" rx="6" fill="rgba(255,255,255,0.12)" />
    <text x="320" y="217" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Staff Office & Sleep-In Suite</text>
    <text x="320" y="232" font-family="-apple-system, sans-serif" font-size="9" fill="#93C5FD" text-anchor="middle">Secure CD Meds BS 2881 Cabinet</text>
  </g>

  <!-- PARTY WALL INDICATOR -->
  <line x1="480" y1="96" x2="480" y2="256" stroke="#C5A059" stroke-width="3" stroke-dasharray="6,4" />
  <circle cx="480" cy="176" r="14" fill="#C5A059" />
  <text x="480" y="180" font-family="-apple-system, sans-serif" font-size="10" font-weight="900" fill="#1E293B" text-anchor="middle">PW</text>

  <!-- 78 Marston Gardens (Right House) -->
  <g filter="url(#shadowCard)">
    <rect x="500" y="96" width="280" height="160" rx="12" fill="url(#grad78)" stroke="#3B82F6" stroke-width="2" />
    <rect x="515" y="112" width="110" height="22" rx="4" fill="rgba(255,255,255,0.18)" />
    <text x="570" y="127" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#93C5FD" text-anchor="middle">78 MARSTON GDNS</text>
    <text x="640" y="128" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#FFFFFF">5 SPECIALIST SUITES</text>

    <!-- Rooms Breakdown inside 78 -->
    <rect x="515" y="145" width="125" height="46" rx="6" fill="rgba(255,255,255,0.1)" />
    <text x="577" y="163" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">5 Beds (1 En-Suite)</text>
    <text x="577" y="179" font-family="-apple-system, sans-serif" font-size="9" fill="#93C5FD" text-anchor="middle">Large Wetroom + Sep WC</text>

    <rect x="650" y="145" width="115" height="46" rx="6" fill="rgba(255,255,255,0.1)" />
    <text x="707" y="163" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Commercial Kitchen</text>
    <text x="707" y="179" font-family="-apple-system, sans-serif" font-size="9" fill="#FCD34D" text-anchor="middle">Food Hygiene 5 Rating</text>

    <rect x="515" y="200" width="250" height="42" rx="6" fill="rgba(255,255,255,0.12)" />
    <text x="640" y="217" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Communal Dining & Activity Hall</text>
    <text x="640" y="232" font-family="-apple-system, sans-serif" font-size="9" fill="#A7F3D0" text-anchor="middle">Bi-Fold Access directly to Sensory Garden</text>
  </g>

  <!-- 100FT ENCLOSED SENSORY REAR GARDENS -->
  <rect x="180" y="280" width="600" height="120" rx="12" fill="url(#gradGarden)" stroke="#059669" stroke-width="1.5" stroke-dasharray="5,3" />
  <text x="480" y="315" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#065F46" text-anchor="middle">100FT PRIVATE ENCLOSED SENSORY REAR GARDENS</text>
  <text x="480" y="336" font-family="-apple-system, sans-serif" font-size="11" fill="#047857" text-anchor="middle">Outdoor Therapeutic Pathways • Raised Sensory Herb Planters • 6ft Security Fencing • De-escalation Space</text>

  <!-- Garden Amenities Badges -->
  <rect x="230" y="352" width="140" height="30" rx="15" fill="#FFFFFF" stroke="#10B981" />
  <text x="300" y="371" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Therapeutic Pavilion</text>

  <rect x="410" y="352" width="140" height="30" rx="15" fill="#FFFFFF" stroke="#10B981" />
  <text x="480" y="371" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Tactile Acoustic Features</text>

  <rect x="590" y="352" width="140" height="30" rx="15" fill="#FFFFFF" stroke="#10B981" />
  <text x="660" y="371" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Safe De-escalation Zone</text>

  <!-- Campus Summary Strip -->
  <rect x="40" y="420" width="880" height="42" rx="8" fill="#1E293B" />
  <text x="480" y="445" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#F8FAFC" text-anchor="middle">
    UNIFIED 8-BED CAMPUS: 78 (5 Beds) + 80 (3 Beds) // 8 Parking Spaces // 82 Retained as Director Residence (BIK Exempt s.105/106)
  </text>
</svg>"""

with open('portal/assets/diagrams/diagram_campus_masterplan.svg', 'w', encoding='utf-8') as f:
    f.write(svg_campus)
print("Generated diagram_campus_masterplan.svg")

# 2. Corporate Structure Diagram
svg_corp = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 440" width="100%" height="100%">
  <defs>
    <linearGradient id="gradNavy" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="gradGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#B45309" />
      <stop offset="100%" stop-color="#78350F" />
    </linearGradient>
    <linearGradient id="gradGreen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#047857" />
      <stop offset="100%" stop-color="#064E3B" />
    </linearGradient>
  </defs>

  <rect width="960" height="440" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5" />

  <!-- TOP TIER: HOLDING COMPANY -->
  <rect x="330" y="30" width="300" height="85" rx="12" fill="url(#gradNavy)" stroke="#38BDF8" stroke-width="1.5" />
  <text x="480" y="58" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#38BDF8" text-anchor="middle" letter-spacing="1">PARENT HOLDING CO (100% ULTIMATE OWNER)</text>
  <text x="480" y="82" font-family="-apple-system, sans-serif" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">MAMUN LIMITED</text>
  <text x="480" y="100" font-family="-apple-system, sans-serif" font-size="10.5" fill="#94A3B8" text-anchor="middle">Sole Shareholder &amp; Ultimate Beneficiary</text>

  <!-- Connectors -->
  <line x1="480" y1="115" x2="480" y2="155" stroke="#94A3B8" stroke-width="2" />
  <line x1="240" y1="155" x2="720" y2="155" stroke="#94A3B8" stroke-width="2" />
  <line x1="240" y1="155" x2="240" y2="185" stroke="#94A3B8" stroke-width="2" marker-end="url(#arrow)" />
  <line x1="720" y1="155" x2="720" y2="185" stroke="#94A3B8" stroke-width="2" marker-end="url(#arrow)" />

  <!-- LEFT: PROPCO -->
  <rect x="90" y="185" width="300" height="150" rx="12" fill="url(#gradGold)" stroke="#F59E0B" stroke-width="1.5" />
  <text x="240" y="212" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FDE68A" text-anchor="middle" letter-spacing="1">PROPERTY CO (PROPCO)</text>
  <text x="240" y="235" font-family="-apple-system, sans-serif" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">ADOV LIMITED</text>
  <text x="240" y="255" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#FEF3C7" text-anchor="middle">Holds 100% Freehold Real Estate</text>

  <rect x="110" y="270" width="260" height="50" rx="8" fill="rgba(0,0,0,0.2)" />
  <text x="240" y="290" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">Freehold Assets: 78, 80 &amp; 82 Marston Gdns</text>
  <text x="240" y="306" font-family="-apple-system, sans-serif" font-size="9.5" fill="#FDE68A" text-anchor="middle">Rental Income: £97,000 / Yr (Commercial FRI)</text>

  <!-- RIGHT: OPCO -->
  <rect x="570" y="185" width="300" height="150" rx="12" fill="url(#gradGreen)" stroke="#10B981" stroke-width="1.5" />
  <text x="720" y="212" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#A7F3D0" text-anchor="middle" letter-spacing="1">OPERATING CARE CO (OPCO)</text>
  <text x="720" y="235" font-family="-apple-system, sans-serif" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">ADOV CARE GROUP LIMITED</text>
  <text x="720" y="255" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#D1FAE5" text-anchor="middle">Regulated Service Provider</text>

  <rect x="590" y="270" width="260" height="50" rx="8" fill="rgba(0,0,0,0.2)" />
  <text x="720" y="290" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">CQC 'Personal Care' Regulated Provider</text>
  <text x="720" y="306" font-family="-apple-system, sans-serif" font-size="9.5" fill="#A7F3D0" text-anchor="middle">Turnover: £977,600 / Yr // EBITDA: £341,392</text>

  <!-- INTERCOMPANY FRI LEASE CONNECTOR -->
  <path d="M 390 260 L 570 260" stroke="#0284C7" stroke-width="3" stroke-dasharray="6,4" />
  <rect x="420" y="244" width="120" height="28" rx="6" fill="#0284C7" />
  <text x="480" y="262" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#FFFFFF" text-anchor="middle">Commercial FRI Lease</text>

  <!-- BOTTOM STRIP: BENEFICIARY / 82 RELOCATION -->
  <rect x="90" y="360" width="780" height="55" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
  <text x="480" y="384" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#1E293B" text-anchor="middle">
    DIRECTOR RESIDENCE AT 82 MARSTON GARDENS: OPEN MARKET AST (s.105/106 ITEPA 2003)
  </text>
  <text x="480" y="402" font-family="-apple-system, sans-serif" font-size="10.5" fill="#059669" text-anchor="middle">
    Paying open market commercial rent eliminates HMRC Benefit in Kind (BIK = Nil) and creates total corporate veil protection.
  </text>
</svg>"""

with open('portal/assets/diagrams/diagram_corporate_structure.svg', 'w', encoding='utf-8') as f:
    f.write(svg_corp)
print("Generated diagram_corporate_structure.svg")

# 3. CQC Approval Roadmap Flow
svg_cqc = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 280" width="100%" height="100%">
  <rect width="960" height="280" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5" />
  <text x="480" y="36" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="1">CQC FAST-TRACK APPROVAL ROADMAP (5 MILESTONE PHASES)</text>

  <!-- Phase 1 -->
  <rect x="30" y="65" width="168" height="150" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5" />
  <rect x="42" y="77" width="60" height="20" rx="4" fill="#E0F2FE" />
  <text x="72" y="91" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#0369A1" text-anchor="middle">PHASE 1</text>
  <text x="42" y="118" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#0F172A">Pre-Application</text>
  <text x="42" y="138" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• CQC DBS Countersign</text>
  <text x="42" y="154" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• GP Medical Form</text>
  <text x="42" y="170" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Statement of Purpose</text>
  <text x="42" y="186" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• 7 Core Safe Policies</text>
  <text x="114" y="204" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#0284C7" text-anchor="middle">Days 1 - 20</text>

  <!-- Phase 2 -->
  <rect x="218" y="65" width="168" height="150" rx="10" fill="#FFFFFF" stroke="#6366F1" stroke-width="1.5" />
  <rect x="230" y="77" width="60" height="20" rx="4" fill="#EEF2FF" />
  <text x="260" y="91" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#4338CA" text-anchor="middle">PHASE 2</text>
  <text x="230" y="118" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#0F172A">Governance &amp; RM</text>
  <text x="230" y="138" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Reg 7 RM Level 5</text>
  <text x="230" y="154" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Reg 6 Nominated Ind</text>
  <text x="230" y="170" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Reg 5 Director FPP</text>
  <text x="230" y="186" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Reg 13 Financial Signoff</text>
  <text x="302" y="204" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#6366F1" text-anchor="middle">Days 21 - 40</text>

  <!-- Phase 3 -->
  <rect x="406" y="65" width="168" height="150" rx="10" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="1.5" />
  <rect x="418" y="77" width="60" height="20" rx="4" fill="#F5F3FF" />
  <text x="448" y="91" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#6D28D9" text-anchor="middle">PHASE 3</text>
  <text x="418" y="118" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#0F172A">Portal Submission</text>
  <text x="418" y="138" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• CQC Provider Portal</text>
  <text x="418" y="154" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Upload Master Dossier</text>
  <text x="418" y="170" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Validation &amp; Receipt</text>
  <text x="418" y="186" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Inspector Assigned</text>
  <text x="490" y="204" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#8B5CF6" text-anchor="middle">Days 41 - 55</text>

  <!-- Phase 4 -->
  <rect x="594" y="65" width="168" height="150" rx="10" fill="#FFFFFF" stroke="#F59E0B" stroke-width="1.5" />
  <rect x="606" y="77" width="60" height="20" rx="4" fill="#FEF3C7" />
  <text x="636" y="91" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#B45309" text-anchor="middle">PHASE 4</text>
  <text x="606" y="118" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#0F172A">RM Interview &amp; Site</text>
  <text x="606" y="138" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• 5 Scenarios Interview</text>
  <text x="606" y="154" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Marston Gdns Inspection</text>
  <text x="606" y="170" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• BS 5839-1 Fire Signoff</text>
  <text x="606" y="186" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">• Notice of Proposal (NOP)</text>
  <text x="678" y="204" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#D97706" text-anchor="middle">Days 56 - 75</text>

  <!-- Phase 5 -->
  <rect x="782" y="65" width="150" height="150" rx="10" fill="#FFFFFF" stroke="#10B981" stroke-width="2" />
  <rect x="794" y="77" width="60" height="20" rx="4" fill="#D1FAE5" />
  <text x="824" y="91" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#047857" text-anchor="middle">PHASE 5</text>
  <text x="794" y="118" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#065F46">Certificate &amp; DPS</text>
  <text x="794" y="138" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">• S.28(3) Fast-Track</text>
  <text x="794" y="154" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">• Cuts 28-day delay</text>
  <text x="794" y="170" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">• CQC Certificate</text>
  <text x="794" y="186" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">• Luton DPS Activated</text>
  <text x="857" y="204" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" fill="#10B981" text-anchor="middle">Day 90 APPROVED</text>

  <!-- Bottom Fast-Track Note -->
  <rect x="30" y="230" width="902" height="34" rx="6" fill="#ECFDF5" stroke="#A7F3D0" />
  <text x="481" y="252" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">
    EXECUTIVE ACCELERATION: Submitting the Section 28(3) Statutory Waiver immediately upon Notice of Proposal cuts 28 days off registration time.
  </text>
</svg>"""

with open('portal/assets/diagrams/diagram_cqc_roadmap.svg', 'w', encoding='utf-8') as f:
    f.write(svg_cqc)
print("Generated diagram_cqc_roadmap.svg")

# 4. MCDA 4 Options Comparison Bar Chart
svg_mcda = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 320" width="100%" height="100%">
  <rect width="960" height="320" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5" />
  <text x="480" y="34" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="1">4-CARE SECTORS MULTI-CRITERIA DECISION ANALYSIS (100-POINT SCORING)</text>

  <!-- Option 4: Supported Living (WINNER) -->
  <g>
    <text x="50" y="78" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#047857">OPTION 4: Supported Living (Autism/LD) — [RECOMMENDED]</text>
    <rect x="50" y="88" width="860" height="32" rx="6" fill="#E2E8F0" />
    <rect x="50" y="88" width="808" height="32" rx="6" fill="#10B981" />
    <text x="825" y="109" font-family="-apple-system, sans-serif" font-size="12" font-weight="900" fill="#FFFFFF">94 / 100</text>
    <text x="65" y="108" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF">£341k EBITDA (35%) • S.192 Planning Immunity • Low CapEx (£68k) • High Local Repatriation Demand</text>
  </g>

  <!-- Option 1: Children's Home -->
  <g>
    <text x="50" y="142" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">Option 1: Ofsted Children's Home (EBD Cohort)</text>
    <rect x="50" y="152" width="860" height="28" rx="6" fill="#E2E8F0" />
    <rect x="50" y="152" width="619" height="28" rx="6" fill="#3B82F6" />
    <text x="640" y="170" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#1E293B">72 / 100</text>
    <text x="65" y="170" font-family="-apple-system, sans-serif" font-size="10" fill="#FFFFFF">High fees (£4.5k/wk) but extreme neighbour objection risk, severe Ofsted enforcement, high staff burnout</text>
  </g>

  <!-- Option 2: Elderly Dementia Care Home -->
  <g>
    <text x="50" y="202" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">Option 2: Elderly Dementia C2 Residential Care Home</text>
    <rect x="50" y="212" width="860" height="28" rx="6" fill="#E2E8F0" />
    <rect x="50" y="212" width="585" height="28" rx="6" fill="#F59E0B" />
    <text x="605" y="230" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#1E293B">68 / 100</text>
    <text x="65" y="230" font-family="-apple-system, sans-serif" font-size="10" fill="#FFFFFF">Full C2 planning permission required, high CapEx (£240k+ lift/sluice), sub-scale margins on only 8 beds</text>
  </g>

  <!-- Option 3: General Shared HMO -->
  <g>
    <text x="50" y="262" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">Option 3: Standard Professional / Student Shared HMO</text>
    <rect x="50" y="272" width="860" height="28" rx="6" fill="#E2E8F0" />
    <rect x="50" y="272" width="499" height="28" rx="6" fill="#94A3B8" />
    <text x="520" y="290" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#1E293B">58 / 100</text>
    <text x="65" y="290" font-family="-apple-system, sans-serif" font-size="10" fill="#FFFFFF">Low regulatory barrier but lowest profitability (£62k/yr net), tenant turnover, zero public sector moat</text>
  </g>
</svg>"""

with open('portal/assets/diagrams/diagram_4options_mcda.svg', 'w', encoding='utf-8') as f:
    f.write(svg_mcda)
print("Generated diagram_4options_mcda.svg")

# 5. Financial Waterfall Chart
svg_fin = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 300" width="100%" height="100%">
  <rect width="960" height="300" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5" />
  <text x="480" y="32" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="1">ANNUAL FINANCIAL FLOW &amp; EBITDA MARGIN CONSOLIDATION (£)</text>

  <!-- Gross Turnover -->
  <rect x="40" y="60" width="130" height="160" rx="8" fill="#1E293B" />
  <text x="105" y="85" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#94A3B8" text-anchor="middle">GROSS TURNOVER</text>
  <text x="105" y="112" font-family="-apple-system, sans-serif" font-size="15" font-weight="900" fill="#FFFFFF" text-anchor="middle">£977,600</text>
  <text x="105" y="132" font-family="-apple-system, sans-serif" font-size="9.5" fill="#38BDF8" text-anchor="middle">8 Beds @ £2,350/wk</text>
  <text x="105" y="150" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">Core + 1:1 + SEA</text>

  <!-- Deductions Arrow -->
  <text x="190" y="145" font-family="-apple-system, sans-serif" font-size="18" font-weight="900" fill="#EF4444" text-anchor="middle">−</text>

  <!-- Care Payroll -->
  <rect x="210" y="75" width="130" height="145" rx="8" fill="#EF4444" />
  <text x="275" y="100" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FEE2E2" text-anchor="middle">CARE PAYROLL</text>
  <text x="275" y="125" font-family="-apple-system, sans-serif" font-size="15" font-weight="900" fill="#FFFFFF" text-anchor="middle">£355,108</text>
  <text x="275" y="145" font-family="-apple-system, sans-serif" font-size="9.5" fill="#FEE2E2" text-anchor="middle">36.3% of Turnover</text>
  <text x="275" y="163" font-family="-apple-system, sans-serif" font-size="9" fill="#FFFFFF" text-anchor="middle">Campus Shared Rota</text>

  <!-- Deductions Arrow -->
  <text x="360" y="145" font-family="-apple-system, sans-serif" font-size="18" font-weight="900" fill="#F59E0B" text-anchor="middle">−</text>

  <!-- PropCo Rent -->
  <rect x="380" y="90" width="130" height="130" rx="8" fill="#D97706" />
  <text x="445" y="115" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#FEF3C7" text-anchor="middle">PROPCO LEASE</text>
  <text x="445" y="140" font-family="-apple-system, sans-serif" font-size="15" font-weight="900" fill="#FFFFFF" text-anchor="middle">£97,000</text>
  <text x="445" y="160" font-family="-apple-system, sans-serif" font-size="9.5" fill="#FEF3C7" text-anchor="middle">78 (£65k) + 80 (£32k)</text>
  <text x="445" y="178" font-family="-apple-system, sans-serif" font-size="9" fill="#FFFFFF" text-anchor="middle">Retained in PropCo</text>

  <!-- Deductions Arrow -->
  <text x="530" y="145" font-family="-apple-system, sans-serif" font-size="18" font-weight="900" fill="#64748B" text-anchor="middle">−</text>

  <!-- Other OpEx -->
  <rect x="550" y="105" width="130" height="115" rx="8" fill="#64748B" />
  <text x="615" y="130" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#F1F5F9" text-anchor="middle">FACILITIES &amp; OPEX</text>
  <text x="615" y="155" font-family="-apple-system, sans-serif" font-size="15" font-weight="900" fill="#FFFFFF" text-anchor="middle">£184,100</text>
  <text x="615" y="175" font-family="-apple-system, sans-serif" font-size="9.5" fill="#F1F5F9" text-anchor="middle">Power, Food, Legal</text>
  <text x="615" y="193" font-family="-apple-system, sans-serif" font-size="9" fill="#FFFFFF" text-anchor="middle">+£70k Contingency</text>

  <!-- Equals Arrow -->
  <text x="700" y="145" font-family="-apple-system, sans-serif" font-size="20" font-weight="900" fill="#10B981" text-anchor="middle">=</text>

  <!-- OpCo EBITDA -->
  <rect x="720" y="60" width="200" height="160" rx="10" fill="#047857" stroke="#10B981" stroke-width="2" />
  <text x="820" y="85" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#A7F3D0" text-anchor="middle">OPCO EBITDA (NET MARGIN)</text>
  <text x="820" y="115" font-family="-apple-system, sans-serif" font-size="20" font-weight="900" fill="#FFFFFF" text-anchor="middle">£341,392</text>
  <text x="820" y="138" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#FCD34D" text-anchor="middle">35.0% OPERATING MARGIN</text>
  <text x="820" y="160" font-family="-apple-system, sans-serif" font-size="10" fill="#A7F3D0" text-anchor="middle">+£28,449 / Month Net Cash</text>
  <text x="820" y="180" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">Group Pre-Tax: £438,392/Yr</text>

  <!-- Bottom Break-Even Pill -->
  <rect x="40" y="240" width="880" height="40" rx="8" fill="#FFFFFF" stroke="#059669" stroke-width="1.5" />
  <text x="480" y="265" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#065F46" text-anchor="middle">
    BREAK-EVEN OCCUPANCY: 3.8 BEDS (47.5%) // 52.5% OCCUPANCY SAFETY BUFFER BEFORE DEFICIT // 100% CQC REG 13 SOLVENT
  </text>
</svg>"""

with open('portal/assets/diagrams/diagram_financial_waterfall.svg', 'w', encoding='utf-8') as f:
    f.write(svg_fin)
print("Generated diagram_financial_waterfall.svg")

# 6. Resident Intake SOP Flowchart
svg_intake = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 260" width="100%" height="100%">
  <rect width="960" height="260" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5" />
  <text x="480" y="32" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="1">ZERO-VOID RESIDENT INTAKE PATHWAY (6 CLINICAL STAGES)</text>

  <!-- Step 1 -->
  <rect x="30" y="60" width="135" height="140" rx="8" fill="#FFFFFF" stroke="#3B82F6" stroke-width="1.5" />
  <rect x="40" y="70" width="50" height="18" rx="4" fill="#DBEAFE" />
  <text x="65" y="83" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#1D4ED8" text-anchor="middle">STAGE 1</text>
  <text x="40" y="106" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#0F172A">Referral Intake</text>
  <text x="40" y="125" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• Luton Council DPS</text>
  <text x="40" y="140" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• BLMK ICB CHC/S117</text>
  <text x="40" y="155" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• Hospital Discharge</text>
  <text x="97" y="185" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#3B82F6" text-anchor="middle">&lt; 24h Response</text>

  <!-- Step 2 -->
  <rect x="180" y="60" width="135" height="140" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5" />
  <rect x="190" y="70" width="50" height="18" rx="4" fill="#E0F2FE" />
  <text x="215" y="83" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#0369A1" text-anchor="middle">STAGE 2</text>
  <text x="190" y="106" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#0F172A">Desk Assessment</text>
  <text x="190" y="125" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• Care Act assessment</text>
  <text x="190" y="140" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• PBS Behaviour plan</text>
  <text x="190" y="155" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• Risk review</text>
  <text x="247" y="185" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#0284C7" text-anchor="middle">Day 1 - 2</text>

  <!-- Step 3 -->
  <rect x="330" y="60" width="135" height="140" rx="8" fill="#FFFFFF" stroke="#6366F1" stroke-width="1.5" />
  <rect x="340" y="70" width="50" height="18" rx="4" fill="#EEF2FF" />
  <text x="365" y="83" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#4338CA" text-anchor="middle">STAGE 3</text>
  <text x="340" y="106" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#0F172A">F2F Clinical Visit</text>
  <text x="340" y="125" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• RM visits resident</text>
  <text x="340" y="140" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• Sensory profile</text>
  <text x="340" y="155" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• Family consultation</text>
  <text x="397" y="185" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#6366F1" text-anchor="middle">Day 3 - 5</text>

  <!-- Step 4 -->
  <rect x="480" y="60" width="135" height="140" rx="8" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="1.5" />
  <rect x="490" y="70" width="50" height="18" rx="4" fill="#F5F3FF" />
  <text x="515" y="83" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#6D28D9" text-anchor="middle">STAGE 4</text>
  <text x="490" y="106" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#0F172A">Peer Matching</text>
  <text x="490" y="125" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• Compatibility matrix</text>
  <text x="490" y="140" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• 78 vs 80 house fit</text>
  <text x="490" y="155" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• MDT Signoff</text>
  <text x="547" y="185" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#8B5CF6" text-anchor="middle">Zero Friction</text>

  <!-- Step 5 -->
  <rect x="630" y="60" width="135" height="140" rx="8" fill="#FFFFFF" stroke="#F59E0B" stroke-width="1.5" />
  <rect x="640" y="70" width="50" height="18" rx="4" fill="#FEF3C7" />
  <text x="665" y="83" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#B45309" text-anchor="middle">STAGE 5</text>
  <text x="640" y="106" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#0F172A">Transition Visits</text>
  <text x="640" y="125" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• 1hr afternoon tea</text>
  <text x="640" y="140" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• Half-day sensory visit</text>
  <text x="640" y="155" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">• 1 overnight stay</text>
  <text x="697" y="185" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#D97706" text-anchor="middle">Week 1 - 2</text>

  <!-- Step 6 -->
  <rect x="780" y="60" width="150" height="140" rx="8" fill="#FFFFFF" stroke="#10B981" stroke-width="2" />
  <rect x="790" y="70" width="50" height="18" rx="4" fill="#D1FAE5" />
  <text x="815" y="83" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#047857" text-anchor="middle">STAGE 6</text>
  <text x="790" y="106" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#065F46">Admission &amp; Tenancy</text>
  <text x="790" y="125" font-family="-apple-system, sans-serif" font-size="9.5" fill="#047857">• AST / Tenancy start</text>
  <text x="790" y="140" font-family="-apple-system, sans-serif" font-size="9.5" fill="#047857">• Care package begins</text>
  <text x="790" y="155" font-family="-apple-system, sans-serif" font-size="9.5" fill="#047857">• Council billing active</text>
  <text x="855" y="185" font-family="-apple-system, sans-serif" font-size="9" font-weight="800" fill="#10B981" text-anchor="middle">100% Retained</text>

  <!-- Bottom Pathway Summary -->
  <rect x="30" y="215" width="900" height="32" rx="6" fill="#F1F5F9" />
  <text x="480" y="235" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#334155" text-anchor="middle">
    CLINICAL SEPARATION: Supported Living Tenancy (PropCo housing benefit £350/wk) is legally separate from OpCo Personal Care Contract.
  </text>
</svg>"""

with open('portal/assets/diagrams/diagram_intake_pathway.svg', 'w', encoding='utf-8') as f:
    f.write(svg_intake)
print("Generated diagram_intake_pathway.svg")
