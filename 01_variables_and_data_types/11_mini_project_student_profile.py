"""
===============================================================================
File    : 11_mini_project_student_profile.py
Project : AI Academy Student Management System

Part 1 : Student Registration & Profile Creation

Concepts Covered
----------------
✓ Variables
✓ Data Types
✓ Type Casting
✓ User Input
✓ String Operations
✓ Numbers
✓ Boolean Values
✓ Identity & Membership
===============================================================================
"""

print("=" * 80)
print("AI ACADEMY STUDENT MANAGEMENT SYSTEM")
print("=" * 80)

# ------------------------------------------------------------------------------
# ACADEMY INFORMATION
# ------------------------------------------------------------------------------

ACADEMY_NAME = "OpenAI AI Academy"
ACADEMY_CODE = "OAA2026"
PASS_PERCENTAGE = 40
SCHOLARSHIP_PERCENTAGE = 90

print(f"Academy Name : {ACADEMY_NAME}")
print(f"Academy Code : {ACADEMY_CODE}")

print("\n" + "=" * 80)

# ------------------------------------------------------------------------------
# STUDENT REGISTRATION
# ------------------------------------------------------------------------------

student_name = input("Student Name        : ").title()
roll_number = input("Roll Number         : ").upper()
age = int(input("Age                 : "))
gender = input("Gender              : ").title()

email = input("Email               : ").lower()

phone = input("Phone Number        : ")

course = input(
    "Course (AI/ML/Data/Web): "
).title()

city = input("City                : ").title()

# ------------------------------------------------------------------------------
# SKILLS
# ------------------------------------------------------------------------------

print("\nEnter your skills separated by commas.")
print("Example: Python, SQL, Git")

skills = [
    skill.strip().lower()
    for skill in input("Skills : ").split(",")
]

# ------------------------------------------------------------------------------
# PROFILE CREATION
# ------------------------------------------------------------------------------

student_profile = {
    "Name": student_name,
    "Roll Number": roll_number,
    "Age": age,
    "Gender": gender,
    "Email": email,
    "Phone": phone,
    "Course": course,
    "City": city
}

student_reference = student_profile

print("\n")
print("=" * 80)
print("PROFILE CREATED")
print("=" * 80)

for key, value in student_profile.items():
    print(f"{key:<15}: {value}")

# ------------------------------------------------------------------------------
# PROFILE VALIDATION
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("PROFILE VALIDATION")
print("=" * 80)

email_valid = "@" in email

phone_valid = len(phone) == 10

python_skill = "python" in skills

sql_skill = "sql" in skills

git_skill = "git" in skills

print(f"Email Valid           : {email_valid}")
print(f"Phone Valid           : {phone_valid}")
print(f"Knows Python          : {python_skill}")
print(f"Knows SQL             : {sql_skill}")
print(f"Knows Git             : {git_skill}")

# ------------------------------------------------------------------------------
# IDENTITY DEMONSTRATION
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("PROFILE IDENTITY")
print("=" * 80)

print("student_profile is student_reference")
print(student_profile is student_reference)

student_copy = student_profile.copy()

print("student_profile == student_copy")
print(student_profile == student_copy)

print("student_profile is student_copy")
print(student_profile is student_copy)

print("\nMemory Addresses")

print(f"Original : {id(student_profile)}")
print(f"Reference: {id(student_reference)}")
print(f"Copy     : {id(student_copy)}")

# ------------------------------------------------------------------------------
# STUDENT STATUS
# ------------------------------------------------------------------------------

registered = True

print("\n" + "=" * 80)
print("REGISTRATION STATUS")
print("=" * 80)

print(f"Registered : {registered}")

print("\nPart 1 Completed Successfully.")

# ==============================================================================
# PART 2 : ACADEMIC PERFORMANCE MANAGEMENT
# ==============================================================================

print("\n" + "=" * 80)
print("ACADEMIC PERFORMANCE MANAGEMENT")
print("=" * 80)

# ------------------------------------------------------------------------------
# SUBJECT MARKS
# ------------------------------------------------------------------------------

subjects = [
    "Python",
    "SQL",
    "Statistics",
    "Machine Learning",
    "Communication Skills"
]

marks = {}

print("\nEnter marks out of 100")

for subject in subjects:

    while True:

        score = float(input(f"{subject:<25}: "))

        if 0 <= score <= 100:
            marks[subject] = score
            break

        print("Marks should be between 0 and 100.")

