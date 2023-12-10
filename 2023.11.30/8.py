numb = int(input())

if numb > 2:
    numb_list = [1, 1]
    for i in range(numb - 2):
        test = numb_list[-1] + numb_list[-2]
        numb_list.append(test)
    for items in numb_list:
        print(items, end=" ")
elif numb == 2:
    print('1 1')
elif numb == 1:
    print('1')
    
# ВВОД:
# 17
# ВЫВОД:
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

# ВВОД:
# 21
# ВЫВОД:
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946
