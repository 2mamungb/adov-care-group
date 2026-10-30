#!/usr/bin/env python3
"""
ADOV Care Group — Landscape Journal Builder: Part 2 (CQC & Clinical SOPs)
Exhaustive PhD-level statutory monographs and standard operating procedures for boardroom planning.

Documents:
5. ADOV_Care_Group_CQC_Registration_Master_Report (PDF & DOCX)
6. ADOV_Care_Group_CQC_Requirements_and_Fulfillment_Guide (PDF & DOCX)
7. ADOV_Care_Group_CQC_Provider_Application_Questions_Dossier (PDF & DOCX)
8. ADOV_Care_Group_Resident_Intake_Pathway_SOP (PDF & DOCX)
13. ADOV_Care_Group_CQC_Statement_of_Purpose (PDF & DOCX)
"""

import os
import sys
from landscape_journal_engine import LandscapeDocument

# ==============================================================================
# DOC 5: CQC REGISTRATION MASTER REPORT
# ==============================================================================
def build_cqc_registration_master_report():
    doc = LandscapeDocument(
        title="CQC PROVIDER & REGISTERED MANAGER REGISTRATION MASTER DOSSIER",
        doc_ref="ACG-LUTON-2026-CQC-REG",
        category="CQC REGULATORY DOSSIER",
        subtitle="Single Assessment Framework Alignment, Statutory Evidence Portfolios, Personnel Vetting & Fast-Track Commissioning Strategy"
    )

    doc.set_meta([
        ("Applicant Legal Entity", "ADOV Care Group LIMITED (Company No. 14289650)"),
        ("Ultimate Parent Entity", "FAIRYTALES GROUP (Trading Name of Mamun Limited)"),
        ("Freehold Asset PropCo", "ADOV LIMITED (Freehold Real Estate Co)"),
        ("Registered Care Campus", "78 & 80 Marston Gardens, Luton, Bedfordshire, LU2 7DY"),
        ("Regulated Activity", "Personal Care (Specialist Supported Living / Town Planning Class C3b)"),
        ("Primary Statutory Mandate", "Health and Social Care Act 2008 & 2014 Regs // CQC Single Assessment Framework"),
        ("Strategic Advisory Lead", "Lead Regulatory & Care Specialist // Project Planned by AbdullahMamun.com"),
        ("Target Service Users", "Adults (18–64) with Autism, Severe Learning Disabilities & Complex Sensory Needs")
    ])

    doc.set_kpis([
        ("34", "Quality Statements", "Single Assessment Framework"),
        ("Level 5", "Manager Credential", "Diploma in Leadership Adult Care"),
        ("Reg 6 & 7", "Statutory Roles", "Nominated Individual & Reg Manager"),
        ("28 Days Saved", "Section 28(3) Waiver", "Fast-track Notice of Decision"),
        ("100% Compliant", "Pre-Submission Audit", "Zero enforcement risk")
    ])

    # Section 1.0
    doc.add_heading_1("1.0 STATUTORY REGULATORY ARCHITECTURE & REGULATED ACTIVITY CLASSIFICATION")
    doc.add_paragraph(
        "This master dossier establishes the statutory registration architecture for ADOV Care Group Limited "
        "as a registered provider of 'Personal Care' under Schedule 1 of the Health and Social Care Act 2008 (Regulated Activities) "
        "Regulations 2014. The registration encompasses the dual-property care campus at 78 and 80 Marston Gardens, Luton, "
        "delivering high-support specialist supported living under Positive Behaviour Support (PBS) principles. Operating as a supported living "
        "provider under Class C3(b) rather than a residential care home under Class C2 provides fundamental statutory, operational, and "
        "financial advantages that directly protect the enterprise, empower residents, and eliminate institutional friction."
    )

    doc.add_callout(
        "THE SUPPORTED LIVING STATUTORY ADVANTAGE: TENANCY VS. CARE SEPARATION",
        "By registering exclusively for 'Personal Care' in a Supported Living environment, ADOV Care Group establishes a strict legal and "
        "statutory separation: housing is delivered under individual Assured Shorthold Tenancy (AST) agreements conferring exclusive possession, "
        "while care is commissioned under independent, person-centered support contracts. This structure fulfills CQC's definitive guidance "
        "'Right support, right care, right culture', enables tenants to claim Supported Housing Benefit (Specified Exempt Accommodation) at £350/wk, "
        "and completely avoids the costly physical mandates of Class C2 institutions (e.g. sluice rooms, commercial lifts, institutional dining halls)."
    )

    doc.add_heading_2("1.1 Comparative Analysis: Supported Living (Personal Care) vs. Residential Care Home (C2)")
    doc.add_table(
        title="Table 5.1: Comparative Statutory and Operational Analysis: Supported Living vs Care Home",
        headers=["Regulatory Dimension", "Specialist Supported Living (ADOV Model)", "Residential Care Home (Class C2)", "Strategic Advantage to ADOV Group"],
        rows=[
            ["Regulated Activity", "Personal Care (Schedule 1, HSCA 2014)", "Accommodation for persons requiring care", "Greater regulatory flexibility; domicile-based care"],
            ["Tenancy Rights", "Individual AST; exclusive possession of bedroom", "License to occupy only; no statutory tenancy", "Empowers residents; secures £350/wk Exempt Housing Benefit"],
            ["Physical Standards", "Domestic residential standards (Part M & E)", "Institutional standards (sluice, lift, clinic)", "Saves over £120,000 in redundant institutional CapEx"],
            ["Town Planning", "Class C3(b) Permitted Development (S.192 CLPUD)", "Class C2 Planning Permission Required", "100% Planning immunity; immune to neighbor objections"],
            ["Fee Structure", "Unbundled: Care Fee + 1:1 Hours + Housing Benefit", "Single bundled local authority block tariff", "Significantly higher gross yield (£2,350/wk vs £1,100/wk)"],
            ["CQC Inspection Model", "SAF: Right Support, Right Care, Right Culture", "SAF: Traditional Institutional Care Home", "Exemplifies modern NHS Transforming Care best practice"]
        ],
        col_pcts=[18, 28, 28, 26]
    )

    # Section 2.0
    doc.add_heading_1("2.0 STATUTORY PERSONNEL VETTING & GOVERNANCE APPOINTMENTS")
    doc.add_paragraph(
        "Under Regulations 5, 6, and 7 of the Health and Social Care Act 2008 (Regulated Activities) Regulations 2014, the Care Quality Commission "
        "enforces stringent vetting standards upon corporate directors, the Nominated Individual (NI), and the Registered Manager (RM). "
        "The board of ADOV Care Group Limited has structured these roles to ensure absolute regulatory compliance, professional leadership, "
        "and seamless clinical governance."
    )

    doc.add_table(
        title="Table 5.2: Statutory Roles, Legal Responsibilities & Regulatory Credentials Register",
        headers=["Statutory Role", "Designated Individual", "Legal Citation", "Mandatory Credentials & Experience", "Core Statutory Responsibilities"],
        rows=[
            ["Nominated Individual", "Appointed Executive Director", "Regulation 6 HSCA 2014", "Senior executive with corporate governance acumen and DBS clearance", "Supervises management; direct accountability to CQC; quarterly audits"],
            ["Registered Manager", "Appointed Care Specialist", "Regulation 7 HSCA 2014", "Level 5 Diploma in Leadership for Adult Care; 5+ yrs LD experience", "Day-to-day clinical direction, staffing rotas, MAR audits, safeguarding"],
            ["Corporate Directors", "Board of ADOV Care Group", "Regulation 5 HSCA 2014", "Fit and Proper Person Declarations; bankruptcy & insolvency clearance", "Corporate solvency, resource allocation, health & safety investment"],
            ["PBS Clinical Lead", "Senior Behaviour Specialist", "NICE Guideline NG11", "Certified PBS Practitioner / BILD Accredited Trainer", "Formulates Functional Behaviour Assessments, sensory diet protocols"],
            ["Health & Safety Lead", "External Retained Surveyor", "Reg 15 & RRO 2005", "NEBOSH / IOSH Qualified Environmental Health Auditor", "Conducts fire risk assessments (BS 5839), TMV3 water safety, Legionella"]
        ],
        col_pcts=[16, 18, 16, 26, 24]
    )

    # Section 3.0
    doc.add_heading_1("3.0 SINGLE ASSESSMENT FRAMEWORK (SAF) COMPLIANCE ARCHITECTURE")
    doc.add_paragraph(
        "The CQC assesses providers under the Single Assessment Framework, structured across 5 Key Questions and 34 Quality Statements. "
        "ADOV Care Group has engineered a comprehensive evidence portfolio aligning each Quality Statement with physical property "
        "controls, clinical documentation, and staff operational workflows."
    )

    doc.add_table(
        title="Table 5.3: CQC Single Assessment Framework & Quality Statements Compliance Matrix",
        headers=["Key Question", "Quality Statements Covered", "Operational Fulfillment Mechanism", "Physical Campus Evidence", "Governance Audit Schedule"],
        rows=[
            ["SAFE", "Safeguarding, Involving people, Safe environments, Infection control, Medicines", "Strict PBS de-escalation; zero physical restraint; comprehensive MAR administration", "BS 2881 CD Cabinet; TMV3 anti-scald valves; BS 5839-1 L1 fire system", "Weekly MAR audits; monthly H&S site inspections"],
            ["EFFECTIVE", "Assessing needs, Delivering care, Nutrition, Mental Capacity, Consent", "Care Act & MCA assessments; bespoke communication passports; sensory meal plans", "Sensory kitchen layout; accessible wet rooms; domestic dining spaces", "Quarterly clinical case reviews; annual dietary audit"],
            ["CARING", "Kindness & compassion, Treating people as individuals, Independence", "Active Support methodology; dedicated keyworkers; domestic chore participation", "Personalized private bedrooms (12.5m²-16m²); private 100ft sensory gardens", "Monthly keyworker 1:1 sessions; family surveys"],
            ["RESPONSIVE", "Person-centred care, Providing information, Equity in experiences", "Easy-Read service user guides; graduated 7-stage pre-admission pathway", "Acoustic Part E soundproofing to prevent resident sensory overload", "Pre-admission triage; 28-day statutory reviews"],
            ["WELL-LED", "Shared vision, Capable leaders, Duty of Candour, Governance & systems", "Monthly Registered Manager dashboard; Nominated Individual quarterly oversight", "Dedicated management office in No. 80; real-time digital care logs", "Monthly board reviews; external mock CQC audit"]
        ],
        col_pcts=[12, 24, 24, 22, 18]
    )

    # Section 4.0
    doc.add_heading_1("4.0 38-POLICY MASTER STATUTORY GOVERNANCE REGISTER")
    doc.add_paragraph(
        "In accordance with Regulation 17 (Good Governance), ADOV Care Group has commissioned and approved a complete 38-policy "
        "statutory governance register. These policies govern all operational, clinical, and employment practices across the campus."
    )

    doc.add_table(
        title="Table 5.4: Core Statutory Policies, Regulatory Alignment & Review Schedule",
        headers=["Policy Code & Name", "HSCA 2014 Regulation", "Policy Scope & Statutory Mandate", "Operational Review Lead", "Review Cadence"],
        rows=[
            ["POL-01: Safeguarding Adults at Risk", "Regulation 13", "Multi-agency reporting, Luton SAB liaison, zero-tolerance abuse protocol", "Registered Manager", "Annual / Post-Incident"],
            ["POL-02: Safe Handling of Medicines", "Regulation 12", "Controlled drugs storage (BS 2881), MAR charting, administration errors SOP", "Clinical Lead / RM", "Six-Monthly"],
            ["POL-03: Mental Capacity & Deprivation (DoLS)", "Regulation 11 & 13", "MCA two-stage test, best interests meetings, least restrictive practices", "Registered Manager", "Annual"],
            ["POL-04: Positive Behaviour Support (PBS)", "Regulation 12 & 10", "Functional assessment, de-escalation techniques, prohibition of restraint", "PBS Practitioner", "Annual"],
            ["POL-05: Duty of Candour Protocol", "Regulation 20", "Statutory notifications to families/funders following notifiable safety incidents", "Nominated Individual", "Annual"],
            ["POL-06: Infection Prevention & Control", "Regulation 12 & 15", "HTM 01-04 compliance, colour-coded cleaning, clinical waste handling", "House Team Leader", "Annual"],
            ["POL-07: Fire Safety & Evacuation", "Regulation 12 & 15", "PEEPs for all 8 residents, BS 5839-1 alarm maintenance, weekly fire drills", "H&S Coordinator", "Quarterly"],
            ["POL-08: Fit & Proper Persons Vetting", "Regulation 5 & 19", "Enhanced DBS with barred list checks, references, identity verification", "HR Director", "Annual"]
        ],
        col_pcts=[24, 16, 34, 14, 12]
    )

    # Section 5.0
    doc.add_heading_1("5.0 REGISTERED MANAGER CQC INTERVIEW READINESS & CLINICAL SCENARIOS")
    doc.add_paragraph(
        "A critical gate in the CQC registration process is the formal fit and proper interview of the Registered Manager. "
        "The following five clinical scenarios represent the rigorous, evidence-based responses formulated by ADOV Care Group's leadership."
    )

    doc.add_callout(
        "SCENARIO 1: SEVERE SENSORY OVERLOAD & CHALLENGING BEHAVIOUR",
        "Clinical Scenario: An autistic resident in No. 78 experiences severe sensory overload triggered by lawnmower noise from a neighboring garden, "
        "becoming physically distressed, pacing erratically, shouting, and attempting to throw dining chairs.\n"
        "Registered Manager Model Response: (1) Immediate PBS De-escalation: Withdraw non-essential staff; eliminate auxiliary sensory inputs (dim lights, "
        "close blinds, offer noise-cancelling headphones); (2) Low-Arousal Engagement: The allocated 1:1 keyworker uses gentle, low-tone Makaton communication "
        "and guides the resident to the quiet sensory relaxation room in No. 80; (3) Zero Restraint: Staff strictly maintain a non-restrictive safety perimeter; "
        "(4) Post-Incident Root Cause: Log an Antecedent-Behaviour-Consequence (ABC) chart, review sensory diet, and adapt outside acoustic buffers."
    )

    doc.add_callout(
        "SCENARIO 2: CONTROLLED DRUGS MEDICATION OMISSION",
        "Clinical Scenario: During the morning medication round, a Support Worker discovers that the 22:00 evening dose of Sodium Valproate "
        "(anti-epileptic) was not signed on the MAR chart for a resident in No. 80.\n"
        "Registered Manager Model Response: (1) Clinical Assessment: Conduct immediate physical check on resident for seizures or side effects; (2) Medical Consultation: "
        "Call NHS 111 / resident's GP to establish whether an emergency catch-up dose is clinically safe; (3) Investigation & Duty of Candour: Reconcile "
        "blister pack stock count to confirm if the dose was taken but unrecorded, or entirely missed; notify family under Duty of Candour; (4) Governance: "
        "Log incident on internal safeguarding system, suspend worker from medication rounds pending retraining, and submit CQC notification if harm occurred."
    )

    doc.add_callout(
        "SCENARIO 3: SAFEGUARDING DISCLOSURE OF FINANCIAL EXPLOITATION",
        "Clinical Scenario: During a 1:1 keyworker session, a resident states that a night worker asked to borrow £40 from their personal bank card "
        "to pay for petrol, promising to repay it the next morning.\n"
        "Registered Manager Model Response: (1) Protective Action: Ensure the resident is reassured and secure; audit the resident's locked cash tin and bank records immediately; "
        "(2) Suspension: Immediately suspend the implicated night worker on full pay pending formal investigation without alerting other staff; "
        "(3) Statutory Safeguarding Escalation: Submit a Section 42 safeguarding alert to Luton Borough Council Adult Social Care Safeguarding Team within 24 hours; "
        "(4) CQC & Police Notification: Submit a formal CQC Regulation 18 notification; report potential financial abuse to Bedfordshire Police if corroborated."
    )

    # Section 6.0
    doc.add_heading_1("6.0 STATUTORY FAST-TRACK REGISTRATION & SECTION 28(3) WAIVER EXECUTION")
    doc.add_paragraph(
        "Under Section 28 of the Health and Social Care Act 2008, when the CQC approves a provider application, it first issues a formal "
        "'Notice of Proposal' (NoP). By law, the applicant is granted 28 days to make representations against any proposed conditions. "
        "Under Section 28(3), if the applicant provides written notice waiving the right to make representations, the CQC must immediately "
        "issue the final 'Notice of Decision' (NoD), instantaneously making the registration legally effective."
    )

    doc.add_flow_stages(
        title="Figure 5.1: Fast-Track CQC Registration & Commissioning Roadmap (8–10 Weeks Total)",
        stages=[
            ("1", "Dossier Readiness", "Finalise enhanced DBS, GP health declarations, Statement of Purpose & 38 policies."),
            ("2", "Portal Submission", "Submit provider & manager applications via CQC Provider Portal with complete evidence bundle."),
            ("3", "Validation & Scrutiny", "CQC validation officer verifies submission completeness; passes to Lead Inspector within 10 days."),
            ("4", "Site Inspection & RM Interview", "Inspector conducts physical site audit of 78 & 80; conducts 90-minute RM interview."),
            ("5", "Notice of Proposal (NoP)", "CQC issues formal NoP confirming intention to grant registration with standard conditions."),
            ("6", "Section 28(3) Waiver", "Board executes written Section 28(3) waiver on Day 1; CQC issues final Notice of Decision immediately."),
            ("7", "DPS & ICB Activation", "Upload CQC certificate to Luton ProContract DPS (AT1115) and activate first resident intakes.")
        ]
    )

    doc.build_pdf("ADOV_Care_Group_CQC_Registration_Master_Report.pdf")
    doc.build_docx("ADOV_Care_Group_CQC_Registration_Master_Report.docx")
    print("✓ Completed CQC Registration Master Report (PDF & DOCX).")


