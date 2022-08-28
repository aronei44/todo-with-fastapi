import imp
from fastapi import FastAPI 
from migrations.main import Base, engine
from routes import todoRoute

Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
async def main():
    return "home"

app.include_router(todoRoute.router, prefix="/todo", tags=["Todo Feature"])