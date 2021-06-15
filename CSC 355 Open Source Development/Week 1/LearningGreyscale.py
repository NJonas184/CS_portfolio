#Nicholas Jonas
#10/16/2020
#Week 1 Assignment
#CSC355: Open Source Development
#The goal of this program was to immitate Leon's greyscale program off of memory
#and notes.
import numpy as np
from PIL import Image, ImageDraw, ImageOps


def main():
    #Main function that turns a photo into it's greyscale version.
    print("Hello World!")
    lady = Image.open("1.jpg")
    ladyW, ladyH = lady.size
    print("Picture Mode: " + lady.mode) #checking the mode just out of curiosity
    lady.show()
    alt_lady = ImageOps.grayscale(lady).convert("RGB") #makes the greyscale photo

    maskData = np.zeros((ladyH, ladyW), dtype = np.uint8)
    maskData[:,(ladyW//2):] = 255 #dividing the photo in half
    mask = Image.fromarray(maskData, mode = "L")
    half = Image.composite(lady, alt_lady, mask)# half in color, half greyscale
    
    draw = ImageDraw.Draw(half)
    start = (ladyW // 2, 0)
    end = (ladyW // 2, ladyH) #sets ups a line
    fillColor = (0, 0, 0) #colors line black

    draw.line([start, end], fill = fillColor, width = 6)
    #^ create a line to divide the two different photos

    half.show()

    #half.save("GreyLady.jpg")#save the photo
#main



if __name__ == "__main__":
    main()
    
