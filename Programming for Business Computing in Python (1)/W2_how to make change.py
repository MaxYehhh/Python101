expense = int(input())
change = 1000 - expense
a = change // 500
b = (change - 500*a) // 100
c = (change - 500*a - 100*b) // 50
d = (change - 500*a - 100*b - 50*c) // 10
e = (change - 500*a - 100*b - 50*c - 10*d) // 5
f = (change - 500*a - 100*b - 50*c - 10*d - 5*e) // 1
print(a,b,c,d,e,f)