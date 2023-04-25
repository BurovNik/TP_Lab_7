from main import Products
from main import Freezer
from main import Fridge


def test_freezer_1():
    freezer = Freezer(-15)
    freezer.add_product('Milk', 5, -20)
    freezer.add_product('Meat', -3, -25)
    freezer.add_product('Ice Cream', 5, -20)
    assert freezer.count_products() == 3


def test_freezer_2():
    freezer = Freezer(-15)
    freezer.add_product('Apple', 15, 0)
    freezer.add_product('Meat', -3, -25)
    freezer.add_product('Ice Cream', 5, -20)
    assert freezer.count_products() == 2

