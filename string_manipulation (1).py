a = "this is my car"
b = a.split(" ")
print(b)
n = len(b)
for i in range(n):
    b[i] = b[i] + 'ly'
print(b)
c=[]
d = []
for i in range(n):
    c=[]
    for items in b[i]:
        c.append(items)
    temp=c[0]
    c[0]=c[1]
    c[1]=temp
    d.append(c)
print(d)
t=[]
for i in range (len(d)):
    e="".join(d[i])
    t.append(e)
print (t)
f=" ".join(t)
print (f)


