class Resturant: 
    """An attempt to model a resturant"""

    def __init__(self, resturant_name, cuisine_type):
        """Intializing attributes of a resturant"""
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        """Simulate a resturant's name and menu"""
        print(f"{self.resturant_name} serves only {self.cuisine_type}")

    def open_resturant(self):
        """Simulate an opening of a resturant"""
        print(f"{self.resturant_name} is now open")

    def customers_served(self):
        """Total numbers of customers served"""
        print(f"We served {self.number_served} customers")

    def set_number_served(self, number):
        """Give the value of the total customers served"""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """add increments to the number of customers served"""
        self.number_served += additional_customers


my_resturant = Resturant('The house', 'African dishes')
his_resturant = Resturant('Tobis', 'Intercontinental dishes')
her_resturant = Resturant('The place', 'Chinese dishes')

print(f"The name of my resturant is {my_resturant.resturant_name}")
print(f"our cuisine is {my_resturant.cuisine_type}")
my_resturant.describe_resturant()
my_resturant.open_resturant()

print(f"\nThe name of this resturant is {his_resturant.resturant_name}")
print(f"our cuisine is {his_resturant.cuisine_type}")
his_resturant.describe_resturant()
his_resturant.open_resturant()

print(f"\nThe name of this resturant is {her_resturant.resturant_name}")
print(f"our cuisine is {her_resturant.cuisine_type}")
her_resturant.describe_resturant()
her_resturant.open_resturant()

resturant = Resturant('trillo', 'jamaican')
print(f"\nThe name of this resturant is {resturant.resturant_name}")
resturant.describe_resturant()
resturant.open_resturant()
resturant.customers_served()

resturant.set_number_served(2)
resturant.customers_served()

resturant.increment_number_served(4)
resturant.customers_served()