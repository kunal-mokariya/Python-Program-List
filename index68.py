a = int(input("Enter the value: "));
sum = 0;
temp = 0;
for i in range(1,(a+1)):
	if(temp>=2):
		temp = 0;
	else:
		sum = sum+i;
		temp = temp+1;
		#print(i);
print("Total: ",sum);