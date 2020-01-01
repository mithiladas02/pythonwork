#fname=input("enter the file name :")
#if len==0:
    
 #   fname = 'mbox-short.txt'

    

#fhand=open(fname)
#count=0
#tot=0
#ans=0
#for lx in fhand:
   # ly=lx.rstrip()
    
    #if not  ly.startswith("X-DSPAM-Confidence:0.8475"):
    #    continue
   # count=count+1
  #  num=float(ly)
 #   tot=num+tot
#ans=tot / count
        
        
#print("Average spam confidence:"  , ans)
#fname = input("Enter file name: ")
#if len(fname) == 0:
    #fname = 'mbox-short.txt'
#fh = open(fname)
#count = 0
#tot = 0
#ans = 0
#for line in fh:
    #if not line.startswith("X-DSPAM-Confidence:") : continue
   # count = count + 1
  #  num = float(line[21:])
 #   tot = num + tot
#ans = tot / count
#print("Average spam confidence:", ans)

#fhand=open('mbox-short.txt')
#inp=fhand.read()
#print(len(inp))
#print(inp[21:])
fhand=open('mbox-short.txt')
for line in fhand:
    if line .startswith('from:') :
        print(line)


   

   