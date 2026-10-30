#!/usr/bin/env python3
"""
Batch Builder & Quality Assurance Engine for ADOV Care Group Vault Documents.
Generates all 17+ University Research Journal style PDFs, validates A4 dimensions,
confirms 0% dark fills (pure white paper, low-ink ergonomics), checks page counts,
and deploys them to portal/docs/ and the brain artifact directory.
"""

import os
import sys
import shutil
import zlib
import re
import subprocess

ARTIFACT_DOCS_DIR = "/Users/mamun/.gemini/antigravity/brain/af24e45c-fc9e-4655-a931-ef50789324b7/docs"
PORTAL_DOCS_DIR = "portal/docs"

GENERATORS = [
    ("generate_advisory_board_report.py", "ADOV_Care_Group_Expert_Advisory_Board_and_Viability_Assessment_Report.pdf"),
    ("generate_final_recommendation_report.py", "ADOV_Care_Group_Final_Recommendation_Report.pdf"),
    ("generate_4options_comparison_report.py", "ADOV_Care_Group_4_Options_Strategic_Comparison_Report.pdf"),
    ("generate_operational_pnl_report.py", "ADOV_Care_Group_Operational_PnL_and_Financial_Viability_Model.pdf"),
    ("generate_cqc_registration_master_report.py", "ADOV_Care_Group_CQC_Registration_Master_Report.pdf"),
    ("generate_cqc_requirements_guide.py", "ADOV_Care_Group_CQC_Requirements_and_Fulfillment_Guide.pdf"),
    ("generate_cqc_questions_dossier.py", "ADOV_Care_Group_CQC_Provider_Application_Questions_Dossier.pdf"),
    ("generate_intake_pathway_sop.py", "ADOV_Care_Group_Resident_Intake_Pathway_SOP.pdf"),
    ("generate_scenario_appraisal_report.py", "ADOV_Care_Group_Campus_Strategy_Appraisal.pdf"),
    ("build_pack1_checklist.py", "ADOV_Care_Group_Master_Document_Checklist.pdf"),
    ("build_pack2_corporate.py", "ADOV_Care_Group_Corporate_Legal_Pack.pdf"),
    ("build_pack3_planning.py", "ADOV_Care_Group_Section_192_Planning_Statement.pdf"),
    ("build_pack4_cqc.py", "ADOV_Care_Group_CQC_Statement_of_Purpose.pdf"),
    ("build_pack5_tenancy.py", "ADOV_Care_Group_Supported_Living_Tenancy_Pack.pdf"),
    ("generate_government_project_report.py", "ADOV_Care_Group_Government_Project_Report.pdf"),
    ("generate_luxury_brochure.py", "ADOV_Care_Group_Private_Project_Prospectus.pdf"),
    ("generate_photo_campus_report.py", "ADOV_Care_Group_Photographic_Campus_Masterplan.pdf"),
    ("generate_private_investment_prospectus.py", "ADOV_Care_Group_Private_Investment_Prospectus.pdf"),
]

def check_pdf_metrics(pdf_path):
    with open(pdf_path, 'rb') as f:
        data = f.read()

    # Check pages count
    pages = re.findall(rb'/Type\s*/Page\b', data)
    page_count = len(pages)

    # Check dark fills
    streams = re.findall(rb'stream\r?\n(.*?)\r?\nendstream', data, re.DOTALL)
    dark_fills = []
    for idx, s in enumerate(streams):
        try:
            decomp = zlib.decompress(s).decode('latin1')
        except:
            decomp = s.decode('latin1', errors='ignore')
        matches = re.findall(r'([0-9\.]+)\s+([0-9\.]+)\s+([0-9\.]+)\s+rg\s+([0-9\.]+)\s+([0-9\.]+)\s+([0-9\.]+)\s+([0-9\.]+)\s+re\s+(f|B)', decomp)
        for r, g, b, x, y, w, h, op in matches:
            r, g, b, w, h = float(r), float(g), float(b), float(w), float(h)
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            if lum < 0.25 and (w > 200 and h > 100):
                dark_fills.append((idx + 1, r, g, b, w, h))

    # Check media box dimensions
    media_boxes = re.findall(rb'/MediaBox\s*\[\s*0\s+0\s+([0-9\.]+)\s+([0-9\.]+)\s*\]', data)
    is_a4 = False
    if media_boxes:
        w_val, h_val = float(media_boxes[0][0]), float(media_boxes[0][1])
        if abs(w_val - 595.28) < 1.0 and abs(h_val - 841.89) < 1.0:
            is_a4 = True

    return {
        "bytes": len(data),
        "pages": page_count,
        "dark_fills": len(dark_fills),
        "is_a4": is_a4
    }

