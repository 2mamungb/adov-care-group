#!/usr/bin/env python3
"""
ADOV Care Group — Landscape Journal Builder: Part 4 (Government & Prospectus)
Exhaustive PhD-level commissioning, investment, architectural, and M&A monographs for boardroom planning.

Documents:
15. ADOV_Care_Group_Government_Project_Report (PDF & DOCX)
16. ADOV_Care_Group_Private_Project_Prospectus (PDF & DOCX)
17. ADOV_Care_Group_Photographic_Campus_Masterplan (PDF & DOCX)
18. ADOV_Care_Group_Private_Investment_Prospectus (PDF & DOCX)
"""

import os
import sys
from landscape_journal_engine import LandscapeDocument

# ==============================================================================
# DOC 15: GOVERNMENT PROJECT REPORT
# ==============================================================================
def build_government_project_report():
    doc = LandscapeDocument(
        title="MASTER GOVERNMENT & PUBLIC SECTOR COMMISSIONING REPORT",
        doc_ref="ACG-LUTON-2026-GOV",
        category="PUBLIC SECTOR COMMISSIONING REPORT",
        subtitle="Transforming Care Alignment, Value for Money Analysis, Social Value & Local Repatriation Strategy for Luton Social Care & BLMK ICB"
    )

    doc.set_meta([
        ("Commissioning Authority", "Luton Borough Council Adult Social Care & Procurement Directorate"),
        ("NHS Integrated Care Board", "Bedfordshire, Luton and Milton Keynes Integrated Care Board (BLMK ICB)"),
        ("Applicant Provider", "ADOV Care Group LIMITED (Company No. 14289650)"),
        ("Campus Location", "78 & 80 Marston Gardens, Luton, LU2 7DY (8 Specialist Supported Living Beds)"),
        ("National Policy Driver", "NHS Transforming Care Agenda & Building the Right Support Framework"),
        ("Local Authority Savings", "Saving £120,000–£180,000 per resident annually vs. Out-of-Area Inpatient Placements"),
        ("Strategic Advisory Lead", "Public Sector Healthcare Advisory // Project Planned by AbdullahMamun.com"),
        ("Publication Date", "October 2026 // Public Sector Edition")
    ])

    doc.set_kpis([
        ("£1.2M / Yr", "Council Savings", "Repatriating 8 out-of-area beds"),
        ("£2,350 / Wk", "All-Inclusive Fee", "Core care + 1:1 + exempt rent"),
        ("35 FTE", "Local Employment", "Direct care & management jobs"),
        ("100% Repatriation", "Local Focus", "Bringing Luton citizens home"),
        ("PBS Certified", "Quality Rating", "Positive Behaviour Support standard")
    ])

    # Section 1.0
    doc.add_heading_1("1.0 PUBLIC SECTOR COMMISSIONING MANDATE & LOCAL REPATRIATION IN LUTON")
    doc.add_paragraph(
        "Luton Borough Council Adult Social Care and the Bedfordshire, Luton and Milton Keynes Integrated Care Board (BLMK ICB) "
        "face acute commissioning pressures for adults diagnosed with autism spectrum conditions and severe learning disabilities. "
        "Due to a historical lack of high-acuity local supported accommodation, dozens of Luton citizens are currently placed in high-cost, "
        "out-of-borough independent hospitals, assessment and treatment units (ATUs), or external residential care homes at unsustainable "
        "rates ranging from £4,500 to £7,500 per week. ADOV Care Group establishes an 8-bed specialist campus at 78 and 80 Marston Gardens, "
        "Luton, delivering an institutional-quality, localized repatriation solution that returns vulnerable citizens to their home borough, "
        "reconnects them with their families, and eliminates massive out-of-area commissioning deficits."
    )

    doc.add_callout(
        "NATIONAL STATUTORY ALIGNMENT: THE TRANSFORMING CARE AGENDA",
        "The ADOV Care Group campus directly operationalizes the government's statutory mandate under 'Building the Right Support' and the "
        "NHS Long Term Plan: ending inappropriate institutional inpatient admissions for people with learning disabilities and autism by developing "
        "high-quality, person-centred community housing. Supported living under Positive Behaviour Support (PBS) represents the definitive "
        "gold-standard care model endorsed by the Department of Health and Social Care and the Care Quality Commission."
    )

    # Section 2.0
    doc.add_heading_1("2.0 VALUE FOR MONEY (VfM) & PUBLIC SECTOR COST SAVINGS")
    doc.add_paragraph(
        "A rigorous comparative benchmarking analysis demonstrates that commissioning 8 beds with ADOV Care Group generates "
        "over £1.31M in annual cash savings for Luton Borough Council and the NHS compared to private specialist hospitals, "
        "and over £603k in savings compared to out-of-county Class C2 care homes."
    )

    doc.add_table(
        title="Table 15.1: Comparative Public Sector Value for Money Cost Analysis",
        headers=["Placement Model", "Placement Location", "Weekly Cost / Bed", "Annual Cost / Resident", "8-Person Campus Total", "Public Sector Savings"],
        rows=[
            ["Specialist Out-of-Area Inpatient Hospital", "Private Hospital (Out-of-County)", "£5,500.00", "£286,000.00", "£2,288,000.00", "+£1,310,400 (Excess Deficit)"],
            ["External Residential Care Home (C2)", "Independent Care Home (Out-of-County)", "£3,800.00", "£197,600.00", "£1,580,800.00", "+£603,200 (Excess Deficit)"],
            ["ADOV Care Group Supported Living", "78 & 80 Marston Gardens, Luton", "£2,350.00", "£122,200.00", "£977,600.00", "BASELINE VALUE STANDARD"],
            ["NET LOCAL AUTHORITY CASH SAVINGS", "Public Sector Cost Reduction", "-£3,150.00 / wk", "-£163,800.00 / yr", "-£1,310,400.00 / yr", "57.3% BUDGET SAVINGS"]
        ],
        col_pcts=[24, 22, 12, 14, 14, 14]
    )

    # Section 3.0
    doc.add_heading_1("3.0 SOCIAL VALUE, LOCAL EMPLOYMENT & ECONOMIC REINVESTMENT")
    doc.add_paragraph(
        "In accordance with the Public Services (Social Value) Act 2012, ADOV Care Group delivers measurable, enduring economic "
        "and social benefits to the Borough of Luton:"
    )

    doc.add_key_value_grid(
        title="Social Value & Community Impact Commitments",
        items=[
            ("Real Living Wage Employment", "Creation of 25–30 permanent care positions (Support Workers, Team Leaders, Maintenance) recruited locally from LU1, LU2, and LU3 at or above the Real Living Wage."),
            ("Family Cohesion & Wellbeing", "Repatriating Luton citizens allows weekly family visits and active involvement in care planning, ending the severe emotional distress of 100+ mile out-of-county travels."),
            ("Local Supply Chain Reinvestment", "Provisions, maintenance, sensory equipment, and specialist trades are procured directly from independent Luton and Bedfordshire commercial suppliers."),
            ("Emergency Services Relief", "Specialist PBS de-escalation environments reduce 999 emergency call-outs, hospital A&E crisis attendances, and mental health crisis team interventions by over 80%.")
        ],
        num_cols=2
    )

    # Section 4.0
    doc.add_heading_1("4.0 COMMISSIONING PROCUREMENT PATHWAYS & CONTRACTING")
    doc.add_paragraph(
        "ADOV Care Group contracts through established statutory procurement vehicles: (1) Luton Borough Council Supported Living "
        "Dynamic Purchasing System (DPS AT1115 via ProContract); (2) NHS BLMK ICB Continuing Healthcare (CHC) Framework; and (3) Section 117 "
        "Mental Health Act joint funding agreements, providing transparent, auditable individual placement agreements (IPAs)."
    )

    doc.build_pdf("ADOV_Care_Group_Government_Project_Report.pdf")
    doc.build_docx("ADOV_Care_Group_Government_Project_Report.docx")
    print("✓ Completed Government Project Report (PDF & DOCX).")


