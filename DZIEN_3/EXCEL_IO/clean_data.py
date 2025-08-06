import pandas as pd
import numpy as np
import missingno as msno

#wcztaj dane
df = pd.read_excel('missing_data.xlsx')

#podglad i naaanalia braków
print(df.head())
print(df.isnull().sum()) #liczba braków w kolumnach

#usunięcie wierszy z brakami
df_clean = df.dropna(subset=['ilość', 'cena jednostkowa'])

#uzupełninie braków średnią lub medianą
df['ilość'] = df['ilość'].fillna(df['ilość'].mean())
df['cena jednostkowa'] = df['cena jednostkowa'].fillna(df['cena jednostkowa'].median())


#uzupełnienie brakujących nazw
df['produkt'] = df['produkt'].fillna('brak')
df['region'] = df['region'].fillna('brak')
df['sprzedawca'] = df['sprzedawca'].fillna('nieznany')

#aalternatywa - oznaczenie w raporcie
df['braki'] = df.isnull().any(axis=1)

#przeliczenie wartości sprzedaży

df['wartość sprzedaży'] = df['ilość'] * df['cena jednostkowa']

#analixy
print(df.groupby('region')['wartość sprzedaży'].sum())

#zapis do excela

df.to_excel("dane_clean.xlsx", index=False)

print("_________________________________________________")
print(msno.matrix(df))
