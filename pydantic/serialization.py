from pydantic import BaseModel

class Address(BaseModel):
    vill:str
    teh:str
    city:str
    state:str
    pincode:int




class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict={'vill':'palla','teh':"nuh",'city':'nuh','state':'HR','pincode':122107}
add=Address(**address_dict)
patient_dict={'name':'ali','gender':'male','age':22,'address':address_dict}
patient=Patient(**patient_dict)
print(patient)
print(patient.address.vill)
print(patient.address.state)
print(patient.address.pincode)

temp=patient.model_dump()
print(temp)

print(patient.model_dump_json())

print(patient.model_dump(include=['name','age']))
print(patient.model_dump(exclude=['name']))