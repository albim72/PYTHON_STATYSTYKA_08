#reguła Bayesa
P_chora = 0.02
P_zdrowa = 0.98

P_plus_chora = 0.99
P_plus_zdrowa = 0.05

P_chora_jesli_test_plus = (P_plus_chora * P_chora) / (P_plus_chora * P_chora + P_plus_zdrowa * P_zdrowa)
print(f"prawdopodobieństwo że osoba z pozytywnym testem jest chora: {P_chora_jesli_test_plus}")
