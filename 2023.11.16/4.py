numb = int(input('Введите трёхзначное число: '))
third_numb = numb % 10
aNumb = numb // 10
second_numb = aNumb % 10
first_numb = aNumb // 10
print(f'Сумма цифр = {first_numb + second_numb + third_numb}', f'Произведение цифр = {first_numb * second_numb * third_numb}', sep = '\n')

# Ввод: 123
# Вывод: 
# Сумма цифр = 6
# Произведение цифр = 6