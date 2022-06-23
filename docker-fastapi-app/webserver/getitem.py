from fastapi import APIRouter
import json
import pymongo  # package for working with MongoDB


router2 = APIRouter()


def connect_db():
    client = pymongo.MongoClient(host='db',
                                 port=27017,
                                 authSource="admin")
    db = client["test"]
    collection = db["test"]
    return db


@router2.get('/get-item/{item_id}')
def extract_db(item_id):
    db = connect_db()
    collection = db["test"]
    for extracts in collection.find({"name": item_id}):
        print(extracts["price"])
    return extracts["price"]






