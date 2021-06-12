# Folder Compiler
Compiles folders with same-name subdirectories into one folder with all files from all subdirectories

## Usage
Download the `.py` file then run the file in python while in the directory you want to be compiled

### Example
Folder Tree:
```
root-folder
|
| - folder x
|   |
|   | - folder 1
|   |   |
|   |   | - file x.txt
|   |   | - same.txt
|
| - folder y
|   |
|   | - folder 1
|   |   |
|   |   | - file y.txt
|   |   | - same.txt
```

The contents of `same.txt` under `folder x` and `folder y` is `Stuff from x` and `Stuff from y`, respectively.

Running `folder-compiler.py` in the `root-folder` adds a folder named `compiled-folder` with the following tree:
```
compiled-folder
|
| - folder 1
|   |
|   | - file x.txt
|   | - file y.txt
|   | - same.txt
```

The contents of `same.txt` is now
```
Stuff from x
Stuff from y
```
