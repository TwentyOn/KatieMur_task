import logging
from datetime import date, timedelta

from models import Order
from service.data_generator import generate_data

logger = logging.getLogger(__name__)


def get_orders(token: str) -> list[Order]:
    """
    Функция для получения заказов из API
    :param token: API-токен
    :return:
    """

    # ИМИТАЦИЯ ЗАПРОСА К API
    # настройка запроса
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # как пример
    params = {
        'date_from': date.today() - timedelta(days=1),
        'date_to': date.today()
    }

    # запрос к API.
    # todo заменить тестовую функцию

    try:
        orders = generate_data()
        return orders
    except Exception as err:
        logger.error(exc_info=True)
        raise Exception('Ошибка запроса к API: {}'.format(err))
