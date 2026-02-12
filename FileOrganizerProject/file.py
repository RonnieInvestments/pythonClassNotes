import os
import shutil

# list all the files
def read_folder(folder_path):
    files = os.listdir(folder_path)
    #print(files)
    return files

# input working_dir, file_name, folder_name
def move_files(working_dir, file_name, folder_name):
    destination_path = os.path.join(working_dir, folder_name)
    # check for destination path
    # if there is no destination create it
    source = os.path.join(working_dir, file_name)
    print("Moving file to ", destination_path)

    if not os.path.isdir:
        # create it first
        os.makedirs(destination_path)
    shutil.move(src = source, dst = destination_path)

