import random

def main():
    array = [i for i in range(1, 101)]
    key = int(input("Please input a number from 0-100 (0 is worst case)"))

    while True:
        if 0 <= key <= 100:
            break
        else:
            key = int(input("Please input a number from 0-100 (0 is worst case)"))

    random.shuffle(array)

    answer = -1

    for i in range(len(array)):
        if array[i] == key:
            answer = i
            break
    print(answer)


if __name__ == "__main__":
    main()
