""" The purpose of this program is to create a database called population_JS that houses the following fields:
city, year, and population. 10 cities in Florida along with their populations in 2023 will then be inserted into 
population_JS as a table named 'Population'. After this table is created a function will pull the population 
statistics from the table and simulate population growth for 20 years at a 2% growth rate for each year. This 
data will then be inserted into the population table. Finally, matplotlib is used to display the population 
growth for a specified city in a graph.
"""

# Import sqlite3
import sqlite3

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Import numpy as np
import numpy as np


# Def main
def main():

    # Set variable 'conn' equal to sqlite3 connecting to database 'population_JS.db'
    conn = sqlite3.connect('population_JS.db')

    # Set variable 'cur' equal to variable 'conn' using the cursor method
    cur = conn.cursor()

    # Call 'add_population_table' passing in variable 'cur'
    add_population_table(cur)

    # Call 'add_population' passing in variable 'cur'
    add_population(cur)

    # Commit the changes to the connection through variable 'conn'
    conn.commit()

    # Call 'display_population' passing in variable 'cur'
    display_population(cur)

    # Call choice
    choice()

    # Call add_growth_column_and_populate
    add_growth_column_and_populate()

    # Call 'diagram' passing in variables 'cur' and 'city
    diagram(cur, city)

    # Close the connection
    conn.close()


# Define 'add_population_table' passing in variable 'cur'
def add_population_table(cur):

    # Execute cursor to drop table if it already exists
    cur.execute('DROP TABLE IF EXISTS Population')

    # Execute cursor to create a table named 'Population' that has three fields: 'City', 'Year', and 'Population'
    cur.execute(""" CREATE TABLE Population (
                City TEXT,
                Year INT(4),
                Population INT(7))""")


# Define 'add_population' passing in variable 'cur'
def add_population(cur):
    # Set variable 'population_pop' equal to a list filled with the information for the table 'Population'
    population_pop = [('Cape Coral', 2023, 224455),
                      ('Dunedin', 2023, 35930),
                      ('Gainesville', 2023, 145812),
                      ('Jupiter', 2023, 61291),
                      ('Largo', 2023, 82248),
                      ('Miami', 2023, 455924),
                      ('Okeechobee', 2023, 5602),
                      ('Pensacola', 2023, 53724),
                      ('St. Cloud', 2023, 66448),
                      ('Winter Haven', 2023, 57109)]

    # For loop
    # For row in 'population_pop'
    for row in population_pop:
        # Execute cursor to insert list 'population_pop' into table 'Population'
        cur.execute('''INSERT INTO Population (City, Year, Population)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))


# The display_population function displays the contents of the Population table
def display_population(cur):

    # Print statement explaining to the user where the table is from
    print('Contents of population_JS.db/Population table:')

    # Execute cursor to select everything from the table 'Population'
    cur.execute('SELECT * FROM Population')

    # Set variable 'results' equal to cursor using the 'fetchall' method
    results = cur.fetchall()

    # For loop
    # For row in variable 'results'
    for row in results:

        # Formatted print statement to display the information from table 'Population'
        print(f'{row[0]:15}{row[1]:0}{row[2]:10,.0f}')


# Define add_growth_column_and_populate
def add_growth_column_and_populate():

    # Set variable 'conn' equal to sqlite3 connecting to database 'population_JS.db'
    conn = sqlite3.connect('population_JS.db')

    # Set variable 'cur' equal to variable 'conn' using the cursor method
    cur = conn.cursor()

    # Execute cursor to alter table 'Population' and add 'Projected_Population' expecting data type integer
    cur.execute("""
        ALTER TABLE Population
            ADD [Projected_Population] INT;
        """)

    # Execute cursor to update table 'Population' with the projected population growth set to 'Projected_Population'
    cur.execute("""
            UPDATE Population
            SET Projected_Population = ROUND(Population * POWER(1.02, 20), 2);
            """)

    # Commit the changes to the connection through variable 'conn'
    conn.commit()

    # Close the connection
    conn.close()


# Define choice
def choice():

    # Set variable 'city' to global
    global city

    # Print statement to inform the user to pick a city
    print('Pick a City that you would like to see the projected population growth of. (1-10)')

    # Print statement to inform the user what citys are available in the table
    print('The following cities are available to select: ',
          '\n1) Cape Coral',
          '\n2) Dunedin',
          '\n3) Gainesville',
          '\n4) Jupiter',
          '\n5) Largo'
          '\n6) Miami',
          '\n7) Okeechobee',
          '\n8) Pensacola',
          '\n9) St. Cloud',
          '\n10) Winter Haven')

    # Set variable 'city' equal to the input from the user converted to an integer
    city = (int(input('Please make a selection. ')))


# Define diagram passing in variables 'cur' and 'city'
def diagram(cur, city):

    # Set variable 'city_dic' equal to a dictionary full of the cities from the table along with corresponding keys
    city_dic = {1: 'Cape Coral', 2: 'Dunedin', 3: 'Gainesville', 4: 'Jupiter', 5: 'Largo',
                6: 'Miami', 7: 'Okeechobee', 8: 'Pensacola', 9: 'St. Cloud', 10: 'Winter Haven'}

    # Set variable 'print_city' equal to the value from dictionary 'city_dic' passing in the key that the user entered
    print_city = city_dic[city]

    # Print statement to inform the user which city's population growth they are viewing
    print(f'Displaying the projected population growth of {print_city} across the next 20 years.')

    # Execute cursor on formatted string to pull 'Population' and 'Projected_Population' from the specified city
    cur.execute(f"select Population, Projected_Population from Population where city = '{print_city}'")

    # Set variable 'data' equal to cursor using the method fetchone
    data = cur.fetchone()

    # Print variable 'data'
    print(data)

    # Set variable 'x_points' equal to a numpy array ranging from 1 to 20
    x_points = np.array([1, 20])

    # Set variable 'y_points' equal to a numpy array ranging from the values
    # 'data[0]' to 'data[1]' converted to integers
    y_points = np.array([int(data[0]), int(data[1])])

    # Create a graph defining the x-axis as 'x_points' and the y-axis as 'y_points'
    plt.plot(x_points, y_points)

    # Show the graph that has been created
    plt.show()


# Execute the main function.
if __name__ == '__main__':
    main() 
