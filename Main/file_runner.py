import os
import subprocess

def run(files):
    for file in files:
        if file not in ['show.py','picture.py'] and file.endswith(".py"):
            os.system(f"python3 {file}")
            print(f"run successfully __{file}__")

files = os.listdir()
run(files)
