import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
godziny_nauki = np.random.randint(1, 15, 25)
print(godziny_nauki)

wynik_egzaminu = godziny_nauki*5+np.random.randint(1, 7, 25) + 50
print(wynik_egzaminu)

df = pd.DataFrame({'Godziny nauki':godziny_nauki, 'Wynik':wynik_egzaminu})
print(df.head(5))

#wizualizacja danych
plt.scatter(df['Godziny nauki'],df['Wynik'],color='royalblue')
plt.xlabel('Godziny nauki')
plt.ylabel('Wynik egzaminu')
plt.title('Zależność: czas nauki - wynik egzaminu')
plt.grid(True)
plt.show()

#obliczenie współczynnika korelacji
korelacja = df['Godziny nauki'].corr(df['Wynik'])
print(f"współczynnik korelacji: {korelacja}")
