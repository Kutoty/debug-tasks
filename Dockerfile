FROM python:3.12-slim
WORKDIR /app
COPY check.py check.py
COPY tasks tasks
CMD ["python", "check.py"]
