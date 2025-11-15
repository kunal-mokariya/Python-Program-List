a = int(input("Enter a: "));
b = int(input("Enter b: "));
c = int(input("Enter c: "));
d = "a is big" if(a>=b and a>=c) else ("b is big" if b>=c and b>=a else "c is big");
print(d);