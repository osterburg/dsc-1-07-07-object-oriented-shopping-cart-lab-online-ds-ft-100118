import numpy as np

class ShoppingCart:
    # write your code here
    def __init__(self, discount=None):
        self._total = 0
        self._items = []
        self._discount = discount

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
        return self._total

    @total.deleter
    def total(self):
        del self._total

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items
        return self._items

    @items.deleter
    def items(self):
        del self._items

    @property
    def employee_discount(self):
        return self._discount

    @employee_discount.setter
    def employee_discount(self, value):
        self._discount = value
        return self._discount

    def add_item(self, name, price, quantity=1):
        self._items.append({"name": name, "price": price})
        self._total = price * quantity
        return self._total

    def get_all_prices(self):
        return [x['price'] for x in self._items]

    def mean_item_price(self):
        return np.mean(self.get_all_prices())

    def median_item_price(self):
        return np.median(self.get_all_prices())

    def apply_discount(self):
        if self._discount:
            d = self._discount/100
            new_price = self._total * ( 1 - d)
            return new_price
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def item_names(self):
        return [x['name'] for x in self._items]

    def void_last_item(self):
        if self._items:
            del_item = self._items.pop()
            self._total -= del_item['price']
        else:
            return "There are no items in your cart!"
