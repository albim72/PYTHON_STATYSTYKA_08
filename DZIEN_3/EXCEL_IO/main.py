import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#wczytanie danych z excela
df = pd.read_excel('dane_sprzedaz.xlsx')

#wyliczenie dodatkowej kolumny - wartość sprzedaży
df['wartość sprzedaży'] = df['ilość'] * df['cena jednostkowa']

#podstawowe statystyki
suma_sprzedazy = df['wartość sprzedaży'].sum()
srednia_cena = df['cena jednostkowa'].mean()
max_sprzedaz = df['wartość sprzedaży'].max()
min_sprzedaz = df['wartość sprzedaży'].min()


#korelacja między ilością a ceną
korelacja = df['ilość'].corr(df['cena jednostkowa'])

#sprzedaż wg regionów
sprzedaz_region = df.groupby('region')['wartość sprzedaży'].sum().reset_index()

#wykres sprzdazy wg regionów
plt.figure(figsize=(8, 6))
plt.bar(sprzedaz_region['region'], sprzedaz_region['wartość sprzedaży'])
plt.title('Sprzedaż wg regionów')
plt.xlabel('Region')
plt.ylabel('Wartość sprzedaży')
plt.tight_layout()
plt.savefig('wykres_sprzedaz_region.png')
plt.show()

#zapis statystyk do excela
with pd.ExcelWriter('statystyki.xlsx') as writer:
    df.to_excel(writer, sheet_name='stats', index=False)
    stat_df = pd.DataFrame({
        'Statystyka': ['Suma sprzedazy', 'Średnia cena', 'Max sprzedazy', 'Min sprzedazy', 'Korelacja'],
        'Wartość': [suma_sprzedazy, srednia_cena, max_sprzedaz, min_sprzedaz, korelacja]
    })
    stat_df.to_excel(writer, sheet_name='statystyki', index=False)
    sprzedaz_region.to_excel(writer, sheet_name='regiony', index=False)

print("Statystyki zapisane do excela")

