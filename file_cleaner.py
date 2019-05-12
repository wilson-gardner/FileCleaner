import time
from os import listdir, remove, system, name
from os.path import getmtime
from win10toast import ToastNotifier
from tqdm import tqdm


#VARIABLES
notifier = ToastNotifier() # win10toast
status = tqdm() # progress bar
max_age = 604800 # this is 1 week
folders = [ "D:\\Downloads" ] # add multiple folder paths for cleaning
total_files_cleaned = 0 # total files will be printed at the end


#FUNCTIONS
def clear_command_line(): # clear command prompt / terminal
    if name == 'nt': # if windows
        system('cls')
    else:
        system('clear')


def attempt_clear_files(folder):
    print("Attempting to clear {}:".format(folder))
    
    del_obj = [] # will hold all string paths for files/folder paths to be deleted
    objects = listdir(folder) # holds all string paths of files/folders in directory
    status.total = len(objects) # sets progress bar length
    
    for obj in objects: # iterates through each 
        path = get_obj_path(folder, obj)
        if (time.time() - getmtime(path)) > max_age:
            del_obj.append(path)
    
    if len(del_obj) > 0:
        for obj_path in del_obj: # iterates through each file/folder path
            remove(obj_path) 
            total_files_cleaned = total_files_cleaned + 1 # increment total files cleaned for final total
            status.update() # update progress bar
        status.close() # terminate current status bar
        print("-> File cleanup complete for {}...".format(folder))
    else:
        print("-> No files to clear.")
        print("Cancelling.........")


def get_obj_path(folder, obj):
    return "{}/{}".format(folder, obj) # returns fully formatted file/folder path


# MAIN PROGRAM
clear_command_line()
print("Beginning file cleanup...")
for folder in folders:
    attempt_clear_files(folder)
notifier.show_toast("File Cleaner", "{} files cleaned.".format(total_files_cleaned)) # show toast alert with total files/folders removed