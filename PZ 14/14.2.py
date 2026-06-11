''' Дана строка, изображающая целое положительное число. Вывести сумму цифр этого
числа.'''
import tkinter as tk
from tkinter import ttk

def calculate_sum():
    try:
        number_str = entry_number.get().strip()
        
        if not number_str.isdigit():
            label_result.config(text="Ошибка: введите целое положительное число!", fg="red")
            return
        
        digit_sum = sum(int(digit) for digit in number_str)
        
        label_result.config(text=f"Сумма цифр числа {number_str} = {digit_sum}", fg="black")
        
    except Exception as e:
        label_result.config(text=f"Ошибка: {str(e)}", fg="red")

def clear_fields():
    entry_number.delete(0, tk.END)
    label_result.config(text="")

root = tk.Tk()
root.title("Сумма цифр числа - Обработка")
root.geometry("500x300")
root.resizable(False, False)

root.attributes('-topmost', True) 

title_label = tk.Label(root, text="Вычисление суммы цифр числа", 
                      font=("Arial", 14, "bold"))
title_label.pack(pady=10)

form_frame = tk.Frame(root, bd=2, relief="groove")
form_frame.pack(padx=20, pady=10, fill="both", expand=True)

label_number = tk.Label(form_frame, text="Введите целое положительное число:", 
                       anchor="w", font=("Arial", 10))
label_number.grid(row=0, column=0, sticky="w", padx=10, pady=10)

entry_number = tk.Entry(form_frame, width=40, font=("Arial", 10))
entry_number.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

tk.Label(form_frame).grid(row=1, column=0, columnspan=2, pady=5)

label_result = tk.Label(form_frame, text="", anchor="w", font=("Arial", 11, "bold"))
label_result.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=10)

tk.Label(form_frame).grid(row=3, column=0, columnspan=2, pady=10)

button_frame = tk.Frame(form_frame)
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

button_calculate = tk.Button(button_frame, text="Вычислить сумму", 
                            width=20, command=calculate_sum,
                            font=("Arial", 10))
button_calculate.pack(side="left", padx=10)

button_clear = tk.Button(button_frame, text="Очистить", 
                        width=15, command=clear_fields,
                        font=("Arial", 10))
button_clear.pack(side="left", padx=10)

form_frame.columnconfigure(1, weight=1)

root.update() 

root.mainloop()