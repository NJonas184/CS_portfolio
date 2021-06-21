import pickle

def unpickle(file):
    with open(file, 'rb') as fo:
        cifar_dict = pickle.load(fo, encoding='bytes')
    return cifar_dict


def main():
    print("Hello World!")

    cifar = unpickle("cifar-10-python.tar.gz")


if __name__ == "__main__":
    main()
