#! /usr/bin/env python3

class Flower:
    """A class for a Flower
    
    name            name of the flower
    petal_count     number of petals
    price           price of the flower
    """

    def __init__(self, name, petal_count, price):
        self._name = name
        self._petal_count = petal_count
        self._price = price

    def get_name(self):
        return self._name

    def get_petal_count(self):
        return self._petal_count

    def get_price(self):
        return self._price

    def set_name(self, new_name):
        self._name = new_name

    def set_petal_count(self, new_petal_count):
        self._petal_count = new_petal_count

    def set_price(self, new_price):
        self._price = new_price

    def __str__(self):
        return "<Flower name='" + self._name + "' petal_count='" + str(self._petal_count) + "' price='" + str(self._price) + "'>"

if __name__ == '__main__':
    f = Flower('Delphinium', 4, 20)
    print(f)

    f.set_price(5)
    f.set_petal_count(10)
    print(f)
