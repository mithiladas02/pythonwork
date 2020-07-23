#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and print the result. 


# In[2]:


def nums_func(a):
    return lambda a:a+15
c=nums_func(10)
print(c(5))


# In[3]:


r=lambda x,y:x*y
print(r(2,3))


# In[4]:


#  Write a Python program to create a function that takes one argument, and that argument will be multiplied with an 
# unknown given number.
def fun_one(n):
    return lambda x:x*n

result=fun_one(3)
print("double number is :" , result(15))
    


# In[5]:


# 3. Write a Python program to sort a list of tuples using Lambda

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)


# In[6]:


subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)


# In[7]:


a=[("English",88),("Science",32),("Math",100)]
a.sort(key=lambda x:x[1])
print(a)


# In[8]:


# 4. Write a Python program to sort a list of dictionaries using Lambda.

models = [{'make':'Nokia', 'model':216, 'color':'Black'}, 
          {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
sorted_models=sorted(models,key=lambda x:x['color'])
print(models)


# In[9]:


# Write a Python program to filter a list of integers using Lambda.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v=list(filter(lambda x: x%2 == 0 , nums))
v


# In[10]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
va=list(filter(lambda x:x%2!=0,nums))
print(var)


# In[ ]:


# 6. Write a Python program to square and cube every number in a given list of integers using Lambda
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(map(lambda x:x**2, nums))
new_list                
                


# In[ ]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cube_nums = list(map(lambda x: x ** 3, nums))
cube_nums


# In[ ]:


# 7. Write a Python program to find if a given string starts with a given character using Lambda.
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Java'))


# In[ ]:


start_with=lambda x:True if x.startswith('P') else False
print(start_with('Python'))


# In[ ]:


# 8. Write a Python program to extract year, month, date and time using Lambda.
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))


# In[ ]:


import datetime
now=datetime.datetime.now()
print(now)
month=lambda x:x.month
day=lambda x:x.day
year=lambda x:x.year
print(month(now))
print(day(now))
print(year(now))


# In[11]:


# 9. Write a Python program to check whether a given string is number or not using Lambda.
is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))


# In[12]:


is_num=lambda x:x.replace('.','',1).isdigit()
print(is_num('2678'))
print(is_num('abc'))


# In[13]:


is_num=lambda x:x.replace('.','',1).isdigit()
print(is_num('abc'))


# In[14]:


# 10. Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))


# In[15]:


from functools import reduce
fib_series=lambda n:reduce(lambda x, _: x+[x[-1]=x[-2]],range(n-2),[0,1])
print(fib_series(2))


# In[16]:


# 11. Write a Python program to find intersection of two given arrays using Lambda
array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]

results=list(filter(lambda x:x in array_nums1,array_nums2))
print(results)


# In[17]:


# 2. Write a Python program to rearrange positive and negative numbers in a given array using Lambda. 
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
results=[x for x in array_nums if x<0]+[x for x in array_nums if x>0]
results


# In[18]:


# 13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]

results1=len(list(filter(lambda x: (x%2!=0),array_nums)))
results2=len(list(filter(lambda x:(x%2==0),array_nums)))
print(results1)
print(results2)


# In[19]:


# find the prime numkber
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
results=list(filter(lambda x: x%2==0,array_nums))
print(results)


# In[20]:


# 14. Write a Python program to filter a given list whether the values in the list are having length of 6 using Lambda.
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
    print(d)


# In[21]:


# 15. Write a Python program to add two given lists using map and lambda.
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
results=map(lambda a,b : a+b,nums1,nums2)
print(list(results))


# In[22]:


# 16. Write a Python program to find the second lowest grade of any student(s) from the given names and grades of
# each student using lists and lambda. Input number of students, names and grades of each student.

students = []
sec_name = []
second_low = 0
n = int(input("Input number of students: "))
for _ in range(n):
   s_name = input("Name: ")
   score = float(input("Grade: "))
   students.append([s_name,score])
print("\nNames and Grades of all students:")
print(students)
order =sorted(students, key = lambda x: int(x[1]))
for i in range(n):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
print("\nSecond lowest grade: ",second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nNames:")
for s_name in sec_student_name:
   print(s_name)


# In[23]:


# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda
nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
new_list=list(filter(lambda x:( x%19==0 or x%13==0), nums))
new_list


# In[24]:


nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("Orginal list:")
print(nums) 
result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), nums)) 
print("\nNumbers of the above list divisible by nineteen or thirteen:")
print(result)


# In[25]:


#  Write a Python program to find palindromes in a given list of strings using Lambda

from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]

str="abcd"
results=list(filter(lambda x:(Counter(str) == Counter(x)), texts))
print(results)


# In[27]:


# 19. Write a Python program to find all anagrams of a string in a given list of strings using lambda
from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
print("\nAnagrams of 'abcd' in the above string: ")


# In[28]:


#  Write a Python program to find the numbers of a given string and store them in a list, display the numbers which
#     are bigger than the length of the list in sorted form. Use lambda function to solve the problem.

str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
print("Original string: ",str1)
str_num=[i for i in str1.split(' ')]
lenght=len(str_num)
numbers=sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
for i in ((filter(lambda x:x>lenght,numbers))):
    print(i,end=' ')


# In[ ]:


abc=" ab 23 cd 19 gh 21"


# In[29]:


# Write a Python program that multiply each number of given list with a given number using lambda function. 
nums = [2, 4, 6, 9 , 11]
new_list=list(map(lambda x: x*2,nums))
print(new_list)


# In[30]:


# Write a Python program that sum the length of the names of a given list of names after removing the names that starts 
# with an lowercase letter. Use lambda function
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print("Result:")
print(len(''.join(sample_names)))


# In[31]:


# Write a Python program that removes the positive numbers from a given list of numbers. Sum the negative numbers and print
# the absolute value using lambda function.

nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print("Original list: ", nums)
print("Result:")
print(abs(sum([i for i in nums if i < 0]))) 


# In[ ]:





# In[ ]:





# In[ ]:




