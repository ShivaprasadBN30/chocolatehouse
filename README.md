# chocolatehouse
Chocolate House Application

Welcome to the Chocolate House Application! This fun, easy-to-use Python app helps you manage everything about your chocolate shop, from seasonal flavors to customer suggestions and allergy tracking. It’s built with SQLite to keep all your data neatly organized and accessible.

What Can You Do With This App?

Add Seasonal Flavors: Easily update new chocolate flavors and their availability.

Manage Ingredient Inventory: Keep tabs on the ingredients you need.

Customer Suggestions: Let customers suggest new chocolate flavors.

Allergy Concerns: Record and manage customers' allergies for a safer experience.

User-Friendly Interface: Navigate smoothly with a simple command-line menu.


How the Database Works

The app sets up the following tables in SQLite to store everything:

1. seasonal_flavors

id: Unique ID

flavor_name: Name of the flavor

availability: Availability status



2. ingredient_inventory

id: Unique ID

ingredient_name: Ingredient name

quantity: Quantity on hand



3. customer_suggestions

id: Unique ID

customer_name: Customer’s name

suggested_flavor: Their flavor suggestion



4. allergy_concerns

id: Unique ID

customer_name: Customer’s name

allergy: Allergy info




Setting Up

To get started, you’ll need Python and SQLite. You can download Python from python.org.

1. Clone the repository:

git clone <repository-url>
cd chocolate_house


2. Run the application:

python chocolate_house.py



Using the App

When you launch the app, you’ll see a menu with options like:

1. Add Seasonal Flavor


2. Add Ingredient


3. Add Customer Suggestion


4. Add Allergy Concern


5. Exit


6. Show Allergy



Just enter the number of the action you want to take, and follow the prompts!

Contributing

Got ideas? Contributions are welcome! Feel free to submit a pull request if you have suggestions for improvement.

License

This project is open-source under the MIT License - check the LICENSE file for details.