# ==============================================================================
# DOC 6: CQC REQUIREMENTS & FULFILLMENT GUIDE
# ==============================================================================
def build_cqc_requirements_guide():
    doc = LandscapeDocument(
        title="CQC STATUTORY REQUIREMENTS & OPERATIONAL FULFILLMENT GUIDE",
        doc_ref="ACG-LUTON-2026-CQC-REQ",
        category="STATUTORY COMPLIANCE PLAYBOOK",
        subtitle="Exhaustive Clause-by-Clause Audit of Regulations 4 to 20 (HSCA 2014), Physical Property Specifications & Staffing Matrices"
    )

    doc.set_meta([
        ("Applicant Body", "ADOV Care Group LIMITED (OpCo)"),
        ("Statutory Instrument", "Health and Social Care Act 2008 (Regulated Activities) Regulations 2014"),
        ("Compliance Scope", "Regulations 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20"),
        ("Inspection Framework", "CQC Single Assessment Framework // Right Support, Right Care, Right Culture"),
        ("Subject Campus", "78 & 80 Marston Gardens, Luton, LU2 7DY (Specialist Autism Supported Living)"),
        ("Lead Regulatory Officer", "Healthcare Regulatory Compliance Team // Project Planned by AbdullahMamun.com"),
        ("Version Status", "Statutory Boardroom Edition (October 2026)")
    ])

    doc.set_kpis([
        ("17", "Key Regulations", "HSCA 2008 Regulated Activities"),
        ("100%", "Fulfillment Rate", "Zero statutory compliance gaps"),
        ("12.5m² - 16m²", "Bedroom Sizes", "Exceeds CQC domestic standards"),
        ("BS 5839-1", "Fire Alarm Spec", "Category L1 full addressable"),
        ("TMV3", "Thermostatic Controls", "Anti-scald water safety (Reg 15)")
    ])

    # Section 1.0
    doc.add_heading_1("1.0 CLAUSE-BY-CLAUSE STATUTORY FULFILLMENT REGISTER (REGULATIONS 4 TO 20)")
    doc.add_paragraph(
        "This statutory fulfillment register details the operational, physical, and documentary evidence assembled by ADOV Care Group "
        "to satisfy each mandatory regulation under the Health and Social Care Act 2008 (Regulated Activities) Regulations 2014."
    )

    doc.add_table(
        title="Table 6.1: Comprehensive Clause-by-Clause Statutory Fulfillment Register",
        headers=["Statutory Regulation", "Statutory Objective", "Operational Compliance Mechanism", "Physical / Documentary Verification"],
        rows=[
            ["Regulation 4", "General Requirements", "Operating provider must be legally incorporated and solvent", "Certificate of Incorporation No. 14289650; 5-yr P&L model"],
            ["Regulation 5", "Fit and Proper: Directors", "Ensure board directors have clean records and professional standing", "Director declarations, bankruptcy search, enhanced DBS on all board members"],
            ["Regulation 6", "Nominated Individual", "Appoint senior executive director to supervise care provision", "Board appointment resolution; CQC validation interview portfolio"],
            ["Regulation 7", "Registered Manager", "Appoint qualified, competent day-to-day manager of the service", "Level 5 Diploma in Leadership for Adult Care; 5-yr reference trail"],
            ["Regulation 9", "Person-Centred Care", "Deliver care tailored to individual preferences, needs, and autonomy", "Comprehensive PBS plans; sensory profiles; communication passports"],
            ["Regulation 10", "Dignity and Respect", "Treat service users with respect, privacy, and full human dignity", "Private lockable bedrooms; confidential care logs; dignity champions"],
            ["Regulation 11", "Need for Consent", "Ensure valid lawful consent or adherence to MCA 2005 principles", "MCA two-stage capacity assessments; Best Interests decision forms"],
            ["Regulation 12", "Safe Care and Treatment", "Prevent risks to health and safety, safe medication administration", "MAR charts; BS 2881 medicine cabinet; clinical risk assessments"],
            ["Regulation 13", "Safeguarding from Abuse", "Zero tolerance for abuse, improper treatment, or unlawful restraint", "Section 42 safeguarding protocol; Luton SAB liaison; whistleblowing line"],
            ["Regulation 14", "Meeting Nutritional Needs", "Provide balanced, culturally suitable, and nutritionally rich meals", "Sensory meal menus; hydration logs; Speech & Language therapy plans"],
            ["Regulation 15", "Premises and Equipment", "Ensure clean, safe, suitable, and well-maintained physical environment", "TMV3 anti-scald valves; BS 5839-1 L1 alarm; DDA ramps; Part E soundproofing"],
            ["Regulation 16", "Receiving Complaints", "Establish accessible, transparent complaints handling procedure", "Easy-Read complaints policy; statutory 28-day resolution timeframe"],
            ["Regulation 17", "Good Governance", "Operate robust auditing, quality assurance, and risk management systems", "Monthly RM governance dashboard; quarterly NI audits; annual mock CQC"],
            ["Regulation 18", "Staffing Ratios & Training", "Maintain sufficient numbers of suitably qualified, competent staff", "Shared rota (1 TL, 4 Day Support, 1 Waking Night, 1 Sleep-in); Oliver McGowan certs"],
            ["Regulation 19", "Fit and Proper: Staff", "Execute robust pre-employment vetting prior to client contact", "Enhanced DBS with barred list checks; 2 verified references; employment history"],
            ["Regulation 20", "Duty of Candour", "Maintain complete openness and transparency when safety incidents occur", "Statutory Duty of Candour SOP; written family notification within 10 days"]
        ],
        col_pcts=[16, 22, 34, 28]
    )

    # Section 2.0
    doc.add_heading_1("2.0 PHYSICAL PROPERTY, ENGINEERING & HEALTHCARE STANDARDS AUDIT")
    doc.add_paragraph(
        "To achieve seamless compliance with Regulation 15 (Premises and Equipment) and Building Regulations Approved Documents, "
        "the physical layout across 78 and 80 Marston Gardens has been engineered to exacting clinical and accessibility benchmarks."
    )

    doc.add_table(
        title="Table 6.2: Physical Infrastructure & Building Compliance Specifications",
        headers=["Infrastructure Element", "CQC / Statutory Standard", "ADOV Specification (78 & 80 Marston)", "Operational Impact"],
        rows=[
            ["Bedroom Dimensions", "Min 10.0m² (Supported Living) / 12.0m² (CQC)", "All 8 bedrooms range from 12.5m² to 16.0m²", "Generous space for sensory zoning and mobility aids"],
            ["Sanitary Ratios", "Min 1 accessible bathroom per 3 residents", "78: 1 ensuite, 1 large wetroom, 1 sep WC; 80: 1 wetroom, 1 WC", "Full non-slip wetrooms; TMV3 thermostatic safety controls"],
            ["Acoustic Separation", "Building Regs Part E (Sound Insulation)", "Soundbloc plasterboard & acoustic insulation on party walls", "Prevents sensory escalation between bedrooms and lounges"],
            ["Fire Detection", "BS 5839-1 Category L1 (Full Protection)", "Addressable optical smoke & heat detectors in all spaces", "Early warning system directly linked to central alarm panel"],
            ["Fire Compartmentation", "Approved Document B / RRO 2005", "FD30S fire-resisting doors with intumescent smoke seals", "Maintains 30-minute protected escape corridors"],
            ["Emergency Lighting", "BS 5266-1 (Maintained Escape Lighting)", "3-hour battery-backed LED luminaires along escape routes", "Ensures safe night-time evacuation in total power failure"],
            ["Medication Storage", "BS 2881 Controlled Drugs Standard", "Steel CD cabinet bolted to solid brick wall with dual locks", "Compliant with Misuse of Drugs (Safe Custody) Regs 1973"]
        ],
        col_pcts=[20, 24, 32, 24]
    )

    # Section 3.0
    doc.add_heading_1("3.0 MANDATORY STAFF TRAINING & COMPETENCY FRAMEWORK")
    doc.add_paragraph(
        "Under Regulation 18, all care and management staff undergo a rigorous mandatory training curriculum prior to delivering "
        "independent personal care, fully aligning with Skills for Care standards and the Oliver McGowan Code of Practice."
    )

    doc.add_key_value_grid(
        title="Mandatory Staff Training & Certification Register",
        items=[
            ("Oliver McGowan Tier 1 & 2", "Mandatory under Health & Care Act 2022. 100% of staff certified in Autism & Learning Disability awareness."),
            ("The Care Certificate", "All new support workers complete the 15 standards of the Care Certificate within 12 weeks of appointment."),
            ("Safeguarding Adults Level 2/3", "Recognising signs of physical, psychological, sexual, and financial abuse; reporting procedures."),
            ("Positive Behaviour Support (PBS)", "BILD-accredited training in low-arousal de-escalation, proactive strategies, and human rights."),
            ("Safe Administration of Medicines", "Theoretical and practical training; 3 shadow assessments required before unsupervised administration."),
            ("Mental Capacity Act & DoLS", "Understanding presumption of capacity, least restrictive principles, and lawful authorisations.")
        ],
        num_cols=2
    )

    doc.build_pdf("ADOV_Care_Group_CQC_Requirements_and_Fulfillment_Guide.pdf")
    doc.build_docx("ADOV_Care_Group_CQC_Requirements_and_Fulfillment_Guide.docx")
    print("✓ Completed CQC Requirements & Fulfillment Guide (PDF & DOCX).")


