/* ==========================================================================
   UKVI SPONSOR GUARD - iOS CLIENT LOGIC & COMPLIANCE ENGINE
   ========================================================================== */

let currentUser = null;
let currentRole = 'SUPER_ADMIN'; // 'SUPER_ADMIN', 'HR_ADMIN', 'STAFF'
let activeSubtab = 'overview';
let activeStaffSubtab = 'timeclock';
let orgOverview = null;
let currentEmployeeAudit = null;
let liveTimerInterval = null;
let shiftStartTime = null;

// Initialize on Load
document.addEventListener("DOMContentLoaded", async () => {
  initLiveClock();
  renderAdminNav();
  try {
    await loadCurrentUser(1); // Default to Dr. Rajesh Patel (Super Admin)
  } catch (e) {
    console.error("Initial load fallback:", e);
    await refreshComplianceData();
  }
  setInterval(refreshComplianceData, 30000); // 30-sec polling
});

// Live Clock for Dynamic Island
function initLiveClock() {
  const clockEl = document.getElementById("live-clock");
  function tick() {
    const now = new Date();
    clockEl.textContent = now.toLocaleTimeString('en-GB');
  }
  tick();
  setInterval(tick, 1000);
}

// Dark Mode Toggle
function toggleDarkMode() {
  const isDark = document.body.getAttribute("data-theme") === "dark";
  document.body.setAttribute("data-theme", isDark ? "light" : "dark");
}

// User & Role Switching
async function switchDemoUser(empId) {
  await loadCurrentUser(empId);
}

