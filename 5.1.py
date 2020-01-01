#count=0
#total=0
#while True:
    #en=input('enter number :')
    #if en=="done" :
     #   break
    #fen=float(en)
   # print(fen)
  #  count=count+1
 #   total=total+fen
#print("All done")
#print(total,count,total/count)

count=0
total=0
while True:
    en=input('enter number :')
    if en=="done" :
        break
    try:
        fen=float(en)
    except:
        print("Invalid input") 
        continue   

    
    count=count+1
    total=total+fen
    
print("All done")
print(total,count,total/count)