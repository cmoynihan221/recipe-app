#!/bin/bash
# Run Alembic migrations and dump schema to schema.sql

set -e

# Activate virtual environment
source "$(dirname "$0")/venv/bin/activate"

# Ensure DATABASE_URL is set
if [ -z "$DATABASE_URL" ]; then
  echo "DATABASE_URL is not set. Please export it before running this script."
  exit 1
fi

# Run Alembic migrations
alembic upgrade head

# Dump schema to schema.sql
mkdir -p "$(dirname "$0")/db"
pg_dump --schema-only --no-owner --no-privileges -U postgres -h localhost recipedb > "$(dirname "$0")/db/schema.sql"

echo "Migrations applied and schema dumped to backend/schema.sql."