# ------------------------------------------------------------------------------
# ATTENDANCE
# ------------------------------------------------------------------------------

attendance = float(
    input("\nAttendance Percentage : ")
)

# ------------------------------------------------------------------------------
# ACADEMIC CALCULATIONS
# ------------------------------------------------------------------------------

total_marks = sum(marks.values())

maximum_marks = len(subjects) * 100

percentage = total_marks / maximum_marks * 100

highest_mark = max(marks.values())

lowest_mark = min(marks.values())

average_mark = total_marks / len(subjects)

passed_all_subjects = all(mark >= PASS_PERCENTAGE for mark in marks.values())

distinction = percentage >= 75

# ------------------------------------------------------------------------------
# GRADE CALCULATION
# ------------------------------------------------------------------------------

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= PASS_PERCENTAGE:
    grade = "D"
else:
    grade = "F"

# ------------------------------------------------------------------------------
# ATTENDANCE STATUS
# ------------------------------------------------------------------------------

attendance_good = attendance >= 75

attendance_excellent = attendance >= 90

# ------------------------------------------------------------------------------
# SUBJECT ANALYSIS
# ------------------------------------------------------------------------------

best_subject = max(marks, key=marks.get)

weakest_subject = min(marks, key=marks.get)

# ------------------------------------------------------------------------------
# PERFORMANCE CATEGORY
# ------------------------------------------------------------------------------

if percentage >= 90 and attendance_excellent:
    performance = "Outstanding"

elif percentage >= 80:
    performance = "Excellent"

elif percentage >= 70:
    performance = "Very Good"

elif percentage >= 60:
    performance = "Good"

elif percentage >= PASS_PERCENTAGE:
    performance = "Average"

else:
    performance = "Needs Improvement"

# ------------------------------------------------------------------------------
# ACADEMIC REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("ACADEMIC REPORT")
print("=" * 80)

for subject, score in marks.items():
    print(f"{subject:<25}: {score:>6.2f}")

print("-" * 80)

print(f"Total Marks              : {total_marks:.2f}/{maximum_marks}")
print(f"Percentage               : {percentage:.2f}%")
print(f"Average Marks            : {average_mark:.2f}")
print(f"Highest Mark             : {highest_mark:.2f}")
print(f"Lowest Mark              : {lowest_mark:.2f}")

print("-" * 80)

print(f"Best Subject             : {best_subject}")
print(f"Weakest Subject          : {weakest_subject}")

print("-" * 80)

print(f"Passed All Subjects      : {passed_all_subjects}")
print(f"Attendance               : {attendance:.2f}%")
print(f"Attendance Good          : {attendance_good}")
print(f"Attendance Excellent     : {attendance_excellent}")

print("-" * 80)

print(f"Grade                    : {grade}")
print(f"Performance              : {performance}")

# ------------------------------------------------------------------------------
# ACADEMIC SCORE
# ------------------------------------------------------------------------------

academic_score = sum([
    passed_all_subjects,
    attendance_good,
    attendance_excellent,
    distinction,
    percentage >= 80,
    percentage >= 90
])

print("\n" + "=" * 80)
print("ACADEMIC SCORECARD")
print("=" * 80)

print(f"Academic Score : {academic_score}/6")

if academic_score == 6:
    academic_status = "TOP PERFORMER"
elif academic_score >= 4:
    academic_status = "HIGH ACHIEVER"
elif academic_score >= 2:
    academic_status = "GOOD STANDING"
else:
    academic_status = "ACADEMIC SUPPORT REQUIRED"

print(f"Academic Status : {academic_status}")

print("\nPart 2 Completed Successfully.")

# ==============================================================================
# PART 3 : CAREER READINESS & SCHOLARSHIP EVALUATION
# ==============================================================================

print("\n" + "=" * 80)
print("CAREER READINESS & SCHOLARSHIP EVALUATION")
print("=" * 80)

# ------------------------------------------------------------------------------
# CERTIFICATIONS
# ------------------------------------------------------------------------------

certifications = int(
    input("\nNumber of Certifications : ")
)

projects_completed = int(
    input("Projects Completed        : ")
)

coding_hours = int(
    input("Coding Hours Per Week     : ")
)

github_profile = (
    input("GitHub Profile Available? (yes/no): ")
    .strip()
    .lower() == "yes"
)

