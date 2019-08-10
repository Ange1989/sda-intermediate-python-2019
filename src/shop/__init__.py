import typing

from src.shop.customer import Customer
from src.shop.exceptions import ItemValueNotPositive
from src.shop.item import Item
from src.shop.order import Order


def notify_everyone(orders: typing.List[Order]):
    for order in orders:
        order.customer.notify()


def place_order(customer: Customer, *items: Item) -> Order:
    order = Order(customer)
    for item in items:
        try:
            order.add_item(item)
        except ItemValueNotPositive as error:
            # print("you must provide a positive quantity")
            print(error.message)
    return order


if __name__ == "__main__":
    bob = Customer("Bob")
    john = Customer("John")

    order_1 = Order(bob)
    order_2 = Order(john)

    notify_everyone([order_1, order_2])
