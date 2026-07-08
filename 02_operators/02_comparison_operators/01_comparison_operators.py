"""
======================================================================
🐍 Python Fundamentals

Module 02 : Operators
File       : 01_comparison_operators.py

Topic:
Comparison Operators

Description:
This lesson demonstrates how comparison operators work in
Python through practical examples. Each comparison returns
either True or False.

Concepts Used:
• Equal To (==)
• Not Equal To (!=)
• Greater Than (>)
• Less Than (<)
• Greater Than or Equal To (>=)
• Less Than or Equal To (<=)

Difficulty Level : Beginner
Python Version   : 3.x

Author : Krishna Panchal
======================================================================
"""

# ====================================================================
#                    COMPARISON OPERATORS
# ====================================================================

print("=" * 70)
print("                 PYTHON COMPARISON OPERATORS")
print("=" * 70)

# ====================================================================
# Example 1 : Comparing Integer Values
# ====================================================================

print("\nEXAMPLE 1 : COMPARING INTEGER VALUES")
print("-" * 70)

first_number = 25
second_number = 15

print(f"\nFirst Number  : {first_number}")
print(f"Second Number : {second_number}")

print("\nComparison Results")
print("-" * 70)

print(f"{first_number} == {second_number} : {first_number == second_number}")
print(f"{first_number} != {second_number} : {first_number != second_number}")
print(f"{first_number} >  {second_number} : {first_number > second_number}")
print(f"{first_number} <  {second_number} : {first_number < second_number}")
print(f"{first_number} >= {second_number} : {first_number >= second_number}")
print(f"{first_number} <= {second_number} : {first_number <= second_number}")

# ====================================================================
# Example 2 : Comparing Floating-Point Numbers
# ====================================================================

print("\n" + "=" * 70)
print("EXAMPLE 2 : COMPARING FLOATING-POINT NUMBERS")
print("=" * 70)

price_1 = 499.99
price_2 = 799.99

print(f"\nProduct 1 Price : ₹{price_1}")
print(f"Product 2 Price : ₹{price_2}")

print("\nComparison Results")
print("-" * 70)

print(f"{price_1} == {price_2} : {price_1 == price_2}")
print(f"{price_1} != {price_2} : {price_1 != price_2}")
print(f"{price_1} >  {price_2} : {price_1 > price_2}")
print(f"{price_1} <  {price_2} : {price_1 < price_2}")
print(f"{price_1} >= {price_2} : {price_1 >= price_2}")
print(f"{price_1} <= {price_2} : {price_1 <= price_2}")

# ====================================================================
# Example 3 : Comparing User Input
# ====================================================================

print("\n" + "=" * 70)
print("EXAMPLE 3 : COMPARING USER INPUT")
print("=" * 70)

first_value = float(input("\nEnter the first number  : "))
second_value = float(input("Enter the second number : "))

print("\nComparison Results")
print("-" * 70)

print(f"{first_value} == {second_value} : {first_value == second_value}")
print(f"{first_value} != {second_value} : {first_value != second_value}")
print(f"{first_value} >  {second_value} : {first_value > second_value}")
print(f"{first_value} <  {second_value} : {first_value < second_value}")
print(f"{first_value} >= {second_value} : {first_value >= second_value}")
print(f"{first_value} <= {second_value} : {first_value <= second_value}")

print("\n" + "=" * 70)
print("End of Part 1")
print("=" * 70)

"""
Part 2 will cover:

• Comparing Variables
• Comparing Arithmetic Expressions
• Comparing Strings
• Real-World Comparison Examples
"""

# ====================================================================
# Example 4 : Comparing Variables
# ====================================================================

print("\n" + "=" * 70)
print("EXAMPLE 4 : COMPARING VARIABLES")
print("=" * 70)

employee_age = 28
minimum_age = 18

print(f"\nEmployee Age : {employee_age}")
print(f"Minimum Age  : {minimum_age}")

