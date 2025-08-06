import pandas as pd
import numpy as np
from faker import Faker
import datetime

fake = Faker("pl_PL")
np.random.seed(42)

produkty = ['Laptop', 'Smartfon', 'Monitor', 'Drukarka', 'Router', 'Tablet','Myszka','Mikrofon']
regiony = ['Mazowieckie', 'Śląskie', 'Małopolskie', 'Pomorskie', 'Dolnośląskie', 'Wielkopolskie','Lubelskie']

def random_or_none(val, prob_nan=0.1):
    """Zwraca None z prawdopodobieństwem prob_nan, inaczej val."""
    return val if np.random.rand() > prob_nan else None

rekordy = []
for _ in range(1000):
    rekord = {
        "data": random_or_none(
            fake.date_between(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
        ),
        "produkt": random_or_none(np.random.choice(produkty)),
        "region": random_or_none(np.random.choice(regiony)),
        "sprzedawca": random_or_none(fake.name()),
        "ilość": random_or_none(np.random.randint(1, 30)),
        "cena jednostkowa": random_or_none(np.round(np.random.uniform(99, 6000), 2))
    }
    rekordy.append(rekord)

df = pd.DataFrame(rekordy)
df.to_excel("missing_data.xlsx", sheet_name="dane", index=False)
