#return value
def formatted_names(first_name, last_name):
    """Return formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

footballer = formatted_names('lionel', 'messi')
print(footballer)

#returning a dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

athlete = build_person('Amaka', 'Tobi', age=26)
print(athlete)