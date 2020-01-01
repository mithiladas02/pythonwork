#exercise 9.2
#fname = input("Enter file name :")
#fhand = open(fname)
#days=dict()
#for line in fhand:
 #   if line.startswith("From"):


  #      line=line.split()
   #     day= line[2]
    #    days[day]=days.get(day,0)+1
#print(days)

#exercise 9.3

#fname=input("enter file name :")
#fhand=open(fname)
#counts=dict()
#for line in fhand:
 #   if line.startswith("From"):
  #      line=line.split()
   #     count=line[1]
    #    counts[count]=counts.get(count,0)+1


#print(counts)


#exercise 9.4

#fname=input("enter file name :")
#if len(fname) < 1 : fname="mbox.txt"
#fhand=open(fname)
#emails=dict()
#for line in fhand:
 #   if line.startswith("From"):
  #      line=line.split()
   #     email=line[1]
    #    emails[email]=emails.get(email,0)+1
#largest = None
#for key in emails:
#	if largest is None or emails[key] > largest:
#		largest = emails[key]
#		bigword = key
#print (bigword, largest)


#exercise 9.5

#fname=input("enter file name:")
#fhand=open(fname)
#emails=dict()
#for line in fhand:
 #   if line.startswith("From"):
  #      line=line.split()
   #     email=line[1]
    #    email=email.split("@")
     #   domain=email[1]
      #  emails[domain]=emails.get(domain,0)+1
#print(emails)


#python for everybody book assignmenst. Chapter-9