#using a while loop with list and dictionaries
unconfirmed_users = ['toni', 'tobi', 'gina']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Veryfing Users: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#remove all instances of a value from a list
pets = ['cat', 'dog', 'rabbit']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#filling a dictionary with user inputs
responses = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name?. ")
    response = input("What mountain would you like to climb someday?. ")
    
    responses[name] = response

    repeat = input("Would you like anyone else to take the poll?. (yes/no). ")
    if repeat == 'no':
        polling_active = False

print("\n....Polling results...")
for name, response in responses.items():
    print(f"{name} would like to climb mount {response}.")
