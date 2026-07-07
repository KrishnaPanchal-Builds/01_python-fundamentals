"""
======================================================================
🐍 Python Fundamentals
Module 02 : Operators

Project : Smart Salary & Finance Analyzer

Description:
This project demonstrates the practical use of Python
arithmetic operators by generating a professional salary
and personal finance report.

Concepts Used:
• Addition (+)
• Subtraction (-)
• Multiplication (*)
• Division (/)
• Floor Division (//)
• Modulus (%)
• Exponentiation (**)

Difficulty : Beginner
Python Version : 3.x

Author : Krishna Panchal
======================================================================
"""

# ====================================================================
#                       SMART SALARY & FINANCE ANALYZER
# ====================================================================

print("=" * 70)
print("             SMART SALARY & FINANCE ANALYZER")
print("=" * 70)

print("""
Welcome!

This application generates a professional salary report
using Python Arithmetic Operators.

You will be asked to enter salary details,
allowances, deductions and monthly expenses.

At the end, a complete financial summary
will be generated.
""")

print("=" * 70)

# ====================================================================
# Employee Information
# ====================================================================

print("\nEMPLOYEE INFORMATION")
print("-" * 70)

employee_name = input("Employee Name            : ")
employee_id = input("Employee ID              : ")
department = input("Department               : ")
designation = input("Designation              : ")

# ====================================================================
# Salary Details
# ====================================================================

print("\nSALARY DETAILS")
print("-" * 70)

basic_salary = float(input("Basic Salary (₹)         : "))
hra = float(input("House Rent Allowance     : "))
da = float(input("Dearness Allowance       : "))
medical_allowance = float(input("Medical Allowance        : "))
travel_allowance = float(input("Travel Allowance         : "))
special_allowance = float(input("Special Allowance        : "))
performance_bonus = float(input("Performance Bonus        : "))

# ====================================================================
# Gross Salary Calculation
# ====================================================================

gross_salary = (
    basic_salary
    + hra
    + da
    + medical_allowance
    + travel_allowance
    + special_allowance
    + performance_bonus
)

print("\nGross Salary Calculated Successfully!")

# ====================================================================
# Deduction Details
# ====================================================================

print("\nDEDUCTION DETAILS")
print("-" * 70)

income_tax = float(input("Income Tax               : "))
provident_fund = float(input("Provident Fund           : "))
professional_tax = float(input("Professional Tax         : "))
insurance = float(input("Insurance Premium        : "))
other_deductions = float(input("Other Deductions         : "))

# ====================================================================
# Total Deductions
# ====================================================================

total_deductions = (
    income_tax
    + provident_fund
    + professional_tax
    + insurance
    + other_deductions
)

# ====================================================================
# Net Salary
# ====================================================================

net_salary = gross_salary - total_deductions

print("\nNet Salary Calculated Successfully!")

# ====================================================================
# Monthly Expenses
# ====================================================================

print("\nMONTHLY EXPENSE DETAILS")
print("-" * 70)

house_rent = float(input("House Rent               : "))
food = float(input("Food Expenses            : "))
transport = float(input("Transport Expenses       : "))
electricity = float(input("Electricity Bill         : "))
internet = float(input("Internet Bill            : "))
mobile = float(input("Mobile Recharge          : "))
entertainment = float(input("Entertainment            : "))
shopping = float(input("Shopping                 : "))
other_expenses = float(input("Other Expenses           : "))

# ====================================================================
# Total Monthly Expenses
# ====================================================================

monthly_expenses = (
    house_rent
    + food
    + transport
    + electricity
    + internet
    + mobile
    + entertainment
    + shopping
    + other_expenses
)

# ====================================================================
# Monthly Savings
# ====================================================================

monthly_savings = net_salary - monthly_expenses

# ====================================================================
# Annual Calculations
# ====================================================================

annual_salary = net_salary * 12
annual_expenses = monthly_expenses * 12
annual_savings = monthly_savings * 12

# Savings Percentage

savings_percentage = (
    (monthly_savings / net_salary) * 100
)

print("\nFinancial Analysis Completed Successfully!")

print("\n" + "=" * 70)
print("Generating Financial Report...")
print("=" * 70)

"""
======================================================================

                    PART 1 COMPLETED

Part 2 will include:

✓ Employee Financial Report
✓ Salary Report
✓ Deduction Report
✓ Expense Report
✓ Savings Analysis
✓ Annual Analysis
✓ Final Financial Summary
✓ Beautiful Professional Output

======================================================================
"""

