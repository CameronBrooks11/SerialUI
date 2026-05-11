@echo off
set PYTHON=python
if not "%1"=="" (
  set PYTHON=%1
)

echo Creating virtual environment with %PYTHON%...
%PYTHON% -m venv .venv || goto :error

echo Activating virtual environment...
call .venv\Scripts\activate

echo Upgrading pip...
pip install --upgrade pip

echo Installing requirements...
pip install -r requirements.txt

echo [OK] Environment setup complete. Use ".venv\Scripts\activate" to activate.
goto :eof

:error
echo [!] Failed to create virtual environment. Check your Python installation.
