import numpy as np
#import random

def main():
    print("Hello World!")
    students = ["Drak Twining", "Nicholas O'Keefe", "Nick Jonas", "Dan Heinsch"]

    #Shuffle the list with random library
    #random.shuffle(students)
    rng = np.random.default_rng()


    rng.shuffle(students)
    for i in students:
        print(i)
    
if __name__ == "__main__":
    main()
