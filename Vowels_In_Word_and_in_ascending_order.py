word = "sasdafgiwnidoosdu"
a=[]
for letters in word:
    if letters in"AEIOUaeiou":
        a.append(letters)

print(a)
b = sorted(a)
print(b)

if a == b:
    print("Vowels Contained and in order")
else:
    print("Not in order")
