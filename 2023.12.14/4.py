def countable_nouns(digit : int, words : tuple[str, str, str]) -> str:
""" Согласовывает числительное со словом  """
    digit_str = str(digit)
    if digit != 11 and digit_str.endswith('1'):
        return words[0]
    elif digit_str.endswith('2') and digit != 12 or digit_str.endswith('3') and digit != 13 or digit_str.endswith('4') and digit != 14:
        return words[1]
    else:
        return words[2]
        

# Проверка:
# >>> countable_nouns(17, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(11, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(135, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(132, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(6, ("год", "года", "лет"))
# 'лет'