filename = 'files_exceptions/learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

# print(len(lines))
# sentences = " "
# for line in lines:
#     sentences += line
    # print(line)

# print(len(line)) 

def my_print(list):
    for line in list:
        print(line.rstrip())


my_print(lines)
print()
my_print(lines)
print()
my_print(lines)
print()

