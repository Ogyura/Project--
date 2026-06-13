'''
Приложение ТЕЛЕМАСТЕРСКАЯ для автоматизированного контроля работ по
ремонту бытовой техники. БД должна содержать таблицу Ремонт телевизоров, имеющую
следующую структуру записи: Марка телевизора, Завод-изготовитель, Цена, Дата
ремонта, Документ, Мастер, Сумма оплаты. 

'''
import sqlite3 as sq
import os
from data import DATA

DB = "telemaster.db"

def init_db():
    if os.path.exists(DB):
        os.remove(DB)
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Ремонт_телевизоров (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Марка_телевизора TEXT NOT NULL,
                Завод_изготовитель TEXT,
                Цена REAL CHECK(Цена >= 0),
                Дата_ремонта TEXT,
                Документ TEXT,
                Мастер TEXT,
                Сумма_оплаты REAL CHECK(Сумма_оплаты >= 0)
            )""")

            cur.executemany(
                """INSERT INTO Ремонт_телевизоров 
                   (Марка_телевизора, Завод_изготовитель, Цена, Дата_ремонта, Документ, Мастер, Сумма_оплаты) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)""", DATA)
            print("База данных 'ТЕЛЕМАСТЕРСКАЯ' успешно создана и заполнена.\n")
    except sq.Error as e:
        print(f"Ошибка инициализации БД: {e}")

def show_all():
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Ремонт_телевизоров")
            rows = cur.fetchall()
            if not rows:
                print("Записей нет.")
            else:
                print(f"{'ID':<3} | {'Марка':<15} | {'Завод':<20} | {'Цена':<8} | {'Дата':<10} | {'Документ':<8} | {'Мастер':<12} | {'Оплата':<8}")
                print("-" * 95)
                for row in rows:
                    print(f"{row[0]:<3} | {row[1]:<15} | {row[2]:<20} | {row[3]:<8} | {row[4]:<10} | {row[5]:<8} | {row[6]:<12} | {row[7]:<8}")
    except sq.Error as e:
        print(f"Ошибка чтения: {e}")

def search_by_brand():
    brand = input("Поиск по марке телевизора: ")
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Ремонт_телевизоров WHERE Марка_телевизора LIKE ?", (f"%{brand}%",))
            rows = cur.fetchall()
            if not rows:
                print("Ничего не найдено.")
            else:
                for row in rows:
                    print(row)
    except sq.Error as e:
        print(f"Ошибка поиска: {e}")

def search_by_master():
    master = input("Поиск по мастеру: ")
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Ремонт_телевизоров WHERE Мастер LIKE ?", (f"%{master}%",))
            rows = cur.fetchall()
            if not rows:
                print("Ничего не найдено.")
            else:
                for row in rows:
                    print(row)
    except sq.Error as e:
        print(f"Ошибка поиска: {e}")

def search_by_date():
    date = input("Поиск по дате ремонта (ГГГГ-ММ-ДД): ")
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Ремонт_телевизоров WHERE Дата_ремонта = ?", (date,))
            rows = cur.fetchall()
            if not rows:
                print("Ничего не найдено.")
            else:
                for row in rows:
                    print(row)
    except sq.Error as e:
        print(f"Ошибка поиска: {e}")

def edit_payment():
    try:
        pid = int(input("ID заказа для изменения оплаты: "))
        new_payment = float(input("Новая сумма оплаты: "))
        if new_payment < 0:
            print("Сумма оплаты не может быть отрицательной!")
            return
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Ремонт_телевизоров SET Сумма_оплаты = ? WHERE id = ?", (new_payment, pid))
            print("Сумма оплаты обновлена." if cur.rowcount else "Заказ с таким ID не найден.")
    except ValueError:
        print("Ошибка ввода данных. Введите число.")
    except sq.Error as e:
        print(f"Ошибка обновления: {e}")

def edit_master():
    try:
        pid = int(input("ID заказа для изменения мастера: "))
        new_master = input("Новый мастер: ")
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Ремонт_телевизоров SET Мастер = ? WHERE id = ?", (new_master, pid))
            print("Мастер обновлен." if cur.rowcount else "Заказ с таким ID не найден.")
    except ValueError:
        print("Ошибка ввода данных. ID должен быть числом.")
    except sq.Error as e:
        print(f"Ошибка обновления: {e}")

def delete_by_id():
    try:
        pid = int(input("ID заказа для удаления: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Ремонт_телевизоров WHERE id = ?", (pid,))
            print(f"Удалено записей: {cur.rowcount}")
    except ValueError:
        print("Ошибка ввода данных. ID должен быть числом.")
    except sq.Error as e:
        print(f"Ошибка удаления: {e}")

def delete_by_master():
    master = input("Удалить все заказы мастера: ")
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Ремонт_телевизоров WHERE Мастер = ?", (master,))
            print(f"Удалено записей: {cur.rowcount}")
    except sq.Error as e:
        print(f"Ошибка удаления: {e}")

init_db()

while True:
    print("\n=== МЕНЮ 'ТЕЛЕМАСТЕРСКАЯ' ===")
    print("1 - Показать все заказы на ремонт")
    print("2 - Поиск по марке телевизора")
    print("3 - Поиск по мастеру")
    print("4 - Поиск по дате ремонта")
    print("5 - Изменить сумму оплаты")
    print("6 - Изменить мастера")
    print("7 - Удалить заказ по ID")
    print("8 - Удалить все заказы конкретного мастера")
    print("0 - Выход")

    cmd = input("Выберите действие: ")
    if cmd == '1':
        show_all()
    elif cmd == '2':
        search_by_brand()
    elif cmd == '3':
        search_by_master()
    elif cmd == '4':
        search_by_date()
    elif cmd == '5':
        edit_payment()
    elif cmd == '6':
        edit_master()
    elif cmd == '7':
        delete_by_id()
    elif cmd == '8':
        delete_by_master()
    elif cmd == '0':
        print("Выход из программы.")
        break
    else:
        print("Неверная команда. Попробуйте снова.")