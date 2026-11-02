N , l , u = list(map(int,input().split()))
dem = 0

for x0 in range(l, min(u, N) + 1):
    dem += N -x0 + 1

print(dem)