def Waiting_Time(n,wt,bt):
	wt[0]=0

	for i in range(0,n):
		wt[i]=wt[i-1]+bt[i-1]
		print(wt[i])

def TurnAround_Time(n,tat,wt):
	tat[0]=0

	for i in range(1,n):
		tat[i]=tat[i]+wt[i]
		print(tat[i])

def avg(n,bt):
	wt=[0]*n
	wt[0]=0
	tat=[0]*n
	tat[0]=0
	avg_Tat=0
	avg_Wt=0

	Waiting_Time(n,wt,bt)
	TurnAround_Time(n,tat,wt)

	print("process"+"\t\t"+"burst time"+"\t\t"+"TurnAround_Time"+"\t\t"+"Waiting_Time")

	for i in range(n):
		print("P",str(i)+"\t\t"+str(bt[i])+"\t\t"+str(tat[i])+"\t\t"+str(wt[i]))

		avg_Wt=avg_Wt+wt[i]
		avg_Tat=avg_Tat+tat[i]

	print("Average waiting time is : ",str(avg_Wt/n))
	print("Average TurnAround  time is : ",str(avg_Tat/n))



def main():
	n=int(input("Enter the number of process:"))
	bursttime=[]
	for i in range(n):
		z=int(input("Enter the burst time of process "+str(i+1)+":"))
		bursttime.append(z)

	print(bt)

	bt= sorted(bursttime)

	avg(n,bt)

if __name__=="__main__":
	main()