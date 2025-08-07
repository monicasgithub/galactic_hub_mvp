# Use a slim Python 3.11 base image
FROM python:3.11-slim

# Don’t write .pyc files and ensure stdout/stderr are unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# On container start:
# 1. Autogenerate migrations for 'core'
# 2. Apply migrations
# 3. Load sample data
# 4. Run the dev server
CMD ["sh","-c", "\
    python manage.py makemigrations core && \
    python manage.py migrate && \
    python manage.py load_sample_data && \
    python manage.py runserver 0.0.0.0:8000 \
"]
