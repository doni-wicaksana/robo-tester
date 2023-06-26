# robo-tester
initialisasi:
  Set-ExecutionPolicy Unrestricted -Scope Process
  python -m venv venv        # Create a virtual environment named "venv"
  source venv/bin/activate   # Activate the virtual environment (Unix/Linux)
  .\venv\Scripts\activate    # Activate the virtual environment (Windows)
install all package:
  pip install -r requirements.txt
  rfbrowser init

To create a requirements.txt file for your current Python project:
  pip freeze > requirements.txt