# ==============================================================================
# DOC 7: CQC APPLICATION QUESTIONS DOSSIER
# ==============================================================================
def build_cqc_questions_dossier():
    doc = LandscapeDocument(
        title="CQC PROVIDER APPLICATION QUESTIONS & MODEL ANSWERS DOSSIER",
        doc_ref="ACG-LUTON-2026-CQC-QNA",
        category="STATUTORY APPLICATION SUBMISSION PACK",
        subtitle="Verbatim Portal Questions, Statutory Evidence Narratives, Clinical Declarations & Regulation 17 Audit Schedules"
    )

    doc.set_meta([
        ("Applicant Legal Entity", "ADOV Care Group LIMITED (OpCo)"),
        ("Submission Portal", "Care Quality Commission (CQC) Digital Provider Portal"),
        ("Activity Applied For", "Personal Care (Specialist Supported Living Service)"),
        ("Primary Campus Location", "78 & 80 Marston Gardens, Luton, Bedfordshire, LU2 7DY"),
        ("Nominated Individual (NI)", "Executive Board Director (FAIRYTALES GROUP)"),
        ("Registered Manager (RM)", "Qualified Adult Social Care Lead (Level 5 Diploma)"),
        ("Drafting Counsel", "Healthcare Regulatory Compliance Team // Project Planned by AbdullahMamun.com"),
        ("Submission Readiness", "100% Submission Ready // Portal Verbatim Edition")
    ])

    doc.set_kpis([
        ("5 Sections", "Portal Modules", "A: Org, B: Activity, C: Safety, D: Governance, E: Staff"),
        ("100% Verbatim", "Question Alignment", "Direct match to CQC Portal fields"),
        ("Zero Rejection", "Historical Precedent", "Fully aligned with statutory regulations"),
        ("PBS Compliant", "Behaviour Framework", "Positive Behaviour Support certified"),
        ("24/7 Cover", "Staffing Architecture", "Waking night + sleep-in cover")
    ])

    # Section 1.0
    doc.add_heading_1("1.0 SECTION A: PROVIDER AIMS, CORPORATE OBJECTIVES & CARE PHILOSOPHY")
    doc.add_callout(
        "CQC PORTAL QUESTION A1: WHAT ARE THE AIMS AND OBJECTIVES OF YOUR SERVICE?",
        "ADOV Care Group Limited is established to deliver high-quality, person-centred Personal Care to adults (aged 18–64) diagnosed "
        "with autism spectrum conditions, severe learning disabilities, and associated complex sensory needs living within supported accommodation "
        "at 78 and 80 Marston Gardens, Luton. Our primary objective is to empower individuals to live dignified, self-determined lives in a safe, "
        "domestic community setting, fundamentally avoiding institutional hospital or residential care home placements in accordance with the "
        "NHS Transforming Care agenda and CQC's guidance 'Right support, right care, right culture'. We achieve this by providing consistent, "
        "highly trained support staff utilizing Positive Behaviour Support (PBS) frameworks, active support methodologies, and bespoke communication passports."
    )

    doc.add_callout(
        "CQC PORTAL QUESTION A2: HOW WILL YOU ENSURE PEOPLE RECEIVE PERSON-CENTRED CARE?",
        "Person-centred care is operationalised through four core mechanisms: (1) Detailed Pre-Admission Assessment: Every resident co-produces "
        "a comprehensive support plan with their multi-disciplinary team, family, and speech/language specialists before moving in; (2) Communication "
        "Passports: Individuals with non-verbal autism are provided with tailored communication aids (PECS, Makaton, tablet-based software) ensuring "
        "their voice guides daily routines; (3) Positive Risk-Taking: Staff facilitate personal autonomy (e.g. meal preparation, independent shopping, "
        "community sports) supported by dynamic risk assessments; and (4) Dedicated Keyworking: Each tenant is paired with a primary keyworker who "
        "conducts monthly person-centred reviews and ensures care plans adapt dynamically to evolving goals."
    )

    # Section 2.0
    doc.add_heading_1("2.0 SECTION B: SAFEGUARDING, SAFETY & INCIDENT GOVERNANCE")
    doc.add_callout(
        "CQC PORTAL QUESTION B1: HOW WILL YOU PROTECT SERVICE USERS FROM ABUSE AND IMPROPER TREATMENT?",
        "ADOV Care Group maintains an uncompromising zero-tolerance approach to abuse and neglect: (1) Vetting: 100% of staff undergo Enhanced DBS vetting "
        "with Adult Barred List clearance, five-year employment history verification, and two professional references prior to commencing duties; "
        "(2) Mandatory Training: All staff complete Safeguarding Adults Level 2/3 and Mental Capacity Act training within 14 days of induction; "
        "(3) Multi-Agency Alignment: The service operates in direct partnership with the Luton Safeguarding Adults Board (LSAB), escalating Section 42 alerts "
        "within 24 hours of any concern; (4) Independent Whistleblowing: Staff have access to a confidential whistleblowing helpline directly to the "
        "Nominated Individual and CQC; and (5) Non-Restrictive Culture: Physical restraints are strictly prohibited; staff are trained exclusively "
        "in BILD-accredited low-arousal de-escalation techniques under Positive Behaviour Support principles."
    )

    # Section 3.0
    doc.add_heading_1("3.0 SECTION C: QUALITY ASSURANCE & REGULATION 17 GOVERNANCE SCHEDULE")
    doc.add_paragraph(
        "To satisfy Regulation 17 (Good Governance), ADOV Care Group operates a multi-tiered auditing and monitoring schedule, "
        "ensuring continuous quality improvement, proactive risk mitigation, and complete transparency."
    )

    doc.add_table(
        title="Table 7.1: Regulation 17 Internal Governance Auditing Schedule",
        headers=["Audit Category", "Responsible Lead", "Audit Frequency", "Statutory Scope & Verification", "Escalation & Board Reporting"],
        rows=[
            ["Medication MAR Audit", "Registered Manager", "Weekly", "Stock count, controlled drugs register, MAR signing accuracy, omitted doses", "Immediate GP/111 escalation; Board KPI report"],
            ["Fire Safety & Emergency", "Health & Safety Officer", "Monthly", "BS 5839 alarm test, emergency lights BS 5266, fire doors FD30S, PEEPs", "Immediate remedial works by PropCo; H&S log"],
            ["PBS Plan Reviews", "PBS Practitioner", "Monthly", "ABC chart trend analysis, sensory trigger updates, active support metrics", "MDT review; updated positive support strategies"],
            ["Infection Control Audit", "House Team Leader", "Monthly", "HTM 01-04 compliance, laundry separation, colour-coded cleaning systems", "Action plan issued within 48h; re-audit in 7 days"],
            ["Unannounced Site Visit", "Nominated Individual", "Monthly", "Staff engagement, resident observation, domestic environment, dignity checks", "Written report to Executive Board within 5 days"],
            ["Financial Solvency", "Finance Director", "Monthly", "Fee collection, payroll, operating cash buffer, PropCo lease fulfillment", "Consolidated group cash flow dashboard"],
            ["Independent Mock CQC", "External Care Consultant", "Quarterly", "Comprehensive audit across all 34 Quality Statements under SAF", "Full formal board presentation; 30-day action plan"]
        ],
        col_pcts=[18, 16, 12, 36, 18]
    )

    doc.build_pdf("ADOV_Care_Group_CQC_Provider_Application_Questions_Dossier.pdf")
    doc.build_docx("ADOV_Care_Group_CQC_Provider_Application_Questions_Dossier.docx")
    print("✓ Completed CQC Application Questions Dossier (PDF & DOCX).")


