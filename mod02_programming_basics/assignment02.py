# ------------------------------------------------------------------------------------------ #
# Title: Assignment02
# Desc: This assignment demonstrates using constants, variables,
#         operators, formatting, and files and calculations
# Change Log: (Who, When, What)
#   AHilgendorf,8/7/2023,Created Script
# ------------------------------------------------------------------------------------------ #

'''
Constants are named using ALL CAPS per convention
The data type for COURSE_NAME is a string str
The data type for COURSE_PRICE and STATE_TAX is a float 
The TOTAL_PRICE is also storing a float data type and it is the result of
    using arithmetic operators
'''

# Define the Data Constants
COURSE_NAME = "Python 100"
COURSE_PRICE = 999.98
STATE_TAX = .09
TOTAL_PRICE = COURSE_PRICE + COURSE_PRICE * STATE_TAX
FILE_NAME = "Enrollments.csv"


'''
As for the variables, I am declaring them but leaving them "empty"
    since there will be input later that will assign a value. This
    is OK because variables can change.
'''

# Define the Data Variables
student_first_name = ""
student_last_name = ""
course_name = ""
csv_data = ""
file_obj = None


# Get data from the user
student_first_name = input("What is your first name? ")
student_last_name = input("What is your last name? ")

# Present the data to the user
csv_data = f"{student_first_name}, {student_last_name}, \
{COURSE_NAME}, {COURSE_PRICE}, {TOTAL_PRICE}"
print(csv_data)

# Process the data to a file
csv_file = open("Enrollments.csv", 'w')
csv_file.write(csv_data)
