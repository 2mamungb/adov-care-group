"""
Ether Worldwide Ltd - HMRC Compliant PAYE Payroll Engine & UKVI Salary Verification Module
Complies with HMRC PAYE Tax Regulations (2026/27), National Insurance Contributions,
Workplace Pensions Act 2008, and Home Office Appendix Skilled Worker minimum going rates.
"""

from typing import Dict, Any, Tuple

# 2026/2027 Statutory Thresholds (Monthly Rates)
TAX_YEAR_DEFAULT = "2026/27"
STANDARD_TAX_CODE = "1257L"
STANDARD_PERSONAL_ALLOWANCE_ANNUAL = 12570.0
STANDARD_PERSONAL_ALLOWANCE_MONTHLY = STANDARD_PERSONAL_ALLOWANCE_ANNUAL / 12.0  # £1,047.50

# Income Tax Bands (Annual & Monthly)
BASIC_RATE_LIMIT_MONTHLY = 4189.17       # £50,270 / 12
HIGHER_RATE_LIMIT_MONTHLY = 10428.33     # £125,140 / 12
BASIC_RATE = 0.20
HIGHER_RATE = 0.40
ADDITIONAL_RATE = 0.45

# National Insurance Category A (Monthly Thresholds)
NI_LEL_MONTHLY = 533.0     # Lower Earnings Limit (Qualifies for state pension)
NI_PT_MONTHLY = 1048.0     # Primary Threshold (Employee starts paying NI)
NI_UEL_MONTHLY = 4189.0    # Upper Earnings Limit
NI_EMPLOYEE_MAIN_RATE = 0.08   # 8% between PT and UEL
NI_EMPLOYEE_UPPER_RATE = 0.02  # 2% above UEL

# Employer Class 1 Secondary NI
NI_SECONDARY_THRESHOLD_MONTHLY = 758.0  # Secondary Threshold
NI_EMPLOYER_RATE = 0.138                # 13.8% above Secondary Threshold

# Auto-Enrolment Workplace Pension (Pensions Act 2008)
PENSION_QUALIFYING_LOWER_MONTHLY = 520.0   # £6,240 / 12
PENSION_QUALIFYING_UPPER_MONTHLY = 4189.0  # £50,270 / 12
STATUTORY_PENSION_EMPLOYEE_RATE = 0.05    # 5%
STATUTORY_PENSION_EMPLOYER_RATE = 0.03    # 3%

# National Minimum Wage Benchmark (per hour)
NATIONAL_MINIMUM_WAGE_HOURLY = 11.44

def parse_tax_code(tax_code: str) -> float:
    """Calculates monthly tax-free allowance from UK Tax Code."""
    code = tax_code.strip().upper()
    if code in ["BR", "0T"]:
        return 0.0
    if code.endswith("L") or code.endswith("M") or code.endswith("N"):
        try:
            num = int(code[:-1].replace("S", "").replace("C", ""))
            return (num * 10) / 12.0
        except ValueError:
            return STANDARD_PERSONAL_ALLOWANCE_MONTHLY
    return STANDARD_PERSONAL_ALLOWANCE_MONTHLY

def calculate_paye_income_tax(taxable_gross: float, tax_code: str = STANDARD_TAX_CODE) -> float:
    """Calculates HMRC PAYE Monthly Income Tax deduction."""
    code = tax_code.strip().upper()
    if code == "BR":
        return round(taxable_gross * BASIC_RATE, 2)
    
    allowance = parse_tax_code(tax_code)
    net_taxable = max(0.0, taxable_gross - allowance)
    if net_taxable <= 0:
        return 0.0

    basic_band_width = BASIC_RATE_LIMIT_MONTHLY - STANDARD_PERSONAL_ALLOWANCE_MONTHLY
    higher_band_width = HIGHER_RATE_LIMIT_MONTHLY - BASIC_RATE_LIMIT_MONTHLY

    tax = 0.0
    if net_taxable <= basic_band_width:
        tax = net_taxable * BASIC_RATE
    elif net_taxable <= (basic_band_width + higher_band_width):
        tax = (basic_band_width * BASIC_RATE) + ((net_taxable - basic_band_width) * HIGHER_RATE)
    else:
        tax = (basic_band_width * BASIC_RATE) + (higher_band_width * HIGHER_RATE) + \
              ((net_taxable - basic_band_width - higher_band_width) * ADDITIONAL_RATE)

    return round(tax, 2)

