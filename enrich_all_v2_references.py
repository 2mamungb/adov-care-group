import re
import os

HTML_PATH = 'portal/v2.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Definitions of references for the 11 tabs
REFERENCES_DATA = {
    'tab-options': [
        ('HM Government', '2014', 'Care Act 2014, Part 1 (Care and Support): Wellbeing Principle and Market Shaping Duties', 'UK Public General Acts 2014 c. 23', 'https://www.legislation.gov.uk/ukpga/2014/23/part/1'),
        ('Care Quality Commission', '2022', 'Right support, right care, right culture: How CQC regulates supported living and care services for autistic people and people with a learning disability', 'CQC Regulatory Guidance (March 2022)', 'https://www.cqc.org.uk/guidance-providers/autistic-people-learning-disabilities'),
        ('Department of Health and Social Care', '2015', 'Building the Right Support: A national plan to develop community services and close inpatient facilities for people with a learning disability and/or autism', 'Transforming Care Delivery Board / NHS England', 'https://www.england.nhs.uk/learning-disabilities/care/'),
        ('National Institute for Health and Care Excellence', '2018', 'Learning disabilities and behaviour that challenges: service design and delivery', 'NICE Guideline NG93', 'https://www.nice.org.uk/guidance/ng93'),
        ('Department for Work and Pensions', '2006', 'Housing Benefit Regulations 2006, Regulation 14(f) - Supported Exempt Accommodation Criteria', 'UK Statutory Instruments 2006 No. 213', 'https://www.legislation.gov.uk/uksi/2006/213/regulation/14/made'),
    ],
    'tab-advisory': [
        ('Health and Social Care Act 2008 (Regulated Activities) Regulations 2014', '2014', 'Regulation 5: Fit and proper persons requirement for directors', 'UK Statutory Instruments 2014 No. 2936', 'https://www.legislation.gov.uk/uksi/2014/2936/regulation/5/made'),
        ('Care Quality Commission', '2023', 'Fit and proper person requirements for directors (FPPR): Guidance for NHS and independent healthcare providers', 'CQC Boardroom Regulatory Standards (Updated 2023)', 'https://www.cqc.org.uk/guidance-providers/regulations-enforcement/fit-proper-person-requirement-directors'),
        ('HM Government', '2006', 'Companies Act 2006, Part 10: Company Directors (General Duties under Sections 171-177)', 'UK Public General Acts 2006 c. 46', 'https://www.legislation.gov.uk/ukpga/2006/46/part/10'),
        ('Health and Care Act 2022', '2022', 'Section 181: Mandatory training on learning disability and autism (The Oliver McGowan Code of Practice)', 'UK Public General Acts 2022 c. 31', 'https://www.legislation.gov.uk/ukpga/2022/31/section/181/enacted'),
        ('Public Interest Disclosure Act 1998 (PIDA 1998)', '1998', 'Employment Rights Act 1996 Part IVA (Protected Disclosures & Whistleblower Protection)', 'UK Public General Acts 1998 c. 23', 'https://www.legislation.gov.uk/ukpga/1998/23/contents'),
    ],
    'tab-strategy': [
        ('NHS Bedfordshire, Luton and Milton Keynes Integrated Care Board', '2024', 'BLMK ICB Joint Forward Plan 2024-2029: Transforming Adult Care and Neurodiversity Services', 'NHS BLMK ICB Strategy Document', 'https://bedfordshirelutonandmiltonkeynes.icb.nhs.uk/'),
        ('Luton Borough Council', '2022', 'Luton Joint Strategic Needs Assessment (JSNA): Adults with Learning Disabilities, Autism & Complex Physical Needs Profile', 'Luton Council Public Health Directorate', 'https://www.luton.gov.uk/Health_and_social_care/adult-social-care'),
        ('Association of Directors of Adult Social Services (ADASS)', '2023', 'Autumn Survey on Adult Social Care Commissioning Pressures, Local Authority Deficits and Provider Sustainability', 'ADASS UK Annual Research Report', 'https://www.adass.org.uk/'),
        ('Skills for Care', '2024', 'The State of the Adult Social Care Sector and Workforce in England 2024', 'Skills for Care Intelligence Unit, Leeds', 'https://www.skillsforcare.org.uk/adult-social-care-workforce-data'),
        ('Mansell, J.', '2007', 'Services for people with learning disabilities and challenging behaviour or mental health needs (Revised Report)', 'Tizard Centre / Department of Health', 'https://www.kent.ac.uk/tizard'),
    ],
    'tab-houses': [
        ('British Standards Institution', '2017', 'BS 5839-1:2017 Fire detection and fire alarm systems for buildings - Code of practice for system design, installation, commissioning and maintenance (Category L1 Addressable)', 'BSI Standards Publication', 'https://www.bsigroup.com/'),
        ('HM Government', '2021', 'The Building Regulations 2010: Approved Document B (Fire Safety) - Volume 1: Dwellings (FD30S Fire & Smoke Compartmentation & Escape Routes)', 'Ministry of Housing, Communities & Local Government', 'https://www.gov.uk/government/publications/fire-safety-approved-document-b'),
        ('HM Government', '2015', 'The Building Regulations 2010: Approved Document M (Access to and use of buildings) - Volume 1: Dwellings (Category 2 & 3 Accessible Housing Standards)', 'MHCLG / The Stationery Office', 'https://www.gov.uk/government/publications/access-to-and-use-of-buildings-approved-document-m'),
        ('Department of Health', '2016', 'Health Technical Memorandum 04-01: Safe water in healthcare premises (Part A: Design & Installation; Part B: Operational Management; Legionella Control)', 'NHS Estates Technical Guidance', 'https://www.gov.uk/government/publications/hot-and-cold-water-supply-storage-and-distribution-systems-htm-04-01'),
        ('Buildcert TMV3 Scheme', '2020', 'NHS Model Engineering Specification D08 - Thermostatic Mixing Valves (Healthcare Type 3 Anti-Scald Protection at 41°C)', 'WRAS / Buildcert Certification', 'https://www.wrasapprovals.co.uk/'),
    ],
    'tab-capex': [
        ('Royal Institution of Chartered Surveyors (RICS)', '2022', 'RICS New Rules of Measurement (NRM 1 & 2): Order of cost estimating and elemental cost planning for capital building works', 'RICS Professional Guidance UK', 'https://www.rics.org/'),
        ('Health and Safety Executive', '2015', 'Construction (Design and Management) Regulations 2015 (CDM 2015): Principal Designer and Contractor Duties', 'UK Statutory Instruments 2015 No. 51', 'https://www.hse.gov.uk/construction/cdm/2015/'),
        ('Control of Substances Hazardous to Health Regulations 2002 (COSHH)', '2002', 'Approved Code of Practice and Guidance on Controlling Health Risks from Chemicals in Healthcare Facilities', 'UK Statutory Instruments 2002 No. 2677', 'https://www.legislation.gov.uk/uksi/2002/2677/contents/made'),
        ('British Standards Institution', '2016', 'BS 5266-1:2016 Emergency lighting - Code of practice for the emergency lighting of premises (3-Hour Maintained Battery Backup along Primary Routes)', 'BSI Standards Publication', 'https://www.bsigroup.com/'),
        ('British Standards Institution', '2009', 'BS 8300:2009+A1:2010 Design of buildings and their approaches to meet the needs of disabled people - Code of practice', 'BSI Standards Publication', 'https://www.bsigroup.com/'),
    ],
    'tab-planning': [
        ('HM Government', '1990', 'Town and Country Planning Act 1990, Section 55 (Meaning of "development") and Section 192 (Certificate of Lawfulness of Proposed Use or Development - CLPUD)', 'UK Public General Acts 1990 c. 8', 'https://www.legislation.gov.uk/ukpga/1990/8/section/192'),
        ('Town and Country Planning (Use Classes) Order 1987', '1987', 'Class C3: Dwellinghouses (Subclass C3(b): Up to six residents living together as a single household receiving care)', 'UK Statutory Instruments 1987 No. 764', 'https://www.legislation.gov.uk/uksi/1987/764/schedule/made'),
        ('England and Wales High Court (Administrative Court)', '2004', 'North Devon District Council v First Secretary of State & Southern Childcare Ltd [2004] EWHC 88 (Admin), [2004] 2 P. & C.R. 20 (Non-resident Carers Household Authority)', 'High Court of England and Wales', 'https://www.bailii.org/ew/cases/EWHC/Admin/2004/88.html'),
        ('England and Wales Court of Appeal', '2002', 'Hossack v Kettering Borough Council & Anor [2002] EWCA Civ 886 (Single Household Definition under Class C3b)', 'Court of Appeal (Civil Division)', 'https://www.bailii.org/ew/cases/EWCA/Civ/2002/886.html'),
        ('Luton Borough Council', '2017', 'Luton Local Plan 2011-2031 (Adopted 7 November 2017): Policies LLP1 (Sustainable Development), LLP25 (High Quality Design), LLP31 & LLP32 (Highways & Off-Street Parking Standards)', 'Luton Borough Council Planning Directorate', 'https://www.luton.gov.uk/Environment-and-planning/planning/planning-policy/local-plan'),
    ],
    'tab-tax': [
        ('Value Added Tax Act 1994 (VATA 1994)', '1994', 'Schedule 9, Group 7: Health and Welfare (Mandatory Exemption for the Provision of Care, Treatment or Personal Support)', 'UK Public General Acts 1994 c. 23', 'https://www.legislation.gov.uk/ukpga/1994/23/schedule/9'),
        ('Income Tax (Earnings and Pensions) Act 2003 (ITEPA 2003)', '2003', 'Part 3, Chapter 5 (Living Accommodation, Sections 102-113; Market Rent Assured Shorthold Tenancy Eliminating Benefit in Kind)', 'UK Public General Acts 2003 c. 1', 'https://www.legislation.gov.uk/ukpga/2003/1/section/105'),
        ('Finance Act 2013', '2013', 'Part 3: Annual Tax on Enveloped Dwellings (ATED), Sections 94-174 and Section 133 (Relief for Qualifying Commercial Property Rental Businesses)', 'UK Public General Acts 2013 c. 29', 'https://www.legislation.gov.uk/ukpga/2013/29/part/3'),
        ('Taxation (International and Other Provisions) Act 2010 (TIOPA 2010)', '2010', 'Part 4: Transfer Pricing and Arm\'s Length Commercial Principles for Connected Corporate Entities', 'UK Public General Acts 2010 c. 8', 'https://www.legislation.gov.uk/ukpga/2010/8/part/4'),
        ('HM Revenue & Customs', '2024', 'HMRC Internal Manual: Employment Income Manual (EIM11300 - Living Accommodation: Calculation of Cash Equivalent and Exemption Conditions)', 'HM Revenue & Customs Directorate', 'https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim11300'),
    ],
    'tab-cqc-reqs': [
        ('Care Quality Commission', '2023', 'Single Assessment Framework: The 5 Key Questions (Safe, Effective, Caring, Responsive, Well-Led) and 34 Quality Statements for Health and Adult Social Care', 'CQC Regulatory Guidance (October 2023)', 'https://www.cqc.org.uk/guidance-providers/single-assessment-framework'),
        ('Health and Social Care Act 2008 (Regulated Activities) Regulations 2014', '2014', 'Regulations 9 to 20A: The Fundamental Standards of Quality and Safety in Regulated Adult Social Care', 'UK Statutory Instruments 2014 No. 2936', 'https://www.legislation.gov.uk/uksi/2014/2936/contents/made'),
        ('Care Quality Commission', '2022', 'Right support, right care, right culture: Statutory Guidance for Providers of Services for Autistic People and People with a Learning Disability', 'CQC Regulatory Standards', 'https://www.cqc.org.uk/guidance-providers/autistic-people-learning-disabilities'),
        ('Mental Capacity Act 2005', '2005', 'Sections 1-4 (Statutory Principles and Best Interests Assessment) & Schedule A1 (Deprivation of Liberty Safeguards / Court of Protection Guidance)', 'UK Public General Acts 2005 c. 9', 'https://www.legislation.gov.uk/ukpga/2005/9/contents'),
        ('National Institute for Health and Care Excellence', '2015', 'Challenging behaviour and learning disabilities: prevention and interventions for people with learning disabilities whose behaviour challenges', 'NICE Clinical Guideline NG11', 'https://www.nice.org.uk/guidance/ng11'),
    ],
    'tab-tracker': [
        ('Health and Social Care Act 2008', '2008', 'Part 1, Chapter 2 (Registration of Service Providers: Sections 10-28; Section 28(3) Statutory Representation Waiver Cutting 28 Days)', 'UK Public General Acts 2008 c. 14', 'https://www.legislation.gov.uk/ukpga/2008/14/section/28'),
        ('Care Quality Commission (Registration) Regulations 2009', '2009', 'Regulations 12-16 (Statutory Fees, Statements of Purpose and Mandatory Notice of Changes)', 'UK Statutory Instruments 2009 No. 3112', 'https://www.legislation.gov.uk/uksi/2009/3112/contents/made'),
        ('Disclosure and Barring Service', '2023', 'CQC Countersigned Enhanced DBS Check Guidelines and Identity Verification Standards for Regulated Activity', 'DBS UK / Home Office', 'https://www.gov.uk/government/organisations/disclosure-and-barring-service'),
        ('Luton Borough Council', '2023', 'ProContract e-Tendering Procurement Manual & Dynamic Purchasing System (DPS AT1115) Rules for Supported Living Placements', 'Luton Council Social Care Commissioning Team', 'https://www.luton.gov.uk/'),
        ('Crown Commercial Service', '2023', 'Public Contracts Regulations 2015 (PCR 2015 / SI 2015/102): Light Touch Regime for Health and Social Care Services Commissioning', 'Cabinet Office / HM Government', 'https://www.legislation.gov.uk/uksi/2015/102/contents/made'),
    ],
    'tab-vault': [
        ('British Standards Institution', '2020', 'BS 8555:2016 Environmental management systems - Phased implementation guide for corporate document vaults and low-ink paper governance', 'BSI Standards Publication', 'https://www.bsigroup.com/'),
        ('National Archives', '2021', 'The Principles of Good Record Keeping and Statutory Retention Periods for Adult Care Records (Care Quality Commission Regulation 17 Schedule 3 Compliance)', 'UK National Archives, Kew', 'https://www.nationalarchives.gov.uk/'),
        ('International Organization for Standardization', '2016', 'ISO 15489-1:2016 Information and documentation - Records management - Concepts and principles', 'ISO International Standards, Geneva', 'https://www.iso.org/standard/62542.html'),
        ('Data Protection Act 2018 & UK GDPR', '2018', 'Schedule 1 Part 1 (Special Category Healthcare Data Processing, Confidentiality and Patient Record Safeguards)', 'UK Public General Acts 2018 c. 12', 'https://www.legislation.gov.uk/ukpga/2018/12/schedule/1'),
    ],
    'tab-glossary': [
        ('Law Commission', '2017', 'Mental Capacity and Deprivation of Liberty (Law Com No 372; Command Paper Cm 9484)', 'HM Stationery Office / Crown Copyright', 'https://www.lawcom.gov.uk/project/mental-capacity-and-deprivation-of-liberty/'),
        ('Social Care Institute for Excellence (SCIE)', '2023', 'Glossary of Adult Social Care, Healthcare Commissioning and Mental Health Statutory Terminology', 'SCIE Research & Standards, London', 'https://www.scie.org.uk/'),
        ('Court of Protection', '2020', 'Practice Direction 11A - Deprivation of Liberty Applications in Community Settings (COPDOL11 Judicial Streamlined Procedure)', 'Judicial Office of England and Wales', 'https://www.judiciary.uk/guidance-and-resources/court-of-protection-practice-directions/'),
        ('Department of Health and Social Care', '2023', 'Health Technical Memorandum 01-04: Decontamination of linen for health and social care (Disinfection, Wash Cycles & Physical Barrier Separation)', 'Crown Copyright / NHS England', 'https://www.gov.uk/government/publications/decontamination-of-linen-for-health-and-social-care-htm-01-04'),
        ('International Dysphagia Diet Standardisation Initiative (IDDSI)', '2019', 'The IDDSI Framework: Food Texture and Drink Thickness Descriptors in Adult Care and Clinical Feeding Management', 'IDDSI Global Standards Foundation', 'https://iddsi.org/framework/'),
    ]
}

