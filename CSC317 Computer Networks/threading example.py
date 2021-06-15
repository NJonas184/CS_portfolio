import _thread
import time


def print_10():
    for i in range(10):
        print(i)
        time.sleep(1)


def main():
    print("Hello World!")
    test = _thread.start_new_thread(print_10())


if __name__ == "__main__":
    main()
