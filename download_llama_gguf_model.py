#!/usr/bin/env python3

import argparse
import os
from huggingface_hub import hf_hub_download

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_model_name_and_basename(parameter, quantize):
    return f'TheBloke/Llama-2-{parameter}-Chat-GGUF', f'llama-2-{parameter.lower()}-chat.{quantize}_0.gguf'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to download Llama models from Hugging Face's Model Hub.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--parameters", 
                        choices=["7B", "13B", "70B"], 
                        default="7B", 
                        help="Specify which Llama model parameter to download.")
    parser.add_argument("--quantize", 
                        type=str, 
                        default="Q4", 
                        help="Specify the quantization level.")
    args = parser.parse_args()

    ensure_directory_exists('models')

    model_name_or_path, model_basename = get_model_name_and_basename(args.parameters, args.quantize)
    
    model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename, local_dir='models')
    print(f"Model downloaded to: {model_path}")
