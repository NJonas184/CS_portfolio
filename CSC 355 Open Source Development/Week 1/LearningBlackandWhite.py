#Nicholas Jonas
#10/16/2020
#Week 1 Assignment
#CSC355: Open Source Development
#The goal of this program was to fully convert an image to black and white.
#I recieved help from Cameron King on this program. 
from PIL import Image
import numpy as np


def main():
    #Main function that creates the black and white image.
    print("Hello World!")

    cosmo = Image.open("6.jpg")
    print(type(cosmo))
    grayC = cosmo.convert("L")
    grayC.show()

    arrayC = np.asarray(grayC).copy() #This is the part that Cameron helped with
    #.copy() needed because the array is read-only (Error I got)

    arrayC[arrayC < 128] = 0 #black
    arrayC[arrayC > 128] = 255 #white

    black_n_white_cosmo = Image.fromarray(arrayC) #Converts the array to an image
    black_n_white_cosmo.show()
    print(type(black_n_white_cosmo))
    #black_n_white_cosmo.save("PIL_Photos/blacknwhiteLady.jpg")
#main


if __name__ == "__main__":
    main()
