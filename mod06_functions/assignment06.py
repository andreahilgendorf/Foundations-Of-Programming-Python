# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions with structured error handling
# Change Log: (Who, When, What)
#   AHilgendorf,9/10/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course.
    2. Show current data.
    3. Save data to a file.
    4. Exit the program.
-----------------------------------------

Please enter a menu option:
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = list[dict[str, str, str]]
menu_choice: str  # Holds the choice made by the user.

class IO:
    ''' A class to handle Input/Output '''

    
    @staticmethod
    def output_student_courses(student_data: list):
        ''' This function reads the JSON information from the FILE file '''
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        ''' shows an error message with its technical details   '''
        print(message)
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        '''Presents the menu to the users'''
        print(menu)
    
    @staticmethod
    def input_menu_choice():
        '''Takes user input and prints error message if choice is not allowed '''
        str_choice = input()
        while str_choice not in ["1", "2", "3", "4"]:
            str_choice = input()
            IO.output_error_messages("Please enter an option between 1 and 4")
        return str_choice

    @staticmethod
    def input_student_data(students: list[dict[str, str, str]]) -> list[dict[str, str, str]]:
        student_first_name: str = ''  # Holds the first name of a student entered by the user.
        student_last_name: str = ''  # Holds the last name of a student entered by the user.
        course_name: str = '' # Holds the course name for the student
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should be alphabetic")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should alphabetic.")
            course_name = input("Enter the student's course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            return students
        except ValueError as e:
            IO.output_error_messages(str(e), e)
        except Exception as e:
            IO.output_error_messages(str(e), e)


class FileProcessor:
    ''' A class that manages reading the current data and appending data '''    

    @staticmethod
    def write_data_to_file(students_table, file_name):
        '''The function writes data to the JSON file'''
        try:
            file = open(file_name, "w")
            json.dump(students_table, file)
            file.close()
        except Exception as e:
            if file.closed == False: file.close()
            IO.output_error_messages('Error writing, closing file', e)

    @staticmethod
    def read_data_from_file(file_name: str) -> list[dict[str, str, str]]:
        ''''The function reads JSON information from a file'''
        student_table: list[dict[str, str, str]] = []
        try:
            file = open(file_name, "r")
            student_json = json.load(file)
            return student_json
        except FileNotFoundError as e:
            IO.output_error_messages('Creating file as it does not exist..', e)
        except json.JSONDecodeError as e:
            IO.output_error_messages("Data in file is not valid, resetting it..", e)
        except Exception as e:
            print('Unhandled exception')
            IO.output_error_messages(e)
        finally:
            if not file.closed:
                file.close()



# Present and Process the data
students = FileProcessor.read_data_from_file(FILE_NAME)
while (True):
    # Present the menu of choices and get the menu option
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            students = IO.input_student_data(students)
        except Exception as e:
            print(e)

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)

    # Save the data to a file
    elif menu_choice == "3":
            FileProcessor.write_data_to_file(students_table=students,file_name=FILE_NAME)
            print("The following data was saved to file!")
            IO.output_student_courses(student_data=students)

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")