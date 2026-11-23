from fastapi import FastAPI

app = FastAPI()

@app.get("/shipment")   
def get_shipment():
    return {'product':'keyboard','status':'shipped'}

@app.get("/")   
def shipment():
    return {'welcome to shipment app'}

