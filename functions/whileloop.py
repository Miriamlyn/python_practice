

#using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return fully formatted name of a person"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name.")
    print("(Please enter q anytime to quit)")

    f_name = input("First name  ")
    if f_name == 'q':
        break
    l_name = input("Last name  ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

def city_country(city_name, country_name):
    """Return full city and country name full formatted"""
    place = f"{city_name} {country_name}"
    return place.title()

visited_place = city_country('lagos', 'nigeria')
print(visited_place)

def make_album(artist, album_title, song_number=None):
    """Return full details about an album"""
    full_album = {'name': artist, 'song': album_title}
    if song_number:
        full_album['song_number'] = song_number
    return full_album

album = make_album('Ckay', 'love_laughter', song_number=4)
print(album)

