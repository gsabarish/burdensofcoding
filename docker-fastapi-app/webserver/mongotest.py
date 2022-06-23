import pymongo  # package for working with MongoDB


def connect_db():
    client = pymongo.MongoClient(host='db',
                                 port=27017,
                                 authSource="admin")
    db = client["test"]
    collection = db["test"]
    return db


def extract_db():
    db = connect_db()
    collection = db["test"]
    for extracts in collection.find({"name": "Milk"}):
        print(extracts["name"])
    return extracts["name"]


if __name__ == "__main__":
    extract_db()
