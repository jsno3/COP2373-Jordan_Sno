
import sqlite3

def main():

    conn = sqlite3.connect('population_JS.db')

    cur = conn.cursor()

    add_population_table(cur)

    add_population(cur)

    conn.commit()

    display_population(cur)

    conn.close()


def add_population_table(cur):

    cur.execute('DROP TABLE IF EXISTS Population')

    cur.execute(""" CREATE TABLE Population (
                City TEXT,
                Year INT(4),
                Population INT(7))""")

def add_population(cur):
    population_pop = [('Cape Coral', 2023, 224455),
                  ('Dunedin', 2023, 35930),
                  ('Gainesville', 2023, 145812),
                  ('Jupiter', 2023, 61291),
                  ('Largo', 2023, 82248),
                  ('Miami', 2023, 455924),
                  ('Okeechobee', 2023, 5602),
                  ('Pensacola',2023, 53724),
                  ('St. Cloud',2023, 66448),
                  ('Winter Haven', 2023, 57109)]

    for row in population_pop:
        cur.execute('''INSERT INTO Population (City, Year, Population)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

# The display_population function displays the contents of the Population table
def display_population(cur):

    print('Contents of population_JS.db/Population table:')

    cur.execute('SELECT * FROM Population')

    results = cur.fetchall()

    for row in results:

        print(f'{row[0]:15}{row[1]:0}{row[2]:10,.0f}')

# Execute the main function.
if __name__ == '__main__':
    main()


def pop():

    global pop_list

    conn = sqlite3.connect('population_JS.db')

    cur = conn.cursor()

    cur.execute("SELECT population FROM Population")

    pop_list = []

    for i in range(10):

        for i in cur.fetchone():

            pop_list.append(i)

    print(pop_list)

    for i in pop_list:

        print(i)

    conn.close()

pop()


def pop_growth():

    global pop_growth_list

    pop_growth_list = []

    for int in pop_list:

        i = float(int)

        t = 20

        r = 0.02

        for x in range(t):

            i *= (1.0 + r)


        i = round(i)

        pop_growth_list.append(i)

    print(pop_growth_list)


pop_growth()


# def add_row():
#
#     conn = sqlite3.connect('population_JS.db')
#
#     cur = conn.cursor()
#
#     for row in pop_growth:
#
#         cur.execute('''INSERT INTO Population (Predicted Growth,)
#                        VALUES (?)''', (row[3]))
#
# add_row()

