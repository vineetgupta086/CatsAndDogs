import matplotlib.pyplot as plt
import numpy as np
from tensorflow.python.ops.gen_string_ops import AsString

def ShowIm(image, label, val = False):
    """Displays image

    Args:
        img (image): Image object
        label (string): String object predicted by the model
    """
    #img = plt.imread(image_loc)
    x = val[0][0]
    plt.figure()
    plt.imshow(image)
    if val:
        if x<0:
            plt.title(label = f"{label}({np.round(x)})")
        else:
            plt.title(label = f"{label}(+{np.round(x)})")
    else:
        plt.title(label = label)
    plt.show()