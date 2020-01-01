import re
fname=open('regex.txt')
sum=0
for line in fname:
    line=line.rstrip()
    numbers=re.findall('[0-9]+',line)
    for number in numbers:
        sum=sum+int(number)
print(sum)