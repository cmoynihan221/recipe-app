# Copilot Instructions for Recipe App

## Build, Test, and Lint Commands
- No build or test commands yet; backend will use FastAPI and Python.
- To run FastAPI locally: `uvicorn main:app --reload`
- To test Google Drive integration, use local OAuth2 credentials and run FastAPI on localhost.

## High-Level Architecture
- **Frontend:** React (planned), for searching/filtering recipes and tags.
- **Backend:** FastAPI, syncs with Google Drive, parses markdown files, manages recipes and tags.
- **Google Drive Integration:** Uses OAuth2 and Google Drive API to fetch markdown recipe files.
- **Tagging System:** Tags extracted from markdown files; automatic tagging via async job (word count/key term analysis) is a secondary feature.

## Key Conventions

### Backend Project Structure Guidelines
- Place SQLAlchemy models in `backend/models/`
- Place Pydantic schemas in `backend/schemas/`
- Place API controllers/routers in `backend/controllers/`
- Place database utilities and seed scripts in `backend/db/`
- Place tests in `backend/tests/`

- Recipes are stored as markdown files in Google Drive.
- Tags are initially extracted from markdown metadata/content; frontend only supports searching/filtering tags.
- Backend syncs recipes periodically and updates the database.
- Database models for recipes and tags; supports multiple tags per recipe.
- Code comments should be kept to a minimum; only comment code that needs clarification.
- Keep the codebase DRY and tidy: always check for duplicated code, remove unused files and methods.
- Follow best practices for file structure and naming conventions according to the chosen tech stack.
- Keep backend and frontend code in separate directories for clarity and maintainability.
- For shared knowledge (e.g., constants, types), use isolated Python packages that generate TypeScript code for the frontend.

## Additional Notes
- Local development uses test Google account and credentials.
- Deployment will use Docker and environment variables for credentials.

---

Update this file as build, test, and lint commands are added, or as architecture evolves.