from migrations import Todo
from fastapi import HTTPException

def index(session):
    todos = session.query(Todo).all()
    return {
        "message": "success",
        "data" : todos
    }

def store(todo, session):
    if not todo.job == "":
        todo = Todo(job=todo.job)
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {
            "message": "success",
            "data" : todo
        }
    raise HTTPException(status_code=400, detail="job required")

def show(id, session):
    todo = session.query(Todo).get(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not Found")
    return {
        "message": "success",
        "data": todo
    }

def update(id, newTodo, session):
    todo = session.query(Todo).get(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not Found")
    todo.job = newTodo.job
    session.commit()
    return {
        "message": "success",
        "data": todo
    }

def delete(id, session):
    todo = session.query(Todo).get(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not Found")
    session.delete(todo)
    session.commit()
    session.close()
    return {
        "message": "success",
        "data": ""
    }