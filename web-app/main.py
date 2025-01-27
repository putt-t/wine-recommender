from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

with open("static/form_data.json", "r") as f:
    form_data = json.load(f)

@app.get("/form-data")
async def get_form_data():
    return form_data