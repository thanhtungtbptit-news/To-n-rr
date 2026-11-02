n , r = map(int,input().split())

dieu_kien = {}

for i in range (r):
    u, v = map(int, input().split())
    dieu_kien[u] = v

a = [0] * n
used = [False] * (n+1)
co_nghiem = False

def quay_lui(i):
    global co_nghiem

    if i == n :
        co_nghiem = True
        print(*a)
        return

    if i in dieu_kien:
        v = dieu_kien[i]

        if not used[v]:
            a[i] = v
            used[v] = True
            
            quay_lui(i + 1)

            used[v] = False

    else:
        for v in range(1, n+1):
            if not used[v]:
                a[i] = v
                used[v] = True

                quay_lui(i+1)

                used[v] = False
quay_lui(0)

if not co_nghiem:
    print(0)