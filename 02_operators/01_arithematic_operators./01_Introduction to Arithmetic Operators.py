"""
============================================================
🐍 Python Fundamentals
Module 02 : Operators
File       : 01_arithmetic_operators.py

Topic:
Arithmetic Operators in Python

Description:
This lesson introduces Python's arithmetic operators through
well-structured explanations, practical examples, and
real-world applications.

Concepts Covered:
• Addition (+)
• Subtraction (-)
• Multiplication (*)
• Division (/)
• Floor Division (//)
• Modulus (%)
• Exponentiation (**)

Difficulty Level : Beginner
Prerequisites    : Variables, Data Types & User Input
Python Version   : 3.x

Author : Krishna Panchal
============================================================
"""

# ==========================================================
#                 ARITHMETIC OPERATORS
# ==========================================================

print("=" * 70)
print("              PYTHON ARITHMETIC OPERATORS")
print("=" * 70)

# ==========================================================
# Introduction
# ==========================================================

"""
Arithmetic operators are used to perform mathematical
calculations in Python.

These operators are among the most frequently used operators
because almost every Python application performs calculations
at some point.

Examples include:
• Shopping Bill Calculators
• Banking Systems
• Payroll Software
• Scientific Calculations
• Data Analytics
• Game Development
"""

# ==========================================================
# Learning Objectives
# ==========================================================

"""
After completing this lesson, you will be able to:

✓ Perform mathematical calculations in Python.
✓ Understand every arithmetic operator.
✓ Differentiate between division and floor division.
✓ Use modulus to find remainders.
✓ Calculate powers using exponentiation.
✓ Apply arithmetic operators in real-world programs.
"""

# ==========================================================
# Quick Facts
# ==========================================================

"""
✓ Python provides seven arithmetic operators.
✓ Arithmetic operators work with integers and floating-point numbers.
✓ Division (/) always returns a floating-point value.
✓ Floor Division (//) removes the decimal part.
✓ Modulus (%) returns the remainder after division.
✓ Exponentiation (**) calculates powers.
"""

# ==========================================================
# Arithmetic Operators Reference Table
# ==========================================================

print("\nARITHMETIC OPERATORS REFERENCE")
print("-" * 70)

print(f"{'Operator':<15}{'Name':<25}{'Example'}")
print("-" * 70)

print(f"{'+':<15}{'Addition':<25}15 + 5")
print(f"{'-':<15}{'Subtraction':<25}15 - 5")
print(f"{'*':<15}{'Multiplication':<25}15 * 5")
print(f"{'/':<15}{'Division':<25}15 / 5")
print(f"{'//':<15}{'Floor Division':<25}15 // 4")
print(f"{'%':<15}{'Modulus':<25}15 % 4")
print(f"{'**':<15}{'Exponentiation':<25}2 ** 5")

# ==========================================================
# Example 1 : Basic Arithmetic Operations
# ==========================================================

"""
Objective:
Understand how each arithmetic operator works.
"""

print("\n" + "=" * 70)
print("EXAMPLE 1 : BASIC ARITHMETIC OPERATIONS")
print("=" * 70)

first_number = 20
second_number = 6

print(f"\nFirst Number  : {first_number}")
print(f"Second Number : {second_number}")

print("\nResults")
print("-" * 70)

print(f"Addition (+)")
print(f"{first_number} + {second_number} = {first_number + second_number}")

print()

print(f"Subtraction (-)")
print(f"{first_number} - {second_number} = {first_number - second_number}")

print()

print(f"Multiplication (*)")
print(f"{first_number} × {second_number} = {first_number * second_number}")

print()

print(f"Division (/)")
print(f"{first_number} / {second_number} = {first_number / second_number}")

print()

print(f"Floor Division (//)")
print(f"{first_number} // {second_number} = {first_number // second_number}")

print()

print(f"Modulus (%)")
print(f"{first_number} % {second_number} = {first_number % second_number}")

print()

print(f"Exponentiation (**)")
print(f"{first_number} ** {second_number} = {first_number ** second_number}")