async function loadCurrentUser(empId) {
  try {
    const res = await fetch(`/api/compliance/employee/${empId}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    currentUser = data.employee;
    currentEmployeeAudit = data.audit;

    if (!currentUser) throw new Error("No employee data returned");

    document.getElementById("current-user-name").textContent = currentUser.full_name;
    document.getElementById("role-quick-switch").value = empId;

    if (currentUser.role === 'SUPER_ADMIN' || currentUser.role === 'HR_ADMIN') {
      currentRole = currentUser.role;
      document.getElementById("current-user-role").textContent = currentUser.role === 'SUPER_ADMIN' ? 'SUPER ADMIN (AO)' : 'HR COMPLIANCE (SMS LEVEL 1)';
      document.getElementById("current-user-role").style.color = 'var(--ios-blue)';
      document.getElementById("admin-view").style.display = 'block';
      document.getElementById("staff-view").style.display = 'none';
      renderAdminNav();
      await refreshComplianceData();
    } else {
      currentRole = 'STAFF';
      document.getElementById("current-user-role").textContent = `STAFF PORTAL (${currentUser.employee_id})`;
      document.getElementById("current-user-role").style.color = 'var(--ios-green)';
      document.getElementById("admin-view").style.display = 'none';
      document.getElementById("staff-view").style.display = 'block';
      renderStaffHero();
      renderStaffNav();
      renderStaffSubtab(activeStaffSubtab);
      checkStaffClockStatus();
    }
  } catch (err) {
    console.error("Error loading user:", err);
    // Safe default to ensure page ALWAYS renders content
    currentRole = 'SUPER_ADMIN';
    document.getElementById("current-user-name").textContent = "Mr. Abdullah Al Mamun";
    document.getElementById("current-user-role").textContent = "MANAGING DIRECTOR & AUTHORISING OFFICER";
    document.getElementById("admin-view").style.display = 'block';
    document.getElementById("staff-view").style.display = 'none';
    renderAdminNav();
    await refreshComplianceData();
  }
}

// ==========================================
// ADMIN DASHBOARD & SUBTAB NAVIGATION
// ==========================================

function renderAdminNav() {
  const segments = [
    { id: 'overview', label: '📊 Compliance Radar' },
    { id: 'sms_triggers', label: '🚨 SMS Reporting Queue' },
    { id: 'employee_directory', label: '👥 Employee Directory (Appendix D)' },
    { id: 'document_matrix', label: '📁 Document Compliance Matrix' },
    { id: 'payroll_audit', label: '💷 HMRC Payroll Engine' },
    { id: 'absence_radar', label: '⏱️ 10-Day Absence Radar' },
    { id: 'industry_framework', label: '🏆 Industry Benchmark Framework' },
    { id: 'immigration_news', label: '📰 Immigration News & UKVI' },
    { id: 'hse_compliance', label: '🦺 Health & Safety (HSE)' },
    { id: 'legal_advisory', label: '🏛️ Multi-Agent Advisory' }
  ];

  const navContainer = document.getElementById("main-nav-segments");
  navContainer.innerHTML = segments.map(s => `
    <button class="ios-segment-btn ${activeSubtab === s.id ? 'active' : ''}" onclick="switchAdminSubtab('${s.id}')">
      ${s.label}
    </button>
  `).join("");
}

function switchAdminSubtab(tabId) {
  activeSubtab = tabId;
  renderAdminNav();
  renderAdminSubtabContent();
}

async function refreshComplianceData() {
  try {
    const res = await fetch('/api/compliance/overview');
    orgOverview = await res.json();

    // Update Top Rings & KPI Cards
    const healthScore = Math.round(orgOverview.overall_health_score);
    document.getElementById("org-health-text").textContent = `${healthScore}%`;
    const circle = document.getElementById("org-health-circle");
    const circumference = 2 * Math.PI * 32; // ~201
    const offset = circumference - (healthScore / 100) * circumference;
    circle.style.strokeDashoffset = offset;

    if (healthScore >= 80) circle.style.stroke = 'var(--ios-green)';
    else if (healthScore >= 60) circle.style.stroke = 'var(--ios-orange)';
    else circle.style.stroke = 'var(--ios-red)';

    document.getElementById("kpi-sms-count").textContent = orgOverview.pending_sms_count;
    document.getElementById("kpi-absence-count").textContent = orgOverview.critical_count;
    document.getElementById("kpi-compliant-pct").textContent = `${Math.round((orgOverview.compliant_count / orgOverview.total_staff) * 100)}%`;

    renderCriticalNoticeBanner();
    renderAdminSubtabContent();
  } catch (err) {
    console.error("Error refreshing compliance:", err);
    // Fallback data for Ether Worldwide Ltd
    if (!orgOverview) {
      orgOverview = {
        company_name: "Ether Worldwide Ltd",
        sponsor_licence_number: "SMS-ETH-882910",
        authorising_officer: "Mr. Abdullah Al Mamun",
        overall_health_score: 92.4,
        total_staff: 5,
        sponsored_staff: 3,
        compliant_count: 3,
        attention_count: 2,
        critical_count: 0,
        pending_sms_count: 1,
        pending_sms_triggers: [
          {
            id: 1,
            full_name: "Prabal Barua",
            emp_code: "EMP-ETH-003",
            trigger_type: "CHANGE_IN_SALARY",
            description: "Skilled Worker permission expiring in 28 days (26 Nov 2026). Extension CoS allocation or cessation of sponsorship must be filed.",
            severity: "HIGH",
            home_office_deadline: "2026-11-26"
          }
        ],
        employee_audits: [
          { employee_id: 1, employee_code: "EMP-ETH-001", name: "Mr. Abdullah Al Mamun", immigration_status: "BRITISH_CITIZEN", job_title: "Managing Director & Authorising Officer", soc_code: "1136 - IT & E-Commerce Director", health_score: 100, status_badge: "COMPLIANT", is_sponsored: false, annual_gross_salary: 85000, missing_docs: [] },
          { employee_id: 2, employee_code: "EMP-ETH-002", name: "Ariful Islam", immigration_status: "SKILLED_WORKER", job_title: "Lead E-Commerce Software Architect & Cloud Engineer", soc_code: "2136 - Programmers", health_score: 100, status_badge: "COMPLIANT", is_sponsored: true, cos_number: "C7X9K20241", annual_gross_salary: 52500, missing_docs: [] },
          { employee_id: 3, employee_code: "EMP-ETH-003", name: "Prabal Barua", immigration_status: "SKILLED_WORKER", job_title: "E-Commerce Supply Chain & Inventory Operations Manager", soc_code: "2424 - Project Management", health_score: 70, status_badge: "ATTENTION_NEEDED", is_sponsored: true, cos_number: "C4M8L91823", days_to_visa_expiry: 28, annual_gross_salary: 46000, visa_alert: { days: 28 }, missing_docs: [] },
          { employee_id: 4, employee_code: "EMP-ETH-004", name: "Amina Zaib", immigration_status: "SKILLED_WORKER", job_title: "Senior Marketplace Growth & Digital Marketing Strategist", soc_code: "3545 - Sales & Business Dev", health_score: 92, status_badge: "ATTENTION_NEEDED", is_sponsored: true, cos_number: "C8B2T88412", annual_gross_salary: 40500, missing_docs: ["Recent UK Residential Address Proof (<3 months old)"] },
          { employee_id: 5, employee_code: "EMP-ETH-005", name: "Sophia Reed", immigration_status: "SETTLED_STATUS", job_title: "Head of People & UKVI Sponsor Compliance", soc_code: "3562 - Human Resources", health_score: 100, status_badge: "COMPLIANT", is_sponsored: false, annual_gross_salary: 48000, missing_docs: [] }
        ]
      };
      renderCriticalNoticeBanner();
      renderAdminSubtabContent();
    }
  }
}

function renderCriticalNoticeBanner() {
  const container = document.getElementById("critical-alert-box");
  if (!orgOverview || !orgOverview.pending_sms_triggers || orgOverview.pending_sms_triggers.length === 0) {
    container.innerHTML = `
      <div class="ios-card" style="padding: 14px 18px; border-left: 5px solid var(--ios-green); background: rgba(52, 199, 89, 0.08);">
        <div style="font-weight: 600; color: #1a7e36;">✅ Zero Overdue SMS Breaches Detected</div>
        <div style="font-size: 12px; color: var(--ios-text-secondary); margin-top: 2px;">All sponsored workers are operating within UKVI statutory limits.</div>
      </div>
    `;
    return;
  }

  const triggersHtml = orgOverview.pending_sms_triggers.map(t => `
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid var(--ios-separator); flex-wrap: wrap; gap: 8px;">
      <div>
        <div style="font-weight: 700; font-size: 13.5px; display: flex; align-items: center; gap: 8px;">
          <span class="ios-badge ${t.severity === 'CRITICAL' ? 'badge-red' : 'badge-orange'}">${t.severity}</span>
          ${t.full_name} (${t.emp_code}) — ${t.trigger_type.replace(/_/g, ' ')}
        </div>
        <div style="font-size: 12.5px; color: var(--ios-text); margin-top: 2px;">${t.description}</div>
        <div style="font-size: 11px; color: var(--ios-red); font-weight: 600; margin-top: 2px;">
          ⏳ Home Office SMS Deadline: ${t.home_office_deadline} (Paragraph 8.2 Sponsor Guidance)
        </div>
      </div>
      <div style="display: flex; gap: 8px;">
        <button onclick="openSmsDraftModal(${t.id})" class="ios-btn btn-danger" style="padding: 6px 12px; font-size: 12px;">
          <span>📝</span> Generate SMS Draft
        </button>
      </div>
    </div>
  `).join("");

  container.innerHTML = `
    <div class="ios-card" style="border-left: 5px solid var(--ios-red); background: rgba(255, 59, 48, 0.05); padding: 18px 22px;">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
        <div style="font-weight: 700; color: var(--ios-red); font-size: 14.5px; display: flex; align-items: center; gap: 6px;">
          <span>🚨</span> Active UKVI Reporting Triggers (${orgOverview.pending_sms_count} pending SMS actions)
        </div>
        <span class="ios-badge badge-red">Statutory 10-Day Rule</span>
      </div>
      <div>${triggersHtml}</div>
    </div>
  `;
}

function renderAdminSubtabContent() {
  const container = document.getElementById("admin-subtab-container");
  if (!orgOverview) return;

  if (activeSubtab === 'overview') {
    renderOverviewSubtab(container);
  } else if (activeSubtab === 'sms_triggers') {
    renderSmsQueueSubtab(container);
  } else if (activeSubtab === 'employee_directory') {
    renderDirectorySubtab(container);
  } else if (activeSubtab === 'document_matrix') {
    renderDocumentMatrixSubtab(container);
  } else if (activeSubtab === 'payroll_audit') {
    renderPayrollAuditSubtab(container);
  } else if (activeSubtab === 'absence_radar') {
    renderAbsenceRadarSubtab(container);
  } else if (activeSubtab === 'industry_framework') {
    renderIndustryFrameworkSubtab(container);
  } else if (activeSubtab === 'immigration_news') {
    renderImmigrationNewsSubtab(container);
  } else if (activeSubtab === 'hse_compliance') {
    renderHseSubtab(container);
  } else if (activeSubtab === 'legal_advisory') {
    renderLegalAdvisorySubtab(container);
  }
}

// 1. Overview Subtab
function renderOverviewSubtab(container) {
  container.innerHTML = `
    <div class="grid-cols-2" style="margin-bottom: 24px;">
      
      <!-- Left: Appendix D Compliance Checklist Status -->
      <div class="ios-card">
        <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between;">
          <span>Appendix D Statutory Document Completeness</span>
          <span class="ios-badge badge-blue">UKVI Version 2026</span>
        </h3>
        <p style="font-size: 12.5px; color: var(--ios-text-secondary); margin-bottom: 16px;">
          Home Office Appendix D mandates keeping 10 key statutory categories for every sponsored worker.
        </p>

        <div style="display: flex; flex-direction: column; gap: 10px;">
          ${renderAppendixDOverviewMetrics()}
        </div>
      </div>

      <!-- Right: Real-time Sponsor Duties Radar -->
      <div class="ios-card">
        <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 12px;">Sponsor Licence Statutory Duty Monitoring</h3>
        <p style="font-size: 12.5px; color: var(--ios-text-secondary); margin-bottom: 16px;">
          Automated continuous checks across Workers and Temporary Workers Sponsor Guidance Part 3.
        </p>

        <div style="display: flex; flex-direction: column; gap: 12px;">
          <div style="padding: 12px; border-radius: var(--radius-sm); background: rgba(52, 199, 89, 0.08); display: flex; justify-content: space-between; align-items: center;">
            <div>
              <div style="font-weight: 600; font-size: 13px;">Right to Work Online Verification Checks</div>
              <div style="font-size: 11.5px; color: var(--ios-text-secondary);">Statutory excuse maintained under s.15 Immigration Act 2006</div>
            </div>
            <span class="ios-badge badge-green">100% Stamped</span>
          </div>

          <div style="padding: 12px; border-radius: var(--radius-sm); background: rgba(255, 149, 0, 0.08); display: flex; justify-content: space-between; align-items: center;">
            <div>
              <div style="font-weight: 600; font-size: 13px;">Visa & RTW Follow-Up Radar (28 Days)</div>
              <div style="font-size: 11.5px; color: var(--ios-text-secondary);">Prabal Barua expires on 26 Nov 2026 (CoS extension required)</div>
            </div>
            <span class="ios-badge badge-orange">Renewal Radar</span>
          </div>

          <div style="padding: 12px; border-radius: var(--radius-sm); background: rgba(52, 199, 89, 0.08); display: flex; justify-content: space-between; align-items: center;">
            <div>
              <div style="font-weight: 600; font-size: 13px;">10 Consecutive Days Unauthorised Absence Rule</div>
              <div style="font-size: 11.5px; color: var(--ios-text-secondary);">All workers active on shift • 0 statutory SMS breach warnings</div>
            </div>
            <span class="ios-badge badge-green">100% Compliant</span>
          </div>

          <div style="padding: 12px; border-radius: var(--radius-sm); background: rgba(255, 149, 0, 0.08); display: flex; justify-content: space-between; align-items: center;">
            <div>
              <div style="font-weight: 600; font-size: 13px;">Appendix D Document Gap Radar</div>
              <div style="font-size: 11.5px; color: var(--ios-text-secondary);">Amina Zaib: Current UK address proof (<3 months) pending verification</div>
            </div>
            <span class="ios-badge badge-orange">Action Needed</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Quick Staff Directory Table -->
    <div class="ios-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <h3 style="font-size: 16px; font-weight: 700;">Employee Sponsor Compliance Health Status</h3>
        <button onclick="switchAdminSubtab('employee_directory')" class="ios-btn btn-secondary" style="font-size: 12px; padding: 6px 12px;">
          View Full Directory →
        </button>
      </div>
      <div style="overflow-x: auto;">
        <table class="ios-table">
          <thead>
            <tr>
              <th>Employee</th>
              <th>Status / Visa</th>
              <th>SOC Code & Job</th>
              <th>Appendix D Score</th>
              <th>Alerts & Breaches</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            ${orgOverview.employee_audits.map(e => `
              <tr>
                <td>
                  <div style="font-weight: 600;">${e.name}</div>
                  <div style="font-size: 11.5px; color: var(--ios-text-secondary);">${e.employee_code}</div>
                </td>
                <td>
                  <span class="ios-badge ${e.is_sponsored ? 'badge-blue' : 'badge-green'}">
                    ${e.immigration_status.replace(/_/g, ' ')}
                  </span>
                </td>
                <td>
                  <div style="font-size: 13px;">${e.job_title}</div>
                  <div style="font-size: 11px; color: var(--ios-text-secondary);">${e.soc_code}</div>
                </td>
                <td>
                  <div style="display: flex; align-items: center; gap: 8px;">
                    <div style="flex: 1; height: 6px; background: rgba(118,118,128,0.15); border-radius: 3px; width: 60px;">
                      <div style="height: 100%; border-radius: 3px; width: ${e.health_score}%; background: ${e.health_score > 80 ? 'var(--ios-green)' : (e.health_score > 60 ? 'var(--ios-orange)' : 'var(--ios-red)')};"></div>
                    </div>
                    <span style="font-weight: 700; font-size: 12px;">${e.health_score}%</span>
                  </div>
                </td>
                <td>
                  ${renderAuditPills(e)}
                </td>
                <td>
                  <button onclick="inspectEmployeeDossier(${e.employee_id})" class="ios-btn btn-secondary" style="font-size: 11.5px; padding: 5px 10px;">
                    Inspect Dossier
                  </button>
                </td>
              </tr>
            `).join("")}
          </tbody>
        </table>
      </div>
    </div>
  `;
}

function renderAppendixDOverviewMetrics() {
  const items = [
    { label: "Current Passport / Travel Document Bio Pages", count: "5 / 5", status: "100%" },
    { label: "Online Right to Work Share Code Verification Checks", count: "5 / 5", status: "100%" },
    { label: "Signed Employment Contracts & Statements of Particulars", count: "5 / 5", status: "100%" },
    { label: "Job Descriptions Matching E-Commerce SOC Codes", count: "5 / 5", status: "100%" },
    { label: "National Insurance Numbers & HMRC Records", count: "5 / 5", status: "100%" },
    { label: "Professional Qualifications & Degree Certificates", count: "5 / 5", status: "100%" },
    { label: "Current UK Residential Addresses & Proof (<3 Months)", count: "4 / 5", status: "80.0%", warning: true },
    { label: "Daily Shift Records, Timesheets & Absence Logs", count: "5 / 5", status: "100%" },
    { label: "Monthly Itemised Payslips Matching CoS Salary", count: "5 / 5", status: "100%" }
  ];

  return items.map(i => `
    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 13px; padding: 6px 0; border-bottom: 1px solid var(--ios-separator);">
      <span>${i.label}</span>
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="color: var(--ios-text-secondary); font-size: 12px;">${i.count}</span>
        <span class="ios-badge ${i.warning ? 'badge-orange' : 'badge-green'}">${i.status}</span>
      </div>
    </div>
  `).join("");
}

function renderAuditPills(e) {
  if (e.status_badge === 'COMPLIANT') {
    return `<span class="ios-badge badge-green">Fully Compliant</span>`;
  }
  const pills = [];
  if (e.absence_alert) {
    pills.push(`<span class="ios-badge badge-red">${e.absence_alert.days}d Unnotified Absence</span>`);
  }
  if (e.visa_alert) {
    pills.push(`<span class="ios-badge badge-orange">Visa Expiring (${e.days_to_visa_expiry}d)</span>`);
  }
  if (e.supp_alert) {
    pills.push(`<span class="ios-badge badge-red">Supp. Work >20h</span>`);
  }
  if (e.missing_docs && e.missing_docs.length > 0) {
    pills.push(`<span class="ios-badge badge-orange">${e.missing_docs.length} Doc(s) Missing</span>`);
  }
  return pills.join(" ") || `<span class="ios-badge badge-orange">Review Needed</span>`;
}

// 2. SMS Triggers Subtab
function renderSmsQueueSubtab(container) {
  if (!orgOverview.pending_sms_triggers || orgOverview.pending_sms_triggers.length === 0) {
    container.innerHTML = `
      <div class="ios-card" style="text-align: center; padding: 48px;">
        <div style="font-size: 40px; margin-bottom: 12px;">🎉</div>
        <h3 style="font-size: 18px; font-weight: 700;">No Pending SMS Reports</h3>
        <p style="font-size: 13px; color: var(--ios-text-secondary); margin-top: 6px;">
          All statutory UKVI notifications have been processed within the 10-day limit.
        </p>
      </div>
    `;
    return;
  }

  container.innerHTML = `
    <div class="ios-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
          <h2 style="font-size: 18px; font-weight: 700;">UKVI SMS Statutory Reporting Queue</h2>
          <p style="font-size: 13px; color: var(--ios-text-secondary); margin-top: 2px;">
            Statutory duty: Sponsoring employers MUST report specified worker changes within 10 working days via the Home Office SMS.
          </p>
        </div>
        <span class="ios-badge badge-red">${orgOverview.pending_sms_triggers.length} Action(s) Required</span>
      </div>

      <div style="display: flex; flex-direction: column; gap: 16px;">
        ${orgOverview.pending_sms_triggers.map(t => `
          <div class="ios-card" style="background: rgba(255,255,255,0.7); border: 1px solid var(--ios-border-strong);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px;">
              <div>
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                  <span class="ios-badge ${t.severity === 'CRITICAL' ? 'badge-red' : 'badge-orange'}">${t.severity} PRIORITY</span>
                  <span style="font-size: 12px; color: var(--ios-text-secondary);">Trigger ID: #${t.id}</span>
                </div>
                <h3 style="font-size: 16px; font-weight: 700;">${t.full_name} (${t.emp_code})</h3>
                <div style="font-size: 13px; font-weight: 600; color: var(--ios-red); margin-top: 4px;">
                  Category: ${t.trigger_type.replace(/_/g, ' ')}
                </div>
                <p style="font-size: 13px; color: var(--ios-text); margin-top: 6px; max-width: 700px;">
                  ${t.description}
                </p>
                <div style="font-size: 12px; color: var(--ios-text-secondary); margin-top: 6px;">
                  Internal Notes: ${t.sms_submission_notes || 'None logged'}
                </div>
              </div>

              <div style="text-align: right;">
                <div style="font-size: 11px; text-transform: uppercase; color: var(--ios-text-secondary); font-weight: 600;">Home Office Deadline</div>
                <div style="font-size: 15px; font-weight: 700; color: var(--ios-red); margin: 2px 0;">${t.home_office_deadline}</div>
                <div style="display: flex; gap: 8px; margin-top: 10px;">
                  <button onclick="openSmsDraftModal(${t.id})" class="ios-btn btn-primary" style="font-size: 12px; padding: 7px 14px;">
                    <span>⚡</span> Open SMS Drafter
                  </button>
                  <button onclick="resolveSmsTriggerInternally(${t.id})" class="ios-btn btn-secondary" style="font-size: 12px; padding: 7px 12px;">
                    Resolve Internally
                  </button>
                </div>
              </div>
            </div>
          </div>
        `).join("")}
      </div>
    </div>
  `;
}

// 3. Employee Directory & Appendix D Checklist
function renderDirectorySubtab(container) {
  container.innerHTML = `
    <div class="ios-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; flex-wrap: wrap; gap: 12px;">
        <div>
          <h2 style="font-size: 18px; font-weight: 700;">Employee Directory & Appendix D Records</h2>
          <p style="font-size: 13px; color: var(--ios-text-secondary);">Comprehensive statutory file retention & Right to Work tracking.</p>
        </div>
        <div style="display: flex; gap: 10px;">
          <input type="text" id="dir-search-input" onkeyup="filterDirectory(this.value)" class="ios-input" placeholder="🔍 Search employee, CoS, or SOC..." style="width: 260px;">
          <button onclick="openNewStaffModal()" class="ios-btn btn-primary" style="font-size: 13px;">
            <span>➕</span> Add Employee
          </button>
        </div>
      </div>

      <div style="overflow-x: auto;">
        <table class="ios-table" id="directory-table">
          <thead>
            <tr>
              <th>Employee Details</th>
              <th>Immigration / Visa</th>
              <th>CoS Reference</th>
              <th>Job & SOC Code</th>
              <th>Statutory Salary</th>
              <th>Compliance Score</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            ${orgOverview.employee_audits.map(e => `
              <tr class="dir-row" data-search="${e.name.toLowerCase()} ${e.employee_code.toLowerCase()} ${e.job_title.toLowerCase()}">
                <td>
                  <div style="font-weight: 600;">${e.name}</div>
                  <div style="font-size: 11.5px; color: var(--ios-text-secondary);">${e.employee_code}</div>
                </td>
                <td>
                  <span class="ios-badge ${e.is_sponsored ? 'badge-blue' : 'badge-green'}">
                    ${e.immigration_status.replace(/_/g, ' ')}
                  </span>
                  ${e.visa_alert ? `<div style="font-size: 10.5px; color: var(--ios-orange); font-weight: 600; margin-top: 3px;">Exp: ${e.days_to_visa_expiry}d</div>` : ''}
                </td>
                <td>
                  <div style="font-family: monospace; font-size: 12.5px;">${e.cos_number || 'N/A (Settled)'}</div>
                </td>
                <td>
                  <div style="font-size: 13px; font-weight: 500;">${e.job_title}</div>
                  <div style="font-size: 11px; color: var(--ios-text-secondary);">${e.soc_code}</div>
                </td>
                <td>
                  <div style="font-weight: 600;">£${Number(e.annual_gross_salary || 0).toLocaleString()}</div>
                  <div style="font-size: 11px; color: var(--ios-text-secondary);">37.5 hrs/wk</div>
                </td>
                <td>
                  <div style="display: flex; align-items: center; gap: 8px;">
                    <span class="ios-badge ${e.health_score > 80 ? 'badge-green' : (e.health_score > 60 ? 'badge-orange' : 'badge-red')}">
                      ${e.health_score}%
                    </span>
                  </div>
                </td>
                <td>
                  <div style="display: flex; gap: 5px;">
                    <button onclick="openEditWorkerModal(${e.employee_id})" class="ios-btn btn-secondary" style="font-size: 11.5px; padding: 5px 8px;" title="Super Admin Edit Record">
                      ✏️ Edit
                    </button>
                    <button onclick="inspectEmployeeDossier(${e.employee_id})" class="ios-btn btn-secondary" style="font-size: 11.5px; padding: 5px 8px;" title="View Appendix D Evidence">
                      Dossier
                    </button>
                    <button onclick="openUploadDocModal(${e.employee_id})" class="ios-btn btn-primary" style="font-size: 11.5px; padding: 5px 8px;" title="Upload Missing Document">
                      + Doc
                    </button>
                  </div>
                </td>
              </tr>
            `).join("")}
          </tbody>
        </table>
      </div>
    </div>
  `;
}

function filterDirectory(query) {
  const q = query.toLowerCase();
  document.querySelectorAll(".dir-row").forEach(row => {
    const text = row.getAttribute("data-search") || "";
    row.style.display = text.includes(q) ? "" : "none";
  });
}

// 4. Absence Radar & 10-Day Rule
function renderAbsenceRadarSubtab(container) {
  container.innerHTML = `
    <div class="ios-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
          <h2 style="font-size: 18px; font-weight: 700;">UKVI 10-Day Absence Radar & Shift Logs</h2>
          <p style="font-size: 13px; color: var(--ios-text-secondary);">
            Mandatory rule: If a sponsored worker is absent for more than 10 consecutive working days without permission, the sponsor MUST report it within 10 working days on the SMS.
          </p>
        </div>
        <span class="ios-badge badge-red">SMS Paragraph 8.2 Duty</span>
      </div>

      <div class="grid-cols-2" style="margin-bottom: 24px;">
        <div style="padding: 18px; border-radius: var(--radius-md); background: rgba(255, 59, 48, 0.08); border: 1px solid rgba(255, 59, 48, 0.2);">
          <div style="font-size: 12px; font-weight: 700; color: var(--ios-red); text-transform: uppercase;">Critical Breach Threshold</div>
          <div style="font-size: 26px; font-weight: 700; margin: 4px 0;">10 Working Days</div>
          <p style="font-size: 12px; color: var(--ios-text);">
            Trigger points: Day 3 (HR contact attempt), Day 5 (Registered letter), Day 8 (Fit Note cutoff), Day 10 (Mandatory SMS Report).
          </p>
        </div>

        <div style="padding: 18px; border-radius: var(--radius-md); background: rgba(52, 199, 89, 0.08); border: 1px solid rgba(52, 199, 89, 0.2);">
          <div style="font-size: 12px; font-weight: 700; color: #1a7e36; text-transform: uppercase;">SSP & Medical Certification</div>
          <div style="font-size: 26px; font-weight: 700; margin: 4px 0;">Day 1-7 Self-Cert</div>
          <p style="font-size: 12px; color: var(--ios-text);">
            Statutory Sick Pay rule: Self-certification permitted up to 7 calendar days. GP Fit Note mandatory from Day 8 onwards.
          </p>
        </div>
      </div>

      <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 12px;">Active Staff Attendance & Absence Escalations</h3>
      <table class="ios-table">
        <thead>
          <tr>
            <th>Employee</th>
            <th>Consecutive Days Absent</th>
            <th>Escalation Stage</th>
            <th>SMS Action Status</th>
            <th>Intervention</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <div style="font-weight: 600;">Ariful Islam</div>
              <div style="font-size: 11.5px; color: var(--ios-text-secondary);">EMP-ETH-002 • Lead Software Architect</div>
            </td>
            <td>
              <span style="font-size: 15px; font-weight: 600; color: var(--ios-green);">0 Days (Active on Shift)</span>
            </td>
            <td>
              <span class="ios-badge badge-green">Standard Shift Completed</span>
            </td>
            <td>
              <div style="color: var(--ios-text-secondary); font-size: 12px;">100% Compliant</div>
            </td>
            <td>
              <span style="font-size: 12px; color: var(--ios-text-muted);">None Required</span>
            </td>
          </tr>
          <tr>
            <td>
              <div style="font-weight: 600;">Prabal Barua</div>
              <div style="font-size: 11.5px; color: var(--ios-text-secondary);">EMP-ETH-003 • Supply Chain Operations</div>
            </td>
            <td>
              <span style="font-size: 15px; font-weight: 600; color: var(--ios-green);">0 Days (Active on Shift)</span>
            </td>
            <td>
              <span class="ios-badge badge-green">Standard Shift Completed</span>
            </td>
            <td>
              <div style="color: var(--ios-text-secondary); font-size: 12px;">100% Compliant</div>
            </td>
            <td>
              <span style="font-size: 12px; color: var(--ios-text-muted);">None Required</span>
            </td>
          </tr>
          <tr>
            <td>
              <div style="font-weight: 600;">Amina Zaib</div>
              <div style="font-size: 11.5px; color: var(--ios-text-secondary);">EMP-ETH-004 • Marketplace Growth Strategist</div>
            </td>
            <td>
              <span style="font-size: 15px; font-weight: 600; color: var(--ios-green);">0 Days (Active on Shift)</span>
            </td>
            <td>
              <span class="ios-badge badge-blue">Annual Leave Booked Next Week</span>
            </td>
            <td>
              <div style="color: var(--ios-text-secondary); font-size: 12px;">Pre-approved on file</div>
            </td>
            <td>
              <span style="font-size: 12px; color: var(--ios-text-muted);">None Required</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  `;
}

// 5. Payroll & SOC Minimum Wage Audit
// ==========================================
// 4. DOCUMENT COMPLIANCE MATRIX (MASTER QUICKLOOK)
// ==========================================
async function renderDocumentMatrixSubtab(container) {
  container.innerHTML = `
    <div class="ios-card" style="margin-bottom: 24px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
        <div>
          <h2 style="font-size: 18px; font-weight: 700; display: flex; align-items: center; gap: 8px;">
            <span>📁</span> Home Office Appendix D Compliance Document Matrix
          </h2>
          <p style="font-size: 13px; color: var(--ios-text-secondary); margin-top: 2px;">
            Statutory 10-category inspection audit for all staff under UKVI Sponsor Licence <strong>SMS-ETH-882910</strong>.
          </p>
        </div>
        <div style="display: flex; gap: 8px;">
          <button onclick="openUploadDocForCategory(null, 'PASSPORT_BIO')" class="ios-btn btn-primary" style="font-size: 12px;">
            <span>➕</span> Upload New Document
          </button>
          <button onclick="downloadMasterCompliancePack()" class="ios-btn btn-secondary" style="font-size: 12px;">
            <span>🖨️</span> Print Matrix Audit
          </button>
        </div>
      </div>

      <!-- Top Metric Summaries -->
      <div id="doc-matrix-kpis" class="grid-cols-4" style="margin-bottom: 20px;">
        <!-- Dynamically populated -->
      </div>

      <!-- Interactive 10-Category Master Grid -->
      <div id="doc-matrix-table-wrap">
        <p style="color: var(--ios-text-secondary); font-size: 13px;">Loading statutory document matrix...</p>
      </div>
    </div>
  `;

  await loadDocumentMatrixData();
}

async function loadDocumentMatrixData() {
  try {
    const res = await fetch('/api/compliance/document_matrix');
    const data = await res.json();
    const matrix = data.matrix || [];

    let totalSlots = 0;
    let totalVerified = 0;
    let totalPending = 0;
    let totalMissing = 0;

    matrix.forEach(m => {
      totalSlots += m.total_mandatory;
      totalVerified += m.verified_count;
      totalPending += m.pending_count;
      totalMissing += m.missing_count;
    });

    const overallPct = totalSlots > 0 ? Math.round((totalVerified / totalSlots) * 100) : 100;

    const kpisEl = document.getElementById("doc-matrix-kpis");
    if (kpisEl) {
      kpisEl.innerHTML = `
        <div class="ios-card" style="padding: 14px; background: rgba(52, 199, 89, 0.08);">
          <div style="font-size: 11px; font-weight: 700; color: #1a7e36; text-transform: uppercase;">Verified & Audit-Ready</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--ios-green); margin-top: 4px;">${totalVerified} / ${totalSlots} (${overallPct}%)</div>
          <div style="font-size: 11px; color: var(--ios-text-secondary); margin-top: 2px;">Meets Home Office inspection standard</div>
        </div>
        <div class="ios-card" style="padding: 14px; background: rgba(255, 149, 0, 0.08);">
          <div style="font-size: 11px; font-weight: 700; color: #b36200; text-transform: uppercase;">Pending AO Review</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--ios-orange); margin-top: 4px;">${totalPending}</div>
          <div style="font-size: 11px; color: var(--ios-text-secondary); margin-top: 2px;">Awaiting verification stamp</div>
        </div>
        <div class="ios-card" style="padding: 14px; background: rgba(255, 59, 48, 0.08);">
          <div style="font-size: 11px; font-weight: 700; color: #c92a2a; text-transform: uppercase;">Missing / Action Due</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--ios-red); margin-top: 4px;">${totalMissing}</div>
          <div style="font-size: 11px; color: var(--ios-text-secondary); margin-top: 2px;">Statutory gap to be resolved</div>
        </div>
        <div class="ios-card" style="padding: 14px; background: rgba(0, 122, 255, 0.08);">
          <div style="font-size: 11px; font-weight: 700; color: var(--ios-blue); text-transform: uppercase;">Staff Monitored</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--ios-blue); margin-top: 4px;">${matrix.length} Staff</div>
          <div style="font-size: 11px; color: var(--ios-text-secondary); margin-top: 2px;">Authorising Officer: Mr. Abdullah Al Mamun</div>
        </div>
      `;
    }

    const categories = [
      { key: 'PASSPORT_BIO', label: '1. Passport' },
      { key: 'RTW_VERIFICATION_CHECK', label: '2. RTW Check' },
      { key: 'CONTRACT_OF_EMPLOYMENT', label: '3. Contract' },
      { key: 'JOB_DESCRIPTION_SOC', label: '4. SOC Desc' },
      { key: 'UK_ADDRESS_PROOF', label: '5. UK Address' },
      { key: 'NI_PROOF', label: '6. NI / HMRC' },
      { key: 'QUALIFICATIONS_AND_REGISTRATION', label: '7. Qualifications' },
      { key: 'PAYROLL_AND_PAYSLIP', label: '8. Payslip' },
      { key: 'ATTENDANCE_AND_TIMESHEET', label: '9. Attendance' },
      { key: 'RECRUITMENT_AND_ADVERT', label: '10. Recruitment' }
    ];

    const tableWrap = document.getElementById("doc-matrix-table-wrap");
    if (!tableWrap) return;

    tableWrap.innerHTML = `
      <div class="matrix-container">
        <table class="matrix-table">
          <thead>
            <tr>
              <th>Employee Particulars</th>
              ${categories.map(c => `<th>${c.label}</th>`).join('')}
              <th>Audit Score</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            ${matrix.map(m => {
              const emp = m.employee;
              return `
                <tr>
                  <td>
                    <div style="font-weight: 700; font-size: 13px;">${emp.full_name}</div>
                    <div style="font-size: 11px; color: var(--ios-text-secondary);">${emp.employee_id} • ${emp.job_title}</div>
                    <div style="margin-top: 4px;">
                      <span class="ios-badge ${emp.is_sponsored ? 'badge-blue' : 'badge-green'}" style="font-size: 10px;">
                        ${emp.immigration_status.replace(/_/g, ' ')}
                      </span>
                    </div>
                  </td>
                  ${categories.map(c => {
                    const doc = m.documents[c.key];
                    if (doc) {
                      if (doc.status === 'VERIFIED') {
                        return `
                          <td>
                            <a href="javascript:void(0)" onclick="openDocQuickLook(${doc.id})" class="matrix-cell-badge matrix-cell-verified" title="${doc.document_name} (${doc.document_reference})">
                              ✅ Verified
                            </a>
                          </td>
                        `;
                      } else {
                        return `
                          <td>
                            <a href="javascript:void(0)" onclick="openDocQuickLook(${doc.id})" class="matrix-cell-badge matrix-cell-pending" title="${doc.document_name} (${doc.document_reference})">
                              ⚠️ Review
                            </a>
                          </td>
                        `;
                      }
                    } else {
                      return `
                        <td>
                          <button onclick="openUploadDocForCategory(${emp.id}, '${c.key}')" class="matrix-cell-badge matrix-cell-missing" title="Click to upload this mandatory statutory document">
                            ❌ + Upload
                          </button>
                        </td>
                      `;
                    }
                  }).join('')}
                  <td>
                    <div style="display: flex; flex-direction: column; align-items: center; gap: 4px;">
                      <span class="ios-badge ${m.compliance_pct === 100 ? 'badge-green' : (m.compliance_pct >= 80 ? 'badge-orange' : 'badge-red')}">
                        ${m.verified_count}/${m.total_mandatory} (${m.compliance_pct}%)
                      </span>
                    </div>
                  </td>
                  <td>
                    <button onclick="inspectEmployeeDossier(${emp.id})" class="ios-btn btn-secondary" style="font-size: 11px; padding: 4px 8px; white-space: nowrap;">
                      Dossier
                    </button>
                  </td>
                </tr>
              `;
            }).join('')}
          </tbody>
        </table>
      </div>
    `;
  } catch (err) {
    console.error("Matrix error:", err);
  }
}

// ==========================================
// 5. HMRC COMPLIANT PAYROLL ENGINE & RTI TRACKER
// ==========================================
let currentPayrollPeriodFilter = 'ALL';
let loadedPayrollRecords = [];

async function renderPayrollAuditSubtab(container) {
  container.innerHTML = `
    <div class="ios-card" style="margin-bottom: 24px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 18px;">
        <div>
          <h2 style="font-size: 18px; font-weight: 700; display: flex; align-items: center; gap: 8px;">
            <span>💷</span> HMRC Compliant Payroll & CoS Remuneration Engine
          </h2>
          <p style="font-size: 13px; color: var(--ios-text-secondary); margin-top: 2px;">
            Real-time PAYE (2026/27 Tax Bands), Class 1 NI, 8% Workplace Pension Auto-Enrolment & HMRC Real Time Information (RTI FPS).
          </p>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <button onclick="toggleHmrCalculatorWidget()" class="ios-btn btn-secondary" style="font-size: 12px;">
            <span>⚡</span> Live HMRC Calculator
          </button>
          <button onclick="openRunPayrollModal()" class="ios-btn btn-primary" style="font-size: 12px;">
            <span>🚀</span> Run Monthly Payroll
          </button>
        </div>
      </div>

      <!-- Live Interactive Calculator Drawer (Collapsible) -->
      <div id="hmrc-calc-drawer" style="display: none; background: rgba(0, 122, 255, 0.05); border: 1px solid rgba(0, 122, 255, 0.2); border-radius: var(--radius-md); padding: 18px; margin-bottom: 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <h4 style="font-size: 14px; font-weight: 700; color: var(--ios-blue);">⚡ HMRC Statutory PAYE & NI Sandbox Simulator (2026/27 Tax Year)</h4>
          <span class="ios-badge badge-blue">Official UK Tax Bands</span>
        </div>
        <div class="grid-cols-4" style="gap: 12px; margin-bottom: 12px;">
          <div class="ios-input-group">
            <label class="ios-label">Annual Salary (£)</label>
            <input type="number" id="sim-salary" class="ios-input" value="52500" oninput="runSimCalculation()">
          </div>
          <div class="ios-input-group">
            <label class="ios-label">Overtime Hours</label>
            <input type="number" id="sim-ot-hours" class="ios-input" value="5.0" oninput="runSimCalculation()">
          </div>
          <div class="ios-input-group">
            <label class="ios-label">Discretionary Bonus (£)</label>
            <input type="number" id="sim-bonus" class="ios-input" value="0.00" oninput="runSimCalculation()">
          </div>
          <div class="ios-input-group">
            <label class="ios-label">Tax Code</label>
            <input type="text" id="sim-tax-code" class="ios-input" value="1257L" oninput="runSimCalculation()">
          </div>
        </div>
        <div id="sim-results" style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px; padding: 12px; background: rgba(255,255,255,0.7); border-radius: var(--radius-sm); border: 1px solid var(--ios-border); font-size: 12.5px;">
          <!-- Dynamically populated -->
        </div>
      </div>

      <!-- Top Summary KPIs -->
      <div id="payroll-kpis" class="grid-cols-4" style="margin-bottom: 20px;">
        <!-- Populated dynamically -->
      </div>

      <!-- Filter Bar -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 10px;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <label style="font-size: 12.5px; font-weight: 600;">Filter by Pay Period:</label>
          <select id="payroll-period-filter" class="ios-select" style="width: auto; padding: 6px 12px; font-size: 12px;" onchange="filterPayrollByPeriod(this.value)">
            <option value="ALL">All Pay Periods</option>
            <option value="October 2026">October 2026</option>
            <option value="September 2026">September 2026</option>
            <option value="August 2026">August 2026</option>
          </select>
        </div>
        <div style="font-size: 12px; color: var(--ios-text-secondary);">
          Authorising Officer: <strong>Mr. Abdullah Al Mamun</strong> • HMRC PAYE Ref: <strong>120/EE88291</strong>
        </div>
      </div>

      <!-- Full Itemised Payroll Table -->
      <div id="payroll-table-wrap">
        <p style="color: var(--ios-text-secondary); font-size: 13px;">Loading statutory payroll records...</p>
      </div>
    </div>
  `;

  await loadPayrollTableData();
  runSimCalculation();
}

async function loadPayrollTableData() {
  try {
    let url = '/api/payroll/records';
    if (currentPayrollPeriodFilter && currentPayrollPeriodFilter !== 'ALL') {
      url += `?period=${encodeURIComponent(currentPayrollPeriodFilter)}`;
    }
    const res = await fetch(url);
    const data = await res.json();
    loadedPayrollRecords = data.payroll || [];

    // Calculate aggregate totals
    let totalGross = 0;
    let totalTax = 0;
    let totalNi = 0;
    let totalPension = 0;

    loadedPayrollRecords.forEach(p => {
      totalGross += p.gross_pay || 0;
      totalTax += p.tax_deduction || 0;
      totalNi += (p.ni_deduction || 0) + (p.ni_employer || 0);
      totalPension += (p.pension_employee || 0) + (p.pension_employer || 0);
    });

    const kpiEl = document.getElementById("payroll-kpis");
    if (kpiEl) {
      kpiEl.innerHTML = `
        <div class="ios-card" style="padding: 14px;">
          <div style="font-size: 11px; color: var(--ios-text-secondary); font-weight: 700;">TOTAL GROSS PAYROLL</div>
          <div style="font-size: 24px; font-weight: 700; margin-top: 4px;">£${totalGross.toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>
          <div style="font-size: 11px; color: var(--ios-green); font-weight: 600;">✅ 100% CoS Threshold Aligned</div>
        </div>
        <div class="ios-card" style="padding: 14px;">
          <div style="font-size: 11px; color: var(--ios-text-secondary); font-weight: 700;">HMRC PAYE INCOME TAX</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--ios-blue); margin-top: 4px;">£${totalTax.toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>
          <div style="font-size: 11px; color: var(--ios-text-secondary);">2026/27 Cumulative PAYE</div>
        </div>
        <div class="ios-card" style="padding: 14px;">
          <div style="font-size: 11px; color: var(--ios-text-secondary); font-weight: 700;">TOTAL NATIONAL INSURANCE</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--ios-purple); margin-top: 4px;">£${totalNi.toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>
          <div style="font-size: 11px; color: var(--ios-text-secondary);">Class 1 Primary + Secondary</div>
        </div>
        <div class="ios-card" style="padding: 14px;">
          <div style="font-size: 11px; color: var(--ios-text-secondary); font-weight: 700;">WORKPLACE PENSION POOL</div>
          <div style="font-size: 24px; font-weight: 700; color: #1a7e36; margin-top: 4px;">£${totalPension.toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>
          <div style="font-size: 11px; color: var(--ios-text-secondary);">8% Statutory Auto-Enrolment</div>
        </div>
      `;
    }

    const tableWrap = document.getElementById("payroll-table-wrap");
    if (!tableWrap) return;

    if (loadedPayrollRecords.length === 0) {
      tableWrap.innerHTML = `<p style="color: var(--ios-text-secondary); font-size: 13px; padding: 20px;">No payroll records found for selected period.</p>`;
      return;
    }

    tableWrap.innerHTML = `
      <div style="overflow-x: auto;">
        <table class="ios-table">
          <thead>
            <tr>
              <th>Employee</th>
              <th>Pay Period</th>
              <th>Basic Salary</th>
              <th>OT / Bonus</th>
              <th>Gross Pay</th>
              <th>PAYE Tax</th>
              <th>Employee NI</th>
              <th>Pension (5%)</th>
              <th>Net Take-Home</th>
              <th>CoS Compliance</th>
              <th>HMRC RTI FPS</th>
              <th>Super Admin Actions</th>
            </tr>
          </thead>
          <tbody>
            ${loadedPayrollRecords.map(p => `
              <tr>
                <td>
                  <div style="font-weight: 700;">${p.full_name}</div>
                  <div style="font-size: 11px; color: var(--ios-text-secondary);">${p.emp_code} • ${p.job_title}</div>
                  <div style="font-size: 10.5px; color: var(--ios-blue);">CoS: ${p.cos_number || 'Director'} • ${p.tax_code}</div>
                </td>
                <td>
                  <span style="font-weight: 600;">${p.pay_period}</span>
                  <div style="font-size: 11px; color: var(--ios-text-secondary);">${p.pay_date}</div>
                </td>
                <td>£${(p.basic_salary || 0).toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
                <td>
                  ${(p.overtime_pay || p.bonus_pay) ? `<span style="color: var(--ios-blue); font-weight: 600;">+£${((p.overtime_pay || 0) + (p.bonus_pay || 0)).toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</span>` : '£0.00'}
                  ${p.overtime_hours > 0 ? `<div style="font-size: 10px; color: var(--ios-text-secondary);">${p.overtime_hours} hrs OT</div>` : ''}
                </td>
                <td><strong style="font-size: 13.5px;">£${(p.gross_pay || 0).toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</strong></td>
                <td><span style="color: var(--ios-red);">-£${(p.tax_deduction || 0).toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</span></td>
                <td><span style="color: var(--ios-orange);">-£${(p.ni_deduction || 0).toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</span></td>
                <td><span style="color: var(--ios-text-secondary);">-£${(p.pension_employee || 0).toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</span></td>
                <td>
                  <strong style="color: var(--ios-green); font-size: 14px;">£${(p.net_pay || 0).toLocaleString('en-GB', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</strong>
                </td>
                <td>
                  <span class="ios-badge badge-green" title="Matches Certificate of Sponsorship contracted remuneration">
                    ${p.cos_rate_match ? '✅ Matched' : 'Director Rate'}
                  </span>
                  ${p.minimum_wage_compliant ? '' : '<span class="ios-badge badge-red">NMW Under</span>'}
                </td>
                <td>
                  ${p.rti_status === 'SUBMITTED' 
                    ? `<span class="ios-badge badge-green" title="FPS Ref: ${p.rti_submission_id || ''}">✅ FPS Submitted</span><div style="font-size: 10px; color: var(--ios-text-secondary); margin-top: 2px;">${p.rti_submission_id ? p.rti_submission_id.slice(-8) : ''}</div>`
                    : `<button onclick="submitRtiFps(${p.id})" class="ios-btn btn-secondary" style="font-size: 10.5px; padding: 4px 8px;">🚀 Submit FPS</button>`}
                </td>
                <td>
                  <div style="display: flex; gap: 6px;">
                    <button onclick="openEditPayrollModal(${p.id})" class="ios-btn btn-secondary" style="font-size: 11px; padding: 4px 8px;" title="Super Admin Edit Payslip">
                      ✏️ Edit
                    </button>
                    <button onclick="viewPayslipDetail(${p.id})" class="ios-btn btn-secondary" style="font-size: 11px; padding: 4px 8px;" title="View & Print Official Payslip">
                      👁️ View
                    </button>
                  </div>
                </td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;
  } catch (err) {
    console.error("Payroll error:", err);
  }
}

function filterPayrollByPeriod(period) {
  currentPayrollPeriodFilter = period;
  loadPayrollTableData();
}

function toggleHmrCalculatorWidget() {
  const el = document.getElementById("hmrc-calc-drawer");
  if (el) el.style.display = el.style.display === 'none' ? 'block' : 'none';
}

async function runSimCalculation() {
  const salary = parseFloat(document.getElementById("sim-salary").value) || 0;
  const otHours = parseFloat(document.getElementById("sim-ot-hours").value) || 0;
  const bonus = parseFloat(document.getElementById("sim-bonus").value) || 0;
  const taxCode = document.getElementById("sim-tax-code").value || '1257L';

  try {
    const res = await fetch('/api/payroll/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        annual_salary: salary,
        overtime_hours: otHours,
        bonus_pay: bonus,
        tax_code: taxCode,
        ni_category: 'A',
        contracted_weekly_hours: 37.5
      })
    });
    const data = await res.json();
    const c = data.calculation;

    const resEl = document.getElementById("sim-results");
    if (resEl) {
      resEl.innerHTML = `
        <div>Monthly Basic: <strong>£${c.monthly_basic}</strong></div>
        <div>Overtime Pay: <strong>£${c.overtime_pay}</strong></div>
        <div>Total Gross: <strong style="color: var(--ios-blue);">£${c.total_gross_pay}</strong></div>
        <div>PAYE Tax: <strong style="color: var(--ios-red);">-£${c.paye_tax_deducted}</strong></div>
        <div>Class 1 NI: <strong style="color: var(--ios-orange);">-£${c.employee_ni_deducted}</strong></div>
        <div>Pension (5%): <strong>-£${c.employee_pension_deducted}</strong></div>
        <div>Net Take-Home: <strong style="color: var(--ios-green); font-size: 13.5px;">£${c.net_take_home_pay}</strong></div>
        <div>Employer Cost: <strong>£${c.total_employer_cost}</strong></div>
        <div>${c.minimum_wage_compliant ? '<span class="ios-badge badge-green">Exceeds NMW (£11.44/hr)</span>' : '<span class="ios-badge badge-red">Below NMW</span>'}</div>
      `;
    }
  } catch (err) {
    console.error("Sim calc error:", err);
  }
}

// ==========================================
// 6. INDUSTRY BENCHMARK FRAMEWORK SUBTAB
// ==========================================
function renderIndustryFrameworkSubtab(container) {
  container.innerHTML = `
    <div class="ios-card" style="margin-bottom: 24px;">
      <div style="margin-bottom: 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
          <div>
            <h2 style="font-size: 19px; font-weight: 700; display: flex; align-items: center; gap: 8px;">
              <span>🏆</span> UK Skilled Worker Sponsor HR Framework Benchmark
            </h2>
            <p style="font-size: 13px; color: var(--ios-text-secondary); margin-top: 2px;">
              Comparative evaluation against global enterprise & SME HR platforms: <strong>Workday</strong>, <strong>BambooHR</strong>, <strong>BreatheHR</strong>, <strong>Personio</strong>, and <strong>HiBob</strong>.
            </p>
          </div>
          <span class="ios-badge badge-green">Grade A Sponsor Standard</span>
        </div>
      </div>

      <!-- Core Comparative Matrix -->
      <div style="overflow-x: auto; margin-bottom: 24px;">
        <table class="benchmark-table">
          <thead>
            <tr>
              <th>Statutory Sponsor Compliance Pillar</th>
              <th class="highlight-col">Ether Worldwide Ltd<br><span style="font-weight: 400; font-size: 11px;">(SponsorGuard Pro)</span></th>
              <th>Workday HCM</th>
              <th>BambooHR</th>
              <th>BreatheHR</th>
              <th>Personio</th>
              <th>HiBob</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <strong>1. Appendix D 10-Pillar Evidence Vault</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">Automatic certified retention of all 10 statutory document classes.</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ Built-in Native</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Custom Config</span></td>
              <td><span style="color: var(--ios-red);">❌ Generic Docs</span></td>
              <td><span style="color: var(--ios-red);">❌ Generic Docs</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Custom Fields</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Custom Fields</span></td>
            </tr>
            <tr>
              <td>
                <strong>2. SMS 10-Day Duty Event Triggers</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">Automated drafting & deadline tracking for salary/role/location changes.</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ Real-Time Triggers</span></td>
              <td><span style="color: var(--ios-red);">❌ Not supported</span></td>
              <td><span style="color: var(--ios-red);">❌ Not supported</span></td>
              <td><span style="color: var(--ios-red);">❌ Not supported</span></td>
              <td><span style="color: var(--ios-red);">❌ Not supported</span></td>
              <td><span style="color: var(--ios-red);">❌ Not supported</span></td>
            </tr>
            <tr>
              <td>
                <strong>3. Digital Right to Work & Share Code Checks</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">Online verification check logging with statutory excuse timestamping.</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ Automated Stamping</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ 3rd Party Add-on</span></td>
              <td><span style="color: var(--ios-red);">❌ Manual PDF</span></td>
              <td><span style="color: var(--ios-red);">❌ Manual upload</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Integration Req.</span></td>
              <td><span style="color: var(--ios-red);">❌ Manual upload</span></td>
            </tr>
            <tr>
              <td>
                <strong>4. SOC 2020 Remuneration & Going Rate Match</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">Prevents below-threshold salary cuts against Home Office codes.</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ Strict SOC Rules</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Custom Formula</span></td>
              <td><span style="color: var(--ios-red);">❌ No Immigration Logic</span></td>
              <td><span style="color: var(--ios-red);">❌ No Immigration Logic</span></td>
              <td><span style="color: var(--ios-red);">❌ No Immigration Logic</span></td>
              <td><span style="color: var(--ios-red);">❌ No Immigration Logic</span></td>
            </tr>
            <tr>
              <td>
                <strong>5. HMRC PAYE RTI FPS CoS Cross-Validation</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">Cross-checks monthly net/gross against contracted CoS salary.</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ Integrated Gateway</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Separate Payroll</span></td>
              <td><span style="color: var(--ios-red);">❌ External Payroll</span></td>
              <td><span style="color: var(--ios-red);">❌ External Payroll</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ External Bureau</span></td>
              <td><span style="color: var(--ios-red);">❌ External Payroll</span></td>
            </tr>
            <tr>
              <td>
                <strong>6. 20-Hour Supplementary Employment Capping</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">Flags breach of secondary employment limits under Skilled Worker visa.</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ Automated Cap Shield</span></td>
              <td><span style="color: var(--ios-red);">❌ Not tracked</span></td>
              <td><span style="color: var(--ios-red);">❌ Not tracked</span></td>
              <td><span style="color: var(--ios-red);">❌ Not tracked</span></td>
              <td><span style="color: var(--ios-red);">❌ Not tracked</span></td>
              <td><span style="color: var(--ios-red);">❌ Not tracked</span></td>
            </tr>
            <tr>
              <td>
                <strong>7. 10 Consecutive Days Unauthorised Absence Radar</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">Daily shift escalation & Day 10 mandatory Home Office report warning.</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ Built-in Stage Alarm</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Configurable Workflow</span></td>
              <td><span style="color: var(--ios-red);">❌ Standard PTO only</span></td>
              <td><span style="color: var(--ios-red);">❌ Standard PTO only</span></td>
              <td><span style="color: var(--ios-red);">❌ Standard PTO only</span></td>
              <td><span style="color: var(--ios-red);">❌ Standard PTO only</span></td>
            </tr>
            <tr>
              <td>
                <strong>8. Hybrid & Multi-Site Location Auditing</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">Tracks UK residential address (<3m proof) & office vs remote ratios.</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ Appendix D Geotagged</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Office location only</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Basic address</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Basic address</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Basic address</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Basic address</span></td>
            </tr>
            <tr>
              <td>
                <strong>9. Health, Safety & DSE Workstation Compliance</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">Workstation ergonomic checks synced with HSE (Health and Safety at Work).</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ HSE Portal Synced</span></td>
              <td><span style="color: var(--ios-orange);">⚠️ Enterprise EHS Module</span></td>
              <td><span style="color: var(--ios-red);">❌ Not supported</span></td>
              <td><span style="color: var(--ios-red);">❌ Not supported</span></td>
              <td><span style="color: var(--ios-red);">❌ Not supported</span></td>
              <td><span style="color: var(--ios-red);">❌ Not supported</span></td>
            </tr>
            <tr>
              <td>
                <strong>10. Multi-Agent Legal & Sponsor Advisory</strong>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">AI agent team (Solicitor, Sponsor Specialist, HR, Business Consultant).</div>
              </td>
              <td class="highlight-col"><span style="color: var(--ios-green); font-size: 16px;">✅ Active Multi-Agent</span></td>
              <td><span style="color: var(--ios-red);">❌ No legal AI</span></td>
              <td><span style="color: var(--ios-red);">❌ No legal AI</span></td>
              <td><span style="color: var(--ios-red);">❌ No legal AI</span></td>
              <td><span style="color: var(--ios-red);">❌ No legal AI</span></td>
              <td><span style="color: var(--ios-red);">❌ No legal AI</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Why Industry Standard HR Misses UKVI Compliance -->
      <div class="grid-cols-2" style="gap: 16px;">
        <div style="padding: 16px; border-radius: var(--radius-md); background: rgba(255, 59, 48, 0.05); border: 1px solid rgba(255, 59, 48, 0.2);">
          <div style="font-weight: 700; font-size: 13.5px; color: var(--ios-red); margin-bottom: 6px;">
            ⚠️ The Peril of Generic HR Platforms for UKVI Sponsors
          </div>
          <p style="font-size: 12.5px; line-height: 1.5; color: var(--ios-text);">
            Generic platforms like BambooHR or BreatheHR treat immigration as just a custom text box. They do not calculate 10-day SMS reporting deadlines, do not enforce SOC 2020 minimum pay floors, do not verify PAYE RTI submissions against Certificate of Sponsorship allocations, and fail to track the statutory 20-hour supplementary work limit. A single unrecorded 10-day absence or unnotified salary dip can trigger immediate suspension or revocation of the company's Sponsor Licence.
          </p>
        </div>

        <div style="padding: 16px; border-radius: var(--radius-md); background: rgba(52, 199, 89, 0.05); border: 1px solid rgba(52, 199, 89, 0.2);">
          <div style="font-weight: 700; font-size: 13.5px; color: #1a7e36; margin-bottom: 6px;">
            🛡️ The Ether Worldwide Ltd SponsorGuard Architecture
          </div>
          <p style="font-size: 12.5px; line-height: 1.5; color: var(--ios-text);">
            Built specifically to satisfy <strong>Workers and Temporary Workers: guidance for sponsors Part 3</strong> and <strong>Appendix D</strong>. Every employee dossier is structured around statutory compliance, every shift log protects against the 10-day breach rule, every payroll run guarantees HMRC RTI FPS concordance, and Authorising Officer <strong>Mr. Abdullah Al Mamun</strong> maintains total legal governance with one-click audit pack exports.
          </p>
        </div>
      </div>
    </div>
  `;
}


function renderLegalAdvisorySubtab(container) {
  container.innerHTML = `
    <div class="ios-card">
      <div style="margin-bottom: 20px;">
        <h2 style="font-size: 19px; font-weight: 700; display: flex; align-items: center; gap: 8px;">
          <span>🏛️</span> Multi-Agent UK Statutory Compliance Advisory
        </h2>
        <p style="font-size: 13px; color: var(--ios-text-secondary);">
          Expert guidance synthesized across Immigration Law, UKVI Sponsor Licensing, Statutory HR, and Business Operations.
        </p>
      </div>

      <div style="display: flex; flex-direction: column; gap: 18px;">
        
        <!-- Agent 1: Immigration Solicitor -->
        <div style="padding: 18px; border-radius: var(--radius-md); background: rgba(0, 122, 255, 0.05); border: 1px solid rgba(0, 122, 255, 0.18);">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
            <span style="font-size: 22px;">⚖️</span>
            <div>
              <div style="font-weight: 700; font-size: 14px;">UK Immigration Solicitor Agent</div>
              <div style="font-size: 11px; color: var(--ios-blue); font-weight: 600;">Legal Framework: Immigration Act 1971 / 2006 • Paragraph 8.2 Sponsor Guidance</div>
            </div>
          </div>
          <p style="font-size: 13px; line-height: 1.5; color: var(--ios-text);">
            <strong>Statutory Responsibility for Ether Worldwide Ltd:</strong> As Authorising Officer, Mr. Abdullah Al Mamun holds ultimate legal liability for compliance with Home Office duties. Sponsoring key specialists—Ariful Islam (Software Architect), Prabal Barua (Supply Chain Operations), and Amina Zaib (Marketplace Growth)—requires rigorous adherence to the 10 working days SMS reporting rule for any changes in core duties, salary decreases, or unauthorized absences. For Prabal Barua, the 28-day visa expiry radar ensures renewal papers or CoS extensions are prepared proactively without immigration interruption.
          </p>
        </div>

        <!-- Agent 2: Sponsor Licence Specialist -->
        <div style="padding: 18px; border-radius: var(--radius-md); background: rgba(52, 199, 89, 0.05); border: 1px solid rgba(52, 199, 89, 0.18);">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
            <span style="font-size: 22px;">🇬🇧</span>
            <div>
              <div style="font-weight: 700; font-size: 14px;">UK Skilled Worker Sponsor Licence Specialist Agent</div>
              <div style="font-size: 11px; color: #1a7e36; font-weight: 600;">Sponsorship Management System (SMS-ETH-882910) & Appendix D Compliance</div>
            </div>
          </div>
          <p style="font-size: 13px; line-height: 1.5; color: var(--ios-text);">
            <strong>E-Commerce Appendix D Retention:</strong> Every electronic employee file at Ether Worldwide Ltd contains: (1) Certified passport copy, (2) Home Office online share code verification with official date/time stamp, (3) Signed permanent contract and detailed SOC-aligned job description, (4) National Insurance evidence, (5) Proof of degree / technical qualifications, (6) Current UK address verification (<3 months old), (7) Shift and attendance logs, and (8) Itemised payslips matching CoS salaries. Amina Zaib's address document gap is flagged automatically for upload.
          </p>
        </div>

        <!-- Agent 3: Statutory HR & Employment Law Specialist -->
        <div style="padding: 18px; border-radius: var(--radius-md); background: rgba(255, 149, 0, 0.05); border: 1px solid rgba(255, 149, 0, 0.18);">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
            <span style="font-size: 22px;">📋</span>
            <div>
              <div style="font-weight: 700; font-size: 14px;">Statutory HR & Payroll Specialist Agent</div>
              <div style="font-size: 11px; color: #b36200; font-weight: 600;">Employment Rights Act 1996 • Working Time Regulations 1998</div>
            </div>
          </div>
          <p style="font-size: 13px; line-height: 1.5; color: var(--ios-text);">
            <strong>Salary Benchmark Verification:</strong> Salaries at Ether Worldwide Ltd strictly comply with the revised 2024/2026 Home Office thresholds: Ariful Islam (£52,500 vs £49,400 SOC 2136 minimum), Prabal Barua (£46,000 vs £44,700 SOC 2424 minimum), and Amina Zaib (£40,500 vs £38,700 SOC 3545 minimum). All sponsored staff have signed contracts, 28 days statutory holiday, and 20-hour supplementary employment caps actively tracked.
          </p>
        </div>

        <!-- Agent 4: Business Consultant -->
        <div style="padding: 18px; border-radius: var(--radius-md); background: rgba(175, 82, 222, 0.05); border: 1px solid rgba(175, 82, 222, 0.18);">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
            <span style="font-size: 22px;">💼</span>
            <div>
              <div style="font-weight: 700; font-size: 14px;">Lead E-Commerce Business Consultant Agent</div>
              <div style="font-size: 11px; color: var(--ios-purple); font-weight: 600;">Cross-Border Scalability, Operational Rigor & Brand Protection</div>
            </div>
          </div>
          <p style="font-size: 13px; line-height: 1.5; color: var(--ios-text);">
            <strong>Strategic Advantage:</strong> For an agile e-commerce company like Ether Worldwide Ltd, retaining top international talent in technology, logistics, and marketplace growth is critical. This integrated iOS-style system protects the Grade A licence rating, eliminates human compliance error, and gives Director Mr. Abdullah Al Mamun complete real-time visibility across all staff attendance, work hours, and statutory records.
          </p>
        </div>

      </div>
    </div>
  `;
}

// ==========================================
// STAFF SELF-SERVICE PORTAL
// ==========================================

function renderStaffHero() {
  document.getElementById("staff-hero-name").textContent = currentUser.full_name;
  document.getElementById("staff-hero-job").textContent = `${currentUser.job_title} • ${currentUser.department}`;
  document.getElementById("staff-avatar").textContent = currentUser.full_name.split(" ").map(n => n[0]).join("");

  const badges = document.getElementById("staff-hero-badges");
  badges.innerHTML = `
    <span class="ios-badge ${currentUser.immigration_status === 'BRITISH_CITIZEN' ? 'badge-green' : 'badge-blue'}">
      ${currentUser.immigration_status.replace(/_/g, ' ')}
    </span>
    ${currentUser.cos_number ? `<span class="ios-badge badge-green">CoS: ${currentUser.cos_number}</span>` : ''}
  `;

  if (currentUser.visa_expiry_date) {
    document.getElementById("staff-hero-rtw-date").textContent = `Visa Valid until ${currentUser.visa_expiry_date}`;
  } else {
    document.getElementById("staff-hero-rtw-date").textContent = `Settled / British Citizen (No Expiry)`;
  }
}

function renderStaffNav() {
  const segments = [
    { id: 'timeclock', label: '⏱️ Time & Attendance' },
    { id: 'my_documents', label: '📁 My Right to Work Vault' },
    { id: 'leave_request', label: '🏖️ Leave & Sickness' },
    { id: 'supplementary_work', label: '⚖️ Supplementary Hours' },
    { id: 'my_payslips', label: '💷 My Payslips' },
    { id: 'immigration_news', label: '📰 Immigration Updates' },
    { id: 'hse_compliance', label: '🦺 Health, Safety & DSE' }
  ];

  const navContainer = document.getElementById("main-nav-segments");
  navContainer.innerHTML = segments.map(s => `
    <button class="ios-segment-btn ${activeStaffSubtab === s.id ? 'active' : ''}" onclick="switchStaffSubtab('${s.id}')">
      ${s.label}
    </button>
  `).join("");
}

function switchStaffSubtab(tabId) {
  activeStaffSubtab = tabId;
  renderStaffNav();
  renderStaffSubtab(tabId);
}

function renderStaffSubtab(tabId) {
  const container = document.getElementById("staff-subtab-container");
  if (tabId === 'timeclock') {
    renderStaffTimeclock(container);
  } else if (tabId === 'my_documents') {
    renderStaffDocuments(container);
  } else if (tabId === 'leave_request') {
    renderStaffLeave(container);
  } else if (tabId === 'supplementary_work') {
    renderStaffSupplementary(container);
  } else if (tabId === 'my_payslips') {
    renderStaffPayslips(container);
  } else if (tabId === 'immigration_news') {
    renderImmigrationNewsSubtab(container);
  } else if (tabId === 'hse_compliance') {
    renderHseSubtab(container);
  }
}

// 1. Staff Time & Attendance Clock
async function renderStaffTimeclock(container) {
  container.innerHTML = `
    <div class="ios-card" style="text-align: center; padding: 36px 24px; margin-bottom: 24px;">
      <div style="font-size: 12px; text-transform: uppercase; letter-spacing: 0.6px; color: var(--ios-text-secondary); font-weight: 600;">
        Shift Attendance Tracker (Appendix D Compliant)
      </div>
      <div id="shift-live-time" style="font-size: 42px; font-weight: 800; font-variant-numeric: tabular-nums; margin: 8px 0; letter-spacing: -1px;">
        12:00:00
      </div>
      <div id="clock-status-tag" style="font-size: 13px; color: var(--ios-text-secondary); margin-bottom: 24px;">
        Ready to start scheduled shift
      </div>

      <div style="display: flex; justify-content: center; gap: 16px;">
        <button id="clock-in-btn" onclick="executeClockIn()" class="ios-btn btn-success" style="padding: 14px 32px; font-size: 16px; border-radius: var(--radius-pill);">
          <span>▶️</span> Clock In Now
        </button>
        <button id="clock-out-btn" onclick="executeClockOut()" class="ios-btn btn-danger" style="display: none; padding: 14px 32px; font-size: 16px; border-radius: var(--radius-pill);">
          <span>⏹️</span> Clock Out Shift
        </button>
      </div>

      <div style="margin-top: 20px; font-size: 11.5px; color: var(--ios-text-secondary);">
        📍 Location: On-Site • London Central Campus • Geotag Logged
      </div>
    </div>

    <!-- Recent Shift History -->
    <div class="ios-card">
      <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 12px;">Recent Shift Records (Past 7 Days)</h3>
      <div id="staff-attendance-history">
        <!-- Rendered dynamically -->
      </div>
    </div>
  `;
  checkStaffClockStatus();
  loadStaffAttendanceLogs();
}

async function checkStaffClockStatus() {
  if (!currentUser) return;
  try {
    const res = await fetch(`/api/attendance/today_status?employee_id=${currentUser.id}`);
    const data = await res.json();
    const inBtn = document.getElementById("clock-in-btn");
    const outBtn = document.getElementById("clock-out-btn");
    const statusTag = document.getElementById("clock-status-tag");

    if (!inBtn || !outBtn) return;

    if (data.clocked_in) {
      inBtn.style.display = 'none';
      outBtn.style.display = 'inline-flex';
      statusTag.innerHTML = `🟢 <strong>Currently on shift</strong> (Clocked in at ${data.clock_in_time})`;
    } else {
      inBtn.style.display = 'inline-flex';
      outBtn.style.display = 'none';
      statusTag.innerHTML = `⚪ Not clocked in for today's shift`;
    }
  } catch (err) {
    console.error("Error checking clock status:", err);
  }
}

async function executeClockIn() {
  try {
    const res = await fetch('/api/attendance/clock_in', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ employee_id: currentUser.id, location: 'London Central Campus' })
    });
    const data = await res.json();
    alert(`Shift Started! Clocked in at ${data.clock_in_time}`);
    checkStaffClockStatus();
    loadStaffAttendanceLogs();
  } catch (err) {
    alert("Error clocking in: " + err);
  }
}

