import os
import subprocess

def run(files):
    
    while True:
        i = -1
        for j in range(len(files)):
            i += 1
            if files[i] not in ['show.py','picture.py','file_runner.py'] and files[i].endswith(".py"):
                subprocess.check_call(["python3",files[i]])
                print(f"run successfully __{files[i]}__")
                
        if i == len(files):
            i = -1

files = os.listdir()
run(files)
