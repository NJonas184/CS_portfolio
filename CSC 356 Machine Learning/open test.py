import os
import pickle

def main():
    print("Hello World!")
    cifarDir = "cifar10dataset"
    dataDir = "cifar-10-batches-py"
    start = os.path.join(cifarDir, dataDir)
    end = os.path.join(start, "data_batches_1")
    


if __name__ == "__main__":
    main()
