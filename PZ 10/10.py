'''
Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
Исходные данные:
Количество элементов:
Максимальный элемент:
Среднее арифметическое элементов первой трети:
'''
import random

input_file = "data_input.txt"
output_file = "data_output.txt"

count_nums = random.randint(10, 20)
random_numbers = [random.randint(-50, 50) for _ in range(count_nums)]
data_str = " ".join(map(str, random_numbers))

f_in = open(input_file, 'w', encoding='utf-8')
f_in.write(data_str)
f_in.close()

f_in = open(input_file, 'r', encoding='utf-8')
content = f_in.read().strip()           
numbers = [int(x) for x in content.split()]  
f_in.close()

count = len(numbers)                    
max_val = max(numbers)                  
third_len = count // 3                  

if third_len > 0:
    mean_third = sum(numbers[:third_len]) / third_len
else:
    mean_third = 0.0

f_out = open(output_file, 'w', encoding='utf-8')
f_out.write(f'Исходные данные: {content}\n')
f_out.write(f'Количество элементов: {count}\n')
f_out.write(f'Максимальный элемент: {max_val}\n')
f_out.write(f'Среднее арифметическое элементов первой трети: {mean_third:.2f}\n')
f_out.close()

print(f'Файлы созданы: {input_file}, {output_file}')