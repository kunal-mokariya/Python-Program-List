a = input("Enter Digit: ");
b = 1;
if(a.isdigit()):
	c = int(a);
	for i in range(1,c+1):
		b = b*i;
	print(b);