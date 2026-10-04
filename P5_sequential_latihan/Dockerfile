FROM python:3.11-slim

WORKDIR /app-sequential

COPY app-sequential.py .
COPY app-konkuren-single-core.py .
COPY app-konkuren-multi-core.py .

# Pertemuan 6
COPY app-parallel-speed-up.py .

CMD ["python", "app-parallel-speed-up.py"]