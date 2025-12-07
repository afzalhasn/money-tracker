FROM python:3.11-slim
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./pytest.ini ./pytest.ini

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Copy application code under /app/app
COPY ./app ./app

ENV PYTHONPATH=/app

CMD ["./entrypoint.sh"]
