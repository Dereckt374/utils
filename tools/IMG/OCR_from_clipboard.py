from PIL import ImageGrab, Image
import pytesseract
from pytesseract import Output
import cv2
import pyperclip
import time  

#Recuperer image from clipboard
img = ImageGrab.grabclipboard()

if isinstance(img, Image.Image):

    # extract txt from image
    text = pytesseract.image_to_string(img)
    print(text)

    # txt to clipboard
    pyperclip.copy(text)
    print('success')


    
else : print('Fail')


time.sleep(5)

