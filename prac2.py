#eh=input("enter hour:")
#er=input ("enter rate:")


#feh=float(eh)
#fer=float(er)

#if feh > 40 :
   # reg= feh * fer
    #ex=(feh - 40) * (fer * 0.5)
    #tp= reg + ex
    #print(tp)
#else:
 #   reg= feh * fer
  #  print(reg)

grd=input("Enter score :")

try:
    fgrd=float(grd)

except:
    print("bad score")
    

if  fgrd >= 0.9 and fgrd <=1 :
    print("A")
elif fgrd >= 0.8  and fgrd <=.9:
    print("B")
elif fgrd >=0.7 and fgrd <=.8 :
    print("C")
elif fgrd >=0.6 and fgrd <=.7 :
    print("D")
elif fgrd < 0.6 :
    print("F")

else : 
    print("error")
    



