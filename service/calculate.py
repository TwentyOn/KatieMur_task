import logging

import pandas as pd
import duckdb

logger = logging.getLogger(__name__)


def get_orders_rating(orders: pd.DataFrame) -> list[tuple[int, int]]:
    """
    Функция для подсчета рейтинга заказов
    :param orders:
    :return:
    """
    try:
        result = duckdb.sql("""
            SELECT article, COUNT(*) as count 
            FROM 'orders' 
            GROUP BY article 
            ORDER BY count DESC 
            LIMIT 3"""
            )
        return result.fetchall()
    except Exception as err:
        logger.error(exc_info=True, msg='Ошибка при подсчете рейтинга заказов')
        raise err
