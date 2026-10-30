import re
import os

print("Building V2.1 Executive Planning & Readers-Friendly Layout...")

with open('portal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the 4 Planning Stages and their tabs
STAGES = [
    {
        "id": "stage-1",
        "title": "Stage 1: Strategy & Viability",
        "desc": "Market options, investment verdict & campus strategy",
        "tabs": ["tab-overview", "tab-options", "tab-advisory", "tab-strategy"]
    },
    {
        "id": "stage-2",
        "title": "Stage 2: Real Estate & Legal",
        "desc": "Properties, fit-out budget, planning law & tax structure",
        "tabs": ["tab-houses", "tab-capex", "tab-planning", "tab-tax"]
    },
    {
        "id": "stage-3",
        "title": "Stage 3: CQC & Launch",
        "desc": "CQC statutory approval, financial model & intake SOP",
        "tabs": ["tab-cqc", "tab-cqc-reqs", "tab-financials", "tab-commissioning"]
    },
    {
        "id": "stage-4",
        "title": "Stage 4: Execution & Governance",
        "desc": "90-day tracker, master document vault & glossary",
        "tabs": ["tab-tracker", "tab-vault", "tab-glossary"]
    }
]

# Tab metadata for Sticky Rail & Executive Takeaway Box
TAB_META = {
    "tab-overview": {
        "stage": "Stage 1: Strategy & Viability",
        "short_title": "Overview",
        "takeaway": "Unanimously selected Option 4 (8-bed Supported Living across 78 & 80 Marston Gardens) yields £341k EBITDA (35% margin) with planning immunity under TCPA 1990 S.192 and full CQC Reg 13 financial solvency.",
        "decision": "Approve 90-day execution roadmap and sanction £68,400 CapEx fit-out.",
        "statute": "TCPA 1990 s.192 • HSCA 2008 Regs 2014 • ITEPA 2003 s.105/106",
        "stats": [("Specialist Capacity", "8 Suites (100%)"), ("Turnover", "£977,600 / Yr"), ("OpCo EBITDA", "£341,392 (35%)"), ("Break-Even", "3.8 Beds (47.5%)")],
        "pdf": "docs/ADOV_Care_Group_Final_Recommendation_Report.pdf",
        "docx": "docs/ADOV_Care_Group_Final_Recommendation_Report.docx",
        "anchors": [("sec-verdict", "1. Executive Verdict & Bottom Line"), ("sec-appraisal", "2. 4 Care Sector Comparison"), ("sec-pillars", "3. Operational Architecture"), ("sec-action", "4. 90-Day Execution Action Plan")],
        "diagrams": ["campus", "waterfall", "cqc"]
    },
    "tab-options": {
        "stage": "Stage 1: Strategy & Viability",
        "short_title": "4-Options Comparison",
        "takeaway": "Supported Living (Autism/LD) scores 94/100 on multi-criteria MCDA scoring, defeating Children's Home (72), Elderly Dementia (68), and Shared HMO (58) across profit, planning ease, and regulatory speed.",
        "decision": "Reject Children's Home and C2 Elderly models; proceed exclusively with Option 4.",
        "statute": "MCDA 100-Point Scoring Model • CQC Single Assessment Framework",
        "stats": [("Option 4 Score", "94 / 100 (Winner)"), ("EBITDA Advantage", "+£122k vs Children's"), ("Planning Risk", "Zero (S.192 CLPUD)"), ("Local Demand", "High (Repatriation)")],
        "pdf": "docs/ADOV_Care_Group_4_Options_Strategic_Comparison_Report.pdf",
        "docx": "docs/ADOV_Care_Group_4_Options_Strategic_Comparison_Report.docx",
        "anchors": [("sec-formula", "1. MCDA Scoring Formula"), ("sec-matrix", "2. Master Multi-Dimensional Matrix"), ("sec-breakdown", "3. Strategic Forensic Breakdown"), ("sec-stress", "4. Financial Viability & Stress-Test")],
        "diagrams": ["mcda"]
    },
    "tab-advisory": {
        "stage": "Stage 1: Strategy & Viability",
        "short_title": "Advisory Board",
        "takeaway": "Multidisciplinary appraisal from 7 senior specialists (Strategist, Care CEO, Financial Adviser, Barrister, Surveyor, CQC Inspector, Tax Partner) rates project viability at Grade A- (9.3 / 10).",
        "decision": "Adopt the 5 Operator Golden Rules and maintain £80k cash reserve for local authority billing lag.",
        "statute": "Health and Social Care Act 2008 • Luton Local Plan LLP32",
        "stats": [("Advisory Verdict", "Grade A- (9.3 / 10)"), ("Solvency Rating", "100% Pass"), ("Enterprise Value", "£2.22M – £2.90M"), ("Payback Period", "< 2.5 Months")],
        "pdf": "docs/ADOV_Care_Group_Expert_Advisory_Board_and_Viability_Assessment_Report.pdf",
        "docx": "docs/ADOV_Care_Group_Expert_Advisory_Board_and_Viability_Assessment_Report.docx",
        "anchors": [("sec-moats", "1. Economic Moats & SWOT"), ("sec-rota", "2. Operational Discipline & Safeguards"), ("sec-economics", "3. Unit Economics & Void Sensitivity"), ("sec-valuation", "4. Commercial Valuation & DSCR"), ("sec-cqc-hurdle", "5. Single Assessment Framework")],
        "diagrams": ["corp"]
    },
    "tab-strategy": {
        "stage": "Stage 1: Strategy & Viability",
        "short_title": "Campus Strategy",
        "takeaway": "Management unanimously selects Scenario A (Deploying both 78 & 80 Marston Gardens as unified 8-bed campus while Director moves to 82 Marston Gardens under market AST).",
        "decision": "Execute Director relocation to 82 Marston Gardens; formalize intercompany campus lease.",
        "statute": "Town & Country Planning Act 1990 s.55(2)(f) • ITEPA 2003 s.105/106",
        "stats": [("Selected Strategy", "Scenario A (78 + 80)"), ("Shared Rota Saving", "£85k / Yr Synergy"), ("Director Residence", "82 Marston Gardens"), ("HMRC BIK", "Nil (£0 Tax)")],
        "pdf": "docs/ADOV_Care_Group_Campus_Strategy_Appraisal.pdf",
        "docx": "docs/ADOV_Care_Group_Campus_Strategy_Appraisal.docx",
        "anchors": [("sec-scenario-a", "1. Management Narrative for Scenario A"), ("sec-comp-model", "2. Scenario A vs Scenario B Model"), ("sec-synergies", "3. Shared Campus Rota Synergies")],
        "diagrams": ["photo", "campus"]
    },
    "tab-houses": {
        "stage": "Stage 2: Real Estate & Legal",
        "short_title": "Properties & Gardens",
        "takeaway": "Three properties on Marston Gardens offer 8 specialist suites (5 in 78, 3 in 80), 8 off-street parking bays, and 100ft therapeutic enclosed sensory rear gardens with direct bi-fold access.",
        "decision": "Sanction external garden sensory pathway landscaping and secure boundary fencing.",
        "statute": "National Minimum Standards • HTM 01-04 Infection Control • BS 2881",
        "stats": [("78 Capacity", "5 Suites (1 En-Suite)"), ("80 Capacity", "3 Suites + Staff Office"), ("Parking", "8 Off-Street Spaces"), ("Sensory Gardens", "100ft Enclosed (Both)")],
        "pdf": "docs/ADOV_Care_Group_Photographic_Campus_Masterplan.pdf",
        "docx": "docs/ADOV_Care_Group_Photographic_Campus_Masterplan.docx",
        "anchors": [("sec-shared-arch", "1. External Architecture & Drives"), ("sec-topology", "2. Internal Room Structure & Specs"), ("sec-gardens", "3. 100ft Sensory Gardens Masterplan")],
        "diagrams": ["photo", "campus"]
    },
    "tab-capex": {
        "stage": "Stage 2: Real Estate & Legal",
        "short_title": "CapEx Fit-Out",
        "takeaway": "Total conversion CapEx is £68,400 (£38.6k for 78, £29.8k for 80), paid back in under 2.5 months from operating cashflows. Zero structural demolition required.",
        "decision": "Approve contractor tender for BS 5839-1 Category L1 fire alarm and FD30S doors.",
        "statute": "Regulatory Reform (Fire Safety) Order 2005 • BS 5839-1 • Approved Doc B",
        "stats": [("Total CapEx", "£68,400"), ("78 Allocation", "£38,600 (5 Beds)"), ("80 Allocation", "£29,800 (3 Beds)"), ("Payback Period", "2.4 Months (<75 Days)")],
        "pdf": "docs/ADOV_Care_Group_CQC_Registration_Master_Report.pdf",
        "docx": "docs/ADOV_Care_Group_CQC_Registration_Master_Report.docx",
        "anchors": [("sec-budget-table", "1. Itemized Fit-Out Budget Breakdown"), ("sec-fire-specs", "2. BS 5839 L1 Fire Alarm Specifications")],
        "diagrams": []
    },
    "tab-planning": {
        "stage": "Stage 2: Real Estate & Legal",
        "short_title": "Town Planning CLPUD",
        "takeaway": "Converting 78 and 80 Marston Gardens into Supported Living operates under Class C3(b) (up to 6 residents receiving care per dwelling). Planning permission is NOT required; S.192 CLPUD is legally unchallengeable.",
        "decision": "Submit two separate Section 192 CLPUD applications to Luton Borough Council.",
        "statute": "Town & Country Planning Act 1990 s.192 • North Devon DC v FSS [2004]",
        "stats": [("Planning Class", "Class C3(b) Permitted"), ("Application Type", "Section 192 CLPUD"), ("Highways Policy", "LLP32 Satisfied (8 Cars)"), ("Neighbour Objections", "Legally Inadmissible")],
        "pdf": "docs/ADOV_Care_Group_Section_192_Planning_Statement.pdf",
        "docx": "docs/ADOV_Care_Group_Section_192_Planning_Statement.docx",
        "anchors": [("sec-c3b-law", "1. Class C3(b) Planning Law & Case Precedent"), ("sec-llp32", "2. Luton Local Plan LLP32 Highways Compliance")],
        "diagrams": ["campus"]
    },
    "tab-tax": {
        "stage": "Stage 2: Real Estate & Legal",
        "short_title": "Corporate Structure & Tax",
        "takeaway": "Three-tier architecture (Mamun Ltd Holding Co -> ADOV Ltd PropCo -> ADOV Care Group Ltd OpCo) shields real estate from clinical liabilities and creates tax-deductible intercompany rent.",
        "decision": "Execute 10-year FRI commercial leases at £65k (78) and £32k (80); sign AST for 82.",
        "statute": "ITEPA 2003 s.105/106 • VATA 1994 Sch 9 Group 7 (Welfare Exemption)",
        "stats": [("Holding Co", "Mamun LIMITED (100%)"), ("PropCo Rent", "£97,000 / Yr (FRI)"), ("Corporation Tax", "19-25% Deductible"), ("82 Director AST", "BIK = Nil (£0 Tax)")],
        "pdf": "docs/ADOV_Care_Group_Corporate_Legal_Pack.pdf",
        "docx": "docs/ADOV_Care_Group_Corporate_Legal_Pack.docx",
        "anchors": [("sec-corp-summary", "1. Corporate Architecture Flow"), ("sec-lease-summary", "2. Statutory Commercial Lease Summary")],
        "diagrams": ["corp"]
    },
    "tab-cqc": {
        "stage": "Stage 3: CQC & Launch",
        "short_title": "CQC Approval Roadmap",
        "takeaway": "Detailed 5-phase statutory roadmap to secure CQC 'Personal Care' provider registration. Utilizing Section 28(3) statutory representations waiver cuts 28 days off registration time.",
        "decision": "Appoint Registered Manager (Level 5) and submit pre-application pack.",
        "statute": "Health & Social Care Act 2008 s.26-28 • CQC Registration Regs 2009",
        "stats": [("Approval Target", "90 Calendar Days"), ("Registered Manager", "Level 5 Leadership"), ("Fast-Track Saving", "28 Days (S.28(3) Waiver)"), ("Interview Format", "5 Clinical Scenarios")],
        "pdf": "docs/ADOV_Care_Group_CQC_Registration_Master_Report.pdf",
        "docx": "docs/ADOV_Care_Group_CQC_Registration_Master_Report.docx",
        "anchors": [("sec-cqc-steps", "1. 5-Phase Registration Steps"), ("sec-cqc-leadership", "2. Leadership & RM Qualifications"), ("sec-s28", "3. Section 28(3) Fast-Track Waiver"), ("sec-rm-interview", "4. 5 Core RM Interview Clinical Scenarios"), ("sec-cqc-questions", "5. Complete CQC Provider Application Questions")],
        "diagrams": ["cqc"]
    },
    "tab-cqc-reqs": {
        "stage": "Stage 3: CQC & Launch",
        "short_title": "CQC Statutory Standards",
        "takeaway": "Complete fulfillment guide across all 10 Statutory Pillars (Regulations 4-20) under CQC's New Single Assessment Framework (Safe, Effective, Caring, Responsive, Well-Led).",
        "decision": "Audit all 24 statutory verification checkboxes prior to CQC inspector site visit.",
        "statute": "Health and Social Care Act 2008 (Regulated Activities) Regs 2014 Reg 4-20",
        "stats": [("Compliance Pillars", "10 Statutory Pillars"), ("Quality Statements", "34 Framework Statements"), ("Mandatory Training", "Oliver McGowan Tier 2"), ("Medication Standard", "BS 2881 Controlled Drugs")],
        "pdf": "docs/ADOV_Care_Group_CQC_Requirements_and_Fulfillment_Guide.pdf",
        "docx": "docs/ADOV_Care_Group_CQC_Requirements_and_Fulfillment_Guide.docx",
        "anchors": [("sec-reqs-audit", "1. Interactive 24-Point Compliance Audit"), ("sec-pillar1", "2. Pillar 1: Fit and Proper Persons (Reg 4-5)"), ("sec-pillar2", "3. Pillar 2: Registered Manager Competency (Reg 7)"), ("sec-pillar3", "4. Pillar 3: Statement of Purpose (Reg 12)")],
        "diagrams": ["cqc"]
    },
    "tab-financials": {
        "stage": "Stage 3: CQC & Launch",
        "short_title": "Financial P&L Model",
        "takeaway": "Consolidated Group turnover of £977,600 generates £341,392 OpCo EBITDA (35.0% margin) and £97,000 PropCo net rent, totaling £438,392 annual pre-tax cashflow (£36,532/month).",
        "decision": "Review stress-test sensitivity table and establish working capital cash buffer.",
        "statute": "CQC Regulation 13 (Financial Viability) • Supported Exempt Accommodation",
        "stats": [("Gross Revenue", "£977,600 / Yr"), ("OpCo EBITDA", "£341,392 (35.0%)"), ("PropCo Net Rent", "£97,000 / Yr"), ("Group Cash Flow", "£438,392 / Yr")],
        "pdf": "docs/ADOV_Care_Group_Operational_PnL_and_Financial_Viability_Model.pdf",
        "docx": "docs/ADOV_Care_Group_Operational_PnL_and_Financial_Viability_Model.docx",
        "anchors": [("sec-fin-simulator", "1. Interactive Placement Fee Simulator"), ("sec-fin-waterfall", "2. 3-Year Operating Waterfall"), ("sec-fin-opex", "3. Itemized Monthly OpEx Running Costs"), ("sec-fin-pnl", "4. Stabilized Year Operational P&L")],
        "diagrams": ["waterfall"]
    },
    "tab-commissioning": {
        "stage": "Stage 3: CQC & Launch",
        "short_title": "Commissioning & SOP",
        "takeaway": "Six-stage zero-void clinical pathway integrating Luton Borough Council DPS (Framework AT1115), NHS BLMK ICB Continuing Healthcare, and Supported Exempt Housing Benefit (£350/wk).",
        "decision": "Register OpCo profile on ProContract (Proactis) e-tendering portal upon CQC submission.",
        "statute": "Care Act 2014 • Transforming Care Agenda • Section 117 Mental Health Act",
        "stats": [("Council Portal", "ProContract AT1115"), ("NHS Commissioning", "BLMK ICB CHC / S.117"), ("Housing Benefit", "£350 / Wk Exempt"), ("Intake Protocol", "6 Phased Clinical Stages")],
        "pdf": "docs/ADOV_Care_Group_Resident_Intake_Pathway_SOP.pdf",
        "docx": "docs/ADOV_Care_Group_Resident_Intake_Pathway_SOP.docx",
        "anchors": [("sec-comm-dps", "1. Luton Council DPS & NHS Commissioning"), ("sec-comm-s1", "2. Strategy 1: Multi-Channel Pipeline"), ("sec-comm-s2", "3. Strategy 2: Pre-Admission Clinical Triage")],
        "diagrams": ["intake"]
    },
    "tab-tracker": {
        "stage": "Stage 4: Execution & Governance",
        "short_title": "90-Day Tracker",
        "takeaway": "Operational master checklist spanning 4 distinct execution phases from initial corporate leases and S.192 planning filing to full occupancy and CQC inspection signoff.",
        "decision": "Assign team responsibilities and monitor weekly milestone completion percentages.",
        "statute": "Project Management Governance • Statutory Filing Timelines",
        "stats": [("Total Tasks", "24 Key Milestones"), ("Launch Target", "90 Calendar Days"), ("Phases", "4 Execution Phases"), ("Responsible Parties", "Director, RM & Surveyor")],
        "pdf": "docs/ADOV_Care_Group_Master_Document_Checklist.pdf",
        "docx": "docs/ADOV_Care_Group_Master_Document_Checklist.docx",
        "anchors": [("sec-track-p1", "1. Phase 1: Legal Leases & Planning"), ("sec-track-p2", "2. Phase 2: Fit-Out & Landscaping"), ("sec-track-p3", "3. Phase 3: CQC & Procurement"), ("sec-track-p4", "4. Phase 4: Launch & Full Occupancy")],
        "diagrams": []
    },
    "tab-vault": {
        "stage": "Stage 4: Execution & Governance",
        "short_title": "Document Vault",
        "takeaway": "Central executive filing repository housing all 30 master reports, statutory legal packs, and editable Word templates ready for download, printing, or bank submission.",
        "decision": "Download complete corporate and planning document packs for solicitor execution.",
        "statute": "Statutory Document Retention • Executive Governance",
        "stats": [("Master Reports", "15 Dedicated Filings"), ("Formats", "PDF Dossier + Word DOCX"), ("Corporate Packs", "Leases, Tenancies, S192"), ("Total Files", "30 Verified Downloads")],
        "pdf": "docs/ADOV_Care_Group_Government_Project_Report.pdf",
        "docx": "docs/ADOV_Care_Group_Government_Project_Report.docx",
        "anchors": [("sec-vault-reports", "1. Executive Strategic Reports"), ("sec-vault-packs", "2. Statutory Legal & Governance Packs")],
        "diagrams": []
    },
    "tab-glossary": {
        "stage": "Stage 4: Execution & Governance",
        "short_title": "Glossary",
        "takeaway": "Exhaustive executive glossary defining 40+ statutory, regulatory, clinical, and financial terms and legal citations used throughout the project.",
        "decision": "Use as reference guide during CQC Registered Manager interview and Council meetings.",
        "statute": "Care Act 2014 • HSCA 2008 • Mental Capacity Act 2005 (DoLS)",
        "stats": [("Defined Terms", "40+ Statutory Acronyms"), ("Regulatory Bodies", "CQC, Ofsted, ICB, LBC"), ("Legal Precedents", "North Devon, Hossack"), ("Clinical Standards", "PBS, MAR, DoLS, LPS")],
        "pdf": "docs/ADOV_Care_Group_Final_Recommendation_Report.pdf",
        "docx": "docs/ADOV_Care_Group_Final_Recommendation_Report.docx",
        "anchors": [("sec-glossary-filter", "1. Searchable Acronyms Filter"), ("sec-glossary-table", "2. Complete Definitions Table")],
        "diagrams": []
    }
}

print("Loaded metadata for all 15 tabs.")
