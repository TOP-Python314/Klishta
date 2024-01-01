def deck() -> tuple:
    """Создаёт колоду карт"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    wards = ['черви', "бубны", "пики", "трефы"]
    for ward in wards:
        for numbs in cards:
            resume = [numbs, ward]
            resume = tuple(resume)
            yield resume

# ПРОВЕРКА:
# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]