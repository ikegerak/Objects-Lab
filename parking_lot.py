class Car:
    def __init__(self, make, model, mpg):
        self.make = make
        self.model = model
        self.mpg = mpg

def main():
    car1 = Car("Toyota", "Prius", 35)
    car2 = Car("Subaru","Outback", 32)
    car3 = Car("Ford", "F150", 25)
    totalmpg = 0
    parking_lot = [car1, car2, car3]

    for car in parking_lot:
        totalmpg += car.mpg
        
    print(totalmpg)

main()