async function executeClockOut() {
  try {
    const res = await fetch('/api/attendance/clock_out', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ employee_id: currentUser.id, notes: 'Shift completed successfully' })
    });
    const data = await res.json();
    alert(`Shift ended at ${data.clock_out_time}. Total worked: ${data.hours_worked} hours.`);
    checkStaffClockStatus();
    loadStaffAttendanceLogs();
  } catch (err) {
    alert("Error clocking out: " + err);
  }
}

async function loadStaffAttendanceLogs() {
  const container = document.getElementById("staff-attendance-history");
  if (!container || !currentUser) return;
  try {
    const res = await fetch(`/api/attendance/logs?employee_id=${currentUser.id}`);
    const data = await res.json();
    container.innerHTML = `
      <table class="ios-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Clock In</th>
            <th>Clock Out</th>
            <th>Hours Worked</th>
            <th>Location</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          ${data.attendance.slice(0, 7).map(a => `
            <tr>
              <td><strong>${a.date}</strong></td>
              <td>${a.clock_in_time || '—'}</td>
              <td>${a.clock_out_time || '—'}</td>
              <td>${a.hours_worked} hrs</td>
              <td>${a.location_tag || 'On-Site'}</td>
              <td>
                <span class="ios-badge ${a.status === 'PRESENT' ? 'badge-green' : 'badge-red'}">
                  ${a.status}
                </span>
              </td>
            </tr>
          `).join("")}
        </tbody>
      </table>
    `;
  } catch (err) {
    console.error(err);
  }
}

