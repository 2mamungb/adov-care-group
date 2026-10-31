def generate_blueprint_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 720" width="100%" height="auto" class="blueprint-svg" style="max-width:100%; height:auto; display:block; background:#0B192C; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Blueprint Grid Pattern -->
    <pattern id="bpGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1E3E62" stroke-width="0.8" opacity="0.45" />
      <path d="M 200 0 L 0 0 0 200" fill="none" stroke="#2563EB" stroke-width="1.2" opacity="0.3" />
    </pattern>
    <!-- Card Gradients -->
    <linearGradient id="bpWall78" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="bpWall80" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#065F46" />
      <stop offset="100%" stop-color="#022C22" />
    </linearGradient>
    <linearGradient id="bpWall82" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155" />
      <stop offset="100%" stop-color="#1E293B" />
    </linearGradient>
    <linearGradient id="bpGarden" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#064E3B" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#022C22" stop-opacity="0.95" />
    </linearGradient>
    <filter id="bpGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5" />
    </filter>
  </defs>

  <!-- Background with Grid -->
  <rect width="1100" height="720" rx="12" fill="#0A1628" />
  <rect width="1100" height="720" fill="url(#bpGrid)" />

  <!-- Outer Architectural Border -->
  <rect x="18" y="18" width="1064" height="684" rx="8" fill="none" stroke="#38BDF8" stroke-width="1.5" opacity="0.6" />
  <rect x="24" y="24" width="1052" height="672" rx="6" fill="none" stroke="#1E40AF" stroke-width="0.8" opacity="0.4" />

  <!-- BLUEPRINT TITLE BLOCK (Top Header) -->
  <rect x="36" y="32" width="1028" height="52" rx="6" fill="#0F172A" stroke="#38BDF8" stroke-width="1.2" />
  <text x="56" y="55" fill="#38BDF8" font-size="13" font-weight="800" letter-spacing="1.5">ARCHITECTURAL CAMPUS MASTERPLAN // CLASS C3(b) SPECIALIST SUPPORTED LIVING</text>
  <text x="56" y="73" fill="#F8FAFC" font-size="16" font-weight="700">78 &amp; 80 Marston Gardens, Luton, LU2 7DY // 8-Bed Unified Healthcare Campus</text>
  <rect x="910" y="42" width="140" height="32" rx="4" fill="#0284C7" />
  <text x="980" y="63" fill="#FFFFFF" font-size="13" font-weight="800" text-anchor="middle">SCALE: 1:100 NTS</text>

  <!-- 1. HIGHWAYS / ROAD ACCESS -->
  <rect x="36" y="96" width="1028" height="48" rx="6" fill="#1E293B" stroke="#475569" stroke-width="1" />
  <line x1="36" y1="120" x2="1064" y2="120" stroke="#FCD34D" stroke-width="2" stroke-dasharray="12,12" />
  <text x="550" y="117" fill="#F8FAFC" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="2">MARSTON GARDENS (RESIDENTIAL CUL-DE-SAC // HIGHWAYS COMPLIANT)</text>
  <text x="550" y="135" fill="#94A3B8" font-size="12" font-weight="600" text-anchor="middle">Luton Local Plan Policy LLP31 &amp; LLP32 Approved Access Route</text>

  <!-- 2. FLANK PARKING DRIVEWAYS -->
  <!-- Left Flank Parking: 80 Marston Gardens (4 Dedicated Spaces) -->
  <g filter="url(#bpGlow)">
    <rect x="36" y="156" width="140" height="180" rx="8" fill="#0F172A" stroke="#10B981" stroke-width="1.8" />
    <rect x="44" y="166" width="124" height="26" rx="4" fill="#065F46" />
    <text x="106" y="184" fill="#6EE7B7" font-size="13" font-weight="800" text-anchor="middle">4 CAR SPACES</text>
    <!-- Parking Bays -->
    <rect x="46" y="200" width="120" height="28" rx="3" fill="#1E293B" stroke="#334155" />
    <text x="106" y="219" fill="#E2E8F0" font-size="12" font-weight="700" text-anchor="middle">Bay 1 (Staff 80)</text>
    <rect x="46" y="232" width="120" height="28" rx="3" fill="#1E293B" stroke="#334155" />
    <text x="106" y="251" fill="#E2E8F0" font-size="12" font-weight="700" text-anchor="middle">Bay 2 (MDT/Doctor)</text>
    <rect x="46" y="264" width="120" height="28" rx="3" fill="#1E293B" stroke="#334155" />
    <text x="106" y="283" fill="#E2E8F0" font-size="12" font-weight="700" text-anchor="middle">Bay 3 (Visitor/SW)</text>
    <rect x="46" y="296" width="120" height="28" rx="3" fill="#1E293B" stroke="#334155" />
    <text x="106" y="315" fill="#6EE7B7" font-size="12" font-weight="700" text-anchor="middle">Bay 4 (Accessible EV)</text>
    <text x="106" y="331" fill="#94A3B8" font-size="10.5" font-weight="600" text-anchor="middle">Outer Flank Driveway</text>
  </g>

  <!-- Right Flank Parking: 78 Marston Gardens (4 Dedicated Spaces) -->
  <g filter="url(#bpGlow)">
    <rect x="924" y="156" width="140" height="180" rx="8" fill="#0F172A" stroke="#38BDF8" stroke-width="1.8" />
    <rect x="932" y="166" width="124" height="26" rx="4" fill="#1E3A8A" />
    <text x="994" y="184" fill="#93C5FD" font-size="13" font-weight="800" text-anchor="middle">4 CAR SPACES</text>
    <!-- Parking Bays -->
    <rect x="934" y="200" width="120" height="28" rx="3" fill="#1E293B" stroke="#334155" />
    <text x="994" y="219" fill="#E2E8F0" font-size="12" font-weight="700" text-anchor="middle">Bay 5 (Registered Mgr)</text>
    <rect x="934" y="232" width="120" height="28" rx="3" fill="#1E293B" stroke="#334155" />
    <text x="994" y="251" fill="#E2E8F0" font-size="12" font-weight="700" text-anchor="middle">Bay 6 (Staff 78)</text>
    <rect x="934" y="264" width="120" height="28" rx="3" fill="#1E293B" stroke="#334155" />
    <text x="994" y="283" fill="#E2E8F0" font-size="12" font-weight="700" text-anchor="middle">Bay 7 (Support Worker)</text>
    <rect x="934" y="296" width="120" height="28" rx="3" fill="#1E293B" stroke="#334155" />
    <text x="994" y="315" fill="#93C5FD" font-size="12" font-weight="700" text-anchor="middle">Bay 8 (Accessible EV)</text>
    <text x="994" y="331" fill="#94A3B8" font-size="10.5" font-weight="600" text-anchor="middle">Outer Flank Driveway</text>
  </g>

  <!-- 3. CAMPUS RESIDENTIAL PROPERTIES -->
  <!-- PROPERTY 80 MARSTON GARDENS (3 Beds + Calm Hub + Staff Office) -->
  <g filter="url(#bpGlow)">
    <rect x="194" y="156" width="340" height="220" rx="10" fill="url(#bpWall80)" stroke="#10B981" stroke-width="2.5" />
    <!-- Property Title Badge -->
    <rect x="206" y="168" width="160" height="28" rx="5" fill="#064E3B" stroke="#34D399" stroke-width="1.2" />
    <text x="286" y="187" fill="#A7F3D0" font-size="13.5" font-weight="800" text-anchor="middle">80 MARSTON GDNS</text>
    <rect x="374" y="168" width="148" height="28" rx="5" fill="#047857" />
    <text x="448" y="187" fill="#FFFFFF" font-size="13" font-weight="800" text-anchor="middle">3 RESIDENT SUITES</text>

    <!-- Rooms Layout Grid -->
    <!-- Room 1: Resident Bedrooms -->
    <rect x="206" y="206" width="154" height="64" rx="6" fill="#064E3B" stroke="#059669" stroke-width="1.2" />
    <text x="283" y="226" fill="#F0FDF4" font-size="13" font-weight="700" text-anchor="middle">3 Large Bedrooms</text>
    <text x="283" y="244" fill="#A7F3D0" font-size="11.5" text-anchor="middle">12.4m² – 14.8m² usable</text>
    <text x="283" y="260" fill="#FCD34D" font-size="11" font-weight="700" text-anchor="middle">FD30S Fire Doors • Cat L1</text>

    <!-- Room 2: Accessible Wet Room -->
    <rect x="368" y="206" width="154" height="64" rx="6" fill="#064E3B" stroke="#059669" stroke-width="1.2" />
    <text x="445" y="226" fill="#F0FDF4" font-size="13" font-weight="700" text-anchor="middle">Accessible Wet Room</text>
    <text x="445" y="244" fill="#6EE7B7" font-size="11.5" text-anchor="middle">TMV3 Anti-Scald (41°C)</text>
    <text x="445" y="260" fill="#93C5FD" font-size="11" font-weight="700" text-anchor="middle">+ Separate Visitor WC</text>

    <!-- Room 3: Sensory Calm Hub -->
    <rect x="206" y="278" width="154" height="88" rx="6" fill="#047857" stroke="#34D399" stroke-width="1.2" />
    <text x="283" y="299" fill="#FFFFFF" font-size="13" font-weight="800" text-anchor="middle">Calm Sensory Lounge</text>
    <text x="283" y="318" fill="#D1FAE5" font-size="11.5" text-anchor="middle">Dimmable LED Lighting</text>
    <text x="283" y="335" fill="#D1FAE5" font-size="11.5" text-anchor="middle">Acoustic Damping Wall Panels</text>
    <text x="283" y="353" fill="#FCD34D" font-size="11" font-weight="700" text-anchor="middle">De-escalation Zone</text>

    <!-- Room 4: Staff Office & Sleep-In -->
    <rect x="368" y="278" width="154" height="88" rx="6" fill="#047857" stroke="#34D399" stroke-width="1.2" />
    <text x="445" y="299" fill="#FFFFFF" font-size="13" font-weight="800" text-anchor="middle">Staff Office &amp; Sleep-In</text>
    <text x="445" y="318" fill="#FDE68A" font-size="11.5" font-weight="700" text-anchor="middle">BS 2881 Meds CD Safe</text>
    <text x="445" y="335" fill="#D1FAE5" font-size="11.5" text-anchor="middle">Nourish e-MAR Terminal</text>
    <text x="445" y="353" fill="#93C5FD" font-size="11" font-weight="700" text-anchor="middle">Waking Night Base</text>
  </g>

  <!-- PARTY WALL INDICATOR (Between 78 & 80) -->
  <line x1="550" y1="156" x2="550" y2="376" stroke="#F59E0B" stroke-width="4" stroke-dasharray="8,6" />
  <g filter="url(#bpGlow)">
    <circle cx="550" cy="266" r="22" fill="#D97706" stroke="#FEF3C7" stroke-width="2" />
    <text x="550" y="262" fill="#FFFFFF" font-size="11" font-weight="900" text-anchor="middle">PARTY</text>
    <text x="550" y="276" fill="#FFFFFF" font-size="11" font-weight="900" text-anchor="middle">WALL</text>
    <rect x="506" y="296" width="88" height="22" rx="4" fill="#78350F" />
    <text x="550" y="311" fill="#FDE68A" font-size="10" font-weight="700" text-anchor="middle">DOC E SOUND</text>
  </g>

  <!-- PROPERTY 78 MARSTON GARDENS (5 Beds + Commercial Kitchen + Dining Hall) -->
  <g filter="url(#bpGlow)">
    <rect x="566" y="156" width="340" height="220" rx="10" fill="url(#bpWall78)" stroke="#38BDF8" stroke-width="2.5" />
    <!-- Property Title Badge -->
    <rect x="578" y="168" width="160" height="28" rx="5" fill="#1E3A8A" stroke="#60A5FA" stroke-width="1.2" />
    <text x="658" y="187" fill="#BFDBFE" font-size="13.5" font-weight="800" text-anchor="middle">78 MARSTON GDNS</text>
    <rect x="746" y="168" width="148" height="28" rx="5" fill="#2563EB" />
    <text x="820" y="187" fill="#FFFFFF" font-size="13" font-weight="800" text-anchor="middle">5 RESIDENT SUITES</text>

    <!-- Rooms Layout Grid -->
    <!-- Room 1: 5 Specialist Bedrooms -->
    <rect x="578" y="206" width="154" height="64" rx="6" fill="#1E3A8A" stroke="#3B82F6" stroke-width="1.2" />
    <text x="655" y="226" fill="#EFF6FF" font-size="13" font-weight="700" text-anchor="middle">5 Bedrooms (1 En-Suite)</text>
    <text x="655" y="244" fill="#93C5FD" font-size="11.5" text-anchor="middle">13.2m² – 16.5m² usable</text>
    <text x="655" y="260" fill="#FCD34D" font-size="11" font-weight="700" text-anchor="middle">FD30S Fire Doors • Cat L1</text>

    <!-- Room 2: Assisted Wet Room -->
    <rect x="740" y="206" width="154" height="64" rx="6" fill="#1E3A8A" stroke="#3B82F6" stroke-width="1.2" />
    <text x="817" y="226" fill="#EFF6FF" font-size="13" font-weight="700" text-anchor="middle">Assisted Wet Room</text>
    <text x="817" y="244" fill="#93C5FD" font-size="11.5" text-anchor="middle">TMV3 Anti-Scald (41°C)</text>
    <text x="817" y="260" fill="#FCD34D" font-size="11" font-weight="700" text-anchor="middle">+ Separate Visitor WC</text>

    <!-- Room 3: Commercial Kitchen -->
    <rect x="578" y="278" width="154" height="88" rx="6" fill="#1D4ED8" stroke="#60A5FA" stroke-width="1.2" />
    <text x="655" y="299" fill="#FFFFFF" font-size="13" font-weight="800" text-anchor="middle">Commercial Kitchen</text>
    <text x="655" y="318" fill="#FDE68A" font-size="11.5" font-weight="700" text-anchor="middle">Food Hygiene Rating 5</text>
    <text x="655" y="335" fill="#BFDBFE" font-size="11.5" text-anchor="middle">Stainless Steel Workstations</text>
    <text x="655" y="353" fill="#6EE7B7" font-size="11" font-weight="700" text-anchor="middle">HTM 01-04 Laundry Flow</text>

    <!-- Room 4: Communal Dining & Activity Hall -->
    <rect x="740" y="278" width="154" height="88" rx="6" fill="#1D4ED8" stroke="#60A5FA" stroke-width="1.2" />
    <text x="817" y="299" fill="#FFFFFF" font-size="13" font-weight="800" text-anchor="middle">Communal Dining Hall</text>
    <text x="817" y="318" fill="#BFDBFE" font-size="11.5" text-anchor="middle">Resident Social &amp; Dining Hub</text>
    <text x="817" y="335" fill="#BFDBFE" font-size="11.5" text-anchor="middle">Bi-Fold Doors to Garden</text>
    <text x="817" y="353" fill="#FDE68A" font-size="11" font-weight="700" text-anchor="middle">Direct Sensory Access</text>
  </g>

  <!-- 4. 100FT ENCLOSED SENSORY REAR GARDENS -->
  <g filter="url(#bpGlow)">
    <rect x="36" y="394" width="1028" height="190" rx="10" fill="url(#bpGarden)" stroke="#10B981" stroke-width="2" stroke-dasharray="8,4" />
    <!-- Garden Title Banner -->
    <rect x="56" y="408" width="988" height="34" rx="6" fill="#065F46" stroke="#34D399" stroke-width="1.2" />
    <text x="550" y="430" fill="#6EE7B7" font-size="14.5" font-weight="800" text-anchor="middle" letter-spacing="1.5">100FT PRIVATE ENCLOSED SENSORY REAR GARDENS (SHARED CAMPUS THERAPEUTIC ZONE)</text>

    <!-- Garden Feature Zones -->
    <!-- Feature 1: Therapeutic Pavilion -->
    <rect x="66" y="454" width="220" height="114" rx="8" fill="#047857" stroke="#34D399" stroke-width="1.2" />
    <text x="176" y="478" fill="#FFFFFF" font-size="13.5" font-weight="800" text-anchor="middle">Therapeutic Pavilion</text>
    <text x="176" y="498" fill="#D1FAE5" font-size="12" text-anchor="middle">Covered Outdoor Seating</text>
    <text x="176" y="516" fill="#D1FAE5" font-size="12" text-anchor="middle">All-Weather Heated Area</text>
    <text x="176" y="534" fill="#D1FAE5" font-size="12" text-anchor="middle">Quiet Sensory Retreat</text>
    <text x="176" y="552" fill="#FCD34D" font-size="11" font-weight="700" text-anchor="middle">CQC 'Right Support' Aligned</text>

    <!-- Feature 2: Sensory Raised Beds & Herb Pathway -->
    <rect x="306" y="454" width="230" height="114" rx="8" fill="#047857" stroke="#34D399" stroke-width="1.2" />
    <text x="421" y="478" fill="#FFFFFF" font-size="13.5" font-weight="800" text-anchor="middle">Sensory Herb &amp; Planters</text>
    <text x="421" y="498" fill="#D1FAE5" font-size="12" text-anchor="middle">Raised Wheelchair Planters</text>
    <text x="421" y="516" fill="#D1FAE5" font-size="12" text-anchor="middle">Lavender, Mint, Rosemary</text>
    <text x="421" y="534" fill="#D1FAE5" font-size="12" text-anchor="middle">Non-Slip Rubberized Pathway</text>
    <text x="421" y="552" fill="#FCD34D" font-size="11" font-weight="700" text-anchor="middle">Horticultural Therapy</text>

    <!-- Feature 3: Tactile Water Feature & Acoustic Damping -->
    <rect x="556" y="454" width="230" height="114" rx="8" fill="#047857" stroke="#34D399" stroke-width="1.2" />
    <text x="671" y="478" fill="#FFFFFF" font-size="13.5" font-weight="800" text-anchor="middle">Tactile Acoustic Feature</text>
    <text x="671" y="498" fill="#D1FAE5" font-size="12" text-anchor="middle">Self-Contained Bubble Fountain</text>
    <text x="671" y="516" fill="#D1FAE5" font-size="12" text-anchor="middle">Calming Audio White Noise</text>
    <text x="671" y="534" fill="#D1FAE5" font-size="12" text-anchor="middle">Smooth River Pebble Textures</text>
    <text x="671" y="552" fill="#FCD34D" font-size="11" font-weight="700" text-anchor="middle">Sensory Modulation</text>

    <!-- Feature 4: De-escalation & Perimeter Security -->
    <rect x="806" y="454" width="238" height="114" rx="8" fill="#047857" stroke="#34D399" stroke-width="1.2" />
    <text x="925" y="478" fill="#FFFFFF" font-size="13.5" font-weight="800" text-anchor="middle">Safe Security Perimeter</text>
    <text x="925" y="498" fill="#D1FAE5" font-size="12" text-anchor="middle">6ft Acoustic Security Fencing</text>
    <text x="925" y="516" fill="#D1FAE5" font-size="12" text-anchor="middle">Anti-Climb Softened Boundary</text>
    <text x="925" y="534" fill="#D1FAE5" font-size="12" text-anchor="middle">Safe De-escalation Zones</text>
    <text x="925" y="552" fill="#FCD34D" font-size="11" font-weight="700" text-anchor="middle">100% Secure Enclosure</text>
  </g>

  <!-- 5. STATUTORY COMPLIANCE & LEGAL BOTTOM LEGEND -->
  <rect x="36" y="600" width="1028" height="90" rx="8" fill="#0F172A" stroke="#38BDF8" stroke-width="1.2" />
  
  <!-- Left Cell: Planning & Statutory -->
  <text x="56" y="624" fill="#38BDF8" font-size="12" font-weight="800" letter-spacing="1">TOWN PLANNING &amp; STATUTORY IMMUNITY:</text>
  <text x="56" y="643" fill="#F1F5F9" font-size="12.5" font-weight="600">• S.192 CLPUD Permitted Development Class C3(b) (Up to 6 residents living together receiving care)</text>
  <text x="56" y="662" fill="#94A3B8" font-size="12">• North Devon DC v FSS [2004] Precedent: Non-resident carers establish single household C3(b) use</text>
  <text x="56" y="680" fill="#FCD34D" font-size="11.5" font-weight="700">• 82 Marston Gardens: Director Private Residence (let on AST, eliminates BIK under ITEPA 2003 s.105/106)</text>

  <!-- Right Cell: Health & Safety / CQC -->
  <text x="620" y="624" fill="#34D399" font-size="12" font-weight="800" letter-spacing="1">FIRE SAFETY &amp; CLINICAL SPECIFICATIONS:</text>
  <text x="620" y="643" fill="#F1F5F9" font-size="12.5" font-weight="600">• BS 5839 Category L1 Addressable Automatic Fire Detection System</text>
  <text x="620" y="662" fill="#94A3B8" font-size="12">• FD30S Fire &amp; Smoke Resisting Doors with Dorgard magnetic hold-open</text>
  <text x="620" y="680" fill="#6EE7B7" font-size="11.5" font-weight="700">• BS 5266 3-Hour Maintained Emergency Lighting &amp; Document M Accessible Access</text>
</svg>'''

if __name__ == '__main__':
    svg_code = generate_blueprint_svg()
    print('Generated SVG size:', len(svg_code), 'bytes')
    with open('portal/assets/diagrams/diagram_campus_masterplan.svg', 'w', encoding='utf-8') as f:
        f.write(svg_code)
    print('Wrote portal/assets/diagrams/diagram_campus_masterplan.svg successfully!')
