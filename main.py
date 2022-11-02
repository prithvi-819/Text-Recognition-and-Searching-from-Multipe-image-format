# from curses import ACS_DARROW
from tkinter import filedialog
from PIL import Image
import numpy
from easygui import*
# from cv2 import adaptiveThreshold
# from psutil import STATUS_DEAD
import pytesseract as tess
# from zmq import HELLO_MSG



# message / information to be displayed on the screen
text1 = "Welcome To Text Finder!" 
text2 = "Please Select Files To Search From"
text = [text1, text2]
  
# title of the window
title = "Text Finder"

buttonlist = []

button1 = "Select Files"
button2 = "Exit"

buttonlist.append(button1)
buttonlist.append(button2)

img = "insert image here"
   
# creating a button box
output = buttonbox(text, title, image = img, choices = buttonlist)



tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract():
    # files = os.listdir('P:\CODES\Python')
    files = filedialog.askopenfilenames(title="Select Files")
    text = []
    n = len(files)
    print("number of files = ", n)
    string1 = input("Please Insert The string you are looking for: ") 
    
    for i in range(0,n):
        img = Image.open(files[i])

        text.append(tess.image_to_string(img))
        # numpy.char.lower(text)
        # print(text)
        # print(text[i])

        # for lines in text:
        #     if string1 in lines:
        #         print("string found!")
        #         # print(files)
        #     else:
        #         print("String not found")

        if string1 in text[i]:
            print("string found")
            print("File Location: ", files[i])
        else: 
            print("string not found")
        
        text_files = open(f'text{i+1}.txt',"w")
        text_files.write(text[i])


if __name__ == "__main__":
    extract()


