def orth_triangle(*, hypotenuse: float = 0, cathetus1: float = 0, cathetus2: float = 0):
""" по ключевым параметрам получает 2 стороны  треугольника и вычисляет третью, если это возможно"""
    if hypotenuse != 0 and cathetus1 != 0 and cathetus2 != 0:
        return None
    if hypotenuse == 0:
        result = round((cathetus1**2 + cathetus2**2)**0.5, 2)
        return result
    cathet = cathetus1 + cathetus2
    if hypotenuse > cathet:
        result = round((hypotenuse**2 - cathet**2)**0.5, 2)
    elif hypotenuse <= cathet:
        result = None
    return result
    
    
# ПРОВЕРКА:
# >>> orth_triangle(hypotenuse = 6, cathetus2 = 4)
# 4.47