words_collect = []
word = input()
while word != "":
    words_collect.append(word)
    word = input()
for i in range(len(words_collect)):
    if i == (len(words_collect) - 1):
        print(f'и {words_collect[i]}.')
    elif (i == (len(words_collect) - 2)):
        print(words_collect[i], end=' ')
    else:
            print(words_collect[i], end=', ')

# ВВОД:
# яблоко
# груша
# лимон
# апельсин
# ВЫВОД:
# яблоко, груша, лимон и апельсин.
# ВВОД:
# Лимон
# груша
# ВЫВОД:
# Лимон и груша.