a = [];
for i in range(3):
	temp = []
	for j in range(4):
		temp.append(int(input()))
	a.append(temp);
r = 0
c = 0
for i in range(3):
	for j in range(4):
		r = r+a[i][j]
for i in range(3):
	for j in range(4):
		c= c+a[i][0];
a2 = []
maxv = 0;
for i in range(3):
	for j in range(4):
		a2.append(a[i][j])
for i in range(12):
	if(a2[i]>maxv):
		maxv = a2[i];
min = maxv;
for i in range(12):
	if(a2[i]<min):
		min = a2[i]
print("row: ",r);
print("col: ",c);
print("Minimum value: ",min)
print("Maximum value: ",maxv)


