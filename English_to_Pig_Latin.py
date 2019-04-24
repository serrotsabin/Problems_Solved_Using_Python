a = "Smile is good"

print(a)
a = a.lower()
a = a.split(' ')
count=0
f=[]
for i in range(len(a)):
    conso = ''
    count = 0
    for word in a[i]:
        if word not in "aeiou":
            conso=conso+word
            count = count +1
        if word in "aeiou":
            break
    b=''
    if count != 0:
        b = a[i][count:]
        b = b+conso+'ly'
        f.append(b)
    else:
        b = a[i]+'ay'
        f.append(b)
c =" ".join(f)
print(c)
