
# import csv

from numpy import genfromtxt

def main():

    array = genfromtxt('grades.csv', delimiter=',', dtype=None)

    print(array)

    exit()

main()
