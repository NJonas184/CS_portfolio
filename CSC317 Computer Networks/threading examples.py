from threading
import time

class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

def print10():
    for i in range(10):
        print(i)
        time.sleep(1)

def main():
    print("Hello World!")
    thread1 = MyThread()


if __name__ == "__main__":
    main()
