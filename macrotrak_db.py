import psycopg2

conn = psycopg2.connect(
    dbname="macrotrak_db",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT CURRENT_DATE;")

curr_date = cur.fetchone()
print("current date: ", curr_date) 

# Create table query
cur.execute("""
    DROP TABLE IF EXISTS food_items;

CREATE TABLE food_items (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(255),
    calories INT NOT NULL,
    fat FLOAT NOT NULL,
    sat_fat FLOAT NOT NULL,
    poly_fat FLOAT NOT NULL,
    mono_fat FLOAT NOT NULL,
    carbs FLOAT NOT NULL,
    fiber FLOAT NOT NULL,
    insol_fiber FLOAT NOT NULL,
    sol_fiber FLOAT NOT NULL,
    sugar FLOAT NOT NULL,
    protein FLOAT NOT NULL);
""")
# Commit the changes (save them to the database)
conn.commit()
# Print success message
print("Table 'food_items' created successfully.")


# Insert data into the 'food_items' table
# cur.execute("""
#     INSERT INTO food_items (calories, fat, sat_fat, poly_fat, mono_fat, carbs, fiber, insol_fiber, sol_fiber, sugar, protein)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
# """, (250, 15, 5, 4, 6, 30, 5, 3, 2, 10, 5))
# Commit the transaction (save changes)
# conn.commit()
# # Print success message
# print("Data inserted into 'food_items' table.")

cur.close()
conn.close()