# Development Environment Requirements

To ensure consistent development and deployment, use the following versions:

## Required Versions

- **Python:** 3.13.x (recommended: latest 3.13 release)
- **Node.js:** 20.x (for frontend development)
- **PostgreSQL:** 18.x (server and client tools, e.g., `pg_dump`)
- **pip:** Latest (upgrade with `pip install --upgrade pip`)
- **Alembic:** Latest (install with `pip install alembic`)

## Version Checks

- Check your Python version:
  ```bash
  python3 --version
  ```
- Check your Node.js version:
  ```bash
  node --version
  ```
- Check your PostgreSQL server and client version:
  ```bash
  psql --version
  pg_dump --version
  ```
  Ensure `pg_dump` version matches your PostgreSQL server version (18.x).

## Notes
- Use a virtual environment for Python dependencies.
- Use Homebrew, apt, or your OS package manager to install/upgrade PostgreSQL and Node.js.
- If you use Docker/Podman for Postgres, ensure your local client tools match the container version.
