from user_folder import get_user_folder
from file import read_folder, move_files
import os

# Use all caps to create a constant
IMAGES = [".jpd", ".jpeg", ".png"]
MUSIC = [".mp3", ".wav"]
PDF = [".pdf"]
ZIP = [".rar", ".zip", ".tar"]


def main():
    print("Welcome to folder organization app")
    print("----------------------------------")
    working_folder = get_user_folder()
    items = read_folder(working_folder)

    for item in items:
        # print a single file in the array
        print("Single item is ", item)
        split_item = os.path.splitext(item)
        print("Split item is ", split_item)
        extension = split_item[1]

        folder_name = "Other"

        if extension in IMAGES:
            print(f"file {item} is an image")
            folder_name = "Image"
        elif extension in MUSIC:
            print(f"file {item} is a music")
            folder_name = "Music"
        elif extension in PDF:
            print(f"file {item} is a pdf")
            folder_name = "PDF"
        elif extension in ZIP:
            print(f"file {item} is a zip")
            folder_name = "ZIP"
        else:
            print(f"file {item} is unknown or others")

        move_files (file_name = item, working_dir = working_folder, folder_name = folder_name)

main()