import re
import os
from html.parser import HTMLParser

print("Starting V 2.1 Reader-Friendly Layout Generator...")

# 1. Load original index.html
with open('portal/index.html', 'r', encoding='utf-8') as f:
    source_html = f.read()

# Verify that all 6 diagram files and photo exist
diagram_files = [
    'portal/assets/diagrams/diagram_campus_masterplan.svg',
    'portal/assets/diagrams/diagram_corporate_structure.svg',
    'portal/assets/diagrams/diagram_cqc_roadmap.svg',
    'portal/assets/diagrams/diagram_4options_mcda.svg',
    'portal/assets/diagrams/diagram_financial_waterfall.svg',
    'portal/assets/diagrams/diagram_intake_pathway.svg',
    'portal/assets/images/marston_gardens_campus.jpg'
]

for df in diagram_files:
    if os.path.exists(df):
        print(f"  ✓ Found visual asset: {df}")
    else:
        print(f"  ✗ WARNING: Visual asset missing: {df}")

# Define the HTML snippet for each visual asset
DIAGRAM_SNIPPETS = {
    "campus": """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-blue">Architectural Blueprint</span>
          <span class="visual-diagram-title">78 &amp; 80 Marston Gardens // 8-Bed Unified Specialist Campus</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/diagram_campus_masterplan.svg" alt="Campus Masterplan Blueprint" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Campus Topology:</strong> 78 (5 Suites + Commercial Kitchen + Activity Hall), 80 (3 Suites + Sensory Lounge + Staff Office &amp; Sleep-in), 8 off-street parking spaces (4 on each flank), and shared 100ft therapeutic rear sensory gardens.
        </div>
      </div>
    """,
    "photo": """
      <div class="visual-diagram-card visual-photo-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-green">Site Photographic Survey</span>
          <span class="visual-diagram-title">78 &amp; 80 Marston Gardens, Luton (LU2 7DY) — Freehold Properties</span>
        </div>
        <div class="visual-photo-wrap">
          <img src="assets/images/marston_gardens_campus.jpg" alt="78 &amp; 80 Marston Gardens Campus Photo" class="visual-photo-img" loading="lazy">
          <div class="photo-overlay-tags">
            <div class="photo-tag tag-left">
              <span class="tag-house">80 Marston Gardens</span>
              <span class="tag-meta">3 Suites • Sensory Hub • Staff Office</span>
            </div>
            <div class="photo-tag tag-drive-left">
              <span class="tag-house">Flank Drive A</span>
              <span class="tag-meta">4 Off-Street Cars</span>
            </div>
            <div class="photo-tag tag-right">
              <span class="tag-house">78 Marston Gardens</span>
              <span class="tag-meta">5 Suites • Comm. Kitchen • Dining Hall</span>
            </div>
            <div class="photo-tag tag-drive-right">
              <span class="tag-house">Flank Drive B</span>
              <span class="tag-meta">4 Off-Street Cars</span>
            </div>
          </div>
        </div>
        <div class="visual-diagram-caption">
          <strong>Survey Verification:</strong> Showing Left Semi-Detached House (80), Right Semi-Detached House (78), independent side vehicular access driveways (8 total parking spaces satisfying Luton Council LLP32 highways policy), and rear garden access gates.
        </div>
      </div>
    """,
    "corp": """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-purple">Corporate Legal Architecture</span>
          <span class="visual-diagram-title">Three-Tier Holding, PropCo &amp; OpCo Governance &amp; Tax Structure</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/diagram_corporate_structure.svg" alt="Corporate Structure Diagram" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Asset Ring-Fencing:</strong> Holding Co (Mamun Limited) owns 100% of PropCo (ADOV Limited) which holds freeholds and leases to OpCo (ADOV Care Group Limited) under commercial FRI leases. Director resides at 82 under market AST (BIK = Nil).
        </div>
      </div>
    """,
    "cqc": """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-gold">CQC 90-Day Approval Pathway</span>
          <span class="visual-diagram-title">5 Sequential Statutory Milestones &amp; Section 28(3) Fast-Track Waiver</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/diagram_cqc_roadmap.svg" alt="CQC Approval Roadmap" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Fast-Track Acceleration:</strong> Phase 1 Pre-App -&gt; Phase 2 Governance &amp; RM -&gt; Phase 3 Submission -&gt; Phase 4 RM Interview &amp; Site Visit -&gt; Phase 5 S.28(3) Fast-Track Waiver Certificate (cuts 28 calendar days off registration).
        </div>
      </div>
    """,
    "mcda": """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-green">Strategic Decision Matrix</span>
          <span class="visual-diagram-title">MCDA 100-Point Scoring Analysis Across All 4 Care Sector Models</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/diagram_4options_mcda.svg" alt="MCDA 4 Options Scoring" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Forensic Appraisal:</strong> Demonstrating why Option 4 (Supported Living) dominates with 94/100, outperforming Children's Home (72), Elderly Dementia (68), and Shared HMO (58) across profitability, regulatory ease, and planning immunity.
        </div>
      </div>
    """,
    "waterfall": """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-blue">Financial Model &amp; Waterfall</span>
          <span class="visual-diagram-title">Gross Turnover to Operating EBITDA Waterfall Breakdown (£)</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/diagram_financial_waterfall.svg" alt="Financial Waterfall Flow" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Cashflow Velocity:</strong> Financial flow from £977.6k gross turnover through care payroll (£355k), PropCo rent (£97k), and facility OpEx (£184k), delivering £341,392 OpCo EBITDA (35% margin) and 3.8 beds break-even threshold.
        </div>
      </div>
    """,
    "intake": """
      <div class="visual-diagram-card">
        <div class="visual-diagram-header">
          <span class="visual-diagram-badge badge-blue">Clinical Operations SOP</span>
          <span class="visual-diagram-title">Zero-Void Resident Intake Pathway SOP (6 Phased Stages)</span>
        </div>
        <div class="visual-diagram-body">
          <img src="assets/diagrams/diagram_intake_pathway.svg" alt="Resident Intake Pathway SOP" class="visual-diagram-img" loading="lazy">
        </div>
        <div class="visual-diagram-caption">
          <strong>Intake Governance:</strong> Clinical pathway protocol: Referral -&gt; Desk Pre-Screen -&gt; F2F Assessment -&gt; Peer Matching -&gt; Phased Transition Visits -&gt; Tenancy &amp; Personal Care Commencement.
        </div>
      </div>
    """
}

# Ordered list of tabs for Prev/Next navigation
TAB_ORDER = [
    "tab-overview", "tab-options", "tab-advisory", "tab-strategy",
    "tab-houses", "tab-capex", "tab-planning", "tab-tax",
    "tab-cqc", "tab-cqc-reqs", "tab-financials", "tab-commissioning",
    "tab-tracker", "tab-vault", "tab-glossary"
]

print("Defined diagram snippets and tab order.")
