
import numpy as np

def main():

    # 2
    array = np.genfromtxt('grades.csv', delimiter=',', dtype = str)

    # print(array)

    # 3
    print('Here are the first three lines of the array: \n', array[:3], '\n')

    # 4
    column_1 = array[1:, 2]

    column_1 = np.astype(column_1, 'i')

    # print(column_1)

    column_2 = array[1:, 3]

    column_2 = np.astype(column_2, 'i')

    # print(column_2)

    column_3 = array[1:, 4]

    column_3 = np.astype(column_3, 'i')

    # print(column_3)

    stats = ['Mean score', 'Median score', 'Standard Deviation', 'Minimum score', 'Maximum score']

    column_1_stats = []

    column_1_stats_fl = []

    column_1_mean = np.mean(column_1, axis=0)

    column_1_stats.append(column_1_mean)

    column_1_median = np.median(column_1, axis=0)

    column_1_stats.append(column_1_median)

    column_1_std = np.std(column_1, axis=0)

    column_1_stats.append(column_1_std)

    column_1_min = np.min(column_1, axis=0)

    column_1_stats.append(column_1_min)

    column_1_max = np.max(column_1, axis=0)

    column_1_stats.append(column_1_max)



    for i in column_1_stats:

        column_1_stats_fl.append(round(float(i), 2))

    x = 0

    for i in stats:
        print(f'The {i} for Exam 1 was {column_1_stats_fl[x]}')
        x += 1

    print('\n')

    column_2_stats = []

    column_2_stats_fl = []

    column_2_mean = np.mean(column_2, axis=0)

    column_2_stats.append(column_2_mean)

    column_2_median = np.median(column_2, axis=0)

    column_2_stats.append(column_2_median)

    column_2_std = np.std(column_2, axis=0)

    column_2_stats.append(column_2_std)

    column_2_min = np.min(column_2, axis=0)

    column_2_stats.append(column_2_min)

    column_2_max = np.max(column_2, axis=0)

    column_2_stats.append(column_2_max)



    for i in column_2_stats:
        column_2_stats_fl.append(round(float(i), 2))

    x = 0

    for i in stats:
        print(f'The {i} for Exam 2 was {column_2_stats_fl[x]}')
        x += 1

    print('\n')



    column_3_stats = []

    column_3_stats_fl = []

    column_3_mean = np.mean(column_3, axis=0)

    column_3_stats.append(column_3_mean)

    column_3_median = np.median(column_3, axis=0)

    column_3_stats.append(column_3_median)

    column_3_std = np.std(column_3, axis=0)

    column_3_stats.append(column_3_std)

    column_3_min = np.min(column_3, axis=0)

    column_3_stats.append(column_3_min)

    column_3_max = np.max(column_3, axis=0)

    column_3_stats.append(column_3_max)




    for i in column_3_stats:

        column_3_stats_fl.append(round(float(i), 2))

    x = 0

    for i in stats:
        print(f'The {i} for Exam 3 was {column_3_stats_fl[x]}')
        x += 1

    print('\n')


    # 5
    all_exams = np.concatenate((column_1, column_2, column_3), axis=0)

    # print(all_exams)

    all_exams_stats = []

    all_exams_stats_fl = []

    all_exams_stats_mean = np.mean(all_exams, axis=0)

    all_exams_stats.append(all_exams_stats_mean)

    all_exams_stats_median = np.median(all_exams, axis=0)

    all_exams_stats.append(all_exams_stats_median)

    all_exams_stats_std = np.std(all_exams, axis=0)

    all_exams_stats.append(all_exams_stats_std)

    all_exams_stats_min = np.min(all_exams, axis=0)

    all_exams_stats.append(all_exams_stats_min)

    all_exams_stats_max = np.max(all_exams, axis=0)

    all_exams_stats.append(all_exams_stats_max)



    for i in all_exams_stats:

        all_exams_stats_fl.append(round(float(i), 2))

    x = 0

    for i in stats:
        print(f'The {i} for all Exams was {all_exams_stats_fl[x]}')
        x += 1

    print('\n')

    # 6
    exam_1_pass = 0

    exam_1_fail = 0

    for grade in column_1:

        if grade >= 60:

            exam_1_pass += 1

        if grade < 60:

            exam_1_fail += 1

    print(f'{exam_1_pass}/{(int(len(column_1)))} students passed the first exam.\n')

    # print(exam_1_fail, 'students failed the first exam.')



    exam_2_pass = 0

    exam_2_fail = 0

    for grade in column_2:

        if grade >= 60:
            exam_2_pass += 1

        if grade < 60:
            exam_2_fail += 1

    print(f'{exam_2_pass}/{(int(len(column_2)))} students passed the second exam.\n')

    # print(exam_2_fail, 'students failed the second exam.')



    exam_3_pass = 0

    exam_3_fail = 0

    for grade in column_3:

        if grade >= 60:
            exam_3_pass += 1

        if grade < 60:
            exam_3_fail += 1

    print(f'{exam_3_pass}/{(int(len(column_1)))} students passed the third exam.\n')

    # print(exam_3_fail, 'students failed the third exam.')



    # 7
    all_exam_pass = 0

    all_exam_fail = 0

    for grade in all_exams:

        if grade >= 60:
            all_exam_pass += 1

        if grade < 60:
            all_exam_fail += 1

    # print(all_exam_pass)

    all_exam_pass_percentage = ((all_exam_pass/(int(len(all_exams))))*100)

    print(f'The overall pass percentage across all exams is {all_exam_pass_percentage}%\n')

    close = input('Hit enter to close the program. ')

main()
