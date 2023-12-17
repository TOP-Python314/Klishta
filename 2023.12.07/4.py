thing = input()
dict_values = []
trouble_dict = {}
while thing != "":
    dict_values.append(thing.split())
    thing = input()
# print(dict_values)
for items in dict_values:
    trouble_dict[items[0]] = items[1]
flag = False
needed = input()
for key in trouble_dict:
    if  trouble_dict[key] == needed:
        flag = True
        our_value = key
        break
if flag:
    print(our_value)
else:
    print('! value error !')

    
# ВВОД:
# 1004 one
# 1005 two
# 1006 three
# 1007 four

# two
# ВЫВОД:
# 1005

# ВВОД:
# 1004 one
# 1005 two
# 1006 three
# 1007 four

# six
# ВЫВОД:
# ! value error !