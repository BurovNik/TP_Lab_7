
class Book:
    def __init__(self, w = 0.4, author = 'Smith', cost = 1000 ):
        self.weight = w
        self.author = author
        self.cost = cost

    def show_detail(self):
        print(self.weight)
        print(self.author)
        print(self.cost)


class Library:
    def __init__(self, max_w = 100, ):
        self.max_weight = max_w
        self.curr_weight = 0
        self.BookList = []

    def addbook(self, w = 0.4, author = 'Smith', cost = 1000):
        (self.BookList).append(Book(w, author, cost))
        self.curr_weight += w

    def findbook(self, author: str) -> None:
        for it in self.BookList:
            if author == it.author:
                it.show_detail()

    def show_detail(self):
        print('max weight=', self.max_weight)
        print('Current weight =', self.curr_weight)
        print('Now in library', len(self.BookList), 'books')


book_1 = Book(0.2, "Adler", 1200)
book_2 = Book(0.4, "Max", 1230)

book_2.show_detail()
Library_1 = Library(20)
Library_1.addbook(0.4, "Max", 1230)
Library_1.addbook(0.3, "Max", 1030)
Library_1.addbook(0.4, "Smith", 1230)
Library_1.BookList[0].show_detail()
print('---------------')
Library_1.findbook('Max')
print('---------------')
Library_1.show_detail()
