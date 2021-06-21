import numpy as np
import pandas as pd


def main():
    print("Hello World!")
    #Data from 2010
    state_gpd = np.array([["Texas", 25145561, 1445266000],
                         ["California", 37253956, 2305213000],
                         ["Arizona", 6392017, 289829000],
                         ["Oregon", 3831074, 191362000],
                         ["Nevada", 2700551, 144435000],
                         ["New Mexico", 2059179, 981630000]])    

    column_names = ["States", "Population", "GDP"]

    df = pd.DataFrame(state_gpd , columns = column_names)
    df["Population"] = df["Population"].astype(int)
    df["GDP"] = df["GDP"].astype(float)

    print(repr(df))

    df["GDP/Person"] = df["GDP"]/df["Population"]

    print(repr(df))

if __name__ == "__main__":
    main()
