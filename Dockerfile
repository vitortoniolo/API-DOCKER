FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk update && \
    apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