linkedin_profile = (
    input("LinkedIn Profile Available? (yes/no): ")
    .strip()
    .lower() == "yes"
)

hackathon_participation = (
    input("Participated in Hackathons? (yes/no): ")
    .strip()
    .lower() == "yes"
)

# ------------------------------------------------------------------------------
# SKILL ANALYSIS
# ------------------------------------------------------------------------------

required_skills = {
    "python",
    "sql",
    "git",
    "communication"
}

student_skills = set(skills)

matched_skills = required_skills.intersection(student_skills)

missing_skills = required_skills.difference(student_skills)

skill_score = len(matched_skills)

# ------------------------------------------------------------------------------
# ELIGIBILITY CHECKS
# ------------------------------------------------------------------------------

scholarship_eligible = all([
    percentage >= SCHOLARSHIP_PERCENTAGE,
    attendance >= 90,
    passed_all_subjects
])

internship_eligible = all([
    percentage >= 75,
    github_profile,
    projects_completed >= 2,
    "python" in student_skills
])

placement_ready = all([
    percentage >= 70,
    github_profile,
    linkedin_profile,
    projects_completed >= 3,
    certifications >= 2,
    coding_hours >= 10
])

ai_specialization_ready = all([
    "python" in student_skills,
    "sql" in student_skills,
    projects_completed >= 3,
    percentage >= 80
])

# ------------------------------------------------------------------------------
# CAREER READINESS SCORE
# ------------------------------------------------------------------------------

career_score = sum([
    scholarship_eligible,
    internship_eligible,
    placement_ready,
    ai_specialization_ready,
    github_profile,
    linkedin_profile,
    hackathon_participation,
    certifications >= 2,
    projects_completed >= 3,
    coding_hours >= 10
])

# ------------------------------------------------------------------------------
# REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("CAREER ASSESSMENT REPORT")
print("=" * 80)

print(f"Matched Skills           : {sorted(matched_skills)}")
print(f"Missing Skills           : {sorted(missing_skills)}")

print("-" * 80)

print(f"Scholarship Eligible     : {scholarship_eligible}")
print(f"Internship Eligible      : {internship_eligible}")
print(f"Placement Ready          : {placement_ready}")
print(f"AI Specialization Ready  : {ai_specialization_ready}")

print("-" * 80)

print(f"Skill Score              : {skill_score}/{len(required_skills)}")
print(f"Career Score             : {career_score}/10")

if career_score >= 9:
    career_status = "EXCELLENT"
elif career_score >= 7:
    career_status = "VERY GOOD"
elif career_score >= 5:
    career_status = "GOOD"
else:
    career_status = "NEEDS IMPROVEMENT"

print(f"Career Status            : {career_status}")

# ------------------------------------------------------------------------------
# RECOMMENDATIONS
# ------------------------------------------------------------------------------

recommendations = []

if "python" not in student_skills:
    recommendations.append("Learn Python thoroughly.")

if "sql" not in student_skills:
    recommendations.append("Develop SQL skills.")

if "git" not in student_skills:
    recommendations.append("Learn Git and GitHub.")

if projects_completed < 3:
    recommendations.append("Build more practical projects.")

if certifications < 2:
    recommendations.append("Earn industry-recognized certifications.")

if coding_hours < 10:
    recommendations.append("Increase weekly coding practice.")

if not github_profile:
    recommendations.append("Create and maintain a GitHub portfolio.")

if not linkedin_profile:
    recommendations.append("Build a professional LinkedIn profile.")

print("\n" + "=" * 80)
print("PERSONALIZED RECOMMENDATIONS")
print("=" * 80)

if recommendations:
    for index, recommendation in enumerate(recommendations, start=1):
        print(f"{index}. {recommendation}")
else:
    print("Excellent! You have a strong career profile.")

print("\nPart 3 Completed Successfully.")

# ==============================================================================
# PART 4 : EXECUTIVE STUDENT DASHBOARD & FINAL REPORT
# ==============================================================================

print("\n" + "=" * 80)
print("AI ACADEMY EXECUTIVE STUDENT DASHBOARD")
print("=" * 80)

# ------------------------------------------------------------------------------
# OVERALL SCORE
# ------------------------------------------------------------------------------

overall_score = academic_score + career_score

maximum_score = 16

overall_percentage = (overall_score / maximum_score) * 100

# ------------------------------------------------------------------------------
# STUDENT CLASSIFICATION
# ------------------------------------------------------------------------------

