import os
import string

def rename_file():
    #(1) get file names from a folder
    file_path = os.listdir('./prank')
    saved_path = os.getcwd()
    os.chdir('./prank')
    #(2) for each file, rename rename_file
    # file that doesn't exist
    os.rename('asdf.jpg', 'thenwhat.jpg')
    # for file_name in file_path:
    #     os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_file()
