b = input("Enter Year: "); 

if(len(b)==4):
	a = int(b);
	if((a%100==0 and a%400==0) or (a%4==0)):
		print("leap year");
	else:
		print("is not leap year");
else:
	print("Enter Valid Input");