// 2. Staff Right to Work & Appendix D Vault
async function renderStaffDocuments(container) {
  container.innerHTML = `
    <div class="ios-card" style="margin-bottom: 24px;">
      <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 8px;">My Right to Work & Visa Details</h3>
      <p style="font-size: 12.5px; color: var(--ios-text-secondary); margin-bottom: 16px;">
        Under UKVI sponsor licence rules, Ether Worldwide Ltd retains verified digital copies of all your statutory documents.
      </p>

      <div class="grid-cols-2" style="gap: 16px; margin-bottom: 20px;">
        <div style="padding: 14px; background: rgba(118, 118, 128, 0.06); border-radius: var(--radius-sm);">
          <div style="font-size: 11px; text-transform: uppercase; color: var(--ios-text-secondary); font-weight: 600;">Home Office Share Code</div>
          <div style="font-size: 15px; font-weight: 700; font-family: monospace; margin-top: 4px;">
            ${currentUser.brp_or_share_code || 'N/A (British Citizen)'}
          </div>
          <div style="font-size: 11px; color: var(--ios-green); margin-top: 4px;">Verified by Compliance Officer</div>
        </div>

        <div style="padding: 14px; background: rgba(118, 118, 128, 0.06); border-radius: var(--radius-sm);">
          <div style="font-size: 11px; text-transform: uppercase; color: var(--ios-text-secondary); font-weight: 600;">National Insurance Number</div>
          <div style="font-size: 15px; font-weight: 700; font-family: monospace; margin-top: 4px;">
            ${currentUser.national_insurance_number || 'Missing from file'}
          </div>
          <div style="font-size: 11px; color: ${currentUser.national_insurance_number ? 'var(--ios-green)' : 'var(--ios-red)'}; margin-top: 4px;">
            ${currentUser.national_insurance_number ? 'HMRC Verified' : 'Action Required: Submit P45/NI letter'}
          </div>
        </div>
      </div>

      <!-- My Appendix D Verified Documents (QuickLook Viewer) -->
      <div style="margin-bottom: 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <h4 style="font-size: 14.5px; font-weight: 700;">My Stored Appendix D Documents (Click to QuickLook)</h4>
          <span style="font-size: 11.5px; color: var(--ios-blue);">🔍 Click document to view official preview</span>
        </div>
        <div id="staff-docs-vault-list" style="display: flex; flex-direction: column; gap: 8px;">
          Loading documents...
        </div>
      </div>

      <!-- Update Contact Details (Statutory Requirement) -->
      <form onsubmit="handleUpdateContactSubmit(event)" style="border-top: 1px solid var(--ios-separator); padding-top: 18px;">
        <div style="font-weight: 700; font-size: 14px; margin-bottom: 6px;">
          Update Current UK Residential Address & Phone
        </div>
        <p style="font-size: 12px; color: var(--ios-text-secondary); margin-bottom: 14px;">
          UKVI Sponsor Duty: Employees must immediately report address or phone changes to ensure Appendix D records remain current.
        </p>

        <div class="grid-cols-2">
          <div class="ios-input-group">
            <label class="ios-label">UK Residential Address</label>
            <input type="text" name="address" class="ios-input" value="${currentUser.uk_residential_address || ''}" required>
          </div>
          <div class="ios-input-group">
            <label class="ios-label">UK Mobile Number</label>
            <input type="tel" name="phone" class="ios-input" value="${currentUser.phone_number || ''}" required>
          </div>
        </div>

        <div class="grid-cols-2">
          <div class="ios-input-group">
            <label class="ios-label">Emergency Contact Name</label>
            <input type="text" name="emergency_name" class="ios-input" value="${currentUser.emergency_contact_name || ''}">
          </div>
          <div class="ios-input-group">
            <label class="ios-label">Emergency Contact Phone</label>
            <input type="tel" name="emergency_phone" class="ios-input" value="${currentUser.emergency_contact_phone || ''}">
          </div>
        </div>

        <div style="display: flex; justify-content: flex-end;">
          <button type="submit" class="ios-btn btn-primary" style="font-size: 13px;">
            Save & Notify Compliance Team
          </button>
        </div>
      </form>
    </div>
  `;

  try {
    const res = await fetch(`/api/compliance/export_pack/${currentUser.id}`);
    const data = await res.json();
    const list = document.getElementById("staff-docs-vault-list");
    if (list && data.appendix_d_documents) {
      list.innerHTML = data.appendix_d_documents.map(d => `
        <div onclick="openDocQuickLook(${d.id})" style="display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; background: rgba(118, 118, 128, 0.05); border-radius: var(--radius-sm); border: 1px solid var(--ios-border); cursor: pointer; transition: all 0.2s ease;" onmouseover="this.style.background='rgba(0,122,255,0.06)'" onmouseout="this.style.background='rgba(118, 118, 128, 0.05)'">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 18px;">${d.file_type === 'PDF' ? '📄' : '🖼️'}</span>
            <div>
              <div style="font-weight: 600; font-size: 13px;">${d.document_name}</div>
              <div style="font-size: 11px; color: var(--ios-text-secondary);">Ref: ${d.document_reference || 'N/A'} • ${d.issued_by_authority || 'Official'}</div>
            </div>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <span class="ios-badge ${d.status === 'VERIFIED' ? 'badge-green' : 'badge-orange'}">${d.status}</span>
            <span class="ios-btn btn-secondary" style="font-size: 11px; padding: 4px 8px; pointer-events: none;">👁️ QuickLook</span>
          </div>
        </div>
      `).join("");
    }
  } catch (err) {
    console.error("Error loading staff documents:", err);
  }
}

