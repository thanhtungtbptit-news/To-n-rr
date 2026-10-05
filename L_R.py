import math

L, R, a, b = map(int,input("Nhập giá trị yêu cầu : ").split())
# L//a - (L-1) // a 
BCNN = a*b // math.gcd(a,b)

# A + B - 2C

A = R // a - (L-1) // a

B = R // b - (L-1) // b

C = R // BCNN - (L-1) // BCNN

ans = A + B - 2*C
print("số nguyên chia hết cho a hoặc b trong khoảng [L,R] là : ",ans)