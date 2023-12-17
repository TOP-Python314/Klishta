doubles = {'1', '0'}
number = input()
if number.startswith('0b'):
    test = set(number[2:])
    if  test <= doubles:
        print('да')
    else:
        print('нет')
elif number.startswith('b'):
    test = set(number[1:])
    if test <= doubles:
        print('да')
    else:
        print('нет')
elif number.startswith('0') or number.startswith('1'):
    test = set(number)
    if test <= doubles:
        print('да')
    else:
        print("нет")
else:
    print('нет')


# ВВОД:
# 10101003
# ВЫВОД:
# нет

# ВВОД:
# 0b1010
# ВЫВОД:
# да

# ВВОД:
# 1b0101
# ВЫВОД:
# нет