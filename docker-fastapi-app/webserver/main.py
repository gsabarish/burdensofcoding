from fastapi import FastAPI
from about import router1
from getitem import router2


app = FastAPI()
app.include_router(router1)
app.include_router(router2)


@app.get('/')
def index():
    return "Hello"

