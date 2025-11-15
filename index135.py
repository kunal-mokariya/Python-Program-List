name=["a","b","c","d","e"];
sales=[[10,20,30,40],[60,70,80,90],[100,110,120,130],[140,150,160,170],[180,190,200,210]];
ans = [];
for i in range(5):
	temp = 0;
	for j in range(4):
		temp = temp + sales[i][j];
	print("Customer name: ",name[i],"total: ",temp)