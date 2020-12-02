from typing import Optional

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from src.controllers import register_view, session_manager_view

app = FastAPI()

app.mount("/static", StaticFiles(directory="./src/static"), name="static")

app.include_router(register_view, prefix='/register')
app.include_router(session_manager_view)

