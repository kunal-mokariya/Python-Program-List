import os;
def my(file1,file2):
	f1 = open(file1);
	fdata = f1.read();
	f2 = open(file2,"w");
	f2.write(fdata);
	f1.close();
	f2.close();
	print("Data Copy Complete");
a = input("Enter file name for copy content another file: ");
b = input("Enter file name for copy data: ");
my(a,b)