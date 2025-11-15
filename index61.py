a = input("Enter a digit: ");
ans = 1;
if(a.isdigit()):
	b = int(a);
	c = b+1;
	for i in range(1,c):
		ans = i*ans;
	print(ans);
else:
	print("Enter only digit ");
	