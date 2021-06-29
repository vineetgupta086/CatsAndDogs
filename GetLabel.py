def Label(val):
    """Returns the label of the prediction

    Args:
        val (float): negative/positive values

    Returns:
        str: 'cat'/'dog'
    """
    x = val[0][0]
    try:
        if x > 0:
            return 'Dog'
        elif x < 0:
            return 'Cat'
    except ValueError as ve:
        print(f'You inserted an image which is neither a cat or a dog.')
