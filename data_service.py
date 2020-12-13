""" модуль для доступу до вхідних даних
"""

def get_orders():
    """отримує данні по замовленням
    Returns:
        orders_list : список замовлень
    """

    from_file = [
 "КНТЕУ;202;10;10",
 "КНЕУ;203;20;10",
 "КНУ;205;30;5",
 "КНТЕУ;207;40;10",
 "КНЕУ;211;20;5",
 "КНУ;204;10;5",
 "КНТЕУ;206;30;5",
 "КНЕУ;210;50;3",
 "КНУ;212;60;4",
 "КНТЕУ;213;70;5",
    ]

    # накопичувач рядків
    orders_list = []

    for line in from_file:
        line_list = line.split(';')
        orders_list.append(line_list)

    return orders_list

def show_orders(orders):
    """виводить список замовлень за заданої умови
    Args:
        order :  список замовлень
    """
    orders_code_from = input("з якого кода замовлення?")
    orders_code_to = input("по який код замовлення?")
    for orders in orders:
        if orders_code_from <= orders[2] <= orders_code_to:
             print("Клієнт = {:7} Номер заказу = {:5} Kод : {:5} Kількість = {:10} " .format(orders[0], orders[1], orders[2], orders[3]))


orders = get_orders()
show_orders(orders)

""" модуль для доступу до вхідних даних
"""

def get_clients():
    """отримує данні по замовленням
    Returns:
        clients_list : список замовлень
    """

    from_file = [
  "10;План розрахунків підприємств;40",
  "20;ППП УЗПИКС;900",
  "30;ППП УТЕП;900",
  "40;ППП УОС;600",
  "50;ППП УФРО;1245",
  "60;АРМ бухгалтера матеріально-технічного відділу;500",
  "70;АРМ бухгалтера фінансового відділу;500",
  "80;ППП Облік договорів;150",
    ]

    # накопичувач рядків
    clients_list = []

    for line in from_file:
        line_list = line.split(';')
        clients_list.append(line_list)

    return clients_list

def show_clients(clients):
    """виводить список замовлень за заданої умови
    Args:
        clients :  список замовлень
    """
    clients_code_from = input("з якого кода замовлення?")
    clients_code_to = input("по який код замовлення?")
    for clients in clients:
        if clients_code_from <= clients[0] <= clients_code_to:
             print(" Код: {:5} Найменування товару = {:48} Ціна = {:10}  ".format(clients[0], clients[1], clients[2]))

clients = get_clients()
show_clients(clients)