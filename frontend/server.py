from flask import Flask, jsonify
import datetime
import random

app = Flask(__name__)

@app.route('/data')
def get_data():
    return jsonify({
        'temperature': random.uniform(-10, 40),  # Temperature in °C
        'pressure': random.uniform(90, 110),     # Pressure in kPa
        'altitude': random.uniform(0, 1000),     # Altitude in meters
        'velocity': random.uniform(0, 50)        # Velocity in m/s
    })

@app.route('/telemetry')
def get_telemetry():
    return jsonify({
        'gnssTime': datetime.now().strftime('%H:%M:%S'),  # Current time
        'latitude': round(random.uniform(-90, 90), 6),    # Latitude
        'longitude': round(random.uniform(-180, 180), 6), # Longitude
        'altitude': round(random.uniform(0, 1000), 1),    # Altitude in meters
        'voltage': round(random.uniform(3.5, 5.0), 1),    # Voltage in volts
        'temperature': round(random.uniform(-10, 40), 1), # Temperature in °C
        'humidity': round(random.uniform(0, 100), 1),     # Humidity in %
        'pressure': round(random.uniform(90, 110), 1),    # Pressure in kPa
        'velocity': round(random.uniform(0, 50), 1),      # Velocity in m/s
        'gyroX': round(random.uniform(-1, 1), 2),         # Gyroscope X
        'gyroY': round(random.uniform(-1, 1), 2),         # Gyroscope Y
        'gyroZ': round(random.uniform(-1, 1), 2),         # Gyroscope Z
        'accelX': round(random.uniform(-1, 1), 2),        # Accelerometer X
        'accelY': round(random.uniform(-1, 1), 2),        # Accelerometer Y
        'accelZ': round(random.uniform(-1, 1), 2),        # Accelerometer Z
        'magX': round(random.uniform(-1, 1), 2),          # Magnetometer X
        'magY': round(random.uniform(-1, 1), 2),          # Magnetometer Y
        'magZ': round(random.uniform(-1, 1), 2),          # Magnetometer Z
        'velocityX': round(random.uniform(-1, 1), 2),     # Velocity X
        'velocityY': round(random.uniform(-1, 1), 2),     # Velocity Y
        'velocityZ': round(random.uniform(-1, 1), 2),     # Velocity Z
        'velocityTotal': round(random.uniform(0, 50), 1), # Total Velocity
        'logs': f"{random.randint(1000, 9999)}, {datetime.now().strftime('%H:%M:%S')}, {random.randint(100, 999)}, FLIGHT, DESCENT, {round(random.uniform(800, 900), 1)}, {round(random.uniform(20, 30), 1)}, {round(random.uniform(90, 100), 1)}, {round(random.uniform(4, 5), 1)}, {round(random.uniform(0, 1), 2)}, {round(random.uniform(0, 1), 2)}, {round(random.uniform(0, 1), 2)}, {round(random.uniform(0, 1), 2)}, {round(random.uniform(0, 1), 2)}, {round(random.uniform(0, 1), 2)}, {round(random.uniform(0, 1), 2)}, {round(random.uniform(0, 1), 2)}, {round(random.uniform(0, 1), 2)}, {round(random.uniform(0, 1), 2)}, {datetime.now().strftime('%H:%M:%S')}, {round(random.uniform(800, 900), 1)}, {round(random.uniform(-90, 90), 6)}, {round(random.uniform(-180, 180), 6)}, {random.randint(0, 10)}, RESET_CMD"
    })


@app.route('/map-data')
def get_map_data():
    return jsonify({
        'latitude': round(random.uniform(-90, 90), 6),    # Latitude
        'longitude': round(random.uniform(-180, 180), 6)  # Longitude
    })

if __name__ == '__main__':
    app.run(debug=True)