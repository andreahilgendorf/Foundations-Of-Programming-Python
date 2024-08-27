# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Who, When, What)
#   ahilgendorf,8/14/2024,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """ 
---- Course Registration Program ----
    Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
---------------------------------
"""

FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file_obj = None
menu_choice: str = ""

# Present and Process the data
# Present the menu of choices

while menu_choice != "4":
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    # TODO The program takes the user's input for a student's first, last name, and course name.
    if menu_choice == "1":
       student_first_name = input("Enter the student's first name: ")
       student_last_name = input("Enter the student's last name: ")
       course_name = input("Please enter the name of the course: ")

    # Present the current data
    # TODO The program displays the user's input for a student's first, last name, and course name.
    elif menu_choice == "2":
        csv_data += f"{student_first_name},{student_last_name},{course_name}\n"
        print("The current data is: \n" + csv_data)

    # Save the data to a file
        # The program saves the user's input for a student's first, last name, and course name to a coma-separated
        # string file. (check this in a simple text editor like notepad.)
    elif menu_choice == "3":
        file_obj = open("Enrollments.csv", 'w')
        file_obj.write(csv_data)
        print("You have registered " + student_first_name + " " + student_last_name + " for " + course_name)
        file_obj.close()

# Stop the loop
print("Program Ended")

# TODO The program allows users to enter multiple registrations (first name, last name, course name).
# TODO The program runs correctly in both PyCharm and from the console or terminal.