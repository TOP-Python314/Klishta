year = int(input())
if year % 4 != 0:
    print("нет")
elif year % 100 == 0 and year % 400 != 0:
    print("нет")
else:
    print("да")
    
# ввод 1:
# 2023
# вывод 1:
# нет
# ввод 2:
# 2024
# вывод 2:
# да