# ==============================================================================
# DOC 16: PRIVATE PROJECT PROSPECTUS
# ==============================================================================
def build_private_project_prospectus():
    doc = LandscapeDocument(
        title="PRIVATE PROJECT & COMMERCIAL INVESTMENT PROSPECTUS",
        doc_ref="ACG-LUTON-2026-PROSPECTUS",
        category="INVESTMENT PROSPECTUS & MASTERPLAN",
        subtitle="Commercial Proposition, Freehold Asset Backing, Corporate Yields & Executive Exit Roadmap"
    )

    doc.set_meta([
        ("Project Sponsor", "FAIRYTALES GROUP (Trading Name of Mamun Limited)"),
        ("Asset Holding PropCo", "ADOV LIMITED (Freehold Real Estate Entity)"),
        ("Operating Company", "ADOV Care Group LIMITED (CQC Care Operations)"),
        ("Campus Assets", "78 & 80 Marston Gardens (Care Campus) // 82 Marston Gardens (Executive Residence)"),
        ("Target Investment", "£68,400 Turnkey Working Capital & Refurbishment"),
        ("Annual Net Cash Flow", "£438,392 Consolidated Pre-Tax Cash Flow (+£36,532 / Month)"),
        ("Lead Investment Lead", "Strategic Healthcare Finance // Project Planned by AbdullahMamun.com"),
        ("Distribution Standard", "Private & Confidential // Qualified Investors & Board Directors")
    ])

    doc.set_kpis([
        ("£977,600", "Gross Turnover", "8 beds @ £2,350/wk avg"),
        ("£341,392", "OpCo EBITDA", "35.0% operating margin"),
        ("£97,000", "PropCo Rent", "FRI Commercial Leases"),
        ("£438,392", "Group Cash Flow", "+£36,532 / month liquid buffer"),
        ("<2.5 Months", "Payback Period", "Exceptional capital velocity")
    ])

    # Section 1.0
    doc.add_heading_1("1.0 EXECUTIVE INVESTMENT PROPOSITION & COMMERCIAL SUMMARY")
    doc.add_paragraph(
        "ADOV Care Group presents a premier social infrastructure investment opportunity: the commercial conversion and operation "
        "of an 8-bed specialist Supported Living campus across 78 and 80 Marston Gardens, Luton, coupled with the integration of 82 Marston Gardens "
        "as the private executive residence for the Director. The business model generates £977,600 in annual turnover funded by statutory local authority "
        "and NHS budgets under the Care Act 2014, delivering an operating EBITDA of £341,392 (35.0% margin) in OpCo and £97,000 in net rental income "
        "in PropCo, yielding a total consolidated group cash flow of £438,392 annually. With an upfront turnkey capital expenditure of just £68,400, "
        "the project achieves full capital payback in under 2.5 months and generates an annual Return on Capital Employed (ROCE) exceeding 500%."
    )

    # Section 2.0
    doc.add_heading_1("2.0 FREEHOLD ASSET SECURITY & DUAL-EXIT DEFENSIVENESS")
    doc.add_paragraph(
        "Unlike standard healthcare operating businesses that rent commercial premises, ADOV Care Group is 100% asset-backed by prime "
        "unencumbered freehold real estate held in ADOV LIMITED. The properties command an unencumbered residential bricks-and-mortar value "
        "exceeding £1.50M. As a commissioned care campus generating £97,000/yr in passing FRI commercial rent, the real estate achieves a commercial "
        "investment valuation of £1.38M (at a 7.0% capitalization rate), giving lenders and investors complete capital preservation."
    )

    doc.add_table(
        title="Table 16.1: 5-Year Consolidated Financial Forecast & Capital Accumulation Schedule",
        headers=["Financial Metric", "Year 1 (Commissioning)", "Year 2 (Steady State)", "Year 3 (Inflation +3%)", "Year 4 (Expansion)", "Year 5 (Terminal Value)"],
        rows=[
            ["Gross Care Turnover", "£977,600.00", "£1,006,928.00", "£1,037,136.00", "£1,068,250.00", "£1,100,297.00"],
            ["Care Operating Costs", "£636,208.00", "£655,294.00", "£674,953.00", "£695,202.00", "£716,058.00"],
            ["OpCo Operating EBITDA", "£341,392.00", "£351,634.00", "£362,183.00", "£373,048.00", "£384,239.00"],
            ["PropCo FRI Rental Income", "£97,000.00", "£97,000.00", "£99,910.00", "£102,907.00", "£105,994.00"],
            ["Consolidated Pre-Tax Cash Flow", "£438,392.00", "£448,634.00", "£462,093.00", "£475,955.00", "£490,233.00"],
            ["Cumulative Net Cash Generated", "£438,392.00", "£887,026.00", "£1,349,119.00", "£1,825,074.00", "£2,315,307.00"]
        ],
        col_pcts=[24, 15, 15, 15, 15, 16]
    )

    # Section 3.0
    doc.add_heading_1("3.0 CAPITAL EFFICIENCY, TAX ARCHITECTURE & DIRECTOR HOME INTEGRATION")
    doc.add_callout(
        "THE TRIPLE-WIN EXECUTIVE ARCHITECTURE",
        "1. Executive Quality of Life: Living at 82 Marston Gardens provides an executive family haven with secluded private gardens and 4 bedrooms, "
        "allowing 30-second on-site management presence without living inside the care facility.\n"
        "2. Total Tax Neutrality: Open-market AST agreement between ADOV Limited and the Director at £1,500/mo completely eliminates HMRC Benefit in Kind "
        "(s.105/106 ITEPA 2003) to NIL.\n"
        "3. Corporate Shielding: Freehold assets in PropCo are completely insulated from OpCo clinical risks, and OpCo commercial rents are 100% tax-deductible."
    )

    doc.build_pdf("ADOV_Care_Group_Private_Project_Prospectus.pdf")
    doc.build_docx("ADOV_Care_Group_Private_Project_Prospectus.docx")
    print("✓ Completed Private Project Prospectus (PDF & DOCX).")


