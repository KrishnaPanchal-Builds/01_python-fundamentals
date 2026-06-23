"""
Python Numbers and Math Operations Showcase
Author: Krishna Panchal

This program demonstrates arithmetic operations,
built-in mathematical functions, and the math module.
"""

import math

print("=" * 60)
print("PYTHON NUMBERS AND MATH SHOWCASE")
print("=" * 60)

num1 = 25
num2 = 7
negative_num = -42
decimal_num = 16.75

print("\nArithmetic Operations")
print("-" * 40)
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")

print("\nBuilt-in Functions")
print("-" * 40)
print("Absolute Value :", abs(negative_num))
print("Round Number   :", round(decimal_num))
print("Power Function :", pow(2, 10))
print("Maximum Value  :", max(10, 20, 30, 40))
print("Minimum Value  :", min(10, 20, 30, 40))
print("Divmod Result  :", divmod(25, 7))

print("\nMath Module Functions")
print("-" * 40)
print("Square Root    :", math.sqrt(144))
print("Ceiling Value  :", math.ceil(16.25))
print("Floor Value    :", math.floor(16.75))
print("Factorial      :", math.factorial(5))
print("GCD            :", math.gcd(36, 48))

print("\nMathematical Constants")
print("-" * 40)
print("Pi             :", math.pi)
print("Euler Number   :", math.e)

print("\nTrigonometric Functions")
print("-" * 40)
print("sin(90°)       :", round(math.sin(math.radians(90)), 2))
print("cos(0°)        :", round(math.cos(math.radians(0)), 2))
print("tan(45°)       :", round(math.tan(math.radians(45)), 2))

print("\nLogarithmic Functions")
print("-" * 40)
print("log10(1000)    :", math.log10(1000))
print("Natural Log(5) :", round(math.log(5), 4))

print("\nPractical Example")
print("-" * 40)

radius = 7
area = math.pi * radius ** 2

print(f"Circle Radius  : {radius}")
print(f"Circle Area    : {area:.2f}")

print("\n" + "=" * 60)
print("NUMBERS AND MATH OPERATIONS COMPLETED SUCCESSFULLY")
print("=" * 60)
