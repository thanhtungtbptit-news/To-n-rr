n, k = map(int,input().split())

a = [0] * k
used = [False] * (n+1)

def quay_lui(i):
    if i == k:
        print(*a)
        return

    for v in range( 1, n+1):
        if not used[v]:
            a[i] = v
            used[v] = True

            quay_lui(i+1)

            used[v] = False
quay_lui(0)
