#Nicholas Jonas
#10/16/2020
#Week 1 Assignment
#CSC355: Open Source Development
#The goal of this program is to create a reusable mask/filter and use it in
#an example.
import numpy as np
from PIL import Image


def makeFade(start, stop, width, height, isHorizontal):
    #Function that equally arranges input arrays on the filter.
    if isHorizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T
#makeFade


def makeFadeFilter(startList, stopList, width, height, isHorizontalList):
    #Function that calls the makeFade function multiple times
    #and returns the result as an np.float array.
    result = np.zeros((height, width, len(startList)), dtype =np.float)

    for i, (start, stop, isHorizontal) in enumerate(zip(startList, stopList, isHorizontalList)):
        result[:,:, i] = makeFade(start, stop, width, height, isHorizontal)
        #puts the result of the makeFade function in the 3rd dimension of result

    return result
#makeFadeFilter

    
def main():
    #Executes all functions and creates the test image using the newly crafted mask.
    print("Hello World!")
    lady = Image.open("1")
    ladyW, ladyH = lady.size
    fade = makeFadeFilter((0,0,0), (255,255,255), ladyW, ladyH, (True,True,True))
    #^ creation of the mask using the other two functions
    fMask = Image.fromarray(np.uint8(fade))#turns the new filter into a mask
    #fMask.save("FadeFilter.jpg") 
    fMask = Image.open("FadeFilter.jpg").convert("L")
    cosmo = Image.open("5.jpg")
    img = Image.composite(cosmo,lady, fMask)
    img.show()
    #img.save("PIL_Photos/FadeFilterExample.jpg")
#main


#Guide used: https://note.nkmk.me/en/python-numpy-generate-gradation-image/


if __name__ == "__main__":
    main()
