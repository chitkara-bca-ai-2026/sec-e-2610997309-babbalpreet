

import os

def display_menu():
    print("\n===============================")
    print(" STUDENT NOTES MANAGEMENT SYSTEM")
    print("===============================")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")
    print("===============================")

def write_notes():
    filename = "notes.txt"
    try:
        with open(filename, "w") as file:
            print("\nEnter your notes (type 'SAVE' on a new line when finished):")
            while True:
                line = input()
                if line == "SAVE":
                    break
                file.write(line + "\n")
        print("Notes successfully saved to 'notes.txt'.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def view_notes():
    filename = "notes.txt"
    if not os.path.exists(filename):
        print("\nError: No saved notes found. Please create notes first.")
        return

    try:
        print("\n--- Saved Student Notes ---")
        with open(filename, "r") as file:
            content = file.read()
            if content.strip() == "":
                print("(The notes file is empty.)")
            else:
                print(content)
        print("---------------------------")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            write_notes()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("\nExiting Student Notes Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 3.")