import re

HTML_PATH = 'portal/v2.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Tab footnote mappings: (tab_id, [(target_pattern, ref_num)])
FOOTNOTE_MAP = {
    'tab-options': [
        (r'\bCare Act 2014\b', 1),
        (r'\bRight support, right care, right culture\b', 2),
        (r'\bTransforming Care\b', 3),
        (r'\bNG93\b', 4),
        (r'\bExempt Accommodation\b|\bRegulation 14\(f\)\b', 5),
    ],
    'tab-advisory': [
        (r'\bRegulation 5\b', 1),
        (r'\bFit and proper persons?\b', 2),
        (r'\bCompanies Act 2006\b', 3),
        (r'\bOliver McGowan\b', 4),
        (r'\bWhistleblowing\b|\bPIDA 1998\b', 5),
    ],
    'tab-strategy': [
        (r'\bBLMK ICB\b', 1),
        (r'\bJSNA\b|\bJoint Strategic Needs Assessment\b', 2),
        (r'\bADASS\b', 3),
        (r'\bSkills for Care\b', 4),
        (r'\bMansell\b', 5),
    ],
    'tab-houses': [
        (r'\bBS 5839\b|\bCategory L1\b', 1),
        (r'\bApproved Document B\b|\bFD30S\b', 2),
        (r'\bApproved Document M\b', 3),
        (r'\bHTM 04-01\b', 4),
        (r'\bTMV3\b', 5),
    ],
    'tab-capex': [
        (r'\bRICS\b|\bNRM\b', 1),
        (r'\bCDM 2015\b|\bConstruction \(Design and Management\)\b', 2),
        (r'\bCOSHH\b', 3),
        (r'\bBS 5266\b|\b3-hour emergency lighting\b', 4),
        (r'\bBS 8300\b', 5),
    ],
    'tab-planning': [
        (r'\bSection 192\b|\bCLPUD\b', 1),
        (r'\bClass C3\(b\)\b|\bC3\(b\)\b', 2),
        (r'\bNorth Devon\b', 3),
        (r'\bHossack\b', 4),
        (r'\bLuton Local Plan\b|\bLLP1\b', 5),
    ],
    'tab-tax': [
        (r'\bSchedule 9, Group 7\b|\bVAT exempt\b|\bVAT exemption\b', 1),
        (r'\bBenefit in Kind\b|\bSection 105\b', 2),
        (r'\bATED\b', 3),
        (r'\barm\'s length\b|\bTIOPA\b', 4),
        (r'\bEIM11300\b|\bHMRC Internal Manual\b', 5),
    ],
    'tab-cqc-reqs': [
        (r'\bSingle Assessment Framework\b', 1),
        (r'\bFundamental Standards\b|\bRegulated Activities\b', 2),
        (r'\bRight support, right care, right culture\b', 3),
        (r'\bMental Capacity Act\b|\bDoLS\b', 4),
        (r'\bNICE Clinical Guideline\b|\bNG11\b', 5),
    ],
    'tab-tracker': [
        (r'\bSection 28\(3\)\b', 1),
        (r'\bRegistration Regulations 2009\b', 2),
        (r'\bEnhanced DBS\b', 3),
        (r'\bAT1115\b|\bDynamic Purchasing System\b', 4),
        (r'\bPublic Contracts Regulations\b|\bLight Touch Regime\b', 5),
    ],
}

total_inserted = 0

for tab_id, mappings in FOOTNOTE_MAP.items():
    tab_start_tag = f'id="{tab_id}"'
    start_pos = content.find(tab_start_tag)
    if start_pos == -1:
        continue
    
    # Find end of tab (before next tab pane or section)
    ref_sec_tag = f'id="sec-references-{tab_id}"'
    end_pos = content.find(ref_sec_tag, start_pos)
    if end_pos == -1:
        end_pos = content.find('class="tab-pane', start_pos + len(tab_start_tag))
    if end_pos == -1:
        end_pos = len(content)
        
    tab_html = content[start_pos:end_pos]
    
    for pattern, ref_num in mappings:
        fn_tag = f'id="fn-{tab_id}-{ref_num}"'
        if fn_tag in tab_html:
            continue # already present
            
        # Match only inside text (not inside HTML tags or attributes)
        # We can find matches that are outside `<...>`
        matches = list(re.finditer(pattern, tab_html, re.IGNORECASE))
        if not matches:
            continue
            
        # Pick first match that is not inside an HTML tag
        for m in matches:
            m_start, m_end = m.span()
            # check if inside tag: count '<' and '>' before m_start
            before_text = tab_html[:m_start]
            last_open = before_text.rfind('<')
            last_close = before_text.rfind('>')
            if last_open > last_close:
                # Inside a tag attribute, skip
                continue
                
            # Found good match!
            matched_str = m.group(0)
            replacement = f'{matched_str} <a href="#ref-{tab_id}-{ref_num}" id="fn-{tab_id}-{ref_num}" class="footnote-ref">[{ref_num}]</a>'
            tab_html = tab_html[:m_start] + replacement + tab_html[m_end:]
            total_inserted += 1
            print(f'{tab_id}: Inserted footnote [{ref_num}] for "{matched_str}"')
            break
            
    content = content[:start_pos] + tab_html + content[end_pos:]

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done! Successfully inserted {total_inserted} inline footnote links.')
