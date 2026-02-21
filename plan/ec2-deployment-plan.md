# EC2 Deployment Plan for Recipe App Backend

1. Launch an EC2 instance (Ubuntu recommended).
2. Install Python, pip, and a process manager (systemd or supervisord).
3. Clone the repository to the EC2 instance.
4. Set up a Python virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
5. Set environment variables, especially `DATABASE_URL` (use AWS RDS or another managed PostgreSQL service).
6. Use a production ASGI server (e.g., uvicorn or gunicorn with uvicorn workers):
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   # or
   gunicorn -k uvicorn.workers.UvicornWorker main:app
   ```
7. Set up a reverse proxy (e.g., Nginx) to forward HTTP requests to the ASGI server.
8. Optionally, use Docker/Podman for containerized deployment.
9. Configure security groups and firewalls to allow HTTP/HTTPS traffic.
10. Set up monitoring, logging, and backups as needed.

---

Adjust steps as needed for your infrastructure and security requirements.
