a = 2
for i in range(a):
	for j in range(a-i+1):
		print(" ", end="  ") 
	b = 1 
	for k in range(i+1):
		print("  ",b, end="  ")
		b = b*(i-k)//(k+1); #b = 1*(1-0)//0+1
		print("i: ",i) 
	print()
"""
    1  
"""