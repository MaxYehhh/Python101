c = int(input("Enter c: "))
r = int(input("Enter r: "))
n = int(input("Enter N: "))
# q = int(input())
p0 = float(input("Enter p0: "))
p1 = float(input("Enter p1: "))
p2 = float(input("Enter p2: "))
p3 = float(input("Enter p3: "))
p4 = float(input("Enter p4: "))
p5 = float(input("Enter p5: "))
p6 = float(input("Enter p6: "))
p7 = float(input("Enter p7: "))
p8 = float(input("Enter p8: "))

# Version 1

# Q = int()
# q = 0
# ep = 0
# max_ep = 0

# for Q in range(0,q+1):
#     if Q == 0:
#         ep += r*Q*p0
#     elif Q == 1:
#         if q == 1:
#             ep = ep + r*Q*(1-p0)
#             # break
#         else:
#             ep = ep + r*Q*p1
#             continue
#     elif Q == 2:
#         if q == 2:
#             ep = ep + r*Q*(1-p0-p1)
#             # break
#         else:
#             ep = ep + r*Q*p2
#             continue
#     elif Q == 3:
#         if q == 3:
#             ep = ep + r*Q*(1-p0-p1-p2)
#             # break
#         else:
#             ep = ep + r*Q*p3
#             continue
#     elif Q == 4:
#         if q == 4:
#             ep = ep + r*Q*(1-p0-p1-p2-p3)
#             # break
#         else:
#             ep = ep + r*Q*p4
#             continue
#     elif Q == 5:
#         if q == 5:
#             ep = ep + r*Q*(1-p0-p1-p2-p3-p4)
#             # break
#         else:
#             ep = ep + r*Q*p5
#             continue
#     elif Q == 6:
#         if q == 6:
#             ep = ep + r*Q*(1-p0-p1-p2-p3-p4-p5)
#             # break
#         else:
#             ep = ep + r*Q*p6
#             continue
#     elif Q == 7:
#         if q == 7:
#             ep = ep + r*Q*(1-p0-p1-p2-p3-p4-p5-p6)
#             # break
#         else:
#             ep = ep + r*Q*p7
#             continue
#     elif Q == 8:
#         if q == 8:
#             ep = ep + r*Q*(1-p0-p1-p2-p3-p4-p5-p6-p7)
#             # break
#         else:
#             ep = ep + r*Q*p8
#             continue
#     elif Q > 8:
#         Q == 0
#         q = q - 8
#         continue
#     if ep >= max_ep:
#         max_ep = ep
#         q += 1
#         continue
#     else:
#         break

# C = c*q
# EP = max_ep - C

# print(q," ",int(EP))

q = 0
s0 = 0 * p0
s1 = 1 * p1
s2 = 2 * p2
s3 = 3 * p3
s4 = 4 * p4
s5 = 5 * p5
s6 = 6 * p6
s7 = 7 * p7
s8 = 8 * p8
d1 = 1 * (1 - p0)
d2 = 2 * (1 - p0 - p1)
d3 = 3 * (1 - p0 - p1 - p2)
d4 = 4 * (1 - p0 - p1 - p2 - p3)
d4 = 4 * (1 - p0 - p1 - p2 - p3)
d5 = 5 * (1 - p0 - p1 - p2 - p3 - p4)
d6 = 6 * (1 - p0 - p1 - p2 - p3 - p4 - p5)
d7 = 7 * (1 - p0 - p1 - p2 - p3 - p4 - p5 - p6)

while q >= 0:
    if q == 0:
        ep0 = r * s0 - c * q
        q += 1
        continue
    elif q == 1:
        ep1 = r * (s0 + d1) - c * q
        q += 1
        continue
        # if ep2 >= ep:
        #     ep = ep2
        #     q += 1
        #     continue
        # else:
        #     break
    elif q == 2:
        ep2 = r * (s0 + s1 + d2) - c * q
        q += 1
        continue
        # if ep2 >= ep:
        #     ep = ep2
        #     q += 1
        #     continue
        # else:
        #     break
    elif q == 3:
        ep3 = r * (s0 + s1 + s2 + d3) - c * q
        q += 1
        continue
        # if ep2 >= ep:
        #     ep = ep2
        #     q += 1
        #     continue
        # else:
        #     break
    elif q == 4:
        ep4 = r * (s0 + s1 + s2 + s3 + d4) - c * q
        q += 1
        continue
        # if ep2 >= ep:
        #     ep = ep2
        #     q += 1
        #     continue
        # else:
        #     break
    elif q == 5:
        ep5 = r * (s0 + s1 + s2 + s3 + s4 + d5) - c * q
        q += 1
        continue
        # if ep2 >= ep:
        #     ep = ep2
        #     q += 1
        #     continue
        # else:
        #     break
    elif q == 6:
        ep6 = r * (s0 + s1 + s2 + s3 + s4 + s5 + d6) - c * q
        q += 1
        continue
        # if ep2 >= ep:
        #     ep = ep2
        #     q += 1
        #     continue
        # else:
        #     break
    elif q == 7:
        ep7 = r * (s0 + s1 + s2 + s3 + s4 + s5 + s6 + d7) - c * q
        q += 1
        continue
        # if ep2 >= ep:
        #     ep = ep2
        #     q += 1
        #     continue
        # else:
        #     break
    elif q >= 8:
        ep8 = r * (s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8) - c * q
        break
        # if ep2 >= ep:
        #     ep = ep2
        #     q += 1
        #     continue
        # else:
        #     break

EP = [ep0,ep1,ep2,ep3,ep4,ep5,ep6,ep7,ep8]
# Q = q - 1

print(EP.index(max(EP)),int(max(EP)))