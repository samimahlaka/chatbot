# Use Python image
FROM python:3.11

# Set work directory in container
WORKDIR /app

# Copy everything into container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
