a = input().split()
b = input().split()
a = [int(numb) for numb in a]
b = [int(numb) for numb in b]
flag = False
for i in range(len(a) - len(b) + 1):
    test = []
    for j in range(len(b)):
        test.append(a[i + j])
    if test == b:
        flag = True
        break
if flag:
    print("да")
else:
    print('нет')


# ВВОД:
# 1 2 4 5 6 7 2 5 13
# 2 4 5
# ВЫВОД:
# да

# ВВОД:
# 1 2 3 4
# 2 4
# ВЫВОД:
# нет
# да
# ВВОД:
# 1 2 3 4 11 22 33
# 4 11 22 33
# ВЫВОД:
# да