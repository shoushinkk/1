""" формування заявок на устаткування по магазину
"""
from data_service import get_clients, get_orders


# структура рядка вихідних даних
zajavka = {

    'namet'         : '',  # найменування
    'order_number'  : '',  # номер заказа
    'client_code'   : '',  # код клієнта
    'kol'           : 0,   # кількість 
    'price'         : 0.0, # ціна
    'total'         : 0.0, # сума
}


clients = get_clients()
orders = get_orders()


def create_zajavka():  
    """Формування аналізу руху основних засобів
    """
    
    def get_clients_name(clients_code):
        """повертає назву клієнта по його коду
        Args:
            clients_code ([type]): код клієнта
        Returns:
            [type]: назва клієнта
        """
        for clients in clients:
            if clients_code == clients[0]:
                return clients[1]
        return "назва не знайдена"
    
    # накопичувач заявок
    zajavka_list = []

    for orders in orders:   
        
        # створити робочу копію
        zajavka_work = zajavka.copy()
        
        zajavka_work['namet']           = orders[2]
        zajavka_work['order_number']    = orders[1]
        zajavka_work['client_code']     = orders[3]
        zajavka_work['kol']             = orders[4]
        zajavka_work['price']           = orders[3]
        zajavka_work['total']           = zajavka_work['kol'] *  zajavka_work['price']
        zajavka_work['client_name']     = get_clients_name(orders[0])
        
        zajavka_list.append(zajavka_work)
        
    return zajavka_list