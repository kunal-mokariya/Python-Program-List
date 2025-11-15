a = input("Enter Only Digits: ");
b=0;
ans = 0;
if(a.isdigit()):
	c = int(a);
	while(c!=0):
		ans = c%10;
		b=b*10+ans;
		c=c//10;
	print(b);
else:
	print("Enter only Digit 1");