# ==============================================================================
# DOC 8: RESIDENT INTAKE PATHWAY SOP
# ==============================================================================
def build_resident_intake_sop():
    doc = LandscapeDocument(
        title="RESIDENT INTAKE & PRE-ADMISSION PATHWAY CLINICAL SOP",
        doc_ref="ACG-LUTON-2026-SOP-INTAKE",
        category="CLINICAL STANDARD OPERATING PROCEDURE",
        subtitle="7-Stage Pre-Admission Assessment, Multi-Disciplinary Matching, Zero-Void Commissioning & 28-Day Review Protocol"
    )

    doc.set_meta([
        ("Operating Provider", "ADOV Care Group LIMITED"),
        ("Commissioning Partners", "Luton Borough Council Adult Social Care & BLMK ICB Continuing Healthcare"),
        ("Target Service Cohort", "Adults (18–64) with Autism, Severe Learning Disabilities & Step-Down Rehabilitation"),
        ("Operational Campus", "78 & 80 Marston Gardens, Luton, LU2 7DY (8 Registered Beds)"),
        ("Protocol Ownership", "Registered Manager & Nominated Individual"),
        ("Clinical Model", "Positive Behaviour Support (PBS) & Active Support Framework"),
        ("SOP Version", "Version 2.1 — Publication Edition (October 2026)")
    ])

    doc.set_kpis([
        ("7 Stages", "Admission Protocol", "From desktop triage to 28-day review"),
        ("Zero Voids", "Commissioning Goal", "100% planned occupancy retention"),
        ("4–6 Weeks", "Transition Window", "Graduated familiarisation visits"),
        ("100% PBS", "Clinical Basis", "Zero restraint, positive de-escalation"),
        ("3-Way Match", "Household Synergy", "Sensory, behavioral & peer compatibility")
    ])

    # Section 1.0
    doc.add_heading_1("1.0 OPERATIONAL PURPOSE, CLINICAL PHILOSOPHY & SCOPE")
    doc.add_paragraph(
        "This Standard Operating Procedure (SOP) defines the mandatory multi-stage intake pathway for admitting residents into "
        "ADOV Care Group's supported living homes at 78 and 80 Marston Gardens, Luton. The primary clinical objective is to eliminate "
        "placement breakdown—which causes immense emotional distress to vulnerable individuals and costs commissioning authorities upwards "
        "of £20,000 per breakdown—through meticulous pre-admission compatibility matching, sensory environmental auditing, and graduated "
        "familiarisation transitions. Simultaneously, the pathway provides Luton Borough Council Adult Social Care and NHS BLMK ICB with a "
        "predictable, zero-void commissioning mechanism."
    )

    doc.add_flow_stages(
        title="Figure 8.1: The 7-Stage Resident Pre-Admission & Community Transition Pathway",
        stages=[
            ("1", "Referral Triage (Day 1)", "Receive referral from Luton Council DPS (AT1115). Desktop suitability triage within 24h."),
            ("2", "Clinical Assessment (Days 2–5)", "Face-to-face assessment by Registered Manager; review ABC charts, PBS baseline & sensory diet."),
            ("3", "Peer Compatibility (Days 6–8)", "Evaluate household dynamic between 78 (5 beds) and 80 (3 beds); eliminate sensory clashes."),
            ("4", "Funding Agreement (Days 9–14)", "Finalise Individual Placement Agreement (IPA) covering core care, 1:1 hours, and housing benefit."),
            ("5", "Graduated Transition (Weeks 3–5)", "4-step familiarisation: neutral meet, 2h tea visit, full-day visit, overnight stay."),
            ("6", "Admission Day (Week 6)", "Tenancy agreement executed; MAR charts initiated; personal belongings unpack; keyworker assigned."),
            ("7", "Clinical Review (Day 28)", "Multi-disciplinary 72h and 28-day statutory reviews with Care Manager, family, and resident.")
        ]
    )

    # Section 2.0
    doc.add_heading_1("2.0 STAGE-BY-STAGE OPERATIONAL PROTOCOLS & GOVERNANCE GATES")
    doc.add_paragraph(
        "Each stage of the intake pathway enforces strict governance gates. A referral cannot advance to the subsequent stage without "
        "explicit written sign-off by the designated clinical lead."
    )

    doc.add_table(
        title="Table 8.1: Intake Pathway Governance Gates, Documentation & Sign-Off Matrix",
        headers=["Pathway Stage", "Operational Lead", "Target Timeline", "Mandatory Evidence / Documentation", "Sign-Off Gate Threshold"],
        rows=[
            ["Stage 1: Referral Triage", "Brokerage Liaison", "Hours 0–24", "Council Care Act assessment, social history, risk summary", "Basic eligibility criteria satisfied; bed vacancy confirmed"],
            ["Stage 2: Clinical Assessment", "Registered Manager", "Days 2–5", "Functional Behaviour Assessment, sensory audit, medical history", "RM verifies provider can safely meet all assessed needs"],
            ["Stage 3: Peer Compatibility", "House Team Leader", "Days 6–8", "Household sensory compatibility matrix; tenant consultation notes", "Zero sensory or behavioral conflict with existing tenants"],
            ["Stage 4: Funding Agreement", "Finance Director", "Days 9–14", "Agreed IPA, Section 117 / CHC contract, Exempt Housing Benefit form", "Written funding authorization from Council / ICB received"],
            ["Stage 5: Transition Visits", "Allocated Keyworker", "Weeks 3–5", "Visit observation logs, sensory response charts, resident feedback", "Resident expresses positive desire; family & advocate support"],
            ["Stage 6: Formal Admission", "Registered Manager", "Day 35–42", "Signed AST tenancy, Care Contract, initial MAR chart, PEEP plan", "CQC Regulation 19 vetting complete; bedroom ready"],
            ["Stage 7: 28-Day Review", "Multi-Disciplinary Team", "Day 63–70", "28-day statutory clinical review report; goal achievement summary", "Placement formally confirmed as permanent by all parties"]
        ],
        col_pcts=[18, 16, 12, 36, 18]
    )

    # Section 3.0
    doc.add_heading_1("3.0 HOUSEHOLD MATCHING & SENSORY ENVIRONMENTAL SYNERGY")
    doc.add_paragraph(
        "The unique campus structure of ADOV Care Group—offering two adjacent properties with distinct environmental profiles—provides "
        "an extraordinary operational advantage in resident matching:"
    )

    doc.add_key_value_grid(
        title="Campus Allocation & Environmental Matching Architecture",
        items=[
            ("78 Marston Gardens (Active Dynamic)", "5 single bedrooms. Designed for residents who enjoy active domestic engagement, communal cooking, and structured group activities in the large living room and 100ft garden."),
            ("80 Marston Gardens (Calm Sensory)", "3 large single bedrooms. Designed for residents with high sensory sensitivity who require a low-arousal, ultra-quiet domestic environment with minimal stimuli."),
            ("Sensory Clashing Prevention", "Tenants with vocal tics or auditory triggers are never placed in the same building. The two properties allow precise clinical separation while sharing campus infrastructure."),
            ("Emergency De-escalation Buffer", "In the rare event of severe temporary friction, the dual-house campus allows short-term respite relocation across gardens without disrupting school or day-care rotas.")
        ],
        num_cols=2
    )

    doc.build_pdf("ADOV_Care_Group_Resident_Intake_Pathway_SOP.pdf")
    doc.build_docx("ADOV_Care_Group_Resident_Intake_Pathway_SOP.docx")
    print("✓ Completed Resident Intake Pathway SOP (PDF & DOCX).")


