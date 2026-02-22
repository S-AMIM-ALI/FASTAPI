from fastapi import  FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field
from typing import Annotated,Optional,Literal
from fastapi.responses import JSONResponse
import json
import pickle 
import pandas as pd
app=FastAPI()
with open('p2.pkl','rb') as f :
    model=pickle.load(f)
@app.get("/")
def home():
    return {"messages":"welcome ml project using fastapi"}
class UserInput(BaseModel):
    age:Annotated[int,Field(...,description='enter your age',gt=0)]
    gender:Literal['Male','Female']
    marital_status:Literal["Divorced", "Married", "Single"]
    annual_income:Annotated[int,Field(...,description='enter your income',gt=0)]
    loan_amount:Annotated[int,Field(...,description='enter your loan amount',gt=0)]
    credit_score:Annotated[int,Field(...,description='enter your score',gt=0)]
    num_dependents:Annotated[int,Field(...,description='enter your num_dependents',gt=0)]
    existing_loans_count:Annotated[int,Field(...,description='enter your age',gt=0)]
    employment_status:Literal['Unemployed', 'Employed', 'Self-employed']
@app.post("/predict")
def pred(data:UserInput):
    input_df = pd.DataFrame([{
        "age": data.age,
        "gender": data.gender,
        "marital_status": data.marital_status,
        "annual_income": data.annual_income,
        "loan_amount": data.loan_amount,
        "credit_score": data.credit_score,
        "num_dependents": data.num_dependents,
        "existing_loans_count": data.existing_loans_count,
        "employment_status": data.employment_status
    }])
    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1])

    result = "Approved" if prediction == 1 else "Rejected"

    return {
        "prediction_result": result,
        "approval_probability": round(probability * 100, 2)
    }


