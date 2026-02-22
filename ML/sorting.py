from fastapi import FastAPI,Path,Query,HTTPException
import json
app=FastAPI()
with open('student.json','r') as f:
    data=json.load(f)
@app.get('/')
def root():
    return {'message':"sorting and ordering concept"}
@app.get('/sorting')
def sorting(sort_by:str=Query('st_id',description='field to sort'),
            order:str=Query('asc',description='asc/desc',pattern="^(asc|desc)$")

    ):

  valid_field=['st_id','st_name','height','weight','rollno']
  if sort_by not in valid_field:
        raise HTTPException(status_code=400,detail='enter valid fields')
  reverse = True if order == "desc" else False

  sorted_data=sorted(data,key=lambda x:x[sort_by],reverse=reverse)
  return sorted_data 

# /sorting
# /sorting?sort_by=st_name
# /sorting?sort_by=weight&order=desc
# /sorting?sort_by=rollno&order=asc
