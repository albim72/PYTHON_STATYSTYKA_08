import pandas as pd
import numpy as np
from faker import Faker
import datetime

fake = Faker("pl_PL")
np.random.seed(42)

produkty = ['Laptop', 'Smartfon', 'Monitor', 'Drukarka', 'Router', 'Tablet','Myszka','Mikrofon']
regiony = ['Mazowieckie', 'Śląskie', 'Małopolskie', 'Pomorskie', 'Dolnośląskie', 'Wielkopolskie','Lubelskie']

data = {
    "data": [
        fake.date_between(
            start_date=datetime.date(2024, 1, 1),
            end_date=datetime.date(2024, 12, 31)
        ) for _ in range(1000)
    ],
    "produkt": [np.random.choice(produkty) for _ in range(1000)],
    "region": [np.random.choice(regiony) for _ in range(1000)],
    "sprzedawca": [fake.name() for _ in range(1000)],
    "ilość": np.random.randint(1, 30, 1000),
    "cena jednostkowa": np.round(np.random.uniform(99, 6000, 1000), 2)
}

df = pd.DataFrame(data)
df.to_excel("dane_sprzedaz.xlsx", sheet_name="dane", index=False)
