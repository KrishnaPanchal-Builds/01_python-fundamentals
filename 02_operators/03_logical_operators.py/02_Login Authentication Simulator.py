"""
======================================================================
🐍 Python Fundamentals

Module 02 : Operators

Application : Login Authentication System

Description:
This application demonstrates the practical use of Python
logical operators by simulating a simple login
authentication system.

Only logical operators are used for evaluation.
No conditional statements (if, elif, else) are used.

Concepts Covered:
• and
• or
• not

Difficulty Level : Beginner
Python Version   : 3.x

Author : Krishna Panchal
======================================================================
"""

# =====================================================================
# LOGIN AUTHENTICATION SYSTEM
# =====================================================================

print("=" * 70)
print("                LOGIN AUTHENTICATION SYSTEM")
print("=" * 70)

print("""
Welcome!

This application demonstrates how logical operators
are used internally during the authentication process
of a login system.

First, create your account.

Then, try logging in using your credentials.
""")

# =====================================================================
# CREATE ACCOUNT
# =====================================================================

print("\n" + "=" * 70)
print("                    CREATE ACCOUNT")
print("=" * 70)

full_name = input("Full Name        : ")
phone = input("Phone Number     : ")
email = input("Email Address    : ")

registered_username = input("Create Username  : ")
registered_password = input("Create Password  : ")

print("\nAccount Created Successfully!")

# =====================================================================
# SYSTEM SETTINGS
# =====================================================================

# These values are maintained internally by the system.

two_factor_enabled = True
account_blocked = False

# =====================================================================
# LOGIN
# =====================================================================

print("\n" + "=" * 70)
print("                         LOGIN")
print("=" * 70)

entered_username = input("Username : ")
entered_password = input("Password : ")

# =====================================================================
# LOGIN VALIDATION
# =====================================================================

# -------------------------
# Comparison Operators
# -------------------------

username_matches = entered_username == registered_username
password_matches = entered_password == registered_password

# -------------------------
# Logical Operators
# -------------------------

credentials_valid = (
    username_matches
    and
    password_matches
)

account_accessible = (
    not
    account_blocked
)

authentication_successful = (
    credentials_valid
    and
    two_factor_enabled
)

login_requirements_met = (
    credentials_valid
    and
    account_accessible
    and
    two_factor_enabled
)

# =====================================================================
# LOGIN ANALYSIS REPORT
# =====================================================================

print("\n" + "=" * 70)
print("                 LOGIN ANALYSIS REPORT")
print("=" * 70)

print(f"""
Account Holder              : {full_name}

Phone Number                : {phone}

Email Address               : {email}

Username Matches            : {username_matches}

Password Matches            : {password_matches}

Credentials Valid           : {credentials_valid}

Two-Factor Authentication   : {two_factor_enabled}

Account Accessible          : {account_accessible}

Authentication Successful   : {authentication_successful}

Login Requirements Met      : {login_requirements_met}
""")

# =====================================================================
# APPLICATION SUMMARY
# =====================================================================

print("\n" + "=" * 70)
print("                 APPLICATION SUMMARY")
print("=" * 70)

print("""
This application demonstrated how logical operators work
behind the scenes in a simple login authentication system.

Logical operators allow multiple Boolean expressions to be
combined into a single result.

Operators Used

✓ and
Returns True only when all conditions are True.

✓ or
Returns True when at least one condition is True.

✓ not
Reverses the Boolean value.

Although this application evaluates login requirements,
it does not decide whether access should be granted or
denied. Making decisions requires conditional statements,
which will be introduced in the next module.
""")

# =====================================================================
# HOW THIS APPLICATION WORKS
# =====================================================================

print("\n" + "=" * 70)
print("              APPLICATION WORKFLOW")
print("=" * 70)

print("""
1. The user creates an account.

2. The system stores the account information.

3. The user attempts to log in.

4. The system compares the entered credentials
   with the registered credentials.

5. Logical operators combine multiple Boolean
   expressions into meaningful validation results.

6. The application displays the final analysis report.
""")

# =====================================================================
# REAL-WORLD APPLICATIONS
# =====================================================================

print("\n" + "=" * 70)
print("               REAL-WORLD APPLICATIONS")
print("=" * 70)

print("""
Logical operators are widely used in:

🔐 Login Authentication Systems

🏦 Online Banking Applications

🛒 E-Commerce Platforms

📱 Mobile Applications

🎓 Student Management Systems

🏥 Hospital Management Systems

☁️ Cloud Computing Platforms

🤖 Artificial Intelligence

🎮 Online Gaming Platforms

✈️ Airline Reservation Systems
""")

# =====================================================================
# INTERVIEW CORNER
# =====================================================================

print("\n" + "=" * 70)
print("                  INTERVIEW CORNER")
print("=" * 70)

print("""
1. What are logical operators?

Answer:
Logical operators combine or modify Boolean
expressions.

------------------------------------------------------------

2. Which logical operator returns True only
when every condition is True?

Answer:
and

------------------------------------------------------------

3. Which logical operator returns True when
at least one condition is True?

Answer:
or

------------------------------------------------------------

4. What does the 'not' operator do?

Answer:
It reverses a Boolean value.

------------------------------------------------------------

5. Which data type is returned by logical
operators?

Answer:
Boolean (True or False)
""")
