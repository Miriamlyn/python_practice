import json

numbers = [2,4,6,8,10]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# saving user generated data

import json

username = input('What is your name? ')
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
print(f"We'll  remember you next time you come back,{username}!")