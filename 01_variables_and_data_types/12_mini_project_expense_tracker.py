"""
===============================================================================
File    : 12_mini_project_expense_tracker.py
Project : Personal Finance & Expense Analytics System
Author  : Krishna Panchal

Part 1 : User Registration & Financial Profile

Concepts Covered
----------------
✓ Variables
✓ Data Types
✓ Type Casting
✓ User Input
✓ String Operations
✓ Boolean Logic
✓ Identity & Memrship
===============================================================================
"""

print("=" * 80)
print("PERSONAL FINANCE & EXPENSE ANALYTICS SYSTEM")
print("=" * 80)

# ------------------------------------------------------------------------------
# APPLICATION INFORMATION
# ------------------------------------------------------------------------------

APP_NAME = "Personal Finance & Expense Analytics System"
CURRENCY = "INR"

print(f"Application : {APP_NAME}")
print(f"Currency    : {CURRENCY}")

print("\n" + "=" * 80)

# ------------------------------------------------------------------------------
# USER REGISTRATION
# ------------------------------------------------------------------------------

full_name = input("Full Name                : ").title()

age = int(
    input("Age                      : ")
)

occupation = input(
    "Occupation               : "
).title()

city = input(
    "City                     : "
).title()

email = input(
    "Email                    : "
).lower()

phone = input(
    "Phone Number             : "
)

monthly_income = float(
    input("Monthly Income (₹)       : ")
)

monthly_budget = float(
    input("Monthly Budget (₹)       : ")
)

# ------------------------------------------------------------------------------
# FINANCIAL GOALS
# ------------------------------------------------------------------------------

print("\nAvailable Financial Goals")

print("1. Emergency Fund")
print("2. Home Purchase")
print("3. Car Purchase")
print("4. Higher Education")
print("5. Retirement")
print("6. Vacation")

financial_goal = input(
    "\nSelect Goal : "
).title()

# ------------------------------------------------------------------------------
# BANK ACCOUNTS
# ------------------------------------------------------------------------------

bank_accounts = [
    account.strip().title()
    for account in input(
        "\nBank Accounts (comma separated): "
    ).split(",")
]

# ------------------------------------------------------------------------------
# INVESTMENT TYPES
# ------------------------------------------------------------------------------

investments = [
    investment.strip().title()
    for investment in input(
        "Investments (comma separated): "
    ).split(",")
]

# ------------------------------------------------------------------------------
# PROFILE CREATION
# ------------------------------------------------------------------------------

finance_profile = {
    "Name": full_name,
    "Occupation": occupation,
    "City": city,
    "Income": monthly_income,
    "Budget": monthly_budget,
    "Goal": financial_goal
}

finance_reference = finance_profile

finance_copy = finance_profile.copy()

# ------------------------------------------------------------------------------
# PROFILE VALIDATION
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("PROFILE VALIDATION")
print("=" * 80)

email_valid = "@" in email

phone_valid = len(phone) == 10

budget_valid = monthly_budget <= monthly_income

has_bank_account = len(bank_accounts) > 0

has_investment = len(investments) > 0

print(f"Email Valid             : {email_valid}")
print(f"Phone Valid             : {phone_valid}")
print(f"Budget Within Income    : {budget_valid}")
print(f"Bank Account Available  : {has_bank_account}")
print(f"Investment Available    : {has_investment}")

# ------------------------------------------------------------------------------
# IDENTITY OPERATORS
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("IDENTITY ANALYSIS")
print("=" * 80)

print(f"finance_profile is finance_reference : "
      f"{finance_profile is finance_reference}")

print(f"finance_profile == finance_copy      : "
      f"{finance_profile == finance_copy}")

print(f"finance_profile is finance_copy      : "
      f"{finance_profile is finance_copy}")

print("\nMemory Addresses")

print(f"Original  : {id(finance_profile)}")
print(f"Reference : {id(finance_reference)}")
print(f"Copy      : {id(finance_copy)}")

# ------------------------------------------------------------------------------
# FINANCIAL SUMMARY
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("USER FINANCIAL PROFILE")
print("=" * 80)

for key, value in finance_profile.items():
    print(f"{key:<15}: {value}")

print("\nBank Accounts")

for account in bank_accounts:
    print(f"• {account}")

print("\nInvestments")

for investment in investments:
    print(f"• {investment}")

print("\nPart 1 Completed Successfully.")

# ===============================================================================
# PART 2 : EXPENSE MANAGEMENT & BUDGET ANALYSIS
# ===============================================================================

