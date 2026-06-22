"""
Python Type Casting Showcase
Author: Krishna Panchal

This program demonstrates explicit type conversion
between various Python data types.
"""

print("=" * 60)
print("PYTHON TYPE CASTING SHOWCASE")
print("=" * 60)

# String to Integer
age_str = "25"
age_int = int(age_str)

print("\nString to Integer")
print("-" * 30)
print(f"Original Value : {age_str}")
print(f"Original Type  : {type(age_str)}")
print(f"Converted Value: {age_int}")
print(f"Converted Type : {type(age_int)}")

# Integer to Float
marks = 95
marks_float = float(marks)

print("\nInteger to Float")
print("-" * 30)
print(f"Original Value : {marks}")
print(f"Original Type  : {type(marks)}")
print(f"Converted Value: {marks_float}")
print(f"Converted Type : {type(marks_float)}")

# Float to Integer
salary = 75899.75
salary_int = int(salary)

print("\nFloat to Integer")
print("-" * 30)
print(f"Original Value : {salary}")
print(f"Original Type  : {type(salary)}")
print(f"Converted Value: {salary_int}")
print(f"Converted Type : {type(salary_int)}")

# Number to String
experience = 5
experience_str = str(experience)

print("\nInteger to String")
print("-" * 30)
print(f"Original Value : {experience}")
print(f"Original Type  : {type(experience)}")
print(f"Converted Value: {experience_str}")
print(f"Converted Type : {type(experience_str)}")

# List to Tuple
skills_list = ["Python", "SQL", "Git", "Machine Learning"]
skills_tuple = tuple(skills_list)

print("\nList to Tuple")
print("-" * 30)
print(f"Original Value : {skills_list}")
print(f"Original Type  : {type(skills_list)}")
print(f"Converted Value: {skills_tuple}")
print(f"Converted Type : {type(skills_tuple)}")

# Tuple to List
roadmap_tuple = ("Python", "Data Science", "Machine Learning")
roadmap_list = list(roadmap_tuple)

print("\nTuple to List")
print("-" * 30)
print(f"Original Value : {roadmap_tuple}")
print(f"Original Type  : {type(roadmap_tuple)}")
print(f"Converted Value: {roadmap_list}")
print(f"Converted Type : {type(roadmap_list)}")

# List to Set
numbers = [1, 2, 3, 3, 4, 4, 5]
unique_numbers = set(numbers)

print("\nList to Set")
print("-" * 30)
print(f"Original Value : {numbers}")
print(f"Original Type  : {type(numbers)}")
print(f"Converted Value: {unique_numbers}")
print(f"Converted Type : {type(unique_numbers)}")

# Boolean Casting
print("\nBoolean Casting")
print("-" * 30)
print(f"bool(1)     -> {bool(1)}")
print(f"bool(0)     -> {bool(0)}")
print(f"bool('AI')  -> {bool('AI')}")
print(f"bool('')    -> {bool('')}")
print(f"bool([])    -> {bool([])}")
print(f"bool([1])   -> {bool([1])}")

print("\n" + "=" * 60)
print("TYPE CASTING COMPLETED SUCCESSFULLY")
print("=" * 60)
