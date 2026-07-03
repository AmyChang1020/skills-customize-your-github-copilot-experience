from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

class TodoIn(BaseModel):
    title: str = Field(..., min_length=1)
    completed: bool = False

class Todo(TodoIn):
    id: int

todos: List[Todo] = []
_next_id = 1

@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: TodoIn):
    global _next_id
    item = Todo(id=_next_id, **todo.dict())
    _next_id += 1
    todos.append(item)
    return item

@app.get("/todos", response_model=List[Todo])
def list_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for t in todos:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoIn):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            updated = Todo(id=todo_id, **todo.dict())
            todos[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(i)
            return
    raise HTTPException(status_code=404, detail="Todo not found")
