from fastapi import FastAPI
from app.routes.category_routes import router as category_routes

app = FastAPI()
@app.get('/hello')
def hello():
    return "Hello!!!"

app.include_router(category_routes)