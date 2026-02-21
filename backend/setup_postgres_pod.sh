#!/bin/bash
# Start a local PostgreSQL database using Podman

POD_NAME=recipe-postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=recipedb
POSTGRES_USER=postgres

podman run --name $POD_NAME -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -e POSTGRES_DB=$POSTGRES_DB -e POSTGRES_USER=$POSTGRES_USER -p 5432:5432 -d docker.io/library/postgres:14

# Log output to backend/postgres_pod.log
# Wait for Postgres to be ready
until podman exec $POD_NAME pg_isready -U $POSTGRES_USER; do
  echo "Waiting for Postgres to be ready..."
  sleep 2
done

# Load schema if it exists
SCHEMA_FILE="$(dirname "$0")/db/schema.sql"
if [ -f "$SCHEMA_FILE" ]; then
  echo "Loading schema from $SCHEMA_FILE..."
  podman exec -i $POD_NAME psql -U $POSTGRES_USER -d $POSTGRES_DB < "$SCHEMA_FILE"
  echo "Schema loaded."
else
  echo "No schema file found at $SCHEMA_FILE. Skipping schema load."
fi

echo "Tailing logs from the PostgreSQL pod... (Ctrl+C to stop viewing logs)"
podman logs -f $POD_NAME | tee backend/postgres_pod.log

echo "PostgreSQL pod started."
echo "Connection string: postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@localhost:5432/$POSTGRES_DB"
echo "Set DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@localhost:5432/$POSTGRES_DB in your environment."
