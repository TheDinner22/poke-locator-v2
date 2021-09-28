# DO NOT ALTER THIS FILE

# dependencies
import os, sys

# add project dir to path
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)

# get the location of pytesseract on the computer
from lib.config import pytesseract_location

# uninstall all pip packages
os.system("pip freeze > unin.txt")
os.system("pip uninstall -r unin.txt -y")


# install all pip packages
os.system("pip install -r requirements.txt")

# make sure pytesseract is working
try:
    import pytesseract

    # tell pytesseract where to look
    pytesseract.pytesseract.tesseract_cmd = pytesseract_location
except Exception:
    print("")
    print("---error pytesseract not installed---")
    print("")
