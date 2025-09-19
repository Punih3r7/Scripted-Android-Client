import requests
from faker import Faker
import random

# Initialize faker
fake = Faker()

# Function to generate a fake 15-digit IMEI
def generate_imei():
    return "".join([str(random.randint(0, 9)) for _ in range(15)])

# Fake device data
device_data = {
    "device_id": fake.uuid4(),
    "user": fake.user_name(),
    "location": fake.city(),
    "imei": generate_imei()
}

print("[*] Generated fake device data:")
print(device_data)

# Send data to the collector API (server must be running on port 5000)
try:
    response = requests.post("http://server:5000/collect", json=device_data)
    print("[+] Response from server:", response.text)
except Exception as e:
    print("[-] Error sending data:", e)
