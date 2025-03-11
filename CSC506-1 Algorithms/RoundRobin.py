#Round Robin Draft Algorithm
#Necessary inputs: Process list, time quantum
#Process should contain - [Arrival time, burst time, proccess id]


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
    process_list = [[2,6,"p1"],[5,2,"p2"],[1,8,"p3"],[0,3,"p4"],[4,4,"p5"]]
    time_quantum = 2
    print(f"List of processes: {process_list}")
    print(f"Time Quantum: {time_quantum}")
    RoundRobin(process_list, time_quantum)


if __name__ == "__main__":
    main()
