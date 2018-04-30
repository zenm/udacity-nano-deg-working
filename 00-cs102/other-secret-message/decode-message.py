import os
import string

def rename_file():
    #(1) get file names from a folder
    file_path = os.listdir('./secret-message-code')
    saved_path = os.getcwd()
    os.chdir('./secret-message-code')
    #(2) for each file, rename rename_file
    for file_name in file_path:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_file()
