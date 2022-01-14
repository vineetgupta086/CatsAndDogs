import numpy as np

def Label(val):
    """Returns the label of the prediction

    Args:
        val (float): negative/positive values

    Returns:
        str: 'cat'/'dog'
    """
    x = val[0][0]
    x = np.round(x,3)
    
    if x > 0:
        y = 'Dog'
        print(f"Prediction Magnitude: +{x}")
    elif x < 0:
        y = 'Cat'
        print(f"Prediction Magnitude: {x}")
    return f'Prediction: {y}'