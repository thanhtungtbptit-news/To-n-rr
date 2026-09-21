n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = []

for i in range(n):
    if a[i] == 1 and b[i] == 0:
        ans.append(i+1)
print(len(ans))
if len(ans) > 0:
    print(*ans)

