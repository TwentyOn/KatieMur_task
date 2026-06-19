import pandas as pd



def csv_writer(orders: pd.DataFrame) -> None:
    try:
       orders.to_csv('orders.csv', index=False)
    except Exception as err:
        raise ValueError('Ошибка записи данных в файл: {}'.format(err))

