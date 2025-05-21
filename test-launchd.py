# ~/IdeaProjects/Mac-Copy-Recorder/test-launchd.py
import time
with open("/tmp/launchd-test.txt", "a") as f:
    f.write("launchd is working!\n")
    time.sleep(10)
