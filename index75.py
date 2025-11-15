a = int(input("Enter the value: "))
temp = 1;
for i in range(1,(a+1)):
	if(i%2!=0):
		temp = temp*i;
print("ans: ",temp);