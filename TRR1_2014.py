def binary(n):
    for i in range(2**n):
        xau = bin(i)[2:].zfill(n)
        if "1" * k in xau:
            print(xau)

n,k = map(int,input().split())
binary(n)
        