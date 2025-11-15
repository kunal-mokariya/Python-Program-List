te = 1;
a = 1;
for i in range(1,6):
	if(te<=3):
		if(i%2!=0):
			print(i)
		te =te+1;
		a = a+1;
	else:
		for j in range(i-2):
			a = a+1;
			print(a,end=" ")
		a = a+1;
		print();
			