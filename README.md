# FileCleaner
This is a simple script that cleans out files/folders from directories given to the program (by hand for now). The files to be deleted are determined by the time since last modified. The user of the script can modify this time (in seconds) so that the script will only clear files/folders that are older than the set value they determine to be appropriate. The script can be accessed and executed from the batch file included by adding the .bat file to either a task (Task Scheduler on Windows) or by adding it to the system startup folder.

The inspiration behind this project was the fact that I was constantly running into the issue that I seemed to keep old files/folders on my PC for too long. This led to me constantly having to remove old files and downloads that I hadn't touched in weeks and even months. I wanted a simple script that I could customize to clear out old files and folders from the directories I wanted (like Downloads). The logic behind using this to clear out files/folders by their last modified time was that if I hadn't used it in a certain amount of time it didn't really matter.

NOTE: This would be disasterous if used incorrectly, for example by giving it a system directory. This should only be used for directories like Downloads that are temporary containers to hold installers and other downloaded data.

WISH LIST:
- Add a GUI to make it more user friendly
--- Allow the user to provide directories in GUI
--- Allow the user to determine wether to run the script on startup, etc.
- Add checks to make sure the directory paths are not critical system directories.