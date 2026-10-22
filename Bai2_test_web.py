a,b,c = list(map(float,input().split()))

delta = b**2-4*a*c

if a == 0:
    if b == 0:
        if c == 0:
            print("1")
        else:
            print("0")
    else:
        if -c/b > 0 :
            print("1")
        else:
            print("0")
else:
    if delta < 0:
        print("0")
    else:
        P = c/a
        S = -b/a
        if P < 0 or (P >=0 and S > 0):
            print("1")
        else:
            print("0")