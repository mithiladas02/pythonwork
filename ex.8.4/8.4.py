#list

        

    
#ex.8.4


#my_list = []
#fhand = open('romeo.txt')
#for line in fhand:
 #   words = line.split()                 
  #  for word in words:
   #     if word in my_list:
    #        continue                    
     #   my_list.append(word)           
#print(sorted(my_list))  

#fname=input("enter file name:")
#if len(fnmae) < 1:
 #    fname="mbox-short.txt"


#ex. 8.5


#fname=input('enter file name :')
#if len(fname) <1:
 #    fname='mbox-short.txt'


#fhand=open(fname)
#count=0

#for line in fhand:
 #    line=line.rstrip()
  #   wds=line.split()
   #  if line.startswith("From "):
    #      print(wds[1])
     #     count=count+1
#print ("There were", count, "lines in the file with From as the first word")

#ex 8.6


#my_list=[]
#while True:

 #    fname=input('enter a number :')
  #   if fname=="done":
   #       break
     
    # try:
     #     value=float(fname)
         #my_list.append(value)

     #except:
      #    print("invalid input")
       #   quit()
         
    
#print("maximum :", max(my_list))
#print("minimum :" , min(my_list))









     

#exercise 10.2

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. 
# Note that the autograder does not have support for the sorted() function.

#name =input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)

#hcount = dict()                                     #create empty dictionary
#hlst = []                                           #create empty list

#for line in handle: 
 #   words = line.split()
  #  if len(words) > 2 and words[0] == 'From':       #Select lines with 'From'
   #     hr = words[5].split(':')                    #Select hour (5th index) and split string with colon
    #    hcount[hr[0]] = hcount.get(hr[0], 0) + 1    #increase count for each hour
    #else:
     #   continue

#for k,v in hcount.items():                           #k = hour, v = count
 #   hlst.append((k,v))                               #append tuples to list

#hlst.sort()                                         #sort list by hour
#for k,v in hlst:                                    #loop through list of tuples
 #   print (k,v)                                      #print counts sorted by hour



fname=input("enter the file :")
if len(fname) < 1 : fname="mbox-short.txt"
fhand=open(fname)
hcount=dict()
h1st=[]
for line in fhand:
    words=line.split()
    if len(words) > 2 and words[0]==("From"):
        hr=words[5].split(':')
        hcount[hr[0]]=hcount.get(hr[0],0+1)
    else:
        continue
for k,v in hcount.items():
    h1st.append((k,v))
h1st.sort()
for k,v in h1st:
    print(k,v)

