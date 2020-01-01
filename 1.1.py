sh=input("enter hours :")
sr=input("enter rate :")

fh=float(sh)
fr=float(sr)

if fh > 40 :
    reg= fh * fr
    exh=(fh - 40) * (fr * .5)
    ep=(reg + exh)

    print(ep)

else:
    ep= fh * fr
    print(ep)    

