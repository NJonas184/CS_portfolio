#Job scheduler created using python
#Said job scheduler will run different processes
import threading
import time
import itertools
import os
import csv

lock = threading.Lock()

class Process:
    #Class to handle process construction
    #TODO: Design other "processes" seperate from this file

    #Process features:
    #id = id of process
    #arrival_time = time of process arrival
    #burst_time = how long process takes to execute
    #deadline = how long (from process arrival) until process deadline
    #Handled = will mark the thread as "hanedled" by a processors, only necessary for EDF
    #original_burst_time = keep track of unmodified burst time for analysis
    def __init__(self, id, arrival_time, burst_time, deadline):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.deadline = deadline
        self.handled = False
        self.original_burst_time = burst_time

    def decrement(self, deadline=0, burst_time=0):
        #Decrements burst time and deadline
        self.burst_time -= burst_time
        self.deadline -= deadline


class JobScheduler:
    #Class for Job Scheduler, will queue processes
    #Will have scheduling algorithms for Greedy(SJF), EDF, Round Robin and FCFS
    #processes = list of processes to be run
    #gantt = list for keeping track of processor activity
    #completed = dictionary keeping track of completed processes and timestamps
    #processors = amount of processors available for scheduler
    def __init__(self, processors):
        self.processes = []
        self.gantt = []
        self.completed = {}
        self.processors = processors

    def add_process(self, process):
        if isinstance(process, Process):
            self.processes.append(process)


    def FCFSHelper(self, iterable, name):
        t=0
        while True:
            lock.acquire()
            x = next(iterable, None)
            if x is None:
                lock.release()
                break
            if x.arrival_time > t:
                self.gantt.append([name,"Idle"])
                t+= 1
                iterable = itertools.chain([x], iterable)
                lock.release()
                time.sleep(1)
                continue
            else:
                print(f"{name}: {x.id}")
                self.gantt.append([name, x.id])
                t+=x.burst_time
                x.deadline = x.deadline - t + x.arrival_time
                self.completed[x.id] = (x.arrival_time, x.original_burst_time, t, x.deadline)
                lock.release()

                time.sleep(x.burst_time)

        print(f"{name}: done")

    def FCFS(self):
        threads = []
        self.processes.sort(key= lambda x: x.arrival_time)
        iter_processes = iter(self.processes)

        for i in range(self.processors):
            temp = threading.Thread(target=self.FCFSHelper, args=(iter_processes, f"t{i}"))
            threads.append(temp)

        for x in threads:
            x.start()

        for thread in threads:
            thread.join()

        print(self.gantt)
        print(self.completed)


    def Countdown(self, processes, name):
        t=0
        while True:
            if processes == [] or t > 50:
                break
            lock.acquire()
            arrived = []
            for p in processes:
                temp = p.arrival_time
                if p.arrival_time <= t and p.handled == False:
                    arrived.append(p)
            if arrived == []:
                t+=1
                lock.release()
                continue
            else:
                for i in arrived:
                    index = processes.index(i)
                    processes[index].decrement(deadline=1)
            lock.release()
            time.sleep(1)
            t+=1

    def EDFHelper(self, processes, name):
        t=0
        while True:
            if not processes:
                break
            lock.acquire()
            arrived = []
            for p in processes:
                temp = p.arrival_time
                if p.arrival_time <= t and p.handled == False:
                    arrived.append(p)

            if arrived == []:
                self.gantt.append([name,"Idle"])
                t+= 1
                lock.release()
                time.sleep(1)
                continue
            else:
                arrived.sort(key= lambda x: x.deadline)
                process = arrived[0]
                process.handled = True
                print(f"{name}: {process.id}, {process.burst_time}, {process.deadline}")
                self.gantt.append([name, process.id])
                for p in arrived:
                    index = processes.index(p)
                    if p == process:
                        if process.burst_time - 1 == 0:
                            processes.remove(process)
                            self.completed[process.id] = (process.arrival_time, process.original_burst_time, t+1, process.deadline)
                        else:
                            processes[index].decrement(burst_time=1, deadline=1)

            lock.release()
            time.sleep(1)
            process.handled = False
            t+=1



    def EDF(self):
        threads=[]
        self.processes.sort(key= lambda x: x.arrival_time)

        processes = list(self.processes)
        for i in range(self.processors):
            temp = threading.Thread(target=self.EDFHelper, args=(processes, f"t{i}"))
            threads.append(temp)

        time_keeper = threading.Thread(target=self.Countdown, args=(processes, "timer"))
        threads.append(time_keeper)
        for x in threads:
            x.start()

        for thread in threads:
            thread.join()

        print(self.gantt)
        print(self.completed)


    def RoundRobinHelper(self, processes, name, time_quantum):
        t=0
        while True:
            if not processes:
                break
            lock.acquire()
            arrived = []
            for p in processes:
                temp = p.arrival_time
                if p.arrival_time <= t and p.handled == False:
                    arrived.append(p)

            if arrived == []:
                self.gantt.append([name,"Idle"])
                t+= 1
                lock.release()
                time.sleep(1)
                continue
            else:
                arrived.sort(key= lambda x: x.deadline)
                process = arrived[0]
                process.handled = True
                print(f"{name}: {process.id}, {process.burst_time}, {process.deadline}")
                self.gantt.append([name, process.id])
                remaining_burst = process.burst_time
                if remaining_burst <= time_quantum:
                    t += remaining_burst
                    processes.remove(process)
                    process.deadline = process.deadline - t + process.arrival_time
                    self.completed[process.id] = (process.arrival_time, process.original_burst_time, t, process.deadline)
                    lock.release()
                    time.sleep(remaining_burst)

                    continue
                else:
                    for p in arrived:
                        index = processes.index(p)
                        if p == process:
                            processes[index].decrement(burst_time=time_quantum, deadline=0)
                    t += time_quantum
                    lock.release()
                    time.sleep(time_quantum)
                    process.handled= False
        print(f"{name}: done")




    def RoundRobin(self, time_quantum):
        threads = []
        self.processes.sort(key= lambda x: x.arrival_time)

        processes = list(self.processes)

        for i in range(self.processors):
            temp = threading.Thread(target=self.RoundRobinHelper, args=(processes, f"t{i}", time_quantum))
            threads.append(temp)

        for x in threads:
            x.start()

        for thread in threads:
            thread.join()

        print(self.gantt)
        print(self.completed)


    def GreedyHelper(self, processes, name):
        t=0
        while True:
            if not processes:
                break
            lock.acquire()
            arrived = []
            for p in processes:
                temp = p.arrival_time
                if p.arrival_time <= t:
                    arrived.append(p)

            if arrived == []:
                self.gantt.append([name,"Idle"])
                t+= 1
                lock.release()
                time.sleep(1)
                continue
            else:
                arrived.sort(key= lambda x: x.burst_time)
                process = arrived[0]
                t+=process.burst_time
                self.gantt.append([name, process.id])
                print(f"{name}: {process.id}, {process.burst_time}")
                self.completed[process.id] = (process.arrival_time, process.original_burst_time, t, process.deadline - t + process.arrival_time)
                processes.remove(process)
                lock.release()

                time.sleep(process.burst_time)
        print(f"{name} done")




    def Greedy(self):
        threads=[]
        self.processes.sort(key= lambda x: x.arrival_time)

        processes = list(self.processes)
        for i in range(self.processors):
            temp = threading.Thread(target=self.GreedyHelper, args=(processes, f"t{i}"))
            threads.append(temp)

        for x in threads:
            x.start()

        for thread in threads:
            thread.join()

        print(self.gantt)
        print(self.completed)


