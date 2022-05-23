#storing your functions in modules
#import statement tells python to make a code in a module available in the current running file


def make_pizza(size, *toppings):
    """Details of making a pizza"""
    print(f"\nmaking a {size}-inch pizza with the below toppings:")
    for topping in toppings:
        print(f"- {topping}")