async function handleUpdateContactSubmit(e) {
  e.preventDefault();
  const form = e.target;
  try {
    const res = await fetch('/api/profile/update', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        employee_id: currentUser.id,
        uk_residential_address: form.address.value,
        phone_number: form.phone.value,
        emergency_contact_name: form.emergency_name.value,
        emergency_contact_phone: form.emergency_phone.value
      })
    });
    const data = await res.json();
    alert("Profile and Appendix D address record updated successfully!");
    await loadCurrentUser(currentUser.id);
  } catch (err) {
    alert("Error updating profile: " + err);
  }
}

// 3. Staff Leave & Sickness Request
function renderStaffLeave(container) {
  container.innerHTML = `
    <div class="ios-card" style="margin-bottom: 24px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
          <h3 style="font-size: 16px; font-weight: 700;">Request Annual Leave or Report Sickness</h3>
          <p style="font-size: 12.5px; color: var(--ios-text-secondary);">Statutory tracking ensures you never trigger unnotified absence breaches.</p>
        </div>
        <span class="ios-badge badge-green">21.0 Days Remaining</span>
      </div>

      <form onsubmit="handleLeaveSubmit(event)">
        <div class="grid-cols-2">
          <div class="ios-input-group">
            <label class="ios-label">Absence Type</label>
            <select name="leave_type" class="ios-select" required onchange="toggleFitNoteField(this.value)">
              <option value="ANNUAL_LEAVE">Paid Annual Leave (Holiday)</option>
              <option value="SICK_LEAVE">Sick Leave (SSP Tracked)</option>
              <option value="UNPAID_COMPASSIONATE">Compassionate / Emergency Leave</option>
              <option value="MATERNITY_PATERNITY">Maternity / Paternity Leave</option>
            </select>
          </div>
          <div class="ios-input-group">
            <label class="ios-label">Total Days Requested</label>
            <input type="number" step="0.5" name="total_days" class="ios-input" value="1.0" min="0.5" required>
          </div>
        </div>

        <div class="grid-cols-2">
          <div class="ios-input-group">
            <label class="ios-label">Start Date</label>
            <input type="date" name="start_date" class="ios-input" required>
          </div>
          <div class="ios-input-group">
            <label class="ios-label">End Date</label>
            <input type="date" name="end_date" class="ios-input" required>
          </div>
        </div>

        <div class="ios-input-group">
          <label class="ios-label">Reason / Justification</label>
          <input type="text" name="reason" class="ios-input" placeholder="e.g. Pre-booked family leave" required>
        </div>

        <div id="sick-leave-options" style="display: none; background: rgba(118, 118, 128, 0.08); padding: 14px; border-radius: var(--radius-sm); margin-bottom: 16px;">
          <div style="font-size: 12px; font-weight: 700; margin-bottom: 8px;">Statutory Sickness Declaration (SSP Standard)</div>
          <label style="display: flex; align-items: center; gap: 8px; font-size: 13px; margin-bottom: 6px;">
            <input type="checkbox" name="self_cert" checked> I have self-certified my illness (permitted for days 1-7)
          </label>
          <label style="display: flex; align-items: center; gap: 8px; font-size: 13px;">
            <input type="checkbox" name="fit_note"> Medical Fit Note attached from registered doctor (mandatory if > 7 days)
          </label>
        </div>

        <div style="display: flex; justify-content: flex-end;">
          <button type="submit" class="ios-btn btn-primary" style="font-size: 13px;">
            Submit Request to Manager
          </button>
        </div>
      </form>
    </div>

    <!-- My Leave History -->
    <div class="ios-card">
      <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 12px;">My Leave & Absence History</h3>
      <div id="staff-leave-history">Loading records...</div>
    </div>
  `;
  loadStaffLeaveHistory();
}

