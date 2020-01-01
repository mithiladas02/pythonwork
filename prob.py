#year=input("enter the year :")
#year_num=int(year)
#if year_num % 4==0 :
 #   print(year_num, 'is a leap year')
#else:
    #print(year_num, 'is not a leap year')


#word count

#text="i will love you if you love me back"
#count=0
#for char in text:
  #  if char==' ':
 #       count=count+1
#count=count+1
#print(count)


 #count vowels

#def countvowels(sentence):
 #   vowels=0

#for char in sentence:
  #  if char in list1:
    
 #       count=count+1
#print("number vowels in sentence:", count)


#def countvowels(sentence):
    #vowels=0
    
  
    #for i in sentence :
    #  if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O"or i=="U") :
   #     vowels=vowels+1
  #  print("number of vowels :")
 #   return vowels
#print(countvowels("i live i Dhaka"))


#remove duplicate list:



#def duplicate(my_list):
  #unique=[]
  #for char in my_list:
   # if char  not in unique:
  #    unique.append(char)
 # return unique
#numbers=["mithila","bappi","ankit","ankit","adhrit"]
#print(duplicate(numbers))

#find largest and smallest number:
#my_list=[]
#while True:

  #try:
        #num=input("Enter number :")
        #if num=="done" :
        #    print(my_list)
       #     print("Largest element is :" , max(my_list))
      #      print("Smallest element is :" , min(my_list))
     #       break
    #    num=int(num)
   #     my_list.append(num)
  #except:
      #print("Invalid input")




#friends = [ 'Joseph', 'Glenn', 'Sally' ]
#friends.sort()
#print(friends[0])


#** means power

#en=int(input("enter the number :"))
#fn=float(input("enter the number:"))
#print("result:",pow(en,fn))

#random number randint method

#import random
#random_num=random.randint(0,10)
#print(random_num)

#floor division
#import math
#en=int(input("enter the number :"))
#f1=int(input("enter the number :"))
#result=math.floor(en/f1)
#print(result)

#import math
#result=math.floor(3.4)
#print(result)

#swap variable
#a=10
#b=5
#ex=int(input("enter the number :"))
#ey=int(input("enter the number :"))
#c=x
#x=y
#y=c
#x,y=y,x
#a=a+b
#b=a-b
#a=a-b
#print(a,b)

#print("the value of x after swapping:",x)
#print("the value of y after swapping:",y)

#find the largest number:

#a=17
#b=2
#c=21
#largest=max(a,b,c)
#print("largest number :", largest)

#x=int(input("enter 1st number:"))
#y=int(input("enter 2nd number:"))
#z=int(input("enter 2nd number:"))

#if x>y and x>z:
 # print('the largest number is :',x)
#elif y>z:
 # print("the largest number is:",y)
#else:
 # print("the largest number is :",z)




#average number
#len=int(input("how many numbers do you want:"))
#nums=[]
#for i in range(0,len):
  #elements=int(input("enter the elements:"))
  #nums.append(elements)
 # print('nums',nums)
#total=sum(nums)
#avg=total/len
#print("average of elements:",round(avg,2))

#print("nums",nums,total,round(avg,2))



#2nd type average
#len=int(input("how many numbers do you want:"))
#total=0
#for i in range(0,len):
 # elements=int(input("enter the elements:"))
  
 # total=elements+total
  #print("elements",elements)
  #print("total",total)


  #avg=total/len
#print("elements",elements)
#print("total",total)
#print("average",round(avg,2))


#3rd type average
#numb=int(input("how many numbers do you want to enter:"))
#numbers=[]
#while len(numbers)<numb:
  #no=int(input("enter your number:"))
  #numbers.append(no)
 # print('numbers',numbers)
#print(sum(numbers)/numb)

#divisible 3 and 5

#numbs=int(input("enter the number:"))
#my_list=[]
#for i in range(0,numbs):
  #if i<numbs and i%5==0 and i%3==0:
    #my_list.append(i)
#print("my_list",my_list)
  


#find the sum of every disit:such as 12=1+2



#def get_sum_of_disit(num):
 # sum=0
  #while(num>0):
   # last_disit=num % 10
    #sum=sum+last_disit
    #num=num//10
  #return sum

#user_num=int(input("enter a number :"))
#total=get_sum_of_disit(user_num)
#print("the total sum of disit is :",total)


#loop( for given list get the sum of each number in the list)


#def get_sum(nums):
  #sum=0
  #for i in nums:
   # sum=sum+i
  #return sum
#nums=[13,12,65,42,12,11,56]
#total=get_sum(nums)
#print("the total of each elements:",total)


#find the largest element of a list

#my_list=[12,56,7,79,98,2]
#largest=max(my_list)
#print("largest number:",largest)

#2nd types

#def get_largest(nums):
 # largest=nums[0]

  #for num in nums:
   # if num > largest :
      #  largest=num
  #return largest
