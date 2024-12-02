# Use the official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code
COPY . /app/

# Run Django's collectstatic command for production (optional)
#RUN python manage.py collectstatic --noinput

# Expose the port for the application
EXPOSE 8000

# Start the application with Gunicorn
CMD ["gunicorn", "projectname.wsgi:application", "--bind", "0.0.0.0:8000"]
