a = input("Enter Digit: ");
if(a.isdigit()):
	b = int(a);
	ans = 0;
	d = 0;
	e = 1;
	for i in range((b+1)):
		print(d);
		ans = d+e;
		d = e;
		e = ans;