import os

FILE_PATH = ""

def filter_num(file_name):
    return file_name.translate(None, "1234567890")
    

def rename_files():
    file_list = os.listdir(FILE_PATH)
    for file_name in file_list:
        os.rename(file_name, filter_num(file_name))


