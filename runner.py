from food import Food
import psycopg2

def connect_to_db():
    """Function to connect to the PostgreSQL database."""
    return psycopg2.connect(
        dbname="macrotrak_db",   # Your database name
        user="postgres",            # Your database username
        password="password",     # Your database password
        host="localhost",        # Use localhost for local PostgreSQL server
        port="5432"              # Default PostgreSQL port
    )

def insert_food_item(cur, food):
    """Function to insert a food item into the database using the Food object."""
    cur.execute("""
        INSERT INTO food_items (item_name, calories, fat, sat_fat, poly_fat, mono_fat, carbs, fiber, insol_fiber, sol_fiber, sugar, protein)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (food.get_item_name(), food.get_calories(), food.get_fat(), food.get_saturated_fat(), food.get_polyunsaturated_fat(),
          food.get_monounsaturated_fat(), food.get_carbs(), food.get_fiber(), food.get_insoluble_fiber(),
          food.get_soluble_fiber(), food.get_sugar(), food.get_protein()))

def get_food_input():
    """Function to get food details from the user and return as a Food object."""
    print("\nEnter the food details:")
    item_name = input("Food Item Name: ")  # Ask for the food name
    calories = int(input("Calories: "))
    fat = float(input("Fat (grams): "))
    sat_fat = float(input("Saturated Fat (grams): "))
    poly_fat = float(input("Polyunsaturated Fat (grams): "))
    mono_fat = float(input("Monounsaturated Fat (grams): "))
    carbs = float(input("Carbohydrates (grams): "))
    fiber = float(input("Fiber (grams): "))
    insol_fiber = float(input("Insoluble Fiber (grams): "))
    sol_fiber = float(input("Soluble Fiber (grams): "))
    sugar = float(input("Sugar (grams): "))
    protein = float(input("Protein (grams): "))

    # Create a Food object with the user input
    food = Food(item_name, calories, fat, sat_fat, poly_fat, mono_fat, carbs, fiber, insol_fiber, sol_fiber, sugar, protein)
    return food

def runner():
    """Function to repeatedly ask for user input and insert the food data into the database."""
    conn = connect_to_db()  # Connect to the database
    cur = conn.cursor()  # Create a cursor to interact with the database
    
    while True:
        # Get food details from the user and create a Food object
        food = get_food_input()
        
        # Insert the food item into the database
        insert_food_item(cur, food)
        
        # Commit the transaction (save changes)
        conn.commit()
        print("\nFood item added successfully!\n")
        
        # Ask if the user wants to add another food item
        another = input("Do you want to add another food item? (y/n): ")
        if another.lower() != 'y':
            break  # Exit the loop if the user doesn't want to add more items

    # Close the cursor and connection
    cur.close()
    conn.close()
    print("\nExiting...")

if __name__ == "__main__":
    runner()