# Explore the AI Singapore SEA-LION model with Chainlit and Ollama

## Overview
- [Getting Started](#getting-started)
- [Getting Started with Docker](#getting-started-with-docker)
- [Default Model](#default-model)
- [Customisations](#customisations)
- [Acknowledgements](#acknowledgements)

> [!NOTE]
> This project is designed for local environments. Do not run it in production.

## Meet the Cast
- [AI Singapore SEA-LION](https://github.com/aisingapore/sealion)
  - Model: https://ollama.com/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct:q4_0
- [Chainlit](https://github.com/Chainlit/chainlit)
- [Ollama](https://ollama.com/)

## Getting Started
### Prerequisites
- Python 3.9 or newer
- [Ollama](https://ollama.com/download)

### Run the app
- Install [Ollama](https://ollama.com/download), if it is not already installed.
- Pull the model.
  ```bash
  ollama pull aisingapore/gemma2-9b-cpt-sea-lionv3-instruct:q4_0
  ```
- In the project directory, create a virtual environment and activate it.
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
- Copy ```.env``` and update the values, if necessary:
  ```bash
  cp .env.example .env
  ```
- Install the packages.
  ```
  pip install -r requirements.txt
  ```
- Run the app.
  ```bash
  chainlit run src/main.py -w
  ```
- Navigate to http://localhost:8000 to access the chatbot.
  <img width="920" alt="image" src="https://github.com/user-attachments/assets/6ca473ad-e1bc-4bdb-aa85-c802416738e0">

## Getting Started with Docker
> [!NOTE]
> At the time of writing, [GPU support in Docker Desktop](https://docs.docker.com/desktop/features/gpu/) is only available on Windows with the WSL2 backend.

### Prerequisites
- [Docker](https://docs.docker.com/engine/install/)
  - For the default [model](https://ollama.com/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct:q4_0), set the memory limit to 6GB or more.
  - If a larger model is used, or if there are other active Docker containers in the environment, increase the memory limit further to take into account their memory requirements.
    <img width="600" alt="docker_resources" src="https://github.com/user-attachments/assets/069da8c8-66e9-4a9a-9820-9e2fcb5430f9">

### Run the app with Docker
- Copy ```.env``` and update the values, if necessary:
  ```bash
  cp .env.example .env
  ```
- Start the services:
  ```bash
  docker compose up
  ```
- Pull the SEA-LION model with Ollama:
  ```bash
  docker compose exec ollama ollama pull aisingapore/gemma2-9b-cpt-sea-lionv3-instruct:q4_0
  ```
- Navigate to http://localhost:8000 to access the chatbot.
  <img width="920" alt="image" src="https://github.com/user-attachments/assets/6ca473ad-e1bc-4bdb-aa85-c802416738e0">

## Default Model
- The default model is [gemma2-9b-cpt-sea-lionv3-instruct:q4_0](https://ollama.com/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct:q4_0).
- If you would like to test the other models, choose the model in https://ollama.com/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct.
  - Check that there is sufficient disk storage and memory. For example, [gemma2-9b-cpt-sea-lionv3-instruct:q8_0](https://ollama.com/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct:q8_0) requires at least 10GB of disk storage and 12GB of available memory in Docker.
  - Pull the model with Ollama.
    ```bash
    docker compose exec ollama ollama pull aisingapore/gemma2-9b-cpt-sea-lionv3-instruct:q8_0
    ```
  - Update the model name in  `.env`.
    ```
    LLM_MODEL=aisingapore/gemma2-9b-cpt-sea-lionv3-instruct:q8_0
    ```

## Customisations
- Please feel free to fork this repo and customise it.
- Examples:
  - [OAuth](https://docs.chainlit.io/authentication/oauth)
  - [Data Persistence](https://docs.chainlit.io/data-persistence/custom#sql-alchemy-data-layer)
  - Integrations with [LangChain](https://docs.chainlit.io/integrations/langchain) or other [inference servers](https://docs.chainlit.io/integrations/message-based)

## Acknowledgements
- Kudos to the [AI Singapore Team](https://huggingface.co/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct#the-team) for their good work!
