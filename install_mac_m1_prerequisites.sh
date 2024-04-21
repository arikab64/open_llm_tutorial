#!/bin/bash 

# Check if XCode command line tools are already installed.
install_xcode_tools() {
    if xcode-select -p &>/dev/null; then
        echo "Xcode Command Line Tools are already installed."
    else
        echo "Xcode Command Line Tools are not installed. Installing now..."
        xcode-select --install

        # Wait until the Xcode Command Line Tools are installed
        while ! xcode-select -p &>/dev/null; do
            sleep 5 
        done
        echo "Xcode Command Line Tools have been installed successfully!"
    fi
}

install_conda() {
    # Download the latest Miniforge for macOS arm64
    wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
    bash Miniforge3-MacOSX-arm64.sh -u
    echo "Conda (Miniforge) has been installed successfully!"
}

make_conda_environment() {
    export PATH="$HOME/miniforge3/bin:$PATH"
    conda create -n llama python=3.9.16
    conda activate llama
}

echo ">>>> Install XCode Tools"
install_xcode_tools

echo ">>>> Prepare Conda Environment"
install_conda
make_conda_environment