from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from fastapi import FastAPI, File, UploadFile

from uvicorn import run

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


@app.get("/")
async def root():
    return {"message": "Welcome to Better SEO API!"}


@app.post("/score")
async def get_score(file: Annotated[bytes, File()]):
    print(type(file))
    return {"file_size": len(file)}

@app.post("/score_alt")
async def get_score_alt(file: UploadFile):
    
    return {"Uploaded filename": file.filename}
