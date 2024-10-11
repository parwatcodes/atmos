#!/bin/bash

REPO_URL="https://raw.githubusercontent.com/parwatcodes/atmos/develop/atmos.py"
INSTALL_DIR="/usr/local/bin"
COMMAND_NAME="atmos"
REQUIREMENTS_URL="https://raw.githubusercontent.com/parwatcodes/atmos/develop/requirements.txt"

# Check if Python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install it first."
    exit 1
fi

# Create a temporary directory for downloading files
TMP_DIR=$(mktemp -d)
cd $TMP_DIR

# Download the Python script using curl or wget
if command -v wget &> /dev/null; then
    wget -q -O $COMMAND_NAME $REPO_URL
elif command -v curl &> /dev/null; then
    curl -s -o $COMMAND_NAME $REPO_URL
else
    echo "Neither wget nor curl is installed. Please install one of them and try again."
    exit 1
fi

# Make the script executable
chmod +x $COMMAND_NAME

# Move the script to the installation directory
sudo mv $COMMAND_NAME $INSTALL_DIR/$COMMAND_NAME

# Cleanup temporary directory
cd ..
rm -rf $TMP_DIR

# Verify installation
if command -v $COMMAND_NAME &> /dev/null; then
    echo "Atmos CLI weather app installed successfully!"
    echo "Run '$COMMAND_NAME -c \"City Name\"' to get started."
else
    echo "Failed to install the Atmos CLI weather app."
    exit 1
fi