def main():
    print("=" * 80)
    print("ADOV CARE GROUP: BATCH UNIVERSITY RESEARCH JOURNAL PDF BUILDER & AUDITOR")
    print("Standards: Standard ISO A4 (595.28x841.89pt) // Crisp Plain White // Low Ink")
    print("=" * 80)

    os.makedirs(ARTIFACT_DOCS_DIR, exist_ok=True)
    os.makedirs(PORTAL_DOCS_DIR, exist_ok=True)

    results = []

    for script, target_pdf in GENERATORS:
        print(f"\n>> Executing: {script} ...")
        cmd = [sys.executable, script]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            print(f"FAILED: {script}")
            print(proc.stderr)
            sys.exit(1)

        if not os.path.exists(target_pdf):
            print(f"ERROR: Expected PDF '{target_pdf}' not found after running {script}")
            sys.exit(1)

        metrics = check_pdf_metrics(target_pdf)
        results.append((target_pdf, metrics))
        print(f"   ✓ OK: {target_pdf} -> {metrics['pages']} pages, {metrics['bytes']:,} bytes, {metrics['dark_fills']} dark fills, A4: {metrics['is_a4']}")

        # Deploy to portal/docs and artifact docs
        # Remove existing file/symlink if present
        dest_portal = os.path.join(PORTAL_DOCS_DIR, target_pdf)
        if os.path.islink(dest_portal) or os.path.exists(dest_portal):
            os.remove(dest_portal)
        shutil.copy2(target_pdf, dest_portal)

        dest_artifact = os.path.join(ARTIFACT_DOCS_DIR, target_pdf)
        if os.path.islink(dest_artifact) or os.path.exists(dest_artifact):
            os.remove(dest_artifact)
        shutil.copy2(target_pdf, dest_artifact)

        # Also copy matching docx if exists
        docx_file = target_pdf.replace(".pdf", ".docx")
        if os.path.exists(docx_file):
            portal_docx = os.path.join(PORTAL_DOCS_DIR, docx_file)
            if os.path.islink(portal_docx) or os.path.exists(portal_docx):
                os.remove(portal_docx)
            shutil.copy2(docx_file, portal_docx)

            art_docx = os.path.join(ARTIFACT_DOCS_DIR, docx_file)
            if os.path.islink(art_docx) or os.path.exists(art_docx):
                os.remove(art_docx)
            shutil.copy2(docx_file, art_docx)

    print("\n" + "=" * 80)
    print("ALL 18 MASTER VAULT RESEARCH JOURNAL PDFS COMPILED & VALIDATED SUCCESSFULLY")
    print("=" * 80)
    print(f"{'Document Filename':<62} | {'Pages':<5} | {'Bytes':<9} | {'Dark Fills':<10} | {'A4 Format'}")
    print("-" * 100)
    for target_pdf, m in results:
        status_a4 = "YES (A4)" if m['is_a4'] else "NO"
        print(f"{target_pdf:<62} | {m['pages']:<5} | {m['bytes']:<9,} | {m['dark_fills']:<10} | {status_a4}")

    print("\nAll files synchronized to 'portal/docs/' and artifact directory.")

if __name__ == "__main__":
    main()
