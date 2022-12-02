class RoundR :
    @staticmethod
    def main( args) :
        Process = [0] * (10)
        a = [0] * (10)
        Arrival_time = [0] * (10)
        Burst_time = [0] * (10)
        WT = [0] * (10)
        TAT = [0] * (10)
        Pno = 0
        sum = 0
        TimeQuantum = 0
        print("\nEnter the no. of Process::")
        sc =  "Python-inputs"
        Pno = input()
        print("\nEnter each process::")
        i = 0
        while (i < Pno) :
            Process[i] = input()
            i += 1
        print("\nEnter the Burst Time of each process::")
        i = 0
        while (i < Pno) :
            Burst_time[i] = input()
            i += 1
        print("\nEnter the Time Quantum::")
        TimeQuantum = input()
        while True :
            i = 0
            while (i < Pno) :
                if (Burst_time[i] > TimeQuantum) :
                    Burst_time[i] -= TimeQuantum
                    j = 0
                    while (j < Pno) :
                        if ((j != i) and (Burst_time[j] != 0)) :
                            WT[j] += TimeQuantum
                        j += 1
                else :
                    j = 0
                    while (j < Pno) :
                        if ((j != i) and (Burst_time[j] != 0)) :
                            WT[j] += Burst_time[i]
                        j += 1
                    Burst_time[i] = 0
                i += 1
            sum = 0
            k = 0
            while (k < Pno) :
                sum = sum + Burst_time[k]
                k += 1
            if((sum != 0) == False) :
                    break
        i = 0
        while (i < Pno) :
            TAT[i] = WT[i] + a[i]
            i += 1
        print("process\t\tBT\tWT\tTAT")
        i = 0
        while (i < Pno) :
            print("process" + str((i + 1)) + "\t" + str(a[i]) + "\t" + str(WT[i]) + "\t" + str(TAT[i]))
            i += 1
        avg_wt = 0
        avg_tat = 0
        j = 0
        while (j < Pno) :
            avg_wt += WT[j]
            j += 1
        j = 0
        while (j < Pno) :
            avg_tat += TAT[j]
            j += 1
        print("average waiting time " + str((avg_wt / Pno)) + "\n Average turn around time" + str((avg_tat / Pno)))
    

if __name__=="__main__":
    RoundR.main([])