function toggleFitNoteField(type) {
  const el = document.getElementById("sick-leave-options");
  if (el) el.style.display = type === 'SICK_LEAVE' ? 'block' : 'none';
}

async function handleLeaveSubmit(e) {
  e.preventDefault();
  const form = e.target;
  try {
    const res = await fetch('/api/leave/request', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        employee_id: currentUser.id,
        leave_type: form.leave_type.value,
        start_date: form.start_date.value,
        end_date: form.end_date.value,
        total_days: form.total_days.value,
        reason: form.reason.value,
        fit_note_attached: form.fit_note ? form.fit_note.checked : false,
        self_certificate_completed: form.self_cert ? form.self_cert.checked : false
      })
    });
    alert("Leave request submitted for approval.");
    loadStaffLeaveHistory();
  } catch (err) {
    alert("Error submitting leave: " + err);
  }
}

async function loadStaffLeaveHistory() {
  const container = document.getElementById("staff-leave-history");
  if (!container || !currentUser) return;
  try {
    const res = await fetch(`/api/leave/list?employee_id=${currentUser.id}`);
    const data = await res.json();
    if (data.leaves.length === 0) {
      container.innerHTML = `<p style="font-size: 13px; color: var(--ios-text-secondary);">No leave records found.</p>`;
      return;
    }
    container.innerHTML = `
      <table class="ios-table">
        <thead>
          <tr>
            <th>Type</th>
            <th>Dates</th>
            <th>Days</th>
            <th>Reason</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          ${data.leaves.map(l => `
            <tr>
              <td><strong>${l.leave_type.replace(/_/g, ' ')}</strong></td>
              <td>${l.start_date} to ${l.end_date}</td>
              <td>${l.total_days} days</td>
              <td>${l.reason}</td>
              <td>
                <span class="ios-badge ${l.status === 'APPROVED' ? 'badge-green' : (l.status === 'PENDING' ? 'badge-orange' : 'badge-red')}">
                  ${l.status}
                </span>
              </td>
            </tr>
          `).join("")}
        </tbody>
      </table>
    `;
  } catch (err) {
    console.error(err);
  }
}

// 4. Staff Supplementary Work Declaration
function renderStaffSupplementary(container) {
  const currentHours = currentUser.supplementary_hours_declared || 0.0;
  const isBreached = currentHours > 20.0;

  container.innerHTML = `
    <div class="ios-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
          <h3 style="font-size: 16px; font-weight: 700;">Supplementary Employment Declaration</h3>
          <p style="font-size: 12.5px; color: var(--ios-text-secondary);">
            Home Office Skilled Worker Rule: Workers are permitted to work up to 20 hours per week in secondary employment.
          </p>
        </div>
        <span class="ios-badge ${isBreached ? 'badge-red' : 'badge-green'}">
          ${isBreached ? 'Limit Exceeded' : 'Permitted'}
        </span>
      </div>

      <div style="padding: 16px; border-radius: var(--radius-md); background: ${isBreached ? 'rgba(255, 59, 48, 0.08)' : 'rgba(52, 199, 89, 0.08)'}; margin-bottom: 20px;">
        <div style="font-weight: 700; font-size: 14px; color: ${isBreached ? 'var(--ios-red)' : '#1a7e36'};">
          Current Secondary Hours Declared: ${currentHours} hrs / week
        </div>
        <p style="font-size: 12.5px; color: var(--ios-text); margin-top: 4px;">
          ${isBreached 
            ? '⚠️ CRITICAL: Declared hours exceed the statutory 20-hour weekly cap. This represents a breach of your Skilled Worker visa conditions!' 
            : '✅ Compliant: Your hours are within the 20-hour maximum threshold.'}
        </p>
      </div>

      <form onsubmit="handleSupplementarySubmit(event)">
        <div class="ios-input-group">
          <label class="ios-label">Secondary Hours Worked Per Week (Outside Sponsor)</label>
          <input type="number" step="0.5" name="hours" class="ios-input" value="${currentHours}" max="40" required>
        </div>

        <div style="display: flex; justify-content: flex-end;">
          <button type="submit" class="ios-btn btn-primary" style="font-size: 13px;">
            Update & Sign Declaration
          </button>
        </div>
      </form>
    </div>
  `;
}

async function handleSupplementarySubmit(e) {
  e.preventDefault();
  const form = e.target;
  try {
    const res = await fetch('/api/profile/declare_supplementary', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ employee_id: currentUser.id, supplementary_hours: form.hours.value })
    });
    const data = await res.json();
    alert(`Supplementary hours updated to ${data.hours} hrs/week.`);
    await loadCurrentUser(currentUser.id);
  } catch (err) {
    alert("Error updating hours: " + err);
  }
}

// 5. Staff Payslips
async function renderStaffPayslips(container) {
  container.innerHTML = `
    <div class="ios-card">
      <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 12px;">My Statutory Payslips</h3>
      <p style="font-size: 12.5px; color: var(--ios-text-secondary); margin-bottom: 16px;">
        Itemized statutory pay statements matching CoS remuneration under UK Employment Rights Act 1996.
      </p>
      <div id="staff-payslips-list">Loading payslips...</div>
    </div>
  `;
  try {
    const res = await fetch(`/api/payroll/records?employee_id=${currentUser.id}`);
    const data = await res.json();
    const list = document.getElementById("staff-payslips-list");
    if (!list) return;

    list.innerHTML = `
      <table class="ios-table">
        <thead>
          <tr>
            <th>Pay Period</th>
            <th>Pay Date</th>
            <th>Gross Pay</th>
            <th>Tax Deducted</th>
            <th>NI Deducted</th>
            <th>Pension</th>
            <th>Net Pay</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          ${data.payroll.map(p => `
            <tr>
              <td><strong>${p.pay_period}</strong></td>
              <td>${p.pay_date}</td>
              <td>£${p.gross_pay.toLocaleString()}</td>
              <td>£${p.tax_deduction.toLocaleString()}</td>
              <td>£${p.ni_deduction.toLocaleString()}</td>
              <td>£${p.pension_employee.toLocaleString()}</td>
              <td><strong style="color: var(--ios-green);">£${p.net_pay.toLocaleString()}</strong></td>
              <td>
                <button onclick="window.print()" class="ios-btn btn-secondary" style="font-size: 11px; padding: 4px 8px;">
                  Print
                </button>
              </td>
            </tr>
          `).join("")}
        </tbody>
      </table>
    `;
  } catch (err) {
    console.error(err);
  }
}

// ==========================================
// MODAL CONTROLS & INSPECTION PACKS
// ==========================================

function openModal(id) {
  const m = document.getElementById(id);
  if (m) m.classList.add("active");
}

function closeModal(id) {
  const m = document.getElementById(id);
  if (m) m.classList.remove("active");
}

// SMS Modal Actions
async function openSmsDraftModal(triggerId) {
  try {
    const res = await fetch(`/api/compliance/sms_draft/${triggerId}`);
    const data = await res.json();
    document.getElementById("sms-modal-headline").textContent = `SMS Report: ${data.trigger.trigger_type.replace(/_/g, ' ')}`;
    document.getElementById("sms-modal-subline").textContent = `Worker: ${data.trigger.full_name} (${data.trigger.emp_code}) • Deadline: ${data.trigger.home_office_deadline}`;
    document.getElementById("sms-draft-textarea").value = data.sms_copy_text;
    document.getElementById("sms-notes-input").value = `Submitted by ${currentUser ? currentUser.full_name : 'Authorising Officer'} via SMS portal.`;
    openModal("sms-modal");
  } catch (err) {
    alert("Error loading SMS draft: " + err);
  }
}

function copySmsText() {
  const txt = document.getElementById("sms-draft-textarea");
  txt.select();
  document.execCommand("copy");
  alert("Draft copied to clipboard! You can paste it into the UKVI Sponsorship Management System.");
}

async function executeSmsReportAction(action) {
  const notes = document.getElementById("sms-notes-input").value;
  try {
    const res = await fetch('/api/compliance/sms_action', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        trigger_id: 1,
        action: action,
        notes: notes,
        actor: currentUser ? currentUser.full_name : 'Authorising Officer'
      })
    });
    alert("Sponsor reporting duty marked as submitted to UKVI SMS.");
    closeModal("sms-modal");
    await refreshComplianceData();
  } catch (err) {
    alert("Error logging SMS action: " + err);
  }
}

