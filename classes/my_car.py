from car import Car

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_description_name())

my_new_car.odometer_reading = 24
my_new_car.read_odometer()

#you can import multiple classes, a module(syntax used is the modulename.classname eg car.Car())
#a module can also be imported into another module