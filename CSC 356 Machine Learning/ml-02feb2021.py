
import matplotlib
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

import numpy as np

def scale_and_translate( min, max ):
    '''
    Create and return a function whose one
    argument is a number between -1.0 and +1.0
    and which returns to its caller a number between
    min and max.

    min is a floating point number
    max is a floating point number

    min < max

    return a function whose single argument
    is a number and which returns to its caller
    another number
    '''
    return lambda x: min + (max - min) * (x + 1)/2
# end of scale_and_translate()

def place_point( x_min, x_max, y_min, y_max ):
    '''
    Create a function that scales and translates
    the x and y coordinates of a point, given a
    tuple that contains those coordinates.


    Precondition: the point that the function
    scales and translates has x and y coordinates
    between -1.0 and +1.0.

    x_min is a floating point number
    x_max is a floating point number
    y_min is a floating point number
    y_max is a floating point number

    x_min < x_max
    y_min < y_max

    returns a function whose single argument is a tuple
    that contains 2 numbers and which returns to its caller
    another tuple that contains 2 numbers
    '''
    place_x = scale_and_translate( x_min, x_max )
    place_y = scale_and_translate( y_min, y_max )
    return lambda p: (place_x(p[0]), place_y(p[1]))
# end of place_point()

def points_in_unit_circle( number_of_points ):
    '''
    number_of_points is a positive integer

    return a list of tuples each of which contains
    the x and y coordinates of a point that lies
    within a circle of radius 1.0 whose center is
    at the origin.
    '''
    points = list()

    while len(points) < number_of_points:
        x, y = 2 * np.random.random(2) - 1
        if x * x + y * y <= 1.0:
            points.append( (x, y) )

    return points
# end of points_in_unit_circle()

def create_cluster( center, radius, number_of_points ):
    '''
    center is a tuple that contains 2 floating point numbers
    radius is a floating point number
    number_of_points is an integer

    return a list of tuples, each of which contains
    2 floating point numbers
    '''
    cx, cy = center

    x_min = cx - radius
    x_max = cx + radius

    y_min = cy - radius
    y_max = cy + radius

    points = points_in_unit_circle( number_of_points )

    transform = place_point( x_min, x_max, y_min, y_max )

    return np.array( list( map( transform, points ) ) )
# end of create_cluster()

def plot_dataset(a, b, c):
    # TO-DO: Rewrite this function so that it has
    # 3 parameters, each representing a different
    # cluster of points, and plots each cluster 
    # with a different color.

    # Collect the x coordinates of all of the points in samples.
    x = a[:, 0]
    # Collect the y coordinates of all of the points in samples.
    y = a[:, 1]

    # size of figure is expressed in inches
    fig, ax = plt.subplots( figsize = (6, 6) )
    # see the list of available named colors here:
    #     https://matplotlib.org/3.1.0/gallery/color/named_colors.html
    # the value of s determines the size of the dot in the plot
    
    
    ax.scatter( x, y, color = mcolors.to_rgb('indianred'), s = 16 )

    x = b[:, 0]
    y = b[:, 1]

    ax.scatter(x, y, color = mcolors.to_rgb("blue"), s =16)

    x = c[:, 0]
    y = c[:, 1]

    ax.scatter(x, y, color = mcolors.to_rgb("green"), s =16)
    
    ax.set(
        xlabel='x',
        ylabel='y',
        title='experiment')

    ax.grid()

    plt.show()
# end of plot_dataset()

def findCenter(cluster):
    """Finds the center of a given cluster."""
    x = cluster[:, 0]
    y = cluster[:, 1]
    # Add up contents and divide by members

    xSum = np.sum(x)
    ySum = np.sum(y)

    xEst = xSum / len(x)
    yEst = ySum / len(y)

    return np.array([xEst, yEst])
# end of findCenter()

def main():
    x_min = -1.0
    x_max = +1.0

    y_min = -1.0
    y_max = +1.0

    center = np.random.random( (3, 2) )

    print( '\n' )
    print( 'Centers of circles before transform:' )
    print( center )

    transform = place_point( x_min, x_max, y_min, y_max )

    center = list( map( transform, center ) )

    print( '\n' )
    print( 'Centers of circles after transform:' )
    print( center )

    n = 256

    a = create_cluster( (0.3, 0.4), 0.1, n )
    b = create_cluster( (-0.6, 0.5), 0.2, n )
    c = create_cluster( (0.5, -0.2), 0.2, n )

    all_points = np.concatenate( (a, b, c) )

    # TO-DO: Generate 3 random points. These
    # are the estimated centers of 3 clusters.


    # TO-DO: Write code that takes each point
    # in all_points, finds the nearest estimated
    # center, and points the point in a list of the
    # points that are closest to that estimated center.

    print( 'all_points shape = ', all_points.shape )

    aCenter = findCenter(a)
    bCenter = findCenter(b)
    cCenter = findCenter(c)
    print(f"Estimated center of a: {aCenter}")
    print(f"Estimated center of b: {bCenter}")
    print(f"Estimated center of c: {cCenter}")

    # TO-DO: Call the revised plot_dataset to plot
    # 3 groups of points, each in a different color.
    plot_dataset(a, b, c)
# end of main()

if __name__ == '__main__':
    main()