print("\nComparison Results")
print("-" * 70)

print(f"employee_age == minimum_age : {employee_age == minimum_age}")
print(f"employee_age != minimum_age : {employee_age != minimum_age}")
print(f"employee_age > minimum_age  : {employee_age > minimum_age}")
print(f"employee_age < minimum_age  : {employee_age < minimum_age}")
print(f"employee_age >= minimum_age : {employee_age >= minimum_age}")
print(f"employee_age <= minimum_age : {employee_age <= minimum_age}")

# ====================================================================
# Example 5 : Comparing Arithmetic Expressions
# ====================================================================

print("\n" + "=" * 70)
print("EXAMPLE 5 : COMPARING ARITHMETIC EXPRESSIONS")
print("=" * 70)

number_1 = 15
number_2 = 5
number_3 = 10

print(f"\nNumber 1 : {number_1}")
print(f"Number 2 : {number_2}")
print(f"Number 3 : {number_3}")

print("\nComparison Results")
print("-" * 70)

print(f"({number_1} + {number_2}) == {number_3 * 2} : {(number_1 + number_2) == (number_3 * 2)}")
print(f"({number_1} - {number_2}) > {number_3} : {(number_1 - number_2) > number_3}")
print(f"({number_1} * {number_2}) >= 75 : {(number_1 * number_2) >= 75}")
print(f"({number_1} / {number_2}) < 5 : {(number_1 / number_2) < 5}")
print(f"({number_1} % {number_2}) == 0 : {(number_1 % number_2) == 0}")

# ====================================================================
# Example 6 : Comparing Strings
# ====================================================================

print("\n" + "=" * 70)
print("EXAMPLE 6 : COMPARING STRINGS")
print("=" * 70)

city_1 = "Mumbai"
city_2 = "Delhi"
city_3 = "Mumbai"

print(f"\nCity 1 : {city_1}")
print(f"City 2 : {city_2}")
print(f"City 3 : {city_3}")

print("\nComparison Results")
print("-" * 70)

print(f'"{city_1}" == "{city_2}" : {city_1 == city_2}')
print(f'"{city_1}" == "{city_3}" : {city_1 == city_3}')
print(f'"{city_1}" != "{city_2}" : {city_1 != city_2}')
print(f'"{city_1}" > "{city_2}"  : {city_1 > city_2}')
print(f'"{city_1}" < "{city_2}"  : {city_1 < city_2}')
print(f'"{city_2}" >= "{city_3}" : {city_2 >= city_3}')

# ====================================================================
# Example 7 : Real-World Comparison Examples
# ====================================================================

print("\n" + "=" * 70)
print("EXAMPLE 7 : REAL-WORLD COMPARISONS")
print("=" * 70)

marks = 82
attendance = 91
minimum_marks = 40
minimum_attendance = 75

print(f"\nStudent Marks          : {marks}")
print(f"Student Attendance (%) : {attendance}")

print("\nComparison Results")
print("-" * 70)

print(f"Marks >= Minimum Marks           : {marks >= minimum_marks}")
print(f"Marks < Minimum Marks            : {marks < minimum_marks}")
print(f"Attendance >= Required Attendance: {attendance >= minimum_attendance}")
print(f"Attendance == 100                : {attendance == 100}")
print(f"Attendance != 100                : {attendance != 100}")

print("\n" + "=" * 70)
print("End of Part 2")
print("=" * 70)

"""
Part 3 will include:

• Summary
• Interview Corner
• Common Beginner Mistakes
• Practice Questions
• Mini Challenge
• End of Lesson
"""

# ====================================================================
# SUMMARY
# ====================================================================

print("\n" + "=" * 70)
print("                           SUMMARY")
print("=" * 70)

