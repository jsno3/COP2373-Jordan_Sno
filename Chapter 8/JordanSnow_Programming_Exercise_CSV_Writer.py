""" The purpose of this program is to allow an instructor to input the number of students
they wish to enter into a CSV file, and then the program will iterate through a loop to enter
the student's first name, last name, and their grades for three separate exams.
"""

# Import csv to write 'grades.csv' later in program
import csv


# Define main
def main():

    # Set variable 'entries_amount' equal to the input from the user dictating how many students they wish to enter
    entries_amount = input('How many students are being entered? ')

    # Open 'grades.csv' as 'new_file' in write mode, using the 'with' keyword, and set newline=''
    with open('grades.csv', 'w', newline='') as new_file:

        # Define variable 'fieldnames' to be used in when writing the csv file
        fieldnames = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

        # Define variable 'csv_writer' and set it equal to 'csv.DictWriter(new_file, fieldnames=fieldnames)'
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        # Write headers (First Name, Last Name, Exam 1, Exam 2, Exam 3) for better organization
        csv_writer.writeheader()

        # For loop, for 'i' in the range of 'entries_amount' (the number of students to be entered):
        for i in range(int(entries_amount)):

            # Set variable 'first' equal to the input for string: 'Enter Student's First Name: '
            first = input("Enter Student's First Name: ")

            # Set variable 'last' equal to the input for string: 'Enter Student's Last Name: '
            last = input("Enter Student's Last Name: ")

            # Set variable 'exam_1' equal to the input for string: 'Enter Student's Grade for Exam 1: '
            exam_1 = int(input("Enter Student's Grade for Exam 1: "))

            # Set variable 'exam_2' equal to the input for string: 'Enter Student's Grade for Exam 2: '
            exam_2 = int(input("Enter Student's Grade for Exam 2: "))

            # Set variable 'exam_3' equal to the input for string: 'Enter Student's Grade for Exam 3: '
            exam_3 = int(input("Enter Student's Grade for Exam 3: "))

            # Create variable 'd' and set it equal to a dictionary that assigns the declared fields with the inputted related data
            d = {'First Name': first, 'Last Name': last, 'Exam 1': exam_1, 'Exam 2': exam_2, 'Exam 3': exam_3}

            # Write a new row to 'grades.csv' passing in the dictionary 'd'
            csv_writer.writerow(d)


# Call main
main()