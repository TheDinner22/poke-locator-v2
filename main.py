#TODO make a real requirements.txt and make sure setup.py works

# dependencies
import os, sys, time

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
    print("type 'help for help'\n")
    while 1:
        command = input("$").lower().strip()

        if command == "help":
            print('"help" - prints the help menu')
            print('"test" -  run all tests')
            print('"cam" - set the bounds for a screen shot with that weird click-top-left then drag-to-bottom-right thing')
            print('"start" - run the program')
            print('"kill" stop the CLI')
            
        elif command == "test":
            a = _App()
            a.run_all_tests()
        elif command == "cam":
            cam = Camera()
            cam.define_borders()
            print("\nScreenshot borders defined!!\n")
        elif command == "start":
            while 1:
                cam = Camera()
                p = Parser()
                r = Reader()

                # take screenshot
                cam.take_screen_shot()

                # convert screenshot to black and white
                p.parse_img()

                # get text from image
                text = r.get_text_from_img()

                # check the text for pokemon names
                name_spotted = process_text(text)

                # if a name was spotted, use lt to check for nearby pokemon
                if name_spotted:
                    alert_needed = check_nearby(cam)
                    if alert_needed:
                        loud = Speaker()
                        loud.play()
                
                time.sleep(1)

        elif command == "kill":
            break
