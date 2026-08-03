
# Import packages for use in program
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

# Creates a database with a table that contains 10 Florida cities and their populations in the year 2023
def main():

    # Creates/connects database and makes a cursor for it
    conn = sqlite3.connect('population_CM.db')
    popCursor = conn.cursor()

    # Drop table if it already exists for clean setup
    popCursor.execute('DROP TABLE IF EXISTS population')
    # Creates table in database
    popCursor.execute('''
        CREATE TABLE population (
            city TEXT,
            year INTEGER,
            population INTEGER
            )''')

    # Adds data of 10 Florida cities to table
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("Venice" , 2023, 27793)')
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("Sarasota", 2023, 57005)')
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("Jacksonville", 2023, 1004869)')
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("North Port", 2023, 86552)')
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("Fort Myers", 2023, 97711)')
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("Punta Gorda", 2023, 20410)')
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("Naples", 2023, 19306)')
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("Fort Lauderdale", 2023, 189118)')
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("Miami", 2023, 464225)')
    popCursor.execute('INSERT INTO population (city, year, population) VALUES ("St. Augustine", 2023, 15307)')

    # Get list of cities in table to go through in other functions
    popCursor.execute('SELECT city FROM population')
    cities = [row[0] for row in popCursor.fetchall()]
    conn.commit()
    conn.close()

    # Call function to simulate 20 years of growth/decline in population
    pop_change(cities)
    # Call function to display graph of user selected city's population changes
    pop_graph(cities)

    # End of program


# Simulates varying population growth/decline over 20 years for each city
# and adds to population table in database
def pop_change(cities):

    # Connect to database
    conn = sqlite3.connect('population_CM.db')
    popCursor = conn.cursor()

    # Go through each city
    for city in cities:
        # Randomized growth/decline set for 20 years, changes each city/loop instance
        # Is randomized between -2% and +2%
        popRate = np.random.uniform(low=-.02, high=.02, size=20)

        # Get starting population (year 2023)
        popCursor.execute('SELECT population FROM population WHERE city = ? AND year = ?', (city, 2023))
        population = popCursor.fetchone()[0]

        # Simulate 20 years for current city
        for i in range(20):
            # Get new population and year
            population = int(population * (1 + popRate[i]))
            newYear = 2023 + i + 1

            # Add new data as new row in table
            popCursor.execute('''INSERT OR IGNORE INTO population (city, year, population) 
            VALUES (?, ?, ?)''', (city, newYear, population))

    # End of simulation function
    conn.commit()
    conn.close()
    return cities



# Displays graph of a city's population changes, city is user selected
def pop_graph(cities):

    # Setup database connection
    conn = sqlite3.connect('population_CM.db')
    popCursor = conn.cursor()

    # Get user's choice of city to graph
    print('Your choices are:')
    print(*cities, sep= ', ')
    print()
    # Checks if user entered a valid choice
    while True:
        try:
            cityChoice = input("Enter the city you'd like to see graphed (case sensitive): ")

            if cityChoice in cities:
                break
            else:
                error()
        except:
            print('Please enter a valid city')

    # Get data from database table
    popCursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (cityChoice,))
    graphData = popCursor.fetchall()

    conn.close()

    # Display graph of data to user
    years = [row[0] for row in graphData]
    pops = [row[1] for row in graphData]
    graphTitle = 'Population graph of %s' %cityChoice

    plt.plot(years, pops)
    plt.xticks(np.arange(2023, 2044, 2))
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(graphTitle)
    plt.show()


# Call main to start program
main()