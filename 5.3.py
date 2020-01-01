largest=0
smallest=0
while True:
    en=input('enter number :')
    if en=="done" :
        print(largest, smallest)
        print("Largest element is :" , max('largest'))
        print("Smallest element is :" , min('smallest'))
        break
    try:
        fen=float(en)
    except:
        print("Invalid input") 
        continue  
         

    

 
    
     
    
print("All done")
