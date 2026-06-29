"""
File: 15_dictionaries.py

Project: Contact Management System

Concepts Covered:
- Dictionaries
- Key-Value Pairs
- Adding Records
- Updating Records
- Deleting Records
- Searching Records
- Dictionary Methods
"""

contacts = {}

while True:

    print("\n" + "=" * 60)
    print("CONTACT MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Statistics")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    # Add Contact

    if choice == "1":

        name = input("Name: ").title()
        phone = input("Phone Number: ")

        contacts[name] = phone

        print("Contact Added Successfully.")

    # View Contacts

    elif choice == "2":

        if not contacts:
            print("No Contacts Available.")

        else:

            print("\nSaved Contacts")

            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    # Search Contact

    elif choice == "3":

        search_name = input(
            "Enter Name: "
        ).title()

        if search_name in contacts:

            print(
                f"{search_name} : "
                f"{contacts[search_name]}"
            )

        else:
            print("Contact Not Found.")

    # Update Contact

    elif choice == "4":

        update_name = input(
            "Enter Name to Update: "
        ).title()

        if update_name in contacts:

            new_phone = input(
                "Enter New Number: "
            )

            contacts[update_name] = new_phone

            print("Contact Updated.")

        else:
            print("Contact Not Found.")

    # Delete Contact

    elif choice == "5":

        delete_name = input(
            "Enter Name to Delete: "
        ).title()

        if delete_name in contacts:

            del contacts[delete_name]

            print("Contact Deleted.")

        else:
            print("Contact Not Found.")

    # Statistics

    elif choice == "6":

        print("\nStatistics")

        print(
            "Total Contacts:",
            len(contacts)
        )

        print(
            "All Contact Names:"
        )

        for name in contacts.keys():
            print(name)

    # Exit

    elif choice == "7":

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice.")

print("\nProgram Completed Successfully.")
