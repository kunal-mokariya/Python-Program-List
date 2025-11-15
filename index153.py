import math
def prime(n):
	if n <= 1:
		return (f"{n} is not a prime number")  
	ans = 120;
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			ans = 0;
			break
	if(ans==0):
		return(f"{n} is not a prime number")
	else:
		return (f"{n} is a prime number")
print(prime(20))

