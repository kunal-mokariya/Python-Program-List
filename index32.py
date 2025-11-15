print("1. Area of Circle");
print("2. Area of Triangle");
print("3. Compute (f+g)*(f+g)");
print("4. Simple Interest");
print("5. Exit");
a = int(input("Enter Your Choice: "));
if(a==1):
	a = int(input("Enter Input: "));
	ans = (3.14*(a*a))
	print("Ans: ",ans);
elif(a==2):
	a = int(input("Enter base: "));
	b = int(input("Enter height: "));
	ans = (1/2*(a*b));
	print("Ans: ",ans);
elif(a==3):
	f=int(input("Enter c: "));
	g=int(input("Enter d: "));
	i = (f+g)*(f+g);
	print("Ans: ",i);
elif(a==4):
	a=int(input("Enter Amount: "));
	b=int(input("Enter rate: "));
	c=int(input("Enter time: "));
	ans = (a*b*c)/100;
	print("interest: ",ans);
elif(a==5):
	exit();
else:
	print("Enter Valid Input !");

