def binary(n):
    for i in range(2**n):
        xau = bin(i)[2:].zfill(n)
        if "1" * k in xau:
            print(xau)

n=int(input("Nhap do dai n: "))
k=int(input("Nhap do dai k: "))
binary(n)
        