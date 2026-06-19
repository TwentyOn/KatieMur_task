import csv

from models import Order


def write_orders(orders: list[Order]) -> None:
    try:
        fields = orders[0].get_fields()
        with open('orders.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for order in orders:
                writer.writerow(order.to_dict())
    except Exception as err:
        raise ValueError('Ошибка записи данных в файл: {}'.format(err))
