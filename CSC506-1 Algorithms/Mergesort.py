import random


def Merge(array, left, right, mid):
    #Helper function
    #Establish sub arrays ranges
    n1 = mid-left+1
    n2 = right-mid

    #Create temp arrays
    L= [0] * (n1)
    R= [0] * (n2)

    #Copy data
    for i in range(0, n1):
        L[i] = array[left + i]

    for j in range(0, n2):
        R[j] = array[mid + 1 + j]

    #Index variables for subarray and merged array
    i = 0
    j = 0
    k = left

    #Merge arrays
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i+=1
        else:
            array[k] = R[j]
            j+=1
        k+=1

    #Copy remaining left elements if any
    while i < n1:
        array[k] = L[i]
        i+=1
        k+=1

    #Copy remaining right elements if any
    while j < n2:
        array[k] = R[j]
        j+=1
        k+=1


def MergeSort(array, left, right):
    if left < right:
        #Find middle
        mid = left+(right-left)//2

        #Sort halves
        MergeSort(array, left, mid)
        MergeSort(array, mid+1, right)
        Merge(array, left, right, mid)


def main():
    array = [i for i in range(1, 21)]
    random.shuffle(array)
    print(f"Before sorting: {array}")

    MergeSort(array, 0, len(array)-1)

    print(f"After sorting {array}")

if __name__ == "__main__":
    main()
