# from os import cpu_count
# from functools import lru_cache
# import time

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# from tkinter.constants import CURRENT, DISABLED
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from PIL import ImageTk, Image
import requests
import webbrowser

from format import Resize
from ShowImage import ShowImage
from GetLabel import Label
from Find import FindFromFile, FindInText
from VersionCheck import VersionValue

global MyFg; global MyBg
global MyVersion
MyVersion = FindFromFile("VERSION", "source/TextData.txt")

class Main:
    global MyFg; global MyBg; global MyVersion; global RootExists
    def __init__(self, parent, MyTextFile = "source/TextData.txt"):
        global RootExists
        RootExists = True
        def CheckUpdates():
            global RootExists; global MyVersion
            
            # MyVersion = FindFromFile("VERSION", MyTextFile)
            
            ProgVersion = FindInText("VERSION", requests.get(FindFromFile("TEXTLINK", MyTextFile)).text)
            
            if int(VersionValue(MyVersion)) < int(VersionValue(ProgVersion)):
                
                MyMsg = f"CatsAndDogs v{ProgVersion} available. Do you want to update?\nClick 'Yes' to go the repository for latest version."
                response = messagebox.askquestion(title = f"CatsAndDogs v{MyVersion}", message = MyMsg)
                
                if response == "no":
                    pass
                elif response == "yes":
                    try:
                        # download msi file
                        webbrowser.open(FindFromFile("REPOLINK", MyTextFile))
                        RootExists = False
                        parent.destroy()
                    except Exception as e:
                        messagebox.showerror("Software update", "An error occured during the update: {e}")
            elif int(VersionValue(MyVersion)) == int(VersionValue(ProgVersion)):
                messagebox.showinfo(f"CatsAndDogs v{MyVersion}", "You are currently using the latest version.")

        CheckUpdates()

        def DocumentFrame():
            """Just a way to softcode my instuctions to the user.
                TextFile (string): takes an argument as string to the
                                path of the text you want to display
            """
            DocumentFrame = tk.LabelFrame(parent, width = 545, height = 75, text = "How it works", padx = 1, pady= 1, fg = MyFg, bg = MyBg)
            DocumentFrame.grid(row = 1, column = 0, columnspan = 3, rowspan = 1)
            
            #Read instructions from external text file
            Instruc = FindFromFile("INSTRUCTIONS", MyTextFile)
                
            tk.Label(DocumentFrame, text = Instruc.strip(), padx = 0, pady= 0, fg = MyFg, bg = MyBg).grid(row = 0, column= 0, columnspan= 3)
        
        if RootExists:
            DocumentFrame()

        def MainFrame():
            """This is going to contain the main functionality of the program.
            """
            MainFrame = tk.LabelFrame(parent, text = "What it needs is an image", padx = 5, pady = 5, fg = MyFg, bg = MyBg)
            MainFrame.place(x = 55, y = 275)

            #Method 1: computer selects a random image
            def RandomImage():
                ImagePath = FindFromFile("PATH", MyTextFile)
                temp = np.random.randint(low = 1, high = 79, size = 1)
                self.Predict(f"{ImagePath}"+str(temp[0])+".jpg")
                
            tk.Button(MainFrame, text = "Random Image", fg = MyFg, bg = MyBg, command = RandomImage).grid(row = 0, column = 0, columnspan= 3)
            tk.Label(MainFrame, text = str("-"*15 + "OR" + "-"*15), fg = "#808080", bg = MyBg).grid(row = 1, column = 0, columnspan = 3)

            #Method 2: User feeds a path to the computer in textual form
            tk.Label(MainFrame, text = "You can even type a path:", fg = MyFg, bg = MyBg).grid(row = 2, column = 0, columnspan = 3)
            EntryText = tk.Entry(MainFrame, fg = MyFg, bg = "#353535", width= 60)
            EntryText.grid(row = 3, column = 0)
            tk.Label(MainFrame, text = "   ", fg = MyFg, bg = MyBg).grid(row = 3, column = 2)
            tk.Button(MainFrame, text = "Insert", fg = MyFg, bg = MyBg, command = lambda: self.Predict(EntryText.get().strip()), padx = 5).grid(row = 3, column = 3)
            tk.Label(MainFrame, text = str("-"*15 + "OR" + "-"*15), fg = "#808080", bg = MyBg).grid(row = 4, column = 0, columnspan = 3)

            #Method 3: User selects an image through dialogue box
            def Browse():
                ImageLoc = filedialog.askopenfilename(initialdir= "D:/Vineet/work", title = "Select An Image:", filetypes= (("JPG Files", "*.jpg"), ("All Files", "*.*")))
                self.Predict(ImageLoc)
            tk.Button(MainFrame, text = "Browse this device", fg = MyFg, bg = MyBg, command = Browse).grid(row = 5, column = 0, columnspan= 3)
        
        if RootExists:
            MainFrame()

    def Predict(self, ImagePath):
        """This function makes the prediction.
        This is used in the Lite version as well.

            path (string): Path to the image that needs to be examined
        """
        try:
            Image = plt.imread(ImagePath)
        except ValueError:
            print(f"No such file or directory: {ImagePath}")
            #Error dialogue to be created

        ResizedImage = Resize(Image)

        """Model and Predictions  
        """
        MyModel = keras.models.load_model('source/model.h5')
        prediction = MyModel.predict(np.array([ResizedImage]))
        animal = Label(prediction)
        
        """Show Output
        """
        ShowImage(image = Image, label = animal, val = prediction)

def main():
    global MyFg; global MyBg
    root = tk.Tk()
    root.title(f"CatsAndDogs v{MyVersion}")
    root.iconbitmap("source/graphics/Icon_C&D.ico")
    root.geometry("545x500")
    root.configure(bg = "#121212")
    myImage = ImageTk.PhotoImage(Image.open("source/graphics/Image_C&D.JPG"))
    ImgLabel = tk.Label(image = myImage)
    ImgLabel.grid(row=0, column = 0, columnspan= 3)
    white = "#ffffff"; dark = "#282828"
    MyFg = white; MyBg = dark # dark mode
    # MyFg = "#000000"; MyBg = white # light mode
    Main(root)
    root.mainloop()
main()