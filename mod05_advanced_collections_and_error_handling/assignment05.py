# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   AHilgendorf,8/28/2024,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list[dict[str]] = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        # Transform the data from the file
        student_data = row.strip().split(',')
        student_data = [student_data[0], student_data[1], student_data[2].strip()]
        # Load it into our collection (list of lists)
        students.append(student_data)
        file.close()
except FileNotFoundError as e:
    print('Text file not found')
    print("----- Error Information -----")
    print(e, e.__doc__, type(e), sep='\n')
    print("Now creating a new file since it doesn't exist")
    file = open(FILE_NAME, "w")

except PermissionError as e:
    print("Permission denied")
    print("----- Error Information -----")
    print(e, e.__doc__, type(e), sep='\n')
    print("Now creating a new file since you don't currently have permissions")
    file = open(FILE_NAME, "w")

# Catch all error handling for any other errors
except Exception as e:
    print("Unexpected error occurred")
    print("----- Error Information -----")
    print(e, e.__doc__, type(e), sep='\n')
    print("Now creating a new file")
    file = open(FILE_NAME, "w")


# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The student's first name is not valid; please enter only alphabetic characters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The student's last name is not valid; please enter only alphabetic characters.")
            course_name = input("Please enter the name of the course: ")
            if not course_name.isalnum():
                raise ValueError("This course is not valid; please enter only alphanumeric characters.")

            student_data = [student_first_name,student_last_name,course_name]
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            #print(e)
            print("----- Error Information -----")
            print(e, e.__doc__, type(e), sep='\n')

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student[0]},{student[1]},{student[2]}\n"
                file.write(csv_data)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        except Exception as e:
            print("Unexpected error occurred")
            print("----- Error Information -----")
            print(e, e.__doc__, type(e), sep='\n')

        finally:
           if not file.closed:
              file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")


print("Program Ended")
