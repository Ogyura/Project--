'''
https://lh5.googleusercontent.com/-wG_YHAIbVZU/Ud696wJg0FI/AAAAAAAACP4/eaIzPTZRixE/w596-h642-no/4_3.png
'''
import tkinter as tk
from tkinter import ttk

def create_registration_form():
    root = tk.Tk()
    root.title("Обработка формы - Mozilla Firefox")
    root.geometry("600x750")
    
    title_label = tk.Label(root, text="Форма регистрации пользователя", 
                          font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    
    form_frame = tk.Frame(root, bd=2, relief="groove")
    form_frame.pack(padx=20, pady=10, fill="both", expand=True)
    
    name_label = tk.Label(form_frame, text="Ваше имя:", anchor="w")
    name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    name_entry = tk.Entry(form_frame, width=40)
    name_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    
    password_label = tk.Label(form_frame, text="Пароль:", anchor="w")
    password_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    password_entry = tk.Entry(form_frame, width=40, show="*")
    password_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

    age_label = tk.Label(form_frame, text="Возраст:", anchor="w")
    age_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    age_entry = tk.Entry(form_frame, width=40)
    age_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
    

    gender_label = tk.Label(form_frame, text="Пол:", anchor="w")
    gender_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    
    gender_frame = tk.Frame(form_frame)
    gender_frame.grid(row=3, column=1, sticky="w", padx=10, pady=5)
    
    gender_var = tk.StringVar()
    male_radio = tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var, value="male")
    male_radio.pack(side="left", padx=5)
    female_radio = tk.Radiobutton(gender_frame, text="Женский", variable=gender_var, value="female")
    female_radio.pack(side="left", padx=20)
    
    hobbies_label = tk.Label(form_frame, text="Ваши увлечения:", anchor="w")
    hobbies_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
    
    hobbies_frame = tk.Frame(form_frame)
    hobbies_frame.grid(row=4, column=1, sticky="w", padx=10, pady=5)
    
    music_var = tk.BooleanVar()
    video_var = tk.BooleanVar()
    drawing_var = tk.BooleanVar()
    
    music_check = tk.Checkbutton(hobbies_frame, text="Музыка", variable=music_var)
    music_check.pack(side="left", padx=5)
    video_check = tk.Checkbutton(hobbies_frame, text="Видео", variable=video_var)
    video_check.pack(side="left", padx=10)
    drawing_check = tk.Checkbutton(hobbies_frame, text="Рисование", variable=drawing_var)
    drawing_check.pack(side="left", padx=10)
    
    country_label = tk.Label(form_frame, text="Ваша страна:", anchor="w")
    country_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
    country_combo = ttk.Combobox(form_frame, width=37, values=["Россия", "Украина", "Беларусь", "Казахстан"])
    country_combo.grid(row=5, column=1, sticky="ew", padx=10, pady=5)
    
    city_label = tk.Label(form_frame, text="Ваш город:", anchor="w")
    city_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)
    city_combo = ttk.Combobox(form_frame, width=37, values=["Москва", "Санкт-Петербург", "Киев", "Минск"])
    city_combo.grid(row=6, column=1, sticky="ew", padx=10, pady=5)
    
    about_label = tk.Label(form_frame, text="Кратко о себе:", anchor="w")
    about_label.grid(row=7, column=0, sticky="nw", padx=10, pady=5)
    about_text = tk.Text(form_frame, width=40, height=3)
    about_text.grid(row=7, column=1, sticky="ew", padx=10, pady=5)
    about_text.insert("1.0", "краткая информация о ваших увлечениях")
    about_text.config(fg="gray")

    math_label = tk.Label(form_frame, text="Решите пример, запишите результат в поле ниже:", anchor="w")
    math_label.grid(row=8, column=0, columnspan=2, sticky="w", padx=10, pady=10)
    
    math_frame = tk.Frame(form_frame)
    math_frame.grid(row=9, column=0, columnspan=2, sticky="w", padx=10, pady=5)
    
    example_label = tk.Label(math_frame, text="2 + 2 = ", font=("Arial", 12))
    example_label.pack(side="left")
    math_entry = tk.Entry(math_frame, width=10)
    math_entry.pack(side="left")
    
    button_frame = tk.Frame(form_frame)
    button_frame.grid(row=10, column=0, columnspan=2, pady=10)
    
    cancel_button = tk.Button(button_frame, text="Отменить ввод", width=15)
    cancel_button.pack(side="left", padx=5)
    
    confirm_button = tk.Button(button_frame, text="Данные подтверждаю", width=20)
    confirm_button.pack(side="left", padx=5)
    
    form_frame.columnconfigure(1, weight=1)
    
    root.mainloop()

if __name__ == "__main__":
    create_registration_form()