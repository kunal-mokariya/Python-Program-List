a = [[10,20,30],[40,50,60],[70,80,90]];
b = [[5,2,3],[4,5,6],[7,8,9]];
for i in range(len(a)):
	for j in range(len(a)):
		ans = a[i][j]+b[i][j];
		print(ans,end=" ");
	print()
for i in range(len(a)):
	for j in range(len(a)):
		ans = a[i][j]-b[i][j];
		print(ans,end=" ");
	print()

