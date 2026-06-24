"""
File: 08_operators.py
Topic: Python Operators (Interactive Version)
"""

print("=" * 50)
print("PYTHON OPERATORS DEMONSTRATION")
print("=" * 50)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nARITHMETIC OPERATORS")
print("-" * 30)

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} // {num2} = {num1 // num2}")
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Division operations cannot be performed by zero.")

print(f"{num1} ** {num2} = {num1 ** num2}")

print("\nCOMPARISON OPERATORS")
print("-" * 30)

print(f"{num1} == {num2} : {num1 == num2}")
print(f"{num1} != {num2} : {num1 != num2}")
print(f"{num1} > {num2} : {num1 > num2}")
print(f"{num1} < {num2} : {num1 < num2}")
print(f"{num1} >= {num2} : {num1 >= num2}")
print(f"{num1} <= {num2} : {num1 <= num2}")

print("\nLOGICAL OPERATORS")
print("-" * 30)

age = int(input("Enter your age: "))
income = int(input("Enter your annual income: "))

eligible_for_loan = age >= 21 and income >= 50000

print("Loan Eligibility:", eligible_for_loan)

print("\nMEMBERSHIP OPERATORS")
print("-" * 30)

skills = ["Python", "SQL", "Pandas", "NumPy", "Machine Learning"]

user_skill = input("Enter a skill to search: ")

print(f"{user_skill} in skills: {user_skill in skills}")
print(f"{user_skill} not in skills: {user_skill not in skills}")

print("\nIDENTITY OPERATORS")
print("-" * 30)

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 == list3 :", list1 == list3)

print("\nBITWISE OPERATORS")
print("-" * 30)

a = int(input("Enter first integer for bitwise operations: "))
b = int(input("Enter second integer for bitwise operations: "))

print("AND :", a & b)
print("OR  :", a | b)
print("XOR :", a ^ b)
print("LEFT SHIFT :", a << 1)
print("RIGHT SHIFT:", a >> 1)

print("\nProgram Completed Successfully!")
