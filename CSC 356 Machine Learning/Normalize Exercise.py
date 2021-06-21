import matplotlib
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#TODO: write code that tests normalize()

def normalize(v):
    return v / np.linalg.norm(v)
#end of normalize()

def vector_to_string(v):
    return f'({v[0]:6.2}, {v[1]:6.2f})'

def printVectors(vectors):
    for v in vectors:
        print(vector_to_string(v))
#end of printVectors()

def random_vector():
    v = normalize(np.random.random_sample(2))
    print(f"type = {type(v)}")
    print(f"shape = {v.shape}")
    print(f"magnitude = {np.linalg.norm(v)}")
    return v
#end of random_vector()

def point_near_line(distance, p0, v, stddev):
    point_on_line = p0 + distance * v

    x = point_on_line[0]
    y = point_on_line[1]

    y = y + np.random.normal(0.0, stddev)
    return np.array((x, y))
# end of point_near_line()

def plot_dataset(samples, line_segment):
    x = samples[:, 0]
    y = samples[:, 1]

    fig, ax = plt.subplots(figsize = (6,6))
    #TODO: Experiment with different colors
    #and sizes for dots. Find a list of permitted names for colors
    ax.scatter(x, y, color = mcolors.to_rgb("indianred"), s =16)
    #TODO: change labels on the coordinate axes and the diagram
    ax.set(
        xlabel = "x",
        ylabel = "y",
        title = "experiment")
    ax.grid()

    s0 = line_segment[0]
    s1 = line_segment[1]

    x0 = s0[0]
    y0 = s0[1]

    x1 = s1[0]
    y1 = s0[1]
    #TODO: Experiment with line colors
    plt.axline((x0, y0), (x1, y1), linewidth=4.0,
               color = mcolors.to_rgb("red"))
    plt.show()
#end of plot_dataset()

    
def main():
    print("Hello World!")
    #TODO: Experiment with different npoints
    npoints = 64

    p0 = random_vector()
    v = random_vector()

    distances = 2.0 * np.random.random_sample(npoints) - 1.0
    distances.sort()

    #TODO: Experiment wiht different stddev values
    stddev = 0.2
    iterator =  map(lambda d: point_near_line(d, p0, v, stddev), distances)
    points = np.array(list(iterator))
    #TODO: Experiment with slices of numpy program
    #Write a short program for this experiment
    #What happens if you put anumber on one side of the colon, on both sides?
    x = points[:,0]
    y = points[:,1]
    #TODO: Which methods of LinearRegression does this program call?
    model = LinearRegression()

    #TODO: Learn what numpy's reshape() function does
    #Write a short program to show what this function does
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    #TODO: Does the shape of a numpy array put the number of rows first or the number columns?
    print(type(x))
    print(x.shape)
    print(type(y))
    print(y.shape)

    model.fit(x,y)
    #TODO: The fit() method computes two values
    #How should we interpret these values, how might we use them?

    print(model.intercept_)
    print(model.coef_)

    x0 = points[0,0]
    x1 = points[-1,0]

    endpoints = np.array((x0, x1))
    endpoints = endpoints.reshape(-1, 1)

    print(f"endpoints type = {type(endpoints)}")
    print(f"endpoints shape = {endpoints.shape}")

    ys = model.predict(endpoints)

    #TODO: Learn what flatten does
    ys = ys.flatten()

    print(ys)
    y0 = ys[0]
    y1 = ys[1]
    print(f"y0 = {y0}")
    print(f"y1 = {y1}")

    line_segment = ((x0, y0),(x1, y1))
    plot_dataset(points, line_segment)


if __name__ == "__main__":
    main()
