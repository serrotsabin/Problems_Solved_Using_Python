a=[1,5,4,6,2,4,4,6,2,6,7,4,4,8]
a = sorted(a)
l=[]
l.append(a[0])
for i in range (len(a)-1):
    if (a[i]==a[i+1]):
        t=0
    else:
        l.append(a[i+1])
a=l
print(a)
    