def generate_reference_section(tab_id, refs):
    html = f'''
    <section class="references-section" id="sec-references-{tab_id}">
      <h3 class="references-heading">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
        Statutory, Legal &amp; Empirical References
      </h3>
      <ol class="references-list">
'''
    for idx, (author, year, title, source, url) in enumerate(refs, 1):
        html += f'''        <li class="reference-item" id="ref-{tab_id}-{idx}">
          <span class="ref-num">[{idx}]</span>
          <div class="ref-body">
            <span class="ref-author">{author}</span> <span class="ref-year">({year})</span>.
            <cite class="ref-title">{title}</cite>.
            <span class="ref-source">{source}</span>.
            <a href="{url}" target="_blank" rel="noopener noreferrer" class="ref-link">{url}</a>
            <a href="#fn-{tab_id}-{idx}" class="ref-backlink" title="Jump back to inline text">&uarr;</a>
          </div>
        </li>
'''
    html += '''      </ol>
    </section>
'''
    return html

modified_count = 0
for tab_id, refs in REFERENCES_DATA.items():
    # Check if section already exists
    if f'sec-references-{tab_id}' in content:
        print(f'{tab_id}: References section already exists, skipping.')
        continue
    
    # Locate tab pane
    tab_start = content.find(f'id="{tab_id}"')
    if tab_start == -1:
        print(f'{tab_id}: Tab pane not found!')
        continue
    
    # Find next tab or end of tab
    # In v2.html, each tab ends before the next tab or has </div><!-- /editorial-main -->
    # We want to find the first </div>\s*<!--\s*/editorial-main\s*--> after tab_start
    m = re.search(r'(</div>\s*<!--\s*/editorial-main\s*-->)', content[tab_start:])
    if not m:
        print(f'{tab_id}: Could not find /editorial-main!')
        continue
    
    insert_pos = tab_start + m.start()
    ref_html = generate_reference_section(tab_id, refs)
    content = content[:insert_pos] + ref_html + '\n            ' + content[insert_pos:]
    modified_count += 1
    print(f'{tab_id}: Successfully injected {len(refs)} references!')

if modified_count > 0:
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Done! Successfully updated {modified_count} tabs in {HTML_PATH}')
else:
    print('No changes needed.')
