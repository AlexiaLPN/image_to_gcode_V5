import subprocess
import os
import sys

def run_app():
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", script_path])

if __name__ == "__main__":
    run_app()