# ====================================================================
# EMPLOYEE FINANCIAL REPORT
# ====================================================================

print("\n" + "=" * 70)
print("                 EMPLOYEE FINANCIAL REPORT")
print("=" * 70)

# ====================================================================
# Employee Details
# ====================================================================

print("\n👤 EMPLOYEE DETAILS")
print("-" * 70)

print(f"Employee Name           : {employee_name}")
print(f"Employee ID             : {employee_id}")
print(f"Department              : {department}")
print(f"Designation             : {designation}")

# ====================================================================
# Salary Breakdown
# ====================================================================

print("\n💰 SALARY BREAKDOWN")
print("-" * 70)

print(f"Basic Salary            : ₹{basic_salary:,.2f}")
print(f"House Rent Allowance    : ₹{hra:,.2f}")
print(f"Dearness Allowance      : ₹{da:,.2f}")
print(f"Medical Allowance       : ₹{medical_allowance:,.2f}")
print(f"Travel Allowance        : ₹{travel_allowance:,.2f}")
print(f"Special Allowance       : ₹{special_allowance:,.2f}")
print(f"Performance Bonus       : ₹{performance_bonus:,.2f}")

print("-" * 70)
print(f"Gross Salary            : ₹{gross_salary:,.2f}")

# ====================================================================
# Deduction Breakdown
# ====================================================================

print("\n➖ DEDUCTION BREAKDOWN")
print("-" * 70)

print(f"Income Tax              : ₹{income_tax:,.2f}")
print(f"Provident Fund          : ₹{provident_fund:,.2f}")
print(f"Professional Tax        : ₹{professional_tax:,.2f}")
print(f"Insurance Premium       : ₹{insurance:,.2f}")
print(f"Other Deductions        : ₹{other_deductions:,.2f}")

print("-" * 70)
print(f"Total Deductions        : ₹{total_deductions:,.2f}")

# ====================================================================
# Net Salary
# ====================================================================

print("\n💵 NET SALARY")
print("-" * 70)

print(f"Net Salary              : ₹{net_salary:,.2f}")

# ====================================================================
# Monthly Expense Report
# ====================================================================

print("\n📊 MONTHLY EXPENSE REPORT")
print("-" * 70)

print(f"House Rent              : ₹{house_rent:,.2f}")
print(f"Food                    : ₹{food:,.2f}")
print(f"Transport               : ₹{transport:,.2f}")
print(f"Electricity             : ₹{electricity:,.2f}")
print(f"Internet                : ₹{internet:,.2f}")
print(f"Mobile Recharge         : ₹{mobile:,.2f}")
print(f"Entertainment           : ₹{entertainment:,.2f}")
print(f"Shopping                : ₹{shopping:,.2f}")
print(f"Other Expenses          : ₹{other_expenses:,.2f}")

print("-" * 70)
print(f"Total Monthly Expenses  : ₹{monthly_expenses:,.2f}")

# ====================================================================
# Savings Analysis
# ====================================================================

print("\n💹 SAVINGS ANALYSIS")
print("-" * 70)

print(f"Monthly Savings         : ₹{monthly_savings:,.2f}")
print(f"Annual Salary           : ₹{annual_salary:,.2f}")
print(f"Annual Expenses         : ₹{annual_expenses:,.2f}")
print(f"Annual Savings          : ₹{annual_savings:,.2f}")
print(f"Savings Percentage      : {savings_percentage:.2f}%")

# ====================================================================
# Financial Summary
# ====================================================================

print("\n📋 FINANCIAL SUMMARY")
print("-" * 70)

print(f"Employee                : {employee_name}")
print(f"Gross Monthly Salary    : ₹{gross_salary:,.2f}")
print(f"Net Monthly Salary      : ₹{net_salary:,.2f}")
print(f"Monthly Expenses        : ₹{monthly_expenses:,.2f}")
print(f"Monthly Savings         : ₹{monthly_savings:,.2f}")
print(f"Annual Savings          : ₹{annual_savings:,.2f}")

print("=" * 70)
print("        FINANCIAL REPORT GENERATED SUCCESSFULLY")
print("=" * 70)

