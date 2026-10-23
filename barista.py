class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self,receipt):
        self.receipt = receipt

    def add_item(self,item):
        self.receipt.append(item)

    def calculate_taxes(self):
        total = 0
        for item in self.receipt:
            total += item.price
        total = total * 7/100
        return total

    def calculate_total(self):
        total = 0
        for item in self.receipt:
            total += item.price
        tax = total * 7/100
        return total + tax

    def print_receipt(self):
        print("CROSSROAD'S CAFE\n----------------")
        for i in self.receipt:
            print(str(i.name) + " : " + str(i.price))
        print(f"----------------\ntaxes: {self.calculate_taxes()}\n----------------\nTotal: {self.calculate_total()}")

menu = [
    MenuItem("bagel", 3.00),
    MenuItem("burrito", 5.00),
    MenuItem("ramen", 1.50),
    MenuItem("gum", 0.50)
]
    
order1 = Order([])
order1.add_item(menu[1])
order1.add_item(menu[1])
order1.add_item(menu[3])

total = order1.calculate_total()
print("The total due is " + str(total))

order1.print_receipt()