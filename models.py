from dataclasses import dataclass, fields, asdict


@dataclass
class Order:
    order_date: str
    article: int
    product_name: str
    status: str
    price: float

    def get_fields(self):
        return [field.name for field in fields(self)]

    def to_dict(self) -> dict:
        return asdict(self)