print("\n" + "=" * 80)
print("EXPENSE MANAGEMENT & BUDGET ANALYSIS")
print("=" * 80)

# ------------------------------------------------------------------------------
# EXPENSE CATEGORIES
# ------------------------------------------------------------------------------

expense_categories = [
    "Food",
    "Transportation",
    "Rent",
    "Utilities",
    "Shopping",
    "Entertainment",
    "Healthcare",
    "Education",
    "Others"
]

expenses = {}

print("\nEnter your monthly expenses")

for category in expense_categories:

    amount = float(
        input(f"{category:<18}: ₹")
    )

    expenses[category] = amount

# ------------------------------------------------------------------------------
# CALCULATIONS
# ------------------------------------------------------------------------------

total_expenses = sum(expenses.values())

remaining_budget = monthly_budget - total_expenses

monthly_savings = monthly_income - total_expenses

budget_utilization = (
    total_expenses / monthly_budget
) * 100

savings_rate = (
    monthly_savings / monthly_income
) * 100

highest_expense_category = max(
    expenses,
    key=expenses.get
)

lowest_expense_category = min(
    expenses,
    key=expenses.get
)

highest_expense = expenses[highest_expense_category]

lowest_expense = expenses[lowest_expense_category]

average_expense = (
    total_expenses /
    len(expenses)
)

# ------------------------------------------------------------------------------
# BUDGET STATUS
# ------------------------------------------------------------------------------

if total_expenses > monthly_budget:

    budget_status = "Budget Exceeded"

elif total_expenses >= monthly_budget * 0.9:

    budget_status = "Near Budget Limit"

else:

    budget_status = "Within Budget"

# ------------------------------------------------------------------------------
# SAVINGS STATUS
# ------------------------------------------------------------------------------

if savings_rate >= 40:

    savings_status = "Excellent"

elif savings_rate >= 25:

    savings_status = "Very Good"

elif savings_rate >= 15:

    savings_status = "Good"

elif savings_rate >= 5:

    savings_status = "Average"

else:

    savings_status = "Needs Improvement"

# ------------------------------------------------------------------------------
# EXPENSE REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("MONTHLY EXPENSE REPORT")
print("=" * 80)

for category, amount in expenses.items():

    print(f"{category:<20} ₹{amount:>10,.2f}")

print("-" * 80)

print(f"Total Expenses         : ₹{total_expenses:,.2f}")
print(f"Monthly Income         : ₹{monthly_income:,.2f}")
print(f"Monthly Budget         : ₹{monthly_budget:,.2f}")
print(f"Remaining Budget       : ₹{remaining_budget:,.2f}")
print(f"Monthly Savings        : ₹{monthly_savings:,.2f}")

print("-" * 80)

print(f"Highest Expense        : {highest_expense_category}")
print(f"Amount                 : ₹{highest_expense:,.2f}")

print(f"Lowest Expense         : {lowest_expense_category}")
print(f"Amount                 : ₹{lowest_expense:,.2f}")

print(f"Average Expense        : ₹{average_expense:,.2f}")

print("-" * 80)

print(f"Budget Utilization     : {budget_utilization:.2f}%")
print(f"Savings Rate           : {savings_rate:.2f}%")

print(f"Budget Status          : {budget_status}")
print(f"Savings Status         : {savings_status}")

# ------------------------------------------------------------------------------
# FINANCIAL SCORE
# ------------------------------------------------------------------------------

financial_score = sum([

    budget_status == "Within Budget",

    monthly_savings > 0,

    savings_rate >= 20,

    budget_utilization <= 90,

    has_bank_account,

    has_investment

])

print("\n" + "=" * 80)
print("FINANCIAL SCORECARD")
print("=" * 80)

print(f"Financial Score : {financial_score}/6")

if financial_score == 6:

    financial_grade = "A+"

elif financial_score >= 5:

    financial_grade = "A"

elif financial_score >= 4:

    financial_grade = "B"

elif financial_score >= 3:

    financial_grade = "C"

else:

    financial_grade = "D"

print(f"Financial Grade : {financial_grade}")

print("\nPart 2 Completed Successfully.")

# ===============================================================================
# PART 3 : FINANCIAL ANALYTICS & SMART INSIGHTS
# ===============================================================================

print("\n" + "=" * 80)
print("FINANCIAL ANALYTICS & SMART INSIGHTS")
print("=" * 80)

# ------------------------------------------------------------------------------
# FINANCIAL INPUT
# ------------------------------------------------------------------------------

existing_savings = float(
    input("\nCurrent Savings (₹)        : ")
)

