import os
import subprocess

def run(files):
    for file in files:
        if file != 'file_runner.py':
            print(file)
            subprocess.check_call(['python3',file])
if __name__ == "__main__":
    files = os.listdir()
    run(files)