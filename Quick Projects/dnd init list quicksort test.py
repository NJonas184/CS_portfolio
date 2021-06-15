
def addToInitiative(initDict, key, value):
    if key in initDict.keys():
        if type(initDict[key]) == tuple:
            print("It's a tuple")
            temp = list(initDict[key])
            temp.append(value)
            initDict[key] = tuple(temp)
        else:
            print("Creating Tuple")
            initDict[key] = (initDict[key], value)
    else:
        print("Adding initiative")
        initDict[key] = value


def partition(arr, l, h):
    i = (l - 1)
    p = arr[h]

    for j in range(l, h):
        if isinstance(arr[j], int) == True and isinstance(p, int) == True:
                if arr[j] > p:

                    i = i + 1
                    arr[i],arr[j] = arr[j],arr[i]
        elif arr[j] == "nat20" or p == "nat1":
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return(i+1)




def quickSort(arr, l, h):
    if l < h:
        pi = partition(arr, l, h)

        quickSort(arr, l, pi-1)
        quickSort(arr, pi+1, h)

def finishInitHelper(initTup):
    print(f"recursion = {initTup}")
    tempList = list(initTup)
    tempDict = {}
    n = len(tempList)
    if n > 1:
        for j in range(n):
            a = int(input(f"Enter new roll for {tempList[j]}: "))
            addToInitiative(tempDict, a, tempList[j])
            tempList[j] = a

        print(tempDict)
        finalList = []
        if len(tempDict.keys()) < n:
            for k in tempDict.keys():
                if isinstance(initTup, tuple) == True:
                    finalList = finishInitHelper(tempDict[k])
            print(f"Unsorted1 = {finalList}")
            quickSort(finalList, 0, n-1)
            print(f"Sorted = {finalList}")
            for i in range(n):
                finalList[i] = finalList[i]
            return finalList
        else:
            finalList = tempList
            print(f"Unsorted2 = {finalList}")
            quickSort(finalList, 0, n-1)
            print(f"Sorted = {finalList}")
            for i in range(n):
                print(tempDict[finalList[i]])
                finalList[i] = tempDict[finalList[i]]
            print(f"Final list = {finalList}")
            return finalList
    else:
        return tempList
    
    

   
def finishInitiative(initList, initDict):
    temp = []
    for i in initList:
        if isinstance(initDict[i], tuple) == False:
            temp.append(initDict[i])
        else:
            tempList = finishInitHelper(initDict[i])

            print(f"extending  = {tempList}")
            
            temp.extend(tempList)
        print(temp)
    return temp
            
            


def main():
    print("Hello World")

    initiativeDict ={
        122423 : ("Vellah"),
        20 : ("Chad"),
        1 : ("Goblin1"),
        "nat1" : ("Garfield", "The Tarrasque running from Toryc"),
        "nat20" : ("Toryc"),
        17 : ("A very scary Lich")
}

    addToInitiative(initiativeDict, 14, "Goblin2")
    addToInitiative(initiativeDict, 17, "Crab1")
    addToInitiative(initiativeDict, "nat1", "Gremlin")
    
    initiative = []
    for k, v in initiativeDict.items():
           initiative.append(k)
           print(f"{k} : {v}")
           print(type(v))


    print("\nInitiative sorting")
    n = len(initiative)
    quickSort(initiative, 0, n-1)

    for i in range(n):
        print(initiative[i])

    print("Finishing initiative:")
    initiative = finishInitiative(initiative, initiativeDict)


    

if __name__ == "__main__":
    main()

