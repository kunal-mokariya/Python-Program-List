a = int(input("Enter a: "));
b = int(input("Enter b: "));
c = int(input("Enter c: "));
d = a if(a>=b and a>=c) else (b if b>=c and b>=a else c);
print(d);