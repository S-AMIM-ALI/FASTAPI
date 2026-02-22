from fastapi import FastAPI
app=FastAPI()
import pickle


@app.get("/")
def root():
    return {"ml progrom"}


with open("p2.pkl",'rb') as f:
    model=pickle.load(f)