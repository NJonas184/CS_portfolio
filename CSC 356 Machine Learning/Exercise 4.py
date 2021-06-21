import pandas as pd
import numpy as np

def main():
    print("Hello World!")

    nanExercise = np.random.randint(30, size = (10, 3))

    preGen = np.array([
        [12, 15, 15],
       [23,  np.nan, 25],
       [14, 17, 21],
       [np.nan,  np.nan, np.nan],
       [np.nan, 25,  1],
       [17, 29, 26],
       [ 5, 19,  np.nan],
       [ 9,  9,  2],
       [np.nan, np.nan,  5],
       [16,  5,  9]])



    print(repr(nanExercise))

    column_names = ["col 1", "col 2", "col 3"]
    
    df = pd.DataFrame(preGen, columns = column_names)


    print(repr(df))

    #How many nan in each col
    print(df.isna().sum())
    #How many nan in each row
    print(df.isnull().sum(axis=1))

    copyOne = df.copy()

    copyTwo = df.copy()

    



if __name__ == "__main__":
    main()
