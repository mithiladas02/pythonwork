year=input("enter the year :")
year_num=int(year)
if year_num % 4==0 :
    print(year_num, 'is a leap year')
else:
    print(year_num, 'is not a leap year')