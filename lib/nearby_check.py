# Check the output of the lt command to see if a leggy is nearby

# dependencies
import os, sys

# TODO del me
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.key_press import type_lt
from lib.process_image import Parser
from lib.img_to_text import Reader


def check_nearby(cam):
    # enter the command in mc
    type_lt()

    # take picture of screen
    cam.take_screen_shot()

    # parse the image with a new (non-yellow) RGB thresh-hold
    p = Parser(MASK_RGB=[255, 85, 85])
    p.parse_img()

    # get the text from the image
    r = Reader()
    text = r.get_text_from_img()

    is_first_part_in_string = True if "no legendary" in text else False
    is_second_part_in_string = True if "is spawned on you" in text else False

    alert_needed = True if (not is_first_part_in_string) and (not is_second_part_in_string) else False
    return alert_needed

if __name__ == "__main__":
    print(check_nearby())