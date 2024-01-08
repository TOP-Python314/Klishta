from pathlib import Path

def  list_files(pname: str) -> None | tuple:
    """Проверяет каталог по переданному абсолютному пути на наличие файлов"""
    path_abs = Path( pname)
    thing = list(path_abs.iterdir())
    result = []
    if len(thing) > 0:
        for item in thing:
            result .append(str(item.name) )
        result = tuple(result)
        return result
    else:
        result = None
        return result
# ПРОВЕРКА:
# >>> list_files(r'C:\Users\Danil\Road2It\python 314\python\0.hw\repOfClasses\_scripts')
# ('.git', '.gitignore', 'base', 'git1.txt', 'git2.txt', 'git3.txt')

# >>> list_files(r'C:\Users\Danil\Road2It\python 314\python\0.hw\repOfClasses\Klishta\2023.12.28\data')
# ('7MD9i.chm', 'c14KE', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'mXbd9', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')