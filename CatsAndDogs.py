import matplotlib.pyplot as plt
from format import Resize
import numpy as np
from tensorflow import keras
from ShowImage import ShowIm
from GetLabel import Label

while True:

    """Importing Image and Resizing
    """
    image_name = input('Image Name:')
    if image_name == '0':
        break

    image_loc = f"data/{image_name}.jpg"
    try:
        image = plt.imread(image_loc)
    except ValueError:
        print(f"No such file or directory:{image_loc}")
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
print("Program Ended.","="*20)