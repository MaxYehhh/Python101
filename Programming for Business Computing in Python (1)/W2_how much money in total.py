# try:
#     w = int(input())
#     if 0 <= w <= 10:
#         total = 50*w
#     else:
#         print('invalid value')
#         quit()
#     x = int(input())
#     if 0 <= x <= 10:
#         total = 50*w + 10*x
#     else:
#         print('invalid value')
#         quit()
#     y = int(input())
#     if 0 <= y <= 10:
#         total = 50*w + 10*x + 5*y
#     else:
#         print('invalid value')
#         quit()
#     z = int(input())
#     if 0 <= z <= 10:
#         total = 50*w + 10*x + 5*y + 1*z
#     else:
#         print('invalid value')
#         quit()
# except:
#     print('Error,please enter integer')
#     quit()
# print(total)

w = int()
x = int()
y = int()
z = int()

try:
    w = int(input())
except:
    print('Please enter integer')
    quit()
if 0 <= w <= 10:
    total = 50*w
else:
    print('Please enter an integer between 0 to 10')
    quit()

try:
    x = int(input())
except:
    print('Please enter integer')
    quit()
if 0 <= x <= 10:
    total = 50*w + 10*x
else:
    print('Please enter an integer between 0 to 10')
    quit()

try:
    y = int(input())
except:
    print('Please enter integer')
    quit()
if 0 <= y <= 10:
    total = 50*w + 10*x + 5*y
else:
    print('Please enter an integer between 0 to 10')
    quit()

try:
    z = int(input())
except:
    print('Please enter integer')
    quit()
if 0 <= z <= 10:
    total = 50*w + 10*x + 5*y + 1*z
else:
    print('Please enter an integer between 0 to 10')
    quit()

print('Total:',total)
