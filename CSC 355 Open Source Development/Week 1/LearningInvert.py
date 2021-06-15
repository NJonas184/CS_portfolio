#Nicholas Jonas
#10/16/2020
#Week 1 Assignment
#CSC355: Open Source Development
#The goal of this program was to create a negative/inverted image using Pillow.
import numpy as np
from PIL import Image


def main():
    #Nested for loop that changes the color values at each pixel.
    print("Hello World")
    copy = Image.open("6.jpg")
    lady = copy
    ladyW, ladyH =lady.size
    #pix = lady.load()
    #print(type(pix))

    for i in range(ladyW): #width
        for j in range(ladyH): #height
            pixel = lady.getpixel((i,j))
            #print(pixel)
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            newColor = (255-r,255-g,255-b) # modifying the pixel rgb values
            #Also have modified these values to see what each picture looks
            #like without r, g, or b
            # (255-r, 0, 255-b), (255-r, g, 255-b)are interesting ones
            lady.putpixel((i,j), newColor) # Places in new rgb values
    lady.show()
    copy.show()
    #lady.save("PIL_Photos/InvertedLady.jpg")
#main


if __name__ == "__main__":
    main()
