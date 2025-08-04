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
