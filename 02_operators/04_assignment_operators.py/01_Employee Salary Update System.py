"""
======================================================================
🐍 Python Fundamentals

Module 02 : Operators

Application : Employee Salary Update System

Description:
This application demonstrates the practical use of Python
assignment operators through a simple payroll system.

Concepts Covered:
• =
• +=
• -=
• *=
• /=
• //=
• %=
• **=

Difficulty Level : Beginner
Python Version   : 3.x

Author : Krishna Panchal
======================================================================
"""

# =====================================================================
# EMPLOYEE SALARY UPDATE SYSTEM
# =====================================================================

print("=" * 70)
print("              EMPLOYEE SALARY UPDATE SYSTEM")
print("=" * 70)

print("""
Welcome!

This application demonstrates how assignment operators
are used in payroll and salary management systems.

Enter the employee details below.
""")

# =====================================================================
# EMPLOYEE DETAILS
# =====================================================================

print("\n" + "=" * 70)
print("                  EMPLOYEE DETAILS")
print("=" * 70)

employee_name = input("Employee Name      : ")
employee_id = input("Employee ID        : ")
department = input("Department         : ")

salary = float(input("Current Salary (₹) : "))

print("\nEmployee information recorded successfully.")

# =====================================================================
# SALARY UPDATE
# =====================================================================

print("\n" + "=" * 70)
print("                  SALARY UPDATE")
print("=" * 70)

bonus = float(input("Performance Bonus (₹)      : "))
salary += bonus

tax = float(input("Tax Deduction (₹)          : "))
salary -= tax

multiplier = float(input("Performance Multiplier     : "))
salary *= multiplier

months = int(input("Number of Working Months   : "))
monthly_salary = salary
monthly_salary /= months

# =====================================================================
# OTHER ASSIGNMENT OPERATORS
# =====================================================================

print("\n" + "=" * 70)
print("          OTHER ASSIGNMENT OPERATOR EXAMPLES")
print("=" * 70)

rounded_salary = salary
rounded_salary //= 1000

salary_remainder = salary
salary_remainder %= 1000

performance_score = int(input("Performance Score (1-10)   : "))
performance_score **= 2

# =====================================================================
# EMPLOYEE SALARY REPORT
# =====================================================================

print("\n" + "=" * 70)
print("                 EMPLOYEE SALARY REPORT")
print("=" * 70)

print(f"""
Employee Name               : {employee_name}
Employee ID                 : {employee_id}
Department                  : {department}

--------------------------------------------------------------

Final Salary                : ₹{salary:,.2f}

Average Monthly Salary      : ₹{monthly_salary:,.2f}

Salary (Rounded in Thousands)
using //=                   : {rounded_salary}

Salary Remainder
using %=                    : ₹{salary_remainder:,.2f}

Performance Score²
using **=                   : {performance_score}

==============================================================
""")

# =====================================================================
# APPLICATION SUMMARY
# =====================================================================

print("=" * 70)
print("                 APPLICATION SUMMARY")
print("=" * 70)

print("""
This application demonstrated how assignment operators
modify the value of an existing variable.

Assignment Operators Used

✓ =    Assign
✓ +=   Add and Assign
✓ -=   Subtract and Assign
✓ *=   Multiply and Assign
✓ /=   Divide and Assign
✓ //=  Floor Divide and Assign
✓ %=   Modulus and Assign
✓ **=  Exponent and Assign

Instead of writing long expressions repeatedly,
assignment operators update variables in a shorter,
cleaner, and more readable way.
""")

# =====================================================================
# REAL-WORLD APPLICATIONS
# =====================================================================

print("\n" + "=" * 70)
print("               REAL-WORLD APPLICATIONS")
print("=" * 70)

print("""
Assignment operators are widely used in:

💰 Payroll Management Systems

🏦 Banking Applications

🛒 Billing & Checkout Systems

📦 Inventory Management

📈 Financial Analysis

🎮 Game Score Tracking

📊 Data Processing

🤖 Artificial Intelligence

🌐 Web Applications

📱 Mobile Applications
""")

# =====================================================================
# INTERVIEW CORNER
# =====================================================================

print("\n" + "=" * 70)
print("                  INTERVIEW CORNER")
print("=" * 70)

print("""
1. What is an assignment operator?

Answer:
It assigns or updates the value of a variable.

--------------------------------------------------------------

2. What does '+=' do?

Answer:
It adds a value to the existing variable and stores
the updated result in the same variable.

--------------------------------------------------------------

3. What is the difference between '=' and '+='?

Answer:
'=' assigns a new value.

'+=' adds a value to the existing variable and updates it.

--------------------------------------------------------------

4. Why are assignment operators useful?

Answer:
They make code shorter, cleaner, and easier to maintain.

--------------------------------------------------------------

5. Name some real-world applications of assignment operators.

Answer:
Payroll systems, banking software, billing systems,
inventory management, game development, and financial
applications.
""")

# =====================================================================
# COMMON BEGINNER MISTAKES
# =====================================================================

print("\n" + "=" * 70)
print("             COMMON BEGINNER MISTAKES")
print("=" * 70)

print("""
❌ Confusing '=' with '=='.

❌ Forgetting that '+=' updates the existing value.

❌ Using assignment operators before initializing a variable.

❌ Assuming '/=' always returns an integer.

❌ Applying assignment operators to incompatible data types.
""")

# =====================================================================
# PRACTICE CHALLENGE
# =====================================================================

print("\n" + "=" * 70)
print("                PRACTICE CHALLENGE")
print("=" * 70)

print("""
Modify this application by adding:

• House Rent Allowance (HRA)

• Travel Allowance

• Medical Allowance

• Provident Fund Deduction

• Annual Bonus

Update the salary after each operation using the
appropriate assignment operator.
""")

# =====================================================================
# APPLICATION COMPLETED
# =====================================================================

print("\n" + "=" * 70)
print("         APPLICATION COMPLETED SUCCESSFULLY!")
print("=" * 70)

print("""
Application:
💼 Employee Salary Update System

Congratulations!

You have successfully learned how assignment
operators modify and update variables efficiently.

Keep Learning.
Keep Practicing.
Keep Building.

🐍 Python Fundamentals Repository

Author : Krishna Panchal
""")

print("=" * 70)
