
class Book:
    def __init__(self, w: float = 0.4, author: str = 'Smith', cost: float = 1000) -> None:
        self.weight = w
        self.author = author
        self.cost = cost

    def show_detail(self) -> None:
        print(self.weight)
        print(self.author)
        print(self.cost)


class Library:
    def __init__(self, max_w: float = 100) -> None:
        self.max_weight = max_w
        self.curr_weight = 0
        self.BookList = []

    def add_book(self, w: float = 0.4, author: str = 'Smith', cost: float = 1000) -> None:
        if self.curr_weight + w > self.max_weight:
            print('Book can`t be added')
            return
        self.BookList.append(Book(w, author, cost))
        self.curr_weight += w

    def find_book(self, author: str) -> None:
        for it in self.BookList:
            if author == it.author:
                it.show_detail()

    def show_detail(self) -> None:
        print('max weight =', self.max_weight)
        print('Current weight =', self.curr_weight)
        print('Now in library', len(self.BookList), 'books')


book_1 = Book(0.2, "Adler", 1200)
book_2 = Book(0.4, "Max", 1230)

book_2.show_detail()
Library_1 = Library(20)
Library_1.add_book(0.4, "Max", 1230)
Library_1.add_book(0.3, "Max", 1030)
Library_1.add_book(0.4, "Smith", 1230)
Library_1.BookList[0].show_detail()
print('---------------')
Library_1.find_book('Max')
print('---------------')
Library_1.show_detail()


class Products:
    def __init__(self, name: str = 'Milk', temp_max: float = 0, temp_min: float =0) -> None:
        self.name = name
        self.temp_max = temp_max
        self.temp_min = temp_min
    def show_detail(self) -> None:
        print(self.name, self.temp_max, self.temp_min)


class Fridge:

    def __init__(self, temp: float = 4) -> None:
        self.product_list = []
        self.temp = temp

    def add_product(self, name: str, temp_max: float, temp_min : float) -> None:
        if (self.temp > temp_max) or (self.temp < temp_min):
            print('Product can`t be added to Fridge')
            return
        product = Products(name, temp_max, temp_min)
        self.product_list.append(product)


    def find_product(self, name: str) -> bool:
        for i in self.product_list:
            if i.name == name:
                print(name, ' is in Fridge')
            return True
        print('There is no ', name, 'in Fridge')
        return False

    def count_products(self) -> int:
        return len(self.product_list)

    def show_detail(self) -> None:
        for i in self.product_list:
            print(i.name, end=", ")
        print()


class Freezer:
    def __init__(self, temp: float = -18) -> None:
        self.temp = temp
        self.product_list = []

    def add_product(self, name: str, temp_max: float, temp_min : float) -> None:
        if (self.temp > temp_max) or (self.temp < temp_min):
            print('Product can`t be added to Fridge')
            return
        product = Products(name, temp_max, temp_min)
        self.product_list.append(product)

    def find_product(self, name: str) -> bool:
        for i in self.product_list:
            if i.name == name:
                print(name, ' is in Freezer')
            return True
        print('There is no ', name, 'in Freezer')
        return False

    def count_products(self) -> int:
        return len(self.product_list)

    def show_detail(self) -> None:
        for i in self.product_list:
            print(i.name, end=", ")
        print()


fridge = Fridge(3)
freezer = Freezer(-10)
fridge.add_product("Tomato", 4, -5)
freezer.add_product("Ice Cream", -1, -15)
fridge.show_detail()
freezer.show_detail()
fridge.add_product("Butter", 6, -10)
fridge.add_product("Milk", 6, 0)
fridge.add_product("Smth", 5, 0)
fridge.show_detail()
freezer.add_product("Ice", 0, -20)
freezer.add_product("Bread", 9, -9)
freezer.show_detail()
fridge.find_product("Tomato")
freezer.find_product("Bread")
print("number of products in fridge - ", fridge.count_products())
print("number of products in freezer - ", freezer.count_products())
