import sqlite3

# Create a database connection
conn = sqlite3.connect('chocolate_house.db')
cursor = conn.cursor()

# Create table for seasonal flavors
cursor.execute('''
CREATE TABLE IF NOT EXISTS seasonal_flavors (
    id INTEGER PRIMARY KEY,
    flavor_name TEXT NOT NULL,
    availability TEXT NOT NULL
)
''')

# Create table for ingredient inventory
cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredient_inventory (
    id INTEGER PRIMARY KEY,
    ingredient_name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')

# Create table for customer flavor suggestions
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer_suggestions (
    id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    suggested_flavor TEXT NOT NULL
)
''')

# Create table for allergy concerns
cursor.execute('''
CREATE TABLE IF NOT EXISTS allergy_concerns (
    id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    allergy TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

def add_flavor(flavor_name, availability):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO seasonal_flavors (flavor_name, availability) VALUES (?, ?)', (flavor_name, availability))
    conn.commit()
    conn.close()

def add_ingredient(ingredient_name, quantity):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)', (ingredient_name, quantity))
    conn.commit()
    conn.close()

def add_suggestion(customer_name, suggested_flavor):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customer_suggestions (customer_name, suggested_flavor) VALUES (?, ?)', (customer_name, suggested_flavor))
    conn.commit()
    conn.close()

def add_allergy(customer_name, allergy):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO allergy_concerns (customer_name, allergy) VALUES (?, ?)', (customer_name, allergy))
    conn.commit()
    conn.close()

def main():
    while True:
        print("\nWelcome to the Chocolate House!")
        print("1. Add Seasonal Flavor")
        print("2. Add Ingredient")
        print("3. Add Customer Suggestion")
        print("4. Add Allergy Concern")
        print("5. Exit")
        print("6. Show Allergy")
        
        choice = input("Select an option: ")

        if choice == '1':
            flavor_name = input("Enter flavor name: ")
            availability = input("Enter availability: ")
            add_flavor(flavor_name, availability)
        elif choice == '2':
            ingredient_name = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            add_ingredient(ingredient_name, quantity)
        elif choice == '3':
            customer_name = input("Enter customer name: ")
            suggested_flavor = input("Enter suggested flavor: ")
            add_suggestion(customer_name, suggested_flavor)
        elif choice == '4':
            customer_name = input("Enter customer name: ")
            allergy = input("Enter allergy: ")
            add_allergy(customer_name, allergy)
        elif choice == '5':
            print("Goodbye!")
            break
        elif choice=='6':
            print(allergy)
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
