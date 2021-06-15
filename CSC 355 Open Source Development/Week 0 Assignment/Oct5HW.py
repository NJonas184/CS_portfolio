#Nicholas Jonas
import numpy as np
from PIL import Image
from numpy.random import default_rng #Numpy random generator Leon used
WIDTH = 512
HEIGHT = 512

class Point:
    """Class to create points on an image"""
    def __init__(self, x, y):
        """The constructor of the class"""
        self.x = x
        self.y = y
    #__init__

    def distance(self, otherPoint):
        """function to calculate the distance between 2 points"""
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y
        return np.sqrt(dx**2+dy**2)
    #distance()
    
    def __str__(self):
        """Returns the point as a string"""
        return f'(_{self.x:6.2f},_{self.y:6.2f})'
    #__str__

    
class Wave:
    """Class that creates sine waves"""
    def __init__(self, center, amplitude, wavelength, phase):
        """The constructor of the class"""
        self.center = center
        self.amplitude = amplitude
        self.wavelength = wavelength
        self.phase = phase
    #__init()__
        
    def height(self, point):
        """Calculates the height of a wave on a given point of the image"""
        r = point.distance(self.center)
        angle = 2.0 * np.pi * r/self.wavelength + self.phase
        return self.amplitude * np.sin(np.sqrt(angle)) #mess with this if you wanna get real weird
    #height()
    
class InterferingWaves:
    """Class that models a collection of waves that collide with each other"""
    def __init__(self):
        """The constructor of the class"""
        self.waves = list()
    #__init__()

    def addWaves(self, wave):
        """Adds waves to the image"""
        self.waves.append(wave)
    #addWaves()

    def height(self, point):
        """Sum of all the heights that meet at a certain point"""
        sum = 0.0
        for wave in self.waves:
            sum += wave.height(point)
        return sum
    #height()

class CoordinateSystem:
    """Creates the coordinate system so the image can be plotted/drawn"""
    def __init__(self, xMin, yMin, xMax, yMax):
        """"Constructor of the class"""
        self.xMin = xMin
        self.yMin = yMin
        self.xMax = xMax
        self.yMax = yMax
    #__init__()

    def normalize(self, point):
        """Method that ensures nothing is out of range of the drawing"""
        x = (point.x - self.xMin)/(self.xMax - self.xMin)
        y = (point.y - self.yMin)/(self.yMax - self.yMin)
        return(Point(x,y))
    #normalize()

    def scaleAndTranslate(self, point):
        """Given a point from the normalize() function,
        scale/translate it to the confines of the image"""
        x = self.xMin + point.x * (self.xMax - self.xMin)
        y = self.yMin + point.y * (self.yMax - self.yMin)
        return(Point(x,y))
    #scaleAndTranslate

#CoorinateSystem
class Transform:
    """Class allows for the transforming of one coordinate system into another"""
    def __init__(self, source, destination):
        """Constructor of the class"""
        self.source = source
        self.destination = destination
    #__init__()

    def map(self, point):
        """conversion of points given to points on the image"""
        n = self.source.normalize(point)
        return self.destination.scaleAndTranslate(n)
    #map
#Transform

def normalize(values):
    """Produces a numpy array of 8 bit unsigned
    integers from a numpy array of floats"""
    minimum = values.min()
    maximum = values.max()

    fun = lambda x : 256 * (x - minimum) / (maximum - minimum)

    return fun(values)
#normalize

def main():
    """Main function, executes all classes and initiates the program"""
    print("oh Hi Mark")

    amplitudes = np.zeros((WIDTH, HEIGHT))
    world = CoordinateSystem (-1.0, -1.0, +1.0, +1.0)
    device = CoordinateSystem (0, 0, WIDTH, HEIGHT)  

    device2world = Transform(device, world) 

    pattern = InterferingWaves()
    numberOfWaves = 20 #4
    radius = 4 #4
    cx = 0.0 #0.0
    cy = 0.0 #0.0

    rng = default_rng() #setting up rng

    for k in range(numberOfWaves):
        angle = 2.0 * np.pi * k / numberOfWaves
        x = cx + radius * np.cos(np.sqrt(angle))
        y = cy + radius * np.cos(angle)
        center = Point(x,y)

        wavelength = rng.exponential(2.0)

        wave = Wave(center, 1.0, wavelength ,0.0)

        pattern.addWaves(wave)

    for row in range (HEIGHT):
        for column in range(WIDTH):
            u = Point(column, row)
            v = device2world.map(u)
            h = pattern.height(v)
            amplitudes[row, column] = h

    normalizedAmplitudes = normalize(amplitudes).astype(np.uint8)


    """Only need a few colors, don't need to
    copy the entire dictionary of x11Colors"""
    colors = [(0x20, 0xb2, 0xaa),
               (0xff, 0xfa, 0xcd),
               (0x1e, 0x90, 0xff),
               (0xff, 0x6a, 0x6a)]
    #LightSeaGreen, LemonChiffon, DogderBlue, IndianRed


    colorSelection = np.zeros((WIDTH,HEIGHT,3), dtype = np.uint8)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            k = normalizedAmplitudes[j,i] % len(colors)
            colorSelection[i,j] = colors[k]
    
    print(normalizedAmplitudes.dtype)

    image = Image.fromarray(colorSelection, "RGB")
    image.show()
    image.save("coolpic.png") #Uncomment if you want to save it.
    
if __name__ == '__main__':
    main()
