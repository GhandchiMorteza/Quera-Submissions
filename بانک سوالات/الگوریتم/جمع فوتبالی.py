t = int(input())
for _ in range(t):
    ph, eg, pg, eh = list(map(int, input().split()))
    p = ph + pg
    e = eh + eg
    if p > e:
        print("perspolis")
    elif e > p:
        print("esteghlal")
    else:
        if eg > pg:
            print("esteghlal")
        elif pg > eg:
            print("perspolis")
        else:
            print("penalty")