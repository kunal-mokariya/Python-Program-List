def my(a):
	b = list(a);
	c = "";
	for i in range(len(b)-1,-1,-1):
		c = c+b[i];
	print(c);
my("123");