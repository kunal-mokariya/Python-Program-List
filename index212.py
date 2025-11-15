import os;
def my(file_name,message):
	f = open(file_name,"w");
	f.write(message);
	f.close();
	print("file save");
a = input("Enter file name for write data: ");
b = input("Enter Text: ");
my(a,b);
