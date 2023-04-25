from main import Products
from main import Freezer
from main import Fridge


def test_fridge_1():
    fridge = Fridge(4)
    fridge.add_product('Milk', 5, -20)
    fridge.add_product('Meat', -3, -25)
    fridge.add_product('Ice Cream', 5, -20)
    assert fridge.count_products() == 2


def test_fridge_2():
    fridge = Fridge(4)
    fridge.add_product('Apple', 15, 0)
    fridge.add_product('Meat', -3, -25)
    fridge.add_product('Ice Cream', -5, -20)
    assert fridge.count_products() == 1

