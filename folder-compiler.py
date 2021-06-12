import os
from typing import List

def filter_func(var):
    return os.path

def main():
    # Throw if the folder that we want to use already exists
    if os.path.exists("./compiled-folder"):
        print("./compiled-folder exists! Please remove this folder so the program can work properly!")
        exit(1)
    os.mkdir("./compiled-folder")
    
    # Get all of the folders within the root directory
    root_folders = list(filter(lambda v: os.path.isdir(v), os.listdir(".")))
    root_folders.remove("compiled-folder")
    print(root_folders)
    

if __name__ == "__main__":
    main()