def load_data(filename):
    #Loads data to be used for the scheduler
    f = open(filename, "r")
    #First line is number of processors
    num_processors = int(f.readline())
    processes = []
    while True:
        process = f.readline()
        if not process:
            break
        temp = process.split(",")
        processes.append(Process(temp[0], int(temp[1]), int(temp[2]), int(temp[3])))
    return num_processors, processes

def main():

    filename = input("Please enter the file to be used as process samples: ")
    while True:
        if os.path.exists(filename):
            break
        else:
            filename = input("Please check file name and try again: ")

    processors, processes = load_data(filename)

    #Create scheduler
    scheduler = JobScheduler(processors)

    for process in processes:
        scheduler.add_process(process)

    print("Please select one of the following:")
    print("1. FCFS")
    print("2. Greedy Algorithm (Modeled off of SJF)")
    print("3. Round Robin")
    print("4. EDF")
    while True:
        algorithm = ""
        try:
            choice = int(input("Please choose from 1-4: "))
            if choice == 1:
                algorithm = "FCFS"
                scheduler.FCFS()
                break
            elif choice == 2:
                algorithm = "Greedy"
                scheduler.Greedy()
                break
            elif choice == 3:
                algorithm = "RoundRobin"
                time_quantum = int(input("Please enter a time quantum: "))
                scheduler.RoundRobin(time_quantum)
                break
            elif choice == 4:
                algorithm = "EDF"
                scheduler.EDF()
                break
            else:
                print("Please enter number from specified range (1-4)")
        except:
            print("Error: Please enter valid option")
            #print(e)

    keys = scheduler.completed.keys()
    with open(f"{processors}-{algorithm}-completed.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["process", "arrival time", "burst time", "time of completion", "deadline"])
        for key, value in scheduler.completed.items():
            writer.writerow([key, value[0], value[1], value[2], value[3]])

    '''
    scheduler.add_process(Process("p1", 1, 3, 7))
    scheduler.add_process(Process("p2", 0, 2, 5))
    scheduler.add_process(Process("p3", 5, 4, 5))
    scheduler.add_process(Process("p4", 6, 1, 2))
    scheduler.EDF()
    print(scheduler.gantt)
    print(scheduler.completed)
    '''

if __name__ == "__main__":
    main()
