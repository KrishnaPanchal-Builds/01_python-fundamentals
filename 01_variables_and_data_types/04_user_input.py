"""
Interactive Career Profile Generator
Author: Krishna Panchal

This program demonstrates user input,
type conversion, formatted output,
and basic calculations.
"""

print("=" * 60)
print("AI ENGINEER PROFILE GENERATOR")
print("=" * 60)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
career_goal = input("Enter your career goal: ")
years_of_learning = float(input("Years spent learning technology: "))

years_until_30 = 30 - age

print("\n" + "=" * 60)
print("PROFILE REPORT")
print("=" * 60)

print(f"Name                : {name}")
print(f"Age                 : {age}")
print(f"City                : {city}")
print(f"Career Goal         : {career_goal}")
print(f"Learning Experience : {years_of_learning} years")

print("\nCareer Insights")
print("-" * 60)

print(f"Years Remaining Until 30 : {years_until_30}")

if years_until_30 > 0:
    print("You still have significant time to build expertise.")
else:
    print("Focus on continuous growth and specialization.")

print("\nSummary")
print("-" * 60)

print(
    f"{name} from {city} is working towards becoming a "
    f"{career_goal} and has already invested "
    f"{years_of_learning} years into learning technology."
)

print("\nProgram Completed Successfully.")
