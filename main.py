import matplotlib.pyplot as plt
from format import Resize
import numpy as np
from tensorflow import keras
from ShowImage import ShowIm
from GetLabel import Label
from IPython.display import Image

"""Importing Image and Resizing
"""
#image_loc = "data/dog3.jpg"
image_loc = input('Image Location:')
image = plt.imread(image_loc)
resized_image = Resize(image)


"""Model and Predictions  
"""
MyModel = keras.models.load_model('model.h5')
prediction = MyModel.predict(np.array([resized_image]))
print("Prediction Value:", prediction)
animal = Label(prediction)

"""Show Output
"""
ShowIm(image = image, label = animal)