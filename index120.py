a= [];
n = 0;
p = 0;
for i in range(10):
	a.append(int(input()));
for j in range(10):
	if(0>a[j]):
		n = n+1;
	else:
		p = p+1;
print("Total Nagetive Value: ",n);
print("Total Positive Value: ",p);

		