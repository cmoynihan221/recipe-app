# Recipe App Backend

## Setup
1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Backend
- To start the backend server:
   ```bash
   ./start.sh
   ```
- The server will run at http://localhost:8000

## Virtual Environment
- To activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
- To exit the virtual environment:
   ```bash
   deactivate
   ```

## Healthcheck
- Test the health endpoint:
   ```bash
   curl http://localhost:8000/health
   ```

## Development Database (PostgreSQL with Podman)
- To start a local PostgreSQL database for development:
   ```bash
   ./setup_postgres_pod.sh
   ```
- Set the following environment variable in your shell or .env file:
   ```bash
   export DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/recipedb
   ```
- The backend will now use PostgreSQL for development, matching production setup.

## Database Migrations (Alembic)
- To create a new migration after changing models:
   ```bash
   alembic revision --autogenerate -m "describe your change"
   ```
- To apply migrations and upgrade the database:
   ```bash
   alembic upgrade head
   ```
- Ensure the DATABASE_URL environment variable is set before running Alembic commands.

## Notes
- Ensure you are in the backend directory before running commands.
- Update requirements.txt after installing new packages.