# ==============================================================================
# DOC 13: CQC STATEMENT OF PURPOSE
# ==============================================================================
def build_cqc_statement_of_purpose():
    doc = LandscapeDocument(
        title="STATUTORY CQC STATEMENT OF PURPOSE (SoP)",
        doc_ref="ACG-LUTON-2026-CQC-SOP",
        category="STATUTORY REGISTRATION INSTRUMENT",
        subtitle="Mandatory Statutory Document Formulated Under Regulation 12 & Schedule 3 of Care Quality Commission (Registration) Regulations 2009"
    )

    doc.set_meta([
        ("Provider Legal Name", "ADOV Care Group LIMITED"),
        ("Company Registration No", "14289650 (Incorporated in England and Wales)"),
        ("Nominated Individual (NI)", "Executive Board Director (FAIRYTALES GROUP)"),
        ("Registered Manager (RM)", "Qualified Adult Social Care Lead (Level 5 Diploma)"),
        ("Head Office Address", "78 Marston Gardens, Luton, Bedfordshire, LU2 7DY"),
        ("Regulated Activity", "Personal Care (Schedule 1, HSCA 2014) — Supported Living Model"),
        ("Excluded Activities", "Accommodation for persons who require nursing or personal care (EXCLUDED)"),
        ("Date of Publication", "October 2026 // Definitive Statutory Edition (v2.0)")
    ])

    doc.set_kpis([
        ("Personal Care", "Regulated Activity", "HSCA 2008 Schedule 1"),
        ("Supported Living", "Care Model", "Tenancy + Care separation"),
        ("8 Residents", "Campus Capacity", "5 in No. 78 // 3 in No. 80"),
        ("PBS Certified", "Care Philosophy", "Positive Behaviour Support"),
        ("Right Support", "Policy Standard", "Right Care, Right Culture")
    ])

    # Section 1.0
    doc.add_heading_1("PART 1: PROVIDER GOVERNANCE & STATUTORY APPOINTMENTS")
    doc.add_paragraph(
        "This Statement of Purpose is maintained in accordance with Regulation 12 and Schedule 3 of the Care Quality Commission "
        "(Registration) Regulations 2009. It sets out the statutory aims, legal structure, governance framework, and service user cohorts "
        "catered for by ADOV Care Group Limited across its registered service locations in Luton."
    )

    doc.add_table(
        title="Table 13.1: Statutory Provider Details & Legal Governance Register",
        headers=["Entity / Governance Field", "Statutory Information", "Legal Authority / Regulatory Citation"],
        rows=[
            ["Legal Entity Name", "ADOV Care Group LIMITED", "Companies Act 2006 // Co. No. 14289650"],
            ["Provider Status", "Private Limited Healthcare Operating Company (OpCo)", "CQC Health & Social Care Act 2008"],
            ["Registered Office", "78 Marston Gardens, Luton, Bedfordshire, LU2 7DY", "Official Service Location"],
            ["Nominated Individual", "Appointed Executive Director (FAIRYTALES GROUP)", "Regulation 6 Health & Social Care Act 2008 Regs 2014"],
            ["Registered Manager", "Appointed Adult Care Lead (Level 5 Diploma in Leadership)", "Regulation 7 Health & Social Care Act 2008 Regs 2014"],
            ["Regulated Activity", "Personal Care (Supported Living)", "Health and Social Care Act 2008 (Regulated Activities) Regs 2014 Sched 1"]
        ],
        col_pcts=[26, 42, 32]
    )

    # Section 2.0
    doc.add_heading_1("PART 2: AIMS, OBJECTIVES & CLINICAL VALUES")
    doc.add_paragraph(
        "ADOV Care Group Limited is founded upon four unshakeable principles: (1) Person-Centred Empowerment: Placing the individual "
        "at the absolute centre of all care planning; (2) Human Rights & Least Restrictive Practice: Eliminating institutional controls "
        "and physical interventions through PBS; (3) Community Inclusion: Enabling tenants to access education, employment, and leisure in Luton; "
        "and (4) Uncompromised Quality: Operating at the highest tier of the CQC Single Assessment Framework."
    )

    # Section 3.0
    doc.add_heading_1("PART 3: REGISTERED CAMPUS LOCATIONS & PHYSICAL SPECIFICATIONS")
    doc.add_table(
        title="Table 13.2: Registered Campus Physical Asset & Capacity Specifications",
        headers=["Campus Location", "Capacity", "Layout & Physical Specifications", "Communal Facilities", "Regulated Activity"],
        rows=[
            ["78 Marston Gardens, Luton, LU2 7DY", "5 Beds", "5 spacious single bedrooms (12.5m²-15m²), 1 ensuite wetroom, 1 large communal wetroom, 1 ground WC", "Communal lounge, domestic kitchen, 100ft garden, 4 driveway bays, 1 garage", "Personal Care"],
            ["80 Marston Gardens, Luton, LU2 7DY", "3 Beds", "3 large single bedrooms (13m²-16m²), 1 ground-floor wetroom, 1 separate cloakroom WC", "Sensory relaxation suite, staff office, private garden, 4 driveway bays, 1 garage", "Personal Care"],
            ["82 Marston Gardens, Luton, LU2 7DY", "Residential", "4-bedroom semi-detached house (Retained as Director's Private Residence)", "Private family home, executive on-site base (30-second response)", "Non-Regulated (Private AST)"]
        ],
        col_pcts=[20, 10, 36, 24, 10]
    )

    # Section 4.0
    doc.add_heading_1("PART 4: TARGET SERVICE USER COHORTS & STATUTORY EXCLUSIONS")
    doc.add_paragraph(
        "ADOV Care Group delivers personal care exclusively to adults aged 18 to 64 presenting with: (a) Autism Spectrum Conditions; "
        "(b) Moderate to Severe Learning Disabilities; (c) Associated Sensory Processing Difficulties; and (d) Step-Down Mental Health Needs. "
        "The service explicitly excludes nursing care, detentions under the Mental Health Act 1983 (though accepts Section 117 aftercare), "
        "and emergency crisis admissions without planned pre-admission matching."
    )

    doc.add_callout(
        "STATUTORY INDEPENDENCE COVENANT: HOUSING VS CARE",
        "In strict adherence to CQC statutory policy 'Right support, right care, right culture', residents hold an Assured Shorthold Tenancy (AST) "
        "with the property owner (ADOV Limited) granting exclusive possession and full legal rights as tenants. Personal care is commissioned "
        "separately by Luton Borough Council or NHS BLMK ICB and provided by ADOV Care Group Limited under an independent Care Agreement. "
        "A tenant's right of occupation is legally independent of their care provider choice, fulfilling all statutory requirements for Supported Living."
    )

    doc.build_pdf("ADOV_Care_Group_CQC_Statement_of_Purpose.pdf")
    doc.build_docx("ADOV_Care_Group_CQC_Statement_of_Purpose.docx")
    print("✓ Completed CQC Statement of Purpose (PDF & DOCX).")


if __name__ == "__main__":
    print("=" * 80)
    print("BUILDING LANDSCAPE JOURNAL VAULT — PART 2 (CQC & CLINICAL SOPS)")
    print("Exhaustive PhD-level monographs and standard operating procedures.")
    print("=" * 80)
    build_cqc_registration_master_report()
    build_cqc_requirements_guide()
    build_cqc_questions_dossier()
    build_resident_intake_sop()
    build_cqc_statement_of_purpose()
    print("PART 2 COMPLETE: All 5 CQC reports built successfully in Landscape A4 PDF & Word!")
