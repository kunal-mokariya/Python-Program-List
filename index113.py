p = 0;
a = int(input("enter row: "));
for i in range(a+1,0,-1):
	for j in range(1,i):
		print(j,"",end="");
	if(p==0):
		for k in range(a+1,i,-1):
			print(" ",end=" ");
		for l in range(i-2,0,-1):
			print(l,"",end="");
			p = 20;
	else:
		for k in range(a,i,-1):
			print("   ",end=" ");
		print("  ",end="")
		for l in range(i-1,0,-1):
			print(l,"",end="");	
	print();