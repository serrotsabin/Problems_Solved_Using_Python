num="234-124-5678"

a=num.split("-")

component1=a[0]
component2=a[1]
component3=a[2]


if int(component1[0])>=2 and int(component1[0])<=9:
    test = 0
else:
    test = 1

if test==0:
    if int(component2[0])>=2 and int(component2[0])<=9:
        test = 0
        if int(component2[1])==1 and int(component2[2])==1:
            test=1
    else:
        test = 1

if test==0:
    print("Valid")
else:
    print("Invalid")

