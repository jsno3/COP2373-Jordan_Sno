
# from numpy import genfromtxt

import numpy as np

def main():

    array = np.genfromtxt('grades.csv', delimiter=',', dtype = str)

    print(array)



    print('Here are the first three lines of the array: \n', array[:3])

    column_1 = array[1:, 2]
    print(column_1)

    column_2 = array[1:, 3]
    print(column_2)

    column_3 = array[1:, 4]
    print(column_3)

    column_1_sum = 0

    for i in range(len(column_1)):

        column_1_sum += (int(column_1[i]))

        print(column_1[i])

    column_1_stats = np.mean(column_1)
    print(column_1_stats)

    # Juniper = array[1]
    #
    # print(Juniper)
    #
    # Mary = array[2]
    #
    # print(Mary)
    #
    # Chester = array[3]
    # print(Chester)
    #
    # Dan = array[4]
    # print(Dan)
    #
    # Leonard = array[5]
    # print(Leonard)
    #
    # Lydia = array[6]
    # print(Lydia)
    #
    # Victoria = array[7]
    # print(Victoria)
    #
    # Michael = array[8]
    # print(Michael)
    #
    # Lily = array[9]
    # print(Lily)
    #
    # Carter = array[10]
    # print(Carter)



    # exit()

main()