# ==============================================================================
# DOC 17: PHOTOGRAPHIC CAMPUS MASTERPLAN
# ==============================================================================
def build_photographic_campus_masterplan():
    doc = LandscapeDocument(
        title="PHOTOGRAPHIC & ARCHITECTURAL CAMPUS MASTERPLAN",
        doc_ref="ACG-LUTON-2026-PHOTO-PLAN",
        category="ARCHITECTURAL & PROPERTY DOSSIER",
        subtitle="Room-by-Room Spatial Layouts, Sanitary Engineering, Environmental Specifications & Turnkey Works Schedule"
    )

    doc.set_meta([
        ("Campus Subject", "78, 80 & 82 Marston Gardens, Luton, Bedfordshire, LU2 7DY"),
        ("Freehold Landlord", "ADOV LIMITED (Freehold Real Estate Co)"),
        ("Operating Provider", "ADOV Care Group LIMITED (Specialist Supported Living)"),
        ("Lead Surveyor", "Healthcare Architectural Surveyor // Project Planned by AbdullahMamun.com"),
        ("Total Usable Area", "Over 3,800 sq ft across 3 residential properties"),
        ("Outdoor Grounds", "2 x 100ft private landscaped rear gardens plus executive grounds at 82"),
        ("Parking Topology", "8 dedicated off-street driveway parking bays + 2 lockable garages"),
        ("Survey Date", "October 2026 // Definitive Architectural Edition")
    ])

    doc.set_kpis([
        ("3,800+ sq ft", "Campus Footprint", "3 conjoined residential properties"),
        ("8 Beds", "Supported Living", "5 beds in 78 // 3 beds in 80"),
        ("4 Wet Rooms", "Sanitary Assets", "High-grade non-slip wetrooms"),
        ("8 Bays + 2 Garages", "Highways Capacity", "Zero on-street parking"),
        ("100% Compliant", "Building Standards", "Part B, E, M & CQC SAF")
    ])

    # Section 1.0
    doc.add_heading_1("1.0 CAMPUS TOPOLOGY, ELEVATIONS & SITE LAYOUT")
    doc.add_paragraph(
        "78, 80, and 82 Marston Gardens represent an exceptional social care infrastructure cluster. Numbers 78 and 80 form a handsome, "
        "symmetrical pair of conjoined two-storey semi-detached properties, while Number 82 stands immediately adjacent. "
        "The site layout benefits from substantial flanking land, providing two separate wide private driveways capable of accommodating 8 vehicles "
        "off-street, flanked by two brick-built garages. To the rear, both properties open onto magnificent 100-foot secluded gardens backing onto "
        "mature trees, providing a therapeutic, low-arousal outdoor environment perfectly suited to adults with autism spectrum conditions."
    )

    # Section 2.0
    doc.add_heading_1("2.0 ROOM-BY-ROOM ARCHITECTURAL & SANITARY REGISTER")
    doc.add_paragraph(
        "The architectural layout has been comprehensively surveyed to verify spatial dimensions, ceiling clearances, acoustic integrity, "
        "and sanitary compliance with CQC and local authority standards."
    )

    doc.add_table(
        title="Table 17.1: Comprehensive Room-by-Room Spatial & Sanitary Register",
        headers=["Campus Unit", "Specific Room & Purpose", "Floor Area", "Ceiling Ht", "Sanitary Specification", "Acoustic & Fire Spec"],
        rows=[
            ["No. 78 Marston", "Bed 1 (Ground Floor - Primary)", "14.2 m²", "2.45 m", "Private ensuite wetroom with level drain & TMV3 shower", "Soundbloc 48dB; FD30S fire door"],
            ["No. 78 Marston", "Bed 2 (First Floor - Front)", "15.0 m²", "2.40 m", "New private ensuite wetroom (WP-02 CapEx addition)", "Soundbloc 48dB; FD30S fire door"],
            ["No. 78 Marston", "Bed 3 (First Floor - Rear)", "13.8 m²", "2.40 m", "Direct access to large communal first-floor wetroom", "Soundbloc 46dB; FD30S fire door"],
            ["No. 78 Marston", "Bed 4 (First Floor - Rear)", "12.5 m²", "2.40 m", "Direct access to large communal first-floor wetroom", "Soundbloc 46dB; FD30S fire door"],
            ["No. 78 Marston", "Bed 5 (First Floor - Side)", "12.8 m²", "2.40 m", "Direct access to large communal first-floor wetroom", "Soundbloc 46dB; FD30S fire door"],
            ["No. 78 Marston", "Communal Living & Dining Lounge", "26.5 m²", "2.45 m", "Ground-floor accessible cloakroom WC with low-level basin", "Acoustic ceiling; BS 5839 optical"],
            ["No. 78 Marston", "Domestic Training Kitchen", "14.0 m²", "2.45 m", "Double stainless sink; commercial dishwasher; safety induction", "Heat detector; non-slip vinyl"],
            ["No. 80 Marston", "Bed 1 (Ground Floor - Sensory)", "15.5 m²", "2.45 m", "Direct access to ground-floor accessible wetroom", "Soundbloc 48dB; low-arousal lights"],
            ["No. 80 Marston", "Bed 2 (First Floor - Master)", "16.0 m²", "2.40 m", "Direct access to communal wetroom & separate cloakroom WC", "Soundbloc 48dB; garden view"],
            ["No. 80 Marston", "Bed 3 (First Floor - Front)", "14.5 m²", "2.40 m", "Direct access to communal wetroom & separate cloakroom WC", "Soundbloc 48dB; bay window"],
            ["No. 80 Marston", "Sensory De-escalation Suite", "18.2 m²", "2.45 m", "Adjacent to ground-floor wetroom", "Acoustic padding; fiber-optic sensory"],
            ["No. 80 Marston", "Registered Management Office", "12.0 m²", "2.45 m", "Staff cloakroom WC", "BS 2881 CD safe; secure records hub"],
            ["No. 82 Marston", "Director's Private Residence", "135.0 m²", "2.45 m", "Full family bathroom, ensuite shower, ground cloakroom", "Domestic Class C3 family home"]
        ],
        col_pcts=[14, 26, 10, 10, 22, 18]
    )

    # Section 3.0
    doc.add_heading_1("3.0 SANITARY ENGINEERING & WET ROOM OPTIMIZATION")
    doc.add_callout(
        "TECHNICAL SPECIFICATIONS OF CAMPUS WET ROOMS",
        "All wet rooms across 78 and 80 Marston Gardens are engineered to healthcare-grade durability: (1) Flooring: Altro Aquarius 2mm slip-resistant "
        "heavy-duty vinyl with welded coved skirtings rising 150mm up walls; (2) Drainage: Impey level-access wet floor former with high-flow gulley; "
        "(3) Thermostatic Mixing Valves: TMV3 certified anti-scald blending valves preset to a fail-safe maximum water temperature of 41°C–43°C "
        "in compliance with NHS Model Engineering Specification D08; (4) Grab Rails: Powder-coated high-contrast drop-down and wall-mounted support rails."
    )

    doc.build_pdf("ADOV_Care_Group_Photographic_Campus_Masterplan.pdf")
    doc.build_docx("ADOV_Care_Group_Photographic_Campus_Masterplan.docx")
    print("✓ Completed Photographic Campus Masterplan (PDF & DOCX).")


