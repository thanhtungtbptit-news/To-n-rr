from functools import cache
n = int(input())
C = [list(map(int,input().split()))for _ in range(n)]

@cache
def shortest(u, mask):
    if mask == 0:
        return C[u][0]
    best = float('inf')

    for v in range(1, n):
        if not (mask >> v) & 1:
            continue
        rest = mask ^ (1 << v)
        tail = shortest(v, rest)
        cost = C[u][v] + tail
        best = min(best, cost)
    return best

remaining = (1 << n) - 2
print(shortest(0, remaining))