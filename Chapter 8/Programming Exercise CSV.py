# Format
# First name, Last name, grades (integers)

import csv

with open('grades.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

# entries_amount = input('How many students are being entered? ')

    # for i in entries_amount:
    with open('new_grades.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)

    # next(csv_reader)

        for line in csv_reader:
            csv_writer.writerow(line)