#Nicholas Jonas
#10/16/2020
#Week 1 Assignment
#CSC355: Open Source Development
#The goal of this program was to use two enhancements on one photo. The first
#enhancement was saved just for comparison.
from PIL import Image, ImageEnhance


def main():
    #Main function that executes the two image enhancements.
    print("Hello World!")

    cosmo = Image.open("5.jpg")
    cosmo.show()

    contrast = ImageEnhance.Contrast(cosmo)
    newImage = contrast.enhance(3.0)
    newImage.save("PIL_Photos/contrastExample.jpg") #Adds contrast

    #newImage = Image.open("PIL_Photos/contrastExample.jpg")
    bright = ImageEnhance.Brightness(newImage)
    bright.enhance(3.0).save("PIL_Photos/ContrastandBrightness.jpg")
    #adds brightness
#main
    

if __name__ == "__main__":
    main()
