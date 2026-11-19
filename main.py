from fastapi import FastAPI, Request
from data import users
from dtos import User


app = FastAPI()


    

@app.get("/")
def home():
    return users

#Create 
@app.post("/add-user")
def add_user(user:User):
    user = user.model_dump()
    users.append(user)
    
    return {
        "message": "User added successfully",
        "data": users
    }
    
#Read 
@app.get("/user/{id}")
def get_user(id:int):
    for user in users:
        if user.get("id") == id:
            return user
    
    return {
        "error":"The user not found"
    }
    
    
#Update  
@app.put("/update/{id}")
def update_user(id:int, data:User):
    for ind, ur in enumerate(users):
        if ur.get("id") == id:
            users[ind] = data
            return {
                        "status": "User updated Successfully",
                        "data":data
                    }
    return {
        "Status": "User Not Found"
    }
        
#Delete      
@app.delete("/delete/{id}")
def delete_user(id:int):
    for ind, user in enumerate(users):
        if user.get("id") == id:
            del_user = users.pop(ind)
            
            return {
                        "status": "User deleted Successfully",
                        "data":del_user
                    }
    return {
        "Status": "User Not Found"
    }
    
#  #for limited query param   
# @app.get("/greet")
# def greet(name:str):
#     return {
#         "message": f"hello {name}, how are you?"
#     }
    
    
# #for many query params
# @app.get("/data")
# def data(request:Request):
#     query_params = dict(request.query_params)
    
#     return f"hello {query_params.get("name")}, your age is {query_params.get("age")}"

