#!/bin/bash
python3 -m llama_cpp.server --model models/llama-2-7b-chat.Q4_0.gguf --n_gpu_layers 8
#python3 -m llama_cpp.server --model models/llama-2-13b-chat.Q4_0.gguf --n_gpu_layers 6