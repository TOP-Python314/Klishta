from pathlib import Path
from sys import path

def ask_for_file():
    file = input()
    file_path = Path(file)
    while file_path.is_file() is False:
        print('! по указанному пути отсутствует необходимый файл !')
        file = input()
        file_path = Path(file)
    if file_path.is_file():
        from utils import load_file
        thing = load_file(file_path)
        helper = str(thing) + '/' + file_path.name
        result = Path(helper)
        return result