# ==========================================================
# Example 2 : Arithmetic Operations Using User Input
# ==========================================================

"""
Objective:
Perform arithmetic operations using values entered by the user.
"""

print("\n" + "=" * 70)
print("EXAMPLE 2 : USER INPUT")
print("=" * 70)

first_number = float(input("\nEnter the first number : "))
second_number = float(input("Enter the second number: "))

print("\nResults")
print("-" * 70)

print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")
print(f"{first_number} / {second_number} = {first_number / second_number}")
print(f"{first_number} // {second_number} = {first_number // second_number}")
print(f"{first_number} % {second_number} = {first_number % second_number}")
print(f"{first_number} ** {second_number} = {first_number ** second_number}")

print("\n" + "=" * 70)
print("End of Part 1")
print("=" * 70)

"""
Part 2 will cover:

• Division vs Floor Division
• Modulus Operator
• Exponentiation
• Operator Precedence
• Real-World Examples
"""

# ==========================================================
# Example 3 : Division vs Floor Division
# ==========================================================

"""
Objective:
Understand the difference between Division (/) and
Floor Division (//).
"""

print("\n" + "=" * 70)
print("EXAMPLE 3 : DIVISION VS FLOOR DIVISION")
print("=" * 70)

dividend = float(input("\nEnter the dividend : "))
divisor = float(input("Enter the divisor  : "))

print("\nResults")
print("-" * 70)

print(f"Division (/)")
print(f"{dividend} / {divisor} = {dividend / divisor}")

print()

print(f"Floor Division (//)")
print(f"{dividend} // {divisor} = {dividend // divisor}")

print()

print("Explanation")
print("-" * 70)
print("Division (/) returns the exact result including decimals.")
print("Floor Division (//) removes the decimal part and")
print("returns the greatest whole number less than or equal")
print("to the actual result.")

# ==========================================================
# Example 4 : Understanding the Modulus Operator
# ==========================================================

"""
Objective:
Learn how the modulus operator (%) returns the remainder
after division.
"""

print("\n" + "=" * 70)
print("EXAMPLE 4 : MODULUS OPERATOR")
print("=" * 70)

first_number = int(input("\nEnter the first number : "))
second_number = int(input("Enter the second number: "))

print("\nResult")
print("-" * 70)

print(f"{first_number} % {second_number} = {first_number % second_number}")

print("\nExplanation")
print("-" * 70)
print(f"When {first_number} is divided by {second_number},")
print(f"the remainder is {first_number % second_number}.")

# ==========================================================
# Example 5 : Exponentiation Operator
# ==========================================================

"""
Objective:
Learn how to calculate the power of a number using (**).
"""

print("\n" + "=" * 70)
print("EXAMPLE 5 : EXPONENTIATION")
print("=" * 70)

base = float(input("\nEnter the base     : "))
exponent = int(input("Enter the exponent: "))

print("\nResult")
print("-" * 70)

print(f"{base} ** {exponent} = {base ** exponent}")

print("\nExplanation")
print("-" * 70)
print(f"{base} raised to the power of {exponent}")
print(f"is equal to {base ** exponent}.")

# ==========================================================
# Example 6 : Operator Precedence
# ==========================================================

"""
Objective:
Understand how Python evaluates arithmetic expressions
using operator precedence (PEMDAS/BODMAS).
"""

print("\n" + "=" * 70)
print("EXAMPLE 6 : OPERATOR PRECEDENCE")
print("=" * 70)

result_1 = 10 + 5 * 2
result_2 = (10 + 5) * 2
result_3 = 100 / 5 + 4
result_4 = 100 / (5 + 5)
result_5 = 2 ** 3 * 4

print("\nExpression Results")
print("-" * 70)

print(f"10 + 5 * 2       = {result_1}")
print(f"(10 + 5) * 2     = {result_2}")
print(f"100 / 5 + 4      = {result_3}")
print(f"100 / (5 + 5)    = {result_4}")
print(f"2 ** 3 * 4       = {result_5}")

