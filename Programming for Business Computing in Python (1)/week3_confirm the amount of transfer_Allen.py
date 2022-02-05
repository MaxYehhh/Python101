
# advanced make change
ans = ""

pay = int(input('how much do you pay: '))

payback = 1000 - pay
coin = [500, 100, 50, 10, 5, 1]

if 0 < pay <= 1000:
  for i in coin:
    quantity = payback // i
    if quantity == 0:
        continue
    ans +=  str(i) + ", " + str(quantity) + "; "
    payback -= quantity*i

print(ans[:-2])



# # account1:x1 account2:x2 account1 to account2:y, 0~100000

# x1 = int(input('$ of account 1:'))
# x2 = int(input('# of account 2:'))
# y = int(input('$ that account1 to accout2:'))

# if 0 <= x1 <= 100000 and 0 <= x2 <= 100000 and 0 <= y <= 100000:
#     if x1 > y:
#         x1 -= y
#         x2 += y
#     else:
#         x2 += x1
#         x1 = 0
# print(x1 , x2)
