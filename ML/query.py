from fastapi import FastAPI,Query,HTTPException,Path
import json
app=FastAPI()

with open("student.json",'r') as f:
    data=json.load(f)

@app.get('/')
def root():
    return {'message':"it is introdctry part of Query"}
@app.get('/data/')
def get_data(name:str=Query(None,title='Name',description='enter name of candidate',
             min_length=3,max_length=100,examples='abc',pattern='^[a-zA-Z ]+$')):
 for item in data:
        if item['st_id']==id  or item['st_name'].lower()==name.lower():
            return item
 raise HTTPException(status_code=404,detail='data doesnt exist')

