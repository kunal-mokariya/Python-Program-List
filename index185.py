def my():
	a = "hello world asd "
	a.rstrip();
	b = list(a);
	ans = 0;
	word = 1;
	for i in b:
		ans = ans+1;
	for j in b:
		if(j==" "):
			word = word+1;
			
	print("total char: ",ans);
	print("total word: ",word);
my();	