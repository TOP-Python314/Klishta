def logger(func_obj: 'function') -> 'function':
    """Функция-обёртка для  указания декорируемой функции и её параметров при выводе"""
    def wrapper(*args, **kwargs):
        
        try:
            a = func_obj.__kwdefaults__
            one = kwargs
            for key in a.keys():
                if key in one.keys():
                    continue
                else:
                    one[key] = a[key]
            print(f'{func_obj.__name__}(', end="")
            print(*args, sep=', ', end = "")
            for key in one.keys():
                print(f', {key} = {one[key]}',end='')
            print(f') -> {func_obj(*args,**kwargs)}')
            # print(func_obj.__name__,
            #     '(',
            #     *args,
            #     one,
            #     ') ->', func_obj(*args,**kwargs), sep=" ")
            return func_obj(*args, **kwargs)
        except Exception as exc:
            print(f') -> {exc}')
            # print(func_obj.__name__,
            #     '(',
            #     *args,
            #     one,
            #     ') ->', exc, sep=" ")
            return exc  
    return wrapper
@logger
def sample(n1: int, n2: int, *, digit: int = 0, some = 3):
    return round(n1/n2 + some, digit)


# ПРОВЕРКА:
# >>> sample(2,0)
# sample(2, 0, digit = 0, some = 3) -> division by zero
# ZeroDivisionError('division by zero')
# >>> sample(2,6)
# sample(2, 6, digit = 0, some = 3) -> 3.0
# 3.0
# >>> sample(2,6,digit=5)
# sample(2, 6, digit = 5, some = 3) -> 3.33333
# 3.33333
# >>> sample(2,0,some = 0)
# sample(2, 0, some = 0, digit = 0) -> division by zero
# ZeroDivisionError('division by zero')