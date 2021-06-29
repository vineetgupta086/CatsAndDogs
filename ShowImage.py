import matplotlib.pyplot as plt
import numpy as np
from tensorflow.python.ops.gen_string_ops import AsString

def ShowIm(image, label):
    """Displays image

    Args:
        img (image): Image object
        label (string): String object predicted by the model
    """
    #img = plt.imread(image_loc)
    plt.figure()
    plt.imshow(image)
    plt.title(label = label)
    plt.show()