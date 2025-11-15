result = [];
total = 0;
sub = ["c","java","c#","asp","python"];
for i in range(5):
	for j in range(1):
		print(sub[i],end=" ")
		result.append(sub[i]);
		m = int(input())
		result.append(m)
		total = total+m;
per = total/5;
print("total: ",total);
print("per: ",per)