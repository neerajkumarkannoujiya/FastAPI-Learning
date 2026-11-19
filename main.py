from fastapi import FastAPI, Request
from data import products


app = FastAPI()

@app.get("/")
def home():
    return products



@app.get("/product/{prod_id}")
def get_products(prod_id:int):
    for pr in products:
        if pr.get("id") == prod_id:
            return pr
    
    return {
        "error":"The product not found"
    }
    
    
 #for limited query param   
@app.get("/greet")
def greet(name:str):
    return {
        "message": f"hello {name}, how are you?"
    }
    
    
#for many query params
@app.get("/data")
def data(request:Request):
    query_params = dict(request.query_params)
    
    return f"hello {query_params.get("name")}, your age is {query_params.get("age")}"