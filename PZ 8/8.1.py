'''
Найдите ключ с минимальным значением в sample_dict = {'Physics': 82, 'Math': 65,
'history': 75}.

'''
sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}

min_key = min(sample_dict, key=sample_dict.get)

print("Словарь:", sample_dict)
print("Ключ с минимальным значением:", min_key)
print("Минимальное значение:", sample_dict[min_key])