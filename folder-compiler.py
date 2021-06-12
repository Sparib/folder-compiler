import os
import shutil
from typing import List

def get_subdirs(directory: str) -> List[str]:
    return list(filter(lambda v: os.path.isdir(v), os.listdir(directory)))

def main():
    # Throw if the folder that we want to use already exists
    if os.path.exists("./compiled-folder"):
        print("./compiled-folder exists! Please remove this folder so the program can work properly!")
        exit(1)
    os.mkdir("./compiled-folder")
    
    # Get all of the folders within the root directory
    file_structure = []
    for root, _, files in os.walk("."):
        if root == ".": continue
        for name in files:
            file_structure.append(os.path.join(root, name).replace("\\", "/"))

    print(file_structure)

    for src in file_structure:
        # Set up target directory for copying
        tgt = src.split("/"); tgt[1] = "compiled-folder"; tgt = "/".join(tgt)
        os.makedirs(os.path.dirname(tgt), exist_ok=True)
        if os.path.isfile(tgt):
            # Append data if file already exists
            try:
                sf = open(src, 'r')
                tf = open(tgt, "a")
                tf.write("\n" + sf.read())
            except:
                # Throw and remove tree
                shutil.rmtree("./compiled-folder")
                print("Error while appending file data!")
                exit(1)
            finally:
                # Close files
                sf.close()
                tf.close()
        else:
            # Copy files
            shutil.copy(src, tgt)

if __name__ == "__main__":
    main()