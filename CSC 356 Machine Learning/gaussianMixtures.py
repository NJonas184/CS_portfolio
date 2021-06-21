import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from sklearn.datasets import make_blobs # Generate data for the gaussian mixtures
from sklearn.mixture import GaussianMixture


def plot_centroids(centroids, weights=None, circle_color='w', cross_color='k'):
    """"Plots the centroids of a clustering algorithm."""
    if weights is not None:
        centroids = centroids[weights > weights.max() / 10]
        
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='o', s=30, linewidths=8,
                color=circle_color, zorder=10, alpha=0.9)
    
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=50, linewidths=50,
                color=cross_color, zorder=11, alpha=1)
    
# End of plot_centroids()

def plot_gaussian_mix(gm, X, resolution = 1000, show_ylabels=True):
    """Plots a Gaussian Mixture."""
    mins = X.min(axis = 0) - 0.1
    maxs = X.max(axis = 0) + 0.1
    
    xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], resolution),
                         np.linspace(mins[1], maxs[1], resolution)) # finish generating x and y inputs
    
    z = -gm.score_samples(np.c_[xx.ravel(), yy.ravel()]) # Create z input
    z = z.reshape(xx.shape)

    plt.contourf(xx, yy, z, norm = LogNorm(vmin = 1.0, vmax = 30.0),
                 levels = np.logspace(0, 2, 12))

    plt.contour(xx, yy, z, norm = LogNorm(vmin = 1.0, vmax = 30.0),
                levels = np.logspace(0, 2, 12),
                linewidths=1, colors = "r", linestyles = "dashed")

    plt.plot(X[:, 0], X[:, 1], "k.", markersize = 2)
    plot_centroids(gm.means_, gm.weights_)

    plt.xlabel("$x_1$", fontsize = 14, rotation = 0)
    if show_ylabels:
        plt.ylabel("$x_2$", fontsize = 14, rotation = 0)
    else:
        plt.tick_params(labelleft = False)
# End of plot_gaussian_mix()


def main():
    print("Hello World!")

    x1, y1 = make_blobs(n_samples=1000, centers=((4, -4), (0, 0)), random_state=42)
    # Generate some blobs for data
    x1 = x1.dot(np.array([[0.374, 0.95], [0.732, 0.598]]))
    x2, y2 = make_blobs(n_samples=250, centers=1, random_state=42)
    X = np.r_[x1, x2]
    Y = np.r_[y1, y2]
    # Data generated!

    # Create the Gaussian Mixture Model
    gaussian = GaussianMixture(n_components = 3, n_init = 10)
    gaussian.fit(X) # Fitting the model

    # Printing some data
    print(f"weights = {gaussian.weights_}")

    print(f"covariances = {gaussian.covariances_}")

    print(f"means = {gaussian.means_}")

    print(f"iterations needed = {gaussian.n_iter_}")

    # Predicting using the previous dataset
    print(f"Prediction: {gaussian.predict(X)}\nProbabilities = {gaussian.predict_proba(X)}")

    # It is also possible to sample new instances, like so:
    Xnew, Ynew = gaussian.sample(10)
    print(f"Xnew = {Xnew}")

    print(f"Ynew = {Ynew}")

    # Estiamte the probability density function
    print(f"PDF = {gaussian.score_samples(X)}")

    # Numbers are cool, but it's also cool to look at them plotted out!
    # Fortunately, the jupyter notebook that came with the book had a
    # couple of neat function on how to plot out gaussian mixtures.
    # Check out plot_centroids and plot_gaussian_mix for the code.

    resolution = 1000

    plt.figure(figsize=(8, 4))

    plot_gaussian_mix(gaussian, X, resolution)
    plt.savefig("gaussian_mix_plot_example.png")

    plt.show()
    


if __name__ == "__main__":
    main()
