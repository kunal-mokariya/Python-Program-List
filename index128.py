a = [];
for i in range(5):
	a.append(int(input()));
for i in range(5):
	for j in range(5):
		if(a[i]<a[j]):
			temp =a[i];
			a[i]=a[j];
			a[j]=temp;
print("********");
for i in range(5):
	print(a[i]);