# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   AHilgendorf,8/21/2024, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
# Constants values do not change throughout the program

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show the latest student added.  
    3. Show all data.
    4. Save data to a file.
    5. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
course_name: str = ""  # Holds the name of a course entered by the user.
csv_data: str = ""  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to a file.
menu_choice: str = "" # Holds the choice made by the user
student_data: list = [] # List holding student first and last name and course
students: list = [] # Holds all students

# When the program starts, read the file data into a list of lists (table)
file_obj = open (FILE_NAME,'r')
for row in file_obj.readlines():
    student_data = row.strip().split(",")
    students.append(student_data)

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    # DONE The program takes the user's input for a student's first, last name, and course name.
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        csv_data = f"\n{student_first_name}, {student_last_name}, {course_name}"
        student_data = [student_first_name, student_last_name, course_name]
        students.append(student_data)
        continue

    # Show user's input
    # DONE The program displays the user's input for a student's first, last name, and course name.
    if menu_choice == "2":
        if csv_data == "":
            print("No student data has been entered.")
        else:
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

    # Present the current data
    elif menu_choice == "3":
        print("The current data is:")
        for student in students:
            student_first_name = student[0]
            student_last_name = student[1]
            course_name = student[2]
            print(f"{student_first_name}, {student_last_name}, {course_name}")
        continue

    # Save the data to a file
    # DONE The program saves the user's input for a student's first, last name, and course name to a CSV file.
    elif menu_choice == "4":
        file_obj = open(FILE_NAME, "w")
        for student in students:
            student_first_name = student[0]
            student_last_name = student[1]
            course_name = student[2]
            file_obj.write(f"\n{student_first_name}, {student_last_name}, {course_name}")
        file_obj.close()
        continue

    # Stop the loop
    elif menu_choice == "5":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, 4, or 5")

print("Program Ended")