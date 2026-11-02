n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = []
q = 0

for i in range(n):
    if A[i] == 1 and B[i] == 1:
        ans.append(i+1)
        q += 1

if q == 0:
    print("0")
elif q > 0:
    print(q)
    print(*ans)

        