from fastapi import FastAPI
from backend.controllers.recipe import router as recipe_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"] ,
)

app.include_router(recipe_router)

@app.get("/")
def read_root():
    return {"message": "Recipe App Backend is running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
