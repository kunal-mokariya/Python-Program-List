a=[];
for i in range(3):
	a.append(int(input()));
for j in range(3):
	for k in range(3):
		if(a[j]<a[k]):
			temp = a[k];
			a[k]=a[k+1];
			a[k+1]=temp;
for k in a:
	print(k);
	