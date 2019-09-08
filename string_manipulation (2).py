a="this is my car."
t = ""
for letter in a:
    if letter in " .":
        t=t+"ly"+letter
    else:
        t=t+letter
print(a)
#print(t)
b=a.split(" ")
d=[]
for i in range (len(b)):
    b[i]=b[i]+"ly"
    e=[]
    for letter in b[i]:
        e.append(letter)
    temp=e[0]
    e[0]=e[1]
    e[1]=temp
    e = "".join(e)
    d.append(e)
f = " ".join(d)
print(f)
    
        
