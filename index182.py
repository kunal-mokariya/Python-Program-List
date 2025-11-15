def my(a):
	b = list(a);
	c = [];
	d = "";
	for i in range(len(b)):
		if(ord(b[i])>96 and ord(b[i])<123):
			c.append(ord(b[i]));
			d = d+chr(c[i]-32)
		if(ord(b[i])>=65 and ord(b[i])<=90):
			c.append(ord(b[i]));
			d = d+chr(c[i])
	print(d);
my("465");