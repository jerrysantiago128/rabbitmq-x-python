FROM python:3.11

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ /app/
WORKDIR /app

# Command to run the application using Uvicorn
# 0.0.0.0 is the host, 8000 is the port, and 'app:app' means look for the 
# 'app' variable (the FastAPI instance) inside the 'app.py' file.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]