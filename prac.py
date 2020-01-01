EH= input("enter hours :")
ER=input("enter rate :")
try:

    fh=float(EH)
    fr=float(ER)

except:

    print("Error ,please enter numeric input")
    quit()



if  fh > 40 :
    reg = fh * fr
    opt= (fh-40) * (fr * 0.5)
    xp = reg + opt

    print(xp)


else:
    xp= fh* fr
    print(xp)



