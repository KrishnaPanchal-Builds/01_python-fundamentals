"""
======================================================================
🐍 Python Fundamentals Repository

Module 03 : Conditional Statements

Application : University Admission Eligibility System

Description:
This application evaluates a student's eligibility for
university admission based on academic qualifications,
entrance examination score, age, attendance, and category.

Concepts Covered:
• if
• if-else
• if-elif-else
• Nested if
• Logical Operators

Difficulty Level : Beginner
Python Version   : 3.x

Author : Krishna Panchal
======================================================================
"""

# =====================================================================
# UNIVERSITY ADMISSION ELIGIBILITY SYSTEM
# =====================================================================

print("=" * 70)
print("          UNIVERSITY ADMISSION ELIGIBILITY SYSTEM")
print("=" * 70)

print("""
Welcome!

This application evaluates a student's eligibility
for university admission.

The system analyzes:

• Personal Details
• Academic Qualifications
• Entrance Examination Score
• Attendance
• Scholarship Eligibility
• Admission Decision
""")

# =====================================================================
# APPLICANT DETAILS
# =====================================================================

print("\n" + "=" * 70)
print("                APPLICANT DETAILS")
print("=" * 70)

full_name = input("Full Name                 : ")
application_id = input("Application ID            : ")
age = int(input("Age                       : "))
category = input("Category (General/OBC/SC/ST): ")

# =====================================================================
# ACADEMIC DETAILS
# =====================================================================

print("\n" + "=" * 70)
print("                ACADEMIC DETAILS")
print("=" * 70)

class_10_percentage = float(input("Class 10 Percentage       : "))
class_12_percentage = float(input("Class 12 Percentage       : "))
entrance_exam_score = float(input("Entrance Exam Score (/100): "))
attendance = float(input("Attendance Percentage     : "))

# =====================================================================
# ELIGIBILITY ANALYSIS
# =====================================================================

admission_status = "Not Eligible"
scholarship_status = "Not Eligible"
hostel_status = "Not Eligible"
attendance_status = "Not Eligible"
admission_grade = "Not Assigned"

# ---------------------------------------------------------------------
# AGE ELIGIBILITY
# ---------------------------------------------------------------------

if age >= 17:

    # -----------------------------------------------------------------
    # ATTENDANCE ELIGIBILITY
    # -----------------------------------------------------------------

    if attendance >= 75:
        attendance_status = "Eligible"
    else:
        attendance_status = "Not Eligible"

    # -----------------------------------------------------------------
    # ADMISSION ELIGIBILITY
    # -----------------------------------------------------------------

    if (
        class_10_percentage >= 60 and
        class_12_percentage >= 60 and
        entrance_exam_score >= 70 and
        attendance >= 75
    ):
        admission_status = "Eligible"

    else:
        admission_status = "Not Eligible"

    # -----------------------------------------------------------------
    # ADMISSION GRADE
    # -----------------------------------------------------------------

    if entrance_exam_score >= 95:
        admission_grade = "Outstanding"

    elif entrance_exam_score >= 90:
        admission_grade = "Excellent"

    elif entrance_exam_score >= 80:
        admission_grade = "Very Good"

    elif entrance_exam_score >= 70:
        admission_grade = "Good"

    else:
        admission_grade = "Needs Improvement"

    # -----------------------------------------------------------------
    # SCHOLARSHIP ELIGIBILITY
    # -----------------------------------------------------------------

    if admission_status == "Eligible":

        if (
            class_10_percentage >= 90 and
            class_12_percentage >= 90 and
            entrance_exam_score >= 95
        ):
            scholarship_status = "100% Scholarship"

        elif (
            class_10_percentage >= 85 and
            class_12_percentage >= 85 and
            entrance_exam_score >= 90
        ):
            scholarship_status = "50% Scholarship"

        elif (
            class_10_percentage >= 80 and
            class_12_percentage >= 80 and
            entrance_exam_score >= 85
        ):
            scholarship_status = "25% Scholarship"

    # -----------------------------------------------------------------
    # HOSTEL ELIGIBILITY
    # -----------------------------------------------------------------

    if admission_status == "Eligible":
        hostel_status = "Eligible"

