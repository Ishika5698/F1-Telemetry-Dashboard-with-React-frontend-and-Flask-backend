from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

def generate_telemetry_batch():
    return {
        'speed': random.randint(200, 300),
        'rpm': random.randint(8000, 12000),
        'throttle': random.randint(0, 100),
        'brake': random.randint(0, 100),
        'gear': random.randint(1, 8),
        'tire_wear': random.randint(10, 100),  # New: 100% = fresh, 10% = worn
        'batch_size': 10000,
        'latency': 0.01
    }

@app.route('/telemetry')
def get_telemetry():
    start_time = time.time()
    data = generate_telemetry_batch()
    data['latency'] = (time.time() - start_time) * 1000
    return jsonify(data)

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': jsonify(generate_telemetry_batch())
    }

if __name__ == '__main__':
    app.run(port=5001)