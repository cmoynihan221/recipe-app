from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.db.db import SessionLocal
from backend.models.recipe import Recipe, Tag
from backend.schemas.recipe import RecipeSchema, RecipeCreate, TagSchema
from typing import List, Optional

router = APIRouter(prefix="/recipes", tags=["recipes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[RecipeSchema])
def list_recipes(skip: int = 0, limit: int = 20, search: Optional[str] = None, db: Session = Depends(get_db)):
    q = db.query(Recipe)
    if search:
        q = q.filter(Recipe.title.ilike(f"%{search}%"))
    return q.offset(skip).limit(limit).all()

@router.get("/{recipe_id}", response_model=RecipeSchema)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


