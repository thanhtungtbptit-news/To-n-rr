import math

def travel(i):
    if i == n:
        update_best()
        return
    for v in range(1, n):
        if v not in used:
            used.add(v)
            p[i] = v
            travel(i + 1)
            used.remove(v)

def update_best():
    global best, best_tour
    total_cost = sum(C[p[i]][p[i + 1]] for i in range(n - 1))
    total_cost += C[p[n - 1]][p[0]]
    if total_cost < best:
        best = total_cost
        best_tour = [0] * n
        for i in range(n):
            best_tour[i] = p[i]
                

n = int(input())
C = [None] * n
for i in range(n):
    C[i] = list(map(int, input().split()))
p = [0] * n
used = set()
used.add(0)
best = math.inf
best_tour = None
travel(1)
print(best)
print(*best_tour, 0)
