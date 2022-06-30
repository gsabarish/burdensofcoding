import pymongo  # package for working with MongoDB

client = pymongo.MongoClient(host='test_mongodb',
                             port=27017,
                             username='admin',
                             password='password',
                             authSource="admin")
db = client["test"]
collection = db["test"]

post = {"_id": 1, "name": "Milk", "price": 4, "brand": "regular"}

collection.insert_one(post)




