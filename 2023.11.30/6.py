take = input()
first = take[0:3]
second = take[3:]
one = 0
two = 0
for digit in first:
    one += int(digit)
for digit in second:
    two += int(digit)
if one == two:
    print('да')
else:
    print('нет')


# ВВОД:    
# 525255
# ВЫВОД:
# да
