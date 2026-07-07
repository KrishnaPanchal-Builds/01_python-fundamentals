"""
===============================================================================
File    : 09_identity_and_membership.py
Project : Digital Library Membership & Identity Explorer
Author  : Krishna Panchal

Concepts Covered
----------------
✓ Lists
✓ Dictionaries
✓ Strings
✓ Membership Operators (in, not in)
✓ Identity Operators (is, is not)
===============================================================================
"""

print("=" * 80)
print("DIGITAL LIBRARY MEMBERSHIP & IDENTITY EXPLORER")
print("=" * 80)

# ------------------------------------------------------------------------------
# LIBRARY DATA
# ------------------------------------------------------------------------------

available_books = [
    "Python Basics",
    "Data Science Handbook",
    "Machine Learning 101",
    "AI for Beginners",
    "SQL Essentials",
    "Deep Learning Guide"
]

registered_members = [
    "Aarav",
    "Diya",
    "Krishna",
    "Riya",
    "Kabir"
]

premium_members = [
    "Krishna",
    "Riya"
]

# ------------------------------------------------------------------------------
# USER INPUT
# ------------------------------------------------------------------------------

member_name = input("\nEnter Your Name : ").title()

book_name = input("Enter Book Name : ").title()

# ------------------------------------------------------------------------------
# MEMBERSHIP OPERATORS
# ------------------------------------------------------------------------------

is_registered = member_name in registered_members

is_premium = member_name in premium_members

book_available = book_name in available_books

book_not_available = book_name not in available_books

# ------------------------------------------------------------------------------
# MEMBERSHIP REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("MEMBERSHIP REPORT")
print("=" * 80)

print(f"Registered Member      : {is_registered}")
print(f"Premium Member         : {is_premium}")
print(f"Book Available         : {book_available}")
print(f"Book Not Available     : {book_not_available}")

# ------------------------------------------------------------------------------
# IDENTITY OPERATORS
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("IDENTITY DEMONSTRATION")
print("=" * 80)

member_record = {
    "name": member_name,
    "membership": "Premium" if is_premium else "Regular"
}

same_reference = member_record

copied_record = member_record.copy()

print(f"member_record is same_reference : "
      f"{member_record is same_reference}")

print(f"member_record == copied_record  : "
      f"{member_record == copied_record}")

print(f"member_record is copied_record  : "
      f"{member_record is copied_record}")

print("\nMemory Addresses")

print(f"Original  : {id(member_record)}")
print(f"Reference : {id(same_reference)}")
print(f"Copy      : {id(copied_record)}")

# ------------------------------------------------------------------------------
# BORROWING ELIGIBILITY
# ------------------------------------------------------------------------------

can_borrow = is_registered and book_available

print("\n" + "=" * 80)
print("BORROWING STATUS")
print("=" * 80)

print(f"Can Borrow Book : {can_borrow}")

if can_borrow:
    print(f"{member_name} can borrow '{book_name}'.")
else:
    print(f"{member_name} cannot borrow '{book_name}'.")

print("=" * 80)
print("DIGITAL LIBRARY EXPLORER COMPLETED")
print("=" * 80)