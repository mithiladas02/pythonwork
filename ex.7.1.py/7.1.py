

fname=input("enter the file name:")
try:
    fhand=open(fname)
except:
    print('file cannot be opened :', fname)
    quit()

for lx in fhand:
    ly=lx.rstrip()
    print(ly.upper())