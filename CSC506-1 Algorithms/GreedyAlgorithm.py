#Greedy Algorithm Draft (Modeled off of a non premptive SJF)
#Logic - completing the most jobs in the shortest amount of time
#Necessary inputs: Process list
#Process should contain - [burst time, arrival time, process id]


def GreedyAlgorithmSJF(process_list):
    t = 0
    gantt = []
    completed = {}
    process_list.sort(key = lambda x: x[1])
    #Sorting process list to simulate recorded arrival time #NOTE: This will be unnecessary in real version

    while process_list != []:
        #Boundary condition
        arrived = []
        for p in process_list:
            if p[1] <= t:
                arrived.append(p)
        if arrived == []:
            gantt.append("Idle")
            t += 1
            continue
        else:
            #Sort for shortest burst time
            arrived.sort()
            process = arrived[0]
            #Service next process
            burst_time = process[0]
            process_id = process[2]
            t += burst_time

            gantt.append(process_id)

            #Remove the process once done
            process_list.remove(process)
            completed[process_id] = t
    print(gantt)
    print(completed)



def main():
    process_list = [[6,2,"p1"],[2,5,"p2"],[8,1,"p3"],[3,0,"p4"],[4,4,"p5"]]
    print(f"List of Processes: {process_list}")
    GreedyAlgorithmSJF(process_list)

if __name__ == "__main__":
    main()
