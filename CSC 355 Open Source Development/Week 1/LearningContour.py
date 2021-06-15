#Nicholas Jonas
#10/16/2020
#Week 1 Assignment
#CSC355: Open Source Development
#The goal of this program is to use the Contour image filter and blend in
#the original image to make something like Leon described in class.
from PIL import Image, ImageFilter, ImageEnhance


def main():
    #Main function that creates the contour photo and the unique one.
    print("Hello World!")

    lady = Image.open("images/flowers-wall.jpg")
    lady.reduce(2)
    ladyContour = lady.copy()
    ladyContour = ladyContour.filter(ImageFilter.CONTOUR) #Apply Contour filter
    ladyContour.show()
    #ladyContour.save("PIL_Photos/LadyContour.jpg") #Save the Image to have

    enhancer = ImageEnhance.Color(lady)
    lady = enhancer.enhance(0.3) #take out some of the color
    #lady.show()

    lady = Image.blend(lady,ladyContour, 0.4) #blend the images together
    lady.show()
    lady.save("PIL_Photos/watercolorFlowers.jpg")
#main
    

if __name__ == "__main__":
    main()
