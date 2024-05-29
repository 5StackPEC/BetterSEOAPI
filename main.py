from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/score")
def get_lighthouse_score():
    return {"LighthouseScore": 100}
