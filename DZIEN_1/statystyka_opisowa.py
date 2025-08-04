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

kolory = ["red","green","blue","yellow","orange","purple","brown","pink","gray","cyan","magenta"]
