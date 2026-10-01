FROM python:3.11-slim

WORKDIR /app-sequential

COPY app-sequential.py .
COPY app-konkuren-single-core.py .
COPY app-konkuren-multi-core.py .

CMD ["python", "app-sequential.py"]