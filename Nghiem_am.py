a , b = map(float,input().split())
if a == 0 and b == 0:
    print("1")
else:
    x = -b/a
    if x < 0:
        print("1")
    else:
        print("0")