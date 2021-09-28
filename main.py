#TODO make a real requirements.txt and make sure setup.py works

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from testing.main_test import _App
from lib.screenshot import Camera
from lib.process_image import Parser
from lib.img_to_text import Reader
from lib.process_text import process_text
from lib.nearby_check import check_nearby
from lib.loud import Speaker

RUN_CLI = True

if RUN_CLI:
    print("type 'help for help\n'")
    while 1:
        command = input("$").lower().strip()

        if command == "help":
            print('"help" - prints the help command')
            
        elif command == "test":
            pass
        elif command == "cam":
            pass
        elif command == "start":
            pass
