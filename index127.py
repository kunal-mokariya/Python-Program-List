a = [];
p = -1;
temp = 0;
for i in range(10):
	a.append(int(input()));
for i in range(10):
	if(a[i]>temp):
		p = i;
		temp =  a[i];
print("Index Of Max Value: ",p);
print("max value: ",a[p])		