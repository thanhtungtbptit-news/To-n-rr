n , k, t =map(int,input().split())
a = list(map(int,input().split()))

for i in range (t):
    i = k-1

    while i >= 0 and a[i] == n - k + i + 1:
        i -= 1

    if i < 0:
        print(0)
        break

    a[i] += 1
    for j in range ( i+1, k):
        a[j] = a[j-1] + 1

    print(*a)