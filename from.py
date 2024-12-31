from flask import Flask, render_template, request
import pickle
import numpy as np

# Mapping of airport cities in India
airport_city_mapping = {
    "Delhi": 1,
    "Mumbai": 2,
    "Bangalore": 3,
    "Chennai": 4,
    "Kolkata": 5,
    "Hyderabad": 6,
    "Ahmedabad": 7,
    "Pune": 8,
    "Jaipur": 9,
    "Goa": 10,
    "Lucknow": 11,
    "Cochin": 12,
    "Kochi": 13,
    "Chandigarh": 14,
    "Indore": 15,
    "Nagpur": 16,
    "Visakhapatnam": 17,
    "Vadodara": 18,
    "Surat": 19,
    "Dehradun": 20,
    "Mangaluru": 21,
    "Ranchi": 22,
    "Agra": 23,
    "Varanasi": 24,
    "Bhopal": 25,
    "Patna": 26,
    "Nashik": 27,
    "Coimbatore": 28,
    "Aurangabad": 29,
    "Raipur": 30,
    "Amritsar": 31,
    "Jammu": 32,
    "Srinagar": 33,
    "Udaipur": 34,
    "Jodhpur": 35,
    "Ludhiana": 36,
    "Kota": 37,
    "Tirupati": 38,
    "Madurai": 39,
    "Bhubaneswar": 40,
    "Guwahati": 41,
    "Imphal": 42,
    "Agartala": 43,
    "Silchar": 44,
    "Aizawl": 45,
    "Dibrugarh": 46,
    "Tezpur": 47,
    "Kozhikode": 48,
    "Vijayawada": 49,
    "Tiruchirappalli": 50,
    "Puducherry": 51,
    "Shillong": 52,
    "Port Blair": 53,
    "Dimapur": 54,
    "Jorhat": 55,
    "Dibrugarh": 56,
    "Gwalior": 57,
    "Bhopal": 58,
    "Jhansi": 59,
    "Jabalpur": 60,
    "Sagar": 61,
    "Hindon": 62,
    "Mysuru": 63,
    "Kozhikode": 64,
    "Salem": 65,
    "Dharamsala": 66,
    "Kullu": 67,
    "Shimla": 68,
    "Hampi": 69,
    "Belgaum": 70,
    "Gulbarga": 71,
    "Kolar": 72,
    "Bardhaman": 73,
    "Malda": 74,
    "Hooghly": 75,
    "Durgapur": 76,
    "Asansol": 77,
    "Nadia": 78,
    "Siliguri": 79,
    "Bardhaman": 80,
    "Kalyani": 81,
    "Murshidabad": 82,
    "Jalpaiguri": 83,
    "Alipurduar": 84,
    "Cooch Behar": 85,
    "Darjeeling": 86,
    "Kangra": 87,
    "Sikkim": 88,
    "Dharamshala": 89,
    "Gulbarga": 90,
    "Latur": 91,
    "Osmanabad": 92,
    "Yavatmal": 93,
    "Wardha": 94,
    "Akola": 95,
    "Amravati": 96,
    "Nagapuri": 97,
    "Jalna": 98,
    "Ahmednagar": 99,
    "Ratnagiri": 100
}

app = Flask(__name__)

# Load the trained model
with open('E:\\fpp_project\\ET_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    cities = list(airport_city_mapping.keys())
    return render_template('index.html', cities=cities)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        source = request.form['source']
        destination = request.form['destination']
        departure_date = request.form['departure_date']
        arrival_date = request.form['arrival_date']
        number_of_passengers = int(request.form['number_of_passengers'])
        
        # Prepare the input for the model
        features = np.zeros(12)  # Adjust the size based on your model
        
        # Map source and destination cities to numerical values
        features[0] = airport_city_mapping[source]  # Source city
        features[1] = airport_city_mapping[destination]  # Destination city
        
        # Example of encoding other features
        features[2] = (number_of_passengers)  # Passengers
        
        # Further features can be added based on your model
        # For simplicity, here we're only showing how to handle basic inputs
        
        # Make prediction
        prediction = model.predict([features])
        
        # Return prediction result
        return f"Predicted Price: {prediction[0]}"
    
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
