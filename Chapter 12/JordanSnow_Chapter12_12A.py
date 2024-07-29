""" This program is intended to utilize numpy to analyze grades stored in a CSV file. The program will find and display
    mean, median, standard deviation, minimum, and maximum scores amongst the grades and display them according to the
    sample size (individual exam or combined exams). This program will also determine the number of students that passed
    each exam and display this information in integer form per exam. Finally, the program will calculate the pass
    percentage across all exams and display it.
"""

# Import numpy as np
import numpy as np


# Define main
def main():

    # 2
    # Set variable 'array' equal to a numpy array pulling data from file 'grades.csv', setting the delimiter as a comma,
    # and the date type as a string
    array = np.genfromtxt('grades.csv', delimiter=',', dtype=str)

    # Test print statement to ensure array is properly formatted
    # print(array)

    # 3
    # Formatted print statement to display to the user the organization of the array
    # (first three lines including the headers)
    print('Here are the first three lines of the array: \n', array[:3], '\n')

    # 4
    # Set variable 'column_1' equal to the Exam 1 column of the numpy array 'array'
    column_1 = array[1:, 2]

    # Update variable 'column_1' with the converted version of the data pulled from 'array' (converted to an integer)
    column_1 = np.astype(column_1, 'i')

    # Test print statement to ensure the converted version is correct
    # print(column_1)

    # Set variable 'column_2' equal to the Exam 2 column of the numpy array 'array'
    column_2 = array[1:, 3]

    # Update variable 'column_2' with the converted version of the data pulled from 'array' (converted to an integer)
    column_2 = np.astype(column_2, 'i')

    # Test print statement to ensure the converted version is correct
    # print(column_2)

    # Set variable 'column_3' equal to the Exam 3 column of the numpy array 'array'
    column_3 = array[1:, 4]

    # Update variable 'column_3' with the converted version of the data pulled from 'array' (converted to an integer)
    column_3 = np.astype(column_3, 'i')

    # Test print statement to ensure the converted version is correct
    # print(column_3)

    # Set variable 'stats' equal to a list containing strings that will be used for multiple print statements
    stats = ['mean score', 'median score', 'standard deviation', 'minimum score', 'maximum score']

    # Set variable 'column_1_stats' equal to an empty list
    column_1_stats = []

    # Set variable 'column_1_stats_fl' equal to an empty list
    column_1_stats_fl = []

    # Set variable 'column_1_mean' equal to the calculated mean of the Exam 1 column
    column_1_mean = np.mean(column_1, axis=0)

    # Append list 'column_1_stats' with variable 'column_1_mean'
    column_1_stats.append(column_1_mean)

    # Set variable 'column_1_median' equal to the calculated median of the Exam 1 column
    column_1_median = np.median(column_1, axis=0)

    # Append list 'column_1_stats' with variable 'column_1_median'
    column_1_stats.append(column_1_median)

    # Set variable 'column_1_std' equal to the calculated standard deviation of the Exam 1 column
    column_1_std = np.std(column_1, axis=0)

    # Append list 'column_1_stats' with variable 'column_1_std'
    column_1_stats.append(column_1_std)

    # Set variable 'column_1_min' equal to the calculated minimum value of the Exam 1 column
    column_1_min = np.min(column_1, axis=0)

    # Append list 'column_1_stats' with variable 'column_1_min'
    column_1_stats.append(column_1_min)

    # Set variable 'column_1_max' equal to the calculated maximum value of the Exam 1 column
    column_1_max = np.max(column_1, axis=0)

    # Append list 'column_1_stats' with variable 'column_1_max'
    column_1_stats.append(column_1_max)

    # For loop
    # For i in list 'column_1_stats'
    for i in column_1_stats:

        # Append the list 'column_1_stats_fl' with the rounded and formatted values from list 'column_1_stats'
        column_1_stats_fl.append(round(float(i), 2))

    # Set variable 'x' equal to 0 to be used as a counter
    x = 0

    # For loop
    # For i in list 'stats'
    for i in stats:

        # Formatted print statement that pulls strings from list 'stats' and floats from list 'column_1_stats' to
        # display the statistical calculations for Exam 1
        print(f'The {i} for exam 1 was {column_1_stats_fl[x]}')

        # Counter to iterate through list 'column_1_stats_fl'
        # variable x+= 1
        x += 1

    # Empty print statement to insert a new line
    print()

    # Set variable 'column_2_stats' equal to an empty list
    column_2_stats = []

    # Set variable 'column_2_stats_fl' equal to an empty list
    column_2_stats_fl = []

    # Set variable 'column_2_mean' equal to the calculated mean of the Exam 2 column
    column_2_mean = np.mean(column_2, axis=0)

    # Append list 'column_2_stats' with variable 'column_2_mean'
    column_2_stats.append(column_2_mean)

    # Set variable 'column_2_median' equal to the calculated median of the Exam 2 column
    column_2_median = np.median(column_2, axis=0)

    # Append list 'column_2_stats' with variable 'column_2_median'
    column_2_stats.append(column_2_median)

    # Set variable 'column_2_std' equal to the calculated standard deviation of the Exam 2
    column_2_std = np.std(column_2, axis=0)

    # Append list 'column_2_stats' with variable 'column_2_std'
    column_2_stats.append(column_2_std)

    # Set variable 'column_2_min' equal to the calculated minimum value of the Exam 2
    column_2_min = np.min(column_2, axis=0)

    # Append list 'column_2_stats' with variable 'column_2_min'
    column_2_stats.append(column_2_min)

    # Set variable 'column_2_max' equal to the calculated maximum value of the Exam 2
    column_2_max = np.max(column_2, axis=0)

    # Append list 'column_2_stats' with variable 'column_2_max'
    column_2_stats.append(column_2_max)

    # For loop
    # For i in list 'column_2_stats'
    for i in column_2_stats:

        # Append the list 'column_2_stats_fl' with the rounded and formatted values from list 'column_2_stats'
        column_2_stats_fl.append(round(float(i), 2))

    # Set variable 'x' equal to 0 to be used as a counter
    x = 0

    # For loop
    # For i in list 'stats'
    for i in stats:

        # Formatted print statement that pulls strings from list 'stats' and floats from list 'column_2_stats_fl' to
        # display the statistical calculations for Exam 2
        print(f'The {i} for exam 2 was {column_2_stats_fl[x]}')

        # Counter to iterate through list 'column_2_stats_fl'
        # variable x+= 1
        x += 1

    # Empty print statement to insert a new line
    print()

    # Set variable 'column_3_stats' equal to an empty list
    column_3_stats = []

    # Set variable 'column_3_stats_fl' equal to an empty list
    column_3_stats_fl = []

    # Set variable 'column_3_mean' equal to the calculated mean of the Exam 3 column
    column_3_mean = np.mean(column_3, axis=0)

    # Append list 'column_3_stats' with variable 'column_3_mean'
    column_3_stats.append(column_3_mean)

    # Set variable 'column_3_median' equal to the calculated median of the Exam 3 column
    column_3_median = np.median(column_3, axis=0)

    # Append list 'column_3_stats' with variable 'column_3_median'
    column_3_stats.append(column_3_median)

    # Set variable 'column_3_std' equal to the calculated standard deviation of the Exam 3
    column_3_std = np.std(column_3, axis=0)

    # Append list 'column_3_stats' with variable 'column_3_std'
    column_3_stats.append(column_3_std)

    # Set variable 'column_3_min' equal to the calculated minimum value of the Exam 3
    column_3_min = np.min(column_3, axis=0)

    # Append list 'column_3_stats' with variable 'column_3_min'
    column_3_stats.append(column_3_min)

    # Set variable 'column_3_max' equal to the calculated maximum value of the Exam 3
    column_3_max = np.max(column_3, axis=0)

    # Append list 'column_3_stats' with variable 'column_3_max'
    column_3_stats.append(column_3_max)

    # For loop
    # For i in list 'column_3_stats'
    for i in column_3_stats:

        # Append the list 'column_3_stats_fl' with the rounded and formatted values from list 'column_3_stats'
        column_3_stats_fl.append(round(float(i), 2))

    # Set variable 'x' equal to 0 to be used as a counter
    x = 0

    # For loop
    # For i in list 'stats'
    for i in stats:

        # Formatted print statement that pulls strings from list 'stats' and floats from list 'column_3_stats_fl' to
        # display the statistical calculations for Exam 3
        print(f'The {i} for exam 3 was {column_3_stats_fl[x]}')

        # Counter to iterate through list 'column_3_stats_fl'
        # variable x+= 1
        x += 1

    # Empty print statement to insert a new line
    print()

    # 5
    # Set variable 'all_exams' equal to the value of the concatenation of all three exam columns
    all_exams = np.concatenate((column_1, column_2, column_3), axis=0)

    # Test print statement to ensure all_exams is correct
    # print(all_exams)

    # Set variable 'all_exams_stats' equal to an empty list
    all_exams_stats = []

    # Set variable 'all_exams_stats_fl' equal to an empty list
    all_exams_stats_fl = []

    # Set variable 'all_exams_stats_mean' equal to the calculated mean of all exam columns
    all_exams_stats_mean = np.mean(all_exams, axis=0)

    # Append list 'all_exams_stats' with the result of 'all_exams_stats_mean'
    all_exams_stats.append(all_exams_stats_mean)

    # Set variable 'all_exams_stats_median' equal to the calculated median of all exam columns
    all_exams_stats_median = np.median(all_exams, axis=0)

    # Append list 'all_exams_stats' with the result of 'all_exams_stats_median'
    all_exams_stats.append(all_exams_stats_median)

    # Set variable 'all_exams_stats_std' equal to the calculated standard deviation of all exam columns
    all_exams_stats_std = np.std(all_exams, axis=0)

    # Append list 'all_exams_stats' with the result of 'all_exams_stats_std'
    all_exams_stats.append(all_exams_stats_std)

    # Set variable 'all_exams_stats_min' equal to the calculated minimum value from all exam columns
    all_exams_stats_min = np.min(all_exams, axis=0)

    # Append list 'all_exams_stats' with the result of 'all_exams_stats_min'
    all_exams_stats.append(all_exams_stats_min)

    # Set variable 'all_exams_stats_max' equal to the calculated maximum value from all exam columns
    all_exams_stats_max = np.max(all_exams, axis=0)

    # Append list 'all_exams_stats' with the result of 'all_exams_stats_max'
    all_exams_stats.append(all_exams_stats_max)

    # For loop
    # For i in list 'all_exams_stats'
    for i in all_exams_stats:

        # Append the list 'all_exams_stats_fl' with the rounded and formatted values from list 'all_exams_stats'
        all_exams_stats_fl.append(round(float(i), 2))

    # Set variable 'x' equal to 0 to be used as a counter
    x = 0

    # For loop
    # For i in list 'stats'
    for i in stats:

        # Formatted print statement that pulls strings from list 'stats' and floats from list 'all_exams_stats_fl' to
        # display the statistical calculations across all exams
        print(f'The {i} for all exams was {all_exams_stats_fl[x]}')

        # Counter to iterate through list 'all_exams_stats_fl'
        x += 1

    # Empty print statement to insert a new line
    print()

    # 6
    # Set variable 'exam_1_pass' equal to 0 to be used as a counter
    exam_1_pass = 0

    # Set variable 'exam_1_fail' equal to 0 to be used as a counter
    exam_1_fail = 0

    # For loop
    # For grade in list 'column_1'
    for grade in column_1:

        # If statement
        # If grade is greater or equal to 60
        if grade >= 60:

            # Add 1 passing grade to the list 'exam_1_pass'
            exam_1_pass += 1

        # If statement
        # If grade is less than 60
        if grade < 60:

            # Add 1 failing grade to the list 'exam_1_fail'
            exam_1_fail += 1

    # Formatted print statement to show the amount of students that passed the first exam out of 10
    print(f'{exam_1_pass}/{(int(len(column_1)))} students passed the first exam.\n')

    # Test print statement to print the amount of students failed for assurance
    # print(exam_1_fail, 'students failed the first exam.')

    # Set variable 'exam_2_pass' equal to 0 to be used as a counter
    exam_2_pass = 0

    # Set variable 'exam_2_fail' equal to 0 to be used as a counter
    exam_2_fail = 0

    # For loop
    # For grade in list 'column_2'
    for grade in column_2:

        # If statement
        # If grade is greater or equal to 60
        if grade >= 60:

            # Add passing grade to the list 'exam_2_pass'
            exam_2_pass += 1

        # If statement
        # If grade is less than 60
        if grade < 60:

            # Add failing grade to the list 'exam_2_fail'
            exam_2_fail += 1

    # Formatted print statement to show the amount of students that passed the second exam out of 10
    print(f'{exam_2_pass}/{(int(len(column_2)))} students passed the second exam.\n')

    # Test print statement to print the amount of students failed for assurance
    # print(exam_2_fail, 'students failed the second exam.')

    # Set variable 'exam_2_pass' equal to 0 to be used as a counter
    exam_3_pass = 0

    # Set variable 'exam_2_fail' equal to 0 to be used as a counter
    exam_3_fail = 0

    # For loop
    # For grade in list 'column_3'
    for grade in column_3:

        # If statement
        # If grade is greater or equal to 60
        if grade >= 60:

            # Add passing grade to the list 'exam_3_pass'
            exam_3_pass += 1

        # If statement
        # If grade is less than 60
        if grade < 60:

            # Add failing grade to the list 'exam_3_fail'
            exam_3_fail += 1

    # Formatted print statement to show the amount of students that passed the third exam out of 10
    print(f'{exam_3_pass}/{(int(len(column_1)))} students passed the third exam.\n')

    # Test print statement to print the amount of students failed for assurance
    # print(exam_3_fail, 'students failed the third exam.')

    # 7
    # Set variable 'all_exam_pass' equal to 0 to be used as a counter
    all_exam_pass = 0

    # Set variable 'all_exam_fail' equal to 0 to be used as a counter
    all_exam_fail = 0

    # For loop
    # For grade in list 'all_exams'
    for grade in all_exams:

        # If statement
        # If grade is greater or equal to 60
        if grade >= 60:

            # Add passing grade to the list 'all_exam_pass'
            all_exam_pass += 1

        # If statement
        # If grade is less than 60
        if grade < 60:

            # Add failing grade to the list 'all_exam_fail'
            all_exam_fail += 1

    # Test print statement to print the amount of students failed across all exams for assurance
    # print(all_exam_pass)

    # Set variable 'all_exam_pass_percentage' equal to the calculated value of variable 'all_exam_pass'
    # divided by the value of all exams taken multiplied by 100
    all_exam_pass_percentage = ((all_exam_pass/(int(len(all_exams))))*100)

    # Formatted print statement to display the variable 'all_exam_pass_percentage' rounded off to two decimals
    print(f'The overall pass percentage across all exams is {all_exam_pass_percentage:.2f}%\n')


# Call main
main()
