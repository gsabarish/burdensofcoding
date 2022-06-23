from fastapi import APIRouter


router1 = APIRouter()


@router1.get('/about')
def about():
    return {"Data": "About"}
