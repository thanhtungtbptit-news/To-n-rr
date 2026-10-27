def binary(n):
    for i in range(2**n):
        xau = bin(i)[2:].zfill(n)
        print(xau)

n=int(input("Nhap do dai n :"))
binary(n)
        