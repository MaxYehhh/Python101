c = int(input("Please enter cost: "))
r = int(input("Please enter price: "))
N = int(input("Please enter N: "))
s = int(input("Please enter residual value: "))

# D = range(N+1)
# Q = range(N+1)
p = []
max_ep = -1
EP = []

for i in range(N+1):
    p.append(float(input("Please enter p" + str(i) + ": ")))  #字串+字串合併為一個字串

for q in range(N+1):
    ep = 0
    for i in range(N+1):
        if q >= i:
            ep += (r * i - c * q + (q - i) * s) * p[i]
        else:
            ep += (r * q - c * q) * p[i]
    # if ep > max_ep:
    #     max_ep = ep
    # else:
    #     break
    EP.append(ep)

# print(q - 1 , int(max_ep))
print(EP.index(max(EP)) , int(max(EP)))