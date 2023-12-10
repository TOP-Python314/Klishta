digit_list= []
while (digit := int(input())) % 7 == 0:
    digit_list.append(digit)
    digit_list1 = digit_list[::-1]
for numbs in digit_list1:
    print(numbs, end=' ')
    
# ВВОД:
# 21
# 77
# 70
# 35
# 12
# ВЫВОД:
# 35 70 77 21