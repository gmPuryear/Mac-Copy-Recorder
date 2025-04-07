import sys
import pyperclip
from pynput import keyboard

COPY_PASTE_FILE_PATH = "~/Documents/mac-copy-recorder-data.txt"


#prints message to console when hotkeys are presssed
def on_activate():
    print('Global hotkey activated!')

# if hotkeys (command + c) are pressed then call write to file func and passes copied value
def listen_for_hotkeys():
    try:
    # creates a HotKey oject from the HotKey class so pynput can read the string
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<cmd>+c'),
            on_activate)
        # creates a listener object that listens for hotkeys to be pressed and released. The 'with' ensures
        # when the listener is stopped or the program ends, resources are cleaned up.
        with keyboard.Listener(
                on_press = hotkey.press,
                on_release = hotkey.release) as listener:
            # Blocks the program from continuing until the listener is explicitly stopped and listens
            # indefinitely.
            listener.join()
    except Exception as e:
        print(f"Error in hotkey listener: {e}")

def open_file_to_write():
    try:
        # if file does not existr, create and open
        with open(COPY_PASTE_FILE_PATH, 'a') as file_to_write:
            print("hello!")
            # 'write_to_file' function to write to file taking in copied value from 'listen' function
            # 'date_time' variable for each value writen to file
            # open file to write to and write value from 'listen' function
            # throws exception for errors
    except Exception as e:
        print(f"Error writing to mac-copy-recorder-data.txt: {e}")




# 'write_to_file' function to write to file taking in copied value from 'listen' function
    # 'date_time' variable for each value writen to file
    # open file to write to and write value from 'listen' function
    # throws exception for errors


def main():
    listen_for_hotkeys()

if __name__ == "__main__":
    main()