existing_investments = float(
    input("Current Investments (₹)   : ")
)

monthly_debt_payment = float(
    input("Monthly Debt Payment (₹)  : ")
)

financial_dependents = int(
    input("Number of Dependents      : ")
)

# ------------------------------------------------------------------------------
# EMERGENCY FUND ANALYSIS
# ------------------------------------------------------------------------------

recommended_emergency_fund = total_expenses * 6

emergency_fund_ready = (
    existing_savings >= recommended_emergency_fund
)

# ------------------------------------------------------------------------------
# DEBT ANALYSIS
# ------------------------------------------------------------------------------

debt_ratio = (
    monthly_debt_payment / monthly_income
) * 100

if debt_ratio <= 20:
    debt_status = "Healthy"
elif debt_ratio <= 35:
    debt_status = "Manageable"
else:
    debt_status = "High"

# ------------------------------------------------------------------------------
# INVESTMENT ANALYSIS
# ------------------------------------------------------------------------------

investment_ratio = (
    existing_investments / monthly_income
) * 100

investment_ready = all([
    monthly_savings > 0,
    savings_rate >= 20,
    debt_ratio <= 35
])

# ------------------------------------------------------------------------------
# SPENDING PATTERN
# ------------------------------------------------------------------------------

essential_categories = {
    "Food",
    "Rent",
    "Utilities",
    "Healthcare",
    "Education",
    "Transportation"
}

essential_expense = sum(
    expenses[category]
    for category in expenses
    if category in essential_categories
)

non_essential_expense = (
    total_expenses - essential_expense
)

essential_percentage = (
    essential_expense / total_expenses
) * 100

non_essential_percentage = (
    non_essential_expense / total_expenses
) * 100

# ------------------------------------------------------------------------------
# FINANCIAL HEALTH SCORE
# ------------------------------------------------------------------------------

health_score = sum([
    monthly_savings > 0,
    savings_rate >= 20,
    budget_status == "Within Budget",
    emergency_fund_ready,
    investment_ready,
    debt_ratio <= 20,
    has_bank_account,
    has_investment
])

# ------------------------------------------------------------------------------
# SMART RECOMMENDATIONS
# ------------------------------------------------------------------------------

recommendations = []

if savings_rate < 20:
    recommendations.append(
        "Increase monthly savings to at least 20% of your income."
    )

if debt_ratio > 35:
    recommendations.append(
        "Reduce debt obligations to improve financial stability."
    )

if not emergency_fund_ready:
    recommendations.append(
        "Build an emergency fund covering six months of expenses."
    )

if non_essential_percentage > 35:
    recommendations.append(
        "Reduce discretionary spending to improve savings."
    )

if not has_investment:
    recommendations.append(
        "Start investing to build long-term wealth."
    )

# ------------------------------------------------------------------------------
# ANALYTICS REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("FINANCIAL ANALYTICS REPORT")
print("=" * 80)

print(f"Emergency Fund Target     : ₹{recommended_emergency_fund:,.2f}")
print(f"Emergency Fund Ready      : {emergency_fund_ready}")

print("-" * 80)

print(f"Debt Ratio               : {debt_ratio:.2f}%")
print(f"Debt Status              : {debt_status}")

print(f"Investment Ratio         : {investment_ratio:.2f}%")
print(f"Investment Ready         : {investment_ready}")

print("-" * 80)

print(f"Essential Expenses       : ₹{essential_expense:,.2f}")
print(f"Non-Essential Expenses   : ₹{non_essential_expense:,.2f}")

print(f"Essential Spending       : {essential_percentage:.2f}%")
print(f"Non-Essential Spending   : {non_essential_percentage:.2f}%")

print("-" * 80)

print(f"Financial Health Score   : {health_score}/8")

if health_score >= 7:
    health_status = "Excellent"
elif health_score >= 5:
    health_status = "Good"
elif health_score >= 3:
    health_status = "Average"
else:
    health_status = "Needs Improvement"

print(f"Financial Health         : {health_status}")

# ------------------------------------------------------------------------------
# RECOMMENDATIONS
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("SMART RECOMMENDATIONS")
print("=" * 80)

if recommendations:
    for index, suggestion in enumerate(recommendations, start=1):
        print(f"{index}. {suggestion}")
else:
    print("Excellent! Your financial profile is well balanced.")

print("\nPart 3 Completed Successfully.")

# ===============================================================================
# PART 4 : EXECUTIVE FINANCIAL DASHBOARD & FINAL REPORT
# ===============================================================================

