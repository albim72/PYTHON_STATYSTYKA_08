class Book:
    #konstruktor --> stan
    def __init__(self, title, author, pages):
        self.book_title = title
        self.author = author
        self.pages = pages
        self.cena = 0
        self.newbook()
        
    def newbook(self):
        print("Nowa książka: Book")

    def cena(self):
        print(f"Cena: {self.cena} zł")
        
    def setcena(self,nowacena):
        self.cena = nowacena
