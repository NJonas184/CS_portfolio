#Round Robin Draft Algorithm
#Necessary inputs: Process list, time quantum
#Process should contain - [Arrival time, burst time, proccess id]
import threading
import itertools
import time


def RoundRobinHelper(self, iterable, name, time_quantum):
    t=0
    while True:
        lock.acquire()
        x = next(iterable, None)
        lock.release()
        if x is None:
            break
        print(f"{name}: {x.id}, {x.burst_time}")
        self.gantt.append([name, x.id])
        remaining_burst = x.burst_time
        if remaining_burst <= time_quantum:
            t += remaining_burst
            time.sleep(remaining_burst)
            x.deadline = x.deadline - t + x.arrival_time
            self.completed[x.id] = (t, x.deadline)
            continue
        else:
            t += time_quantum
            time.sleep(time_quantum)
            x.burst_time -= time_quantum
            lock.acquire()
            iterable = itertools.chain(iterable, [x])
            lock.release()
        time.sleep(0.1) #So threads don't collide
        '''
        else:
            self.gantt.append([name, "idle"])
            t += 1
            iterable = itertools.chain(iterable, [x])
            continue
        '''
    print(f"{name}: done")

def thread_helper(iterable, name, time_quantum):
    #Thread helper function for simulating process usage
    while (x := next(iterable, None)) is not None:
        print(f"{name}: {x[2]}, {x[1]}")
        time.sleep(time_quantum)
        if x[1] - time_quantum > 0:
            temp = [x[0], x[1]-time_quantum, x[2]]
            iterable = itertools.chain(iterable, [temp])
    print(f"{name}: done")


def RoundRobinThreaded(processes, processors=2, time_quantum=2):
    threads = []
    processes.sort()
    iter_process = iter(processes)
    #Turn the list of processes into an iterable for the threads
    print(processors)
    #Create variable number of threads
    for i in range(processors):
        temp = threading.Thread(target=thread_helper, args=(iter_process, f"t{i}", time_quantum)).start()
        threads.append(temp)

def RoundRobinT(self, time_quantum):
    threads = []
    self.processes.sort(key= lambda x: x.arrival_time)
    iter_processes = iter(self.processes)

    for i in range(self.processors):
        temp = threading.Thread(target=self.RoundRobinHelper, args=(iter_processes, f"t{i}", time_quantum))
        threads.append(temp)

    for x in threads:
        x.start()

    for thread in threads:
        thread.join()

    print(self.gantt)
    print(self.completed)


def RoundRobin(process_list, time_quantum):
    t= 0 #Time counter - using a misc unit in place of actual time
    gantt = [] #List processes being serviced, index = t stamps
    completed = {} #Completed processes
    process_list.sort()
    #Sorting to simulate recorded arrival time #NOTE: This will be unnecessary in a real system

    while process_list != []: #While process_list is not empty
        #Boundary condition
        arrived = []
        for p in process_list:
            temp  = p[0]
            if p[0] <= t: #If process arrival time is before current time
                arrived.append(p)
        if arrived == []:
            gantt.append("Idle") #Note that cpu is idle
            t += 1
            continue
        else:
            #Service next process
            process = arrived[0]
            gantt.append(process[2]) # append process id
            #Remove the process after serviced
            process_list.remove(process)
            #Update the burst time
            remaining_burst = process[1]
            #Check if remaining burst was less than time quantum
            if remaining_burst <= time_quantum:
                t += remaining_burst
                completed[process[2]] = t
                continue
            else:
                #If burst time > time time quantum (process not finished)
                t += time_quantum
                process[1] -= time_quantum
                #Readd modified process to list
                process_list.append(process)
    #Print out results
    print(gantt)
    print(completed)



def main():
    '''
    process_list = [[2,6,"p1"],[5,2,"p2"],[1,8,"p3"],[0,3,"p4"],[4,4,"p5"]]
    time_quantum = 2
    print(f"List of processes: {process_list}")
    print(f"Time Quantum: {time_quantum}")
    RoundRobin(process_list, time_quantum)
    '''

    process_list = [[2,6,"p1"],[5,2,"p2"],[1,8,"p3"],[0,3,"p4"],[4,4,"p5"]]
    RoundRobinThreaded(process_list, 2, 2)


if __name__ == "__main__":
    main()
