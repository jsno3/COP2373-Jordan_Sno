
# from numpy import genfromtxt

import numpy as np

# class Calculations():
#
#     def __init__(self, mean, median, std, min, max):
#
#         self.mean = mean
#
#         self.median = median
#
#         self.std = std
#
#         self.min = min
#
#         self.max = max
#
#     def stats(self):
#
#         mean = np.mean()

def main():

    array = np.genfromtxt('grades.csv', delimiter=',', dtype = str)

    print(array)

    print('Here are the first three lines of the array: \n', array[:3])

    column_1 = array[1:, 2]

    column_1 = np.astype(column_1, 'i')

    print(column_1)

    column_2 = array[1:, 3]

    column_2 = np.astype(column_2, 'i')

    print(column_2)

    column_3 = array[1:, 4]

    print(column_3)

    column_3 = np.astype(column_3, 'i')

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

    print(column_1_stats_fl)



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

    print(column_2_stats_fl)

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

    print(column_3_stats_fl)

main()
