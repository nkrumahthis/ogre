#! python

import os
from PIL import Image
from dotenv import load_dotenv

import pytesseract

pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")

print(pytesseract.image_to_string(Image.open('data/test1.png')))
