#!/bin/bash

pip uninstall llama-cpp-python -y

CMAKE_ARGS="-DLLAMA_CUBLAS=on" \
FORCE_CMAKE=1 \
pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir --verbose

# OpenAI Server
pip install llama-cpp-python[server]