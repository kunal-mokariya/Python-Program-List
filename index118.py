ar = [];
a = 1;
for i in range(3):
	temp = []
	for j in range(3):
		temp.append(a);
		a = a+1;
	ar.append(temp)
for i in range(3):
	for j in range(3):
		print(ar[i][j],end=" ");
	print()