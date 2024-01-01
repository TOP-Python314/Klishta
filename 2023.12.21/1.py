
def pick_resistors(num: int) -> dict:
    """Вычисляет ближайшие сопротивления резистора, в зависимости от передаваемого номинала"""
    nominals = {
    'E6': (
        100, 150, 220, 330, 470, 680
    ),
    'E12': (
        100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820
    ),
    'E24': (
        100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910
    ),
    'E48': (
        100, 105, 110, 115, 121, 127, 133, 140, 147, 154, 162, 169, 178, 187, 196, 205, 215, 226, 237, 249, 261, 274, 287, 301, 316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536, 562, 590, 619, 649, 681, 715, 750, 787, 825, 866, 909, 953
    ),
    'E96': (
        100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130, 133, 137, 140, 143, 147, 150, 154, 158, 162, 165, 169, 174, 178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232, 237, 243, 249, 255, 261, 267, 274, 280, 287, 294, 301, 309, 316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412, 422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549, 562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732, 750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976
    )
}
    zero = list(nominals['E6'] + (num,))
    zero.sort()
    first = list(nominals['E12'] + (num,))
    first.sort()
    second = list(nominals['E24'] + (num,))
    second.sort()
    third = list(nominals['E48'] + (num,))
    third.sort()
    fourth = list(nominals['E96'] + (num,))
    fourth.sort()
    list_tuples = []
    list_tuples.append(zero)
    list_tuples.append(first)
    list_tuples.append(second)
    list_tuples.append(third)
    list_tuples.append(fourth)
    list_resist = []
    for item in list_tuples:
        pos = item.index(num)
        
        if pos == 0:
            list_resist.append((item[1]))
        elif pos == len(item):
            list_resist.append((item[len(item)-1]))
        else:
            pos_pre = item[pos-1]
            pos_post = item[pos+1]
            if num - pos_pre < pos_post - num:
                list_resist.append((pos_pre,))
            elif num - pos_pre > pos_post - num:
                list_resist.append((pos_post,))
            else:
                list_resist.append((pos_pre, pos_post))
    result = dict()
    result['E6'] = list_resist[0]
    result['E12'] = list_resist[1]
    result['E24'] = list_resist[2]
    result['E48'] = list_resist[3]
    result['E96'] = list_resist[4]
    return result


# ПРОВЕРКА:

# >>> pick_resistors(112)
# {'E6': (100,), 'E12': (120,), 'E24': (110,), 'E48': (110,), 'E96': (113,)}

# >>> pick_resistors(549)
# {'E6': (470,), 'E12': (560,), 'E24': (560,), 'E48': (536, 562), 'E96': (549,)}