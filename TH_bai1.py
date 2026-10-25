n , k, S = list(map(int,input().split()))

a= []
res= []

def Try(start, total):
    if len(a) == k:
        if total == S:
            res.append(a.copy())
        return

    for i in range(start, n+1):
        if total + i > S:
            break

        a.append(i)
        Try(i + 1, total + i)
        a.pop()

Try(1, 0)
print(len(res))
for x in res:
    print(*x)
