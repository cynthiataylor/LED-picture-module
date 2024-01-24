import os
import subprocess

def run(files):
    for file in files:
        if file != 'file_runner.py' and file.endswith(".py"):
            os.system(f"python3 {file}")
            print(f"run successfully __{file}__")

files = os.listdir()
run(files)
