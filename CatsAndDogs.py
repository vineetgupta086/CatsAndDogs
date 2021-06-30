import matplotlib.pyplot as plt
from format import Resize
import numpy as np
from tensorflow import keras
from ShowImage import ShowIm
from GetLabel import Label

while True:

    """Importing Image and Resizing
    """
    ImageLoc = input('Enter image Path:')
    if ImageLoc == '0':
        break
    
    try:
        Image = plt.imread(ImageLoc)
    except ValueError:
        print(f"No such file or directory:{ImageLoc}")
    ResizedImg = Resize(Image)

    """Model and Predictions  
    """
    MyModel = keras.models.load_model('model.h5')
    prediction = MyModel.predict(np.array([ResizedImg]))
    animal = Label(prediction)

    """Show Output
    """
    ShowIm(image = Image, label = animal)
print("Program Ended.","="*20)