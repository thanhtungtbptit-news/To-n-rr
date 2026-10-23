a,b = list(map(float,input().split()))
x = a*b
if a == 0:
    if b == 0:
        print("1")
    else:
        print("0")
else:
    if x > 0:
        print("1")
    else:
        print("0")
            
