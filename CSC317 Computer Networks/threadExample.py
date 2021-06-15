import time
import threading

val = (12, 34, 54, 65)

def sampleFunction():
    threads = [None]*4 # threads = []
    for i in range(1,5):
        val = (5*i)
        threads[i-1] = threading.Thread(target=print_10, args = [val])
        threads[i-1].start()

    for thread in threads:
        thread.join()
        
    print("main thread terminating.")

def print_10(num_iter):
    for i in range(num_iter):
        print(i, threading.current_thread().getName())

sampleFunction()
