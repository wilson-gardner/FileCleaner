import time
from os import listdir, remove
from os.path import getmtime

# get current time
curr_time = time.time()
# currently hard coded for 1 week
max_age = 604800 
# path to folder to clean
path = "/path/to/folder/"

#loop through all folder objects (both files and folders)
for obj in listdir(path):
    # full file path for getmtime()
    file_path = "{}/{}".format(path, obj)
    # check if modified over 1 week ago
    if (curr_time - getmtime(file_path)) > max_age:
        # delete file
        remove(file_path)
