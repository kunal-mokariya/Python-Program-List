a = []
size = int(input("enter size: "));
for i in range(size):
	temp = []
	for j in range(size):
		temp.append(int(input()));
	a.append(temp);
temp1 = 0
temp2 = 0
for i in range(size):
	temp1 = temp1 + a[i][i]
x = 0; 
for i in range(size-1,-1,-1):
	temp2 = temp2 +a[x][i];
	x = x+1
print("ans1: ",temp1)
print("ans2: ",temp2)
