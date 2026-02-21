from backend.db.db import SessionLocal
from backend.models.recipe import Recipe, Tag

def seed():
    db = SessionLocal()
    # Create a tag
    tag = Tag(name="TestTag")
    db.add(tag)
    db.commit()
    db.refresh(tag)
    # Create a recipe
    recipe = Recipe(
        title="Test Recipe",
        description="A test recipe for seeding the database.",
        file_path="test_recipe.md",
        content="# Test Recipe\n\nThis is a test recipe.",
        tags=[tag]
    )
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    print(f"Seeded recipe: {recipe.title} with tag: {tag.name}")
    db.close()

if __name__ == "__main__":
    seed()
