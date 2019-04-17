mark=input('pls enter your mark')
mark=int(mark)
if mark>=80:
	grade="A+"
elif mark>=70:
	grade="A"
elif mark >=60:
	grade="A-"
elif mark >=50:
	grade='B'
else:
	grade="F"
print('your grade is=',grade)