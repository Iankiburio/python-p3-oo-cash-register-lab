#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, item, price, quantity=1):
        for _ in range(quantity):
            self.items.append(item)
        self.last_transaction = price * quantity
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if len(self.items) > 0:
            self.total -= self.last_transaction
            self.items.pop()
            self.last_transaction = 0
        else:
            self.total = 0

    def get_total(self):
        return self.total

    def get_items(self):
        return self.items

