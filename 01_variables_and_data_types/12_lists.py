"""
File: 12_lists.py
Author : Krishna Panchal

Project: Student Record Manager

Concepts Covered:
- Lists
- List Methods
- Nested Lists
- Searching
- Updating
- Removing
- Looping Through Lists
"""

students = []

while True:

    print("\n" + "=" * 60)
    print("STUDENT RECORD MANAGER")
    print("=" * 60)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Statistics")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    # Add Student

    if choice == "1":

        name = input("Student Name: ").title()
        marks = float(input("Marks: "))

        students.append([name, marks])

        print("Student Added Successfully.")

    # View Students

    elif choice == "2":

        if not students:
            print("No Records Found.")

        else:

            print("\nStudent Records")

            for index, student in enumerate(students, start=1):
                print(
                    f"{index}. {student[0]} - {student[1]}"
                )

    # Search Student

    elif choice == "3":

        search_name = input(
            "Enter Student Name: "
        ).title()

        found = False

        for student in students:

            if student[0] == search_name:

                print(
                    f"Found: {student[0]} | Marks: {student[1]}"
                )

                found = True
                break

        if not found:
            print("Student Not Found.")

    # Update Student

    elif choice == "4":

        update_name = input(
            "Student Name to Update: "
        ).title()

        found = False

        for student in students:

            if student[0] == update_name:

                new_marks = float(
                    input("New Marks: ")
                )

                student[1] = new_marks

                print("Record Updated.")

                found = True
                break

        if not found:
            print("Student Not Found.")

    # Remove Student

    elif choice == "5":

        remove_name = input(
            "Student Name to Remove: "
        ).title()

        found = False

        for student in students:

            if student[0] == remove_name:

                students.remove(student)

                print("Student Removed.")

                found = True
                break

        if not found:
            print("Student Not Found.")

    # Statistics

    elif choice == "6":

        if not students:
            print("No Data Available.")

        else:

            marks_list = []

            for student in students:
                marks_list.append(student[1])

            print("\nStatistics")

            print("Total Students:", len(students))
            print("Highest Marks :", max(marks_list))
            print("Lowest Marks  :", min(marks_list))
            print(
                "Average Marks :",
                round(sum(marks_list) / len(marks_list), 2)
            )

    # Exit

    elif choice == "7":

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice.")
