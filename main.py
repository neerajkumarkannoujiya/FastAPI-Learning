from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI(title="This is a FastAPI Project")


class Task(BaseModel):
    id: int
    name: str
    status: bool = False


class ResponseModel(BaseModel):
    id: int
    name: str


todos = []


@app.get("/")
def home():
    return "Hello Neeraj"


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# Create
@app.post("/add-todos", status_code=status.HTTP_201_CREATED)
def add_todos(task: Task):
    todos.append(task.model_dump())
    return {
        "message": "Todo Added Successfully",
        "Todos": todos
    }


# Read
@app.get("/todo/{id}")
def get_todo(id: int):
    for todo in todos:
        if todo.get("id") == id:
            return todo
        
    raise HTTPException(
        status_code=404,
        detail="User Not Founding"
    )


# Response Model technique
@app.get("/todos", response_model=ResponseModel)
def get_todos():
    return {
        "message": "The Todos are",
        "id": 22,
        "name": "Neeraj",
        "age": 77
    }


# Update
@app.put("/update/{id}")
def update_todo(id: int, task: Task):
    for idx, todo in enumerate(todos):
        if todo.get("id") == id:
            todos[idx] = task
            return task
    return {
        "message": "User Not Found!!"
    }


# Delete
@app.delete("/delete/{id}")
def delete_todos(id: int):
    for idx, todo in enumerate(todos):
        if todo.get("id") == id:
            todos.pop(idx)
            break
    return {
        "message": "The Todos are",
        "todos": todos
    }
