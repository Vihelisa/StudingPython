from fastapi import FastAPI
import test_routes

app = FastAPI()

def start_app():
    app.include_router(test_routes.router)