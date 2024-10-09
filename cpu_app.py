from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
import time
import os
from pprint import pformat

app = FastAPI()

class AppInput(BaseModel):
    text: str


@app.get("/ping")
def read_root():
    return {
        "val1": "hehehee",
        "val2": "ehhehea1",
        "val3": os.environ.get("TEST1_1"),
    }

## USEabcde

@app.post("/generate/")
def generate_response(input: AppInput):
    return "The input was: " + input.text

@app.get("/readiness")
def readiness_probe():
    return {"status": "ready"}

