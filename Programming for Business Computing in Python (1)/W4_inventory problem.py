c = int(input())
r = int(input())
n = int(input())
q = int(input())
p0 = float(input())
p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
p5 = float(input())
p6 = float(input())
p7 = float(input())
p8 = float(input())

Q = int()
for Q in range(0,q+1):
    if Q == 0:
        ep = r*Q*p0
    elif Q == 1:
        if q == 1:
            ep = ep + r*Q*(1-p0)
            break
        else:
            ep = ep + r*Q*p1
            continue
    elif Q == 2:
        if q == 2:
            ep = ep + r*Q*(1-p0-p1)
            break
        else:
            ep = ep + r*Q*p2
            continue
    elif Q == 3:
        if q == 3:
            ep = ep + r*Q*(1-p0-p1-p2)
            break
        else:
            ep = ep + r*Q*p3
            continue
    elif Q == 4:
        if q == 4:
            ep = ep + r*Q*(1-p0-p1-p2-p3)
            break
        else:
            ep = ep + r*Q*p4
            continue
    elif Q == 5:
        if q == 5:
            ep = ep + r*Q*(1-p0-p1-p2-p3-p4)
            break
        else:
            ep = ep + r*Q*p5
            continue
    elif Q == 6:
        if q == 6:
            ep = ep + r*Q*(1-p0-p1-p2-p3-p4-p5)
            break
        else:
            ep = ep + r*Q*p6
            continue
    elif Q == 7:
        if q == 7:
            ep = ep + r*Q*(1-p0-p1-p2-p3-p4-p5-p6)
            break
        else:
            ep = ep + r*Q*p7
            continue
    elif Q == 8:
        if q == 8:
            ep = ep + r*Q*(1-p0-p1-p2-p3-p4-p5-p6-p7)
            break
        else:
            ep = ep + r*Q*p8
            continue

EP = ep - c*q

print(int(EP))