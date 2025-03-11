

class Empty:
    #Adding empty class because "None" wouldn't work
    #Empty class allows for distinguishing between two different empty statuses?
    pass


class HashTable():
    #This will be a Quadratic Hashing Table

    def __init__(self, size=10, c1=1, c2=1):
        #Init function: default size will be 10
        #Constants will be initialized to 1 if no input specified

        #Creating distinctions
        self.empty_since_start = Empty()
        self.empty_after_removal = Empty()

        #Creating table using list
        self.table = [self.empty_since_start] * size

        self.c1 = c1
        self.c2 = c2

        self.load_factor = 0.0

    def CalculateLoadFactor(self):
        count = 0
        for key in self.table:
            if type(key) is not Empty:
                count+= 1
        self.load_factor = count / len(self.table)


    def insert(self, key):
        #Insert function using Quadratic probing, returns nothing
        if self.load_factor >= 0.5:
            self.Resize()
        i=0
        while i < len(self.table):
            bucket = (hash(key) + self.c1 * i + self.c2 * i**2) % len(self.table)
            if type(self.table[bucket]) is Empty:
                self.table[bucket] = key
                break
            i+=1
        self.CalculateLoadFactor()

    def remove(self, key):
        #Remove function using Quadratic probing, returns nothing
        i=0
        bucket = (hash(key) + self.c1 * i + self.c2 * i**2) % len(self.table)
        while self.table[bucket] is not self.empty_since_start and i < len(self.table):
            bucket = (hash(key) + self.c1 * i + self.c2 * i**2) % len(self.table)
            if self.table[bucket] == key:
                self.table[bucket] = self.empty_after_removal
                break

            i+=1

    def search(self, key):
        #Search function using Quadratic probing, returns bucket contents or None if not present in table
        i=0
        bucket = (hash(key) + self.c1 * i + self.c2 * i**2) % len(self.table)
        while self.table[bucket] is not self.empty_since_start and i < len(self.table):
                bucket = (hash(key) + self.c1 * i + self.c2 * i**2) % len(self.table)
                if self.table[bucket] == key:
                    return self.table[bucket]

                i+=1
        return None

    def ResizeInsert(self, newArray, key):
        #Insert function for Resize
        i=0
        while i < len(newArray):
            bucket = (hash(key) + self.c1 * i + self.c2 * i**2) % len(newArray)
            if type(newArray[bucket]) is Empty:
                newArray[bucket] = key
                break
            i+=1


    def Resize(self):
        #Resizing to double the current HashTable size
        #Doing this instead of next prime number of doulbe table size for the sake of simplicity
        new_size = len(self.table) * 2

        new_table = [self.empty_since_start] * new_size

        bucket = 0
        while bucket < len(self.table):
            if self.table is not Empty:
                key = self.table[bucket]
                self.ResizeInsert(new_table, key)
            bucket += 1
        self.table = new_table



    def __str__(self):
        #Practicing good habits
        s= ""
        i = 0
        for bucket in self.table:
            if bucket is self.empty_since_start:
                key = "empty_since_start"
            elif bucket is self.empty_after_removal:
                key = "empty_after_removal"
            else:
                key = bucket

            s += f"index = {i}, key = {key}\n"
            i+= 1
        return s


def main():
    print("Hello World!")
    h = HashTable()
    h.insert(50)
    h.insert(40)
    h.insert(35)

    print(h)


    h.insert(45)
    h.insert(55)
    h.insert(100)


    print(h)
    h.remove(100)
    print(h)

    print(h.search(45))
    print(h.search(100))


if __name__ == "__main__":
    main()
