def my():
	name = []; 
	print("Enter 10 student name");
	for i in range(3):
		name.append(input());
	for i in range(3):
		for j in range(3):
			if(name[i]<name[j]):
				temp = name[i]
				name[i] = name[j]
				name[j] = temp
	print("********");
	for i in name:
		print(i);
my();