import cv2
import requests
import psycopg2
from flask import Flask, request, jsonify, render_template
from food import Food  # Assuming the Food class is defined elsewhere for structuring food data

app = Flask(__name__)

# Database Connection
def connect_to_db():
    return psycopg2.connect(
        dbname="macrotrak_db",  
        user="postgres",           
        password="password",    
        host="localhost",       
        port="5432"              
    )

# Insert food data into the database
def insert_food_item(cur, food):
    cur.execute("""
        INSERT INTO food_items (item_name, calories, fat, sat_fat, poly_fat, mono_fat, carbs, fiber, insol_fiber, sol_fiber, sugar, protein)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (food.get_item_name(), food.get_calories(), food.get_fat(), food.get_saturated_fat(), food.get_polyunsaturated_fat(),
          food.get_monounsaturated_fat(), food.get_carbs(), food.get_fiber(), food.get_insoluble_fiber(),
          food.get_soluble_fiber(), food.get_sugar(), food.get_protein()))

# Fetch food data from Open Food Facts API based on barcode
def fetch_food_data(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get("product", {})
        return data
    else:
        return None

# API endpoint for barcode scanning
@app.route('/scan_barcode', methods=['POST'])
def scan_barcode():
    barcode = request.json.get('barcode')
    food_data = fetch_food_data(barcode)
    if food_data:
        food = Food(
            food_data.get('product_name', 'Unknown'),
            food_data.get('nutriments', {}).get('energy-kcal_100g', 0),
            food_data.get('nutriments', {}).get('fat_100g', 0),
            food_data.get('nutriments', {}).get('saturated-fat_100g', 0),
            food_data.get('nutriments', {}).get('polyunsaturated-fat_100g', 0),
            food_data.get('nutriments', {}).get('monounsaturated-fat_100g', 0),
            food_data.get('nutriments', {}).get('carbohydrates_100g', 0),
            food_data.get('nutriments', {}).get('fiber_100g', 0),
            food_data.get('nutriments', {}).get('insoluble-fiber_100g', 0),
            food_data.get('nutriments', {}).get('soluble-fiber_100g', 0),
            food_data.get('nutriments', {}).get('sugars_100g', 0),
            food_data.get('nutriments', {}).get('proteins_100g', 0)
        )

        # Insert food item into the database
        conn = connect_to_db()
        cur = conn.cursor()
        insert_food_item(cur, food)
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({"message": "Food item added successfully!"}), 200
    else:
        return jsonify({"error": "Product not found."}), 404

# Route to render the barcode scanner HTML page
@app.route('/')
def index():
    return render_template('barcode-scanner.html')

# Barcode scanning using OpenCV
def scan_with_opencv():
    cap = cv2.VideoCapture(0)
    detector = cv2.barcode_BarcodeDetector()  # Barcode detector object
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Barcode Scanner", frame)

        # Barcode detection (using OpenCV)
        retval, decoded_info, _, _ = detector.detectAndDecodeMulti(frame)
        if retval:
            for barcode in decoded_info:
                barcode_data = barcode
                print(f"Detected Barcode: {barcode_data}")
                # Send this barcode to Flask API to fetch and store food data
                # You can use a POST request to your Flask /scan_barcode endpoint
                break  # Stop scanning after detecting the first barcode

        # Exit on ESC key
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    app.run(debug=True)