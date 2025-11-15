a = [];
s = 0;
b = 0
for i in range(5):
	a.append(int(input()));
for j in range(5):
	for k in range(5):
		if(a[j]<a[k]):
			b = a[k];
		if(a[j]>a[k]):
			s = a[k];
print("Max Value: ",b);
print("Min Value: ",s);