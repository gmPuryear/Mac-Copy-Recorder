#!/usr/bin/env python3

import sys
import pyperclip
import os
from pynput import keyboard
from datetime import datetime
from tzlocal import get_localzone
import time


COPY_PASTE_FILE_PATH = os.path.expanduser("~/Documents/mac-copy-recorder-data.txt")


#prints message to console when hotkeys are presssed
def on_activate():
    print('Global hotkey activated!')
    time.sleep(0.1)  # Add a short delay to allow the clipboard to update
    copied_content = pyperclip.paste()
    copied_content_dict = {
        'date_time': datetime.now(get_localzone()).strftime('%Y-%m-%d %H:%M:%S'),
        'copied_content': copied_content
    }
    write_to_file(copied_content_dict['date_time'] + ': ' + copied_content_dict['copied_content'] + '\n')

# hotkeys (command + c) are pressed then call write to file func and passes copied value
def listen_for_hotkeys():
    try:
    # creates a HotKey oject from the HotKey class so pynput can read the string
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<cmd>+c'),
            on_activate)
        # creates a listener object that listens for hotkeys to be pressed and released. The 'with' ensures
        # when the listener is stopped or the program ends, resources are cleaned up.
        with keyboard.Listener(
            # on_press is called when the hotkey is released
                on_release = hotkey.release) as listener:
            # Blocks the program from continuing until the listener is explicitly stopped and listens
            # indefinitely.
            listener.join()
    except Exception as e:
        print(f"Error in hotkey listener: {e}")

def write_to_file(copied_value):
    try:
        # if file does not exist, create and open in apend mode
        # 'with' closes the file automatically
        with open(COPY_PASTE_FILE_PATH, 'a') as file_to_write:
            file_to_write.write(copied_value + '\n')
            # 'date_time' variable for each value writen to file
            # throws exception for errors
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    listen_for_hotkeys()

if __name__ == "__main__":
    main()

