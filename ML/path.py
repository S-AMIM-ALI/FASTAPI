from fastapi import FastAPI,Path,HTTPException
import json
app=FastAPI()

with open("student.json",'r') as f:
    data= json.load(f)

@app.get('/')
def root():
    return {'message':'this is Path ...'}
@app.get("/student")
def student():
    return data
@app.get("/student/id/{id}")
def st_by(id:int=Path(...,title='ID',description='enter your valid ids',gt=0,lt=100)):
    for item in data:
        if item['st_id']==id:
            return item
    raise HTTPException(status_code=404,detail='doesnt exist')
@app.get("/student/Name/{name}")
def st_name(name:str=Path(...,title='Name',description='enter name',min_length=2,max_length=20,pattern='^[a-zA-Z ]{2,20}$')):
    for item in data:
        if item['st_name'].lower()==name.lower():
            return item
    raise HTTPException(status_code=404,detail='name doesnt exist')


    
