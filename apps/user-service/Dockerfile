FROM python:3.9 AS builder
WORKDIR /app
COPY . .
RUN pip install --prefix=/install flask

# Stage 2: runtime stage
FROM python:3.9-slim
WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

CMD ["python", "app.py"]