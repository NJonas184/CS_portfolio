# Quiz Question 1
# Nick Jonas
# CSC356 Machine Learning
# January 21, 2021

import numpy as np
import pandas as pd


def main():
    print("Hello World!")
    
    samples = [(2 * n, np.random.random()) for n in range(50)]#List comprehension


    data = np.array(samples) #np array

    print(data.shape)#Print rows and column #s
    print(data)#Print raw data

    table = pd.DataFrame(data, columns = ["evens", "random values"])
    print("\n------------\n")

    print(table.head(10))#Prints first 10 entrys in table
    print("\n------------\n")
    print(table.tail(10))#Prints last 10 entrys in table

    for column_name in table.columns:
        print(column_name)#Prints all column names

    print("\n------------\n")
    print(table.info())#Print information on table

    print("\n------------\n")

    print(table.describe())#Prints some statistics on table

#end of main()
    
    
if __name__ == "__main__":
    main()
#if()
