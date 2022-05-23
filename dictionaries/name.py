#using variables in strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")
print('Hello, world!')
alien_war = {'colour': 'blue', 'points': '5'}
print(alien_war['colour'])

print(f"New point is; {alien_war['points']}")

#Accessing values in dictionaries
speedvalue = alien_war.get('speed' 'No speed assigned')
print(speedvalue)

#looping through key value pairs
favorite_languages = {
                'jane': 'C',
                'sarah': 'python',
                'tiamiyu': 'java',
                'tobi':'ruby'}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#looping through all the keys in a dictionary
#looping throug the keys is the default when looping through dictionary
for name in favorite_languages.keys():
    print(name.title())


favorite_languages = {
                'jane': 'C',
                'sarah' : 'python',
                'tiamiyu': 'java',
                'tobi' : 'ruby'}

friends = ['jane', 'tobi']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}')

#looping through all the values in a dictionary
favorite_languages = {
                'jane': 'C',
                'sarah' : 'python',
                'tiamiyu': 'java',
                'tobi' : 'ruby'}

print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())
#the above method using .values() might be repetitive so you can use set()
for language in set(favorite_languages.values()):
    print(language.title())

#set() looks like dictionaries but without the key-vaalue pair.  a collection in which each item must be unique

