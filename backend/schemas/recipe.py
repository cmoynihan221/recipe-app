from pydantic import BaseModel
from typing import List, Optional

from pydantic import Field

class TagSchema(BaseModel):
    id: int = Field(..., description="Unique identifier for the tag")
    name: str = Field(..., description="Name of the tag")
    class Config:
        orm_mode = True

class RecipeSchema(BaseModel):
    id: int = Field(..., description="Unique identifier for the recipe")
    title: str = Field(..., description="Title of the recipe")
    description: Optional[str] = Field(None, description="Description of the recipe")
    file_path: Optional[str] = Field(None, description="Path to the markdown file for the recipe")
    content: Optional[str] = Field(None, description="Markdown content of the recipe")
    tags: List[TagSchema] = Field(default_factory=list, description="List of tags associated with the recipe")
    class Config:
        orm_mode = True

class RecipeCreate(BaseModel):
    title: str = Field(..., description="Title of the recipe")
    description: Optional[str] = Field(None, description="Description of the recipe")
    file_path: Optional[str] = Field(None, description="Path to the markdown file for the recipe")
    content: Optional[str] = Field(None, description="Markdown content of the recipe")
    tag_ids: List[int] = Field(default_factory=list, description="IDs of tags to associate with the recipe")
