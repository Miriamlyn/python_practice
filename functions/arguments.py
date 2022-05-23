#positional arguments(order matters in positional arguments)
def describe_pet(animal_type, pet_name):
    """Display a description of a pet"""
    print(f"\nI have a {animal_type.title()} named {pet_name.title()}")

describe_pet("dog", "malcom")

#keyword arguments directly tells which arguments belong to a parameter
describe_pet(animal_type='dog', pet_name= 'malcom' )
#default arguments

def describe_pet2( pet_name, animal_type= 'dog'):
    """Display a description of a pet"""
    print(f"\nI have a {animal_type.title()} named {pet_name}")
describe_pet2(pet_name='timi')



#making an argument optional
def formatted_names2(first_name, middle_name, last_name):
    """Return fullname, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}" 
    return full_name.title()
   
dancer = formatted_names2('jolene', 'maureen', 'solomon')
print(dancer)

def get_formattednames(first_name, last_name, middle_name=""):
    """Return fullname, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formattednames('tina', 'okonkwo')
print(musician)

musician = get_formattednames('tina', 'rita', 'okonkwo')
print(musician)