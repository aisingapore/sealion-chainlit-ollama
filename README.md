# Explore the AI Singapore SEA-LION model with Chainlit and Ollama

## Meet the Cast
- [AI Singapore SEA-LION](https://github.com/aisingapore/sealion)
  - Model: https://ollama.com/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct
- [Chainlit](https://github.com/Chainlit/chainlit)
- [Ollama](https://ollama.com/)

> [!NOTE]  
> This project is designed for local environments. Do not run it in production.

# Prerequisites
- [Docker](https://docs.docker.com/engine/install/)
  - For the default [model](https://ollama.com/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct), set the memory limit to 6GB or more.
  - If a larger model is used, or if there are other active Docker containers in the environment, increase the memory limit further to take into account their memory requirements.
    <img width="600" alt="docker_resources" src="https://github.com/user-attachments/assets/069da8c8-66e9-4a9a-9820-9e2fcb5430f9">

## Getting Started
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
  docker compose exec ollama ollama pull aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct
  ```
- Navigate to http://localhost:8000 to access the chatbot.
  <img width="924" alt="image" src="https://github.com/user-attachments/assets/517c527c-e730-434a-bb35-1550b938ffa2">


## Default Model
- The default model is [llama3-8b-cpt-sea-lionv2-instruct:q4_k_m](https://ollama.com/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct:q4_k_m).
- If you would like to test the other models, choose the model in https://ollama.com/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct.
  - Check that there is sufficient disk storage and memory. For example, [llama3-8b-cpt-sea-lionv2.1-instruct:q8_0](https://ollama.com/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct:q8_0) requires 8.5GB of disk storage and 9.3GB of available memory in Docker.
  - Pull the model with Ollama.
    ```bash
    docker compose exec ollama ollama pull aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct:q8_0
    ```
  - Update the model name in  `.env`.
    ```
    LLM_MODEL=aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct:q8_0
    ```

## Customisations
- Please feel free to fork this repo and customise it.
- Upgrade the [Chainlit version](https://github.com/Chainlit/chainlit/releases) in the ```Dockerfile``` to support newer features.
- Examples:
  - [OAuth](https://docs.chainlit.io/authentication/oauth)
  - [Data Persistence](https://docs.chainlit.io/data-persistence/custom#sql-alchemy-data-layer)
  - Integrations with [LangChain](https://docs.chainlit.io/integrations/langchain) or other [inference servers](https://docs.chainlit.io/integrations/message-based)

## Acknowledgements
- Kudos to the [AI Singapore Team](https://huggingface.co/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct-gguf#the-team) for their good work!
