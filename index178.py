def my(a,b):
	c = list(a);
	d = list(b);
	ans = 0;
	ans2  = 0;
	for i in c:
		ans = ans + (ord(i));
	for j in d:
		ans2 = ans2+ (ord(j));
	if(ans==ans2 and a==b):
		print("Same");
	else:
		print("Not Same");
my("ad","ad");