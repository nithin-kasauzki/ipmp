a = eval(input())
hash = []

for i in a:
    if (a.count(i) % 2 == 1):
        print(i)
        break
