import os;
def my():
	f = open("my.text");
	f2 = f.read();
	f3 = open("my1.text","w");
	f3.write(f2);
	f.close();
	f3.close();
	print("File Content Copy Complete");
my();
