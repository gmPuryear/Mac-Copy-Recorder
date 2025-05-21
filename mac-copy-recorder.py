#!/usr/bin/env python3

import os
import time
import pyperclip
from pynput import keyboard
from datetime import datetime
from tzlocal import get_localzone

COPY_PASTE_FILE_PATH = os.path.expanduser("~/Documents/mac-copy-recorder-data.txt")
DEBUG_LOG = "/tmp/mac-debug.log"

def log_debug(message):
    with open(DEBUG_LOG, "a") as f:
        f.write(f"{datetime.now()}: {message}\n")

def on_activate():
    log_debug("Hotkey activated!")
    time.sleep(0.1)  # Allow clipboard to update

    try:
        copied_content = pyperclip.paste()
    except Exception as e:
        log_debug(f"Error accessing clipboard: {e}")
        return

    timestamp = datetime.now(get_localzone()).strftime('%Y-%m-%d %H:%M:%S')
    full_entry = f"{timestamp}: {copied_content}"

    write_to_file(full_entry)

def write_to_file(copied_value):
    try:
        with open(COPY_PASTE_FILE_PATH, 'a') as f:
            f.write(copied_value + '\n')
        log_debug("Copied text written to file")
    except Exception as e:
        log_debug(f"Error writing to file: {e}")

def listen_for_hotkeys():
    try:
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<cmd>+c'),
            on_activate
        )

        with keyboard.Listener(
            on_press=hotkey.press,
            on_release=hotkey.release
        ) as listener:
            log_debug("Hotkey listener started")
            listener.join()
    except Exception as e:
        log_debug(f"Error in hotkey listener: {e}")

def main():
    log_debug("Script started")
    listen_for_hotkeys()

if __name__ == "__main__":
    main()







# #!/usr/bin/env python3

# import sys
# import pyperclip
# import os
# from pynput import keyboard
# from datetime import datetime
# from tzlocal import get_localzone
# import time


# COPY_PASTE_FILE_PATH = os.path.expanduser("~/Documents/mac-copy-recorder-data.txt")


# #prints message to console when hotkeys are presssed
# def on_activate():
#     print('Global hotkey activated!')
#     time.sleep(0.1)  # Add a short delay to allow the clipboard to update
#     copied_content = pyperclip.paste()
#     copied_content_dict = {
#         'date_time': datetime.now(get_localzone()).strftime('%Y-%m-%d %H:%M:%S'),
#         'copied_content': copied_content
#     }
#     write_to_file(copied_content_dict['date_time'] + ': ' + copied_content_dict['copied_content'] + '\n')

# # hotkeys (command + c) are pressed then call write to file func and passes copied value
# def listen_for_hotkeys():
#     try:
#     # creates a HotKey oject from the HotKey class so pynput can read the string
#         hotkey = keyboard.HotKey(
#             keyboard.HotKey.parse('<cmd>+c'),
#             on_activate)
#         # creates a listener object that listens for hotkeys to be pressed and released. The 'with' ensures
#         # when the listener is stopped or the program ends, resources are cleaned up.
#         with keyboard.Listener(
#             # on_press is called when the hotkey is released
#             on_press = hotkey.press,
#             on_release = hotkey.release) as listener:
#             # Blocks the program from continuing until the listener is explicitly stopped and listens
#             # indefinitely.
#             listener.join()
#     except Exception as e:
#         print(f"Error in hotkey listener: {e}")

# def write_to_file(copied_value):
#     try:
#         # if file does not exist, create and open in apend mode
#         # 'with' closes the file automatically
#         with open(COPY_PASTE_FILE_PATH, 'a') as file_to_write:
#             file_to_write.write(copied_value + '\n')
#             # 'date_time' variable for each value writen to file
#             # throws exception for errors
#     except Exception as e:
#         print(f"Error writing to file: {e}")

# def main():
#     with open("/tmp/mac-debug.log", "a") as f:
#         f.write("Script started...\n")
#     listen_for_hotkeys()

# if __name__ == "__main__":
#     main()

