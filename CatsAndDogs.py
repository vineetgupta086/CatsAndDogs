from os import cpu_count
import tkinter as tk
from tkinter import filedialog
from tkinter.constants import CURRENT, DISABLED

import matplotlib.pyplot as plt
from format import Resize
import numpy as np
from tensorflow import keras
from ShowImage import ShowIm
from GetLabel import Label
from PIL import ImageTk, Image

root = tk.Tk()
root.title("CatsAndDogs")
root.iconbitmap("source/graphics/Icon_C&D.ico")
root.geometry("545x500")
root.configure(bg = "#121212")
myImage = ImageTk.PhotoImage(Image.open("source/graphics/Image_C&D.JPG"))
ImgLabel = tk.Label(image = myImage)
ImgLabel.grid(row=0, column = 0, columnspan= 3)

white = "#ffffff"; dark = "#282828"

def DocFrame(path = "source/TextData.txt"):
    """Just a way to softcode my instuctions to the user.
    """
    DocFrame = tk.LabelFrame(root, width = 545, height = 75, text = "How it works", padx = 1, pady= 1, fg = white, bg = dark)
    DocFrame.grid(row = 1, column = 0, columnspan = 3, rowspan = 1)
    
    #Read instructions from external text file
    with open(path) as MyFile:
        TempData = MyFile.readlines()
    MyFile.close()
    j = 3; doc = ''
    for i in range(0,np.size(TempData)-2):
        temp = "\n" if j > 0 else ''
        doc = str(doc + TempData[i]+temp)
        j = j-1
    tk.Label(DocFrame, text = doc, padx = 0, pady= 0, fg = white, bg = dark).grid(row = 0, column= 0, columnspan= 3)
DocFrame()

def Predict(path):
    """This function takes path as an input and makes the prediction.
    This is used in the Lite version as well.
    """
    try:
        Image = plt.imread(path)
    except ValueError:
        print(f"No such file or directory:{path}")

    ResizedImg = Resize(Image)

    """Model and Predictions  
    """
    MyModel = keras.models.load_model('source/model.h5')
    prediction = MyModel.predict(np.array([ResizedImg]))
    animal = Label(prediction)

    """Show Output
    """
    ShowIm(image = Image, label = animal, val = prediction)


def Main(path = "source/TextData.txt"):
    """This is going to contain the main functionality of the program.
    """
    MainFrame = tk.LabelFrame(root, text = "What it needs is an image", padx = 5, pady = 5, fg = white, bg = dark)
    #MainFrame.grid(row = 2, column = 0, columnspan= 3, rowspan = 1)
    MainFrame.place(x = 55, y = 275)

    #Method 1: computer selects a random image
    def RandImg():
        temp = np.random.randint(low = 1, high = 79, size = 1)
        with open(path) as MyFile:
            ImgLoc = MyFile.readlines() 
        MyFile.close()
        Predict(f"{ImgLoc[5]}"+str(temp[0])+".jpg")

    #tk.Label(MainFrame, text = "Work in Progress", fg = white, bg = dark).pack()
    tk.Button(MainFrame, text = "Random Image", fg = white, bg = dark, command = RandImg).grid(row = 0, column = 0, columnspan= 3)
    tk.Label(MainFrame, text = str("-"*15 + "OR" + "-"*15), fg = "#808080", bg = dark).grid(row = 1, column = 0, columnspan = 3)

    #Method 2: User feeds a path to the computer in textual form
    tk.Label(MainFrame, text = "You can even type a path:", fg = white, bg = dark).grid(row = 2, column = 0, columnspan = 3)
    EntryText = tk.Entry(MainFrame, fg = white, bg = "#353535", width= 60)
    EntryText.grid(row = 3, column = 0)
    tk.Label(MainFrame, text = "   ", fg = white, bg = dark).grid(row = 3, column = 2)
    tk.Button(MainFrame, text = "Insert", fg = white, bg = dark, command = lambda: Predict(EntryText.get().strip()), padx = 5).grid(row = 3, column = 3)
    tk.Label(MainFrame, text = str("-"*15 + "OR" + "-"*15), fg = "#808080", bg = dark).grid(row = 4, column = 0, columnspan = 3)

    #Method 3: User selects an image through dialogue box
    def Browse():
        ImageLoc = filedialog.askopenfilename(initialdir= "D:/Vineet/work", title = "Select An Image:", filetypes= (("JPG Files", "*.jpg"), ("All Files", "*.*")))
        Predict(ImageLoc)
    tk.Button(MainFrame, text = "Browse this device", fg = white, bg = dark, command = Browse).grid(row = 5, column = 0, columnspan= 3)

Main()
root.mainloop()