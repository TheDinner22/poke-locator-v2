# convert text in an image to a string

# dependencies
import os, sys, pytesseract, cv2

# TODO del me
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.config import pytesseract_location

# tell pytesseract where to look
pytesseract.pytesseract.tesseract_cmd = pytesseract_location

class Reader:
    def __init__(self, img_path=False):
        self.ss_path = ".data/images/ss.png" if not img_path else img_path

    def get_text_from_img(self):
        """take all of the text from an image and return it

        Returns:
            [str]: [all of the text found in the ss.png file, newlines are replaced with spaces]
        """
        # load the image
        image = cv2.imread(self.ss_path)

        self.text_from_img = pytesseract.image_to_string(image).strip().lower().replace('\n',' ')
        return self.text_from_img
