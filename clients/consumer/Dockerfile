FROM python:3.11

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ /app/
WORKDIR /app
# -u flag added to force stdout and stderr to be unbuffered; without this, the image logs did not show any content
CMD ["python", "-u",  "consume.py"] 