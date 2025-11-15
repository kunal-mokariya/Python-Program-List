def fact(a):
	ans = 1;
	for i in range(1,a+1):
		ans = ans*i;
	return ans;
print(fact(5));