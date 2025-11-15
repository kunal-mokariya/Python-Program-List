a = 1;
r = int(input("Enter Row Size: "));
for i in range(1,r+r+1):
	if(i%2!=0):
		print(a,end=" ");
		for j in range(i):
			print("*",end=" ");
		print();
		a = a+1;