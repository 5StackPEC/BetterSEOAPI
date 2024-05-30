from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
import os
from typing import Annotated
import controllers.model
import utils.setup


app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

utils.setup.run_setup()

# Load model right away
model = controllers.model.Model()


@app.get("/")
async def root():
    return {"message": "Welcome to Better SEO API!"}


@app.get("/score_dummy")
async def score_dummy():
    return {"message": 100}


@app.post("/score")
async def get_score(file: UploadFile):
    try:
        input_image = await model.get_preprocess_image(file)
        predicted_score = model.predict(input_image)
        return {"SEOScore": predicted_score}
    except Exception as e:
        print(e)
        return {"message": "Internal server"}