print("""
Congratulations!

You have successfully completed the lesson on
Python Comparison Operators.

Throughout this lesson, you learned how to compare
numbers, variables, strings and arithmetic expressions.

Every comparison operation in Python produces a
Boolean value:

✔ True
✔ False

These Boolean values form the foundation of
decision-making in Python programming.
""")

# ====================================================================
# INTERVIEW CORNER
# ====================================================================

print("\n" + "=" * 70)
print("                     INTERVIEW CORNER")
print("=" * 70)

print("""
1. What is the purpose of comparison operators?

   Answer:
   They compare two values or expressions and
   return either True or False.

--------------------------------------------------------------

2. Which comparison operator checks equality?

   Answer:
   ==

--------------------------------------------------------------

3. Which operator checks whether two values
   are not equal?

   Answer:
   !=

--------------------------------------------------------------

4. Which operators compare magnitude?

   >
   <
   >=
   <=

--------------------------------------------------------------

5. What is the return type of a comparison?

   Answer:
   Boolean (bool)
""")

# ====================================================================
# COMMON BEGINNER MISTAKES
# ====================================================================

print("\n" + "=" * 70)
print("                COMMON BEGINNER MISTAKES")
print("=" * 70)

print("""
❌ Using = instead of ==

   =
   Assignment Operator

   ==
   Comparison Operator

--------------------------------------------------------------

❌ Comparing strings without considering
   uppercase and lowercase letters.

Example:

"Python" == "python"

Result:
False

--------------------------------------------------------------

❌ Assuming comparison operators return numbers.

They actually return:

True
or
False

--------------------------------------------------------------

❌ Forgetting to convert user input into
numeric data types before comparison.
""")

# ====================================================================
# REAL-WORLD APPLICATIONS
# ====================================================================

print("\n" + "=" * 70)
print("                 REAL-WORLD APPLICATIONS")
print("=" * 70)

print("""
Comparison operators are used in:

• Login Systems
• Banking Applications
• Student Result Analysis
• Online Shopping Platforms
• Hospital Management Systems
• Payroll Software
• Inventory Management
• Data Validation
• Artificial Intelligence
• Machine Learning
• Game Development
""")

# ====================================================================
# PRACTICE QUESTIONS
# ====================================================================

print("\n" + "=" * 70)
print("                  PRACTICE QUESTIONS")
print("=" * 70)

print("""
1. Compare two numbers entered by the user.

2. Compare the prices of two products.

3. Compare the ages of two people.

4. Compare the marks of two students.

5. Compare two city names.

6. Compare two arithmetic expressions.

7. Compare two floating-point numbers.

8. Compare two employee salaries.

9. Compare the temperatures of two cities.

10. Compare the lengths of two rectangles.
""")

# ====================================================================
# MINI CHALLENGE
# ====================================================================

print("\n" + "=" * 70)
print("                    MINI CHALLENGE")
print("=" * 70)

print("""
Create your own comparison program that accepts
the following inputs:

• Name
• Age
• Marks
• Attendance

Display the results of comparisons such as:

Age >= 18

Marks >= 40

Attendance >= 75

Remember:

Do NOT use if, elif or else.

Simply display the Boolean results of
each comparison.
""")

# ====================================================================
# NEXT LESSON
# ====================================================================

print("\n" + "=" * 70)
print("                     WHAT'S NEXT?")
print("=" * 70)

print("""
Next Lesson:

Logical Operators

You will learn how to combine multiple
comparison results using:

• and
• or
• not

These operators allow you to evaluate
multiple conditions together and prepare
you for writing decision-making programs.
""")

# ====================================================================
# END OF LESSON
# ====================================================================

print("\n" + "=" * 70)
print("             LESSON COMPLETED SUCCESSFULLY!")
print("=" * 70)

print("""
Thank you for completing

⚖️ Python Comparison Operators

Keep Learning.
Keep Practicing.
Keep Building.

🐍 Python Fundamentals Repository

Author: Krishna Panchal

See you in the next lesson!
""")

print("=" * 70)
