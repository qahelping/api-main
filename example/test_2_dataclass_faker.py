import json
from dataclasses import dataclass, field, asdict

from faker import Faker

Faker.seed()

fake = Faker('ru_RU')


@dataclass
class Order:
    transport_name: str = 'автомобиль'
    color: str = field(default_factory=lambda: fake.color_name().lower())
    licence_plate: str = field(default_factory=fake.license_plate)
    paid: bool = field(default_factory=fake.pybool)


@dataclass
class Customer:
    name: str = field(default_factory=fake.name)
    address: str = field(default_factory=fake.address)
    card_number: int = field(default_factory=lambda: int(fake.credit_card_number(card_type='visa')))
    zip: int = None
    order: Order = field(default_factory=Order)

    def __post_init__(self):
        self.zip = int(self.address.split(',')[-1])


def test_faker():
    print(json.dumps(asdict(Customer()), ensure_ascii=False, indent=4))