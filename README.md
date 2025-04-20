# Mac-Copy-Recorder

Everytime you copy text on a mac, the script will save it to a text file for later use.

## Notes

### Functionality:

-When user copys something either from key strokes (command+c) or right/control click, the copied
content will be saved to an external file.
-External file will be saved for a period of a month then deleted.
-Time stamps added to each entry in the external file.
-Create GUI that will display all the previously copied material
-Python gui when launched will automatically show the clipboard history

### Packages/Libraries:

os: for file IO (already a part of python standard library)
sys (maybe):
pynput (library): mouse and keyboard input and monitoring. pip install pynput
pyperclip: for copy paste functionality
launchd: for managing system services and daemons
Tkinter: for building GUI with python

### Setup

launchd differentiates between agents and daemons. The main difference is that an agent is run on behalf of the logged in user while a daemon runs on behalf of the root user or any user you specify with the UserName key. Only agents have access to the macOS GUI.

-Store the .plist file in ~/Library/LaunchAgents if you want script to run only for the current
logged in user
-Store the script in ~/Scripts
-Make the script exectutable with 'chmod +x ~/Scripts/script.py' this will allow the script to be run by a cron job/launchd type srevice