def calculate_national_insurance(gross_pay: float, ni_category: str = "A") -> Tuple[float, float]:
    """Calculates Employee and Employer Class 1 National Insurance."""
    category = ni_category.strip().upper()[0] if ni_category else "A"
    
    # Employee NI
    employee_ni = 0.0
    if category in ["A", "H", "M"]:
        if gross_pay > NI_PT_MONTHLY:
            main_band_earnings = min(gross_pay, NI_UEL_MONTHLY) - NI_PT_MONTHLY
            employee_ni += main_band_earnings * NI_EMPLOYEE_MAIN_RATE
            if gross_pay > NI_UEL_MONTHLY:
                employee_ni += (gross_pay - NI_UEL_MONTHLY) * NI_EMPLOYEE_UPPER_RATE
    elif category == "C": # State Pension age, zero employee NI
        employee_ni = 0.0

    # Employer NI
    employer_ni = 0.0
    if gross_pay > NI_SECONDARY_THRESHOLD_MONTHLY:
        employer_ni = (gross_pay - NI_SECONDARY_THRESHOLD_MONTHLY) * NI_EMPLOYER_RATE

    return round(employee_ni, 2), round(employer_ni, 2)

def calculate_workplace_pension(gross_pay: float, emp_rate: float = STATUTORY_PENSION_EMPLOYEE_RATE, 
                               empr_rate: float = STATUTORY_PENSION_EMPLOYER_RATE) -> Tuple[float, float]:
    """Calculates Auto-Enrolment Qualifying Earnings Pension Contributions."""
    if gross_pay <= PENSION_QUALIFYING_LOWER_MONTHLY:
        return 0.0, 0.0

    qualifying_earnings = min(gross_pay, PENSION_QUALIFYING_UPPER_MONTHLY) - PENSION_QUALIFYING_LOWER_MONTHLY
    employee_pension = qualifying_earnings * emp_rate
    employer_pension = qualifying_earnings * empr_rate
    return round(employee_pension, 2), round(employer_pension, 2)

def calculate_full_statutory_payslip(
    basic_salary_annual: float,
    overtime_hours: float = 0.0,
    overtime_hourly_rate: float = 0.0,
    bonus_pay: float = 0.0,
    tax_code: str = STANDARD_TAX_CODE,
    ni_category: str = "A",
    pension_employee_rate: float = STATUTORY_PENSION_EMPLOYEE_RATE,
    pension_employer_rate: float = STATUTORY_PENSION_EMPLOYER_RATE,
    student_loan_plan: str = "NONE",
    contracted_weekly_hours: float = 37.5,
    cos_minimum_annual_salary: float = 38700.0
) -> Dict[str, Any]:
    """
    Computes a complete HMRC-compliant itemised payslip and validates against UKVI CoS minimum thresholds.
    """
    monthly_basic = round(basic_salary_annual / 12.0, 2)
    overtime_total = round(overtime_hours * overtime_hourly_rate, 2)
    total_gross = round(monthly_basic + overtime_total + bonus_pay, 2)

    # PAYE Tax
    paye_tax = calculate_paye_income_tax(total_gross, tax_code)

    # National Insurance
    employee_ni, employer_ni = calculate_national_insurance(total_gross, ni_category)

    # Pension
    employee_pension, employer_pension = calculate_workplace_pension(total_gross, pension_employee_rate, pension_employer_rate)

    # Student Loan
    student_loan_deduction = 0.0
    if student_loan_plan == "PLAN_1" and total_gross > 2082.0:
        student_loan_deduction = round((total_gross - 2082.0) * 0.09, 2)
    elif student_loan_plan == "PLAN_2" and total_gross > 2274.0:
        student_loan_deduction = round((total_gross - 2274.0) * 0.09, 2)

    total_deductions = round(paye_tax + employee_ni + employee_pension + student_loan_deduction, 2)
    net_pay = round(total_gross - total_deductions, 2)

    # UKVI Skilled Worker & Minimum Wage Verification
    annualized_pay = round(total_gross * 12.0, 2)
    hourly_effective = round(total_gross / ((contracted_weekly_hours * 52) / 12.0), 2) if contracted_weekly_hours > 0 else 0.0
    
    cos_compliant = annualized_pay >= cos_minimum_annual_salary
    nmw_compliant = hourly_effective >= NATIONAL_MINIMUM_WAGE_HOURLY

    return {
        "monthly_basic": monthly_basic,
        "overtime_hours": overtime_hours,
        "overtime_hourly_rate": overtime_hourly_rate,
        "overtime_total": overtime_total,
        "bonus_pay": bonus_pay,
        "total_gross_pay": total_gross,
        "annualized_gross": annualized_pay,
        "tax_code": tax_code,
        "ni_category": ni_category,
        "paye_tax_deducted": paye_tax,
        "employee_ni_deducted": employee_ni,
        "employer_ni_contribution": employer_ni,
        "employee_pension_deducted": employee_pension,
        "employer_pension_contribution": employer_pension,
        "student_loan_deducted": student_loan_deduction,
        "total_statutory_deductions": total_deductions,
        "net_take_home_pay": net_pay,
        "effective_hourly_rate": hourly_effective,
        "cos_rate_match": 1 if cos_compliant else 0,
        "minimum_wage_compliant": 1 if nmw_compliant else 0,
        "cos_minimum_threshold": cos_minimum_annual_salary,
        "compliance_summary": "✅ HMRC & UKVI Fully Aligned" if (cos_compliant and nmw_compliant) else "⚠️ BREACH: Remuneration below CoS or NMW threshold"
    }
