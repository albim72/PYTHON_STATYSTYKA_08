import random

populacja = ["Anna","Bartek","Celina","Marek","Damian","Jakub","Kasia","Michał","Ola","Piotr","Ryszard",
             "Tomasz","Witold","Zdzisiek"]

proba = random.sample(populacja, 5)
print(f"proba badawcza: {proba}")

print("_________________________________________________________________________________")

import numpy as np

punkty = [65,65,34,899,0,25,822,5,8,32,79,112,573,277]
srednia = np.mean(punkty)
odchylenie = np.std(punkty)
mediana = np.median(punkty)

print(f"srednia: {srednia}")
print(f"odchylenie: {odchylenie}")
print(f"mediana: {mediana}")

print("_________________________________________________________________________________")

#skala nominalna: kolory samochodów
kolory = ["red","green","blue","yellow","orange","purple","brown","pink","gray","cyan","magenta"]

#skala kategorialna: rodzaj samochodów
rodzaje = ["sedan","hatchback","suv","truck","convertible","van","pickup","wagon","minivan"]

#skala porządkowa
stopnie_wojskowe = ["szeregowy","kapral","porucznik","kapitan"]

#skala ilorazowa
wzrosty = [153,177,184,190,145,167,180,201,124]
print(f"skala nominalna: {kolory}")
print(f"skala kategorialna: {rodzaje}")
print(f"skala porządkowa: {stopnie_wojskowe}")
print(f"skala ilorazowa: {wzrosty}")