"""
======================================================================

Part 3 will include:

• Project Summary
• Interview Corner
• Common Beginner Mistakes
• Real-World Applications
• Practice Questions
• Mini Challenge
• Project Completion Message

======================================================================
"""

# ====================================================================
# PROJECT SUMMARY
# ====================================================================

print("\n" + "=" * 70)
print("                     PROJECT SUMMARY")
print("=" * 70)

print("""
Congratulations!

You have successfully completed the
Smart Salary & Finance Analyzer.

Throughout this project, you used Python arithmetic
operators to build a real-world financial application.

Arithmetic operators are the foundation of almost every
software application that performs calculations.
""")

# ====================================================================
# INTERVIEW CORNER
# ====================================================================

print("\n" + "=" * 70)
print("                    INTERVIEW CORNER")
print("=" * 70)

print("""
1. Which arithmetic operator is used for exponentiation?
   Answer: **

2. What is the difference between Division (/) and
   Floor Division (//)?

   • Division (/) returns a floating-point value.
   • Floor Division (//) returns the integer quotient.

3. Which operator returns the remainder after division?

   Answer: %

4. Which arithmetic operator is used most frequently in
   financial applications?

   Answer:
   Addition (+), Subtraction (-), Multiplication (*),
   and Division (/)
""")

# ====================================================================
# COMMON BEGINNER MISTAKES
# ====================================================================

print("\n" + "=" * 70)
print("               COMMON BEGINNER MISTAKES")
print("=" * 70)

print("""
❌ Using integer division when decimal values are required.

❌ Confusing Division (/) with Floor Division (//).

❌ Forgetting the order of operations
   (PEMDAS / BODMAS).

❌ Using incorrect variable names that make the
   code difficult to understand.

❌ Forgetting to convert user input into numeric
   data types using int() or float().
""")

# ====================================================================
# REAL-WORLD APPLICATIONS
# ====================================================================

print("\n" + "=" * 70)
print("               REAL-WORLD APPLICATIONS")
print("=" * 70)

print("""
Arithmetic operators are used in:

• Banking Applications
• Payroll Systems
• Billing Software
• GST & Tax Calculators
• E-Commerce Platforms
• Budget Management Apps
• Expense Trackers
• Scientific Calculations
• Data Analysis
• Machine Learning
• Artificial Intelligence
• Game Development
""")

# ====================================================================
# PRACTICE QUESTIONS
# ====================================================================

print("\n" + "=" * 70)
print("                 PRACTICE QUESTIONS")
print("=" * 70)

print("""
1. Write a program to calculate the area and perimeter
   of a square.

2. Create a Body Mass Index (BMI) calculator.

3. Calculate the average of six subject marks.

4. Develop a simple electricity bill calculator.

5. Calculate compound annual savings using arithmetic
   operators.

6. Find the total cost of multiple grocery items.

7. Calculate fuel consumption for a vehicle.

8. Create a monthly budget calculator.

9. Calculate the percentage obtained in an examination.

10. Build your own arithmetic calculator using the
    concepts learned in this lesson.
""")

# ====================================================================
# MINI CHALLENGE
# ====================================================================

print("\n" + "=" * 70)
print("                   MINI CHALLENGE")
print("=" * 70)

print("""
Challenge:

Design a Personal Expense Tracker that asks the user to
enter their monthly income and expenses in different
categories. Calculate:

• Total Expenses
• Monthly Savings
• Annual Savings
• Savings Percentage

Try completing the challenge on your own before moving to
the next lesson.
""")

# ====================================================================
# WHAT'S NEXT?
# ====================================================================

print("\n" + "=" * 70)
print("                    WHAT'S NEXT?")
print("=" * 70)

print("""
Next Lesson:

02_comparison_operators.py

In the next lesson, you will learn how to compare values
using comparison operators such as:

• Equal To (==)
• Not Equal To (!=)
• Greater Than (>)
• Less Than (<)
• Greater Than or Equal To (>=)
• Less Than or Equal To (<=)

These operators form the foundation of decision-making
in Python and prepare you for Conditional Statements.
""")

# ====================================================================
# END OF PROJECT
# ====================================================================

print("\n" + "=" * 70)
print("          PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 70)

print("""
Thank you for completing the

💼 SMART SALARY & FINANCE ANALYZER

Keep Learning.
Keep Practicing.
Keep Building.

🐍 Python Fundamentals Repository
Author: Krishna Panchal

See you in the next lesson!
""")

print("=" * 70)
