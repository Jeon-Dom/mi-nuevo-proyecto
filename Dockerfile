FROM python:3.11-slim

WORKDIR /app

# Instalar Flask directamente (evita necesitar un requirements.txt para algo tan simple)
RUN pip install --no-cache-dir Flask

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]