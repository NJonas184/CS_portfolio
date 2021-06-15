#Nicholas Jonas
#10/16/2020
#Week 1 Assignment
#CSC355: Open Source Development
#The goal of this program is to create a blurry photo with a sphere of clarity
#around my cat's head.
from PIL import Image, ImageDraw, ImageEnhance


def main():
    #Main function that executes the program
    print("Hello World!")
    
    cosmo = Image.open("5.jpg")
    cosmo.show()

    sharp = ImageEnhance.Sharpness(cosmo) #Using the image sharpness module
    print(type(contrast))
    sharp.enhance(-50.0).save("PIL_Photos/BlurryBoy.jpg")
    #^ less than 1.0 causes bluring, only very noticable below 0.0
    
    blur = Image.open("PIL_Photos/BlurryBoy.jpg") #Using the fully blurred photo
    mask = Image.new("L", cosmo.size, 0) #creating a new image for the mask
    draw = ImageDraw.Draw(mask)
    draw.ellipse((950,950,2200,2200), fill = 255)
    #^ drawing a circle around Cosmo's head
    img = Image.composite(cosmo, blur, mask)
    #^ Ensureing that the blur will be the majority
    #img.save("PIL_Photos/Blurwithmask.jpg")
    img.show()
#main


if __name__ == "__main__":
    main()
