#!/bin/bash
MODEL_FILENAME=sea-lion-7b-instruct-Q8_0.gguf
MODELS_DIRECTORY=models
mkdir -p ${MODELS_DIRECTORY}
if [ ! -f ./${MODELS_DIRECTORY}/${MODEL_FILENAME} ]; then
    echo "The model ${MODEL_FILENAME} does not exist. Downloading the model."
    curl -L "https://huggingface.co/aisingapore/sea-lion-7b-instruct-gguf/resolve/main/${MODEL_FILENAME}" -o "${MODELS_DIRECTORY}/${MODEL_FILENAME}"
else
    echo "The model ${MODEL_FILENAME} exists."
fi
