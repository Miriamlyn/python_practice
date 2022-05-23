#nesting(a list of dictionary, a dictionary inside a dictionary or a list of items inside a dictionary)
aliens_0 = {'color': 'blue', 'speed': 'medium', 'points': 5}
aliens_1 = {'color': 'orange', 'speed': 'fast', 'points': 10}

aliens = [aliens_0, aliens_1]

for alien in aliens:
    print(alien)

#using range() to create fleet of 20 aliens
#make an empty list for storing aliens

aliens_2 = []

#make 20 green aliens
for aliens in range(20):
    new_aliens = {'color': 'green', 'speed': 'medium', 'points': '10'}
    aliens_2.append(new_aliens)

#show the first five aliens
for alien in aliens_2[:5]:
    print(alien)
print('....')

#show how many aliens where created
print(f"Total number of aliens:{len(aliens_2)}")

# the for loop and the If statement can be used to modify each alien in the range of aliens


#a list in a dictionary
pizza = {
            'crust' : 'thick',
            'toppings': ['mushroom', 'cheese', 'beef'],
        }

print(f"You ordered a {pizza['crust']}-crust pizza " 
        "with the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)

favorite_languages = {
        'jane': ['c', 'python'],
        'sarah' : ['python'],
        'tiamiyu': ['java', 'ruby'],
        'tobi' : ['ruby', 'go']
        }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#a dictionary in a dictionary
users = {
        'oyelamit':{
            'first': 'tobi',
            'last' : 'oyelami',
            'location' :'ajah',
            },

        'chilakach' : {
            'first' : 'chimamaka',
            'last' : 'chilaka',
            'location' : 'palmgrove',
            },
        }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")