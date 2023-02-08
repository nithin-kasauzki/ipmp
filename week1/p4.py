# n(n+1)/2 - sumofarray
# or another aproach

a = [1, 2, 3, 4, 5, 7, 8]

for i in range(len(a)):
    if (a[i] != i+1):
        print(i+1)
        break
