te = 1;
for i in range(1,6):
	if(te<=3):
		if(i%2!=0):
			print("*")
		te =te+1;
	else:
		for j in range(i-2):
			print("*",end=" ")
		print();
			