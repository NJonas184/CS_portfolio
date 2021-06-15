#Nicholas Jonas
#10/16/2020
#Week 1 Assignment
#CSC355: Open Source Development
#The goal of this program was to create an image quality similar to that of a
#"deep fried" image.
import numpy as np
from PIL import Image, ImageEnhance


def main():
    #Nested for loop that changes the color values at each pixel.
    print("Hello World")
    cosmo = Image.open("1.jpg")
    cosmoW, cosmoH =cosmo.size

    for i in range(cosmoW): #width
        for j in range(cosmoH): #height
            pixel = cosmo.getpixel((i,j))
            #print(pixel)
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if g >= 50: #reducing green beyond a point
                g = g-50
            if r <= 205: #increasing red below a point
                r = r+50
            newColor = (r,g,0) # modifying the pixel rgb values
            cosmo.putpixel((i,j), newColor) # Places in new rgb values
    cosmo.show()
    #cosmo.save("PIL_Photos/RedCosmo.jpg")
    
    contrast = ImageEnhance.Contrast(cosmo)
    cosmoCon = contrast.enhance(3.0)
    #upping the contrast to create distinction between colors

    bright = ImageEnhance.Brightness(cosmoCon)
    cosmoBright = bright.enhance(3.0)
    #upping the brightness to emphasize the bighter colors
    
    cosmoBright.show()
    #cosmoBright.save("PIL_Photos/DeepFriedCosmo2.jpg")
    
#main


if __name__ == "__main__":
    main()
