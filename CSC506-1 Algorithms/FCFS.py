# FCFS Draft Algorithm
# Necessary inputs: Process list
# Process should contain - [Arrival time, burst time, process id]


def FCFS(process_list):
    t=0
    gantt = []
    completed = {}
    process_list.sort()
    #Sorting process list to simulate recorded arrival time #NOTE: This will be unnecessary in real version

    while process_list != []: #Keeping while loop for future dynamic solution
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
            #Service next process
            process = arrived[0]
            gantt.append(process[2])
            burst_time = process[1]
            t += burst_time

            #Remove process from list
            process_list.remove(process)
            completed[process[2]] = t
    print(gantt)
    print(completed)



def main():
    process_list = [[2,6,"p1"],[5,2,"p2"],[1,8,"p3"],[0,3,"p4"],[4,4,"p5"]]
    print(f"List of processes: {process_list}")
    FCFS(process_list)

if __name__ == "__main__":
    main()
