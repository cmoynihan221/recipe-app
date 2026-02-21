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

## Healthcheck
- Test the health endpoint:
   ```bash
   curl http://localhost:8000/health
   ```

## Notes
- Ensure you are in the backend directory before running commands.
- Update requirements.txt after installing new packages.
