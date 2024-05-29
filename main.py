from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from pathlib import Path
import shutil
import os
from typing import Annotated



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
    root_path = os.getcwd()
    try:
        file_path = f"{root_path}/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
            return {"message":  "Filed saved successfully"}
        return {"message": file_path}
    except Exception as e:
        return {"message": "Internal server error"}
