# Explore the AI Singapore SEA-LION model with Chainlit and Ollama

## Meet the Cast
- [AI Singapore SEA-LION](https://github.com/aisingapore/sealion)
- [Chainlit](https://github.com/Chainlit/chainlit)
- [Ollama](https://github.com/ollama/ollama/blob/main/README.md#customize-a-model)

> [!NOTE]  
> This project is designed for local environments. Do not run it in production.

# Prerequisites
- [Docker](https://docs.docker.com/engine/install/)
  - For the default [model](https://huggingface.co/aisingapore/sea-lion-7b-instruct-gguf/blob/main/sea-lion-7b-instruct-Q8_0.gguf), set the memory limit to 9GB or more.
  - If a larger model is used, or if there are other active Docker containers in the environment, increase the memory limit further to take into account their memory requirements.
    <img width="600" alt="docker-memory-limit" src="https://github.com/aisingapore/sealion-chainlit-ollama/assets/62876165/a4268b5f-4ba8-46f4-8460-5d93ace3a455">

## Getting Started
- Download the SEA-LION model. The size of the default [model](https://huggingface.co/aisingapore/sea-lion-7b-instruct-gguf/blob/main/sea-lion-7b-instruct-Q8_0.gguf) is 8GB. Please ensure that there is sufficient storage space and a good internet connection before proceeding:
  ```bash
  ./scripts/download_sealion.sh
  ```
- Copy ```.env``` and update the values, if necessary:
  ```bash
  cp .env.example .env
  ```
- Start the services:
  ```bash
  docker compose up
  ```
- Load the SEA-LION model in Ollama:
  ```bash
  docker compose exec ollama ollama create sealion -f Modelfile
  ```
- Navigate to http://localhost:8000 to access the chatbot.
<img width="858" alt="sealion_chatbot_02" src="https://github.com/aisingapore/sealion-chainlit-ollama/assets/62876165/7d528ec9-604b-4bf1-bd34-a7589bfff433">

## Default Model
- The default model is [sea-lion-7b-instruct-Q8_0.gguf](https://huggingface.co/aisingapore/sea-lion-7b-instruct-gguf/blob/main/sea-lion-7b-instruct-Q8_0.gguf). This project is tested on a MacBook Pro with 2.3 GHz Quad-Core Intel Core i7 CPU and 32 GB 3733 MHz LPDDR4X RAM.
- If you would like to test the other models, choose the model in https://huggingface.co/aisingapore/sea-lion-7b-instruct-gguf.
  - Update the model filename in  ```download_sealion.sh``` in the ```scripts``` directory. Download the model with the script.
    ```bash
    ./scripts/download_sealion.sh
    ```
  - Update the model filename in ```Modelfile``` in the ```sealion``` directory. Load the model in Ollama:
    ```bash
    docker compose exec ollama ollama create sealion -f Modelfile
    ```

## Customisations
- Please feel free to fork this repo and customise it.
- Upgrade the [Chainlit version](https://github.com/Chainlit/chainlit/releases) in the ```Dockerfile``` to support newer features.
- Examples:
  - [OAuth](https://docs.chainlit.io/authentication/oauth)
  - [Data Persistence](https://docs.chainlit.io/data-persistence/custom#sql-alchemy-data-layer)
  - Integrations with [LangChain](https://docs.chainlit.io/integrations/langchain) or other [inference servers](https://docs.chainlit.io/integrations/message-based)

## Acknowledgements
- Kudos to the [SEA-LION Team](https://huggingface.co/aisingapore/sea-lion-7b-instruct-gguf#the-team) for their good work!
