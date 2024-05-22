from pymongo import MongoClient

def setup_mongodb():
    client = MongoClient('localhost', 27017)
    db = client['smartcitynet']
    users = db['users']
    devices = db['devices']
    network_data = db['network_data']

    users.insert_one({"name": "Admin", "role": "admin"})
    devices.insert_one({"device_id": "001", "type": "sensor", "status": "active"})
    network_data.insert_one({"timestamp": "2024-05-21T00:00:00Z", "data": "initial data"})

    print("MongoDB setup complete with initial data.")

if __name__ == '__main__':
    setup_mongodb()
