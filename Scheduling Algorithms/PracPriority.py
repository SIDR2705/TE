def Waiting_Time(order,n,wt):

	wt[0]=0
	for i in range(1,n):
		wt[i]=order[i - 1][1] +wt[i-1]

def TurnAround_time(order,wt,n,tat):
	tat[0]=0
	for i in range(n):
		tat[i]=wt[i]+order[i][1]


def main():

	n=int(input("Enter the number of process:"))
	proc=[]
	bt=[]
	priority=[]
	for i in range(n):
		proc.append(i)
		z=int(input("Enter the burst time of process "+str(i+1)+":"))
		bt.append(z)
		x=int(input("Enter the burst time of process "+str(i+1)+":"))
		priority.append(x)

	new=zip(proc,bt,priority)
	order= sorted(new, key=lambda new: new[2],reverse=True)

	wt=[0]*n
	tat=[0]*n


	print(order)

	Waiting_Time(order,n,wt)
	TurnAround_time(order,wt,n,tat)


	total_wt=0
	total_tat=0

	print("Process       Burst time     Waiting_Time      TurnAround_time ")

	for i in range(n):
		print(str("P["+str(order[i][0]))+"]"+"\t\t"+str(order[i][1])+" \t\t"+str(wt[i])+"\t\t "+ str(tat[i]))

		total_tat=total_tat+tat[i]
		total_wt=total_wt+wt[i]

	print("Average TurnAround_time is :",str(total_tat/n))
	print("Average Waiting_Time is :",str(total_wt/n))



if __name__=="__main__":
	main()