# a specialized version o a diff class
#below is the parent class
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

#modifying using a method()
manual_car.update_odometer(23_500)
manual_car.read_odometer()

manual_car.increment_odometer(100)
manual_car.read_odometer()

#child class. create an electric car class from a parent class
#super() is used to tell python to call the __init__ method from the parent class

class Electric_car(Car):
    """Aspects of a car specific to electric cars"""
    def __init__(self,make, model, year):
        super().__init__(model,make,year)

my_tesla = Electric_car('model s', 'tesla', '2019')
print(my_tesla.get_description_name())

#defing attributes and methods for a child class
class Electric_car2(Car):
    """
    Initialize aspects of the parent class
    and then initialize aspects of a car specific to electric cars
    """
    def __init__(self,make, model, year):
        super().__init__(model,make,year)
        self.battery = 86
    
    def car_battery(self):
        """print a description of the car battery"""
        print(f"The car has a {self.battery}-Kwh battery")

my_tesla = Electric_car2('model s', 'tesla', '2019')
print(my_tesla.get_description_name())
my_tesla.car_battery()

#instances as attributes
#break class into smaller classes that work together
class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """intialize battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a description of the car battery"""
        print(f"This car has a {self.battery_size}-kwh battery")

    def get_range(self):
        """Print a statement of the range an electric car can go based on the battery"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on full charge")

class Electric_car3(Car):
    """
    Initialize aspects of the parent class
    and then initialize aspects of a car specific to electric cars
    """
    def __init__(self,make, model, year):
        super().__init__(model,make,year)
        self.battery = Battery()
    

my_tesla = Electric_car3('model s', 'tesla', '2019')
print(my_tesla.get_description_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#importing classes
