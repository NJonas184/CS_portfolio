from sklearn.mixture import GaussianMixture
import numpy as np
import pandas as pd

def main():
    print("Hello World!")

    data = pd.read_csv("creditcard.csv")

    default = 1

    data = data.sample(frac = 0.2, random_state = default)

    
    # Create Gaussian
    gm = GaussianMixture(n_components=3, n_init=10)
    gm.fit(data)

    densities = gm.score_samples(data)
    density_threshold = np.percentile(densities, 4)
    anomalies = data[densities < density_threshold]

    print(f"{len(anomalies)}")


if __name__ == "__main__":
    main()
