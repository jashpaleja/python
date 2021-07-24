class Bill(object):

    def _init_(self, items, price):
        self.amt = 0
        self.items = items
        self.price = price

        for i in price:
            self.amt += i

    def display(self):
        print("Items\tPrice")
        for i in range(0, len(self.items)):
            print(self.items[i] + "\t" + str(self.price[i]))


class Cash(Bill):
    def _init_(self, items, price, denom, val):
        Bill._init_(self, items, price)
        self.denom = denom
        self.val = val

    def display(self):
        Bill.display(self)
        print("Paid in denominations of " + str(self.denom) + " Having Price : " + str(self.denom * self.val))


class Cheaque(Bill):
    def _init_(self, items, price, cno):
        Bill._init_(self, items, price)
        self.cno = cno

    def display(self):
        Bill.display(self)
        print("Cheaque Number : " + str(self.cno))


items = ['fries', 'banana', 'pasta']
value = [100, 150, 200]

payment1 = Cash()
payment2 = Cheaque()
payment1._init_(items, value, 500, 1)
payment2._init_(items, value, 12541254)
payment1.display()
payment2.display()