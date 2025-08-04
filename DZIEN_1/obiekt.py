class Book:
    #konstruktor --> stan
    def __init__(self, title, author, pages):
        self.book_title = title
        self.author = author
        self.pages = pages
        self._cena = 0
        self.newbook()

    def __repr__(self):
        return f"{self.book_title} - {self.author}"

    def newbook(self):
        print("Nowa książka: Book")

    def cena(self):
        print(f"Cena: {self._cena} zł")

    def setcena(self,nowacena):
        self._cena = nowacena

book1 = Book("Python", "Michal", 100)
book1.cena()
book1.setcena(101.50)
book1.cena()

print(book1)
