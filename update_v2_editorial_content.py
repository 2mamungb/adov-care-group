import re
import os

print("Starting V2.0 Editorial & PhD-Grade Research Portal Upgrade...")

with open("portal/v2.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. EDITORIAL CSS INJECTION
editorial_css = """
/* =============================================================================
   CHIEF EDITORIAL DESIGN SYSTEM: FT × HBR × NATURE × THE ECONOMIST
   ============================================================================= */

/* 1. EDITORIAL ARTICLE CONTAINER & TYPOGRAPHY */
.editorial-article {
  max-width: 100%;
  margin: 0 auto;
  color: var(--text-main, #1E293B);
  font-size: 15px;
  line-height: 1.72;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

.editorial-article p {
  margin-bottom: 1.25em;
  line-height: 1.72;
  color: var(--text-main, #1E293B);
}

.editorial-article h1,
.editorial-article h2,
.editorial-article h3,
.editorial-article h4 {
  font-family: "Charter", "Iowan Old Style", "Sitka Text", "Georgia", serif;
  color: var(--navy, #0F1E36);
  letter-spacing: -0.015em;
}

[data-theme="dark"] .editorial-article h1,
[data-theme="dark"] .editorial-article h2,
[data-theme="dark"] .editorial-article h3,
[data-theme="dark"] .editorial-article h4 {
  color: #F1F5F9;
}

.editorial-article h2 {
  font-size: 22px;
  font-weight: 700;
  margin-top: 36px;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1.5px solid var(--border, #E2E8F0);
}

.editorial-article h3 {
  font-size: 17.5px;
  font-weight: 600;
  margin-top: 28px;
  margin-bottom: 12px;
}

/* Publication Badges & Meta Bylines */
.editorial-meta-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  padding: 10px 0 16px 0;
  margin-bottom: 24px;
  border-bottom: 1px solid var(--border, #E2E8F0);
  font-size: 12px;
  color: var(--text-muted, #64748B);
}

.editorial-pub-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--gold-light, #FBF6EB);
  color: var(--gold-dark, #9A751E);
  border: 1px solid rgba(194, 155, 56, 0.35);
  padding: 3px 9px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

[data-theme="dark"] .editorial-pub-badge {
  background: #2A2518;
  color: #D4AF37;
  border-color: rgba(212, 175, 55, 0.3);
}

.editorial-byline {
  font-weight: 600;
  color: var(--navy, #0F1E36);
}

[data-theme="dark"] .editorial-byline {
  color: #E2E8F0;
}

.editorial-date {
  font-family: ui-monospace, SFMono-Regular, monospace;
}

/* 2. ABSTRACT / EXECUTIVE DECK SUMMARY BOX */
.abstract-lead {
  position: relative;
  background: #FAFBFC;
  border: 1px solid var(--border, #E2E8F0);
  border-left: 5px solid var(--gold, #C29B38);
  border-radius: 6px;
  padding: 22px 26px;
  margin: 24px 0 32px 0;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
}

[data-theme="dark"] .abstract-lead {
  background: #141E33;
  border-color: #334155;
  border-left-color: #D4AF37;
}

.abstract-lead-label {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--gold-dark, #9A751E);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

[data-theme="dark"] .abstract-lead-label {
  color: #D4AF37;
}

.abstract-lead-prose {
  font-family: "Charter", "Iowan Old Style", "Georgia", serif;
  font-size: 16px;
  line-height: 1.65;
  font-style: italic;
  color: var(--navy, #0F1E36);
  margin-bottom: 12px;
}

[data-theme="dark"] .abstract-lead-prose {
  color: #F1F5F9;
}

.abstract-lead-bullets {
  list-style: none;
  padding: 0;
  margin: 12px 0 0 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 8px 16px;
  border-top: 1px dashed var(--border, #E2E8F0);
  padding-top: 12px;
  font-size: 13px;
  color: var(--text-main, #1E293B);
}

[data-theme="dark"] .abstract-lead-bullets {
  border-top-color: #334155;
  color: #CBD5E1;
}

.abstract-lead-bullets li strong {
  color: var(--navy, #0F1E36);
}

[data-theme="dark"] .abstract-lead-bullets li strong {
  color: #FFFFFF;
}

/* 3. DROP-CAP INITIAL STYLING */
.drop-cap {
  float: left;
  font-family: "Charter", "Iowan Old Style", "Georgia", serif;
  font-size: 3.2em;
  line-height: 0.8;
  padding-top: 4px;
  padding-right: 10px;
  padding-bottom: 2px;
  font-weight: 700;
  color: var(--navy, #0F1E36);
}

[data-theme="dark"] .drop-cap {
  color: #D4AF37;
}

/* 4. STATUTORY PULL-QUOTE CALLOUT */
.pull-quote-statute {
  margin: 32px 0;
  padding: 22px 28px;
  border-top: 2px solid var(--navy, #0F1E36);
  border-bottom: 2px solid var(--navy, #0F1E36);
  background: rgba(15, 30, 54, 0.02);
  text-align: center;
  position: relative;
}

[data-theme="dark"] .pull-quote-statute {
  border-top-color: #D4AF37;
  border-bottom-color: #D4AF37;
  background: rgba(212, 175, 55, 0.04);
}

.pull-quote-text {
  font-family: "Charter", "Iowan Old Style", "Georgia", serif;
  font-size: 18px;
  font-style: italic;
  line-height: 1.55;
  color: var(--navy, #0F1E36);
  margin-bottom: 8px;
}

[data-theme="dark"] .pull-quote-text {
  color: #F8FAFC;
}

.pull-quote-cite {
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: var(--gold-dark, #9A751E);
  text-transform: uppercase;
}

[data-theme="dark"] .pull-quote-cite {
  color: #D4AF37;
}

/* 5. SCIENTIFIC FIGURE BOX SYSTEM */
.figure-box {
  background: #FFFFFF;
  border: 1px solid var(--border, #E2E8F0);
  border-radius: 8px;
  padding: 18px 20px;
  margin: 32px 0;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
}

[data-theme="dark"] .figure-box {
  background: #1C2541;
  border-color: #334155;
}

.figure-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--border, #E2E8F0);
}

[data-theme="dark"] .figure-header {
  border-bottom-color: #334155;
}

.figure-title {
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
  font-size: 13.5px;
  font-weight: 800;
  color: var(--navy, #0F1E36);
  letter-spacing: -0.01em;
}

[data-theme="dark"] .figure-title {
  color: #FFFFFF;
}

.figure-badge {
  font-size: 10.5px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 3px;
  background: #F1F5F9;
  color: #475569;
  font-family: ui-monospace, monospace;
}

[data-theme="dark"] .figure-badge {
  background: #334155;
  color: #CBD5E1;
}

.figure-body {
  width: 100%;
  border-radius: 6px;
  overflow: hidden;
  background: #FAFAFC;
  border: 1px solid rgba(0, 0, 0, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
}

[data-theme="dark"] .figure-body {
  background: #0F172A;
  border-color: #334155;
}

.figure-body svg {
  width: 100%;
  height: auto;
  display: block;
}

.figure-caption {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--text-main, #1E293B);
  margin-top: 14px;
  padding-top: 10px;
  border-top: 1px solid var(--border, #E2E8F0);
}

[data-theme="dark"] .figure-caption {
  color: #CBD5E1;
  border-top-color: #334155;
}

.figure-caption strong {
  color: var(--navy, #0F1E36);
}

[data-theme="dark"] .figure-caption strong {
  color: #FFFFFF;
}

.figure-source {
  font-size: 11px;
  color: var(--text-muted, #64748B);
  margin-top: 6px;
  font-style: italic;
}

/* 6. ACADEMIC & FINANCIAL JOURNAL TABLE SYSTEM */
.table-journal-wrap {
  width: 100%;
  overflow-x: auto;
  margin: 30px 0;
  border: 1px solid var(--border, #E2E8F0);
  border-radius: 6px;
  background: #FFFFFF;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
}

[data-theme="dark"] .table-journal-wrap {
  background: #1C2541;
  border-color: #334155;
}

.table-header-block {
  padding: 12px 18px;
  background: #F8FAFC;
  border-bottom: 2px solid var(--navy, #0F1E36);
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 8px;
}

[data-theme="dark"] .table-header-block {
  background: #141E33;
  border-bottom-color: #D4AF37;
}

.table-title {
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
  font-size: 13px;
  font-weight: 800;
  color: var(--navy, #0F1E36);
}

[data-theme="dark"] .table-title {
  color: #FFFFFF;
}

table.table-journal {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
  line-height: 1.5;
  text-align: left;
}

table.table-journal th {
  background: #F1F5F9;
  color: var(--navy, #0F1E36);
  font-weight: 700;
  padding: 10px 14px;
  border-bottom: 1.5px solid var(--border-dark, #CBD5E1);
  text-transform: uppercase;
  font-size: 10.5px;
  letter-spacing: 0.04em;
  white-space: nowrap;
}

[data-theme="dark"] table.table-journal th {
  background: #232F4E;
  color: #F1F5F9;
  border-bottom-color: #475569;
}

table.table-journal td {
  padding: 9px 14px;
  border-bottom: 1px solid var(--border, #E2E8F0);
  color: var(--text-main, #1E293B);
}

[data-theme="dark"] table.table-journal td {
  border-bottom-color: #334155;
  color: #E2E8F0;
}

table.table-journal tbody tr:nth-child(even) {
  background-color: rgba(248, 250, 252, 0.7);
}

[data-theme="dark"] table.table-journal tbody tr:nth-child(even) {
  background-color: rgba(255, 255, 255, 0.02);
}

table.table-journal tbody tr:hover {
  background-color: rgba(194, 155, 56, 0.06);
}

table.table-journal tfoot td {
  background: #F8FAFC;
  font-weight: 800;
  border-top: 2px solid var(--navy, #0F1E36);
  border-bottom: none;
  color: var(--navy, #0F1E36);
}

[data-theme="dark"] table.table-journal tfoot td {
  background: #141E33;
  border-top-color: #D4AF37;
  color: #FFFFFF;
}

.col-num {
  text-align: right;
  font-variant-numeric: tabular-nums;
  font-family: ui-monospace, SFMono-Regular, monospace;
}

.col-center {
  text-align: center;
}

.table-footer-notes {
  padding: 10px 18px 12px 18px;
  background: #FAFBFC;
  border-top: 1px solid var(--border, #E2E8F0);
  font-size: 11px;
  color: var(--text-muted, #64748B);
  line-height: 1.5;
}

[data-theme="dark"] .table-footer-notes {
  background: #121929;
  border-top-color: #334155;
}

.table-source {
  font-weight: 600;
  color: var(--navy, #0F1E36);
  margin-bottom: 3px;
}

[data-theme="dark"] .table-source {
  color: #CBD5E1;
}

/* 7. SCHOLARLY FOOTNOTE & CITATION SYSTEM */
.footnote-ref {
  font-size: 0.72em;
  line-height: 0;
  vertical-align: super;
  margin-left: 2px;
  margin-right: 2px;
}

.footnote-ref a {
  color: #0071E3;
  text-decoration: none;
  font-weight: 700;
  padding: 1px 3px;
  border-radius: 3px;
  transition: all 0.15s ease;
}

[data-theme="dark"] .footnote-ref a {
  color: #60A5FA;
}

.footnote-ref a:hover {
  background-color: rgba(0, 113, 227, 0.12);
  text-decoration: underline;
}

/* References Section at End of Tab */
.references-section {
  margin-top: 56px;
  padding-top: 24px;
  border-top: 2px solid var(--navy, #0F1E36);
  background: #FAFAFC;
  border-radius: 8px;
  padding: 24px 28px;
  border: 1px solid var(--border, #E2E8F0);
}

[data-theme="dark"] .references-section {
  border-top-color: #D4AF37;
  background: #141E33;
  border-color: #334155;
}

.references-heading {
  font-family: "Charter", "Iowan Old Style", "Georgia", serif;
  font-size: 19px;
  font-weight: 700;
  color: var(--navy, #0F1E36);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

[data-theme="dark"] .references-heading {
  color: #F1F5F9;
}

.references-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.reference-item {
  display: flex;
  align-items: baseline;
  gap: 10px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--text-main, #1E293B);
  padding: 4px 8px;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

[data-theme="dark"] .reference-item {
  color: #CBD5E1;
}

.reference-item:target {
  background-color: rgba(194, 155, 56, 0.18);
  outline: 1.5px solid var(--gold, #C29B38);
}

.ref-num {
  font-family: ui-monospace, monospace;
  font-size: 11px;
  font-weight: 800;
  color: var(--gold-dark, #9A751E);
  min-width: 24px;
}

[data-theme="dark"] .ref-num {
  color: #D4AF37;
}

.ref-body {
  flex: 1;
}

.ref-author {
  font-weight: 700;
  color: var(--navy, #0F1E36);
}

[data-theme="dark"] .ref-author {
  color: #FFFFFF;
}

.ref-year {
  font-weight: 600;
}

cite.ref-title {
  font-style: italic;
  color: var(--text-main, #1E293B);
}

[data-theme="dark"] cite.ref-title {
  color: #F1F5F9;
}

.ref-source {
  color: var(--text-muted, #64748B);
}

.ref-link {
  color: #0071E3;
  text-decoration: none;
  word-break: break-all;
  font-size: 12px;
}

.ref-link:hover {
  text-decoration: underline;
}

.ref-backlink {
  color: var(--gold-dark, #9A751E);
  text-decoration: none;
  font-weight: bold;
  font-size: 12px;
  margin-left: 6px;
  padding: 0 4px;
}

.ref-backlink:hover {
  color: var(--navy, #0F1E36);
}
"""

if "/* CHIEF EDITORIAL DESIGN SYSTEM" not in html:
    html = html.replace("</style>", editorial_css + "\n</style>", 1)
    print("Injected Chief Editorial Design System CSS!")

with open("portal/v2.html", "w", encoding="utf-8") as f:
    f.write(html)

print("CSS saved.")
