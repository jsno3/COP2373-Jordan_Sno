# The purpose of this program is to read the created csv file: 'grades.csv' and display it in a formatted DataFrame

# Import package 'pandas' as 'pd' for further use in the program
import pandas as pd


# Define main
def main():

  # Open the CSV file in read mode with 'with' keyword
  with open('grades.csv', 'r'):

    # Set variable 'df' equal to the result of reading the csv file into a DataFrame
    df = pd.read_csv('grades.csv')

    # Print DataFrame with better formatting
    print(df.to_string(index=False))


# Call main
main()