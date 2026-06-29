"""
File: 11_break_continue_pass.py

Project: Secure Login Simulator

Concepts Covered:
- break
- continue
- pass
- while loops
- input validation
- authentication logic
"""

print("=" * 60)
print("SECURE LOGIN SIMULATOR")
print("=" * 60)

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "python123"

attempts = 3

while attempts > 0:

    print(f"\nAttempts Remaining: {attempts}")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    # CONTINUE DEMO

    if username == "" or password == "":
        print("Username and Password cannot be empty.")
        continue

    # BREAK DEMO

    if (
        username == CORRECT_USERNAME
        and password == CORRECT_PASSWORD
    ):
        print("\nLogin Successful!")
        break

    else:
        attempts -= 1
        print("Invalid Credentials.")

else:
    print("\nAccount Temporarily Locked.")

print("\n" + "=" * 60)
print("BREAK DEMONSTRATION")
print("=" * 60)

for number in range(1, 21):

    if number == 13:
        print("Unlucky number encountered.")
        break

    print(number, end=" ")

print()

print("\n" + "=" * 60)
print("CONTINUE DEMONSTRATION")
print("=" * 60)

for number in range(1, 21):

    if number % 2 == 0:
        continue

    print(number, end=" ")

print()

print("\n" + "=" * 60)
print("PASS DEMONSTRATION")
print("=" * 60)

role = input("\nEnter role (admin/user/guest): ").lower()

if role == "admin":
    print("Full Access Granted")

elif role == "user":
    print("Limited Access Granted")

elif role == "guest":
    pass

else:
    print("Unknown Role")

print("\nProgram Completed Successfully.")
