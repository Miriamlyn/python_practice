prompt = "If you tell us who you are, we can personalize the messages you see. \nWhat is your first name? "

name = input(prompt)

print(f"Welcome {name}")

#using int() to accept numerical input


height = input('\nHow tall are you, in inches? ')
height = int(height)

if height >= 40:
    print("\n You're old enough to ride")
else:
    print("You'll be old enough to ride when you're a little older")

#modulor operator %: divides one number by another and returns the remainder

number = input("\nEnter a number and we'll tell you if it's even or odd ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is an even number")
else:
    print(f"\nThe number {number} is an odd number")
