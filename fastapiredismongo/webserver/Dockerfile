# Pull base image
FROM tiangolo/uvicorn-gunicorn:python3.8

# Set working directory
WORKDIR /code/

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy all to container
COPY . /code/

# Port to access from local
EXPOSE 8000

# Start uvicorn
# CMD ["uvicorn", "main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]

