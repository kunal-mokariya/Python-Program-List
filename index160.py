def my():
	a=int(input("Enter Amount: "));
	b=float(input("Enter rate: "));
	c=int(input("Enter time(Year): "));
	ans = a * (1+b/100)**c 
	total = ans - a ;
	print("interest: ",total);
	print("compound interest: ",ans);
my();
