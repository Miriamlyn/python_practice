import pizza

pizza.make_pizza(14, 'pepperoni', 'cheese', 'chicken')
pizza.make_pizza(15, 'mushroom', 'beef', 'sausage')

#if you want to use this means to import a whole module named module.py for eg, the whole function in the module is made available using the followin syntax module.function_name()
#importing specific functions
from pizza import make_pizza

make_pizza(14, 'pepperoni', 'cheese', 'chicken')
make_pizza(15, 'mushroom', 'beef', 'sausage')

#using As to give a function an alias
from pizza import make_pizza as mp 

#using As to give alias to a module
import pizza as p 
#importing all function in a module
from pizza import *