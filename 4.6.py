def coumputepay( hours , rate) :
    print("computepay" , hours, rate)

    if fh > 40 :

        reg = rate * hours
        opt = (hours - 40.0) * (rate * 0.5)
        pay = reg + opt

    else:

        pay = hours * rate 
    print ("returning :"  , pay)
    return pay 
    
    
sh = input("enter Hour ")
sr = input("enter Rate ")

fh = float(sh)
fr = float(sr)

xp = coumputepay(fh , fr)

print("pay :" , xp)



