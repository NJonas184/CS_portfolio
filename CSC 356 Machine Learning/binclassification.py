import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import cv2
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier

#Training a binary classifier to recognize the number 7
def main():
    print("Hello World!")

    #fetching the information
    mnist = fetch_openml("mnist_784", version=1)
    #print out which keys are included
    print(mnist.keys())
    #Fetch the data
    X, y = mnist["data"], mnist["target"]
    y = y.astype(np.uint8)
    X = X.to_numpy()# Converts from pandas dataframe to a np array
    #Weird error I got, completely disrupted the program

    print(X.shape)
    print(type(X))
    
    X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

    #Picking one number to train the model on
    #Because the book chose to use number 5,
    #this example will demonstrate using the number 3
    yTrain3 = (y_train == 3) #True for only 3, false for all other numbers
    yTest3 = (y_test == 3)

    #Construct the classifier
    sgd_clf = SGDClassifier()
    #Demonstrating without random_state, so no reproducable results
    sgd_clf.fit(X_train, yTrain3) #Fitting the classifier

    for i in range(10):#Predict the first 10 numbers in X
        someDigit = X[i]
        someDigitImage = someDigit.reshape(28,28)
        
        print(sgd_clf.predict([someDigit]))#Prints the prediction
        plt.imshow(someDigitImage, cmap = "binary")
        plt.axis("off")
        plt.show()

    #Now that we have looked at images from the mnist dataset,
    #let's try looking at numbers from outside the dataset!
    #These numbers were made with MSPaint, and are naturally 28x28.
    #The images are as follows: 7, 2, 3, 7, 8.
    #Therefore, the predictions should be F,F,T,F,F!

    for j in range(1,5):
        img = cv2.imread(f"image{j}.png")[:,:,0]#Read the image using matplotlib
        bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        imgMod = np.resize(bw, (28,28,1))
        imgMod = np.array(imgMod)
        imgMod = imgMod.reshape(1,28,28,1)
        print(sgd_clf.predict(imgMod))#Prediction
        plt.imshow(img, cmap = "binary")#Plot the image
        plt.show()
        
#End of main()


if __name__ == "__main__":
    main()
