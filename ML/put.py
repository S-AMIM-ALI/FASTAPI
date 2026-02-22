from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Optional
import json
from fastapi.responses import JSONResponse
import os

app=FastAPI()

@app.get("/")
def root():
    return {"messages":" all about put"}
class student(BaseModel):
    st_id:Annotated[Optional[int],Field(default=0)]
    st_name:Annotated[Optional[str],Field(default=None)]
    gender:Annotated[Optional[str],Field(default=None)]
    grad:Annotated[Optional[str],Field(default=None)]
    weight:Annotated[Optional[float],Field(default=None,gt=0)]
    height:Annotated[Optional[float],Field(default=None,gt=0)]
    rollno:Annotated[Optional[int],Field(default=None,gt=0)]

def load_data():
    try:
        with open("student.json",'r') as f:
         return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("student.json",'w') as f:
        json.dump(data,f)

@app.put("/update/{st_id}")
def st_update(st_id:int,su:student):
    data=load_data()
    existing_st = next((item for item in data if item["st_id"] == st_id), None)

    updated_st=su.dict(exclude_unset=True)
    for key,value in updated_st.items():
        existing_st[key]=value
    #data[st_id]=existing_st
    save_data(data)
    raise HTTPException(status_code=200,detail='data updated successfully')

