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
root.iconbitmap("source/Icon_C&D.ico")

myImage = ImageTk.PhotoImage(Image.open("E:/Vineet/work/projects/CatsAndDogs/source/Image_C&D.JPG"))
ImgLabel = tk.Label(image = myImage)
ImgLabel.grid(row=0, column = 0, columnspan= 3)
root.geometry("545x400")



root.mainloop()