from fastapi import FastAPI
from about import router


app = FastAPI()
app.include_router(router)


@app.get('/')
def index():
    return "Hello"

