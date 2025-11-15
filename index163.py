def my1():
	print("Calculate the area of circle");
	a = int(input("Enter Input: "));
	ans = (3.14*(a*a))
	print("Ans: ",ans);

def my2():
	print("Calculate the area of Triangle");
	a = int(input("Enter base: "));
	b = int(input("Enter height: "));
	ans = (1/2*(a*b));
	print("Ans: ",ans);

def my3():
	print("Calculate the are of squere");
	a = int(input("Enter side: "));
	ans = a*a;
	print("Ans: ",ans);


def my4():
	print("Calculate the area of rectangle");
	a = int(input("Enter lenght: "));
	b = int(input("Enter width: "));
	ans = (a*b);
	print("Ans: ",ans);


print("1. Calculate the area of circle");
print("2. Calculate the area of Triangle");
print("3. Calculate the are of squere");
print("4. Calculate the area of rectangle");
ch = int(input("Enter your choice : "));
if(ch==1):
	my1();
if(ch==2):
	my2();
if(ch==3):
	my3();
if(ch==4):
	my4();
if(ch>4 or ch<1):
	print("Invalid Choice !");
