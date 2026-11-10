def knapsack(i):
    if i == n:
        update_best()
        return
    for value in range(2):
        x[i] = value
        knapsack(i + 1)
        
def update_best():
    global best, best_x
    total_weight = sum(a[i] * x[i] for i in range(n))
    total_value = sum(c[i] * x[i] for i in range(n))
    if total_weight <= b and total_value > best:
        best = total_value
        for i in range(n):
            best_x[i] = x[i]
            
n, b = map(int, input().split())
a = [0] * n
c = [0] * n
x = [0] * n
for i in range(n):
    a[i], c[i] = map(int, input().split())
best_x = [0] * n
best = 0
knapsack(0)
print(best)
print(*best_x)
