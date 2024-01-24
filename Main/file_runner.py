import os
import subprocess

def run(files):
    for file in files:
        subprocess.check_call(['python3',file])
        print(file,"run successfully")
if __name__ == "__main__":
    files = os.listdir()
    run(files)