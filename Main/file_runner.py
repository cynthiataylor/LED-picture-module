import os
import subprocess

def run(files):
    for file in files:
        # if file != 'file_runner.py':
        print(file)
        os.system(f"python3 {file}")

files = os.listdir()
run(files)
