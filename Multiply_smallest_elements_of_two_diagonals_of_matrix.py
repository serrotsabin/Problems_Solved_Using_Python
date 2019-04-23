a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]

d1=[]
d2=[]

for i in range(len(a)):
    for j in range(len(a[0])):
        if i==j:
            d1.append(a[i][j])
        if (i+j==len(a)-1):
            d2.append(a[i][j])
num1 = min(d1)
num2=min(d2)

print(num1*num2)
