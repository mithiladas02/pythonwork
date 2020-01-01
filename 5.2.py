#Maximum=None
#Minimum=None
#while True:
    #num=input("Enter number :")
    #if num=="done" :
     #   break
    #if num> "Maximum" :
     #   print("maximum", num)
    #if num< "Minimum" :
        #print("Minimum", num)

    
    #try :
     #   fnum=float(num)
    #except:
      #  print("Invalid input")
     #   continue
    #Maximum=fnum
    #inimum=fnum
    #rint("Maximum is", num)
    #print("Minimum is", num)
#Maximum=None
#Minimum=None
#while True:
    #en=input('enter number :')
    #if en=="done" :
     #   break
    #try:
     #   fen=float(en)
    #except:
    #    print("Invalid input") 
   #     continue   

    
  #  count=count+1
 #   total=total+fen
    
    
#print("All done")
#print(total,count,total/count)
    
my_list=[]


while True:
    try:
        num=input("Enter number :")
        if num=="done" :
            print(my_list)
            print("Largest element is :" , max(my_list))
            print("Smallest element is :" , min(my_list))
            break
        num=int(num)
        my_list.append(num)
    except:
        print("Invalid input")

        

             
        

        
   
    