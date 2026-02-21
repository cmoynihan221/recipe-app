# Recipe App Implementation Plan

## Problem Statement
Build a simple recipe app that allows users to upload markdown recipe files to their personal Google Drive. The backend will periodically sync with Google Drive to fetch recipe files and display them in a simple frontend. The app must support a comprehensive tagging system for recipes.

## Proposed Architecture
- **Frontend:** Simple UI (React recommended) for browsing, searching, and tagging recipes.
- **Backend:** Syncs with Google Drive, parses markdown files, manages recipes and tags. FastAPI will be used for the backend.
- **Google Drive Integration:** Users authenticate and upload markdown files. Backend uses Google Drive API to fetch and sync recipes.
- **Tagging System:** Recipes can be tagged with multiple tags. Tags are managed and searchable.

## Key Features
- Upload markdown recipe files to Google Drive
- Backend syncs recipes from Google Drive
- Display recipes in frontend
- Comprehensive tagging system (add, edit, search tags)

## Todos
1. Use FastAPI as backend framework
2. Set up Google Drive API integration:
   - Register app in Google Cloud Console
   - Enable Google Drive API
   - Configure OAuth2 credentials
   - Implement OAuth2 flow in FastAPI
   - Store and manage user tokens
   - Use Google Drive API to fetch markdown files
3. Implement backend sync logic for recipe files:
   - Schedule periodic sync (e.g., background task or cron)
   - Use Google Drive API to list and fetch new/updated markdown files
   - Parse markdown files and update recipe database
   - Handle errors and token refresh
4. Design and build frontend (React recommended)
5. Implement tagging system (backend and frontend):
   - Design tag schema (support multiple tags per recipe)
   - Backend endpoints for tag CRUD (create, read, update, delete)
   - Associate tags with recipes in database
   - Frontend UI for searching and filtering tags only
   - Tag search/filter functionality
   - Initial tags extracted from markdown file metadata or content
   - (Secondary) Automatic tagging via word count/key term analysis in async job
6. Recipe display and search functionality

## Notes
- Consider authentication for Google Drive access
- Tagging should support multiple tags per recipe and tag search
- Markdown parsing required for recipe content
- Periodic sync can be scheduled (e.g., cron job or background task)



## Comprehensive Backend Plan

### 1. FastAPI Setup
- Initialize FastAPI project structure
- Set up environment variables for Google credentials
- Install required packages: fastapi, uvicorn, google-auth, google-api-python-client, pydantic, etc.

### 2. Google Drive Integration
- Register app in Google Cloud Console
- Enable Google Drive API
- Configure OAuth2 credentials
- Implement OAuth2 flow in FastAPI (user login, token storage)
- Store and manage user tokens securely
- Use Google Drive API to list, fetch, and download markdown files

### 3. Recipe Sync Logic
- Schedule periodic sync (background task or cron)
- List and fetch new/updated markdown files from Google Drive
- Parse markdown files to extract recipe content and tags
- Update recipe database (add/update/delete recipes)
- Handle errors, token refresh, and logging

### 4. Tagging System
- Design tag schema (support multiple tags per recipe)
- Extract initial tags from markdown metadata/content
- (Secondary) Implement async job for automatic tagging via word count/key term analysis
- Backend endpoints for tag CRUD (create, read, update, delete)
- Associate tags with recipes in database

### 5. Recipe Database
- Choose database (e.g., SQLite for local, PostgreSQL for production)
- Define models for recipes and tags
- Implement database migrations

### 6. API Endpoints
- Recipe endpoints: list, get, search
- Tag endpoints: list, search
- Authentication endpoints (if needed)

### 7. Testing & Local Development
- Use test Google account and credentials
- Mock Google Drive API for unit tests
- Test sync, parsing, and tag extraction logic

### 8. Deployment Considerations
- Containerize with Docker
- Set up environment variables for production
- Schedule sync tasks (e.g., Celery, APScheduler)

---

Let me know if you want to adjust the backend plan, add more details, or specify database/infra choices.