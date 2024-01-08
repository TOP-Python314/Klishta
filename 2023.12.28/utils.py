from pathlib import Path
from sys import path
from shutil import copy2

def load_file(file_path):
    """копирует указанный файл в каталог нахождения"""
    copy2(file_path, Path(path[0]))
    return Path(path[0])



def finding_words(*, text_dict: dict, keyword: str, numb: int):
    wordslow = keyword.lower()
    result = []
    for filename in text_dict:
        for i, item in enumerate(text_dict[filename]):
            stringlow = str(item).lower()
            if wordslow in stringlow:
                if numb + 1 < i < len(text_dict[filename]) - (numb + 1):
                    text = []
                    for j in range(numb*2 + 1):
                        text.append(text_dict[filename][i - numb])
                    intergs = {'keyword': keyword,'filename': filename, 'line': i + 1,'context': numb,'text': text }
                    result.append(intergs)
                else:
                    intergs = {'keyword': keyword,'filename': filename, 'line': i + 1,'context': numb,'text': item }
                    result.append(intergs)
            else:
                continue
            
    return result
# print(finding_words(text_dict = {'file-name': ['Солнце море Жара юга', '213123', 'rftadsga', 'жара, моря, пздя']}, keyword='жара',numb=0 ))