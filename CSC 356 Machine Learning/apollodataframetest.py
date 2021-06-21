import numpy as np
import pandas as pd

def main():
    print("Hello World!")
    flights = ["apollo_7",
               "apollo_8",
               "apollo_9",
               "apollo_10",
               "apollo_11"]
    destinations = ["earth_orbit",
                    "lunar_orbit",
                    "earth_orbit",
                    "lunar_orbit",
                    "lunar_surface"]
    
    dictionary = {"flights" : flights,
                  "destinations" : destinations}

    missions = pd.DataFrame(dictionary)

    print(missions)

    df = pd.get_dummies(missions, prefix = "d", columns = ["destinations"])
    print(df)

if __name__ == "__main__":
    main()