print("\n" + "=" * 80)
print("EXECUTIVE FINANCIAL DASHBOARD")
print("=" * 80)

# ------------------------------------------------------------------------------
# OVERALL FINANCIAL PERFORMANCE
# ------------------------------------------------------------------------------

overall_score = financial_score + health_score

maximum_score = 14

overall_percentage = (
    overall_score / maximum_score
) * 100

# ------------------------------------------------------------------------------
# FINANCIAL CLASSIFICATION
# ------------------------------------------------------------------------------

if overall_percentage >= 90:
    financial_class = "Financial Excellence"

elif overall_percentage >= 80:
    financial_class = "Wealth Builder"

elif overall_percentage >= 70:
    financial_class = "Financially Stable"

elif overall_percentage >= 60:
    financial_class = "Improving"

else:
    financial_class = "Needs Financial Planning"

# ------------------------------------------------------------------------------
# GOAL ANALYSIS
# ------------------------------------------------------------------------------

goal_progress = (
    existing_savings /
    recommended_emergency_fund
) * 100

goal_progress = min(goal_progress, 100)

# ------------------------------------------------------------------------------
# NET WORTH
# ------------------------------------------------------------------------------

estimated_net_worth = (
    existing_savings +
    existing_investments -
    (monthly_debt_payment * 12)
)

# ------------------------------------------------------------------------------
# MONTHLY REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("MONTHLY FINANCIAL REPORT")
print("=" * 80)

print(f"Name                     : {full_name}")
print(f"Occupation               : {occupation}")
print(f"City                     : {city}")

print("-" * 80)

print(f"Monthly Income           : ₹{monthly_income:,.2f}")
print(f"Monthly Expenses         : ₹{total_expenses:,.2f}")
print(f"Monthly Savings          : ₹{monthly_savings:,.2f}")
print(f"Savings Rate             : {savings_rate:.2f}%")

print("-" * 80)

print(f"Budget Status            : {budget_status}")
print(f"Financial Health         : {health_status}")
print(f"Financial Grade          : {financial_grade}")

print("-" * 80)

print(f"Emergency Fund Progress  : {goal_progress:.2f}%")
print(f"Estimated Net Worth      : ₹{estimated_net_worth:,.2f}")

print("-" * 80)

print(f"Overall Score            : {overall_score}/{maximum_score}")
print(f"Overall Percentage       : {overall_percentage:.2f}%")
print(f"Financial Classification : {financial_class}")

print("=" * 80)

# ------------------------------------------------------------------------------
# WEALTH BUILDING ROADMAP
# ------------------------------------------------------------------------------

print("WEALTH BUILDING ROADMAP")
print("-" * 80)

roadmap = [
    "Maintain a monthly budget.",
    "Save at least 20% of your income.",
    "Build a six-month emergency fund.",
    "Reduce unnecessary expenses.",
    "Pay off high-interest debt first.",
    "Invest consistently every month.",
    "Review your finances monthly.",
    "Increase income through new skills.",
    "Diversify your investments.",
    "Track your financial goals regularly."
]

for step, item in enumerate(roadmap, start=1):
    print(f"{step}. {item}")

print("=" * 80)

# ------------------------------------------------------------------------------
# FINANCIAL ACHIEVEMENTS
# ------------------------------------------------------------------------------

print("FINANCIAL ACHIEVEMENTS")
print("-" * 80)

if budget_status == "Within Budget":
    print("✅ Budget Managed Successfully")

if savings_rate >= 20:
    print("💰 Healthy Savings Rate")

if emergency_fund_ready:
    print("🛡 Emergency Fund Ready")

if investment_ready:
    print("📈 Investment Ready")

if health_status == "Excellent":
    print("🏆 Excellent Financial Health")

print("=" * 80)

# ------------------------------------------------------------------------------
# FINAL MESSAGE
# ------------------------------------------------------------------------------

if overall_percentage >= 90:
    message = (
        "Outstanding financial discipline! Continue investing "
        "and growing your wealth."
    )

elif overall_percentage >= 75:
    message = (
        "Very good financial habits. Stay consistent and keep "
        "building your emergency fund."
    )

elif overall_percentage >= 60:
    message = (
        "You have a good foundation. Focus on reducing expenses "
        "and increasing savings."
    )

else:
    message = (
        "Review your spending, create a realistic budget, and "
        "build healthy financial habits step by step."
    )

print("FINAL MESSAGE")
print("-" * 80)
print(message)

print("\n" + "=" * 80)
print("PERSONAL FINANCE & EXPENSE ANALYTICS SYSTEM COMPLETED")
print("=" * 80)
