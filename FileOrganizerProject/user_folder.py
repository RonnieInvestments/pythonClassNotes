# check if file path is valid
import os
import sys

'''
os.path.isdir
input of this method - string path
output - True or False
'''

def get_user_folder():
    folder_path = input("Enter the folder path:")
    print(folder_path)

    isdir = os.path.isdir(folder_path)
    if not isdir:
        print("Invalid directory entered.")
        sys.exit()

    return folder_path # print to see if it is ok