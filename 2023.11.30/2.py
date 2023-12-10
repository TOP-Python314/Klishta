times = int(input())
numbs_list = []
for i in range(times):
    a = int(input())
    numbs_list.append(a)
exit_digit = 0
for numb in numbs_list:
    if numb > 0:
        exit_digit += numb
    else:
        continue
print(exit_digit)
    
    
# ВВОД:
# 11
# 24
# -3
# -7
# 0
# ВЫВОД:
# 35

    