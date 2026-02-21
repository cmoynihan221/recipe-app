from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.db import Base

recipe_tag = Table(
    'recipe_tag', Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    file_path = Column(String, unique=True)
    content = Column(Text)
    tags = relationship('Tag', secondary=recipe_tag, back_populates='recipes')

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    recipes = relationship('Recipe', secondary=recipe_tag, back_populates='tags')
