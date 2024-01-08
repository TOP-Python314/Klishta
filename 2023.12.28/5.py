from pathlib import Path
from sys import path
from datetime import datetime

def logger(func_obj: 'function') -> 'function':
    """Функция-обёртка для  указания декорируемой функции и её параметров при выводе"""
    def wrapper(*args, **kwargs):
        base_dir = Path(path[0])
        file_location_dir= base_dir / 'data/function_calls.log'
        today = datetime.now()
        time = str(today).split('.')[0]
        
        try:
            with open(file_location_dir, mode='a', encoding='UTF-8') as file_out:
                print(f'{time} - {func_obj.__name__}(', end="",file=file_out)
            a = func_obj.__kwdefaults__
            one = kwargs
            for key in a.keys():
                if key in one.keys():
                    continue
                else:
                    one[key] = a[key]
            with open(file_location_dir, mode='a', encoding='UTF-8') as file_out:
                print(*args, sep=', ', end = "",file=file_out)
                for key in one.keys():
                    print(f', {key} = {one[key]}',end='',file=file_out)
                print(f') -> {func_obj(*args,**kwargs)}',file=file_out)
            return func_obj(*args, **kwargs)
        except Exception as exc:
            with open(file_location_dir, mode='a', encoding='UTF-8') as file_out:
                print(f') -> {exc}',file=file_out)
            return exc  
    return wrapper

@logger
def div_round(num1, num2, *, digits=0):
    return round(num1 / num2, digits)


# ПРОВЕРКА:
# >>> def test_func():
# ...     pass
# ...
# >>> test_func = logger(test_func)
# >>> test_func()
# AttributeError("'NoneType' object has no attribute 'keys'")
# >>> div_round(24,7,digits=2)
# 3.43
# ВЫВОД:
# 2024-01-08 17:11:27 - test_func() -> 'NoneType' object has no attribute 'keys'
# 2024-01-08 17:11:57 - div_round(24, 7, digits = 2) -> 3.43
