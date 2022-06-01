from fastapi import APIRouter
import json


router2 = APIRouter()


a_file = open("data.json", "r")
json_object = json.load(a_file)
a_file.close()


@router2.get('/get-item/{item_id}')
def get_item(item_id):
    return json_object[item_id]


