a = [];
sum = 0;
for i in range(5):
	a.append(int(input()));
for j in range(5):
	sum = sum + a[j];
ans = sum/5;
print(ans);