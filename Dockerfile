# Dockerfile
FROM python:3.11-slim-bookworm

# Set the work directory
WORKDIR /usr/src/app

# Install the dependencies
RUN pip install aiohttp asyncpg openai python-dotenv sqlalchemy

# Install chainlit
# An earlier release of chainlit (1.0.506) is used
# It works out of the box without having to set up authentication and data persistence
RUN pip install chainlit==1.0.506

# Run the chainlit app
CMD ["chainlit", "run", "src/main.py", "-w", "--headless"]