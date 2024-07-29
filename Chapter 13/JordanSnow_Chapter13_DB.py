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

    # Call 'add_column' passing in variable 'cur'
    # add_column(cur)

    # Commit the changes to the connection through variable 'conn'
    conn.commit()

    # Call 'display_population' passing in variable 'cur'
    display_population(cur)

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





# def add_column(cur, pop_growth_list):

    
#     cur.execute("""ALTER TABLE Population
#                 ADD [Projected_Population]  INT;
#                 """)
    
#     for i in pop_growth_list:
        
#         cur.execute('''INSERT INTO Population (Projected_Population)
#                        VALUES (?)''', (row[3]))

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


# add_column()


# Define pop
def pop():

    # Global variable 'pop_list'
    global pop_list

    # Set variable 'conn' equal to sqlite3 connecting to database 'population_JS.db;'
    conn = sqlite3.connect('population_JS.db')

    # Set variable 'cur' equal to 'conn' using the cursor method
    cur = conn.cursor()

    # Execute cursor to select row 'population' from table 'Population'
    cur.execute("SELECT population FROM Population")

    # Set variable 'pop_list' equal to an empty list
    pop_list = []

    # For loop
    # For x in range(10)
    for x in range(10):

        # For i in cursor using the fetchone method
        for i in cur.fetchone():

            # Append list 'pop_list' passing in i
            pop_list.append(i)

    # Test print statement to display 'pop_list'
    print(pop_list)

    # For loop
    # For i in 'pop_list'
    for i in pop_list:

        # Print(i)
        print(i)
    # Close the connection
    conn.close()


# Define pop_growth
def pop_growth():

    # Global variable 'pop_growth_list'
    global pop_growth_list

    # Set variable 'pop_growth_list' equal to an empty list
    pop_growth_list = []

    # For loop
    # For num in pop_list
    for num in pop_list:

        # Set variable 'i' equal to a float of 'num'
        i = float(num)

        # Set variable 't' equal to 20 (to represent years)
        t = 20

        # Set variable 'r' equal to 0.02 (to represent a 2% increase in population)
        r = 0.02

        # For loop
        # For x in range(t)
        for x in range(t):

            # Set variable 'i' equal to the multiplication of 1.02
            i *= (1.0 + r)

        # Set variable 'i' equal to a rounded version of variable 'i'
        i = round(i)

        # Append list 'pop_growth_list' passing in 'i'
        pop_growth_list.append(i)

    # Test print statment to print variable 'pop_growth_list'
    print(pop_growth_list)


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

    # Set variable 'city' equal to the input from the user set to an integer - 1 to receive 0-9
    city = (int(input('Please make a selection. '))-1)

    # If statement to ensure city is between 0 and 9
    if city < 0 or city > 9:
        
        # Print statement to inform user what values they can enter
        print('\nPlease enter a whole number between 1-10\n')

        # Call choice
        choice()


# Define diagram passing in variable 'city'
def diagram(city):

    # Set variable 'city_dic' equal to a dictionary full of the cities from the table along with corresponding keys
    city_dic = {1: 'Cape Coral', 2: 'Dunedin', 3: 'Gainesville', 4: 'Jupiter', 5: 'Largo',
                6: 'Miami', 7: 'Okeechobee', 8: 'Pensacola', 9: 'St. Cloud', 10: 'Winter Haven'}

    # Set variable 'print_city' equal to the value from dictionary 'city_dic' passing in the key + 1 that the user entered
    print_city = city_dic[city + 1]

    # Print statement to inform the user which city's population growth they are viewing
    print('Displaying the projected population growth of', print_city, 'across the next 20 years.')

    # Set variable 'initial' equal to list 'pop_list' passing in value 'city'
    initial = pop_list[city]

    # Test print for 'initial'
    print(initial)

    # Set variable 'estimated' equal to list 'pop_growth_list' passing in value 'city'
    estimated = pop_growth_list[city]
    
    # Test print for 'estimated'
    print(estimated)

    # Set variable 'x_points' equal to a numpy array ranging from 1 to 20
    x_points = np.array([1, 20])

    # Set variable 'y_points' equal to a numpy array ranging from the values 'initial' to 'estimated'
    y_points = np.array([initial, estimated])
    
    # Create a graph defining the x axis as 'x_points' and the y axis as 'y_points'
    plt.plot(x_points, y_points)

    # Show the graph that has been created
    plt.show()


# Execute the main function.
if __name__ == '__main__':

    # Call main
    main() 
    
    # Call pop
    pop()

    # Call pop_growth
    pop_growth()

    # Call choice
    choice()
    
    # Call diagram passing in 'city'
    diagram(city)
