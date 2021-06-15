#Nicholas Jonas
#10/16/2020
#Week 1 Assignment
#CSC355: Open Source Development
#This was my first attempt learn the Pillow library, the goal was to learn how
#composite photos worked and how to create a mask.
#I made this program during Week 0, but thought
#it would still be an important one to submit
from PIL import Image, ImageDraw


def firstComposite(imageOne, imageTwo):
    #Function to make a mask and use it for a composite and create a blend.
    mask = Image.new("L", imageOne.size,128)#the last number is obsfucation of the mask
    img = Image.composite(imageOne,imageTwo,mask)
    #img.save("LadyandCosmo.png")
    img.show()
#firstComposite
    

def secondComposite(imageOne, imageTwo):
    #Function to make a small rectangular mask for the composite.
    #and create a "window"
    mask = Image.new("L", imageOne.size, 0) #Another mask creation
    drawImage = ImageDraw.Draw(mask)
    drawImage.rectangle((500,1000,1500,2000),fill=255)
    #^draws a rectangle using a list of coordinates [x0, y0, x1, y1]
    img = Image.composite(imageOne,imageTwo,mask)
    #img.save("CosmoandLady.png")
    img.show()
#secondComposite


def main():
    #main function that opens the images and calls the functions.
    print("Hello World!")
    lady = Image.open("1.jpg") #My dog
    cosmo = Image.open("5.jpg") #My cat
    ladyW, ladyH = lady.size
    cosmoW, cosmoH = cosmo.size
    print("Widths: ",ladyW,cosmoW) #Checking dimensions
    print("Heights: ",ladyH,cosmoH)
    firstComposite(lady,cosmo)
    secondComposite(lady,cosmo)
#main
    

if __name__ == "__main__":
    main()
