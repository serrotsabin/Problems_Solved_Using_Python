a=[
    [1,2,3,4,5],
    [5,6,0,7,6],
    [8,9,1,1,0]]

for i in range(len(a)):
    print(a[i])

m = len(a)
n = len(a[0])
print(m)
print(n)
b=[]
for i in range(m):
    for j in range(n):
        if a[i][j]==0:
            b.append([i,j])
print(b)

for item in b:
    m1=item[0]
    n1=item[1]

    for i in range(m):
        for j in range(n):
            if i==m1:
                a[i][j]=0
            if j==n1:
                a[i][j]=0

for i in range(len(a)):
    print(a[i])
