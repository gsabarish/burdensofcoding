from fastapi import APIRouter


router = APIRouter()


@router.get('/about')
def about():
    return {"Data": "About"}
