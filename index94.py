a = int(input("input rows: "));
b= 1;
for i in range(a+1):
	for j in range(i):	
		print(b%2,end=" ");
		b = b+1;
	print();