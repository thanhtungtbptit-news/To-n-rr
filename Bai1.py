n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = []

for i in range(n):
    if A[i] == B[i] == 1:
        ans.append(i+1)

q = len(ans)
print(q)
if q > 0:
    print(*ans)