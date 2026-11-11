import math

def travel(i, curr_cost):
    global best, best_tour
    
    # Điều kiện cắt tỉa (Nhánh cận):
    # Còn (n - i) cạnh nữa mới hoàn thành vòng đi, mỗi cạnh tốn ít nhất c_min
    if curr_cost + (n - i) * c_min >= best:
        return

    # Khi đã đi qua đủ n thành phố
    if i == n:
        total_cost = curr_cost + C[p[n - 1]]
        if total_cost < best:
            best = total_cost
            best_tour = p[:]
        return

    for v in range(1, n):
        if v not in used:
            used.add(v)
            p[i] = v
            # Truyền thêm chi phí cộng dồn vào bước đệ quy tiếp theo
            travel(i + 1, curr_cost + C[p[i - 1]][v])
            used.remove(v)

n = int(input())
C = [list(map(int, input().split())) for _ in range(n)]

# Tìm cạnh có trọng số nhỏ nhất (khác 0) để làm cơ sở tính cận dưới
c_min = math.inf
for r in range(n):
    for c in range(n):
        if r != c and C[r][c] < c_min:
            c_min = C[r][c]

p = [0] * n
used = {0}
best = math.inf
best_tour = None

# Bắt đầu từ đỉnh 0 với chi phí hiện tại bằng 0
travel(1, 0)

print(best)
print(*best_tour, 0)
