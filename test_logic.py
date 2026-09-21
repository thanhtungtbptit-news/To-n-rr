print(" p | q | p -> q ")
for q in [0,1]:
    for p in [0,1]:
        a = (not p) or q
        print(f" {p} | {q} | {int(a)} ")