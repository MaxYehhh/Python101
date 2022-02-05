try:        # Q：try/except沒辦法寫出判別變數是否在範圍內
    account1 = int(input())
except:
    print('Please enter an integer')
    quit()

if 0 <= account1 <= 100000:
    a1 = account1
else:
    print('Please enter amount between 0 to 100000')
    quit()


try:
    account2 = int(input())
except:
    print('Please enter an integer')
    quit()

if 0 <= account2 <= 100000:
    a2 = account2
else:
    print('Please enter amount between 0 to 100000')
    quit()


try:
    transfer = int(input())
except:
    print('Please enter an integer')
    quit()

if 0 <= transfer <= 100000:
    transfer = transfer
else:
    print('Please enter amount between 0 to 100000')
    quit()


if account1 > transfer:
    print(a1 - transfer , a2 + transfer)
else:
    print(0 , a1 + a2)