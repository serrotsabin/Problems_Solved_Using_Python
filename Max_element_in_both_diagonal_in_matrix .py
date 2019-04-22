a=[[1, 2, 3],
   [4 ,5 ,6],
   [7 ,8, 9]]

m=3
n=3

l1=[]
l2=[]
for i in range (m):
    for j in range (n):
        if (i == j):
            l1.append(a[i][j])
        if (i+j==m-1):
            l2.append(a[i][j])
print (l1)
print (l2)
a = max(l1)
b=max(l2)
print (max(a,b))