print("\nExplanation")
print("-" * 70)
print("Python follows the standard order of operations:")
print("1. Parentheses ()")
print("2. Exponentiation (**)")
print("3. Multiplication, Division, Floor Division, Modulus")
print("4. Addition and Subtraction")

print("\n" + "=" * 70)
print("End of Part 2")
print("=" * 70)

"""
Part 3 will cover:

• Area of Rectangle Calculator
• Area of Circle Calculator
• Average Marks Calculator
• Simple Interest Calculator
• Key Takeaways
• Practice Questions
• Did You Know?
"""

# ==========================================================
# Real-World Example 1 : Area of a Rectangle Calculator
# ==========================================================

"""
Objective:
Calculate the area and perimeter of a rectangle using
arithmetic operators.
"""

print("\n" + "=" * 70)
print("REAL-WORLD EXAMPLE 1 : AREA OF A RECTANGLE")
print("=" * 70)

length = float(input("\nEnter the length of the rectangle : "))
width = float(input("Enter the width of the rectangle  : "))

area = length * width
perimeter = 2 * (length + width)

print("\nResults")
print("-" * 70)
print(f"Area of Rectangle      = {area:.2f} square units")
print(f"Perimeter of Rectangle = {perimeter:.2f} units")

# ==========================================================
# Real-World Example 2 : Area of a Circle Calculator
# ==========================================================

"""
Objective:
Calculate the area and circumference of a circle.
"""

print("\n" + "=" * 70)
print("REAL-WORLD EXAMPLE 2 : AREA OF A CIRCLE")
print("=" * 70)

PI = 3.14159

radius = float(input("\nEnter the radius of the circle : "))

area = PI * radius ** 2
circumference = 2 * PI * radius

print("\nResults")
print("-" * 70)
print(f"Area of Circle          = {area:.2f} square units")
print(f"Circumference of Circle = {circumference:.2f} units")

# ==========================================================
# Real-World Example 3 : Average Marks Calculator
# ==========================================================

"""
Objective:
Calculate the average marks of five subjects.
"""

print("\n" + "=" * 70)
print("REAL-WORLD EXAMPLE 3 : AVERAGE MARKS CALCULATOR")
print("=" * 70)

mark1 = float(input("\nEnter marks for Subject 1 : "))
mark2 = float(input("Enter marks for Subject 2 : "))
mark3 = float(input("Enter marks for Subject 3 : "))
mark4 = float(input("Enter marks for Subject 4 : "))
mark5 = float(input("Enter marks for Subject 5 : "))

total_marks = mark1 + mark2 + mark3 + mark4 + mark5
average_marks = total_marks / 5

print("\nResults")
print("-" * 70)
print(f"Total Marks   = {total_marks:.2f}")
print(f"Average Marks = {average_marks:.2f}")

# ==========================================================
# Real-World Example 4 : Simple Interest Calculator
# ==========================================================

"""
Objective:
Calculate simple interest using the formula:

Simple Interest = (Principal × Rate × Time) / 100
"""

print("\n" + "=" * 70)
print("REAL-WORLD EXAMPLE 4 : SIMPLE INTEREST CALCULATOR")
print("=" * 70)

principal = float(input("\nEnter the principal amount : "))
rate = float(input("Enter the annual interest rate (%) : "))
time = float(input("Enter the time (in years) : "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("\nResults")
print("-" * 70)
print(f"Simple Interest = {simple_interest:.2f}")
print(f"Total Amount    = {total_amount:.2f}")

# ==========================================================
# Summary
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("""
✓ Addition (+) combines values.
✓ Subtraction (-) finds the difference.
✓ Multiplication (*) calculates repeated addition.
✓ Division (/) returns a floating-point result.
✓ Floor Division (//) returns the integer quotient.
✓ Modulus (%) returns the remainder.
✓ Exponentiation (**) raises a number to a power.
""")

# ==========================================================
# End of Part 3
# ==========================================================

print("=" * 70)
print("Congratulations! You have completed the lesson on")
print("Python Arithmetic Operators.")
print("=" * 70)
