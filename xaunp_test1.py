n = int(input())
x = [0] * n

i = n - 1 # python đếm từ 0

while x[i] == 1:
    x[i] = 0 # gán = 0
    i -= 1 
    if i == 0 and i < 0:
        break
    x[i] == 1
    continue
print(*x)
