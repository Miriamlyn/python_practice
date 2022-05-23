#a class that can be used to represent a car

class Car:
    """A simple attempt to represent a car"""
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        """A neatly formatted description of a car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
        
    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer reading")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

manual_car = Car('Rio', 'Kia', '2018')
print(manual_car.get_description_name())
manual_car.read_odometer()

#modifying a value directly
manual_car.odometer_reading = 230
manual_car.read_odometer()