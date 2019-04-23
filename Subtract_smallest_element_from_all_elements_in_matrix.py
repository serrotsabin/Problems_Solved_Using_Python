a = [
    [1,2,3,4],
    [5,4,6,7],
    [2,3,6,7]]
b=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        b.append(a[i][j])
small=min(b)
print(small)

for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j]=a[i][j]-small

print(a)
