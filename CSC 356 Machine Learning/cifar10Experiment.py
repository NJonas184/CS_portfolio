import tensorflow as tf
from tensorflow.keras import layers, datasets
import matplotlib.pyplot as plt

def createLeNet(input_shape):
    model = tf.keras.Sequential()

    model.add(layers.Conv2D(120, kernel_size = (5, 5), strides = 1, activation = "tanh", input_shape = input_shape))
    model.add(layers.AveragePooling2D(pool_size = (5,5), strides = 2))
    model.add(layers.Conv2D(16, kernel_size = (5, 5), strides = 1, activation = "tanh"))
    model.add(layers.AveragePooling2D(pool_size = (14, 14), strides = 2))
    model.add(layers.Conv2D(6, kernel_size = (5, 5), strides = 1, activations = "tanh"))

    model.add(layers.Flatten())
    model.add(layers.Dense(10, activation = "softmax"))

    return model
    


def main():
    print("Hello World!")

    img_shape = (32, 32, 3) # Shape of images

    (X_train, Y_train), (X_test, Y_test) = datasets.cifar10.load_data()
    print(X_train.shape)
    print(Y_train.shape)

    LeNet = createLeNet(img_shape)

    

    

if __name__ == "__main__":
    main()
