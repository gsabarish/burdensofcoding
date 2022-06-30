from fastapi import APIRouter
import pymongo  # package for working with MongoDB
import redis
import json
import sys


router2 = APIRouter()


def connect_db():
    client_db = pymongo.MongoClient(host='db',
                                    port=27017,
                                    authSource="admin")
    db = client_db["test"]
    collection = db["test"]
    return db


client_db_connect = connect_db()


def redis_connect():
    try:
        client_redis = redis.Redis(
            host="cache",
            port=6379
        )
        ping = client_redis.ping()
        if ping is True:
            return client_redis
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)


client_redis_connect = redis_connect()


def get_from_cache(key: str) -> str:
    val = client_redis_connect.get(key)
    return val


def set_from_cache(key: str, value: str) -> bool:
    state = client_redis_connect.setex(key, 4, value)
    return state


def get_from_db(item_name: str) -> dict:
    collection = client_db_connect["test"]
    for extracts in collection.find({"name": item_name}):
        print(extracts["price"])
    return extracts["price"]


def optimal_route(item_name: str) -> dict:

    data = get_from_cache(item_name)

    if data is not None:
        dict1 = {item_name: data.decode('utf-8')}
        dict2 = {"Cache": "True"}
        return dict1, dict2

    else:
        data = get_from_db(item_name)
        if data:
            data = json.dumps(data)
            dict1 = {item_name: data}
            dict2 = {"Cache": "False"}
            set_from_cache(item_name, data)
            return dict1, dict2


@router2.get('/get-item-price/{item_name}')
def extract_db(item_name: str) -> dict:
    return optimal_route(item_name)









