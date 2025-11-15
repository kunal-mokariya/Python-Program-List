c = int(input("Enter Mark Of C: "));
java = int(input("Enter Mark Of Java: "));
asp = int(input("Enter Mark Of asp: "));
os = int(input("Enter Mark Of Os: "));
iks = int(input("Enter Mark Of iks: "));
total = c+java+asp+os+iks;
per = total/5;
print("Total Mark: ",total);
print("Per: ",per,"%");
if(per<40):
	print("Fail");
elif(per>=40 and per<50):
	print("PASS CLASS");
elif(per>=50 and per<60):
	print("SECOND CLASS");
elif(per>=60 and per<70):
	print("FIRST CLASS");
elif(per>=70 and per<=100):
	print("DISTINCTION");