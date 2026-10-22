a,b = list(map(float,input().split()))

if a == 0:
    if b == 0:
        print("1")
    else :
        print("0")
else:
    if a * b > 0:
        print("1")
    else:
        print("0")
