def strong_password(password: str) -> bool:
    """Проверяет пароль на *доступность*"""
    length = len(password)
    pas_words = password.strip('1234567890')
    pas_low = pas_words.islower()
    pas_upp = pas_words.isupper()
    pas_numbs = password.strip('ёйцукенгшщзхъэждлорпавыфячсмитьбюЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ')
    pas_clear = password.strip('1234567890ёйцукенгшщзхъэждлорпавыфячсмитьбюЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ')
    if length <= 8:
        return False
    if pas_low == True or pas_upp == True:
        return False
    if len(pas_numbs) < 2:
        return False
    if len(pas_clear) == 0:
        return False
    return True
    
# ПРОВЕРКА:
# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password2019')
# False