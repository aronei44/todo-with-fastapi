import imp
from fastapi import FastAPI 
from migrations.main import Base, engine
from routes import todoRoute
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def main():
    return "home"

app.include_router(todoRoute.router, prefix="/todo", tags=["Todo Feature"])