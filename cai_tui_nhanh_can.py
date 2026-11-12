
def upper_bound(i, total_weight, total_value):
    remain = b - total_weight
    bound = total_value
    j = i

    while j < n and remain > 0:

        if a[j] <= remain:
            remain -= a[j]
            bound += c[j]

        else:
            bound += (c[j] * remain + a[j] - 1) // a[j]
            break

        j += 1

    return bound


def update_best(total_value):
    global best, best_x

    if total_value > best:
        best = total_value
        best_x = [0] * n

        for i in range(n):
            best_x[order[i]] = x[i]


def knapsack(i, total_weight, total_value):

    if i == n:
        update_best(total_value)
        return

    # Kiem tra can tren
    if upper_bound(i, total_weight, total_value) <= best:
        return

    # Nhanh 1: Chon do vat
    if total_weight + a[i] <= b:
        x[i] = 1
        knapsack(i + 1,
                 total_weight + a[i],
                 total_value + c[i])

    # Nhanh 0: Khong chon do vat
    x[i] = 0
    knapsack(i + 1, total_weight, total_value)


n, b = map(int, input().split())

items = []

for i in range(n):
    w, v = map(int, input().split())
    items.append((w, v, i))

# Sap xep theo gia tri / trong luong giam dan
items.sort(key=lambda item: item[1] / item[0], reverse=True)

a = [item[0] for item in items]
c = [item[1] for item in items]
order = [item[2] for item in items]

x = [0] * n
best_x = [0] * n
best = 0

knapsack(0, 0, 0)

print(best)
print(*best_x)