#my_nums=[12,56,7,79,98,2]
#largest=get_largest(my_nums)
#print('the largest number is :',largest)

  
    
#for the smallest number in the elements:
#def get_smallest(nums):
 # smallest=nums[0]
  #for num in nums:
   # if num<smallest:

    #  smallest=num
  #return smallest
#my_list=[12,56,7,79,-21,-3]
#smallest=get_smallest(my_list)
#print("the smallest number :",smallest)


#take a number as a input. then get the sum of the numbers. If the numbers is n. 

#nums=int(input("enter the number:"))
#sum=0
#for i in range(0,nums+1):
 # sum= sum+ i**2
#print("sum of the numbers:", sum)

#2nd type
#def get_number(n):
 # total=(n*(n+1)*(2*n+1))/6
  #return total  
#nums=int(input("enter the number :"))
#total=get_number(nums)
#print("square the sum:",total)

#3rd type
#def get_number(num):
#  sum=0
 # for i in range(num+1):
  #  square=i**2
   # sum=sum+square
  #return sum
#nums=int(input("enter the number:"))
#sum= get_number(nums)
#print("the result is :",sum)


#fine the sumationa of (n(n+1)/2)**2

#def get_number(n):
 # sum=((n*(n+1))/2)**2
  #return sum
#nums=int(input("enter the number:"))
#sum=get_number(nums)
#print("the result is:",sum)

#find the 2nd laregst number:

#my_list=[1,2,3,4,5,6,7,8,9,10]
#newlist=my_list
#newlist.remove(max(my_list))
#print("second largest:",max(newlist))

#find the 2nd smallest number:
#y_list=[3,44,-21,50,10,-3]
#my_list.remove(min(my_list))
#print("second smallest:",(min(my_list)))

#2nd type:
#my_list=[3,44,-21,50,10,-3]
#nums=sorted(my_list)
#print(nums[1])

#remove all duplicate number:

#def duplicate(items):
 # result=''
  #for i in items:
   # if i not in result:#you check whether a character exists in a string-not in.the not-in is just the opposite check of in
    #  result+=i
      
     
   

  #return result

#my_list=input("whats your string:")
#dupli=duplicate(my_list)
#print("without duplicate:",dupli)

#miles to kilometers

#inp=input("enter the miles:")
#finp=float(inp)
#kilometers=(finp*1.6)
#print("result is :",kilometers)

#celcius to fernhiet:

#inp=float(input("enter the fahrenhiet:"))
#celcius=(inp-32.0)*5/9
#print(celcius)

#inp=float(input("enter the celcius:"))
#fahrenhiet=(inp*9/5)+32
#print(fahrenhiet)

#convert a decimal to binary:

#def dec_to_binary(n):
 # my_list=[]
  #while n > 0:
   # my_list.append(n%2)
    #n=n//2
  #my_list.reverse()

  #binary=''
  #for i in my_list:
   # binary+=str(i)
  #return binary

#num=int(input("enter decimal number :"))
#binary=dec_to_binary(num)
#print("binary number is:",binary)

#2nd type

#def dec_to_binary(n):
 # if n > 1 :
  #  dec_to_binary(n//2)
  #print(n%2,end='')
  
#num=int(input("enter the number:"))
#dec_to_binary(num)
#print("")

#convert binary to decimal
#num = input('enter a number: ')
#decimal = 0
#for i in num:
 #   decimal = decimal**2 + int(i)
#print (decimal)

#find celcius,faharenhite,kelvin use in function

#simple interst
#def simple_interest(si):
 
 # return si
#p=int(input("enter Principla:"))
#t=int(input("enter time:"))

#r=int(input("enter interest:"))
#SI=(p*r*t)/100
#interest=simple_interest(SI)
#print("Simple Interest:",interest)

#coumpound interest
#def simple_interest(si):
 
 # return si
#p=int(input("enter Principla:"))
#t=int(input("enter time:"))

#r=int(input("enter interest:"))
#SI=p*((1+(r/100))**t) - p

#interest=simple_interest(SI)
#print("compound interest:",interest)

#calculate grade of five subject:

def average_subject(total):
  avg=total/5
 
  if avg >= 90:
    print ("A")
  elif avg>=80 and avg<90:
    print ("B")
  elif avg >=70 and avg<80:
    print ("C")
  else:
    print("fail")

    return total

m=float(input("enter the  math grade:"))
e=float(input("enter the english grade:"))
p=float(input("enter the physics grade"))
c=float(input("enter the chemistry grade:"))
b=float(input("enter the biology grade:"))
sum=m+e+p+c+b
print(sum)
avg_sub=average_subject(sum)
print(avg_sub)






  

 
    
    
    


 
 








     
      

  




  
  

    
  
     
    




             


      
         
    
    







