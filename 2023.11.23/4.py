pos1 = input()
pos2 = input()
sum1 = ord(pos1[0]) + int(pos1[1])
sum2 = ord(pos2[0]) + int(pos2[1])
if sum1 % 2 == sum2 % 2:
    print('да')
else:
    print('нет')
    
# ввод 1:
# a1
# b2
# вывод 1:
# да

# ввод 2:
# a1
# b1
# вывод 1:
# нет