from main import Book
from main import Library


def test_library_1():
    book_1 = Book(0.2, "Adler", 1200)
    book_2 = Book(0.4, "Max", 1230)
    Library_1 = Library(20)
    Library_1.add_book(0.4, "Max", 1230)
    Library_1.add_book(0.3, "Max", 1030)
    assert Library_1.find_book('Adler') == False


def test_library_2():
    book_1 = Book(0.2, "Adler", 1200)
    book_2 = Book(0.4, "Max", 1230)
    Library_1 = Library(20)
    Library_1.add_book(0.4, "Max", 1230)
    Library_1.add_book(0.3, "Max", 1030)
    assert Library_1.find_book('Adler') == False
