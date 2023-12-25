apex = [1, 2, 3, 4, 5]
def numbers_strip(numbs: list[float], n: int =1, copy: bool =False) -> list:
"""                       Работа с передаваемым списком.                       """
    if copy:
        numbs_copy = numbs[::1]
        if n > 0 and len(numbs_copy) >= n*2:
            for i in range(n):
                numbs_copy.remove(max(numbs_copy))
                numbs_copy.remove(min(numbs_copy))
            return(numbs_copy)
        else:
            return('errore')
    else:
        if n > 0 and len(numbs) >= n*2:
            for i in range(n):
                numbs.remove(max(numbs))
                numbs.remove(min(numbs))
            return(numbs)
        else:
            return('2 error')
            
            
# Тест 1:
# >>> apex
# [1, 2, 3, 4, 5]
# >>> test = numbers_strip(apex)
# >>> test
# [2, 3, 4]
# >>> apex is test
# True
# >>>

# Тест 2:
# >>> apex
# [1, 2, 3, 4, 5]
# >>> test = numbers_strip(apex, n=2, copy=True)
# >>> test
# [3]
# >>> test is apex
# False
# >>> apex
# [1, 2, 3, 4, 5]