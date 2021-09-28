# check if the text had the name of a leggy in it

# dependencies
import os, sys

# TODO del me
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.config import pokemon_list

def process_text(text):
    """check if any part of a string is in a list of pokemon names

    Args:
        text ([str]): [text that might cointain a pokemon name]

    Returns:
        [bool]: [true if text contains a pokemon name]
    """
    text = text.split(" ")

    for text_bit in text:
        if text_bit.lower().strip() in pokemon_list:
            return True

    return False
