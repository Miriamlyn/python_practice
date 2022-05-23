import math

#using range() function to create a list 
number = range(1,7)
num = list(range(1,7))
print(num)

odd_numbers = list(range(1,12,2))
print(odd_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)
print(math.sqrt(squares[1]))

square = [value**2 for value in range (1,10)]
print(square)

#slicing a list
males = ['tobi', 'jay', 'charles', 'tom']
print(males[0:2])

print(males[1:3])
print(males[:2])
print(males[2:])
print(males[-3:])