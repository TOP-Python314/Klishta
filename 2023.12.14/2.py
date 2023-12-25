def taxi_cost(length: int, wtime: int =0) -> int | None:
    """Считает стоимость поездки исходя из передаваемы length - метраж поездки, wtime - время ожидания при поездке"""
    if length < 0 or wtime < 0:
        return None
    if length > 0:
        moneyl = length // 150 
        length_helper = length % 150
        moneyw = 0
        if length_helper >= 75:
            moneyl_sum = (moneyl + 1) * 6
        else:
            moneyl_sum = moneyl * 6
        if wtime > 0:
            moneyw = wtime * 3
        sum_money = 80 + moneyl_sum + moneyw
    elif length == 0:
        moneyw = 0
        if wtime > 0:
            moneyw = wtime * 3
        sum_money = 80*2 + moneyw
    return sum_money    
    
    # Проверка:
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0,5)
# 175
# >>> taxi_cost(42130, 8)
# 1790  ***** в задании 1789, пытался округлять разными 4мя способами... этот самый ближний получается ответ, не понятно в чём ошибка\
# >>> print(taxi_cost(-300))
# None
    