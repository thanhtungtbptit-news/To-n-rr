n = int(input())
a = list(map(int,input().split()))
def bubble_sort(a):
    n = len(a)
    for end in range(n-1,0,-1):
        for i in range(end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

print(*bubble_sort(a)) 