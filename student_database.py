# ------------------------------------------>
# Real Project: Student Database System
# ------------------------------------------>

# Build a simple student database where:
# Each student has a dictionary with details (name, age, course).
# Users can add, remove, or update students.
# Allow for nested information, such as courses completed and grades for each course.

# let's assume the student database info main structure here....
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


# Greetings
print("\n|--------------------------------|")
print("   Welcome To Student Database")
print("|--------------------------------|\n")


# initially student database is empty
Student_info = {}


# function to prints the choices
def print_choices():
    print("Press 0 to 'See' the current students")
    print("Press 1 to 'Add' the new student")
    print("Press 2 to 'Remove' the new student")
    print("Press 3 to 'Update' the new student")
    print("-----------------------------------")


# function to see the current students
def see_current_student_info():
    print("\nHere you can see all the students info:")
    print("---------------------------------------")
    if Student_info == {}:
        print("Currently Student Database empty!\n")
    else:
        print(Student_info)


# function to add new student
def add_new_student():
    print("Adding New Student...")

    # inputting student unique ID with uniquness check
    while True:

        student_unique_id = input("Enter a unique ID for the student\n").strip()        # inputing student id
        if student_unique_id in Student_info:
            print("This ID already exists. Please enter a unique ID.")
        elif not student_unique_id.isdigit():
            print("ID should be numeric. Please try again.")
        else:
            break

    # Creating new entry in Student_info dictionary
    Student_info[student_unique_id] = {}                            # key as 'student id'

    # inputting student details
    student_name = input("Enter Student Name:\n").strip().title()   # Entering Student Name
    student_age = input("Enter Student Age:\n").strip()             # Entering Student Age

    # Adding details to dictionary with basic validation
    if student_name:
        Student_info[student_unique_id]["name"] = student_name      # student_name added to dict
    if student_age:
        Student_info[student_unique_id]["age"] = student_age        # student_age added to dict
    else:
        print("Invalid age entered!. Defaulting age to 0.")         
        Student_info[student_unique_id]["age"] = 0                  # age will set to zero (0)

    
    # Adding Courses
    Student_info[student_unique_id]["courses"] = []                 # setting an empty list for courses
    print("----------------------")
    print("   Entering Courses   ")
    print("----------------------")

    while True:
        # Collect course information in a dictionary
        course_info = {}
        course_info["course_name"] = input("Enter course name:\n").strip()                  # Entering new_course name

        # Input validation for grade
        grade = input("Enter grade for course (e.g., 'A+', 'A', 'B')\n").strip()            # Entering grade for course
        course_info["grade"] = grade if grade in {"A+", "A", "B", "C", "D", "E"} else "N/A"

        # Input validation for completion status
        completion_status = input("Enter completion status (e.g., 'Completed', 'In Progress):\n").strip().lower()   # Course CompletionStatus
        course_info["completion_status"] = completion_status if completion_status in {"completed", "in progress"} else "Unknown"

        # Add course info to student courses list
        Student_info[student_unique_id]["courses"].append(course_info)


        # Check if user wants to add another course
        new_course_adding_status = input("Do you want to add another course? (Y/N)\n").strip()
        if new_course_adding_status == 'n':  
            break
        elif new_course_adding_status != 'y':
            print("Invalid input! Continuing to the next entry...\n")

    print("  Student added successfully!")
    print("||-----------------------------||\n")


# function to remove current student
def remove_existed_student():
    if not Student_info:
        # if no student exist
        print("No 'Students' to Remove.\nThe Database is empty\n")
        
        # Offer to add a new student if the database is empty
        print("---------------------------------")
        add_student_check = input("Do you want to add student? (Y/N)\n").strip().lower()
        if add_student_check == 'y':
            add_new_student()
        elif add_student_check == 'n':
            print("Returning to main menu...\n")
        else:
            print("Invalide input! Please enter 'Y' or 'N'\n")
    else:
        # Taking input for ID with validation
        try:
            student_id = input("Enter Student_ID to remove:\n").strip()
            if student_id in Student_info:
                Student_info.pop(student_id)
                print(f"  Student with ID {student_id} removed successfully.\n")
                print("||-------------------------------------------------||")
            else:
                print(f"No student found with {student_id}. Please try again.\n")
        except ValueError as e:
            print(f"Invalid ID formate. Please enter a numeric ID.\nError Message : {e}")


