"""
File: 09_conditional_statements.py
Author : Krishna Panchal

Project: Smart Banking Eligibility Checker

Concepts Covered:
- if
- if-else
- if-elif-else
- nested if statements
- logical operators
- user input
- conditional decision making
"""

print("=" * 60)
print("SMART BANKING ELIGIBILITY CHECKER")
print("=" * 60)

name = input("Enter Customer Name: ").title()

print("\nAvailable Services")
print("1. Personal Loan")
print("2. Home Loan")
print("3. Car Loan")
print("4. Credit Card")

choice = int(input("\nSelect Service (1-4): "))

age = int(input("Enter Age: "))
monthly_income = float(input("Enter Monthly Income (₹): "))
credit_score = int(input("Enter Credit Score (300-900): "))

existing_loan = input("Any Existing Loan? (yes/no): ").lower()

print("\n" + "=" * 60)
print("APPLICATION RESULT")
print("=" * 60)

print(f"Customer Name : {name}")

# Age Validation

if age < 18:
    print("Application Rejected")
    print("Reason: Applicant must be at least 18 years old.")

else:

    # PERSONAL LOAN

    if choice == 1:

        if monthly_income >= 30000 and credit_score >= 700:

            if existing_loan == "no":
                print("Personal Loan Approved")
                print("Interest Rate : 9%")
                print("Risk Category : Low")

            else:
                print("Personal Loan Approved")
                print("Interest Rate : 11%")
                print("Risk Category : Medium")

        else:
            print("Personal Loan Rejected")

    # HOME LOAN

    elif choice == 2:

        if age >= 21 and monthly_income >= 50000:

            if credit_score >= 750:
                print("Home Loan Approved")
                print("Interest Rate : 8%")
                print("Risk Category : Low")

            elif credit_score >= 650:
                print("Manual Verification Required")
                print("Risk Category : Medium")

            else:
                print("Home Loan Rejected")
                print("Risk Category : High")

        else:
            print("Home Loan Rejected")

    # CAR LOAN

    elif choice == 3:

        if monthly_income >= 25000 and credit_score >= 650:
            print("Car Loan Approved")

            if credit_score >= 750:
                print("Interest Rate : 8.5%")
                print("Risk Category : Low")
            else:
                print("Interest Rate : 10.5%")
                print("Risk Category : Medium")

        else:
            print("Car Loan Rejected")

    # CREDIT CARD

    elif choice == 4:

        if credit_score >= 700:

            if monthly_income >= 20000:
                print("Credit Card Approved")
                print("Card Limit : ₹1,00,000")

            else:
                print("Credit Card Approved")
                print("Card Limit : ₹50,000")

        else:
            print("Credit Card Rejected")

    else:
        print("Invalid Service Selection")

print("\nThank you for using Smart Banking Eligibility Checker.")
