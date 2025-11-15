h = float(input("Enter Hardness: "));
c = float(input("Enter Carbon: "));
t = float(input("Enter Tensile: "));
if(h>=50 and c>=0.7 and t>=5500):
	print("Grade A");
elif(h>=50 and c<=0.7):
	print("Grade B");
elif(c>=0.7 and t>=5500):
	print("Grade C");
elif(h>=50 and t>=5500):
	print("Grade D");
elif(h>=50 or c>=0.7 or t>=5500):
	print("Grade E");
else:
	print("Grade F");