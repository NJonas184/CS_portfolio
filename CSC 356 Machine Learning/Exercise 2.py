import numpy as np

#Goal: find a polynomial of degree 3 that passes through any given 4 points
#Use Lagrange

def print_vector(v):
    print(f"({v[0]:6.2f}, {v[1]:6.2f})")

def lagrange(x, points):
    xs = points[:,0]
    ys = points[:,1]

    #if x == xs[0], then f0 = ys[0]
    f0 = (ys[0] *
          (x - xs[1])/(xs[0] - xs[1]) *
          (x - xs[2])/(xs[0] - xs[2]) *
          (x - xs[3])/(xs[0] - xs[3]))

    f1 = (ys[1] *
          (x - xs[0])/(xs[1] - xs[0]) *
          (x - xs[2])/(xs[1] - xs[2]) *
          (x - xs[3])/(xs[1] - xs[3]))

    f2 = (ys[2] *
          (x - xs[0])/(xs[2] - xs[0]) *
          (x - xs[1])/(xs[2] - xs[1]) *
          (x - xs[3])/(xs[2] - xs[3]))
    
    f3 = (ys[3] *
          (x - xs[0])/(xs[3] - xs[0]) *
          (x - xs[1])/(xs[3] - xs[1]) *
          (x - xs[2])/(xs[3] - xs[2]))
    return f0 + f1 + f2 + f3

def main():
    print("Hello World")
    
    p0 = np.random.random_sample(2)
    print_vector(p0)
    p1 = np.random.random_sample(2)
    print_vector(p1)
    p2 = np.random.random_sample(2)
    print_vector(p2)
    p3 = np.random.random_sample(2)
    print_vector(p3)

    print("\n")

    points = np.random.random_sample((4,2))
    for i in points:
        print_vector(i)

    print(f'at point 0, lagrange = {lagrange(points[0,0], points):6.2f}')
    print(f'at point 1, lagrange = {lagrange(points[1,0], points):6.2f}')
    print(f'at point 2, lagrange = {lagrange(points[2,0], points):6.2f}')
    print(f'at point 3, lagrange = {lagrange(points[3,0], points):6.2f}')
    



if __name__ == "__main__":
    main()