if overall_percentage >= 90:
    student_classification = "Elite AI Scholar"

elif overall_percentage >= 80:
    student_classification = "Advanced AI Learner"

elif overall_percentage >= 70:
    student_classification = "Career Ready Student"

elif overall_percentage >= 60:
    student_classification = "Developing Professional"

else:
    student_classification = "Foundation Level Student"

# ------------------------------------------------------------------------------
# CERTIFICATE ELIGIBILITY
# ------------------------------------------------------------------------------

certificate_eligible = all([
    passed_all_subjects,
    attendance_good
])

gold_certificate = all([
    overall_percentage >= 90,
    scholarship_eligible
])

# ------------------------------------------------------------------------------
# PLACEMENT RECOMMENDATION
# ------------------------------------------------------------------------------

placement_recommendation = any([
    placement_ready,
    internship_eligible
])

# ------------------------------------------------------------------------------
# AI CAREER PATH
# ------------------------------------------------------------------------------

if percentage >= 90 and "python" in student_skills:
    career_path = "AI Engineer"

elif percentage >= 80 and "sql" in student_skills:
    career_path = "Data Scientist"

elif percentage >= 75:
    career_path = "Data Analyst"

else:
    career_path = "Software Developer"

# ------------------------------------------------------------------------------
# FINAL REPORT CARD
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("FINAL STUDENT REPORT CARD")
print("=" * 80)

print(f"Academy                 : {ACADEMY_NAME}")
print(f"Student                 : {student_name}")
print(f"Roll Number             : {roll_number}")
print(f"Course                  : {course}")
print(f"City                    : {city}")

print("-" * 80)

print(f"Percentage              : {percentage:.2f}%")
print(f"Grade                   : {grade}")
print(f"Attendance              : {attendance:.2f}%")

print("-" * 80)

print(f"Academic Score          : {academic_score}/6")
print(f"Career Score            : {career_score}/10")
print(f"Overall Score           : {overall_score}/{maximum_score}")
print(f"Overall Percentage      : {overall_percentage:.2f}%")

print("-" * 80)

print(f"Student Category        : {student_classification}")
print(f"Recommended Career      : {career_path}")

print("-" * 80)

print(f"Certificate Eligible    : {certificate_eligible}")
print(f"Gold Certificate        : {gold_certificate}")
print(f"Placement Recommended   : {placement_recommendation}")

print("=" * 80)

# ------------------------------------------------------------------------------
# ACHIEVEMENTS
# ------------------------------------------------------------------------------

print("ACHIEVEMENTS")
print("-" * 80)

if scholarship_eligible:
    print("🏆 Scholarship Eligible")

if internship_eligible:
    print("💼 Internship Ready")

if placement_ready:
    print("🚀 Placement Ready")

if ai_specialization_ready:
    print("🤖 AI Specialization Ready")

if attendance_excellent:
    print("🎯 Excellent Attendance")

if distinction:
    print("🎓 Academic Distinction")

print("=" * 80)

# ------------------------------------------------------------------------------
# FINAL LEARNING ROADMAP
# ------------------------------------------------------------------------------

print("NEXT LEARNING ROADMAP")
print("-" * 80)

roadmap = [
    "Master Python Fundamentals",
    "Practice Data Structures",
    "Learn Object-Oriented Programming",
    "Study NumPy and Pandas",
    "Master SQL",
    "Learn Data Visualization",
    "Study Machine Learning",
    "Build End-to-End AI Projects",
    "Contribute to GitHub",
    "Prepare for Technical Interviews"
]

for step, item in enumerate(roadmap, start=1):
    print(f"{step}. {item}")

print("=" * 80)

# ------------------------------------------------------------------------------
# FINAL MESSAGE
# ------------------------------------------------------------------------------

if overall_percentage >= 90:
    message = "Outstanding! You are on an excellent path toward an AI career."
elif overall_percentage >= 75:
    message = "Very good progress. Continue building projects and strengthening your portfolio."
elif overall_percentage >= 60:
    message = "Good foundation. Focus on improving practical skills and consistency."
else:
    message = "Keep practicing regularly. Every project you complete builds your confidence and skills."

print("FINAL MESSAGE")
print("-" * 80)
print(message)

print("\n" + "=" * 80)
print("AI ACADEMY STUDENT MANAGEMENT SYSTEM COMPLETED SUCCESSFULLY")
print("=" * 80)
