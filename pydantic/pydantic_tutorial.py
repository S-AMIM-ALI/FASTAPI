from pydantic import Field,BaseModel,EmailStr,AnyUrl
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str=Field(min_length=3,max_length=100,pattern='^[a-zA-Z ]+$')
    age:int=Field(gt=0,lt=150)
    weight:float=Field(gt=0,description='weight should be in kg')
    height:float=Field(gt=0,description='height should be meters')
    link:AnyUrl
    email:EmailStr
    contact:Dict[str,int]
def insert(p:Patient):
    print(p.name,
    p.age,p.weight,p.height,p.link,p.email,p.contact)
    
patient_info={'name':'ali','age':34,'weight':58,'height':1.7,
'link':"https://www.youtube.com/watch?v=sw8V7mLl3OI&list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ&index=6",
'email':'abc@gmail.com' ,
'contact':{'name':8395523859}
  
  }
p=Patient(**patient_info)
insert(p)