from fastapi import FastAPI
import json
import os

app=FastAPI()
@app.get("/")
def root():
    return {'message':"day1 basics of fastapi"}

with open("student.json",'r') as f:
    data=json.load(f)
@app.get("/student")
def st_data():
    return data
@app.get("/student/{idnum}")
def get_st_by_id(idnum:int):
    for item in data:
        if item['st_id']==idnum:
            return item
        return HTTPException(status_code=404,detail="doesnt found")