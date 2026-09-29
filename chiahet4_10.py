n = 0
for i in range(999,5001):
    if i % 4 == 0 or i % 10 == 0:
        n += 1
print(n)