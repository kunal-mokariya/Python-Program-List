a = [];
r = 3
for i in range(3):
	a.append(int(input()));
for i in range(len(a)):  
	for j in range(len(a)-1,i,-1): 
		if(a[j]==a[i]):
			a.pop(i);		
print("*********");
for i in range(len(a)):
	print(a[i]);