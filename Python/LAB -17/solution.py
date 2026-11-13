

def display_menu():
    print("\n--- STUDENT RECORDS HANDLING ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Exit")

def main():
    students = {} 

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            roll_no = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            students[roll_no] = name
            print("Student added successfully!")

        elif choice == '2':
            if not students:
                print("No student records found.")
            else:
                print("\n--- Student Records ---")
                for roll, name in students.items():
                    print(f"Roll No: {roll} | Name: {name}")

        elif choice == '3':
            roll_no = input("Enter Roll Number to search: ")
            if roll_no in students:
                print(f"Student Found! Roll No: {roll_no} | Name: {students[roll_no]}")
            else:
                print("Student not found!")

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 4.")
