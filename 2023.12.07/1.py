mail = input('Введите email: ')
first_singl = int(mail.find('@'))
second_singl = int(mail[first_singl:].find('.'))
if first_singl == -1:
    print('нет')
elif first_singl >= 0:
    if second_singl == -1:
        print('нет')
    else:
        print('да')
        

# ВВОД:
# Введите email: hello@mail
# ВЫВОД:
# нет

# ВВОД:
# Введите email: hello@mail.rs
# ВЫВОД:
# да