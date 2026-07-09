# 🔀 Module 03 - Conditional Statements

> Python Fundamentals Repository

Conditional statements allow a program to make decisions based on specific conditions.

In real-world applications, programs rarely execute every line of code in a fixed sequence. Instead, they evaluate conditions and choose different paths based on user input, data, or system state.

Conditional statements form the foundation of decision-making in programming and are widely used in software development, web applications, mobile applications, artificial intelligence, automation, data analytics, and game development.

---

# 🎯 Learning Objectives

After completing this module, you will be able to:

- ✅ Understand decision-making in Python
- ✅ Use the `if` statement
- ✅ Use the `if-else` statement
- ✅ Use the `if-elif-else` statement
- ✅ Work with nested conditional statements
- ✅ Use the `match-case` statement
- ✅ Build real-world applications using conditional logic

---

# 📚 Topics Covered

| File | Topic |
|--------|--------|
| 01_if_statement.py | If Statement |
| 02_if_else_statement.py | If-Else Statement |
| 03_if_elif_else_statement.py | If-Elif-Else Statement |
| 04_nested_if.py | Nested If Statement |
| 05_match_case.py | Match-Case Statement |
| Mini_Project.py | Practical Application |

---

# 🤔 What is a Conditional Statement?

A conditional statement allows a program to execute specific blocks of code only when certain conditions are satisfied.

Think of conditional statements as decision-makers.

Example:

- If it is raining, carry an umbrella.
- If your score is above 90, assign Grade A.
- If your age is 18 or above, allow voting.

These decisions are made using conditional statements.

---

# 🔹 If Statement

The `if` statement executes a block of code only when the specified condition evaluates to `True`.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

# 🔹 If-Else Statement

The `if-else` statement allows a program to choose between two alternatives.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

---

# 🔹 If-Elif-Else Statement

Used when multiple conditions need to be checked.

### Syntax

```python
if condition:
    statement
elif condition:
    statement
else:
    statement
```

### Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

---

# 🔹 Nested If Statement

A nested if statement is an if statement placed inside another if statement.

### Example

```python
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
```

---

# 🔹 Match-Case Statement

Introduced in Python 3.10.

It provides a cleaner alternative to long if-elif-else chains.

### Example

```python
day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid Day")
```

---

# 🌍 Real-World Applications

Conditional statements are used in:

- 🔐 Login Authentication Systems
- 🏦 Banking Applications
- 🛒 E-Commerce Websites
- 🎓 Student Management Systems
- 🎮 Games
- 🚦 Traffic Control Systems
- 📱 Mobile Applications
- 🌐 Web Applications
- 🤖 Artificial Intelligence
- 📊 Data Analytics

---

# 💼 Practical Application

## Student Grade Analyzer

In this module, you will build a Student Grade Analyzer.

The application will:

- Accept student details
- Accept marks
- Calculate percentage
- Determine grade
- Display performance status
- Generate a professional report

This project demonstrates how conditional statements are used in real-world educational software.

---

# 🎓 Learning Outcomes

After completing this module, you will be able to:

- ✔️ Write decision-making programs
- ✔️ Build interactive applications
- ✔️ Validate user input
- ✔️ Analyze data using conditions
- ✔️ Create real-world projects using conditional logic

---

# 📌 Key Takeaways

- Conditional statements help programs make decisions.
- The `if` statement executes code when a condition is true.
- The `if-else` statement chooses between two paths.
- The `if-elif-else` statement handles multiple conditions.
- Nested if statements allow layered decision-making.
- Match-case provides a cleaner alternative for multiple choices.

---

<div align="center">

# 🎉 Module Complete!

You are now ready to build intelligent programs that can make decisions.

Happy Coding! 🐍🚀

</div>
