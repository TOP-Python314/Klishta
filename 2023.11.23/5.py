pos1 = input()
pos2 = input()
if pos1[0] == pos2[0] and pos1[1] == pos2[1]:
    print('нет')
elif pos1[0] == pos2[0] or pos1[1] == pos2[1]:
    print('да')
else:
    print('нет')


# Ввод 1:
# d1
# d5
# Вывод 1:
# да
# Ввод 2:
# d5
# e1
# Вывод 2:
# нет