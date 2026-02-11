from user_folder import get_user_folder
from file import read_folder

# Use all caps to create a constant
IMAGES = ["jpd", "jpeg", "png"]
MUSIC = ["mp3", "wav"]
PDF = ["pdf"]
ZIP = ["rar", "zip", "tar"]


def main():
    print("Welcome to folder organization app")
    print("----------------------------------")
    working_folder = get_user_folder()
    items = read_folder(working_folder)

    for item in items:
        # print a single file in the array
        print("Single item is ", item)

main()