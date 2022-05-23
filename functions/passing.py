
#passing a list
def print_models(undefined_designs, completed_models):
    #to pass the above function while avoiding modification of the initial file of undefined design, code can be written as print_models(undefined_designs[:], compledted_models)
    """Simulate printing designs, until none are left
    move each design to completed models after printing"""
    while undefined_designs:
       current_design = undefined_designs.pop()
       print(f"\nPrinting models: {current_design}")
       completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show models that has been printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

undefined_designs = ['robocop', 'zeus', 'pendant']
completed_models = []

print_models(undefined_designs, completed_models)
show_completed_models(completed_models)

#passing arbitrary arguments
def make_sandwich(*fillings):
    """Details of fillings for a sandwich"""
    print("\nmaking sandwich with the following fillings:")
    for filling in fillings:
        print(f"- {filling}")

make_sandwich('butter', 'eggs', 'lettuce', 'cabbage', 'carrots')
make_sandwich('jam', 'nuttella', 'chocolate')

#mixing arbitrary and positional arguments
#the function that the takes an arbitrary number of arguments must be placed last.
def make_pizza(size, *toppings):
    """Details of making a pizza"""
    print(f"\nmaking a {size}-inch pizza with the below toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(14, 'pepperoni', 'cheese', 'chicken')
make_pizza(15, 'mushroom', 'beef', 'sausage')


#using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Profile of a user"""
    user_info['First_name']= first
    user_info['Last_name']= last
    return user_info

user_profile= build_profile('amaka' ,'chilaka', 
                            location='lekki', field= 'banking')

print(user_profile)