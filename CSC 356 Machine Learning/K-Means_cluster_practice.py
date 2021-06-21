import numpy as np

def cluster(center, radius, theta):
    """Give a list of points that lie within a circle."""

    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return np.concatenate((x, y), axis = None)

def main():

    print("Hello World!")

    #Create circles
    circ1, circ2 = np.random.randn(2,2)

    theta = np.random.normal(0,1,1)

    r = 6 * np.random.normal(0,1,1)

    print(circ1, circ2)

    point1 = cluster(circ1, r, theta)
    print(point1)



if __name__ == "__main__":
    main()
