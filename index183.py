def my(a):
	b = list(a);
	c = [];
	d = "";
	for i in range(len(b)):
		c.append(ord(b[i]));
	for j in range(len(b)):
		if(c[j]>=65 and c[j]<=96):
			d = d + chr(c[j]+32);
		if(c[j]>=97 and c[j]<=122):
			d = d + chr(c[j]);
	print(d);
my("ABcD");