else:

    admission_status = "Not Eligible (Minimum age requirement not met)"

# =====================================================================
# ADMISSION REPORT
# =====================================================================

print("\n" + "=" * 70)
print("                 ADMISSION REPORT")
print("=" * 70)

print(f"""
Applicant Information

Full Name                 : {full_name}
Application ID            : {application_id}
Age                       : {age}
Category                  : {category}

----------------------------------------------------------------------

Academic Performance

Class 10 Percentage       : {class_10_percentage:.2f}%
Class 12 Percentage       : {class_12_percentage:.2f}%
Entrance Exam Score       : {entrance_exam_score:.2f}/100
Attendance                : {attendance:.2f}%

----------------------------------------------------------------------

Eligibility Status

Attendance Status         : {attendance_status}
Admission Status          : {admission_status}
Admission Grade           : {admission_grade}
Scholarship Status        : {scholarship_status}
Hostel Eligibility        : {hostel_status}

======================================================================
""")

# =====================================================================
# APPLICATION SUMMARY
# =====================================================================

print("=" * 70)
print("                APPLICATION SUMMARY")
print("=" * 70)

print("""
This application demonstrated how conditional
statements are used in real-world software.

Conditional Statements Used

✓ if
Used to evaluate individual conditions.

✓ if-else
Used when there are two possible outcomes.

✓ if-elif-else
Used to evaluate multiple conditions.

✓ Nested if
Used when a condition depends on another condition.

Logical Operators Used

✓ and
✓ or

These concepts form the foundation of
decision-making in Python applications.
""")

# =====================================================================
# REAL-WORLD APPLICATIONS
# =====================================================================

print("\n" + "=" * 70)
print("              REAL-WORLD APPLICATIONS")
print("=" * 70)

print("""
Conditional statements are widely used in:

🎓 University Admission Systems

🏦 Banking Applications

🛒 E-Commerce Platforms

🔐 Login Authentication Systems

🏥 Hospital Management Systems

✈️ Airline Reservation Systems

🚦 Traffic Management Systems

📱 Mobile Applications

🌐 Web Applications

🤖 Artificial Intelligence
""")

# =====================================================================
# INTERVIEW CORNER
# =====================================================================

print("\n" + "=" * 70)
print("                 INTERVIEW CORNER")
print("=" * 70)

print("""
1. What is a conditional statement?

Answer:
A conditional statement allows a program to make
decisions based on specified conditions.

--------------------------------------------------------------

2. Which conditional statements are available in Python?

Answer:
• if
• if-else
• if-elif-else
• Nested if
• match-case (Python 3.10+)

--------------------------------------------------------------

3. When should 'if-elif-else' be used?

Answer:
When multiple conditions need to be checked.

--------------------------------------------------------------

4. What is a nested if statement?

Answer:
A nested if statement is an if statement placed
inside another if statement.

--------------------------------------------------------------

5. Which operators are commonly used with
conditional statements?

Answer:
Comparison operators and logical operators.
""")

# =====================================================================
# PRACTICE CHALLENGE
# =====================================================================

print("\n" + "=" * 70)
print("               PRACTICE CHALLENGE")
print("=" * 70)

print("""
Build similar applications using conditional statements.

Ideas:

• ATM System

• Employee Promotion Checker

• Insurance Eligibility System

• Loan Approval System

• Movie Ticket Booking System

• Passport Eligibility System
""")

# =====================================================================
# APPLICATION COMPLETED
# =====================================================================

print("\n" + "=" * 70)
print("      APPLICATION COMPLETED SUCCESSFULLY!")
print("=" * 70)

print("""
Application

🎓 University Admission Eligibility System

Congratulations!

You have successfully learned how conditional
statements are used to build intelligent applications.

You can now make programs capable of evaluating
conditions and making decisions.

Keep Learning.
Keep Practicing.
Keep Building.

🐍 Python Fundamentals Repository

Author : Krishna Panchal
""")

print("=" * 70)
