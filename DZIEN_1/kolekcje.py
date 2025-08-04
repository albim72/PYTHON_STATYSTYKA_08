#Lista książek
#CTRL + D -> powielenie linii/bloku kodu
#CTRL + / -> komentowanie linii/bloku kodu

books = [
    "Python: Przygłoszenie do programowania",
    "Python: Przygłoszenie do programowania - wersja 2.0",
    "Python: Przygłoszenie do programowania - wersja 3.0",
    "Python: Przygłoszenie do programowania - wersja 3.1",
    "Python: Przygłoszenie do programowania - wersja 3.2",
    "AI - programowanie modeli",
    "AI - programowanie modeli - wersja 2.0",
]

print(books)
print(books[0])
print(books[3])
print(books[2:4])
print(books[:5])
print(books[4:])
print(books[-1])

books[3] = "Programowanie w Java"
print(books)
books.append("Python: Docker")
print(books)
books.insert(1, "Python: Gen")
print(books)
books.remove("Python: Docker")
print(books)
# books.sort()
# print(books)

print(sorted(books))
print(books)

s = "lajkonik"
print(s[::-1])

# krotka  tuple

liczby = (33,5,678,35,-64,3,8,35,96,-54)
print(liczby)
print(liczby.index(35))
print(liczby.count(35))

dl = (4,5,7)
liczby = liczby + dl
print(liczby)

#zbiór
drzewa = {"dąb","topola","jodła","jabłoń","lipa","dąb"}
print(drzewa)
print(drzewa)
print(drzewa)

nb = (3,5,2,6,6,2,3,4,6,2,5,6,7,2,2,3,4,6)
nb = tuple(set(nb))
print(nb)

# słownik
car = {
    "marka":"Jeep",
    "model":"Compass",
    "silnik":1.4,
    "moc":140,
    "nadwozie":"SUV",
    "przebieg":87644
}
print(car)
print(car["marka"])
print(car["nadwozie"])

car["przebieg"] = 62344

print(car)

car["rocznik"] = 2019
print(car)

for i,k in car.items():
    print(f"{i}: {k}")
