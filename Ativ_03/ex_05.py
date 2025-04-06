a = [1,5,7,9,2,1]
b = a[0]
x = 0
for x in range(1, len(a)):
    if a[x] > b:
        b = a[x]
        b = x
print(b)
