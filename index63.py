a = 151
c = list(str(a))  
b = len(c)  
ans = 0


for digit in c:
    ans += int(digit) ** b


if a == ans:
    print("Armstrong")
else:
    print("Not Armstrong")
