from fastapi import FastAPI
from backend.controllers.recipe import router as recipe_router

app = FastAPI()

app.include_router(recipe_router)

@app.get("/")
def read_root():
    return {"message": "Recipe App Backend is running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
