#!/bin/bash
MODEL_FILENAME=llama3-8B-cpt-sealionv2-instruct-Q4_K_M.gguf
MODELS_DIRECTORY=models
mkdir -p ${MODELS_DIRECTORY}
if [ ! -f ./${MODELS_DIRECTORY}/${MODEL_FILENAME} ]; then
    echo "The model ${MODEL_FILENAME} does not exist. Downloading the model."
    curl -L "https://huggingface.co/aisingapore/llama3-8b-cpt-sealionv2-instruct-gguf/resolve/main/${MODEL_FILENAME}" -o "${MODELS_DIRECTORY}/${MODEL_FILENAME}"
else
    echo "The model ${MODEL_FILENAME} exists."
fi
