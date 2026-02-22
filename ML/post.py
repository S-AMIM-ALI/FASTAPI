from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field,computed_field
import json
from fastapi.responses import JSONResponse
from typing import Annotated
import os

app=FastAPI()
@app.get("/")
def root():
    return {"message":"its all about post"}
class Patient(BaseModel):
    id:int=Field(...,description="enter your id")
    name:str=Field(...,description="enter patient name",max_length=50)
    disease:str=Field(...,description="enter your disease")
    height_cm:float=Field(...,description="enter your age",gt=0)
    weight_kg:float=Field(...,description="enter your weight",gt=0)

    @computed_field
    @property
    def bmi(self)->float:
        height_m=self.height_cm/100
        return round((self.weight_kg/(height_m**2)),2)
def save_data(data):
    with open("data.json",'w') as f:
        json.dump(data,f)
def load_data():
    try:
        with open("data.json",'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
@app.post("/create")
def create_patient(patient:Patient):
    data=load_data()

    if 'serial' not in data:
        data['serial']=[]
    if any(p['id']==patient.id for p in data['serial']):
        raise HTTPException(status_code=400,detail='id already exists')
    data['serial'].append(patient.model_dump())
    save_data(data)
    raise HTTPException(status_code=200,detail='data successfully created')

