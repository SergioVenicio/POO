from functools import reduce


class Item():
    def __new__(cls, _id: str, description: str, quantity: int, price: float):
        instance = super(Item, cls).__new__(cls)
        instance._id = _id
        instance.description = description
        instance._discount = 0

        if price <= 0:
            raise ValueError('Ivalid Price')

        instance.unit_price = price

        if quantity > 0:
            instance.quantity = quantity
        else:
            instance.quantity = 0

        return instance

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount: float):
        if discount < 1.0:
            self._discount = discount
        else:
            self._discount = 0

    @property
    def total(self):
        discount = self.unit_price * self.discount
        total = (self.unit_price * self.quantity) - discount
        return total


if __name__ == '__main__':
    milk = Item("Milk", "1 Gallon Milk", 2, 2.5)
    yogurt = Item("Yogurt", "Peach Yogurt", 4, 0.68)
    bread = Item("Bread", "Sliced Bread", 1, 2.55)
    soap = Item("Soap", "6 Pack Soap", 1, 4.51)

    milk.discount = 0.15

    prices = [
        milk.total,
        yogurt.total,
        bread.total,
        soap.total
    ]

    total = reduce(
        lambda sub_total, price: sub_total + price,
        prices
    )

    print("Thank You For Your Purchase.")
    print("Please Come Again!")
    print(f"{milk.description} \t {milk.total}")
    print(f"{yogurt.description} \t {yogurt.total}")
    print(f"{bread.description} \t {bread.total}")
    print(f"{soap.description} \t {soap.total}")
    print(f"Total Price \t ${total}")
