from fastapi import APIRouter
import itemlist


router2 = APIRouter()


inventory = itemlist.data


@router2.get('/get-item/{item_id}')
def get_item(item_id):
    return inventory[item_id]

