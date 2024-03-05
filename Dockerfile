FROM python:3.11
EXPOSE 8080
WORKDIR /app
RUN apt-get update && apt-get install libgl1 -y
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--config", "gunicorn_config.py", "app:app"]
