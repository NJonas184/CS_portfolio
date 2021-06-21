import matplotlib
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np


def main():
    print("Hello World!")

    npoints = 256
    angles = np.linspace(0.0, 2 * np.pi, npoints)

    for a in angles:
        print(f'{a:8.4f}')

    data = np.array(list(map(lambda x: (x, np.sin(x)), angles)))
    #for d in data:
    #    print(f'({d[0]:8.4f}, {d[1]:8.4f})')

    x = data[:,0]
    y = data[:,1]
    
    fig, ax = plt.subplots(figsize = (6,6))

    ax.set(
        xlabel = "x", #label x
        ylabel = "y", #label y
        title = "experiment" # title label
        )
    ax.grid() #Gets gridlines

    #ax.scatter(x,y, color = mcolors.to_rgb('indianred'), s = 128)
    ax.plot(x, y, linewidth = 40, color = mcolors.to_rgb("dodgerblue"))

    plt.show()
#end of main()


if __name__ == "__main__":
    main()
#if()
