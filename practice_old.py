places = ['ghana', 'canada', 'jamaica', 'portugal', 'capetown']
print(places)

print(sorted(places))
print(places)

places.reverse()
print(places)

#length of a list
cars = ['kia', 'honda', 'audi', 'bmw', 'volvo']
# len(cars)
print(len(cars))
print(cars)
print(cars[-1])

name = "tobi/"
print(name.rstrip("/"))

clothes = ['trousers', 'gowns', 'shorts', 'blouse']
print(clothes)
clothes.remove('gowns')
print(clothes)

#for loop
laptops = ['samsung', 'macbook', 'lenovo', 'dell']
for laptop in laptops:
    print(laptop)

fruits = ['mango', 'pineapple', 'apple', 'guava']
for fruit in fruits:
    print(fruit.title() + ", is sweet")
    print("I can't wait to eat, " + fruit.title() +" .\n")

for value in range(1,5):
    print(value)