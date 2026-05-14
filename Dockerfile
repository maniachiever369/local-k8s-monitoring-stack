FROM python:3.11-slim

WORKDIR /app

# DevOps Task: Install curl safely so Docker can execute health checks
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir Flask==3.0.3

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

