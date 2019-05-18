a = [1,2,3,4,5,6,7,8,9]

print(a)
t = a[:2]


t2=a[2:]

t2.append(t[0])
t2.append(t[1])

a = t2
print(a)
