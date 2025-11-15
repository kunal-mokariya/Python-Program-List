c = int(input("Enter Mark Of C: "));
java = int(input("Enter Mark Of Java: "));
asp = int(input("Enter Mark Of asp: "));
os = int(input("Enter Mark Of Os: "));
iks = int(input("Enter Mark Of iks: "));
total = c+java+asp+os+iks;
per = total/5;
print("Total Mark: ",total);
print("Per: ",per,"%");
r = 0;
if(c<40 or java<40 or asp<40 or os<40 or iks<40):
	if(c<40):
		r=r+1;
	if(java<40):
		r=r+1;
	if(asp<40):
		r=r+1;
	if(os<40):
		r=r+1;
	if(iks<40):
		r=r+1;
if(r==1 or r==2):
	print("ATKT");
if(r>2):
	print("FAIL");
if(c>=40 and java>=40 and asp>=40 and os>=40 and iks>40):
	print("PASS");
