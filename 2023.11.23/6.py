pos1 = input()
pos2 = input()
if ord(pos1[0]) - 1 <= ord(pos2[0]) <= ord(pos1[0]) + 1 and int(pos1[1]) - 1 <= int(pos2[1]) <= int(pos1[1]) + 1:
    print("да")
else:
    print('нет')
    
# Ввод 1:
# g3
# f2
# Вывод 1:
# да
# Ввод 2:
# c6
# d4
# Вывод 2:
# нет