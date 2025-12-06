# ./mcp/Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY server.py /app

RUN pip install fastapi uvicorn psycopg2-binary

ENV DB_URL=postgresql://admin:admin@db:5432/moneytracker

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "9000"]
