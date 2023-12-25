def central_tendency(first : float, second : float, *numbers : float):
""" вычисляет основные меры центральной тенденции для некоторого количества чисел  """
    numbers = [numb for numb in numbers]
    numbers += [first]
    numbers += [second]
    quantity = int(len(numbers))
    result_dict = {}
    median = sum(numbers) / quantity
    arithmetic = sum(numbers) / quantity
    geometr = 1
    harmon = 0
    for numb in numbers:
        geometr *= numb
        harmon += (1 / numb)
    geometric = geometr**(1 / quantity)
    harmonic = quantity / harmon
    result_dict['median'] = median
    result_dict['arithmetic'] = arithmetic
    result_dict['geometric'] = geometric
    result_dict['harmonic'] = harmonic
    return result_dict
    
    
# ПРОВЕРКА:
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}

# ПРОВЕРКА 2:
# >>> examp = [1, 2, 3, 4, 5]
# >>> central_tendency(*examp)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# >>>