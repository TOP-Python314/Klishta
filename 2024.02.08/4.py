from pathlib import Path
from sys import path
import csv

class CountableNouns:
    db_path = Path(path[0])
    words = dict()
    with open('words.csv', newline='', encoding='utf-8') as filein:
        test = csv.reader(filein, delimiter=' ', quotechar='|')
        for line in test:
            line = line[0].split(',')
            key_word = line.pop(0)
            line = tuple(line)
            words[key_word] = line
    def __init__(self):
        pass

    def test(self):
        return self.words

    def save_words(word=None):
        if word is None:
            word_1 = input('введите слово, согласующееся с числительным "один": ')
            word_2 = input('введите слово, согласующееся с числительным "два": ')
            word_3 = input('введите слово, согласующееся с числительным "пять": ')
        else:
            word_1 = word
            print(f'существительное "{word}" отсутствует в базе')
            word_2 = input('введите слово, согласующееся с числительным "два": ')
            word_3 = input('введите слово, согласующееся с числительным "пять": ')
        with open('words.csv', newline='', encoding='utf-8', mode='a') as fileout:
            test = csv.writer(fileout, dialect='excel', lineterminator='\n')
            test.writerow([word_1,word_2,word_3])
        with open('words.csv', newline='', encoding='utf-8') as filein:
            test = csv.reader(filein, delimiter=' ', quotechar='|')
            for line in test:
                line = line[0].split(',')
                key_word = line.pop(0)
                line = tuple(line)
                CountableNouns.words[key_word] = line
    
    def pick(number, word):
        if word in CountableNouns.words:
            number = number % 10
            if number <= 1:
                return word
            elif 2 <= number <= 4:
                return CountableNouns.words[word][0]
            elif 5 <= number <= 9:
                return CountableNouns.words[word][1]
        else:
            CountableNouns.save_words(word)
        
        
# ПРОВЕРКА:
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(22,'год')
# 'года'
# >>> CountableNouns.pick(15,'месяц')
# 'месяцев'
# >>> CountableNouns.pick(1,'принц')
# существительное "принц" отсутствует в базе
# введите слово, согласующееся с числительным "два": принца
# введите слово, согласующееся с числительным "пять": принцев
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'принц': ('принца', 'принцев')}
# >>> CountableNouns.save_words()
# введите слово, согласующееся с числительным "один": начальник
# введите слово, согласующееся с числительным "два": начальника
# введите слово, согласующееся с числительным "пять": начальников
# >>> CountableNouns.save_words()
# введите слово, согласующееся с числительным "один": пень
# введите слово, согласующееся с числительным "два": пня
# введите слово, согласующееся с числительным "пять": пней
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'принц': ('принца', 'принцев'), 'начальник': ('начальника', 'начальников'), 'пень': ('пня', 'пней')}