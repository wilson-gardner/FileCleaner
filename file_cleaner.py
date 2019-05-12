import time
from os import listdir, remove, system, name
from os.path import getmtime
from win10toast import ToastNotifier
from tqdm import tqdm


#VARIABLES
notifier = ToastNotifier()
status = tqdm()
max_age = 604800
folders = [ "D:\\Downloads" ]
total_files_cleaned = 0


#FUNCTIONS
def clear_command_line():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def attempt_clear_files(folder):
    print("Attempting to clear {}:".format(folder))
    del_obj = []
    objects = listdir(folder)
    status.total = len(objects)
    for obj in objects:
        if (time.time() - getmtime(get_file_path(folder, obj))) > max_age:
            del_obj.append(obj)
    if len(del_obj) > 0:
        for obj in del_obj:
            remove(get_file_path(folder, obj))
            total_files_cleaned = total_files_cleaned + 1
            status.update()
        status.close()
        print("-> File cleanup complete for {}...".format(folder))
    else:
        print("-> No files to clear.")
        print("Cancelling.........")


def get_file_path(folder, obj):
    return "{}/{}".format(folder, obj)


# MAIN PROGRAM
clear_command_line()
print("Beginning file cleanup...")
for folder in folders:
    attempt_clear_files(folder)
notifier.show_toast("File Cleaner", "{} files cleaned.".format(total_files_cleaned))