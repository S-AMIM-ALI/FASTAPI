from fastapi import FastAPI,HTTPException,Query,Path
import json
import os
app=FastAPI()

@app.get("/")
def home():
    return {"welcome to day2"}
with open("student.json",'r') as f:
      data=json.load(f)
@app.get("/student/name/{st_name}")
def get_data_by_name(name:str=Query(...,description='name of student',max_length=100)):
    result=[a for a in data if a['st_name'].lower()==name.lower()]
    if not result:
        HTTPException(status_code=404,detail='not found')
    
    return result
