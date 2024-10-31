# ------------------------------------------>
# Real Project: Student Database System
# ------------------------------------------>

# Build a simple student database where:
# Each student has a dictionary with details (name, age, course).
# Users can add, remove, or update students.
# Allow for nested information, such as courses completed and grades for each course.

# let's assume the student database info main structure here....
# ------------------------------------------
# Updated Project: Student Database System
# ------------------------------------------

# Importing necessary libraries
import json  # To save and load data as JSON for persistence

# Sample structure for student data
Student_info = {}

# Sample data structure
Student_info_structure = {
    "101": {
        "name": "John Doe",
        "age": 20,
        "courses": [
            {"course_name": "Math", "grade": "A", "completion_status": "Completed"},
            {"course_name": "Physics", "grade": "B+", "completion_status": "In Progress"}
        ]
    },
    "102": {
        "name": "Alice Smith",
        "age": 22,
        "courses": [
            {"course_name": "Chemistry", "grade": "A-", "completion_status": "Completed"},
            {"course_name": "Biology", "grade": "B", "completion_status": "In Progress"}
        ]
    }
}

# ------------------------------------------
# Helper Functions
# ------------------------------------------

def load_data():
    """Load the student data from a JSON file."""
    global Student_info
    try:
        with open("student_data.json", "r") as file:
            Student_info = json.load(file)
    except FileNotFoundError:
        Student_info = {}
        save_data()  # Create file if not found
    except json.JSONDecodeError:
        print("Error loading data. Starting with an empty database.")
        Student_info = {}

def save_data():
    """Save the student data to a JSON file."""
    with open("student_data.json", "w") as file:
        json.dump(Student_info, file)

# Load data at start
load_data()

# ------------------------------------------
# Main Functions
# ------------------------------------------

def print_choices():
    """Display menu options for the user."""
    print("\nMenu Options:")
    print("0: Display All Students")
    print("1: Add New Student")
    print("2: Remove Student")
    print("3: Update Student Information")
    print("4: Save and Exit")
    print("-----------------------------------")

def display_students():
    """Display all current students."""
    if not Student_info:
        print("Student database is empty!")
    else:
        for student_id, info in Student_info.items():
            print(f"ID: {student_id} - Name: {info['name']}, Age: {info['age']}")
            for course in info.get("courses", []):
                print(f"  Course: {course['course_name']}, Grade: {course['grade']}, Status: {course['completion_status']}")

def add_student():
    """Add a new student to the database."""
    student_id = input("Enter unique ID for the student: ").strip()
    if student_id in Student_info:
        print("This ID already exists. Try again with a unique ID.")
        return

    name = input("Enter student name: ").title()
    age = input("Enter student age: ").strip()
    age = int(age) if age.isdigit() else 0

    Student_info[student_id] = {
        "name": name,
        "age": age,
        "courses": []
    }
    add_courses(student_id)
    print(f"Student '{name}' added successfully!")

def add_courses(student_id):
    """Add courses for a specific student."""
    while True:
        course_name = input("Enter course name (or type 'done' to finish): ").title()
        if course_name.lower() == "done":
            break
        grade = input("Enter grade for course (e.g., A+, A, B): ").strip().upper()
        status = input("Enter completion status (Completed/In Progress): ").title()

        Student_info[student_id]["courses"].append({
            "course_name": course_name,
            "grade": grade if grade in {"A+", "A", "B", "C", "D"} else "N/A",
            "completion_status": status if status in {"Completed", "In Progress"} else "Unknown"
        })
        print(f"Course '{course_name}' added for student ID {student_id}.")

def remove_student():
    """Remove a student from the database."""
    student_id = input("Enter student ID to remove: ").strip()
    if student_id in Student_info:
        del Student_info[student_id]
        print(f"Student with ID {student_id} removed successfully.")
    else:
        print(f"No student found with ID {student_id}.")

def update_student():
    """Update student information."""
    student_id = input("Enter student ID to update: ").strip()
    if student_id not in Student_info:
        print(f"No student found with ID {student_id}.")
        return

    print("1: Update Name")
    print("2: Update Age")
    print("3: Update Courses")
    choice = input("Choose an option to update: ").strip()

    if choice == "1":
        new_name = input("Enter new name: ").title()
        Student_info[student_id]["name"] = new_name
        print("Name updated successfully.")
    elif choice == "2":
        new_age = input("Enter new age: ").strip()
        Student_info[student_id]["age"] = int(new_age) if new_age.isdigit() else Student_info[student_id]["age"]
        print("Age updated successfully.")
    elif choice == "3":
        update_courses(student_id)
    else:
        print("Invalid option. Returning to main menu.")

def update_courses(student_id):
    """Update a student's course information."""
    print("Courses:")
    for idx, course in enumerate(Student_info[student_id]["courses"], start=1):
        print(f"{idx}. {course['course_name']} - Grade: {course['grade']}, Status: {course['completion_status']}")
    
    try:
        course_idx = int(input("Enter course number to update: ")) - 1
        if 0 <= course_idx < len(Student_info[student_id]["courses"]):
            course = Student_info[student_id]["courses"][course_idx]
            course["course_name"] = input("Enter new course name: ").title() or course["course_name"]
            course["grade"] = input("Enter new grade: ").strip().upper() or course["grade"]
            course["completion_status"] = input("Enter new status (Completed/In Progress): ").title() or course["completion_status"]
            print("Course updated successfully.")
        else:
            print("Invalid course number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# ------------------------------------------
# Main Program Loop
# ------------------------------------------

def main():
    """Main function to run the student database system."""
    print("Welcome to the Student Database System!")
    while True:
        print_choices()
        choice = input("Select an option: ").strip()

        if choice == "0":
            display_students()
        elif choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            save_data()
            print("Data saved. Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
