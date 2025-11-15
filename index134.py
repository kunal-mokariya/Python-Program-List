size = int(input("enter size: "));
a=[]
for i in range(size):
	abc = []
	for j in range(size):
		abc.append(int(input()));
	a.append(abc);
rtemp = 0;

for i in range(size):
	for j in range(size):
		rtemp = a[i][j]+rtemp;
	print("col ",i+1,":",rtemp)

ctemp = 0
for i in range(size):
	for j in range(size):
		ctemp = a[j][i]+ctemp;
	print("row ",i+1,":",ctemp)