# ==============================================================================
# DOC 18: PRIVATE INVESTMENT PROSPECTUS
# ==============================================================================
def build_private_investment_prospectus():
    doc = LandscapeDocument(
        title="INSTITUTIONAL PRIVATE EQUITY & M&A INVESTMENT MONOGRAPH",
        doc_ref="ACG-LUTON-2026-PE-MA",
        category="INSTITUTIONAL M&A & CORPORATE FINANCE",
        subtitle="Enterprise Valuation (EV), Debt Capacity, Roll-Up M&A Multiples & Institutional Exit Pathways"
    )

    doc.set_meta([
        ("Target Entity", "ADOV Care Group LIMITED (OpCo) & ADOV LIMITED (PropCo)"),
        ("Holding Entity", "FAIRYTALES GROUP (Trading Name of Mamun Limited)"),
        ("Corporate Finance Lead", "Healthcare M&A & Private Equity Advisory // Project Planned by AbdullahMamun.com"),
        ("Operating EBITDA", "£341,392 OpCo EBITDA (35.0% Margin)"),
        ("Commercial Real Estate Rent", "£97,000 PropCo FRI Rental Income"),
        ("Consolidated Group Cash Flow", "£438,392 Pre-Tax Annual Cash Flow"),
        ("EV Valuation Multiple Range", "6.5x to 8.5x EBITDA (£2.22M to £2.90M OpCo Value)"),
        ("Combined Enterprise & Real Estate", "£3.60M to £4.45M Combined Group Valuation")
    ])

    doc.set_kpis([
        ("£3.6M – £4.4M", "Combined Value", "OpCo EV + PropCo Freeholds"),
        ("6.5x – 8.5x", "EBITDA Multiple", "UK Specialist Social Care M&A"),
        ("4.52x", "DSCR Headroom", "Exceptional debt service capacity"),
        ("£438,392", "Annual Cash Flow", "Consolidated group cash yield"),
        ("Trade Sale / REIT", "Exit Strategy", "High institutional liquidity")
    ])

    # Section 1.0
    doc.add_heading_1("1.0 INSTITUTIONAL HEALTHCARE INVESTMENT THESIS & SECTOR DEFENSIVENESS")
    doc.add_paragraph(
        "Specialist Supported Living for adults with autism spectrum disorders and complex learning disabilities represents one of the most "
        "sought-after asset classes in UK healthcare corporate finance. The sector is characterized by: (1) Extreme Supply/Demand Imbalance: "
        "A severe structural shortfall of specialist community beds across the South East and East of England; (2) Statutory Funding Mandate: "
        "Revenues are funded by local authorities and the NHS under statutory duties (Care Act 2014, Autism Act 2009), providing 100% counterparty "
        "solvency immune to macroeconomic recessions; (3) Extraordinary Length of Stay: Specialist supported living placements average 8 to 15 years, "
        "eliminating occupancy volatility; and (4) Exceptionally High Barriers to Entry: Stringent CQC registration requirements and local authority "
        "DPS qualification frameworks prevent casual market entrants."
    )

    # Section 2.0
    doc.add_heading_1("2.0 ENTERPRISE VALUATION (EV) MULTIPLES & M&A BENCHMARKS")
    doc.add_paragraph(
        "M&A transactions in the UK specialist care sector price operating businesses (OpCos) at multiples between 6.5x and 8.5x EBITDA, "
        "depending on CQC rating, clinical acuity, and real estate modernism."
    )

    doc.add_table(
        title="Table 18.1: Enterprise Valuation (EV) & Exit Realization Sensitivity Matrix",
        headers=["Valuation Scenario", "EBITDA Multiple", "OpCo Enterprise Value", "PropCo Freehold Asset Value", "Total Group Enterprise Value", "Net Equity Value"],
        rows=[
            ["Conservative Benchmark", "6.5x EBITDA", "£2,219,048.00", "£1,385,714.00 (7.0% cap)", "£3,604,762.00", "£3,536,362.00"],
            ["Baseline Market Multiple", "7.5x EBITDA", "£2,560,440.00", "£1,492,307.00 (6.5% cap)", "£4,052,747.00", "£3,984,347.00"],
            ["Premium Quality Multiple", "8.5x EBITDA", "£2,901,832.00", "£1,616,666.00 (6.0% cap)", "£4,518,498.00", "£4,450,098.00"],
            ["Roll-Up Platform (3+ Sites)", "9.5x EBITDA", "£3,243,224.00", "£1,763,636.00 (5.5% cap)", "£5,006,860.00", "£4,938,460.00"]
        ],
        col_pcts=[22, 14, 16, 18, 16, 14]
    )

    # Section 3.0
    doc.add_heading_1("3.0 DEBT SERVICE COVERAGE RATIO (DSCR) & REFINANCING CAPACITY")
    doc.add_paragraph(
        "The financial architecture allows the group to secure senior commercial mortgage facilities against the freehold assets "
        "and cash flows, unlocking non-dilutive liquidity for further group expansion."
    )

    doc.add_table(
        title="Table 18.2: Commercial Debt Sizing & Debt Service Coverage Ratios",
        headers=["Debt Facility Metric", "Conservative (60% LTV)", "Baseline (70% LTV)", "Aggressive (75% LTV)", "Prudential Covenant Threshold"],
        rows=[
            ["Senior Debt Facility Sized", "£831,428.00", "£970,000.00", "£1,039,285.00", "Max 75% LTV"],
            ["Commercial Interest Rate", "6.50% (Base + 2.5%)", "6.50% (Base + 2.5%)", "6.75% (Base + 2.75%)", "Market Floating / Fixed Cap"],
            ["Annual Debt Service Cost", "£54,042.00", "£63,050.00", "£70,151.00", "Fully Serviced by PropCo Rent (£97k)"],
            ["PropCo Debt Coverage (DSCR)", "1.79x Coverage", "1.54x Coverage", "1.38x Coverage", "Bank Minimum: 1.30x DSCR"],
            ["Consolidated Group DSCR", "8.11x Coverage", "6.95x Coverage", "6.25x Coverage", "Bank Minimum: 2.00x DSCR"]
        ],
        col_pcts=[26, 18, 18, 18, 20]
    )

    # Section 4.0
    doc.add_heading_1("4.0 INSTITUTIONAL EXIT STRATEGIES & ACQUIRER LANDSCAPE")
    doc.add_callout(
        "FOUR VIABLE CAPITAL REALISATION & EXIT PATHWAYS",
        "1. Trade Sale to National Social Care Operator: Sale of 100% of OpCo shares to established national providers expanding in Bedfordshire "
        "(e.g. Voyage Care, CareTech / Cambian, Accomplish Group, Lifeways), retaining PropCo freehold real estate on a 25-year institutional FRI lease.\n"
        "2. Social Housing REIT Sale-and-Leaseback: Sale of the freehold property assets to specialized healthcare REITs (e.g. Civitas Social Housing, "
        "Triple Point Social Housing REIT) at 5.5%–6.0% yields, recycling £1.6M+ in liquid equity while retaining 100% of OpCo operating cash flows.\n"
        "3. Private Equity Roll-Up Platform: Utilizing the Luton campus as the high-margin seed platform to acquire 2–3 additional care properties "
        "in Hertfordshire and Buckinghamshire, achieving an aggregated £1M+ EBITDA and commanding an exit multiple of 9.0x–10.5x EBITDA.\n"
        "4. Management Buyout (MBO): Transitioning operational leadership to the Registered Manager and clinical leadership team funded by senior debt."
    )

    doc.build_pdf("ADOV_Care_Group_Private_Investment_Prospectus.pdf")
    doc.build_docx("ADOV_Care_Group_Private_Investment_Prospectus.docx")
    print("✓ Completed Private Investment Prospectus (PDF & DOCX).")


if __name__ == "__main__":
    print("=" * 80)
    print("BUILDING LANDSCAPE JOURNAL VAULT — PART 4 (GOVERNMENT & PROSPECTUS)")
    print("Exhaustive PhD-level commissioning, investment, architectural, and M&A monographs.")
    print("=" * 80)
    build_government_project_report()
    build_private_project_prospectus()
    build_photographic_campus_masterplan()
    build_private_investment_prospectus()
    print("PART 4 COMPLETE: All 4 Government & Prospectus reports built successfully in Landscape A4 PDF & Word!")
