a=[];
size = int(input("enter size: "));
for i in range(size):
	abc = []
	for j in range(size):
		abc.append(int(input()));
	a.append(abc)
ans = 0;
for i in range(size):
	for j in range(size):
		print(a[i][j])
		ans = ans + a[i][j];
	print("ans: ",ans);
	ans = 0;