def computetemparature(fahrenheit) :
    #print("computetemparature" , celcius)
    celcius = (fahr - 32.0) * 5.0 / 9.0
    return celcius
    print("returning :"  , celcius)

    



inp = input(' Enter fahrenheit temparature : ')

fahr = float(inp)

#celcius = (fahr - 32.0) * 5.0 / 9.0
#print(celcius)

xp = computetemparature(fahr)

print(xp)

