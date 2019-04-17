year=input("Enter year: ")
year=int(year)

if year%100!=0 and year%4==0:
	print(year," is leap year")
elif year%100==0 and year%400==0:
	print(year," is leap year")
else:
	print(year," is not leap year")
