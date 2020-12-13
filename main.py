"""головний модуль додатку
виводить розрахункову таблицю, зберігає результати в файл
показує на екрані первинні дані
"""
from os import system  
from process_data import create_zajavka
from data_service import show_clients, show_orders, get_orders, get_clients

MAIN_MENU = \
"""
~~~~~~~~~~~~~~~~ ОБРОБКА ЗАЯВОК НА УСТАТКУВАННЯ ~~~~~~~~~~~~~~~~
1 - вивід заявок на екран 
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід списка клієнтів
0 - завершення роботи
-----------------------------------------------
"""
STOP_MESSAGE = "Нажміть будь-яку клавішу для продовження"

TITLE = "ЗАЯВКА НА ПРОДАЖ УСТАТКУВАННЯ"
HEADER = \
"""
=================================================================
Найменування         |  Номер заказа | Код клієнта | Ціна | Сума    
=================================================================
"""
FOOTER = \
"""
=================================================================
"""


def show_create_zajavka(zajavka_list):
    """Вивід таблиці заявок на екран
    Args:
        zajavka_list ([type]): список заявок
    """
    print(f"\n{TITLE:^65}")
    print(HEADER)

    
    for zajavka in zajavka_list:
        print(f"{zajavka['namet']:22}",    
              f"{zajavka['order_number']:^17}", 
              f"{zajavka['client_code']:^14}",    
              f"{zajavka['kol']:>10}",       
              f"{zajavka['price']:>10.2f}",   
              f"{zajavka['total']:>10.2f}",   
              )

    print(FOOTER)       
def write_create_zajavka(zajavka_list):
    """записуємо масив заявок в файл
    Args:
    zajavka_list([type]): Список заявок
    """
    with open('./data/zajavki.txt', "w") as zajavka_file:
        for zajavka in zajavka_list:
            line = \
                zajavka['namet'] + ';' +  \
                str(zajavka['order_number']) + ';' + \
                str(zajavka['client_code']) + ';' + \
                str(zajavka['kol']) + ';' + \
                str(zajavka['price']) + ';' + \
                str(zajavka['total']) + '\n'

            zajavka_file.write(line)
    print("Файл сформовано ...")


while True:
   # Виводить головне меню 
   system('clear')
   print(MAIN_MENU) 
   command_number = input("Введіть номер команди: ")

   if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)

   elif command_number == '1':
       zajavka_list = create_zajavka()
       show_create_zajavka(zajavka_list)
       input(STOP_MESSAGE)

   elif command_number == '2':
        zajavka_list = create_zajavka()
        write_create_zajavka(zajavka_list)
        input(STOP_MESSAGE)

   elif command_number == '3':
       orders = get_orders()
       show_orders(orders)
       input(STOP_MESSAGE)

   elif command_number == '4':
       clients = get_clients()
       show_clients(clients)
       input(STOP_MESSAGE)       