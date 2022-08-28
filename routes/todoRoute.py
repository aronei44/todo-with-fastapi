from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from ses import get_session
from migrations.todo import Todo
from controllers import todoController
from models.todo import Todo as TodoModel

router = APIRouter()

@router.get('/', status_code=200)
async def getAllTodo(session: Session = Depends(get_session)):
    return todoController.index(session)

@router.post("/", status_code=201)
async def createTodo(todo : TodoModel, session: Session = Depends(get_session)):
    return todoController.store(todo, session)

@router.get("/{id}", status_code=200)
async def getTodoById(id: int, session : Session = Depends(get_session)):
    return todoController.show(id, session)

@router.put("/{id}", status_code=200)
async def updateTodoById(id: int, todo : TodoModel, session : Session = Depends(get_session)):
    return todoController.update(id, todo, session)

@router.delete("/{id}", status_code=200)
async def deleteTodoById(id: int, session : Session = Depends(get_session)):
    return todoController.delete(id, session)