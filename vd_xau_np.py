def next_binary(a):
    i = len(a) - 1
    while i >= 0 and a[i] == "1":
        i -= 1
    if i == -1:
        return False
    a[i] = "1"
    for j in range( i+1, len(a)):
        a[j] = "0"
    return True

a = list(input().strip())
print("".join(a) if next_binary(a) else "NO NEXT")