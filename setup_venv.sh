#!/bin/bash
PYTHON_VERSION=${1:-python3.11}

echo "[*] Creating virtual environment using $PYTHON_VERSION..."
$PYTHON_VERSION -m venv .venv || exit 1

echo "[*] Activating virtual environment..."
source .venv/bin/activate

echo "[*] Upgrading pip..."
pip install --upgrade pip

echo "[*] Installing requirements..."
pip install -r requirements.txt

echo "[OK] Environment setup complete. Use 'source .venv/bin/activate' to activate."
