#print("searching for a value 3")
#or i in[9,41,12,3,74,15]:
#    if i==3:
#        print("true",i)
#    elif i!=3:
#        print(i)1x
print("find the smallest value")
small= None
for i in[9,41,12,3,74,15]:
    #if small is none replace it with i
    if small is None:
        small=i
#if i is smaller than small replace small with i
    elif i<small:
        small=i
print("smallest value is: ",small)
