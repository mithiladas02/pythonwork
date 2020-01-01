#str1="hello"
#str2='there'
#tina=str1+str2
#print(tina)

#str3=123
#str4=str3+2
#x=int(str3)+2
#print(x)

#fruit="banana"
#letter=fruit[3]
#print(letter)
#x=3
#w=fruit[x-1]
#print(w)

#fruit='banana'
#print(len(fruit))

#fruit='banana'
#x=len(fruit)
#print(x)
#fruit='banana'
#for letter in fruit :
#    print(letter)

#word='banana'
#count=0
#for letter in word :
    #if letter=='a' :
     #   count=count+1
    #print(count)
#s=" Monty Python"
#print(s [0:4])
#print(s[0:3])
#print(s[6:20])
#print(s[8:])
#print(s[:])
#a='Hello'
#b=a+'There'
#print(b)
#c=a+""+'there'
#print(c)

#fruit='banana'
#'n' in fruit
#True
#'m' in fruit
#False
#'nan' in fruit
#True
#if 'a' in fruit :
    #print('Found it!')
#greet= 'hello amey'
#zap=greet.upper()
#print(zap)
#greet='Hello Tina'
#zap=greet.lower()
#print(zap)
#print(greet)
#a=[1,2,3]
#b=[4,5,6]
#c=a+b
#print(c)
#d=c*2
#print(d)
#fruit="banana"
#pos=fruit.find('na')
#print(pos)
#pos=fruit.find('b')
#print(pos)
#aa=fruit.find('2')
#print(aa)

#greet="Hello Tina"
#nstr=greet.replace('Tina' , 'Bob')
#print(nstr)
#nstr=greet.replace('0' , 'x')
#print(nstr)

#list slics
#le=['a','b','c','d','e','f','g','h','i','j']
#print(letters)
#print(le[3:7])
#print(le[1:8:2])
#greet=' hello bob '
#greet.strip()
#line='please have a nice day'
#line.startswith('please')
#True

#data='From Stephen.marquard@uct.ac.za sat Jan 5 09: 14: 16 2008'
#atpos=data.find('@')
#print(atpos)
#sppos=data.find(' ' , atpos)
#print(sppos)
#host=data[atpos+1 : sppos]
#print(host)
#x = 'From marquard@uct.ac.za'
#qpos=x.find('q')
#print(qpos)
#for letter in 'banana' :
    #print(letter)
#print(len('banana')*7)


#data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#pos = data.find('.')
#print(data[pos:pos+3])


text = 'From marquard@uct.ac.za'
atpos=text.find('@')
print(atpos)
sppos=text.find('uct')
print(sppos)
host=text[atpos+1 : ]

#str = "X-DSPAM-Confidence: 0.8475" 
#ipos=str.find(':')

#print(ipos)
#ex=str[ipos+1:]
#value=float(ex)
#print(value)


#data='From Stephen.marquard@uct.ac.za sat Jan 5 09: 14: 16 2008'
#atpos=data.find( ':')
#print(atpos)
#sppos=data.find[atpos, ' ']
#print(sppos)
#host=data[atpos+1 : sppos]
#print(host)