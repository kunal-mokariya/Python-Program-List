a = int(input("Enter the value: "));
c = a+1;
for i in range(0,c):
	for j in range(c-i):
		print(" ",end="");
	for k in range(1,i+1):
		print(k,end=" ");
	print();