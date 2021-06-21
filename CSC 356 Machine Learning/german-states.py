
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split


def states():
    german_states = np.array( [
        ['Baden-Württemberg', 'Baden-Württemberg', 
            10624000, 35752, 'Stuttgart', 47290, 'old'],
        ['Bayern', 'Bavaria', 
            12563000, 70552, 'Munich', 48323, 'old'],
        ['Berlin', 'Berlin', 
            3415000, 892, 'Berlin', 41967, 'new'],
        ['Brandenburg', 'Brandenburg', 
            2449000, 29479, 'Potsdam', 29541, 'new'],
        ['Bremen', 'Bremen', 
            654800, 419, 'Bremen', 49215, 'old'],
        ['Hamburg', 'Hamburg', 
            1748000, 755, 'Hamburg', 66879, 'old'],
        ['Hessen', 'Hesse', 
            6040000, 21115, 'Wiesbaden', 46923, 'old'],
        ['Niedersachsen', 'Lower Saxony', 
            7792000, 47609, 'Hanover', 38423, 'old'],
        ['Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern', 
            1597000, 23180, 'Schwerin', 28940, 'new'],
        ['Nordrhein-Westfalen', 'North Rhine-Westphalia', 
            17564000, 34085, 'Düsseldorf', 39678, 'old'],
        ['Rheinland-Pfalz', 'Rhineland-Palatinate', 
            3993000, 19853, 'Mainz', 35457, 'old'],
        ['Saarland', 'Saarland', 
            992000, 2569, 'Saarbrücken', 36684, 'old'],
        ['Sachsen', 'Saxony', 
            4044000, 18416, 'Dresden', 31453, 'new'],
        ['Sachsen-Anhalt', 'Saxony-Anhalt', 
            2247000, 20446, 'Magdeburg', 28800, 'new'],
        ['Schleswig-Holstein', 'Schleswig-Holstein', 
            2820000, 15799, 'Kiel', 33712, 'old'],
        ['Thüringen', 'Thuringia', 
            2161000, 16172, 'Erfurt', 29883, 'new']] )

    column_names = ['German name', 'English name', 'population', 
        'area (km2)', 'capital', 'GRP (Euro)', 'old/new']


    df =  pd.DataFrame( german_states, columns = column_names )

    df['population'] = df['population'].astype(int)
    df['area (km2)'] = df['area (km2)'].astype(int)
    df['GRP (Euro)'] = df['GRP (Euro)'].astype(int)

    return df
# end of states()

def main():
    german_states = states()

    print( 'Herzlich Willkommen!' )

    # write code that ...


    # TO-DO: let's us look at the first few records in the dataset
    print(german_states.head())

    # TO-DO: let's us look at the last few records in the dataset
    print(german_states.tail())

    # TO-DO: tells us how many columns, how many rows
    print(german_states.info())

    # TO-DO: gives us some summary statistics
    print(german_states.describe())
    

    # TO-DO: replaces 'new' and 'old' with 0 and 1
    german_states["old/new"] = german_states["old/new"].replace({"new" : 0, "old" : 1})
    print(german_states.head())

    # TO-DO: replaces the population, area, and economy figures
    # with numbers on some standard scale
    
    german_states["population"] = ((german_states["population"] - np.min(german_states["population"]))
                                   /(np.max(german_states["population"]) - np.min(german_states["population"])))
    print(repr(german_states["area (km2)"]))
    german_states["area (km2)"] = ((german_states["area (km2)"] - np.min(german_states["area (km2)"]))
                                   /(np.max(german_states["area (km2)"]) - np.min(german_states["area (km2)"])))
    print(repr(german_states["area (km2)"]))
    german_states["GRP (Euro)"] = ((german_states["GRP (Euro)"] - np.min(german_states["GRP (Euro)"]))
                                   /(np.max(german_states["GRP (Euro)"]) - np.min(german_states["GRP (Euro)"])))
    print(repr(german_states["GRP (Euro)"]))
    
    # TO-DO: divides the dataset into a training set and a test set
    train, test = train_test_split(german_states, test_size = 0.2, random_state = 42, shuffle = True)

# end of main()

if __name__ == '__main__':
    main()
