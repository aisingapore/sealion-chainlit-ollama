# Dockerfile
FROM python:3.11-slim-bookworm

# Set the work directory
WORKDIR /usr/src/app

# Install the packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the chainlit app
CMD ["chainlit", "run", "src/main.py", "-w", "--headless"]