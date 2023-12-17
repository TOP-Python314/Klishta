names = input().split('; ')
names_dict = {}
sorted_names = []
for name in names:
    if name in names_dict:
        hof = names_dict[name] + 1
        num = name.find('.')
        test = name[0:num] + '_' + str(hof )+ name[num:]
        sorted_names.append(test)
    else:
        sorted_names.append(name)
    names_dict[name] = names_dict.get(name, 0) + 1
    sorted_names.sort()
for items in sorted_names:
    print(items)

# ВВОД:
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# ВЫВОД:
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz