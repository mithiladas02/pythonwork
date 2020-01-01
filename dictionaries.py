fname = input("enter the file :")
if len(fname)<1: faname="mbox-short.txt"
handle = open(fname)


dict={}


for line in handle:
    if line.startswith('From :'):
        line=line.rstrip()
      
        words = line.split()
        email=words[1]
        if email not in dict:
            dict[email]=1
        else:
            dict[email]+=1
bigname=None
bigcount=None
for mail in dict:
    if bigcount==None or bigcount < dict[email]:
        bigname= email
        bigcount= dict[email]
print(bigname,bigcount)
    