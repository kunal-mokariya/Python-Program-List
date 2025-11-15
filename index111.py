a = int(input("Enter the value: "));
c = a+1;
d = c+c-1;
for i in range(1,c+c-1):
	if(i%2!=0):
		for j in range(d-i):
			print(" ",end="");
		for k in range(1,i+1):
			print(k%2,end=" ");
		print();