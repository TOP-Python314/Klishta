quant = int(input())

if quant > 1:
    first = '0' * quant
    first = '1' + first[:-1]
    low = int(first)
    second = '9' * quant
    high = int(second)
    good_nums = []
    for i in range(low, high):
        n = 0
        for j in range(2, i//2 + 1):
            if i % j != 0:
                continue
            elif i % j == 0:
                n += 1
        if n == 0:
            good_nums.append(i)
        n = 0
    print(len(good_nums))
elif quant == 1: 
    print('5')
else:
    print('error alerm')


# ВВОД:
# 3
# ВЫВОД:
# 143

# ВВОД:
# 2
# ВЫВОД:
# 21

# ВВОД:
# 4
# ВЫВОД:
# 1061
