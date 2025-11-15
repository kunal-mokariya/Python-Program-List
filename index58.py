a = int(input("Enter the value: "));
b = 10;
ans = 0;
temp = 0;
for i in range(1,a):
	ans = i/b;
	temp = temp + ans;
	b = b*10;
print("Total: ",temp);	