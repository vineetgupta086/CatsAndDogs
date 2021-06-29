import tensorflow as tf

#The entire model and predictions are based on images of size:
#160x160
res = 160
image_size = (res, res)

def Resize(image):
    image_conv = tf.cast(image, tf.float32)
    image_norm = (image_conv/80)-1
    image_resized = tf.image.resize(image_norm, image_size)

    return image_resized