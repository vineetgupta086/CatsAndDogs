from os import cpu_count
import tkinter as tk
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
    with open(path) as MyFile:
        TempData = MyFile.readlines()
    MyFile.close()
    j = 3; doc = ''
    for i in range(0,np.size(TempData)-2):
        temp = "\n" if j > 0 else ''
        doc = str(doc + TempData[i+2]+temp)
        j = j-1
    print(np.size(TempData))
    tk.Label(DocFrame, text = doc, padx = 0, pady= 0, fg = white, bg = dark).grid(row = 0+2, column= 0, columnspan= 3)
DocFrame()

def Main():
    """This is going to contain the main functionality of the program.
    """
    MainFrame = tk.LabelFrame(root, text = "What it needs is an image", padx = 1, pady = 1, fg = white, bg = dark)
    MainFrame.grid(row = 2, column = 0, columnspan= 3, rowspan = 1)
    Buttons = {1,2}
    Labels = {1,2}
    #tk.Label(MainFrame, text = "Work in Progress", fg = white, bg = dark).pack()
    tk.Label(MainFrame, text = "you can type a path:", fg = white, bg = dark).grid(row = 0, column = 0, columnspan= 3)
    temp = tk.Entry(MainFrame, fg = white, bg = "#353535", width= 50).grid(row = 1, column = 0, columnspan= 2)
    tk.Button(MainFrame, text = "Insert", fg = white, bg = dark, command = lambda: 0, padx = 2).grid(row = 1, column = 2)
Main()
root.mainloop()