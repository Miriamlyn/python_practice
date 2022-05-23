filename = 'files_exceptions/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")

with open(filename, 'a') as file_object:
    file_object.write('I love craeting new games.\n')
    file_object.write('I love challenges.\n')

    