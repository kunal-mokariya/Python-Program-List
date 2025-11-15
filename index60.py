a = input("Enter the digit: ");
ans = 0;
if(a.isdigit()):
	b = int(a);
	while(b!=0):
		c = b%10;
		ans = ans+c;
		b= b//10;
	print(ans);
	
else:
	print("Enter Only Digits");
	