import os

# List all the files
def read_folder(folder_path):
    files = os.listdir(folder_path)
    print(files)

    return files

