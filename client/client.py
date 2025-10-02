import requests
import random
import json
import time

# Example of fake WhatsApp data
def generate_fake_whatsapp_data():
    return {
        "name": "John Doe",
        "last_seen": "Yesterday",
        "status": "Feeling lucky!",
        "contacts": ["Alice", "Bob", "Charlie"],
        "messages": [
            {"from": "Alice", "message": "Hey, how are you?"},
            {"from": "Bob", "message": "Let's catch up soon!"}
        ]
    }

# Example of fake photos (just URLs in this case)
def generate_fake_photos():
    return ["http://fakephotos.com/photo1.jpg", "http://fakephotos.com/photo2.jpg"]

# Example of fake location
def generate_fake_location():
    return {"latitude": random.uniform(-90, 90), "longitude": random.uniform(-180, 180)}

# Example of fake IMEI
def generate_fake_imei():
    return f"35{random.randint(100000000000000, 999999999999999)}"

# Server endpoint where data will be sent
server_url = "http://127.0.0.1:5000/api/connect"
print("Connecting to:", server_url)


while True:
    imei = generate_fake_imei()
    location = generate_fake_location()
    whatsapp_data = generate_fake_whatsapp_data()
    photos = generate_fake_photos()

    data = {
        "imei": imei,
        "location": location,
        "whatsapp_data": whatsapp_data,
        "photos": photos
    }

    # Send fake data to the server
    response = requests.post(server_url, json=data)
    print("Server Response:", response.json())

    # Wait before sending the next request (simulating time interval)
    time.sleep(random.randint(5, 15))  # Random time interval
    