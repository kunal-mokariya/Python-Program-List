def isalp(a):
	if((a>='a' and a<='z') or (a>='A' and a<='z')):
		print("Is alphabets");
	else:
		print("Is Not alphabets");
def isnum(a):
	if(a>='0' and a<='9'):
		print("Is Digit");
	else:
		print("Is Not Digit");
def ischr(a):
	if(('A' <= a <= 'Z') or ('a' <= a <= 'z') or ('0' <= a <= '9')):
		print("True");
	else:
		print("False");
isalp("AA");