# function to update the existed student info
def update_existed_student_info():
    if not Student_info:
        print("No 'Student' to Update. The Database is empty.")
        print("----------------------------------------------")
        add_student_check = input("Do you want to add a student? (Y/N)\n").strip().lower()

        if add_student_check == 'y':
            add_new_student()
            print("Returning to the main menu...")
            return

        else:
            print("Returning to the main menu...")
            return

    # Tak input for ID with validation
    student_id = input("Enter Student_ID to Update:\n").strip()

    if student_id not in Student_info:
        print(f"No student found with ID {student_id}! Please try again.\n")
        return
    
    # Displaying Update options
    print(f"\nWhat do you want to update in 'Student info' for ID {student_id}?")
    print("1. Student Name")
    print("2. Student Age")
    print("3. Courses")
    print("----------------------------")
    updation_choice = input("Choose an option (1/2/3): ").strip()

    if updation_choice == '1':
        # Update Name
        Student_info[student_id]["name"] = input(f"Enter a new name for ID {student_id}:\n")
        print(f"Name updated successfully for student {student_id}\n")
        print("---------------------------------------------------")

    elif updation_choice == '2':
        # Update Age
        try:
            new_age = int(input(f"Enter a new age for ID {student_id}:\n"))
            Student_info[student_id]["age"] = new_age
            print(f"Age updated successfully for student {student_id}\n")
            print("-------------------------------------------------")

        except ValueError:
            print("Invalid age formate! Please enter a numeric value.\n")
        
    elif updation_choice == '3':
        # Update Courses
        if not Student_info[student_id]["courses"]:
            print("No courses available to update for this student!\n")
            return

        # List all courses with index
        print("\nAvailable Courses:")
        for idx, course in enumerate(Student_info[student_id]["courses"], start = 1):
            print(f"{idx}. {course["course_name"]} - Grade: {course["grade"]}, Status: {course["completion_status"]}")

        
        # Choose specific course to update
        try:
            course_index = int(input("\nEnter the course number you want to update:\n")) - 1
            if course_index < 0 or course_index >= len(Student_info[student_id]["courses"]):
                print("Invalid course number. Please try again.\n")
                return

            # update course details
            course = Student_info[student_id]["courses"][course_index]
            print(f"\nUpdating course '{course["course_name"]}'")
            print("1. Update Course Name")
            print("2. Update Grade")
            print("3. Update Completion Status\n")

            course_update_choice = input("Choose an option (1/2/3): ").strip()

            if course_update_choice == '1':
                course["course_name"] = input("Enter new course name:\n")
            elif course_update_choice == '2':
                course["grade"] = input("Enter new grade (e.g., A+, B):\n")
            elif course_update_choice == '3':
                course["completion_status"] = input("Enter new completion status:\n")
            else:
                print("Invalid choice! Returning to main menu.\n")

            print(f"Course '{course["course_name"]}' updated successfully.\n")
            print("-----------------------------------------------------")

        except ValueError:
            print("Invalid input! Please enter a numeric value.\n")
    else:
        print("Invalide choice! Returning to main menu.\n")

            
    print(f"Student info for ID {student_id} updated successfully\n")
    print("||---------------------------------------------------||")

    continue_updation = input("\nDo you want to do more updation? (Y/N)").strip().lower()
    if continue_updation == 'n':
        print("Returning to main menu...\n")
        return
    elif continue_updation == 'y':
        update_existed_student_info()
    else:
        print("Invalide input! Please try again.\n")


# function to control the process (Continue/Exit)
def continue_process():
    """Ask the user if they want to continue or exit the process
    
    Returns:
        bool: True if the user wanto to continue, False if they want  to exit.
    """
    while True:
        print("----------------------------")
        user_input = input("Do you continue/Exit? (Y/N):\n").strip().lower()

        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print("Invalid input. Please Enter 'y' for Yes or 'n' for No.\n")

# printing choices through calling print_choices function
print_choices()

# Run until user want to exit using while loop
while True:

    user_choice = int(input())

    if user_choice == 0:
        see_current_student_info()

    elif user_choice == 1:
        add_new_student()

    elif user_choice == 2:
        remove_existed_student()
    
    elif user_choice == 3:
        update_existed_student_info()
    
    else:
        print("invalid choice! Please Try Again...\n")

    if not continue_process():
        print("Exiting Process...\n")
        break

    # Adding new line for clarity
    print()
    # if user want to continue, printing choices again
    print_choices()