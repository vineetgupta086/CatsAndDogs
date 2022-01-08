import matplotlib.pyplot as plt
from format import Resize
import numpy as np
from tensorflow import keras
from ShowImage import ShowIm
from GetLabel import Label

while True:

    """Importing Image and Resizing
    """
    print('='*20,'\nSelect one option:\n1.Random image file\n2.Enter image file location\n0.Exit')
    arg = input('Input:')
    if arg == '1':
        temp = np.random.randint(low = 1, high = 79, size = 1)
        with open("TextData.txt") as MyFile:
            Path = MyFile.readlines() 
        MyFile.close()
        ImageLoc = str(Path[0]+str(temp[0])+'.jpg')
    
    if arg == '2':
        ImageLoc = input('Enter image Path:')
    
    elif arg == '0':
        break
    
    try:
        Image = plt.imread(ImageLoc)
    except ValueError:
        print(f"No such file or directory:{ImageLoc}")

    ResizedImg = Resize(Image)

    """Model and Predictions  
    """
    MyModel = keras.models.load_model('source/model.h5')
    prediction = MyModel.predict(np.array([ResizedImg]))
    animal = Label(prediction)

    """Show Output
    """
    ShowIm(image = Image, label = animal, val = prediction)
print("Program Ended.\n","="*20)