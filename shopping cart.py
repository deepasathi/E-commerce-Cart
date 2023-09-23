class cart:
    def __init__(self):
        self.items = {}
        self.price = {'book': 40, 'pen': 10, 'laptop': 55000}
    def adding_items(self, name_of_the_item, quantity):
        self.items[name_of_the_item] = quantity
    def removing_items(self, name_of_the_item):
        self.items[name_of_the_items]
    def updating_quantity(self, name_of_the_item, quantity):
        self.items[name_of_the_item] = quantity
    def get_items(self):
        list_of_items = []
        list_of_items = list(self.items.keys())
        print(list_of_items)
    def get_total_price(self):
        total_price = 0
        for name_of_the_item, quantity in self.items.items():
            total_price+= self.price[name_of_the_item] * quantity
        return total_price
cart_obj = cart()
cart_obj.adding_items("book",10)
cart_obj.get_items()
cart_obj.adding_items("laptop",2)
cart_obj.get_items()
cart_obj.adding_items("pen",5)
cart_obj.get_items()
print(cart_obj.get_total_price())