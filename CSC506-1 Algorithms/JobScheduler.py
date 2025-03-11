#Job scheduler created using python
#Said job scheduler will run different processes


class Process:
    #Class to handle process construction
    #TODO: Design other "processes" seperate from this file

    #Process features:
    #id = id of process
    #arrival_time = time of process arrival
    #burst_time = how long process takes to execute
    #deadline = how long (from process arrival) until process deadline
    def __init__(self, id, arrival_time, burst_time, deadline):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.deadline = deadline

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
    def __init__(self):
        self.processes = []
        self.gantt = []
        self.completed = {}

    def add_process(self, process):
        if isinstance(process, Process):
            self.processes.append(process)

    def FCFS(self):
        t=0
        #Sort by arrival
        self.processes.sort(key= lambda x: x.arrival_time)
        while self.processes != []:
            arrived = []
            for p in self.processes:
                temp = p.arrival_time
                if p.arrival_time <= t: #If proccess has "arrived"
                    arrived.append(p)
            if arrived == []:
                self.gnatt.append("Idle")
                t+= 1
                continue
            else:
                #Service next process
                process = arrived[0]
                self.gantt.append(process.id)


                t += process.burst_time
                process.deadline = process.deadline - t + process.arrival_time

                #Remove process from list
                self.processes.remove(process)
                self.completed[process.id] = (t, process.deadline)


    def EDF(self):
        t=0
        self.processes.sort(key= lambda x: x.arrival_time)
        while self.processes != []:
            #Boundary condition - if processes have "Arrived"
            arrived = []
            for p in self.processes:
                temp = p.arrival_time
                if p.arrival_time <= t: #If proccess has "arrived"
                    arrived.append(p)
            if arrived == []:
                self.gnatt.append("Idle")
                t+= 1
                continue
            else:
                #Service process with closest deadline'
                arrived.sort(key = lambda x: x.deadline)
                process = arrived[0]
                self.gantt.append(process.id)
                for p in arrived:
                    i = self.processes.index(p)
                    if p == process:
                        if p.burst_time-1 == 0:
                            #Process has finished, remove from list
                            self.processes.remove(process)
                            self.completed[process.id] = (t, process.deadline)
                        else:
                            #Record process time change and deadline decrease
                            self.processes[i].decrement(1, 1)
                    else:
                        #Record only deadline decrease
                        self.processes[i].decrement(deadline=1)
                t += 1

    def RoundRobin(self, time_quantum):
        t=0
        self.processes.sort(key= lambda x: x.arrival_time)

        while self.processes != []: #While self.processes is not empty
            #Boundary condition
            arrived = []
            for p in self.processes:
                temp  = p.arrival_time
                if p.arrival_time <= t: #If process arrival time is before current time
                    arrived.append(p)
            if arrived == []:
                self.gantt.append("Idle") #Note that cpu is idle
                t += 1
                continue
            else:
                #Service next process
                process = arrived[0]
                self.gantt.append(process.id) # append process id
                #Remove the process after serviced
                self.processes.remove(process)
                #Update the burst time
                remaining_burst = process.burst_time
                #Check if remaining burst was less than time quantum
                if remaining_burst <= time_quantum:
                    t += remaining_burst
                    process.deadline = process.deadline - t + process.arrival_time
                    self.completed[process.id] = (t, process.deadline)
                    continue
                else:
                    #If burst time > time time quantum (process not finished)
                    t += time_quantum
                    process.decrement(burst_time=time_quantum)
                    #Readd modified process to list
                    self.processes.append(process)


    def Greedy(self):
        t=0

        self.processes.sort(key= lambda x: x.arrival_time)

        while self.processes != []:
            #Boundary condition
            arrived = []
            for p in self.processes:
                if p.arrival_time <= t:
                    arrived.append(p)
            if arrived == []:
                gantt.append("Idle")
                t += 1
                continue
            else:
                #Sort for shortest burst time
                arrived.sort(key = lambda x: x.burst_time)
                process = arrived[0]
                #Service next process
                burst_time = process.burst_time
                process_id = process.id
                t += burst_time

                self.gantt.append(process_id)

                #Remove the process once done
                self.processes.remove(process)
                process.deadline = process.deadline - t + process.arrival_time
                self.completed[process_id] = (t, process.deadline)


def main():


    scheduler = JobScheduler()

    scheduler.add_process(Process("p1", 2, 6, 8))
    scheduler.add_process(Process("p2", 5, 2, 2))
    scheduler.add_process(Process("p3", 1, 8, 10))
    scheduler.add_process(Process("p4", 0, 3, 4))
    scheduler.add_process(Process("p5", 4, 4, 7))


    print("Please select one of the following:")
    print("1. FCFS")
    print("2. Greedy Algorithm (Modeled off of SJF)")
    print("3. Round Robin")
    print("4. EDF")
    while True:
        try:
            choice = int(input("Please choose from 1-4: "))
            if choice == 1:
                scheduler.FCFS()
                break
            elif choice == 2:
                scheduler.Greedy()
                break
            elif choice == 3:
                time_quantum = int(input("Please enter a time quantum: "))
                scheduler.RoundRobin(time_quantum)
                break
            elif choice == 4:
                scheduler.EDF()
                break
            else:
                print("Please enter number from specified range (1-4)")
        except:
            print("Error: Please enter valid option")

    #scheduler.RoundRobin(2)
    #scheduler.FCFS()
    scheduler.Greedy()
    print(scheduler.gantt)
    print(scheduler.completed)

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
