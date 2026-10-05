import math

L, R, a, b = map(int,input().split())
# L//a - (L-1) // a 
BCNN = a*b // math.gcd(a,b)

# A + B - 2C
for i in range (L,R):
    A = R // a - (L-1) // a
for i in range (L,R):
    B = R // b - (L-1) // b

ans = A + B - 2*BCNN
print(ans)