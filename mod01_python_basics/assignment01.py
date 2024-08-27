# ---------------------------------------------------------------------------- #
# Title: Assignment01
# Desc: This assignment demonstrates using constants, variables, and print()
# Change Log: (Who, When, What)
# AHilgendorf, 7/31/2024, Created Script
# ---------------------------------------------------------------------------- #

# This is a constant and goes all upper case as it will not change
COURSE_NAME = "Python 100"


# The next two pieces of data are variables and are meant to change
# For variables we use lowercase 

student_first_name = input("What is your first name? ")

student_last_name = input("What is your last name? ")

'''
The next two print commands will generate the same output through two different
ways. The first statement runs in one line, but the second statement uses the \
to continue statement in a second line. 
'''

print(student_first_name + " " + student_last_name + " is registered for the " + COURSE_NAME + " course")

print(student_first_name + " " + student_last_name + " is registered for the " \
      + COURSE_NAME + " course")
