import matplotlib.pyplot as plt
import matplotlib.image as mping
import numpy as np



def normalizeHelper(r, g, b):
    """Normalizes rgb values between 0-255.

        Parameters:
                r (numpy.ndarray) : r value of to-be-normalized array
                g (numpy.ndarray) : g value of to-be-normalized array
                b (numpy.ndarray) : b value of to-be-normalized array
        Returns:
                rgb (numpy.ndarray) : The normalized array
    """

    #Normalize the values
    r = 255 * ((r - np.min(r))/(np.max(r) - np.min(r)))
    g = 255 * ((g - np.min(g))/(np.max(g) - np.min(g)))
    b = 255 * ((b - np.min(b))/(np.max(b) - np.min(b)))
    #TODO: Is there another easier way to normalize all of these values?
    
    #Combine the rgb values into an np array with unsigned int8 type
    rgb = np.dstack((r,g,b)).astype(np.uint8)
    return rgb
#Inspiration: https://stats.stackexchange.com/questions/281162/scale-a-number-between-a-range/281164
#End of normalizeHelper()


def frankenPhoto(img1, img2):
    """Combines two photos by multiplying matrices of their rgb values.

        Parameters:
                img1 (numpy.ndarray) : An array that can be plotted as a photo.
                img2 (numpy.ndarray) : An array that can be plotted as a photo.
        Returns:
                frankenstein (numpy.ndarray) : A normalized array
    """

    r1 = img1[:,:,0]#Grabbing all r values from img1
    g1 = img1[:,:,1]#Grabbing all g values from img1
    b1 = img1[:,:,2]#Grabbing all b values from img1

    r2 = img2[:,:,0]#Grabbing all r values from img2
    g2 = img2[:,:,1]#Grabbing all g values from img2
    b2 = img2[:,:,2]#Grabbing all b values from img2

    rFrank = np.matmul(r1, r2)#Matrix multiplication of both r values
    gFrank = np.matmul(g1, g2)#Matrix multiplication of both g values
    bFrank = np.matmul(b1, b2)#Matrix multiplication of both b values

    #Normalize these values and combine them
    frankenstein = normalizeHelper(rFrank, gFrank, bFrank)
    #TODO: Is there another way to combine these values
    #while keeping them within 0-255

    print("returning")
    return frankenstein
#End of frankenPhoto()


def generateStaticImage():
    """Generates static by combining matrixes.

        Returns:
            rgb (numpy.ndarray) : An array that can be plotted as a photo.
    """
    n = (512, 512)# Image size

    #Random matrixes calculated for each color
    r = np.random.randint(256, size= n)
    b = np.random.randint(256, size= n)
    g = np.random.randint(256, size= n)
    #TODO: Experiment with other random modules,
    #Maybe more unique static patterns can be found.

    
    print(repr(r))#Print out the arrays in a clear format
    #print(repr(b))
    #print(repr(g))

    #Stacks the matrixes together and asigns the
    #Unsigned int8 data type for easy conversion
    #to photo
    rgb = np.dstack((r,g,b)).astype(np.uint8)


    print(repr(rgb))
    #TODO: Try to find another way to clearly print
    #out this np.array()
    

    
    plt.imshow(rgb)
    #plot the image
    plt.show()
    return rgb#Return the image
#End of generateStaticImage()


def convertToGrayscale(img):
    """Converts a rgb photo to grayscale.

        Paremeters:
                img (numpy.ndarray) : An array that can be plotted as a photo.
        Returns:
                gray ()
    """
    gray = np.dot(img[...,:3], [0.299, 0.587, 0.144])
    #Modifies the rgb values of the img by using
    #values found on Wikipedia
    #TODO: What other values can be used to convert a
    #photo to grayscale? Do the work better?
    

    plt.imshow(gray, cmap = plt.get_cmap('gray'))
    #plot the image

    plt.savefig('Lady Grayscale.png')#Save the image
    plt.show()
    #Inspiration 0: https://moonbooks.org/Articles/How-to-convert-an-image-to-grayscale-using-python-/
    #Inspiration 1: https://en.wikipedia.org/wiki/Grayscale
    return gray #Return the image
#End of convertToGrayscale()


def main():
    """Main method of the program."""
    print("Hello World!")

    lady = mping.imread("ladySmall.png")
    cosmo = mping.imread("cosmoSmall.png")

    
    grayLady = convertToGrayscale(lady)

    #grayCosmo = convertToGrayscale(cosmo)

    staticImg = generateStaticImage()

    frankenImage = frankenPhoto(lady, cosmo)

    plt.imshow(frankenImage)
    plt.show()

    plt.savefig("Frankenstein.png")
#End of main()


if __name__ == "__main__":
    main()
#if()
