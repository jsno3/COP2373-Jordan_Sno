import pandas as pd


def main():

  # Open the CSV file in read mode with 'with' keyword
  with open('grades.csv', 'r'):

    df = pd.read_csv('grades.csv')

    # Print DataFrame with better formatting
    print(df.to_string(index=False))


main()