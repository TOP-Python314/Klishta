numb = input().split()
digit = 0
for items in numb:
    digit += len(items)

price = digit * 30
rubles = price // 100
cents = price % 100
print(f'{rubles} руб. {cents} коп.')

# Ввод:
# грузите апельсины бочках братья карамазовы
# Вывод:
# 11 руб. 40 коп.

# Ввод:
# И если только дашь слабину, он опрокинет с такой силой тебя, что больше уже не встанешь. Ни ты, ни я, никто на свете не бьет так сильно, как ЖИЗНЬ. Совсем не важно, как ты ударишь, а важно, КАКОЙ ДЕРЖИШЬ УДАР, как двигаешься вперед.
# Вывод:
# 57 руб. 0 коп.