'''В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.''' 

import re

pattern_dot = re.compile(r"[0-3][0-9]\.[01][0-9]\.[0-9]{4}")
pattern_slash = re.compile(r"[0-3][0-9]/[01][0-9]/[0-9]{4}")

count_dot = 0
count_slash = 0
february_dates = []

try:
    with open("dates.txt", "r", encoding="utf-8") as file:
        text = file.read()
        
        for match in pattern_dot.finditer(text):
            count_dot += 1
            if ".02." in match.group(0):
                february_dates.append(re.sub(r"\.", "/", match.group(0)))
                
        for match in pattern_slash.finditer(text):
            count_slash += 1
            if "/02/" in match.group(0):
                february_dates.append(match.group(0))

    with open("february_dates.txt", "w", encoding="utf-8") as out_file:
        for date in february_dates:
            out_file.write(date + "\n")
        out_file.write(f"Всего дат февраля: {len(february_dates)}\n")

    print(f"ДД.ММ.ГГГГ: {count_dot} | ДД/ММ/ГГГГ: {count_slash}")
    print(f"В файл записано дат февраля: {len(february_dates)}")

except FileNotFoundError:
    print("Файл 'dates.txt' не найден.")