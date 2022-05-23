

# List: Array
#adding and changing an item in a list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)

# accessing an item in a list
print(numbers[1])

print(numbers)

#adding and changing an item in a list

cars = ['honda', 'bmw', 'toyota', 'kia']
print(cars)

cars.append('buggatti')
print(cars)

#changing an item in a list
cars[0] = 'porsche'
print(cars)

#inserting an element into a list
cars.insert(0, 'benz')
print(cars)

#changing case of an item in a list

trees = ['guava', 'apple', 'orange', 'mango']
print(trees[0].title())

print(trees)

#removing an element from a list
bags = ['gucci', 'prada', 'valentino', 'lv', 'keith']
print(bags)

del bags[1]
print(bags)

#removing but not deleting an item from a list
old_bag = bags.pop()
print(bags)
print(old_bag)

fine_bag = bags.pop(2)

#using the sorted() function
colors = ['green', 'purple', 'orange', 'ash', 'grey']
print("Here is the original list:")
print(colors)

print("\nHere is the sorted list:")
print(sorted(colors))

#using the sort() function
tv_brands = ['samsung', 'lg', 'polystar', 'panasonic']
tv_brands.sort()
print("\nHere is the TV brands:")
print(tv_brands)

tv_brands.sort(reverse=True)
print("\nHere is the sorted TV brands:")
print(tv_brands)