a = [1,2,3,4,5]
for i in range(1, 5):
    a[i-2] = a[i]
for i in range(0,5):
    print(a[i], end=" ")
    