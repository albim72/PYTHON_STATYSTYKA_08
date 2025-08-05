import itertools

proby = list(itertools.product(['O','R'], repeat=3))
#przestrzeń zdarzeń
print(f"przestrzenie zdarzeń:{proby}")

#liczba przypadków z orłami
dokladnie_2_orly = [x for x in proby if x.count('O') == 2]
prawd = len(dokladnie_2_orly)/len(proby)

print(f"prawdopodobieństwo zdarzenia 2 orly: {prawd}")
