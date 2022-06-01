from fastapi import APIRouter
import json


router2 = APIRouter()


a_file = open("data.json", "r")
json_object = json.load(a_file)
a_file.close()


@router2.get('/get-item/{item_id}')
def get_item(item_id):
    if item_id not in json_object:
        return{"Error": "Item ID does not exists."}

    return json_object[item_id]


