numb = int(input())
arr = [numb]
for i in range(1, (numb // 2) + 1):
    if numb % i == 0:
        arr.append(i)
print(sum(arr))

# ВВОД:
# 50
# ВЫВОД:
# 93

# ВВОД:
# 2000214
# ВЫВОД:
# 4482324