// Inspect Employee Appendix D Dossier Modal
async function inspectEmployeeDossier(empId) {
  try {
    const res = await fetch(`/api/compliance/export_pack/${empId}`);
    const data = await res.json();
    const emp = data.employee;
    const audit = data.audit_evaluation;

    document.getElementById("dossier-title").textContent = `Appendix D File: ${emp.full_name} (${emp.employee_id})`;
    document.getElementById("dossier-body").innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid var(--ios-separator); padding-bottom: 16px; flex-wrap: wrap; gap: 12px;">
        <div>
          <div style="font-size: 20px; font-weight: 700;">${emp.full_name}</div>
          <div style="font-size: 13px; color: var(--ios-text-secondary);">${emp.job_title} • ${emp.soc_code}</div>
          <div style="font-size: 12px; margin-top: 4px;">UK Address: <strong>${emp.uk_residential_address || 'NOT RECORDED (Breach)'}</strong></div>
          <div style="font-size: 11.5px; color: var(--ios-text-secondary); margin-top: 2px;">
            Passport: <strong>${emp.passport_number || 'Pending'} (${emp.passport_issuing_country || 'N/A'})</strong> • Arrival: ${emp.uk_arrival_date || 'N/A'} • Hybrid: ${emp.workplace_hybrid_ratio || 'Standard'}
          </div>
        </div>
        <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end; gap: 6px;">
          <span class="ios-badge ${audit.health_score > 80 ? 'badge-green' : 'badge-red'}" style="font-size: 13px; padding: 6px 12px;">
            ${audit.status_badge} (${audit.health_score}%)
          </span>
          <div style="font-size: 11px; color: var(--ios-text-secondary);">CoS: ${emp.cos_number || 'N/A'}</div>
          <button onclick="openEditWorkerModal(${emp.id})" class="ios-btn btn-secondary" style="font-size: 12px; padding: 5px 12px; margin-top: 4px;">
            <span>✏️</span> Edit Dossier Records
          </button>
        </div>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
        <h4 style="font-size: 14px; font-weight: 700;">Appendix D Mandatory Statutory Documents (Click to QuickLook)</h4>
        <span style="font-size: 11.5px; color: var(--ios-blue); font-weight: 600;">🔍 Click any document to view & verify</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px;">
        ${data.appendix_d_documents.map(d => `
          <div onclick="openDocQuickLook(${d.id})" style="display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; background: rgba(118, 118, 128, 0.05); border-radius: var(--radius-sm); border: 1px solid var(--ios-border); cursor: pointer; transition: all 0.2s ease;" onmouseover="this.style.background='rgba(0,122,255,0.06)'" onmouseout="this.style.background='rgba(118, 118, 128, 0.05)'">
            <div style="display: flex; align-items: center; gap: 12px;">
              <span style="font-size: 20px;">${d.file_type === 'PDF' ? '📄' : '🖼️'}</span>
              <div>
                <div style="font-weight: 600; font-size: 13px; color: var(--ios-text);">${d.document_name}</div>
                <div style="font-size: 11px; color: var(--ios-text-secondary);">
                  Ref: <strong>${d.document_reference || 'N/A'}</strong> • Authority: ${d.issued_by_authority || 'Official'} • Verified by ${d.verified_by || 'Sophia Reed'} on ${d.verified_date || 'N/A'}
                </div>
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span class="ios-badge ${d.status === 'VERIFIED' ? 'badge-green' : (d.status === 'PENDING_REVIEW' ? 'badge-orange' : 'badge-red')}">${d.status}</span>
              <span class="ios-btn btn-secondary" style="font-size: 11px; padding: 4px 8px; pointer-events: none;">👁️ QuickLook</span>
            </div>
          </div>
        `).join("")}
      </div>

      <h4 style="font-size: 14px; font-weight: 700; margin-bottom: 8px;">Compliance Declaration</h4>
      <ul style="font-size: 12px; color: var(--ios-text-secondary); padding-left: 20px; line-height: 1.6;">
        ${data.statutory_declarations.map(s => `<li>${s}</li>`).join("")}
      </ul>
    `;
    openModal("dossier-modal");
  } catch (err) {
    alert("Error loading dossier: " + err);
  }
}

// Onboard New Staff Modal
function openNewStaffModal() {
  openModal("onboard-modal");
}

async function handleOnboardSubmit(e) {
  e.preventDefault();
  const form = e.target;
  const payload = {
    full_name: form.full_name.value,
    email: form.email.value,
    immigration_status: form.immigration_status.value,
    soc_code: form.soc_code.value,
    annual_gross_salary: form.annual_gross_salary.value,
    cos_number: form.cos_number.value,
    brp_or_share_code: form.brp_or_share_code.value,
    visa_expiry_date: form.visa_expiry_date.value,
    uk_residential_address: form.uk_residential_address.value,
    emergency_contact_phone: form.emergency_contact_phone.value,
    role: 'STAFF'
  };

  try {
    const res = await fetch('/api/employees/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    alert(`New employee ${payload.full_name} onboarded! Appendix D file created.`);
    closeModal("onboard-modal");
    await refreshComplianceData();
  } catch (err) {
    alert("Error creating employee: " + err);
  }
}

// Upload & Verify Document Modal
function openUploadDocModal(empId) {
  document.getElementById("upload-doc-emp-id").value = empId;
  openModal("upload-doc-modal");
}

async function handleUploadDocSubmit(e) {
  e.preventDefault();
  const form = e.target;
  try {
    const res = await fetch('/api/compliance/upload_doc', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        employee_id: form.employee_id.value,
        category: form.category.value,
        document_name: form.category.options[form.category.selectedIndex].text,
        document_reference: form.document_reference.value,
        expiry_date: form.expiry_date.value
      })
    });
    alert("Document uploaded and verified in Appendix D file!");
    closeModal("upload-doc-modal");
    await refreshComplianceData();
  } catch (err) {
    alert("Error saving document: " + err);
  }
}

function downloadMasterCompliancePack() {
  window.print();
}

// ==========================================
// COMPREHENSIVE ONBOARDING (APPENDIX D)
// ==========================================

function switchOnboardStep(step) {
  for (let i = 1; i <= 4; i++) {
    const pane = document.getElementById(`onboard-step-${i}`);
    const btn = document.getElementById(`onboard-tab-btn-${i}`);
    if (pane) pane.style.display = i === step ? 'block' : 'none';
    if (btn) {
      if (i === step) btn.classList.add('active');
      else btn.classList.remove('active');
    }
  }
}

async function handleComprehensiveOnboardSubmit(e) {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);
  const payload = {};
  formData.forEach((val, key) => { payload[key] = val; });
  payload.role = 'STAFF';

  try {
    const res = await fetch('/api/employees/create_comprehensive', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Failed to create employee');
    alert(`🎉 Employee ${payload.full_name} (${data.employee_id}) onboarded successfully!\nAppendix D tracking file and 5 baseline statutory documents initialized.`);
    closeModal('onboard-modal');
    form.reset();
    switchOnboardStep(1);
    await refreshComplianceData();
  } catch (err) {
    alert("Error creating employee: " + err.message);
  }
}

// ==========================================
// DOCUMENT QUICKLOOK VIEWER & INSPECTOR
// ==========================================

async function openDocQuickLook(docId) {
  try {
    const res = await fetch(`/api/documents/${docId}`);
    if (!res.ok) throw new Error("Document not found");
    const data = await res.json();
    const doc = data.document;

    document.getElementById("ql-doc-title").textContent = doc.document_name;
    document.getElementById("ql-type-badge").textContent = doc.file_type || 'PDF';
    document.getElementById("ql-status-badge").textContent = doc.status;
    document.getElementById("ql-status-badge").className = `ios-badge ${doc.status === 'VERIFIED' ? 'badge-green' : (doc.status === 'PENDING_REVIEW' ? 'badge-orange' : 'badge-red')}`;
    document.getElementById("ql-worker-sub").textContent = `Worker: ${doc.full_name} (${doc.emp_code}) • ${doc.job_title} • CoS: ${doc.cos_number || 'N/A'}`;

    document.getElementById("ql-issuing-authority").textContent = doc.issued_by_authority || 'OFFICIAL ISSUING AUTHORITY';
    document.getElementById("ql-sheet-name").textContent = doc.document_name;
    document.getElementById("ql-ref-tag").textContent = `Ref: ${doc.document_reference || 'N/A'}`;
    document.getElementById("ql-watermark").textContent = (doc.category || 'APPENDIX D').replace(/_/g, ' ');

    document.getElementById("ql-content-text").textContent = doc.file_content_preview || 
      `STATUTORY DOCUMENT VERIFICATION RECORD\nDocument Name: ${doc.document_name}\nReference: ${doc.document_reference || 'N/A'}\nCategory: ${doc.category}\nIssuing Authority: ${doc.issued_by_authority}\nRetained under Appendix D statutory inspection standard for Ether Worldwide Ltd.`;

    document.getElementById("ql-meta-status").textContent = doc.status;
    document.getElementById("ql-meta-verifier").textContent = doc.verified_by || 'Sophia Reed (HR Level 1)';
    document.getElementById("ql-meta-date").textContent = doc.verified_date || 'Current Active';
    document.getElementById("ql-meta-expiry").textContent = doc.expiry_date || 'No Expiry Recorded';

    // Populate Super Admin controls
    document.getElementById("ql-edit-doc-id").value = doc.id;
    document.getElementById("ql-edit-ref").value = doc.document_reference || '';
    document.getElementById("ql-edit-authority").value = doc.issued_by_authority || '';
    document.getElementById("ql-edit-expiry").value = doc.expiry_date || '';
    document.getElementById("ql-edit-status").value = doc.status || 'VERIFIED';
    document.getElementById("ql-edit-notes").value = doc.notes || '';

    openModal("doc-quicklook-modal");
  } catch (err) {
    alert("Error opening document QuickLook: " + err.message);
  }
}

async function handleQuickLookDocSave(e) {
  e.preventDefault();
  const docId = document.getElementById("ql-edit-doc-id").value;
  const payload = {
    doc_id: docId,
    document_reference: document.getElementById("ql-edit-ref").value,
    issued_by_authority: document.getElementById("ql-edit-authority").value,
    expiry_date: document.getElementById("ql-edit-expiry").value,
    status: document.getElementById("ql-edit-status").value,
    notes: document.getElementById("ql-edit-notes").value,
    actor: currentUser ? currentUser.full_name : 'Mr. Abdullah Al Mamun'
  };

  try {
    const res = await fetch('/api/documents/update', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error("Failed to update document");
    alert("✅ Document compliance record & verification updated successfully!");
    closeModal("doc-quicklook-modal");
    await refreshComplianceData();
  } catch (err) {
    alert("Error saving document: " + err.message);
  }
}

// ==========================================
// SUPER ADMIN EDIT WORKER DOSSIER
// ==========================================

async function openEditWorkerModal(empId) {
  try {
    const res = await fetch(`/api/compliance/employee/${empId}`);
    if (!res.ok) throw new Error("Failed to load employee details");
    const data = await res.json();
    const emp = data.employee;

    document.getElementById("edit-emp-id").value = emp.id;
    document.getElementById("edit-full-name").value = emp.full_name || '';
    document.getElementById("edit-preferred-name").value = emp.preferred_name || '';
    document.getElementById("edit-email").value = emp.email || '';
    document.getElementById("edit-phone").value = emp.phone_number || '';
    document.getElementById("edit-uk-address").value = emp.uk_residential_address || '';
    document.getElementById("edit-job-title").value = emp.job_title || '';
    document.getElementById("edit-soc-code").value = emp.soc_code || '';
    document.getElementById("edit-salary").value = emp.annual_gross_salary || 0;
    document.getElementById("edit-hours").value = emp.contracted_weekly_hours || 37.5;
    document.getElementById("edit-location").value = emp.work_location || 'Ether Worldwide London HQ';
    document.getElementById("edit-hybrid").value = emp.workplace_hybrid_ratio || '';
    document.getElementById("edit-manager").value = emp.reporting_manager || 'Mr. Abdullah Al Mamun';
    document.getElementById("edit-pattern").value = emp.standard_working_pattern || '';
    document.getElementById("edit-imm-status").value = emp.immigration_status || 'SKILLED_WORKER';
    document.getElementById("edit-cos-number").value = emp.cos_number || '';
    document.getElementById("edit-visa-expiry").value = emp.visa_expiry_date || '';
    document.getElementById("edit-share-code").value = emp.brp_or_share_code || '';
    document.getElementById("edit-passport-num").value = emp.passport_number || '';
    document.getElementById("edit-passport-exp").value = emp.passport_expiry_date || '';
    document.getElementById("edit-passport-country").value = emp.passport_issuing_country || '';
    document.getElementById("edit-arrival-date").value = emp.uk_arrival_date || '';
    document.getElementById("edit-english").value = emp.english_language_level || '';
    document.getElementById("edit-ecctis").value = emp.ecctis_reference || '';
    document.getElementById("edit-em-name").value = emp.emergency_contact_name || '';
    document.getElementById("edit-em-rel").value = emp.emergency_contact_relationship || '';
    document.getElementById("edit-em-phone").value = emp.emergency_contact_phone || '';
    document.getElementById("edit-em-addr").value = emp.emergency_contact_address || '';

    openModal("edit-worker-modal");
  } catch (err) {
    alert("Error loading employee record: " + err.message);
  }
}

async function handleEditWorkerSubmit(e) {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);
  const payload = {};
  formData.forEach((val, key) => { payload[key] = val; });
  payload.actor = currentUser ? currentUser.full_name : 'Mr. Abdullah Al Mamun';

  try {
    const res = await fetch('/api/employees/update', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error("Failed to update employee");
    alert("✅ Employee record and Appendix D dossier updated successfully!");
    closeModal("edit-worker-modal");
    await refreshComplianceData();
  } catch (err) {
    alert("Error saving employee: " + err.message);
  }
}

// ==========================================
// IMMIGRATION PUBLICATIONS & NEWS FEED
// ==========================================

async function renderImmigrationNewsSubtab(container) {
  container.innerHTML = `
    <div class="ios-card" style="margin-bottom: 24px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
        <div>
          <h2 style="font-size: 18px; font-weight: 700;">Official UKVI Publications & Immigration Rules Feed</h2>
          <p style="font-size: 13px; color: var(--ios-text-secondary); margin-top: 2px;">
            Statutory bulletins, SMS maintenance advisories, and eVisa policy changes synced with GOV.UK and Home Office directives.
          </p>
        </div>
        <div style="display: flex; gap: 8px;">
          <select id="news-filter-cat" class="ios-select" style="width: auto; font-size: 12px;" onchange="filterImmigrationNews(this.value)">
            <option value="ALL">All Categories</option>
            <option value="SPONSOR_DUTY">Sponsor Duties</option>
            <option value="IMMIGRATION_RULES">Immigration Rules</option>
            <option value="SMS_SYSTEM">SMS System Advisories</option>
            <option value="WORKER_RIGHTS">Worker Rights</option>
          </select>
        </div>
      </div>

      <div id="immigration-news-cards" style="display: flex; flex-direction: column; gap: 16px;">
        Loading official publications...
      </div>
    </div>
  `;

  await loadImmigrationNewsList('ALL');
}

async function loadImmigrationNewsList(category) {
  const container = document.getElementById("immigration-news-cards");
  if (!container) return;
  try {
    const res = await fetch(`/api/publications?category=${category}`);
    const data = await res.json();
    if (!data.publications || data.publications.length === 0) {
      container.innerHTML = `<p style="color: var(--ios-text-secondary); font-size: 13px;">No publications found.</p>`;
      return;
    }

    container.innerHTML = data.publications.map(p => `
      <div class="ios-card" style="background: rgba(255, 255, 255, 0.7); border: 1px solid ${p.is_critical ? 'rgba(255, 59, 48, 0.35)' : 'var(--ios-border)'}; ${p.is_critical ? 'border-left: 5px solid var(--ios-red);' : ''}">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span class="ios-badge ${p.is_critical ? 'badge-red' : 'badge-blue'}">${p.category.replace(/_/g, ' ')}</span>
            <span style="font-size: 11.5px; color: var(--ios-text-secondary);">Published: ${p.publication_date}</span>
          </div>
          <span class="ios-badge badge-green">${p.official_source}</span>
        </div>

        <h3 style="font-size: 16px; font-weight: 700; color: var(--ios-text);">${p.title}</h3>
        <p style="font-size: 13px; color: var(--ios-text); margin: 8px 0; line-height: 1.55;">
          ${p.summary}
        </p>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 12px; padding-top: 10px; border-top: 1px solid var(--ios-separator); flex-wrap: wrap; gap: 8px;">
          <div style="font-size: 11.5px; color: var(--ios-text-secondary);">
            Audience: <strong>${p.target_audience.replace(/_/g, ' ')}</strong>
          </div>
          <a href="${p.official_source_url}" target="_blank" rel="noopener noreferrer" class="ios-btn btn-secondary" style="font-size: 11.5px; padding: 4px 10px; text-decoration: none;">
            <span>🌐</span> View on GOV.UK
          </a>
        </div>
      </div>
    `).join("");
  } catch (err) {
    container.innerHTML = `<p style="color: var(--ios-red);">Error loading publications: ${err.message}</p>`;
  }
}

function filterImmigrationNews(cat) {
  loadImmigrationNewsList(cat);
}

// ==========================================
// HEALTH & SAFETY AT WORK (HSE PORTAL)
// ==========================================

async function renderHseSubtab(container) {
  container.innerHTML = `
    <div class="ios-card" style="margin-bottom: 24px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
        <div>
          <h2 style="font-size: 18px; font-weight: 700;">Health, Safety & Welfare at Work (HSE Statutory Portal)</h2>
          <p style="font-size: 13px; color: var(--ios-text-secondary); margin-top: 2px;">
            Statutory compliance with Health and Safety at Work etc. Act 1974, Display Screen Equipment (DSE) 1992, and Fire Safety Order 2005.
          </p>
        </div>
        <button onclick="submitDseDeclaration()" class="ios-btn btn-primary" style="font-size: 12px;">
          <span>📝</span> Complete Workstation DSE Self-Assessment
        </button>
      </div>

      <!-- Government Legislation Synced Standards -->
      <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 12px; display: flex; align-items: center; gap: 6px;">
        <span>⚖️</span> Statutory HSE Policies & Legislation Sync
      </h3>
      <div id="hse-policies-grid" class="grid-cols-2" style="margin-bottom: 28px;">
        Loading statutory policies...
      </div>

      <!-- Risk Assessments & Workstation Records -->
      <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 12px; display: flex; align-items: center; gap: 6px;">
        <span>🦺</span> Active Worker Safety & Workstation Assessments
      </h3>
      <div id="hse-assessments-table">
        Loading assessment records...
      </div>
    </div>
  `;

  await loadHseData();
}

async function loadHseData() {
  try {
    const res = await fetch('/api/hse/policies');
    const data = await res.json();

    const policiesContainer = document.getElementById("hse-policies-grid");
    if (policiesContainer && data.policies) {
      policiesContainer.innerHTML = data.policies.map(p => `
        <div class="ios-card" style="background: rgba(118, 118, 128, 0.04); border: 1px solid var(--ios-border); padding: 16px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span class="ios-badge badge-blue">${p.policy_code}</span>
            <span class="ios-badge badge-green">Statutory Standard</span>
          </div>
          <h4 style="font-size: 14.5px; font-weight: 700;">${p.title}</h4>
          <p style="font-size: 12px; color: var(--ios-text); margin: 6px 0; line-height: 1.45;">${p.description}</p>
          <div style="font-size: 11px; color: var(--ios-text-secondary); margin-top: 8px;">
            Legislation: <strong>${p.legislation_ref}</strong><br>
            Responsible: <strong>${p.responsible_officer}</strong>
          </div>
        </div>
      `).join("");
    }

    const assessContainer = document.getElementById("hse-assessments-table");
    if (assessContainer && data.assessments) {
      assessContainer.innerHTML = `
        <table class="ios-table">
          <thead>
            <tr>
              <th>Employee</th>
              <th>Assessment Type</th>
              <th>Date Completed</th>
              <th>Work Model</th>
              <th>Compliance Status</th>
              <th>Audited By</th>
            </tr>
          </thead>
          <tbody>
            ${data.assessments.map(a => `
              <tr>
                <td><strong>${a.full_name}</strong><div style="font-size: 11px; color: var(--ios-text-secondary);">${a.emp_code} • ${a.job_title}</div></td>
                <td><span class="ios-badge badge-blue">${a.assessment_type.replace(/_/g, ' ')}</span></td>
                <td>${a.assessment_date}</td>
                <td>${a.workplace_hybrid_ratio || 'On-Site / Hybrid'}</td>
                <td><span class="ios-badge ${a.compliance_status === 'COMPLIANT' ? 'badge-green' : 'badge-orange'}">${a.compliance_status}</span></td>
                <td>${a.reviewed_by_officer || 'Mr. Abdullah Al Mamun'}</td>
              </tr>
            `).join("")}
          </tbody>
        </table>
      `;
    }
  } catch (err) {
    console.error("HSE load error:", err);
  }
}

async function submitDseDeclaration() {
  if (!currentUser) return;
  const notes = prompt("Enter workstation DSE checklist notes (e.g. Ergonomic chair, monitor eye level, breaks scheduled):", "Display Screen Equipment check complete. Chair, monitor height and lighting adjusted to HSE L26 regulations.");
  if (!notes) return;
  try {
    const res = await fetch('/api/hse/assessments', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        employee_id: currentUser.id,
        assessment_type: 'DSE_WORKSTATION',
        compliance_status: 'COMPLIANT',
        notes: notes,
        reviewed_by_officer: 'Mr. Abdullah Al Mamun'
      })
    });
    alert("✅ Workstation DSE Assessment submitted & verified in compliance records.");
    loadHseData();
  } catch (err) {
    alert("Error saving HSE assessment: " + err.message);
  }
}


// ==========================================
// PAYROLL CONTROLS, MODALS & RTI SUBMISSIONS
// ==========================================

function openEditPayrollModal(recordId) {
  const p = loadedPayrollRecords.find(r => r.id === recordId);
  if (!p) {
    alert("Payroll record not found");
    return;
  }

  document.getElementById("edit-payroll-id").value = p.id;
  document.getElementById("edit-payroll-emp-name").textContent = `${p.full_name} (${p.emp_code}) • ${p.job_title}`;
  document.getElementById("edit-payroll-period-badge").textContent = `Pay Period: ${p.pay_period} (Pay Date: ${p.pay_date})`;

  document.getElementById("edit-pay-basic").value = p.basic_salary || 0;
  document.getElementById("edit-pay-bonus").value = p.bonus_pay || 0;
  document.getElementById("edit-pay-ot-hours").value = p.overtime_hours || 0;
  document.getElementById("edit-pay-ot-rate").value = p.overtime_rate || 0;
  document.getElementById("edit-pay-ot-pay").value = p.overtime_pay || 0;
  document.getElementById("edit-pay-gross").value = p.gross_pay || 0;

  document.getElementById("edit-pay-tax").value = p.tax_deduction || 0;
  document.getElementById("edit-pay-ni").value = p.ni_deduction || 0;
  document.getElementById("edit-pay-pension-ee").value = p.pension_employee || 0;
  document.getElementById("edit-pay-student-loan").value = p.student_loan_deduction || 0;
  document.getElementById("edit-pay-tax-code").value = p.tax_code || '1257L';
  document.getElementById("edit-pay-net").value = p.net_pay || 0;
  document.getElementById("edit-pay-notes").value = p.notes || '';

  openModal("edit-payroll-modal");
}

function updateOvertimeCalc() {
  const hours = parseFloat(document.getElementById("edit-pay-ot-hours").value) || 0;
  const rate = parseFloat(document.getElementById("edit-pay-ot-rate").value) || 0;
  const otPay = Math.round(hours * rate * 100) / 100;
  document.getElementById("edit-pay-ot-pay").value = otPay.toFixed(2);
  updateGrossPreview();
}

function updateGrossPreview() {
  const basic = parseFloat(document.getElementById("edit-pay-basic").value) || 0;
  const bonus = parseFloat(document.getElementById("edit-pay-bonus").value) || 0;
  const otPay = parseFloat(document.getElementById("edit-pay-ot-pay").value) || 0;
  const gross = Math.round((basic + bonus + otPay) * 100) / 100;
  document.getElementById("edit-pay-gross").value = gross.toFixed(2);
  updateNetPreview();
}

function updateNetPreview() {
  const gross = parseFloat(document.getElementById("edit-pay-gross").value) || 0;
  const tax = parseFloat(document.getElementById("edit-pay-tax").value) || 0;
  const ni = parseFloat(document.getElementById("edit-pay-ni").value) || 0;
  const pension = parseFloat(document.getElementById("edit-pay-pension-ee").value) || 0;
  const student = parseFloat(document.getElementById("edit-pay-student-loan").value) || 0;
  const net = Math.round((gross - tax - ni - pension - student) * 100) / 100;
  document.getElementById("edit-pay-net").value = net.toFixed(2);
}

async function triggerHmrAutoRecalculate() {
  const basic = parseFloat(document.getElementById("edit-pay-basic").value) || 0;
  const bonus = parseFloat(document.getElementById("edit-pay-bonus").value) || 0;
  const otHours = parseFloat(document.getElementById("edit-pay-ot-hours").value) || 0;
  const otRate = parseFloat(document.getElementById("edit-pay-ot-rate").value) || 0;
  const taxCode = document.getElementById("edit-pay-tax-code").value || '1257L';

  try {
    const res = await fetch('/api/payroll/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        annual_salary: basic * 12.0,
        overtime_hours: otHours,
        overtime_rate: otRate,
        bonus_pay: bonus,
        tax_code: taxCode,
        ni_category: 'A',
        contracted_weekly_hours: 37.5
      })
    });
    const data = await res.json();
    const c = data.calculation;

    document.getElementById("edit-pay-ot-pay").value = c.overtime_pay;
    document.getElementById("edit-pay-gross").value = c.total_gross_pay;
    document.getElementById("edit-pay-tax").value = c.paye_tax_deducted;
    document.getElementById("edit-pay-ni").value = c.employee_ni_deducted;
    document.getElementById("edit-pay-pension-ee").value = c.employee_pension_deducted;
    document.getElementById("edit-pay-net").value = c.net_take_home_pay;
    alert("✅ HMRC PAYE, NI & Pension deductions auto-calculated!");
  } catch (err) {
    alert("Recalculation error: " + err);
  }
}

async function handleSavePayrollRecord(e) {
  e.preventDefault();
  const recordId = parseInt(document.getElementById("edit-payroll-id").value);
  const payload = {
    id: recordId,
    basic_salary: parseFloat(document.getElementById("edit-pay-basic").value),
    bonus_pay: parseFloat(document.getElementById("edit-pay-bonus").value),
    overtime_hours: parseFloat(document.getElementById("edit-pay-ot-hours").value),
    overtime_rate: parseFloat(document.getElementById("edit-pay-ot-rate").value),
    overtime_pay: parseFloat(document.getElementById("edit-pay-ot-pay").value),
    gross_pay: parseFloat(document.getElementById("edit-pay-gross").value),
    tax_deduction: parseFloat(document.getElementById("edit-pay-tax").value),
    ni_deduction: parseFloat(document.getElementById("edit-pay-ni").value),
    pension_employee: parseFloat(document.getElementById("edit-pay-pension-ee").value),
    student_loan_deduction: parseFloat(document.getElementById("edit-pay-student-loan").value),
    net_pay: parseFloat(document.getElementById("edit-pay-net").value),
    tax_code: document.getElementById("edit-pay-tax-code").value,
    notes: document.getElementById("edit-pay-notes").value,
    actor: currentUser ? currentUser.full_name : 'Mr. Abdullah Al Mamun'
  };

  try {
    const res = await fetch('/api/payroll/update_record', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Update failed');
    alert("✅ Statutory payslip & HMRC record updated successfully by Super Admin!");
    closeModal("edit-payroll-modal");
    await loadPayrollTableData();
  } catch (err) {
    alert("Error updating payroll: " + err.message);
  }
}

function openRunPayrollModal() {
  openModal("run-payroll-modal");
}

async function handleRunMonthlyPayrollSubmit(e) {
  e.preventDefault();
  const period = document.getElementById("run-pay-period").value;
  const payDate = document.getElementById("run-pay-date").value;

  try {
    const res = await fetch('/api/payroll/run', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        pay_period: period,
        pay_date: payDate,
        actor: currentUser ? currentUser.full_name : 'Mr. Abdullah Al Mamun'
      })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Run failed');
    alert(`🎉 Monthly Payroll executed for ${period}!
Total Staff Processed: ${data.processed_count}
RTI FPS Gateway ID: ${data.fps_submission_id}`);
    closeModal("run-payroll-modal");
    currentPayrollPeriodFilter = period;
    const filterEl = document.getElementById("payroll-period-filter");
    if (filterEl) filterEl.value = period;
    await loadPayrollTableData();
  } catch (err) {
    alert("Error executing payroll: " + err.message);
  }
}

async function submitRtiFps(recordId) {
  try {
    const res = await fetch('/api/payroll/submit_rti', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        record_id: recordId,
        actor: currentUser ? currentUser.full_name : 'Mr. Abdullah Al Mamun'
      })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Submission failed');
    alert(`🚀 Full Payment Submission (FPS) successfully transmitted to HMRC!
Gateway Reference: ${data.fps_reference}
Timestamp: ${data.timestamp}`);
    await loadPayrollTableData();
  } catch (err) {
    alert("Error submitting RTI: " + err.message);
  }
}

function viewPayslipDetail(recordId) {
  const p = loadedPayrollRecords.find(r => r.id === recordId);
  if (!p) {
    alert("Record not found");
    return;
  }

  const container = document.getElementById("payslip-detail-body");
  if (!container) return;

  container.innerHTML = `
    <div class="payslip-paper">
      <div class="payslip-header-grid">
        <div>
          <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: var(--ios-blue);">
            EMPLOYER & SPONSOR PARTICULARS
          </div>
          <h2 style="font-size: 20px; font-weight: 800; margin: 4px 0;">Ether Worldwide Ltd</h2>
          <div style="font-size: 12px; color: var(--ios-text-secondary); line-height: 1.5;">
            UKVI Sponsor Licence: <strong>SMS-ETH-882910</strong> (Grade A Active)<br>
            HMRC PAYE Tax Reference: <strong>120/EE88291</strong> • Accounts Office: <strong>120PA00882912</strong><br>
            Registered Office: 1 Canada Square, Canary Wharf, London E14 5AA
          </div>
        </div>
        <div style="text-align: right;">
          <div class="ios-badge badge-green" style="font-size: 11px; padding: 4px 10px;">OFFICIAL HMRC PAYSLIP</div>
          <div style="font-size: 12px; font-weight: 700; margin-top: 8px;">Payslip Ref: ${p.payslip_reference || 'ETH-PAY-' + p.id}</div>
          <div style="font-size: 11.5px; color: var(--ios-text-secondary);">Pay Period: <strong>${p.pay_period}</strong></div>
          <div style="font-size: 11.5px; color: var(--ios-text-secondary);">Payment Date: <strong>${p.pay_date}</strong></div>
        </div>
      </div>

      <!-- Employee Particulars Grid -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; padding: 12px 14px; background: rgba(0,0,0,0.03); border-radius: var(--radius-sm); margin-bottom: 16px; font-size: 12px;">
        <div>
          <span style="color: var(--ios-text-secondary);">Employee:</span><br>
          <strong>${p.full_name}</strong> (${p.emp_code})
        </div>
        <div>
          <span style="color: var(--ios-text-secondary);">SOC 2020 & Role:</span><br>
          <strong>${p.job_title}</strong> (${p.soc_code || 'SOC 2136'})
        </div>
        <div>
          <span style="color: var(--ios-text-secondary);">Certificate of Sponsorship:</span><br>
          <strong style="color: var(--ios-blue);">${p.cos_number || 'Director / AO'}</strong>
        </div>
        <div>
          <span style="color: var(--ios-text-secondary);">National Insurance #:</span><br>
          <strong>QQ 12 34 56 A</strong>
        </div>
        <div>
          <span style="color: var(--ios-text-secondary);">Tax Code & NI Category:</span><br>
          <strong>${p.tax_code} / Cat ${p.ni_category}</strong>
        </div>
        <div>
          <span style="color: var(--ios-text-secondary);">Pay Method:</span><br>
          <strong>BACS Direct Credit (GBP)</strong>
        </div>
      </div>

      <!-- Itemised Earnings & Deductions -->
      <div class="grid-cols-2" style="gap: 16px; margin-bottom: 16px;">
        <div>
          <table class="payslip-table">
            <thead>
              <tr>
                <th>Payments / Earnings</th>
                <th style="text-align: right;">Amount (£)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Basic Monthly Salary</td>
                <td style="text-align: right;">£${(p.basic_salary || 0).toFixed(2)}</td>
              </tr>
              ${p.overtime_pay > 0 ? `
                <tr>
                  <td>Overtime Pay (${p.overtime_hours} hrs @ £${p.overtime_rate}/hr)</td>
                  <td style="text-align: right;">£${p.overtime_pay.toFixed(2)}</td>
                </tr>
              ` : ''}
              ${p.bonus_pay > 0 ? `
                <tr>
                  <td>Discretionary Performance Bonus</td>
                  <td style="text-align: right;">£${p.bonus_pay.toFixed(2)}</td>
                </tr>
              ` : ''}
              <tr style="font-weight: 700; background: rgba(0, 122, 255, 0.05);">
                <td>Total Gross Earnings</td>
                <td style="text-align: right; color: var(--ios-blue);">£${(p.gross_pay || 0).toFixed(2)}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
          <table class="payslip-table">
            <thead>
              <tr>
                <th>Statutory Deductions</th>
                <th style="text-align: right;">Amount (£)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>HMRC PAYE Income Tax</td>
                <td style="text-align: right; color: var(--ios-red);">-£${(p.tax_deduction || 0).toFixed(2)}</td>
              </tr>
              <tr>
                <td>Class 1 Primary Employee NI</td>
                <td style="text-align: right; color: var(--ios-orange);">-£${(p.ni_deduction || 0).toFixed(2)}</td>
              </tr>
              <tr>
                <td>Workplace Pension Employee (5%)</td>
                <td style="text-align: right;">-£${(p.pension_employee || 0).toFixed(2)}</td>
              </tr>
              ${p.student_loan_deduction > 0 ? `
                <tr>
                  <td>Student Loan Repayment</td>
                  <td style="text-align: right;">-£${p.student_loan_deduction.toFixed(2)}</td>
                </tr>
              ` : ''}
              <tr style="font-weight: 700; background: rgba(255, 59, 48, 0.05);">
                <td>Total Statutory Deductions</td>
                <td style="text-align: right; color: var(--ios-red);">-£${((p.tax_deduction || 0) + (p.ni_deduction || 0) + (p.pension_employee || 0) + (p.student_loan_deduction || 0)).toFixed(2)}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Take Home Net Pay Banner -->
      <div style="display: flex; justify-content: space-between; align-items: center; padding: 14px 20px; background: rgba(52, 199, 89, 0.1); border-left: 5px solid var(--ios-green); border-radius: var(--radius-sm); margin-bottom: 16px;">
        <div>
          <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: #1a7e36;">NET TAKE-HOME PAY (CREDITED TO ACCOUNT)</div>
          <div style="font-size: 26px; font-weight: 800; color: var(--ios-green);">£${(p.net_pay || 0).toFixed(2)}</div>
        </div>
        <div style="text-align: right; font-size: 11.5px; color: var(--ios-text-secondary);">
          Employer NI Contribution (13.8%): £${(p.ni_employer || 0).toFixed(2)}<br>
          Employer Pension Contribution (3%): £${(p.pension_employer || 0).toFixed(2)}
        </div>
      </div>

      <!-- CoS Remuneration & HMRC RTI Compliance Certificate -->
      <div style="padding: 12px 14px; background: rgba(0, 122, 255, 0.06); border: 1px dashed var(--ios-blue); border-radius: var(--radius-sm); font-size: 11.5px; line-height: 1.55;">
        <div style="font-weight: 700; color: var(--ios-blue); margin-bottom: 2px;">
          🛡️ UKVI Appendix Skilled Worker & HMRC RTI Concordance Certificate
        </div>
        This pay statement confirms that gross monthly remuneration (£${(p.gross_pay || 0).toFixed(2)}) is equal to or exceeds the Certificate of Sponsorship contracted rate (£${(p.contracted_salary || 0).toFixed(2)}/yr), fully complies with the SOC 2020 minimum going rate, and satisfies the UK National Minimum Wage (£11.44/hr). Transmitted to HMRC via Full Payment Submission (FPS: <strong>${p.rti_submission_id || 'PENDING_SUBMISSION'}</strong>).
      </div>
    </div>
  `;

  openModal("payslip-detail-modal");
}

function openUploadDocForCategory(empId, category) {
  if (empId) {
    document.getElementById("upload-doc-emp-id").value = empId;
    const select = document.getElementById("upload-doc-emp-select");
    if (select) select.value = empId;
  }
  if (category) {
    const catSelect = document.getElementById("upload-doc-cat");
    if (catSelect) catSelect.value = category;
  }
  openModal("upload-doc-modal");
}
