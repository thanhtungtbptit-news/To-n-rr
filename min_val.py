n = int(input())
arr = list(map(float,input().split()))
min_val = arr[0]
for i in range(1,n):
    if arr[i] < arr[0]:
        min_val = arr[0]
print(min_val)

