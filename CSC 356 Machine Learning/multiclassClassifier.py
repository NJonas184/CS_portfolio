import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.svm import SVC
import pickle

#Training a multiclass classifier to
#recognize numbers from the mnist dataset.
def main():
    print("Hello World!")
    
    #fetching the information
    mnist = fetch_openml("mnist_784", version=1)

    #Fetching the data
    X, y = mnist["data"], mnist["target"]
    y = y.astype(np.uint8)
    X = X.to_numpy() #Premptive converting to numpy array

    #Splitting the data
    X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

    #The training will be a little different this time,
    #as a different classifier is being used.
    #The classifier below is a Support Vector Machine classifier,
    #which will be talked more about in Chapter 5.

    svm_clf = SVC()
    svm_clf.fit(X_train, y_train)
    #No need to distinguish any numbers like in the binary classifier

    #A quick demonstration of the classifier
    someDigit = X[0]
    someDigitImage = someDigit.reshape(28,28)

    print(f"The decision function was this: \n {svm_clf.decision_function([someDigit])}")
    print(f"The prediction is {svm_clf.predict([someDigit])}!")
    #The decision function will show how much the classifier believes the
    #image was each number 0 - 9
    
    plt.imshow(someDigitImage, cmap = "binary")
    plt.axis("off")
    plt.show()
    
    #This example might have used a SVM classifier, but it's entirely
    #possible to replicate these results using Stochastic Gradient Descent
    #or RandomForest classifiers
    #TODO: Try making a mnist classifier using one of the classifiers mentioned above.

    #All that's left is to plot out the images
    rows = 5 # number of rows
    cols = 2 # number of columns
    axes = [] # list to be plotted
    fig = plt.figure()

    for i in range(rows*cols):
        img = X_test[i] #Grab the image
        imgReshape = img.reshape(28, 28) # reshape the image
        axes.append(fig.add_subplot(rows, cols, i+1)) #Place image on 2D array
        subplot_title= f"{svm_clf.predict([img])}" #Create prediction title
        axes[-1].set_title(subplot_title) #Add title
        plt.imshow(imgReshape, cmap = "binary") #plot the image
        plt.axis("off")
    fig.tight_layout() #Conform to a specific layout
    plt.show() #Plot the images
        

    #Saving the model using pickle
    pickle.dump(svm_clf, open("SVMCLF.p", "wb"))
#End of main()


if __name__ == "__main__":
    main()
