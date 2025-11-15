a = input("Enter Digit: ");
ans = 1;
if(a.isdigit()):
	b = int(a);
	for i in range(1,int(b//2)):
		if(b%2==0):
			ans=0;
			break;
if(ans==1):
	print("Prime Number");
if(ans!=1):
	print("Not Prime Number");