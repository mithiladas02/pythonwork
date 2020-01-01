my_list=[]
while True:

    fname=input('enter the number:')
    if fname=="done":


    
        break
    try:
        fe=float(fname)
        my_list.append(fe)
        
    except:
        print("invalid input")
        quit()
        
    
    
print("maximum :",max(my_list))
print("minimum :" , min(my_list))

    