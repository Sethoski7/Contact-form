FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run Django dev server (since it's just a static site)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]