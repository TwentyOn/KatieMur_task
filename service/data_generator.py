import random
from datetime import date, timedelta

from faker import Faker
import pandas as pd

from models import Order


def generate_data() -> pd.DataFrame:
    result = [None] * 1000

    articles = [random.randrange(100000000, 1000000000) for _ in range(100)]

    fake = Faker('ru_RU')
    for i in range(1000):
        order = Order(
            order_date=(date.today() - timedelta(days=1)).strftime("%d-%m-%Y"),
            article=random.choice(articles),
            product_name=fake.text(),
            status=random.choice(['Оформлен', 'В пути', 'Доставлен']),
            price=random.uniform(500, 100000),
        )
        result[i] = order

    result = pd.DataFrame(result)
    return result
