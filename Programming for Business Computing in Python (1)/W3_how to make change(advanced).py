try:
    expense = int(input())
except:
    print('Please enter an integer')
    quit()
if 1 <= expense <= 999:
    expense = expense
else:
    print('Please enter an amount between 1 to 999')
    quit()

change = 1000 - expense
a = change // 500
b = (change - 500*a) // 100
c = (change - 500*a - 100*b) // 50
d = (change - 500*a - 100*b - 50*c) // 10
e = (change - 500*a - 100*b - 50*c - 10*d) // 5
f = (change - 500*a - 100*b - 50*c - 10*d - 5*e) // 1
result = ''

if a != 0:
    result = '500, ' + str(a) + '; '
if b != 0:
    result = result + '100, ' + str(b) + '; '
if c != 0:
    result = result + '50, ' + str(c) + '; '
if d != 0:
    result = result + '10, ' + str(d) + '; '
if e != 0:
    result = result + '5, ' + str(e) + '; '
if f != 0:
    result = result + '1, ' + str(f) + '; '

print(result[:-2])  #索引'-'代表從後面數回來
# for calculate in [a,b,c,d,e,f]:
#     if calculate is True:
#         A = print('500,',a,';')
#         B = print('100,',b,';')
#         C = print('50,',c,';')
#         D = print('10,',d,';')
#         E = print('5,',e,';')
#         F = print('1,',f,';')
#     else:
#         continue
# print(A,B,C,D,E,F)

# print('500,',a,'; ','100,',b,'; ','50,',c,'; ','10,',d,'; ','5,',e,'; ','1,',f,'; ')