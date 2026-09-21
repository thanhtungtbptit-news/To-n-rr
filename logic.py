print (" p | q | r | p V (q ^ r) | (p v q) ^ (p v r)")
print ("---|---|---|-------------|-----------------|")
menh_de=0

for r in [0,1]:
    for q in [0,1]:
        for p in [0,1]:
            a = p or ( q and r)
            b = (p or q) and (p or r)
            if a != b:
                menh_de += 1
            print(f" {p} | {q} | {r} |      {a}      |        {b}  ")

if menh_de > 0 :
    print("Hai mệnh đề không tương đương")
else:
    print("Hai mệnh đề tương đương")