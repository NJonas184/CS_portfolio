# EDF Draft Algorithm
# Necessary inputs: Process list
# Process should contain - [Arrival time, burst time, deadline (from current time), process id]


def EarliestDeadlineFirst(process_list):
    t=0 #time counter to mimic actual time
    gantt = [] #List order of processes being serviced
    completed = {} #Completed processes
    process_list.sort()
    #Sorting process list to simulate recorded arrival time #NOTE: This will be unnecessary in real version

    while process_list != []:
        #Boundary condition - if processes have "Arrived"
        arrived = []
        for p in process_list:
            temp = p[0]
            if p[0] <= t: #If proccess has "arrived"
                arrived.append(p)
        if arrived == []:
            print("Idle")
            gnatt.append("Idle")
            t+= 1
            continue
        else:
            #Service process with closest deadline'
            arrived.sort(key = lambda x: x[2])
            process = arrived[0]
            gantt.append(process[3])
            for p in arrived:
                i = process_list.index(p)
                if p == process:
                    if p[1]-1 == 0:
                        #Process has finished, remove from list
                        process_list.remove(process)
                        completed[process[3]] = (t, p[2])
                    else:
                        #Record process time change and deadline decrease
                        process_list[i] = [p[0], p[1]-1, p[2]-1, p[3]]
                else:
                    #Record only deadline decrease
                    process_list[i] = [p[0], p[1], p[2]-1, p[3]]
            t += 1
    print(gantt)
    print(completed)


def main():
    #process_list = [[1, 3, 7, "p1"], [0, 2, 5, "p2"], [5, 4, 5, "p3"], [6, 1, 2, "p4"]]
    process_list = [[2, 6, 8, "p1"], [5, 2, 2, "p2"], [1, 8, 10, "p3"], [0, 3, 4, "p4"], [4, 4, 7, "p5"]]
    print(f"List of processes: {process_list}")
    EarliestDeadlineFirst(process_list)

if __name__ == "__main__":
    main()
