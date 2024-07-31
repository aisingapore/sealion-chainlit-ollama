# Explore the AI Singapore SEA-LION model with Chainlit and Ollama

## Meet the Cast
- [AI Singapore SEA-LION](https://github.com/aisingapore/sealion)
- [Chainlit](https://github.com/Chainlit/chainlit)
- [Ollama](https://github.com/ollama/ollama/blob/main/README.md#customize-a-model)

> [!NOTE]  
> This project is designed for local environments. Do not run it in production.

# Prerequisites
- [Docker](https://docs.docker.com/engine/install/)
  - For the default [model](https://huggingface.co/aisingapore/llama3-8b-cpt-sealionv2-instruct-gguf/blob/main/llama3-8B-cpt-sealionv2-instruct-Q4_K_M.gguf), set the memory limit to 6GB or more.
  - If a larger model is used, or if there are other active Docker containers in the environment, increase the memory limit further to take into account their memory requirements.
    <img width="600" alt="docker_resources" src="https://github.com/user-attachments/assets/069da8c8-66e9-4a9a-9820-9e2fcb5430f9">

## Getting Started
- Download the SEA-LION model. The size of the default [model](https://huggingface.co/aisingapore/llama3-8b-cpt-sealionv2-instruct-gguf/blob/main/llama3-8B-cpt-sealionv2-instruct-Q4_K_M.gguf) is 5GB. Please ensure that there is sufficient storage space and a good internet connection before proceeding:
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
  docker compose exec ollama ollama create llama3-8b-cpt-sealionv2 -f Modelfile
  ```
- Navigate to http://localhost:8000 to access the chatbot.
  <img width="924" alt="image" src="https://github.com/user-attachments/assets/517c527c-e730-434a-bb35-1550b938ffa2">


## Default Model
- The default model is [llama3-8B-cpt-sealionv2-instruct-Q4_K_M.gguf](https://huggingface.co/aisingapore/llama3-8b-cpt-sealionv2-instruct-gguf/blob/main/llama3-8B-cpt-sealionv2-instruct-Q4_K_M.gguf). This project is tested on a 14-inch 2023 MacBook Pro M3 Max with 64GB RAM.
- If you would like to test the other models, choose the model in https://huggingface.co/aisingapore/llama3-8b-cpt-sealionv2-instruct-gguf.
  - Update the model filename in  ```download_sealion.sh``` in the ```scripts``` directory. Download the model with the script.
    ```bash
    ./scripts/download_sealion.sh
    ```
  - Update the model filename in ```Modelfile``` in the ```sealion``` directory. Load the model in Ollama:
    ```bash
    docker compose exec ollama ollama create llama3-8b-cpt-sealionv2 -f Modelfile
    ```

## Customisations
- Please feel free to fork this repo and customise it.
- Upgrade the [Chainlit version](https://github.com/Chainlit/chainlit/releases) in the ```Dockerfile``` to support newer features.
- Examples:
  - [OAuth](https://docs.chainlit.io/authentication/oauth)
  - [Data Persistence](https://docs.chainlit.io/data-persistence/custom#sql-alchemy-data-layer)
  - Integrations with [LangChain](https://docs.chainlit.io/integrations/langchain) or other [inference servers](https://docs.chainlit.io/integrations/message-based)

## Acknowledgements
- Kudos to the [AI Singapore Team](https://huggingface.co/aisingapore/llama3-8b-cpt-sealionv2-instruct-gguf#the-team) for their good work!
